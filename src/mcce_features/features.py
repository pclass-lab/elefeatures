"""
MCCE Feature Extractor
This module contains the core logic for extracting electrostatic features from MCCE output files.

"""
import numpy as np
from typing import Dict, List, Optional
from collections import Counter


class MCCEFeatureExtractor:
    """
    A feature extractor for MCCE output files.

    The method extract_all_features() returns a list of floats ordered by feature names
    """

    def __init__(self):
        self.mcce_folder = None
        # REGISTER ALL FEATURE NAMES HERE
        self.feature_names = [
            "total_residues",
        ]


    def extract_composition_features(self) -> Dict[str, float]:
        """
        Extract composition features from MCCE output files.

        Returns:
            A dictionary mapping feature names to their corresponding float values.
        """
        features = {}
        features["total_residues"] = 100  # Placeholder value
        return features

    def extract_all_features(self, folder: Optional[str] = None) -> List[float]:
        """
        Extract all electrostatic features from the MCCE output files in the specified folder.

        Returns:
            A list of floats representing the extracted features, ordered by feature names.
        """
        if folder is not None:
            self.mcce_folder = folder

        self.features = {}
        self.features.update(self.extract_composition_features())
        return list(self.features.values())