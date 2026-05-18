"""
Implementation of core functionalities for the mcce-features package.
"""

import logging
from .features import MCCEFeatureExtractor


# Configure rich to render tracebacks for cleaner CLI output without modifying click globals
from rich.traceback import install
install(show_locals=False)

def extract(mcce_folder: str):
    """Extract electrostatic features from MCCE output files in the specified folder."""
    logging.info(f"Starting feature extraction from MCCE folder: {mcce_folder}")
    extractor = MCCEFeatureExtractor()
    features = extractor.extract_all_features(folder=mcce_folder)
    feature_names = extractor.feature_names
    for name, feature in zip(feature_names, features):
        print(f"{name}: {feature}")

    logging.info(f"Extracted {len(features)} features from MCCE output.")

    return feature_names, features