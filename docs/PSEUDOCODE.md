# Conceptual Algorithm Sketch

This document intentionally avoids implementation-level pseudocode. It describes
only the public-facing research idea and omits proprietary details required for
reproduction.

## Concept

The method aligns a report generator using two complementary forms of feedback:

- **Visual grounding feedback:** encourages the generated report to remain
  consistent with the target medical image.
- **Textual coherence feedback:** encourages the generated report to remain
  clinically coherent with reliable reference evidence.

The private system combines these perspectives during alignment so that the
generator does not over-rely on retrieved text while also avoiding visually
unsupported statements.

## Public Training Sketch

```text
Input:
  A private medical report generation dataset
  A private evidence retrieval system
  A private report generation model
  Private feedback models and alignment code

Output:
  An aligned report generator

Conceptual steps:
  1. Prepare a private evidence store from permitted training materials.
  2. For each training case, collect relevant contextual evidence.
  3. Ask the generator to draft a report under the available context.
  4. Score the draft from a visual-grounding perspective.
  5. Score the draft from a textual-coherence perspective.
  6. Combine the private feedback signals.
  7. Align the generator using the private optimization recipe.
```

## Public Inference Sketch

```text
Input:
  A medical image study
  The aligned private generator
  The private retrieval system

Output:
  A generated report draft

Conceptual steps:
  1. Retrieve limited contextual evidence for the image study.
  2. Build a private generation context.
  3. Generate a report draft with the aligned model.
  4. Return the draft for downstream expert review.
```

## Withheld Details

The following details are intentionally not disclosed:

- retrieval scoring and filtering rules;
- evidence construction and de-duplication policies;
- prompt templates;
- model names and model sizes;
- feedback formulas and weighting;
- private data selection policies;
- training schedule and optimizer settings;
- evaluation scripts and dataset-specific processing;
- implementation code.
