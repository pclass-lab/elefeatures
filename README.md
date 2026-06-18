# MCCE Electrostatic Features

This project is to extract electrostatic features from a protein structure. Proposed stages are:

- Stage 1. Extract proposed electrostatic features an MCCE working directory.
- Stage 2. Extract electrostatic features from a pdb file directly from MCCE-ML module.
- Stage 3. Integrate electrostatic feature to PClass classifier

## Electrostatic Features

Total features: 83.

The feature set summarizes protein electrostatics from MCCE output files. Charges
are taken at pH 6.0, 7.0, and 8.0 from `sum_crg.out`, solvent accessibility from `acc.res`,
pKa values from `pK.out`, and residue coordinates from `step1_out.pdb`.
Surface residues are residues with solvent-accessible surface area fraction
greater than 0.1. Acidic residues are ASP, GLU, and CTR; basic residues are LYS,
ARG, HIS, NTR, and NTG.

## Category: Core Composition (9 features)

- `net_charge`: Total protein charge at pH 7.0 from the `Net_Charge` row in `sum_crg.out`.
- `isoelectric_point`: Estimated pH where total protein charge crosses zero.
- `acid_fraction_all_residues`: Fraction of all residues that are acidic.
- `glu_fraction_all_residues`: Fraction of all residues that are GLU.
- `asp_fraction_all_residues`: Fraction of all residues that are ASP.
- `base_fraction_all_residues`: Fraction of all residues that are basic.
- `lys_fraction_all_residues`: Fraction of all residues that are LYS.
- `arg_fraction_all_residues`: Fraction of all residues that are ARG.
- `acid_to_base_ratio`: Acidic-to-basic residue count ratio, using 999.0 when acids exist but bases do not.

## Category: pKa Perturbation (14 features)

- `acid_big_pka_shift_fraction_all_residues`: Fraction of all residues that are acidic residues with large pKa shifts.
- `glu_big_pka_shift_fraction_all_residues`: Fraction of all residues that are GLU residues with large pKa shifts.
- `asp_big_pka_shift_fraction_all_residues`: Fraction of all residues that are ASP residues with large pKa shifts.
- `base_big_pka_shift_fraction_all_residues`: Fraction of all residues that are basic residues with large pKa shifts.
- `lys_big_pka_shift_fraction_all_residues`: Fraction of all residues that are LYS residues with large pKa shifts.
- `arg_big_pka_shift_fraction_all_residues`: Fraction of all residues that are ARG residues with large pKa shifts.
- `acid_big_pka_shift_fraction_acids_only`: Fraction of acidic residues with large pKa shifts.
- `glu_big_pka_shift_fraction_acids_only`: Fraction of acidic residues that are GLU with large pKa shifts.
- `asp_big_pka_shift_fraction_acids_only`: Fraction of acidic residues that are ASP with large pKa shifts.
- `base_big_pka_shift_fraction_bases_only`: Fraction of basic residues with large pKa shifts.
- `lys_big_pka_shift_fraction_bases_only`: Fraction of basic residues that are LYS with large pKa shifts.
- `arg_big_pka_shift_fraction_bases_only`: Fraction of basic residues that are ARG with large pKa shifts.
- `mean_abs_pka_shift`: Mean absolute pKa shift among acidic and basic residues.
- `max_abs_pka_shift`: Maximum absolute pKa shift among acidic and basic residues.

## Category: Surface Charge (12 features)

- `surface_net_charge_6.0`: Net charge of solvent-exposed residues at pH 6.0.
- `surface_acid_to_base_ratio_6.0`: Exposed negative-to-positive charge ratio at pH 6.0.
- `surface_positive_charge_density_6.0`: Exposed positive charge per exposed SASA at pH 6.0.
- `surface_negative_charge_density_6.0`: Exposed negative charge magnitude per exposed SASA at pH 6.0.
- `surface_net_charge_7.0`: Net charge of solvent-exposed residues at pH 7.0.
- `surface_acid_to_base_ratio_7.0`: Exposed negative-to-positive charge ratio at pH 7.0.
- `surface_positive_charge_density_7.0`: Exposed positive charge per exposed SASA at pH 7.0.
- `surface_negative_charge_density_7.0`: Exposed negative charge magnitude per exposed SASA at pH 7.0.
- `surface_net_charge_8.0`: Net charge of solvent-exposed residues at pH 8.0.
- `surface_acid_to_base_ratio_8.0`: Exposed negative-to-positive charge ratio at pH 8.0.
- `surface_positive_charge_density_8.0`: Exposed positive charge per exposed SASA at pH 8.0.
- `surface_negative_charge_density_8.0`: Exposed negative charge magnitude per exposed SASA at pH 8.0.

## Category: Buried Charge (12 features)

- `buried_net_charge_6.0`: Net charge of buried residues at pH 6.0.
- `buried_acid_to_base_ratio_6.0`: Buried negative-to-positive charge ratio at pH 6.0.
- `buried_positive_charge_density_6.0`: Buried positive charge per buried-residue SASA at pH 6.0.
- `buried_negative_charge_density_6.0`: Buried negative charge magnitude per buried-residue SASA at pH 6.0.
- `buried_net_charge_7.0`: Net charge of buried residues at pH 7.0.
- `buried_acid_to_base_ratio_7.0`: Buried negative-to-positive charge ratio at pH 7.0.
- `buried_positive_charge_density_7.0`: Buried positive charge per buried-residue SASA at pH 7.0.
- `buried_negative_charge_density_7.0`: Buried negative charge magnitude per buried-residue SASA at pH 7.0.
- `buried_net_charge_8.0`: Net charge of buried residues at pH 8.0.
- `buried_acid_to_base_ratio_8.0`: Buried negative-to-positive charge ratio at pH 8.0.
- `buried_positive_charge_density_8.0`: Buried positive charge per buried-residue SASA at pH 8.0.
- `buried_negative_charge_density_8.0`: Buried negative charge magnitude per buried-residue SASA at pH 8.0.

## Category: Charge Patches (18 features)

- `largest_positive_patch_area_6.0`: SASA of the largest positive charge patch at pH 6.0.
- `largest_negative_patch_area_6.0`: SASA of the largest negative charge patch at pH 6.0.
- `largest_positive_patch_charge_6.0`: Total charge of the largest positive patch at pH 6.0.
- `largest_negative_patch_charge_6.0`: Total charge of the largest negative patch at pH 6.0.
- `largest_positive_patch_density_6.0`: Charge density of the largest positive patch at pH 6.0.
- `largest_negative_patch_density_6.0`: Charge density magnitude of the largest negative patch at pH 6.0.
- `largest_positive_patch_area_7.0`: SASA of the largest positive charge patch at pH 7.0.
- `largest_negative_patch_area_7.0`: SASA of the largest negative charge patch at pH 7.0.
- `largest_positive_patch_charge_7.0`: Total charge of the largest positive patch at pH 7.0.
- `largest_negative_patch_charge_7.0`: Total charge of the largest negative patch at pH 7.0.
- `largest_positive_patch_density_7.0`: Charge density of the largest positive patch at pH 7.0.
- `largest_negative_patch_density_7.0`: Charge density magnitude of the largest negative patch at pH 7.0.
- `largest_positive_patch_area_8.0`: SASA of the largest positive charge patch at pH 8.0.
- `largest_negative_patch_area_8.0`: SASA of the largest negative charge patch at pH 8.0.
- `largest_positive_patch_charge_8.0`: Total charge of the largest positive patch at pH 8.0.
- `largest_negative_patch_charge_8.0`: Total charge of the largest negative patch at pH 8.0.
- `largest_positive_patch_density_8.0`: Charge density of the largest positive patch at pH 8.0.
- `largest_negative_patch_density_8.0`: Charge density magnitude of the largest negative patch at pH 8.0.

## Category: Charge Asymmetry and Separation (15 features)

- `all_charge_spatial_moment_magnitude_6.0`: Whole-structure charge spatial moment magnitude at pH 6.0.
- `surface_charge_spatial_moment_magnitude_6.0`: Surface-residue charge spatial moment magnitude at pH 6.0.
- `all_charge_spatial_moment_normalized_6.0`: Size- and charge-normalized whole-structure spatial moment at pH 6.0.
- `surface_charge_spatial_moment_normalized_6.0`: Size- and charge-normalized surface spatial moment at pH 6.0.
- `charge_separation_magnitude_6.0`: Distance-weighted separation of positive and negative charge centers at pH 6.0.
- `all_charge_spatial_moment_magnitude_7.0`: Whole-structure charge spatial moment magnitude at pH 7.0.
- `surface_charge_spatial_moment_magnitude_7.0`: Surface-residue charge spatial moment magnitude at pH 7.0.
- `all_charge_spatial_moment_normalized_7.0`: Size- and charge-normalized whole-structure spatial moment at pH 7.0.
- `surface_charge_spatial_moment_normalized_7.0`: Size- and charge-normalized surface spatial moment at pH 7.0.
- `charge_separation_magnitude_7.0`: Distance-weighted separation of positive and negative charge centers at pH 7.0.
- `all_charge_spatial_moment_magnitude_8.0`: Whole-structure charge spatial moment magnitude at pH 8.0.
- `surface_charge_spatial_moment_magnitude_8.0`: Surface-residue charge spatial moment magnitude at pH 8.0.
- `all_charge_spatial_moment_normalized_8.0`: Size- and charge-normalized whole-structure spatial moment at pH 8.0.
- `surface_charge_spatial_moment_normalized_8.0`: Size- and charge-normalized surface spatial moment at pH 8.0.
- `charge_separation_magnitude_8.0`: Distance-weighted separation of positive and negative charge centers at pH 8.0.

## Category: Nearest Charged-Residue Distances (3 features)

- `nearest_opposite_charge_distance`: Shortest anchor-point distance between oppositely charged residues at pH 7.0.
- `nearest_positive_charge_distance`: Shortest anchor-point distance between two positively charged residues at pH 7.0.
- `nearest_negative_charge_distance`: Shortest anchor-point distance between two negatively charged residues at pH 7.0.

## Quick Start

### Installation
`pip install mcce-features`

The CLI entry point will be available after a successful installation:

```
mcce-features
```

To extract features from an MCCE folder
```
mcce-features extract <folder_name>
```

To extract feature from multiple MCCE folders
```
mcce-features extract-folders <folder.lst>
```

### Installation with latest changes (recommended)
The repo is not yet setup to publish automatically, so the usual pip install will be
the original version.
```
# 1. clone this repo somewhere you want it to be, then enter its dir:
git clone https://github.com/pclass-lab/elefeatures.git
cd elefeatures

# 2. Activate an environment setup for python>-3.12, eg: p312:
conda activate p312
(p312)> pip install -e .

# 3. Go get features:
(p312)> cd my_mcce_simulations

# Extract features using the book.txt files from all the subfolders that have one:
(p312)> mcce-features extract-subfolders-with-book .
```


File <folder.lst> can be a (space, comma, tab) delimited file with a
MCCE folder name in the first column of each line.
