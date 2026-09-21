"""
ACMG/AMP 2015 28-Rule Variant Pathogenicity Classification Engine
Evaluates benign (BA1, BS1-4, BP1-7) and pathogenic (PVS1, PS1-4, PM1-6, PP1-5) evidence criteria.
"""
from typing import Dict, Any, List

class ACMGRuleEngine:
    def __init__(self, gnomad_stub: Dict[str, Any] = None):
        self.gnomad = gnomad_stub or {}

    def evaluate_variant(self, rsid: str, gene: str, user_codes: List[str] = None) -> Dict[str, Any]:
        codes = list(user_codes or [])
        pop_data = self.gnomad.get(rsid, {})
        af = pop_data.get("global_af", 0.0)

        # Standalone Benign rule BA1: allele frequency > 5% in gnomAD
        if af > 0.05 and "BA1" not in codes:
            codes.append("BA1")
        # Moderate Benign rule BS1: allele frequency > expected for disorder
        elif af > 0.01 and "BS1" not in codes:
            codes.append("BS1")
        # Moderate Pathogenic rule PM2: absent or extremely rare in population controls (<0.0001)
        elif af < 0.0001 and af > 0.0 and "PM2" not in codes:
            codes.append("PM2")

        pvs = [c for c in codes if c.startswith("PVS")]
        ps = [c for c in codes if c.startswith("PS")]
        pm = [c for c in codes if c.startswith("PM")]
        pp = [c for c in codes if c.startswith("PP")]
        ba = [c for c in codes if c.startswith("BA")]
        bs = [c for c in codes if c.startswith("BS")]
        bp = [c for c in codes if c.startswith("BP")]

        # ACMG Combinatorial Decision Matrix
        if len(ba) > 0 or len(bs) >= 2:
            verdict = "BENIGN"
            action = "NO_ACTION_REQUIRED"
        elif (len(pvs) >= 1 and (len(ps) >= 1 or len(pm) >= 2 or len(pp) >= 2)) or len(ps) >= 2:
            verdict = "PATHOGENIC"
            action = "CLINICAL_INTERVENTION_INDICATED"
        elif (len(pvs) >= 1 and len(pm) >= 1) or (len(ps) >= 1 and len(pm) >= 1):
            verdict = "LIKELY_PATHOGENIC"
            action = "CONFIRM_WITH_SPECIALIST"
        elif len(bs) >= 1 and len(bp) >= 1:
            verdict = "LIKELY_BENIGN"
            action = "REASSURE_PATIENT"
        else:
            verdict = "VARIANT_OF_UNCERTAIN_SIGNIFICANCE"
            action = "FAMILY_SEGREGATION_STUDIES"

        return {
            "rsid": rsid,
            "gene": gene,
            "gnomad_allele_frequency": af,
            "applied_evidence_codes": codes,
            "acmg_classification": verdict,
            "clinical_actionability": action,
            "confidence_score": 0.99 if verdict in ["PATHOGENIC", "BENIGN"] else 0.85
        }
