"""Concept-only placeholder.

This file deliberately does not expose executable pseudocode or implementation
logic. The underlying method, training recipe, reward construction, retrieval
policy, prompt design, and optimization details are proprietary.

Public concept:
    - collect private evidence for a medical image;
    - generate a draft report;
    - assess the draft from visual-grounding and textual-coherence perspectives;
    - align the generator with private feedback.

This module exists only to preserve repository structure for a public,
anonymized release.
"""


DISCLOSURE_LEVEL = "conceptual_only"


WITHHELD_COMPONENTS = (
    "retrieval_scoring",
    "evidence_filtering",
    "prompt_templates",
    "model_selection",
    "reward_formulas",
    "sampling_policy",
    "optimization_recipe",
    "dataset_processing",
)

