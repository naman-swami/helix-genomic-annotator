# Clinical Genomic Annotation Standards & ACMG/AMP Guidelines

## 1. Clinical Variant Interpretation Framework
Helix implements the standards for interpreting sequence variants established by the **American College of Medical Genetics and Genomics (ACMG)** and the **Association for Molecular Pathology (AMP)** (Richards et al., 2015).

Variants are classified into one of five definitive clinical categories:
1. **Pathogenic (P)**
2. **Likely Pathogenic (LP)**
3. **Variant of Uncertain Significance (VUS)**
4. **Likely Benign (LB)**
5. **Benign (B)**

---

## 2. The 28-Rule ACMG Evidence Criteria

### A. Benign Evidence Criteria
- **BA1 (Stand-alone Benign)**: Allele frequency in gnomAD (or other outbred population cohorts) exceeds $5.0\%$.
- **BS1 (Strong Benign)**: Allele frequency is greater than expected for disorder ($> 1.0\%$).
- **BS2 (Strong Benign)**: Observed in healthy adult individuals for a recessive (homozygous) or dominant (heterozygous) penetrant disorder.
- **BP4 (Supporting Benign)**: Multiple lines of computational in-silico algorithms (SIFT, PolyPhen-2, CADD) suggest no damaging impact.

### B. Pathogenic Evidence Criteria
- **PVS1 (Very Strong Pathogenic)**: Null variant (nonsense, frameshift, canonical $\pm 1$ or $2$ splice sites, initiation codon) in a gene where loss of function (LoF) is a known mechanism of disease.
- **PS1 (Strong Pathogenic)**: Same amino acid change as a previously established pathogenic variant.
- **PM1 (Moderate Pathogenic)**: Located in a critical and well-established functional domain or mutational hotspot.
- **PM2 (Moderate Pathogenic)**: Absent or observed at extremely low allele frequency ($< 0.01\%$) in population databases (gnomAD v4).
- **PP3 (Supporting Pathogenic)**: Multiple lines of computational evidence predict a deleterious effect on the gene product.

---

## 3. Bayesian Combinatorial Classification Engine
The classification engine (`classifiers/acmg_rule_engine.py`) aggregates evidence criteria according to the Bayesian framework (Tavtigian et al., 2018):

| Clinical Tier | Required Combinatorial Rules |
| :--- | :--- |
| **Pathogenic** | (i) 1 Very Strong (PVS1) + $\ge 1$ Strong (PS1-4), OR<br>(ii) 1 Very Strong + $\ge 2$ Moderate (PM1-6), OR<br>(iii) $\ge 2$ Strong (PS1-4) |
| **Likely Pathogenic**| (i) 1 Very Strong + 1 Supporting (PP1-5), OR<br>(ii) 1 Strong + 1-2 Moderate, OR<br>(iii) $\ge 3$ Moderate |
| **Benign** | (i) 1 Stand-alone Benign (BA1), OR<br>(ii) $\ge 2$ Strong Benign (BS1-4) |
| **Variant of Uncertain Significance** | Criteria for benign or pathogenic not met, or conflicting evidence criteria observed |

---

## 4. Variant Call Format (VCF 4.2) Specifications
Input VCF files must conform strictly to the GA4GH VCF 4.2 specification:
- Headers must declare reference genome version (`GRCh38` or `hg19`).
- Variant lines must define `#CHROM`, `POS`, `ID`, `REF`, `ALT`, `QUAL`, `FILTER`, and `INFO`.
- Cross-referencing against ClinVar, dbSNP, and gnomAD is validated via `pipelines/annotation_pipeline.py`.
