# Helix Genomic Annotator

[![OpenGAP](https://img.shields.io/badge/OpenGAP-0.1.0-blue.svg)](agent.yaml)
[![Bioinformatics](https://img.shields.io/badge/Domain-Clinical_Genomics-darkgreen.svg)](docs/acmg_guidelines_ref.md)
[![Standards](https://img.shields.io/badge/Standard-ACMG%2FAMP_2015-orange.svg)](docs/acmg_guidelines_ref.md)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](requirements.txt)
[![Build Status](https://img.shields.io/badge/CI-Passing-brightgreen.svg)](.github/workflows/ci.yml)

A high-throughput clinical variant interpretation engine automating ACMG/AMP (Richards et al. 2015) 28-rule Bayesian pathogenicity classification, gnomAD population control cross-referencing, and ClinVar concordance auditing.

```
                    ┌─────────────────────────┐
                    │    Raw VCF 4.2 File     │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │  parsers/vcf_parser.py  │
                    └────────────┬────────────┘
                                 │
                 ┌───────────────┴───────────────┐
                 ▼                               ▼
      ┌─────────────────────┐         ┌─────────────────────┐
      │ gnomAD v4 Frequency │         │ ClinVar / Evidence  │
      └──────────┬──────────┘         └──────────┬──────────┘
                 │                               │
                 └───────────────┬───────────────┘
                                 ▼
                    ┌─────────────────────────┐
                    │ classifiers/acmg_rule   │
                    │      (28 Criteria)      │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │ Clinical Pathogenicity  │
                    │ Report (JSON / Summary) │
                    └─────────────────────────┘
```

## Features

- **VCF v4.2 Intake**: Deterministic parsing of multi-sample or single-variant records with INFO tags.
- **Population Frequency Grounding**: Automatic evaluation of BA1 (AF > 0.05), BS1 (AF > 0.01), and PM2 (AF < 0.0001) against gnomAD.
- **ACMG 2015 Combinatorial Engine**: Evaluates PVS1, PS, PM, PP, BA, BS, BP rule combinations to assign:
  - `PATHOGENIC`
  - `LIKELY_PATHOGENIC`
  - `VARIANT_OF_UNCERTAIN_SIGNIFICANCE` (VUS)
  - `LIKELY_BENIGN`
  - `BENIGN`
- **Audit & Provenance**: Full evidence code attribution on every emitted clinical recommendation.

## Directory Structure

```
helix-genomic-annotator/
├── agent.yaml                       # OpenGAP 0.1.0 Manifest
├── EXPLAINABILITY.md                # 7-checkpoint clinical decision provenance
├── parsers/
│   └── vcf_parser.py                # VCF v4.2 specification reader
├── classifiers/
│   └── acmg_rule_engine.py          # ACMG/AMP 28-rule Bayesian classifier
├── pipelines/
│   └── annotation_pipeline.py       # End-to-end annotation coordinator
├── data/
│   └── reference/
│       ├── clinvar_sample.vcf       # Benchmark VCF fixture
│       └── gnomad_stub.json         # Reference allele frequencies
├── docs/
│   └── acmg_guidelines_ref.md       # Clinical standard specification
├── tests/
│   └── test_agent.py                # Unit & benchmark test suite
├── annotate.py                          # CLI entry point
└── requirements.txt
```

## Quick Start

```bash
# Run complete test suite
pytest tests/ -v

# Run interactive CLI on benchmark VCF
python annotate.py --demo
```

## Clinical Disclaimer

This software is designed for research and decision-support assistance. Classification output must be reviewed by a certified clinical geneticist or molecular pathologist prior to patient management.
