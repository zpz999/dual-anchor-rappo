# Conceptual Pseudocode

This document presents the method at the same level of disclosure as the ICME
2026 paper. It is explanatory pseudocode, not a runnable training pipeline.

## Stage 1: Cross-modal retrieval training

```text
Input:
  Image-report pairs D = {(X_i, Y_i)}
  Image encoder f_I and text encoder f_T

For each mini-batch:
  1. Encode images:  v_i = normalize(f_I(X_i))
  2. Encode reports: t_i = normalize(f_T(Y_i))
  3. Compute scaled cosine similarities s_ij
  4. Optimize symmetric image-to-text and text-to-image InfoNCE

Output:
  A shared image-report embedding space and indexed report corpus M
```

## Stage 2: Adaptive Top-k evidence construction

```text
Input:
  Target image X_i, report corpus M, maximum evidence count k

1. Rank reports by image-report similarity.
2. Keep reports close to the top-1 score under the relative threshold.
3. Cap the evidence set at k while always retaining the best candidate.
4. During training, exclude the matched ground-truth report and optionally
   other reports from the same study.

Output:
  Evidence set E_i with 1 <= |E_i| <= k
```

## Stage 3: Retrieval-conditioned supervised initialization

```text
Input:
  Visual semantic embedding z_i = f_I(X_i)
  Retrieved evidence E_i
  Mistral-based report generator pi_theta

1. Map z_i into a compact visual semantic prompt.
2. Serialize the visual prompt and E_i into a structured instruction.
3. Optimize negative log-likelihood on the reference report Y_i.

Output:
  Supervised retrieval-conditioned policy pi_theta
```

## Stage 4: Dual-Anchor PPO alignment

```text
Input:
  Supervised policy pi_theta
  Frozen reference policy pi_ref
  Frozen image-report reward encoder
  Frozen report reward encoder

For each PPO update:
  1. Retrieve adaptive evidence E_i for image X_i.
  2. Sample a report Y_hat from pi_theta.
  3. Compute IFR:
       - image-to-text contrastive fidelity;
       - text-to-image contrastive fidelity.
  4. Compute RCR:
       - reference-guided semantic consistency;
       - clinical keyword coverage.
  5. Combine rewards:
       r_DAR = lambda_I * r_IFR + lambda_R * r_RCR
  6. Normalize and clip rewards as configured.
  7. Apply the clipped PPO objective with KL regularization to pi_ref.

Output:
  Dual-anchor aligned report-generation policy
```

## Inference

```text
Input:
  Chest X-ray study X
  Trained retriever and aligned generator

1. Encode X and retrieve an adaptive evidence set E.
2. Build the visual-semantic and evidence-conditioned prompt.
3. Generate a report with the aligned policy.
4. Return the report for qualified expert review.
```

## Intentionally Unreleased Components

- patient data and dataset-specific preprocessing code;
- exact prompts and infrastructure-specific training recipes;
- executable reward-model, PPO, and evaluation implementations;
- checkpoints, tokenizer assets, and private experiment logs.
