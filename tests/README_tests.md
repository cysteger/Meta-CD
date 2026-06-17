# MBARC-26 Test Suite for Meta-CD

This directory contains a validation dataset based on the **MBARC-26 mock community** described in:

Singer et al. (2016). *Next generation sequencing data of a defined microbial mock community.* Scientific Data 3:160081. DOI: https://doi.org/10.1038/sdata.2016.81.

> “We here report the next generation metagenomic sequence data of a defined mock community (Mock Bacteria ARchaea Community; MBARC-26), composed of 23 bacterial and 3 archaeal strains with finished genomes. These strains span 10 phyla and 14 classes, a range of GC contents, genome sizes, repeat content and encompass a diverse abundance profile.”  

## Files

- `mbarc26_inputs.csv`  
  Genome sizes, relative abundances, and sequencing depth for each MBARC-26 member (Illumina dataset).

- `mbarc26_expected_outputs.csv`  
  Expected fold coverage (×) for each genome, matching the Illumina coverage reported in Fig. 3b.

## Data Sources

- **Genome size**: Table 1 — “Genome statistics of each mock community member. Genome size includes chromosomes and plasmids.”  
- **Sequencing depth**: Table 2 — Illumina HiSeq 2000 run with 355,875,608 raw reads and average insert size 219 ± 43 bp (2×150 bp), yielding ~155.8 Gb total sequence.  
- **Relative abundance**: Fig. 2 and Supplementary Table 1 — community composition and relative abundance distribution based on mapped reads and molarity.  
- **Fold coverage**: Fig. 3b — “Percent chromosome coverage and fold coverage of each mock community genome by sequencing platform using unassembled sequences.”

## How to Use with Meta-CD

1. Open the Meta-CD web tool or local `index.html`.
2. For a given species (e.g., *Escherichia coli*):
   - Set **Genome size (Mb)** to the `genome_size_mb` value from `mbarc26_inputs.csv`.
   - Set **Relative abundance (%)** to `relative_abundance_percent`.
   - Set **Sequencing depth (Gb)** to `sequencing_depth_gb`.
   - Leave DNA quantity blank or set to a sufficiently high value if you want to ignore DNA-limited effects.
3. Run the post-sequencing analysis.
4. Compare the **coverage (×)** reported by Meta-CD to the `expected_coverage_x` in `mbarc26_expected_outputs.csv`.

Meta-CD should reproduce the reported fold coverage values (within rounding), confirming that its coverage calculations are consistent with a well-characterized, published mock community dataset.

## Purpose

This test suite is intended to:

- Demonstrate that Meta-CD’s coverage calculations match real, experimentally measured metagenomic data.
- Anchor Meta-CD’s outputs to a benchmark dataset explicitly designed for method evaluation and reproducibility.
