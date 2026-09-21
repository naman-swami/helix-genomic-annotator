import os
import json
import pytest
from parsers.vcf_parser import VCFParser, VCFRecord
from classifiers.acmg_rule_engine import ACMGRuleEngine
from pipelines.annotation_pipeline import GenomicAnnotationPipeline

@pytest.fixture
def sample_gnomad():
    return {
        "rs_pathogenic": {"global_af": 0.00002},
        "rs_benign": {"global_af": 0.08000}
    }

def test_vcf_parser_single_line():
    line = "chr17\t43044295\trs80357906\tT\tG\t.\tPASS\tAF=0.00003;GENE=BRCA1;CLNSIG=Pathogenic"
    rec = VCFParser.parse_line(line)
    assert rec.chrom == "chr17"
    assert rec.pos == 43044295
    assert rec.rsid == "rs80357906"
    assert rec.info["GENE"] == "BRCA1"
    assert rec.info["CLNSIG"] == "Pathogenic"

def test_acmg_benign_rule_ba1(sample_gnomad):
    engine = ACMGRuleEngine(sample_gnomad)
    res = engine.evaluate_variant("rs_benign", "BRCA2")
    assert res["acmg_classification"] == "BENIGN"
    assert "BA1" in res["applied_evidence_codes"]
    assert res["clinical_actionability"] == "NO_ACTION_REQUIRED"

def test_acmg_pathogenic_combination(sample_gnomad):
    engine = ACMGRuleEngine(sample_gnomad)
    # PVS1 + PS1 should trigger PATHOGENIC
    res = engine.evaluate_variant("rs_pathogenic", "BRCA1", ["PVS1", "PS1"])
    assert res["acmg_classification"] == "PATHOGENIC"
    assert res["clinical_actionability"] == "CLINICAL_INTERVENTION_INDICATED"

def test_pipeline_on_benchmark_vcf():
    ref_dir = os.path.join(os.path.dirname(__file__), "..", "data", "reference")
    vcf_path = os.path.join(ref_dir, "clinvar_sample.vcf")
    gnomad_file = os.path.join(ref_dir, "gnomad_stub.json")
    with open(gnomad_file, "r") as f:
        gnomad_data = json.load(f)
    pipeline = GenomicAnnotationPipeline(gnomad_data)
    results = pipeline.run_on_vcf(vcf_path)
    assert len(results) >= 4
    classifications = [r["acmg_classification"] for r in results]
    assert "PATHOGENIC" in classifications
    assert "BENIGN" in classifications
