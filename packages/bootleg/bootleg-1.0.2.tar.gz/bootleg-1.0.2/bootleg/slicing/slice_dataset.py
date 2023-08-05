import hashlib
import logging
import multiprocessing
import os
import shutil
import time
import traceback
from collections import defaultdict

import numpy as np
import ujson
from tqdm import tqdm

from bootleg import log_rank_0_debug, log_rank_0_info
from bootleg.symbols.constants import ANCHOR_KEY, FINAL_LOSS
from bootleg.utils import data_utils, utils

logger = logging.getLogger(__name__)


class InputExample(object):
    """A single training/test example."""

    def __init__(self, sent_idx, subslice_idx, anchor, num_alias2pred, slices):
        self.sent_idx = sent_idx
        self.subslice_idx = subslice_idx
        self.anchor = anchor
        self.num_alias2pred = num_alias2pred
        self.slices = slices

    def to_dict(self):
        return {
            "sent_idx": self.sent_idx,
            "subslice_idx": self.subslice_idx,
            "anchor": self.anchor,
            "num_alias2pred": self.num_alias2pred,
            "slices": self.slices,
        }

    @classmethod
    def from_dict(cls, in_dict):
        return cls(
            in_dict["sent_idx"],
            in_dict["subslice_idx"],
            in_dict["anchor"],
            in_dict["num_alias2pred"],
            in_dict["slices"],
        )

    def __repr__(self):
        return (
            f"Sent: {self.sent_idx} Subsent: {self.subslice_idx} Anchors: {self.anchor} "
            f"Num Alias2Pred: {self.num_alias2pred} Slices: {self.slices}"
        )


class InputFeatures(object):
    """A single set of features of data."""

    def __init__(self, sent_idx, subslice_idx, alias_slice_incidence, alias2pred_probs):
        self.sent_idx = sent_idx
        self.subslice_idx = subslice_idx
        self.alias_slice_incidence = alias_slice_incidence
        self.alias2pred_probs = alias2pred_probs

    def to_dict(self):
        return {
            "sent_idx": self.sent_idx,
            "subslice_idx": self.subslice_idx,
            "alias_slice_incidence": self.alias_slice_incidence,
            "alias2pred_probs": self.alias2pred_probs,
        }

    @classmethod
    def from_dict(cls, in_dict):
        return cls(
            in_dict["sent_idx"],
            in_dict["subslice_idx"],
            in_dict["alias_slice_incidence"],
            in_dict["alias2pred_probs"],
        )


def get_slice_values(slice_names, line):
    """Results a dictionary of all slice values for an input example. Any
    mention with a slice value of > 0.5 gets assigned that slice. If some
    slices are missing from the input, we assign all mentions as not being in
    that slice (getting a 0 label value). We also check that slices are
    formatted correctly.

    Args:
        slice_names: slice names to evaluate on
        line: input data json line

    Returns: Dict of slice name to alias index string to float value of if mention is in a slice or not.
    """
    slices = {}
    if "slices" in line:
        assert type(line["slices"]) is dict
        aliases = line["aliases"]
        slices = line["slices"]
        # remove slices that we don't need
        for slice_name in list(slices.keys()):
            if slice_name not in slice_names:
                del slices[slice_name]
            else:
                assert len(slices[slice_name]) == len(
                    aliases
                ), "Must have a prob label for each mention"
        # FINAL_LOSS and BASE_SLICE are in slice_names but are generated by us so we do not want them to be in slices
        assert (
            FINAL_LOSS not in slices
        ), f"You can't have {FINAL_LOSS} be slice names. You have {slices.keys()}. {FINAL_LOSS} is used internally."
        for slice_name in slice_names:
            if slice_name in [FINAL_LOSS]:
                continue
            # Add slices that are empty
            if slice_name not in slices:
                slices[slice_name] = {str(i): 0.0 for i in range(len(aliases))}
    return slices


def create_examples_initializer(
    data_config, slice_names, use_weak_label, max_aliases, split, train_in_candidates
):
    global constants_global
    constants_global = {
        "slice_names": slice_names,
        "use_weak_label": use_weak_label,
        "max_aliases": max_aliases,
        "split": split,
        "train_in_candidates": train_in_candidates,
    }


def create_examples(
    dataset,
    create_ex_indir,
    create_ex_outdir,
    meta_file,
    data_config,
    dataset_threads,
    slice_names,
    use_weak_label,
    split,
):
    """Creates examples from the raw input data.

    Args:
        dataset: dataset file
        create_ex_indir: temporary directory where input files are stored
        create_ex_outdir: temporary directory to store output files from method
        meta_file: metadata file to save the file names/paths for the next step in prep pipeline
        data_config: data config
        dataset_threads: number of threads
        slice_names: list of slices to evaluate on
        use_weak_label: whether to use weak labeling or not
        split: data split

    Returns:
    """
    log_rank_0_debug(logger, "Starting to extract subsentences")
    start = time.time()
    num_processes = min(dataset_threads, int(0.8 * multiprocessing.cpu_count()))

    log_rank_0_debug(logger, f"Counting lines")
    total_input = sum(1 for _ in open(dataset))
    if num_processes == 1:
        out_file_name = os.path.join(create_ex_outdir, os.path.basename(dataset))
        constants_dict = {
            "slice_names": slice_names,
            "use_weak_label": use_weak_label,
            "max_aliases": data_config.max_aliases,
            "split": split,
            "train_in_candidates": data_config.train_in_candidates,
        }
        files_and_counts = {}
        res = create_examples_single(
            dataset, total_input, out_file_name, constants_dict
        )
        total_output = res["total_lines"]
        max_alias2pred = res["max_alias2pred"]
        files_and_counts[res["output_filename"]] = res["total_lines"]
    else:
        log_rank_0_info(
            logger, f"Strating to extract examples with {num_processes} threads"
        )
        log_rank_0_debug(
            logger, "Parallelizing with " + str(num_processes) + " threads."
        )
        chunk_input = int(np.ceil(total_input / num_processes))
        log_rank_0_debug(
            logger,
            f"Chunking up {total_input} lines into subfiles of size {chunk_input} lines",
        )
        total_input_from_chunks, input_files_dict = utils.chunk_file(
            dataset, create_ex_indir, chunk_input
        )

        input_files = list(input_files_dict.keys())
        input_file_lines = [input_files_dict[k] for k in input_files]
        output_files = [
            in_file_name.replace(create_ex_indir, create_ex_outdir)
            for in_file_name in input_files
        ]
        assert (
            total_input == total_input_from_chunks
        ), f"Lengths of files {total_input} doesn't mathc {total_input_from_chunks}"
        log_rank_0_debug(logger, f"Done chunking files")

        pool = multiprocessing.Pool(
            processes=num_processes,
            initializer=create_examples_initializer,
            initargs=[
                data_config,
                slice_names,
                use_weak_label,
                data_config.max_aliases,
                split,
                data_config.train_in_candidates,
            ],
        )
        total_output = 0
        max_alias2pred = 0
        input_args = list(zip(input_files, input_file_lines, output_files))
        # Store output files and counts for saving in next step
        files_and_counts = {}
        for res in pool.imap_unordered(create_examples_hlp, input_args, chunksize=1):
            total_output += res["total_lines"]
            max_alias2pred = max(max_alias2pred, res["max_alias2pred"])
            files_and_counts[res["output_filename"]] = res["total_lines"]
        pool.close()
    utils.dump_json_file(
        meta_file,
        {
            "num_mentions": total_output,
            "files_and_counts": files_and_counts,
            "max_alias2pred": max_alias2pred,
        },
    )
    log_rank_0_debug(
        logger,
        f"Done with extracting examples in {time.time()-start}. Total lines seen {total_input}. "
        f"Total lines kept {total_output}.",
    )
    return


def create_examples_hlp(args):
    in_file_name, in_file_lines, out_file_name = args
    return create_examples_single(
        in_file_name, in_file_lines, out_file_name, constants_global
    )


def create_examples_single(in_file_name, in_file_lines, out_file_name, constants_dict):
    """Create examples multiprocessing helper."""
    split = constants_dict["split"]
    use_weak_label = constants_dict["use_weak_label"]
    slice_names = constants_dict["slice_names"]
    with open(out_file_name, "w") as out_f:
        total_subsents = 0
        # The memmap stores things differently when you have two integers and we want to keep a2p as an array
        # Therefore for force max the minimum max_a2p to be 2
        max_a2pred = 2
        for ex in tqdm(
            open(in_file_name), total=in_file_lines, desc=f"Reading in {in_file_name}"
        ):
            line = ujson.loads(ex)
            assert "sent_idx_unq" in line
            assert "aliases" in line
            assert ANCHOR_KEY in line
            sent_idx = line["sent_idx_unq"]
            # aliases are assumed to be lower-cased in candidate map
            aliases = [alias.lower() for alias in line["aliases"]]
            num_alias2pred = len(aliases)
            slices = get_slice_values(slice_names, line)
            # We need to only use True anchors for eval
            anchor = [True for i in range(len(aliases))]
            if ANCHOR_KEY in line:
                anchor = line[ANCHOR_KEY]
                assert len(aliases) == len(anchor)
                assert all(isinstance(a, bool) for a in anchor)
                if split != "train":
                    # Reindex aliases to predict to be where anchor == True because we only ever want to predict
                    # those (it will see all aliases in the forward pass but we will only score the True anchors)
                    for slice_name in slices:
                        aliases_to_predict = slices[slice_name]
                        slices[slice_name] = {
                            i: aliases_to_predict[i]
                            for i in aliases_to_predict
                            if anchor[int(i)] is True
                        }

            # Add in FINAL LOSS slice
            if split != "train":
                slices[FINAL_LOSS] = {
                    str(i): 1.0 for i in range(len(aliases)) if anchor[i] is True
                }
            else:
                slices[FINAL_LOSS] = {str(i): 1.0 for i in range(len(aliases))}

            # If not use_weak_label, only the anchor is True aliases will be given to the model
            # We must re-index alias to predict to be in terms of anchors == True
            # Ex: anchors = [F, T, T, F, F, T]
            #     If dataset_is_eval, let
            #     a2p = [2,5]     (a2p must only be for T anchors)
            #     AFTER NOT USE_WEAK_LABEL, DATA WILL BE ONLY THE TRUE ANCHORS
            #     a2p needs to be [1, 2] for the 3rd and 6th true become the 2nd and 3rd after not weak labelling
            #     If dataset_is_eval is False, let
            #     a2p = [0,2,4,5]     (a2p can be anything)
            if not use_weak_label:
                assert (
                    ANCHOR_KEY in line
                ), "Cannot toggle off data weak labelling without anchor info"
                # The number of aliases will be reduced to the number of true anchors
                num_alias2pred = sum(anchor)
                # We must correct this mapping because the indexing will change when we remove False anchors (see
                # comment example above)
                slices = data_utils.correct_not_augmented_dict_values(anchor, slices)
            # print("ANCHOR", anchor, "LINE", line, "SLICeS", slices)
            # Remove slices that have no aliases to predict
            for slice_name in list(slices.keys()):
                if len(slices[slice_name]) <= 0:
                    del slices[slice_name]

            all_false_anchors = all([anc is False for anc in anchor])
            # For nicer code downstream, we make sure FINAL_LOSS is in here
            # Only cases where it won't be is if use_weak_labels is True and the split is train
            # (then we may have all false anchors)
            if FINAL_LOSS not in slices:
                assert (
                    all_false_anchors
                ), f"If {FINAL_LOSS} isn't in slice, it must be that all anchors are False. This is not true"
                assert (
                    split != "train" or not use_weak_label
                ), f"As all anchors are false, this must happen if you are evaling or training and using weak labels"
            # TODO: optimizer here
            # for i in range(0, num_alias2pred, max_aliases):
            #     subset_slices = {}
            #     for slice_name in list(slices.keys()):
            #         subset_slices[slice_name] = dict(str(j):slice[slice_name][str(j)] for
            #                                                       j in range(i:i+max_aliases))
            #     ex = InputExample(
            #         sent_idx=sent_idx,
            #         subslice_idx=i,
            #         anchor=anchor,
            #         num_alias2pred=num_alias2pred,
            #         slices=slices)
            #     examples.append(ex)
            subslice_idx = 0
            total_subsents += 1
            max_a2pred = max(max_a2pred, num_alias2pred)
            out_f.write(
                ujson.dumps(
                    InputExample(
                        sent_idx=sent_idx,
                        subslice_idx=subslice_idx,
                        anchor=anchor,
                        num_alias2pred=num_alias2pred,
                        slices=slices,
                    ).to_dict()
                )
                + "\n"
            )
    return {
        "total_lines": total_subsents,
        "output_filename": out_file_name,
        "max_alias2pred": max_a2pred,
    }


def convert_examples_to_features_and_save_initializer(save_dataset_name, storage):
    global mmap_file_global
    mmap_file_global = np.memmap(save_dataset_name, dtype=storage, mode="r+")


def convert_examples_to_features_and_save(
    meta_file, dataset_threads, slice_names, save_dataset_name, storage
):
    """Converts the prepped examples into input features and saves in memmap
    files. These are used in the __get_item__ method.

    Args:
        meta_file: metadata file where input file paths are saved
        dataset_threads: number of threads
        slice_names: list of slice names to evaluation on
        save_dataset_name: data file name to save
        storage: data storage type (for memmap)

    Returns:
    """
    log_rank_0_debug(logger, "Starting to extract subsentences")
    start = time.time()
    num_processes = min(dataset_threads, int(0.8 * multiprocessing.cpu_count()))

    log_rank_0_info(
        logger, f"Starting to build and save features with {num_processes} threads"
    )

    log_rank_0_debug(logger, f"Counting lines")
    total_input = utils.load_json_file(meta_file)["num_mentions"]
    max_alias2pred = utils.load_json_file(meta_file)["max_alias2pred"]
    files_and_counts = utils.load_json_file(meta_file)["files_and_counts"]

    # IMPORTANT: for distributed writing to memmap files, you must create them in w+ mode before
    # being opened in r+ mode by workers
    memmap_file = np.memmap(
        save_dataset_name, dtype=storage, mode="w+", shape=(total_input,), order="C"
    )
    # Save -1 in sent_idx to check that things are loaded correctly later
    memmap_file[slice_names[0]]["sent_idx"][:] = -1

    input_args = []
    # Saves where in memap file to start writing
    offset = 0
    for i, in_file_name in enumerate(files_and_counts.keys()):
        input_args.append(
            {
                "file_name": in_file_name,
                "in_file_lines": files_and_counts[in_file_name],
                "save_file_offset": offset,
                "ex_print_mod": int(np.ceil(total_input / 20)),
                "slice_names": slice_names,
                "max_alias2pred": max_alias2pred,
            }
        )
        offset += files_and_counts[in_file_name]

    if num_processes == 1:
        assert len(input_args) == 1
        total_output = convert_examples_to_features_and_save_single(
            input_args[0], memmap_file
        )
    else:
        log_rank_0_debug(
            logger,
            "Initializing pool. This make take a few minutes.",
        )
        pool = multiprocessing.Pool(
            processes=num_processes,
            initializer=convert_examples_to_features_and_save_initializer,
            initargs=[save_dataset_name, storage],
        )

        total_output = 0
        for res in pool.imap_unordered(
            convert_examples_to_features_and_save_hlp, input_args, chunksize=1
        ):
            total_output += res
        pool.close()

    # Verify that sentences are unique and saved correctly
    mmap_file = np.memmap(save_dataset_name, dtype=storage, mode="r")
    all_uniq_ids = set()
    for i in tqdm(range(total_input), desc="Checking sentence uniqueness"):
        assert (
            mmap_file[slice_names[0]]["sent_idx"][i] != -1
        ), f"Index {i} has -1 sent idx"
        uniq_id = str(
            f"{mmap_file[slice_names[0]]['sent_idx'][i]}.{mmap_file[slice_names[0]]['subslice_idx'][i]}"
        )
        assert (
            uniq_id not in all_uniq_ids
        ), f"Idx {uniq_id} is not unique and already in data"
        all_uniq_ids.add(uniq_id)

    log_rank_0_debug(
        logger,
        f"Done with extracting examples in {time.time() - start}. Total lines seen {total_input}. "
        f"Total lines kept {total_output}",
    )
    return


def convert_examples_to_features_and_save_hlp(input_dict):
    return convert_examples_to_features_and_save_single(input_dict, mmap_file_global)


def convert_examples_to_features_and_save_single(input_dict, mmap_file):
    """Convert examples to features multiprocessing helper."""
    file_name = input_dict["file_name"]
    in_file_lines = input_dict["in_file_lines"]
    save_file_offset = input_dict["save_file_offset"]
    ex_print_mod = input_dict["ex_print_mod"]
    max_alias2pred = input_dict["max_alias2pred"]
    slice_names = input_dict["slice_names"]
    total_saved_features = 0
    for idx, in_line in tqdm(
        enumerate(open(file_name)), total=in_file_lines, desc=f"Processing {file_name}"
    ):
        example = InputExample.from_dict(ujson.loads(in_line))
        example_idx = save_file_offset + idx
        sent_idx = example.sent_idx
        subslice_idx = example.subslice_idx
        slices = example.slices

        row_data = {}
        for slice_name in slice_names:
            # We use the information in "slices" key to generate two pieces of info
            # 1. Binary info for if a mention is in the slice
            # 2. Probabilistic info for the prob the mention is in the slice, this is used to train indicator heads
            if slice_name in slices:
                # Set indices of aliases to predict relevant to slice to 1-hot vector
                slice_indexes = np.array([0] * (max_alias2pred))
                for idx in slices[slice_name]:
                    # We consider an example as "in the slice" if it's probability is greater than 0.5
                    slice_indexes[int(idx)] = slices[slice_name][idx] > 0.5
                alias_slice_incidence = slice_indexes
            else:
                # Set to zero for all aliases if no aliases in example occur in the slice
                alias_slice_incidence = np.array([0] * max_alias2pred)
            # Add probabilistic labels for training indicators
            if slice_name in slices:
                # padded values are -1 so they are masked in score function
                slices_padded = np.array([-1.0] * (max_alias2pred))
                for idx in slices[slice_name]:
                    # The indexes needed to be string for json
                    slices_padded[int(idx)] = slices[slice_name][idx]
                alias2pred_probs = slices_padded
            else:
                alias2pred_probs = np.array([-1] * max_alias2pred)

            total_saved_features += 1
            # Write slice indices into record array
            feature = InputFeatures(
                sent_idx=sent_idx,
                subslice_idx=subslice_idx,
                alias_slice_incidence=alias_slice_incidence,
                alias2pred_probs=alias2pred_probs,
            )
            # We are storing mmap file in column format, so column name first
            mmap_file[slice_name]["sent_idx"][example_idx] = feature.sent_idx
            mmap_file[slice_name]["subslice_idx"][example_idx] = feature.subslice_idx
            mmap_file[slice_name]["alias_slice_incidence"][
                example_idx
            ] = feature.alias_slice_incidence
            mmap_file[slice_name]["prob_labels"][example_idx] = feature.alias2pred_probs
        if example_idx % ex_print_mod == 0:
            for slice_name in row_data:
                # Make one string for distributed computation consistency
                output_str = ""
                output_str += f'*** Example Slice "{slice_name}" ***' + "\n"
                output_str += (
                    f"sent_idx:                         {example.sent_idx}" + "\n"
                )
                output_str += (
                    f"subslice_idx:                     {example.subslice_idx}" + "\n"
                )
                output_str += (
                    f"anchor:                           {example.anchor}" + "\n"
                )
                output_str += (
                    f"slices:                           {example.slices.get(slice_name, {})}"
                    + "\n"
                )  # Sometimes slices are emtpy if all anchors are false
                output_str += "*** Feature ***" + "\n"
                output_str += (
                    f"alias_slice_incidence:            {row_data[slice_name].alias_slice_incidence}"
                    + "\n"
                )
                output_str += (
                    f"alias2pred_probs:                 {row_data[slice_name].alias2pred_probs}"
                    + "\n"
                )
                print(output_str)
    mmap_file.flush()
    return total_saved_features


class BootlegSliceDataset:
    """Our dataset class for holding data slices (or subpopulations).

    Each mention can be part of 0 or more slices. When running eval, we use
    the SliceDataset to determine which mentions are part of what slices. Importantly, although the model
    "sees" all mentions, only GOLD anchor links are evaluated for eval (splits of test/dev).

    Args:
        main_args: main arguments
        dataset: dataset file
        use_weak_label: whether to use weak labeling or not
        entity_symbols: entity symbols
        dataset_threads: number of processes to use
        split: data split
    """

    def __init__(
        self,
        main_args,
        dataset,
        use_weak_label,
        entity_symbols,
        dataset_threads,
        split="train",
    ):
        global_start = time.time()
        log_rank_0_info(logger, f"Building slice dataset for {split} from {dataset}.")
        spawn_method = main_args.run_config.spawn_method
        data_config = main_args.data_config
        orig_spawn = multiprocessing.get_start_method()
        multiprocessing.set_start_method(spawn_method, force=True)
        self.slice_names = data_utils.get_eval_slices(data_config.eval_slices)
        self.get_slice_dt = lambda max_a2p: np.dtype(
            [
                ("sent_idx", int),
                ("subslice_idx", int),
                ("alias_slice_incidence", int, (max_a2p,)),
                ("prob_labels", float, (max_a2p,)),
            ]
        )
        self.get_storage = lambda max_a2p: np.dtype(
            [
                (slice_name, self.get_slice_dt(max_a2p))
                for slice_name in self.slice_names
            ]
        )
        # Folder for all mmap saved files
        save_dataset_folder = data_utils.get_save_data_folder(
            data_config, use_weak_label, dataset
        )
        utils.ensure_dir(save_dataset_folder)
        # Folder for temporary output files
        temp_output_folder = os.path.join(
            data_config.data_dir, data_config.data_prep_dir, f"prep_{split}_slice_files"
        )
        utils.ensure_dir(temp_output_folder)
        # Input step 1
        create_ex_indir = os.path.join(temp_output_folder, "create_examples_input")
        utils.ensure_dir(create_ex_indir)
        # Input step 2
        create_ex_outdir = os.path.join(temp_output_folder, "create_examples_output")
        utils.ensure_dir(create_ex_outdir)
        # Meta data saved files
        meta_file = os.path.join(temp_output_folder, "meta_data.json")
        # File for standard training data
        hash = hashlib.sha1(str(self.slice_names).encode("UTF-8")).hexdigest()[:10]
        self.save_dataset_name = os.path.join(
            save_dataset_folder, f"ned_slices_{hash}.bin"
        )
        self.save_data_config_name = os.path.join(
            save_dataset_folder, "ned_slices_config.json"
        )

        # =======================================================================================
        # SLICE DATA
        # =======================================================================================
        log_rank_0_debug(logger, "Loading dataset...")
        log_rank_0_debug(logger, f"Seeing if {self.save_dataset_name} exists")
        if data_config.overwrite_preprocessed_data or (
            not os.path.exists(self.save_dataset_name)
        ):
            st_time = time.time()
            try:
                log_rank_0_info(
                    logger,
                    f"Building dataset from scratch. Saving to {save_dataset_folder}",
                )
                create_examples(
                    dataset,
                    create_ex_indir,
                    create_ex_outdir,
                    meta_file,
                    data_config,
                    dataset_threads,
                    self.slice_names,
                    use_weak_label,
                    split,
                )
                max_alias2pred = utils.load_json_file(meta_file)["max_alias2pred"]
                convert_examples_to_features_and_save(
                    meta_file,
                    dataset_threads,
                    self.slice_names,
                    self.save_dataset_name,
                    self.get_storage(max_alias2pred),
                )
                utils.dump_json_file(
                    self.save_data_config_name, {"max_alias2pred": max_alias2pred}
                )

                log_rank_0_debug(
                    logger, f"Finished prepping data in {time.time() - st_time}"
                )
            except Exception as e:
                tb = traceback.TracebackException.from_exception(e)
                logger.error(e)
                logger.error("\n".join(tb.stack.format()))
                shutil.rmtree(save_dataset_folder, ignore_errors=True)
                raise

        log_rank_0_info(
            logger,
            f"Loading data from {self.save_dataset_name} and {self.save_data_config_name}",
        )
        max_alias2pred = utils.load_json_file(self.save_data_config_name)[
            "max_alias2pred"
        ]
        self.data, self.sent_to_row_id_dict = self.build_data_dict(
            self.save_dataset_name, self.get_storage(max_alias2pred)
        )
        assert len(self.data) > 0
        assert len(self.sent_to_row_id_dict) > 0
        log_rank_0_debug(logger, f"Removing temporary output files")
        shutil.rmtree(temp_output_folder, ignore_errors=True)
        # Set spawn back to original/default, which is "fork" or "spawn". This is needed for the Meta.config to
        # be correctly passed in the collate_fn.
        multiprocessing.set_start_method(orig_spawn, force=True)
        log_rank_0_info(
            logger,
            f"Final slice data initialization time from {split} is {time.time() - global_start}s",
        )

    @classmethod
    def build_data_dict(cls, save_dataset_name, storage):
        """Loads the memmap slice dataset and create a mapping from sentence
        index to row index.

        Args:
            save_dataset_name: saved memmap file name
            storage: storage type of memmap file

        Returns: numpy memmap data, Dict of sentence index to row in data
        """
        sent_to_row_id_dict = defaultdict(list)
        data = np.expand_dims(
            np.memmap(save_dataset_name, dtype=storage, mode="r").view(np.recarray),
            axis=1,
        )
        # Get any slice name for getting the sentence index
        slice_name = data[0].dtype.names[0]
        for i in tqdm(range(len(data)), desc="Building sent idx to row idx mapping"):
            sent_idx = data[i][slice_name]["sent_idx"][0]
            sent_to_row_id_dict[sent_idx].append(i)
        return data, dict(sent_to_row_id_dict)

    def contains_sentidx(self, sent_idx):
        """Return true if the sentence index is in the dataset.

        Args:
            sent_idx: sentence index

        Returns: bool whether in dataset or not
        """
        return sent_idx in self.sent_to_row_id_dict

    def get_slice_incidence_arr(self, sent_idx, alias_orig_list_pos):
        """Given the sentence index and the list of aliases to get slice
        indices for (may have -1 indicating no alias), return a dictionary of
        slice_name -> 0/1 incidence array of if each alias in
        alias_orig_list_pos was in the slice or not (-1 for no alias).

        Args:
            sent_idx: sentence index
            alias_orig_list_pos: list of alias positions in input data list
                                 (due to sentence splitting, aliases may be split up)

        Returns: Dict of slice name -> 0/1 incidence array
        """
        assert (
            sent_idx in self.sent_to_row_id_dict
        ), f"Sentence {sent_idx} not in {self.save_dataset_name}"
        alias_orig_list_pos = np.array(alias_orig_list_pos)
        row_ids = self.sent_to_row_id_dict[sent_idx]
        slices_to_return = {}
        for row_i in row_ids:
            for slice_name in self.slice_names:
                slices_to_return[slice_name] = self.data[row_i][slice_name][
                    "alias_slice_incidence"
                ][0][alias_orig_list_pos]
                slices_to_return[slice_name][alias_orig_list_pos == -1] = -1
        return slices_to_return
