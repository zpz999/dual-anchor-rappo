"""Paper-level structural pseudocode for Dual-Anchor RAPPO.

This module documents the public method decomposition from the ICME 2026 paper.
It deliberately omits executable model, data, reward, and optimization code.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class ReleaseMode(str, Enum):
    """Disclosure level of this public repository."""

    PAPER_LEVEL_CONCEPTUAL = "paper_level_conceptual"


@dataclass(frozen=True)
class MethodComponents:
    """Public components described in the accepted paper."""

    retriever: str = "CLIP-style cross-modal retriever"
    evidence_selection: str = "adaptive Top-k with leave-one-out filtering"
    generator: str = "Mistral-7B-Instruct-v0.2"
    policy_optimizer: str = "PPO with KL regularization"
    image_anchor: str = "Image-grounded Fidelity Reward (IFR)"
    reference_anchor: str = "Reference-guided Coherence Reward (RCR)"


RELEASE_MODE = ReleaseMode.PAPER_LEVEL_CONCEPTUAL
COMPONENTS = MethodComponents()


def conceptual_training_pipeline() -> tuple[str, ...]:
    """Return the non-executable, paper-level training stages."""

    return (
        "train shared image-report embeddings with symmetric InfoNCE",
        "build the report index and retrieve adaptive evidence",
        "initialize the evidence-conditioned generator with NLL",
        "sample reports from the current policy",
        "compute IFR and RCR with frozen reward encoders",
        "combine rewards into the Dual-Anchor Reward",
        "apply clipped PPO with KL regularization",
    )


def conceptual_inference_pipeline() -> tuple[str, ...]:
    """Return the non-executable, paper-level inference stages."""

    return (
        "encode the input image",
        "retrieve an adaptive evidence set",
        "assemble visual semantics and retrieved evidence",
        "generate a report with the aligned policy",
        "return the draft for qualified expert review",
    )


UNRELEASED_COMPONENTS = (
    "patient data and dataset preprocessing",
    "prompt templates",
    "executable reward and PPO implementations",
    "exact optimization schedules",
    "model checkpoints and private experiment logs",
)

