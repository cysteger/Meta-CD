import csv

# MBARC-26 INPUT DATA
data = [
    ("Terriglobus roseus", 5227858, 4.79e-15, 155, 2.07),
    ("Corynebacterium glutamicum", 3309401, 4.91e-16, 10, 0.30),
    ("Nocardiopsis dassonvillei", 6543312, 2.67e-17, 6, 0.00),  # RA = 0 → special case
    ("Olsenella uli", 2051896, 3.40e-14, 304, 2.26),
    ("Segniliparus rotundus", 3157527, 1.22e-14, 149, 1.41),
    ("Echinicola vietnamensis", 5608040, 1.26e-15, 41, 0.62),
    ("Meiothermus silvanus", 3721669, 4.38e-14, 213, 8.56),
    ("Clostridium perfringens", 3256683, 5.20e-16, 39, 0.42),
    ("Clostridium thermocellum", 3843301, 4.40e-16, 15, 0.43),
    ("Desulfosporosinus acidiphilus", 4991181, 2.68e-14, 409, 15.11),
    ("Desulfosporosinus meridiei", 4873567, 9.89e-15, 261, 4.61),
    ("Desulfotomaculum gibsoniae", 4855529, 2.93e-14, 535, 6.91),
    ("Streptococcus pyogenes", 1852441, 1.53e-15, 16, 0.43),
    ("Thermobacillus composti", 4355525, 2.39e-16, 7, 8.50),
    ("Escherichia coli", 4639675, 3.90e-16, 16, 0.18),
    ("Frateuria aurantia", 3603458, 2.84e-14, 317, 3.99),
    ("Hirschia baltica", 3540114, 1.78e-14, 400, 8.16),
    ("Pseudomonas stutzeri", 4600489, 1.21e-14, 164, 1.55),
    ("Salmonella bongori", 4460105, 1.72e-16, 31, 0.14),
    ("Salmonella enterica", 4600800, 6.69e-16, 40, 0.52),
    ("Spirochaeta smaragdinae", 4653970, 2.78e-14, 467, 11.39),
    ("Fervidobacterium pennivorans", 2166381, 6.21e-14, 672, 11.26),
    ("Coraliomargarita akajimensis", 3750771, 6.85e-15, 144, 3.41),
    ("Halovivax ruber", 3223876, 2.34e-14, 614, 1.75),
    ("Natronobacterium gregoryi", 3788356, 3.01e-14, 569, 2.46),
    ("Natronococcus occultus", 4314118, 2.15e-14, 933, 3.55),
]

# CONSTANTS
DEPTH_GB = 155.8
TARGET_COVERAGE = 5
AVOGADRO = 6.022e23
BP_MASS_DA = 660

# FUNCTIONS

def compute_bases_sequenced(depth_gb, ra_percent):
    return depth_gb * 1e9 * (ra_percent / 100)

def compute_coverage(bases, genome_bp):
    return bases / genome_bp

def compute_required_depth(genome_bp, ra_percent, target_cov):
    if ra_percent == 0:
        return "NA"
    return (target_cov * genome_bp) / (ra_percent / 100) / 1e9

def compute_min_detectable_ra(genome_bp, depth_gb, target_cov):
    return (target_cov * genome_bp) / (depth_gb * 1e9) * 100

def compute_dna_mass_ng(genome_bp, genome_copies):
    mass_g = genome_copies * (genome_bp * BP_MASS_DA) / AVOGADRO
    return mass_g * 1e9

def compute_dna_limited_coverage(genome_bp, dna_mass_ng):
    genome_copies = dna_mass_ng * 1e-9 * AVOGADRO / (genome_bp * BP_MASS_DA)
    return genome_copies

# WRITE CSV

with open("mbarc26_numeric_expectations.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "species", "genome_size_bp", "genome_size_mb",
        "molarity", "genome_copies_per_ul", "ra_percent",
        "depth_gb", "bases_sequenced_bp", "coverage_x",
        "target_coverage_x", "required_depth_gb",
        "min_detectable_ra_percent", "dna_mass_ng",
        "dna_limited_coverage_x"
    ])

    for species, genome_bp, molarity, copies, ra in data:
        genome_mb = genome_bp / 1e6
        bases = compute_bases_sequenced(DEPTH_GB, ra)
        cov = compute_coverage(bases, genome_bp) if ra > 0 else 0
        req_depth = compute_required_depth(genome_bp, ra, TARGET_COVERAGE)
        min_ra = compute_min_detectable_ra(genome_bp, DEPTH_GB, TARGET_COVERAGE)
        dna_mass = compute_dna_mass_ng(genome_bp, copies)
        dna_cov = compute_dna_limited_coverage(genome_bp, dna_mass)

        writer.writerow([
            species, genome_bp, genome_mb,
            molarity, copies, ra,
            DEPTH_GB, bases, cov,
            TARGET_COVERAGE, req_depth,
            min_ra, dna_mass, dna_cov
        ])

print("CSV generated: mbarc26_numeric_expectations.csv")
