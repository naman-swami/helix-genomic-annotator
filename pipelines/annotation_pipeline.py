"""
Helix Genomic Annotation Pipeline
Coordinates VCF intake, population frequency annotation, and ACMG interpretation.
"""
from typing import List, Dict, Any
from parsers.vcf_parser import VCFParser
from classifiers.acmg_rule_engine import ACMGRuleEngine

class GenomicAnnotationPipeline:
    def __init__(self, gnomad_data: Dict[str, Any] = None):
        self.engine = ACMGRuleEngine(gnomad_data)

    def run_on_vcf(self, vcf_path: str) -> List[Dict[str, Any]]:
        records = VCFParser.parse_file(vcf_path)
        annotated = []
        for rec in records:
            gene = rec.info.get("GENE", "UNKNOWN")
            evidence = []
            if rec.info.get("CLNSIG") == "Pathogenic":
                evidence.append("PVS1")
                evidence.append("PS1")
            
            res = self.engine.evaluate_variant(rec.rsid, gene, evidence)
            res["chrom"] = rec.chrom
            res["pos"] = rec.pos
            annotated.append(res)
        return annotated
