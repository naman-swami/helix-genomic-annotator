# Helix — Variant Pathogenicity & Genomic Annotation Oracle

[![OpenGAP Compliant](https://img.shields.io/badge/OpenGAP-0.1.0-blue.svg)](https://opengap.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

Genomic variant interpretation agent automating ACMG/AMP pathogenicity classification, clinical trial matching, and protein structure perturbation analysis.

## Domain Category
**Healthcare**

## Architecture
- **OpenGAP Specification**: `0.1.0`
- **Role**: Clinical Geneticist & Computational Biologist
- **Primary Goal**: Annotate single nucleotide variants (SNVs) and indels against ClinVar, gnomAD, and AlphaMissense to deliver deterministic ACMG tier classifications.

## Skills Included
- **`variant-pathogenicity-scoring`**: Synthesizing population allele frequencies, in-silico deleterious predictions, and co-segregation statistics.
- **`splice-site-perturbation`**: Evaluating cryptic donor and acceptor activation using deep learning splice site junction predictors.
- **`oncology-trial-matching`**: Matching somatic driver mutations against active basket clinical trials via ClinicalTrials.gov and NCI MATCH.

## Tools Schema
- **`query-gnomad-frequencies`**: Retrieve population-specific minor allele frequencies (MAF) for specified chromosomal coordinates.
- **`compute-acmg-classification`**: Apply standard ACMG/AMP 28-rule Bayesian matrix to classify variant pathogenicity tier.
- **`evaluate-protein-impact`**: Assess AlphaFold structural residue displacement, delta-delta-G folding stability, and binding pocket occlusion.

## Explainability & Verification
Full explainability compliance under OpenGAP Checkpoint 2 is detailed in [EXPLAINABILITY.md](EXPLAINABILITY.md), covering:
- Decision Reasoning
- Data Sources and Inputs Used
- Confidence Scoring Methodology
- Source Attribution Protocol
- Bias Awareness
- Limitation Taxonomy per Domain
- Uncertainty Quantification Approach

## Multi-Framework Compatibility
Adapters and visa export configurations are included in `exports/`:
- Anthropic Claude (`claude-system-prompt.txt`)
- OpenAI Assistants (`openai-assistant.json`)
- LangChain (`langchain-agent.json`)
- CrewAI (`crewai-agent.json`)
- AutoGen (`autogen-agent.json`)

## License
MIT License
