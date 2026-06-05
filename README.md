# MCCE Electrostatic Features

This project is to extract electrostatic features from a protein structure. Proposed stages are:

- Stage 1. Extract proposed electrostatic features an MCCE working directory.
- Stage 2. Extract electrostatic features from a pdb file directly from MCCE-ML module.
- Stage 3. Integrate electrostatic feature to PClass classifier

## Electrostatic Features

The feature set summarizes protein electrostatics from MCCE output files. Charges
are taken at pH 7.0 from `sum_crg.out`, solvent accessibility from `acc.res`,
pKa values from `pK.out`, and residue coordinates from `step1_out.pdb`.
Surface residues are residues with solvent-accessible surface area fraction
greater than 0.1. Acidic residues are ASP, GLU, and CTR; basic residues are LYS,
ARG, HIS, NTR, and NTG.

### Core Composition

These features account for the overall acidic/basic composition and net charge
state of the protein. They are relevant because global charge balance and pI
affect solubility, binding preference, membrane association, and broad functional
classes such as acidic enzymes, nucleic-acid-binding proteins, and strongly basic
surface binders.

| Feature | Measures | Calculation |
| --- | --- | --- |
| `net_charge` | Total protein charge at pH 7.0. | Reads the `Net_Charge` row in `sum_crg.out` and selects the pH 7.0 column. |
| `isoelectric_point` | Estimated pH where the total protein charge is zero. | Linearly interpolates between neighboring sampled pH values where `Net_Charge` changes sign; if no crossing is found, uses the sampled pH with smallest absolute net charge. |
| `acid_fraction_all_residues` | Fraction of all residues that are acidic. | Counts acidic residues and divides by the total residue count. |
| `base_fraction_all_residues` | Fraction of all residues that are basic. | Counts basic residues and divides by the total residue count. |
| `acid_to_base_ratio` | Balance of acidic to basic residue counts. | Divides acidic residue count by basic residue count; returns 1.0 when both counts are zero and 999.0 when acids are present but bases are absent. |

### pKa Perturbation

These features measure how strongly titratable residues are shifted away from
their model-compound pKa values in the folded protein environment. Large pKa
shifts often indicate buried charges, salt bridges, hydrogen-bond networks,
active-site tuning, ligand-coupled protonation, or other electrostatic constraints
that can be informative for function inference.

Intrinsic pKa values used here are ASP/GLU 4.75, LYS 10.4, ARG 12.5, HIS 6.98,
NTR/NTG 8.00, and CTR 3.75. A "big" pKa shift means
`abs(pKa - intrinsic_pKa) >= 1.0`.

| Feature | Measures | Calculation |
| --- | --- | --- |
| `acid_big_pka_shift_fraction_all_residues` | How much of the whole protein is made of acidic residues with large pKa shifts. | Counts acidic residues with big shifts and divides by total residue count. |
| `base_big_pka_shift_fraction_all_residues` | How much of the whole protein is made of basic residues with large pKa shifts. | Counts basic residues with big shifts and divides by total residue count. |
| `acid_big_pka_shift_fraction_acids_only` | Fraction of acidic residues that are strongly perturbed. | Counts acidic residues with big shifts and divides by acidic residue count. |
| `base_big_pka_shift_fraction_bases_only` | Fraction of basic residues that are strongly perturbed. | Counts basic residues with big shifts and divides by basic residue count. |
| `mean_abs_pka_shift` | Average magnitude of pKa perturbation among titratable acidic/basic residues. | Averages `abs(pKa - intrinsic_pKa)` over acidic and basic residues. |
| `max_abs_pka_shift` | Largest single-residue pKa perturbation. | Takes the maximum `abs(pKa - intrinsic_pKa)` over acidic and basic residues. |

### Surface Charge

These features describe the charge exposed to solvent rather than the whole
protein charge inventory. Surface electrostatics is often directly tied to
biophysical behavior because molecular recognition, protein-protein binding,
substrate steering, membrane interaction, and aggregation propensity are governed
by exposed charge.

| Feature | Measures | Calculation |
| --- | --- | --- |
| `surface_net_charge` | Net charge carried by solvent-exposed residues. | Sums pH 7.0 residue charges over residues with SASA fraction greater than 0.1. |
| `surface_acid_to_base_ratio` | Balance of exposed negative and positive charge. | Sums absolute negative surface charge and divides by positive surface charge, with a small pseudocount in the denominator. |
| `surface_positive_charge_density` | Amount of exposed positive charge per exposed surface area. | Sums positive charge over surface residues and divides by total surface-residue SASA. |
| `surface_negative_charge_density` | Amount of exposed negative charge per exposed surface area. | Sums absolute negative charge over surface residues and divides by total surface-residue SASA. |

### Patch Localization

These features account for spatially localized clusters of same-sign charged
residues. Charge patches can mark binding interfaces, catalytic regions,
membrane-contact surfaces, or electrostatic steering regions, so they are often
more functionally specific than global net charge.

Positive and negative patches are built separately from residues with charge
greater than 0.25 or less than -0.25. Residues of the same sign are grouped into
the same patch when their residue anchor points are connected by distances of
10.0 Angstrom or less. The reported patch is the largest patch by summed SASA.

| Feature | Measures | Calculation |
| --- | --- | --- |
| `largest_positive_patch_area` | Solvent-accessible area of the largest positive patch. | Sums SASA over residues in the largest positive patch. |
| `largest_negative_patch_area` | Solvent-accessible area of the largest negative patch. | Sums SASA over residues in the largest negative patch. |
| `largest_positive_patch_charge` | Total charge in the largest positive patch. | Sums pH 7.0 charges over residues in the largest positive patch. |
| `largest_negative_patch_charge` | Total charge in the largest negative patch. | Sums pH 7.0 charges over residues in the largest negative patch. |
| `largest_positive_patch_density` | Positive charge concentration in the largest positive patch. | Divides absolute patch charge by patch SASA. |
| `largest_negative_patch_density` | Negative charge concentration in the largest negative patch. | Divides absolute patch charge by patch SASA. |

### Charge Asymmetry as Spatial Moment

These features measure whether charge is evenly distributed around the protein or
biased toward one side. Asymmetric charge distributions can indicate polarized
binding surfaces, directional encounter complexes, membrane-facing regions, or
proteins whose function depends on orienting a charged face toward a partner.

The spatial moment is calculated as `sum(q_i * (r_i - r_center))`, where `q_i`
is residue charge, `r_i` is the residue anchor point, and `r_center` is the
geometric center of the selected residues. Normalized features divide the moment
magnitude by `(sum(abs(q_i)) * radius_of_gyration)`.

| Feature | Measures | Calculation |
| --- | --- | --- |
| `all_charge_spatial_moment_magnitude` | Strength of whole-protein charge asymmetry. | Computes the magnitude of the charge-weighted spatial moment using all residues with charge and coordinates. |
| `surface_charge_spatial_moment_magnitude` | Strength of exposed charge asymmetry. | Computes the same moment using only surface residues. |
| `all_charge_spatial_moment_normalized` | Whole-protein charge asymmetry independent of charge amount and size scale. | Normalizes the all-residue moment by total absolute charge times radius of gyration. |
| `surface_charge_spatial_moment_normalized` | Exposed charge asymmetry independent of surface charge amount and size scale. | Normalizes the surface-residue moment by surface absolute charge times surface radius of gyration. |

### Dipole as Charge Separation

This feature measures how far the centers of positive and negative charge are
separated. It is a practical charge-separation descriptor rather than a strict
physics dipole, which makes it easier to compare proteins with nonzero net
charge. It can help identify proteins with polarized electrostatic organization
that may orient toward partners, membranes, substrates, or fields.

| Feature | Measures | Calculation |
| --- | --- | --- |
| `charge_separation_magnitude` | Distance-weighted separation of positive and negative charge centers. | Computes charge-weighted centroids for positive and negative residues, measures the distance between them, and multiplies by the smaller of total positive charge and total absolute negative charge. |

## Quick Start

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

File <folder.lst> can be a (space, comma, tab) delimited file with a
MCCE folder name in the first column of each line.
