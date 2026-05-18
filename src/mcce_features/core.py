"""
Implementation of core functionalities for the mcce-features package.
"""

import logging
from pathlib import Path
import csv

from .features import MCCEFeatureExtractor


# Configure rich to render tracebacks for cleaner CLI output without modifying click globals
from rich.traceback import install
install(show_locals=False)

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


def extract_folders(
    folder_file: str,
    output_file: str = "mcce_elefeatures.tsv",
):
    """
    Extract electrostatic features from multiple MCCE folders.

    Input:
        folder_file:
            Text file with one MCCE folder path per line.

    Output:
        TSV file with columns:
            mcce_folder, feature_1, feature_2, ...
    """

    folder_paths = [
        line.strip()
        for line in Path(folder_file).read_text().splitlines()
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