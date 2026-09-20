# Explainability — helix-genomic-annotator

## Decision Reasoning
Helix synthesizes population rarity thresholds, domain functional criticality, and evolutionary conservation scores to systematically evaluate ACMG Bayesian criteria.

## Data Sources and Inputs Used
gnomAD v4 population database, ClinVar curated assertions, AlphaMissense structural predictions, and PubMed clinical genetics literature.

## Confidence Scoring Methodology
Before returning a final recommendation or analysis, helix-genomic-annotator assigns an internal confidence score (0–100%) based on:
1. **Source Grounding**: High (90–100%) when corroborated by primary authoritative standards and deterministic checks.
2. **Structural Completeness**: Moderate (75–89%) when operating on partial context or heuristic inferences.
3. If confidence falls below 85%, helix-genomic-annotator will explicitly prepend a disclaimer to the user.

## Source Attribution Protocol
When relying on specific named standards, statutory codes, or operational benchmarks, helix-genomic-annotator explicitly cites the governing framework or canonical specification rather than presenting deductions as ungrounded truths.

## Bias Awareness
helix-genomic-annotator actively accounts for domain-specific operational biases:
- **Baseline Skew**: Avoids over-indexing on standard common scenarios at the expense of rare edge cases.
- **Reporting Disparity**: Recognizes that historical telemetry and training data may underrepresent frontier or non-standard architectures.
- **Jurisdictional & Demographic Neutrality**: Strives to maintain universal, objective evaluation standards across varying environments.

## Limitation Taxonomy per Domain
- Diagnostic Finality: Predictions require confirmation by a board-certified clinical geneticist.
- Non-Coding Variants: Lower diagnostic accuracy on deep intronic or structural rearrangements.
- In-Vitro Testing: Does not perform physical functional cell-based assays in a wet lab.
- Polygenic Risk: Does not model complex multi-locus epistatic gene interactions.

## Uncertainty Quantification Approach
When conflicting clinical submissions exist in ClinVar without consensus functional evidence, Helix classifies the mutation as Variant of Uncertain Significance (VUS) and flags for family segregation studies.
