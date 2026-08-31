import csv

# MBARC-26 INPUT DATA
data = [
    ("Terriglobus roseus", 5227858, 155, 2.07),
    ("Corynebacterium glutamicum", 3309401, 10, 0.30),
    ("Nocardiopsis dassonvillei", 6543312, 6, 0.00),
    ("Olsenella uli", 2051896, 304, 2.26),
    ("Segniliparus rotundus", 3157527, 149, 1.41),
    ("Echinicola vietnamensis", 5608040, 41, 0.62),
    ("Meiothermus silvanus", 3721669, 213, 8.56),
    ("Clostridium perfringens", 3256683, 39, 0.42),
    ("Clostridium thermocellum", 3843301, 15, 0.43),
    ("Desulfosporosinus acidiphilus", 4991181, 409, 15.11),
    ("Desulfosporosinus meridiei", 4873567, 261, 4.61),
    ("Desulfotomaculum gibsoniae", 4855529, 535, 6.91),
    ("Streptococcus pyogenes", 1852441, 16, 0.43),
    ("Thermobacillus composti", 4355525, 7, 8.50),
    ("Escherichia coli", 4639675, 16, 0.18),
    ("Frateuria aurantia", 3603458, 317, 3.99),
    ("Hirschia baltica", 3540114, 400, 8.16),
    ("Pseudomonas stutzeri", 4600489, 164, 1.55),
    ("Salmonella bongori", 4460105, 31, 0.14),
    ("Salmonella enterica", 4600800, 40, 0.52),
    ("Spirochaeta smaragdinae", 4653970, 467, 11.39),
    ("Fervidobacterium pennivorans", 2166381, 672, 11.26),
    ("Coraliomargarita akajimensis", 3750771, 144, 3.41),
    ("Halovivax ruber", 3223876, 614, 1.75),
    ("Natronobacterium gregoryi", 3788356, 569, 2.46),
    ("Natronococcus occultus", 4314118, 933, 3.55),
]

DEPTH_GB = 155.8
TARGET_COVERAGE = 5
AVOGADRO = 6.022e23
BP_MASS_DA = 660

def dna_mass_ng(genome_bp, genome_copies):
    mass_g = genome_copies * (genome_bp * BP_MASS_DA) / AVOGADRO
    return mass_g * 1e9

def effective_depth(depth_gb, dna_mass_ng):
    return min(depth_gb, dna_mass_ng)

def bases(depth_gb, ra):
    return depth_gb * 1e9 * (ra / 100)

def coverage(depth_gb, genome_mb, ra):
    return (depth_gb * 1000 * (ra / 100)) / genome_mb

def required_depth(genome_mb, ra, target_cov):
    if ra == 0:
        return "NA"
    return (target_cov * genome_mb) / (1000 * (ra / 100))

def min_ra(genome_mb, depth_gb, target_cov):
    return (target_cov * genome_mb) / (1000 * depth_gb) * 100

with open("mbarc26_expectated_outcomes.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "species","genome_bp","genome_mb","copies","ra_percent","depth_gb",
        "bases_naive","bases_dna_limited",
        "coverage_naive","coverage_dna_limited",
        "required_depth_naive",
        "min_ra_naive","min_ra_dna_limited",
        "dna_mass_ng","effective_depth_gb"
    ])

    for species, genome_bp, copies, ra in data:
        genome_mb = genome_bp / 1e6

        dna_ng = dna_mass_ng(genome_bp, copies)
        d_eff = effective_depth(DEPTH_GB, dna_ng)

        bases_naive = bases(DEPTH_GB, ra)
        bases_dna = bases(d_eff, ra)

        cov_naive = coverage(DEPTH_GB, genome_mb, ra)
        cov_dna = coverage(d_eff, genome_mb, ra)

        req_naive = required_depth(genome_mb, ra, TARGET_COVERAGE)

        min_ra_naive = min_ra(genome_mb, DEPTH_GB, TARGET_COVERAGE)
        min_ra_dna = min_ra(genome_mb, d_eff, TARGET_COVERAGE)

        writer.writerow([
            species, genome_bp, genome_mb, copies, ra, DEPTH_GB,
            bases_naive, bases_dna,
            cov_naive, cov_dna,
            req_naive,
            min_ra_naive, min_ra_dna,
            dna_ng, d_eff
        ])

print("CSV generated.")
