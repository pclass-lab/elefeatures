# History

All notable changes to this project will be documented in this file.

The format is loosely based on Keep a Changelog
and this project adheres to Semantic Versioning.

---

## [0.6.1] - 2026-06-18

### Added

- Expanded the feature set to 83 electrostatic descriptors.
- Added residue-specific acid/base composition features for GLU, ASP, LYS, and ARG.
- Added residue-specific pKa perturbation features for GLU, ASP, LYS, and ARG.
- Added pH-specific surface charge features at pH 6.0, 7.0, and 8.0.
- Added pH-specific buried charge features at pH 6.0, 7.0, and 8.0.
- Added pH-specific charge patch features at pH 6.0, 7.0, and 8.0.
- Added pH-specific charge asymmetry and separation features at pH 6.0, 7.0, and 8.0.
- Added nearest charged-residue distance features based on residue anchor points.
- Added optional custom numeric features from `mcce-features.txt` files.

### Changed

- Updated charge-derived feature names to include their pH suffixes.
- Updated README feature documentation with feature categories and counts.
- Updated batch output to include optional custom feature columns across folders.
- Preserved pH 7.0 fallback behavior for callers that provide residue charges directly.
- Standardized no-base acid-to-base ratio handling to use `999.0`.

### Fixed

- Corrected `pk0` naming to `pka0`.
- Corrected Lys/Arg pKa-shift feature labels to use `bases_only`.
- Added the `python -m mcce_features.cli` entry-point block.
- Prevent output file creation when no features are extracted.

## [0.5.0] - 2026-05-18

### Added

- Initial public release of the MCCE electrostatic feature extraction framework
- Feature extraction pipeline for protein electrostatic descriptors
- Support for extracting features directly from MCCE output folders
- Batch extraction from multiple folders using `extract-folders`

### Electrostatic Features

Added support for extracting:

#### Core Composition (5)
- net_charge
- isoelectric_point
- acid_fraction_all_residues
- base_fraction_all_residues
- acid_to_base_ratio

#### pKa perturbation (6)
- acid_big_pka_shift_fraction_all_residues
- base_big_pka_shift_fraction_all_residues
- acid_big_pka_shift_fraction_acids_only
- base_big_pka_shift_fraction_bases_only
- mean_abs_pka_shift
- max_abs_pka_shift

#### Surface charge (4)
- surface_net_charge
- surface_acid_to_base_ratio
- surface_positive_charge_density
- surface_negative_charge_density

#### Patch localization (6)
- largest_positive_patch_area
- largest_negative_patch_area
- largest_positive_patch_charge
- largest_negative_patch_charge
- largest_positive_patch_density
- largest_negative_patch_density

#### Charge Asymmetry (5)
- all_charge_spatial_moment_magnitude
- surface_charge_spatial_moment_magnitude
- all_charge_spatial_moment_normalized
- surface_charge_spatial_moment_normalized
- charge_separation_magnitude

### Internal Improvements

- Added automatic consistency checking between feature names and feature vectors
- Refactored feature extraction to use dictionary-based feature aggregation
- Added connected-component patch detection algorithm
- Added robust handling for missing residue properties
- Added guardrails against division-by-zero and empty datasets
- Improved logging and error reporting

### CLI

- Added `extract` command for single-folder extraction
- Added `extract-folders` command for batch processing

### Notes

- This release is intended as an experimental research framework
  for electrostatic feature engineering and protein function analysis.
- Feature definitions and normalization schemes may evolve in future releases.
- Patch detection thresholds and electrostatic normalization parameters
  are experimental and adjustable

---

## [0.3.x]

### Prototype Stage

- Early concept validation
- Initial feature exploration for protein function classification
- Preliminary physicochemical descriptor experiments
