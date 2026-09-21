"""
VCF v4.2 Record Parser
Extracts chromosomal coordinates, rsID identifiers, and INFO tag key-value pairs.
"""
from typing import List, Dict, Any

class VCFRecord:
    def __init__(self, chrom: str, pos: int, rsid: str, ref: str, alt: str, info: Dict[str, str]):
        self.chrom = chrom
        self.pos = pos
        self.rsid = rsid
        self.ref = ref
        self.alt = alt
        self.info = info

    def to_dict(self) -> Dict[str, Any]:
        return {
            "chrom": self.chrom,
            "pos": self.pos,
            "rsid": self.rsid,
            "ref": self.ref,
            "alt": self.alt,
            "info": self.info
        }

class VCFParser:
    @staticmethod
    def parse_line(line: str) -> VCFRecord:
        line = line.strip()
        if not line or line.startswith("#"):
            return None
        parts = line.split("\t")
        if len(parts) < 8:
            raise ValueError(f"Malformed VCF line: {line}")
        
        info_dict = {}
        for item in parts[7].split(";"):
            if "=" in item:
                k, v = item.split("=", 1)
                info_dict[k] = v
            else:
                info_dict[item] = "true"

        return VCFRecord(
            chrom=parts[0],
            pos=int(parts[1]),
            rsid=parts[2],
            ref=parts[3],
            alt=parts[4],
            info=info_dict
        )

    @classmethod
    def parse_file(cls, filepath: str) -> List[VCFRecord]:
        records = []
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                rec = cls.parse_line(line)
                if rec:
                    records.append(rec)
        return records
