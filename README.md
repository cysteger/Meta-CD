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

# Scientific Overview

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

# Demo

A live, interactive version of Meta‑CD is available at:

**https://cysteger.github.io/Meta-CD/**

This version requires no installation and runs entirely in the browser.

---

# Running Meta‑CD Locally

To run the tool locally:


```bash
git clone https://github.com/cysteger/Meta-CD
cd Meta-CD
```


# References

ADD THESE!!!
