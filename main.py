import argparse
import json
import os
from parsers.vcf_parser import VCFParser
from classifiers.acmg_rule_engine import ACMGRuleEngine
from pipelines.annotation_pipeline import GenomicAnnotationPipeline

def main():
    parser = argparse.ArgumentParser(description="Helix Clinical Genomic Variant Annotator")
    parser.add_argument("--demo", action="store_true", help="Run annotation on benchmark VCF sample")
    parser.add_argument("--vcf", type=str, help="Path to input VCF file")
    parser.add_argument("--variant", type=str, help="Single rsID to query")
    args = parser.parse_args()

    ref_dir = os.path.join(os.path.dirname(__file__), "data", "reference")
    gnomad_file = os.path.join(ref_dir, "gnomad_stub.json")
    gnomad_data = {}
    if os.path.exists(gnomad_file):
        with open(gnomad_file, "r", encoding="utf-8") as f:
            gnomad_data = json.load(f)

    if args.demo or args.vcf:
        vcf_path = args.vcf if args.vcf else os.path.join(ref_dir, "clinvar_sample.vcf")
        pipeline = GenomicAnnotationPipeline(gnomad_data)
        results = pipeline.run_on_vcf(vcf_path)
        print("=== HELIX CLINICAL VARIANT ANNOTATION REPORT ===")
        print(f"Processed VCF: {vcf_path}")
        print(f"Total Variants Evaluated: {len(results)}\n")
        for res in results:
            print(f"[{res['rsid']}] Gene: {res['gene']} | ACMG: {res['acmg_classification']} | Action: {res['clinical_actionability']}")
            print(f"  Codes: {', '.join(res['applied_evidence_codes'])} | gnomAD AF: {res['gnomad_allele_frequency']}")
            print(f"  Confidence: {res['confidence_score']*100:.1f}%\n")
    elif args.variant:
        engine = ACMGRuleEngine(gnomad_data)
        res = engine.evaluate_variant(args.variant, "QUERY_GENE")
        print(json.dumps(res, indent=2))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
