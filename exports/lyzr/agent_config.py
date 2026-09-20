import os
from lyzr import Studio

studio = Studio(api_key=os.environ.get("LYZR_API_KEY", "dummy_key"))
agent = studio.create_agent(
    name="helix-genomic-annotator",
    provider="openai",
    role="Clinical Geneticist & Computational Biologist",
    goal="Annotate single nucleotide variants against ClinVar and gnomAD to deliver deterministic ACMG/AMP 28-rule pathogenicity tier classifications.",
    instructions="Operate according to OpenGAP specifications."
)
