# Meta‑CD  
written by Callie Claiborne — Lyu Lab, North Carolina State University (cysteger@ncsu.edu) 

**Live Tool:** https://cysteger.github.io/Meta-CD/  
**Repository:** https://github.com/cysteger/Meta-CD

---

# Description

Meta‑CD is a browser‑based tool for **species‑specific metagenomic sequencing evaluation**. It provides both **post‑sequencing analysis** and **pre‑sequencing experimental planning**, enabling researchers to estimate:

- Achieved sequencing coverage  
- Required sequencing depth  
- Minimum detectable relative abundance  
- MAG recovery potential  
- Coverage matrices across depth × abundance  
- DNA‑quantity‑adjusted effective depth  

The tool is fully client‑side (HTML/JS/CSS) and requires **no installation**, **no dependencies**, and **no data upload**. All calculations run locally in the user’s browser.

Meta‑CD is designed for microbial ecologists, metagenomic researchers, and sequencing‑based study designers who need fast, interpretable, species‑level coverage predictions.

---

# Overview

Meta‑CD integrates four key parameters:

- Genome size (Mbp)  
- Relative abundance (%)  
- Community sequencing depth (Gb)  
- Sample DNA quantity (ng)  

These parameters determine the number of bases sequenced for a species, the achievable coverage, and the feasibility of downstream analyses such as:

- Taxonomic profiling  
- Functional profiling  
- Rare gene detection  
- MAG recovery  

The tool implements coverage equations commonly used in metagenomics, including:

- **Achieved coverage**  
- **Required depth for target coverage**  
- **Minimum relative abundance for detection**  
- **DNA‑quantity‑limited effective depth**  

MAG recovery thresholds are based on typical coverage requirements for high‑quality genome assembly.

---

# How Meta‑CD Works

## 1. Post‑Sequencing Analysis
Given observed sequencing depth and relative abundance, the tool calculates:

- Bases sequenced for the species  
- Achieved coverage  
- DNA‑quantity‑adjusted coverage  
- MAG recovery potential  
- Coverage estimation table  

## 2. Pre‑Sequencing Estimation
Given a target coverage, the tool estimates:

- Required sequencing depth  
- Minimum detectable relative abundance  
- DNA‑quantity‑adjusted detection thresholds  

## 3. Coverage Estimation Table
A depth × abundance matrix is generated to help users quickly evaluate:

- Feasibility of taxonomic profiling  
- Functional profiling thresholds  
- Rare gene detection  
- MAG recovery likelihood  

---

# How To Use Meta-CD

Meta‑CD is live, free to use, and is available at:

**https://cysteger.github.io/Meta-CD/**

This web-based tool requires no installation or registration to use.

---

# Running Meta‑CD Locally

To run the tool locally:


```bash
git clone https://github.com/cysteger/Meta-CD
cd Meta-CD
```
---

# Validation Test Suite (MBARC‑26)

Meta‑CD includes a fully reproducible validation suite based on the **MBARC‑26 mock community**, a defined mixture of 26 microbial genomes with known genome sizes, molarity, genome copy numbers, and sequencing representation. This dataset was published by Singer et al. (2016) as a benchmark for evaluating metagenomic sequencing and analysis tools.

The MBARC‑26 test suite allows users to verify that Meta‑CD’s calculations match experimentally measured sequencing outcomes.

## What the test suite contains

The directory [`tests/`](tests/) includes:

### **1. `mbarc26_numeric_expectations.csv`**
A machine‑generated table containing the **expected numeric outputs** for all 26 MBARC‑26 organisms, including:

- Genome size (bp, Mb)  
- Relative abundance (% mapped reads)  
- Sequencing depth (155.8 Gb)  
- Bases sequenced  
- Achieved coverage  
- Required depth for 5×  
- Minimum detectable relative abundance  
- DNA mass (ng)  
- DNA‑limited coverage  

These values were computed using the exact formulas implemented in Meta‑CD.

### **2. `generate_mbarc26_csv.py`**
A fully reproducible Python script that regenerates the CSV from:

- Genome sizes (Table 1 of Singer et al.)  
- Illumina % mapped genome (Supplementary Table 1)  
- Genome copies per µL (Supplementary Table 1)  
- Sequencing depth (Table 2)  

This ensures the test suite is transparent, auditable, and scientifically defensible.

### **3. `README_tests.md`**
Documentation describing:

- The formulas used  
- How each expected value is computed  
- How to validate Meta‑CD against the MBARC‑26 dataset  

---

## How to use the test suite

1. Open Meta‑CD (web or local).  
2. Select any organism from the MBARC‑26 dataset.  
3. Enter the values from `mbarc26_numeric_expectations.csv`:  
   - Genome size  
   - Relative abundance  
   - Sequencing depth  
   - DNA quantity (optional)  
4. Compare Meta‑CD’s outputs to the expected values in the CSV.

Meta‑CD should match the expected values within rounding error.

This provides a formal validation for users.

---

# References

## References

1. Nayfach S, Pollard KS. Average genome size estimation improves comparative metagenomics and sheds light on the functional ecology of the human microbiome. *Genome Biol.* 2015;16(1):51. doi:10.1186/s13059-015-0611-7

2. Benchmarking of shotgun sequencing depth reveals the potential and limitations of shallow metagenomics and strain-level analysis. *Nature Microbiology.* Accessed June 24, 2026. https://www.nature.com/articles/s41564-026-02334-2

3. Nayfach S, Pollard KS. Toward Accurate and Quantitative Comparative Metagenomics. *Cell.* 2016;166(5):1103–1116. doi:10.1016/j.cell.2016.08.007

4. Tremblay J, Schreiber L, Greer CW. High-resolution shotgun metagenomics: the more data, the better? *Brief Bioinform.* 2022;23(6):bbac443. doi:10.1093/bib/bbac443

5. Lander ES, Waterman MS. Genomic mapping by fingerprinting random clones: A mathematical analysis. *Genomics.* 1988;2(3):231–239. doi:10.1016/0888-7543(88)90007-9

6. Riesco R, Trujillo ME. Update on the proposed minimal standards for the use of genome data for the taxonomy of prokaryotes. *Int J Syst Evol Microbiol.* 2024;74(3). doi:10.1099/ijsem.0.006300

7. McNulty SN, Mann PR, Robinson JA, Duncavage EJ, Pfeifer JD. Impact of Reducing DNA Input on Next-Generation Sequencing Library Complexity and Variant Detection. *J Mol Diagn.* 2020;22(5):720–727. doi:10.1016/j.jmoldx.2020.02.003

8. Deng C, Daley T, Calabrese P, Ren J, Smith AD. Predicting the Number of Bases to Attain Sufficient Coverage in High-Throughput Sequencing Experiments. *J Comput Biol.* 2020;27(7):1130–1143. doi:10.1089/cmb.2019.0264

9. Singer E, Andreopoulos B, Bowers RM, et al. Next generation sequencing data of a defined microbial mock community. *Sci Data.* 2016;3(1):160081. doi:10.1038/sdata.2016.81


