# Open-Source and Disclosure Notes

This repository is the public companion for the ICME 2026 paper **Dual-Anchor
Reward-Aware Reinforcement Learning for Medical Report Generation**.

## Disclosure Boundary

The repository mirrors information already described in the accepted paper:

- CLIP-style cross-modal retrieval;
- adaptive Top-k evidence selection with leave-one-out filtering;
- a Mistral-based retrieval-conditioned generator;
- PPO alignment with Image-grounded Fidelity Reward (IFR) and
  Reference-guided Coherence Reward (RCR);
- reported MIMIC-CXR results and ablations.

It does not contain private medical data, executable production pipelines,
checkpoints, private prompts, or infrastructure-specific training recipes.

## Data Governance

Never commit:

- DICOM studies, images, reports, annotations, or patient identifiers;
- cached embeddings that can be linked to patient records;
- credentials, access tokens, private endpoints, or dataset access files;
- model checkpoints derived from restricted data without explicit permission.

## Publication Maintenance

- Update the citation when the official proceedings record and DOI are public.
- Keep reported metrics synchronized with the accepted or camera-ready paper.
- Clearly distinguish paper-reported results from independently reproduced runs.
- Review every public commit for medical-data leakage and licensing issues.
- Add a license only after the project owners have selected and approved one.

## Responsible Use

This project is intended for research. Generated reports require review by
qualified clinicians and must not be treated as independent medical advice.
