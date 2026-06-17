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

- \( G \) = genome size (bp)  
- \( D \) = total sequencing depth (Gb)  
- \( p \) = relative abundance (%)  
- \( C_{\text{target}} = 5 \) (target coverage)  
- \( N \) = genome copies per µL  

### **1. Bases sequenced**


\[
B = D \times 10^9 \times \frac{p}{100}
\]



### **2. Coverage**


\[
C = \frac{B}{G}
\]



### **3. Required depth for 5×**
If \( p = 0 \), this is undefined → `"NA"`.



\[
D_{\text{req}} = \frac{5 \times G}{(p/100)} \div 10^9
\]



### **4. Minimum detectable RA at 5×**


\[
p_{\min} = \frac{5 \times G}{D \times 10^9} \times 100
\]



### **5. DNA mass (ng)**


\[
\text{DNA mass (ng)} = N \times \frac{G \times 660}{6.022\times10^{23}} \times 10^9
\]



### **6. DNA‑limited coverage**


\[
C_{\text{DNA}} = \frac{\text{DNA mass (ng)} \times 10^{-9} \times 6.022\times10^{23}}{G \times 660}
\]



This equals the number of unique genome copies present.

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



