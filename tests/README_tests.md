# MBARC‑26 Validation Test Suite for Meta‑CD

This directory contains a complete, reproducible validation dataset based on the **MBARC‑26 mock community**, as described in:

Singer et al. (2016). *Next generation sequencing data of a defined microbial mock community.* Scientific Data 3:160081.  
DOI https://doi.org/10.1038/sdata.2016.81

> “MBARC‑26 consists of 23 bacterial and 3 archaeal strains… Genome sizes span 1.8–6.5 Mbp… All genomes are available as finished sequences.”  
>  
> “Samples were pooled at varying ratios to generate the mock community (Fig. 2, Supplementary Table 1).”

The purpose of this test suite is to provide **confident numeric expectations** for all Meta‑CD calculations, enabling users to confirm that the tool produces correct and biologically consistent results.

---

## Contents

### **1. `mbarc26_expected_outcomes.csv`**
A table containing **all expected Meta‑CD outputs** for each of the 26 MBARC‑26 organisms.

Columns include:

| Column | Description |
|--------|-------------|
| `species` | Organism name (Table 1) |
| `genome_size_bp` | Genome size in base pairs (Table 1) |
| `genome_size_mb` | Genome size in megabases |
| `molarity` | DNA molarity from Supplementary Table 1 |
| `genome_copies_per_ul` | Genome copies per µL (Supplementary Table 1) |
| `ra_percent` | Illumina % mapped genome (used as relative abundance) |
| `depth_gb` | Total sequencing depth (155.8 Gb; Table 2) |
| `bases_naive` | Bases sequenced using total depth |
| `bases_dna_limited` | Bases sequenced using DNA‑limited effective depth |
| `coverage_naive` | Coverage using total depth |
| `coverage_dna_limited` | Coverage using DNA‑limited effective depth |
| `required_depth_naive` | Depth required to reach 5× at observed RA |
| `min_ra_naive` | Minimum RA detectable at 5× using total depth |
| `min_ra_dna_limited` | Minimum RA detectable at 5× using DNA‑limited depth |
| `dna_mass_ng` | DNA mass (ng) computed from genome copies |
| `effective_depth_gb` | Effective sequencing depth (min(total depth, DNA mass)) |

All values are computed using the formulas described below.

---

## How the expected values were calculated

### **Sequencing depth**
From Table 2 of the paper:

> “355,875,608 raw reads… average insert size 219 ± 43 bp…”

Total sequenced bases:

155.8 Gb

This value is used for all organisms.

---

## Core formulas (matching Meta‑CD)

Let:

- G = genome size (bp)  
- D = total sequencing depth (Gb)  
- D<sub>effective</sub> = min(D, DNA<sub>mass,ng</sub>)  
- p = relative abundance (%)  
- C<sub>target</sub> = 5 (target coverage)  
- N = genome copies per µL  

1. **Bases sequenced (naive)**  
   B<sub>naive</sub> = D × 10<sup>9</sup> × (p/100)

2. **Bases sequenced (DNA‑limited)**  
   B<sub>DNA</sub> = D<sub>effective</sub> × 10<sup>9</sup> × (p/100)

3. **Coverage (naive)**  
   C<sub>naive</sub> = (D × 1000 × (p/100)) / G<sub>Mb</sub>

4. **Coverage (DNA‑limited)**  
   C<sub>DNA</sub> = (D<sub>effective</sub> × 1000 × (p/100)) / G<sub>Mb</sub>

5. **Required depth for 5×**  
   If p = 0 → “NA”  
   D<sub>req</sub> = (5 × G<sub>Mb</sub>) / (1000 × (p/100))

6. **Minimum detectable RA (naive)**  
   p<sub>min,naive</sub> = (5 × G<sub>Mb</sub>) / (1000 × D) × 100

7. **Minimum detectable RA (DNA‑limited)**  
   p<sub>min,DNA</sub> = (5 × G<sub>Mb</sub>) / (1000 × D<sub>effective</sub>) × 100

8. **DNA mass (ng)**  
   DNA<sub>ng</sub> = N × (G × 660) / (6.022 × 10<sup>23</sup>) × 10<sup>9</sup>

---

## How to use this test suite

### **1. Open Meta‑CD**
Use the web interface or local `index.html`.

### **2. For any organism (e.g., *Terriglobus roseus*) enter:**
- Genome size (Mb)  
- Relative abundance (%)  
- Sequencing depth (Gb)  
- DNA quantity (optional)  
- Target coverage (5×)

### **3. Compare Meta‑CD’s outputs to the CSV**
Meta‑CD should match:

- Naive coverage (C<sub>naive</sub>)  
- DNA‑limited coverage (C<sub>DNA</sub>)  
- Naive bases sequenced (B<sub>naive</sub>)  
- DNA‑limited bases sequenced (B<sub>DNA</sub>)  
- Required depth (D<sub>req</sub>)  
- Minimum detectable RA (p<sub>min,naive</sub> and p<sub>min,DNA</sub>)  
- DNA mass (DNA<sub>ng</sub>)  
- Effective depth (D<sub>effective</sub>)  

within rounding error.

---

### **2. `generate_mbarc26_expected_outcomes_csv.py`**

This directory includes a fully reproducible Python script that generates the file  
`mbarc26_expected_outcomes.csv` using only values reported in the MBARC‑26 publication.

#### Purpose of the script

The script computes all expected Meta‑CD outputs for each of the 26 MBARC‑26 organisms, including:

- Bases sequenced (B<sub>naive</sub> and B<sub>DNA</sub>)  
- Achieved coverage (C<sub>naive</sub> and C<sub>DNA</sub>)  
- Required depth for 5× (D<sub>req</sub>)  
- Minimum detectable relative abundance (p<sub>min,naive</sub> and p<sub>min,DNA</sub>)  
- DNA mass (DNA<sub>ng</sub>)  
- Effective depth (D<sub>effective</sub>)  

These values are calculated using the exact formulas implemented in Meta‑CD, ensuring that the test suite is:

- Transparent  
- Reproducible  
- Auditable  
- Scientifically defensible  

#### Inputs used by the script

The script pulls its inputs from the MBARC‑26 paper:

- **Genome size (bp)** — Table 1  
- **Illumina % mapped genome (relative abundance)** — Supplementary Table 1  
- **Genome copies per µL** — Supplementary Table 1  
- **Sequencing depth (155.8 Gb)** — Table 2  
- **Target coverage (5×)** — defined for this validation suite  

All values are hard‑coded into the script for reproducibility.

#### What the script produces

Running the script generates: `mbarc26_expected_outcomes.csv`

This CSV contains one row per organism and includes:

- Genome size (bp, Mb)  
- Molarity  
- Genome copies per µL  
- Relative abundance (%)  
- Sequencing depth (Gb)  
- Bases sequenced (B<sub>naive</sub>, B<sub>DNA</sub>)  
- Achieved coverage (C<sub>naive</sub>, C<sub>DNA</sub>)  
- Required depth for 5× (D<sub>req</sub>)  
- Minimum detectable RA (p<sub>min,naive</sub>, p<sub>min,DNA</sub>)  
- DNA mass (DNA<sub>ng</sub>)  
- Effective depth (D<sub>effective</sub>)  

These values represent the **ground‑truth numeric expectations** that Meta‑CD should reproduce.

#### How to run the script

From the repository root:

```bash
cd tests
python generate_mbarc26_expected_outcomes_csv.py
```

---

### **3. `mbarc26_inputs.csv`**

This file contains the **raw biological and sequencing inputs** required to generate the  
`mbarc26_expected_outcomes.csv` validation dataset. These values come directly from the  
MBARC‑26 publication and represent the foundational parameters used by the Python script  
`generate_mbarc26_expected_outcomes_csv.py`.

The file includes the following columns:

| Column | Description |
|--------|-------------|
| `species` | Organism name |
| `genome_size_bp` | Genome size in base pairs (Table 1) |
| `genome_size_mb` | Genome size in megabases (rounded for convenience) |
| `relative_abundance_percent` | Relative abundance used for baseline validation (set to 1.0% for all organisms) |
| `sequencing_depth_gb` | Total sequencing depth (155.8 Gb for MBARC‑26) |
| `platform` | Sequencing platform (Illumina) |

#### Purpose of this file

This CSV provides the **minimal required biological and sequencing parameters** for each  
MBARC‑26 organism. These values serve as the **input layer** for the validation script, which  
computes all downstream Meta‑CD outputs, including:

- Bases sequenced (naive and DNA‑limited)  
- Coverage (naive and DNA‑limited)  
- Required depth for 5×  
- Minimum detectable RA (naive and DNA‑limited)  
- DNA mass (ng)  
- Effective depth (Gb)

#### How this file is used

The script uses hard‑coded MBARC‑26 values. These values are also provided separately in the tests file under the file name "mbarc26_inputs.csv".
`generate_mbarc26_expected_outcomes_csv.py` applies Meta‑CD’s formulas to produce the full expected‑outcomes table. 


## Citation

If you use this test suite in a publication, please cite:

Singer et al. (2016). *Next generation sequencing data of a defined microbial mock community.* Scientific Data 3:160081.

---

## Contact

For questions about this validation dataset or Meta‑CD, please contact:

**Callie Claiborne — NC State University**  
Bioinformatics
cysteger@ncsu.edu


