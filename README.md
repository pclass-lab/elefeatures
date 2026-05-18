# MCCE Electrostatic Features

This project is to extract electrostatic features from a protein structure. Proposed stages are:

- Stage 1. Extract proposed electrostatic features an MCCE working directory.
- Stage 2. Extract electrostatic features from a pdb file directly from MCCE-ML module.
- Stage 3. Integrate electrostatic feature to PClass classifier

The proposed electrostatic features are:

**Core Composition (5)**
- net_charge
- isoelectric_point
- acid_fraction_all_residues
- base_fraction_all_residues
- acid_to_base_ratio

**pKa perturbation (6)**
- acid_big_pka_shift_fraction_all_residues
- base_big_pka_shift_fraction_all_residues
- acid_big_pka_shift_fraction_acids_only
- base_big_pka_shift_fraction_bases_only
- mean_abs_pka_shift
- max_abs_pka_shift

**Surface charge (4)**
- surface_net_charge
- surface_acid_to_base_ratio
- surface_positive_charge_density
- surface_negative_charge_density

**Patch localization (6)**
- largest_positive_patch_area
- largest_negative_patch_area
- largest_positive_patch_charge
- largest_negative_patch_charge
- largest_positive_patch_density
- largest_negative_patch_density

**Charge Assymetry (4)**
- all_charge_dipole_magnitude
- surface_charge_dipole_magnitude
- all_charge_dipole_normalized
- surface_charge_dipole_normalized

## Quick Start

### Installation
1. Clone the repository
```
git clone https://github.com/pclass-lab/elefeatures.git
```

2. Install in Editable (Development) Mode
Editable installs allow you to modify the code and immediately test changes.

```
pip install -e .
```
After this, the CLI entry point will be available:

```
mcce-features
```

To extract features from an MCCE folder
```
mcce-features extract <folder_name>
```