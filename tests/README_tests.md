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

### **1. `mbarc26_numeric_expectations.csv`**
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
| `bases_sequenced_bp` | Expected bases sequenced for the organism |
| `coverage_x` | Expected fold coverage |
| `target_coverage_x` | Target coverage (set to 5×) |
| `required_depth_gb` | Depth required to reach 5× at observed RA |
| `min_detectable_ra_percent` | Minimum RA detectable at 5× given 155.8 Gb |
| `dna_mass_ng` | DNA mass (ng) computed from genome copies |
| `dna_limited_coverage_x` | Maximum theoretical coverage limited by DNA molecules |

All values are computed using the formulas described below.

---

## How the expected values were calculated

### **Sequencing depth**
From Table 2 of the paper:

> “355,875,608 raw reads… average insert size 219 ± 43 bp…”

Total sequenced bases:



\[
155.8\ \text{Gb}
\]



This value is used for all organisms.

---

## Core formulas (matching Meta‑CD)

Let:

- G = genome size (bp)
- D = total sequencing depth (Gb)
- p = relative abundance (%)
- C_target = 5 (target coverage)
- N = genome copies per µL

1. **Bases sequenced**

   B = D × 10^9 × (p / 100)

2. **Coverage**

   C = B / G

3. **Required depth for 5×**

   If p = 0, this is undefined → "NA".

   D_req = (5 × G) / (p / 100) / 10^9

4. **Minimum detectable RA at 5×**

   p_min = (5 × G) / (D × 10^9) × 100

5. **DNA mass (ng)**

   DNA_mass_ng = N × (G × 660) / (6.022 × 10^23) × 10^9

6. **DNA‑limited coverage**

   C_DNA = DNA_mass_ng × 10^-9 × 6.022 × 10^23 / (G × 660)

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

- Coverage  
- Bases sequenced  
- Required depth  
- Minimum detectable RA  
- DNA‑limited coverage  

within rounding error.

---


---

## Python Script: `generate_mbarc26_csv.py`

This directory includes a fully reproducible Python script that generates the file  
`generate_mbarc26_expected_outcomes_csv.py` using only values reported in the MBARC‑26 publication.

### Purpose of the script

The script computes all expected Meta‑CD outputs for each of the 26 MBARC‑26 organisms, including:

- Bases sequenced  
- Achieved coverage  
- Required depth for 5×  
- Minimum detectable relative abundance  
- DNA mass (ng)  
- DNA‑limited coverage  

These values are calculated using the exact formulas implemented in Meta‑CD, ensuring that the test suite is:

- Transparent  
- Reproducible  
- Auditable  
- Scientifically defensible  

### Inputs used by the script

The script pulls its inputs from the MBARC‑26 paper:

- **Genome size (bp)** — Table 1  
- **Illumina % mapped genome (relative abundance)** — Supplementary Table 1  
- **Genome copies per µL** — Supplementary Table 1  
- **Sequencing depth (155.8 Gb)** — Table 2  
- **Target coverage (5×)** — defined for this validation suite  

All values are hard‑coded into the script for reproducibility.

### What the script produces

Running the script generates: `mbarc26_expected_outcomes.csv`


This CSV contains one row per organism and includes:

- Genome size (bp, Mb)  
- Molarity  
- Genome copies per µL  
- Relative abundance (%)  
- Sequencing depth (Gb)  
- Bases sequenced  
- Achieved coverage  
- Required depth for 5×  
- Minimum detectable RA at 5×  
- DNA mass (ng)  
- DNA‑limited coverage  

These values represent the **ground‑truth numeric expectations** that Meta‑CD should reproduce.

### How to run the script

From the repository root:

```bash
cd tests
python generate_mbarc26_csv.py
```

---

## Citation

If you use this test suite in a publication, please cite:

Singer et al. (2016). *Next generation sequencing data of a defined microbial mock community.* Scientific Data 3:160081.

---

## Contact

For questions about this validation dataset or Meta‑CD, please contact:

**Callie — NC State University**  
Bioinformatics
cysteger@ncsu.edu


