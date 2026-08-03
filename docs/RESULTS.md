# Results and Ablations

All values below are transcribed from the accepted ICME 2026 paper. They are
paper-reported results, not fresh runs performed from this conceptual release.

## Comparison on MIMIC-CXR

| Method | BLEU-1 | BLEU-2 | BLEU-3 | BLEU-4 | ROUGE-L | METEOR | CIDEr |
|---|---:|---:|---:|---:|---:|---:|---:|
| M2Transformer | 0.332 | 0.210 | 0.142 | 0.101 | 0.264 | 0.134 | 0.142 |
| R2Gen | 0.353 | 0.218 | 0.145 | 0.103 | 0.277 | 0.142 | - |
| PPKED | 0.360 | 0.224 | 0.149 | 0.106 | 0.284 | 0.149 | 0.237 |
| GSK | 0.363 | 0.228 | 0.156 | 0.115 | 0.284 | - | 0.203 |
| R2GenCMN | 0.353 | 0.218 | 0.148 | 0.106 | 0.278 | 0.142 | - |
| MSAT | 0.373 | 0.235 | 0.162 | 0.120 | 0.282 | 0.143 | 0.299 |
| METransformer | 0.386 | **0.250** | 0.169 | 0.124 | **0.291** | 0.152 | **0.362** |
| R2GenGPT | 0.365 | 0.237 | 0.163 | 0.117 | 0.277 | 0.136 | 0.145 |
| FGIRG | 0.379 | 0.234 | 0.154 | 0.106 | 0.285 | 0.162 | - |
| R2GMMN | 0.396 | 0.244 | 0.162 | 0.115 | 0.274 | 0.151 | - |
| **Dual-Anchor RAPPO (ours)** | **0.407** | 0.247 | **0.170** | **0.137** | 0.271 | **0.190** | 0.345 |

## Retrieval and RL Ablation

| Setting | B-1 | B-2 | B-3 | B-4 | R-L | MTR | CIDEr |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top-1 + original | 0.243 | 0.110 | 0.080 | 0.077 | 0.189 | 0.087 | 0.165 |
| Adaptive Top-k + original | 0.342 | 0.186 | 0.132 | 0.095 | 0.218 | 0.117 | 0.195 |
| **Adaptive Top-k + RL** | **0.407** | **0.247** | **0.170** | **0.137** | **0.271** | **0.190** | **0.345** |

The ablation supports two observations:

1. Adaptive multi-evidence retrieval improves the original generator over Top-1
   retrieval.
2. PPO alignment produces a second, substantial improvement with retrieval held
   fixed.

## Reward Decomposition

| Reward setting | BLEU-4 | ROUGE-L | METEOR | CIDEr | Cosine similarity |
|---|---:|---:|---:|---:|---:|
| **IFR + RCR** | **0.1373** | **0.2714** | **0.1899** | **0.345** | - |
| RCR only | 0.1097 | 0.2636 | 0.1413 | 0.224 | -0.0126 |
| IFR only | 0.0998 | 0.2434 | 0.1377 | 0.202 | -0.0107 |

The full reward provides the strongest overall generation quality. In the paper
analysis, IFR primarily improves image-grounded factual alignment, while RCR
supports coherent clinical narration.

## Interpretation Boundary

The repository does not claim clinical readiness. Standard NLG metrics are useful
but do not replace clinician evaluation, factuality auditing, subgroup analysis,
or prospective validation.
