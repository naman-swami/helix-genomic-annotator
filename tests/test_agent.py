import pytest
from src.genomic_engine import VariantPathogenicityEngine

def test_pathogenic_classification():
    engine = VariantPathogenicityEngine()
    res = engine.classify_variant("VAR-1", 0.00001, ["PVS1", "PS1"])
    assert res["acmg_classification"] == "PATHOGENIC"
    assert res["clinical_actionability"] == "HIGH"

def test_benign_high_frequency():
    engine = VariantPathogenicityEngine()
    res = engine.classify_variant("VAR-2", 0.08, ["BA1"])
    assert res["acmg_classification"] == "BENIGN"
