import json
import argparse
from src.genomic_engine import VariantPathogenicityEngine

def main():
    parser = argparse.ArgumentParser(description="Helix Variant Pathogenicity Classifier CLI")
    parser.add_argument("--demo", action="store_true", help="Run simulated ACMG pathogenicity classification")
    args = parser.parse_args()

    engine = VariantPathogenicityEngine()
    report = engine.classify_variant(
        variant_id="BRCA1:c.5123C>A (p.Ala1708Glu)",
        gnomad_af=0.000008,
        evidence_codes=["PVS1", "PM1", "PM2", "PP3"]
    )
    print("="*60)
    print(" HELIX CLINICAL GENOMIC CLASSIFICATION AUDIT")
    print("="*60)
    print(json.dumps(report, indent=2))
    print("="*60)

if __name__ == "__main__":
    main()
