"""
Implementation of core functionalities for the mcce-features package.
"""
import csv
import logging
from pathlib import Path
from re import split as re_split

from rich.traceback import install

from .features import MCCEFeatureExtractor


# Configure rich to render tracebacks for cleaner CLI output without modifying click globals
install(show_locals=False)


BOOK_HEADER_LINES = 3
BOOK_FOOTER_LINES = 5


def extract(mcce_folder: str,
            verbose: bool = True):
    """Extract electrostatic features from MCCE output files in the specified folder."""
    logging.info(f"Starting feature extraction from MCCE folder: {mcce_folder}")
    extractor = MCCEFeatureExtractor()
    features = extractor.extract_all_features(folder=mcce_folder)
    feature_names = extractor.feature_names
    if verbose:
        for name, feature in zip(feature_names, features):
            print(f"{name}: {feature}")

    return feature_names, features


def get_book_data_bounds(book_fp: Path) -> tuple:
    """Return the start and end indices of the body in
    a book.txt file for slicing lines.
    Usage:
        l1, l2 = get_book_data_bounds(book_fp)
        if l1 is not None:
            lines = book_fp.read_text().splitlines()[l1:l2]
        else:
            lines = book_fp.read_text().splitlines()
    
    Retruns a valued 2-tuple if the book has 2 separator lines 
    for the header and footer as in pro_batch book.txt, else
    the tuple values are both None.
    """
    sep_line = "--------------------------------------"
    txt = book_fp.read_text()
    if txt.count(sep_line) == 2:
        # book from pro_batch has header/footer delineated by sep_line
        return BOOK_HEADER_LINES, -BOOK_FOOTER_LINES
    return None, None


def extract_folders(
    folder_file: str,
    output_file: str = "mcce_elefeatures.tsv",
):
    """
    Extract electrostatic features from multiple MCCE folders.

    Input:
        folder_file:
            Text file with one MCCE folder path per line, or a
            (space, comma, tab) delimited file with the folder 
            name in the first column.

    Output:
        TSV file with columns:
            mcce_folder, feature_1, feature_2, ...
    """
    folders_fp = Path(folder_file)
    is_book = folders_fp.name == "book.txt"
    other_book = False
    if is_book:
        l1, l2 = get_book_data_bounds(folders_fp)
        if l1 is None:  # book not from pro_batch
            other_book = True

    if not is_book or other_book:
        folder_paths = [
            re_split(r"[ ,\t]+", line)[0]
            for line in folders_fp.read_text().splitlines()
            if line.strip() and not line.strip().startswith("#")
        ]       
    else:
        folder_paths = [
            re_split(r"[ ,\t]+", line)[0]
            for line in folders_fp.read_text().splitlines()[l1:l2]
            if line.strip() and not line.strip().startswith("#")
        ]

    if not folder_paths:
        raise ValueError(f"No folders found in {folder_file}")

    logging.info(f"Found {len(folder_paths)} MCCE folders to process")

    header_written = False

    with open(output_file, "w", newline="") as fout:
        writer = None

        for i, mcce_folder in enumerate(folder_paths, start=1):
            logging.info(f"[{i:,}/{len(folder_paths):,}] Processing {mcce_folder}")

            try:
                feature_names, features = extract(mcce_folder, verbose=False)

                if not header_written:
                    writer = csv.writer(fout, delimiter="\t")
                    writer.writerow(["mcce_folder"] + list(feature_names))
                    header_written = True

                writer.writerow([mcce_folder] + list(features))

            except Exception as exc:
                logging.exception(f"Failed to process {mcce_folder}: {exc}")
                continue

    logging.info(f"Wrote feature table to {output_file}")
