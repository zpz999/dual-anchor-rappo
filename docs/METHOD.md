# Method Details

## 1. Cross-modal representation learning

For paired image-report samples, the retriever learns normalized embeddings

$$
\bar{v}_i = \frac{f_I(X_i)}{\|f_I(X_i)\|_2}, \qquad
\bar{t}_i = \frac{f_T(Y_i)}{\|f_T(Y_i)\|_2},
$$

with scaled cosine similarity

$$
s_{i,j} = \gamma \bar{v}_i^\top \bar{t}_j.
$$

The training objective is the mean of image-to-text and text-to-image InfoNCE
losses.

## 2. Adaptive Top-k retrieval

Let the ranked similarities be
$s_{i,(1)} \ge s_{i,(2)} \ge \cdots$. Candidates are retained when

$$
s_{i,(1)} - s_{i,(j)} \le \log \delta,
$$

then capped by the configured maximum $k$. Training uses leave-one-out retrieval
to exclude the paired reference report and avoid trivial conditioning.

## 3. Retrieval-conditioned generation

The generator receives a compact visual semantic representation and retrieved
reports rather than raw image pixels. With context
$C_i = \Phi(z_i, E_i)$, generation is autoregressive:

$$
p_\theta(Y_i \mid C_i)
= \prod_{t=1}^{T_i} p_\theta(y_{i,t} \mid y_{i,<t}, C_i).
$$

The generator is first initialized with supervised negative log-likelihood.

## 4. PPO alignment

The policy is optimized with reward and KL regularization to a reference policy:

$$
\max_\theta\; \mathbb{E}[r_i]
- \beta\,\mathrm{KL}\!\left(
\pi_\theta(\cdot \mid P_i)\,\|\,\pi_{\mathrm{ref}}(\cdot \mid P_i)
\right).
$$

Reward normalization, clipping, KL scheduling, and gradient clipping are used to
stabilize optimization.

## 5. Dual-Anchor Reward

The final reward is

$$
r_{\mathrm{DAR}} = \lambda_I r_{\mathrm{IFR}}
+ \lambda_R r_{\mathrm{RCR}}.
$$

### Image-grounded Fidelity Reward

IFR combines bidirectional image-to-text and text-to-image contrastive rewards:

$$
r_{\mathrm{IFR}}(X, \hat{Y})
= \alpha r_{I\rightarrow T}(X, \hat{Y})
+ (1-\alpha)r_{T\rightarrow I}(\hat{Y}, X).
$$

The reward encoder remains frozen during PPO, and de-leakage negatives exclude
same-study or trivially related examples.

### Reference-guided Coherence Reward

RCR combines an InfoNCE-style semantic reward with clinical keyword coverage:

$$
r_{\mathrm{RCR}}(\hat{Y}, Y^*)
= r_{\mathrm{sem}}(\hat{Y}, Y^*)
+ \lambda_{\mathrm{kw}}r_{\mathrm{kw}}(\hat{Y}, Y^*),
$$

where the keyword term is an F1-style overlap:

$$
r_{\mathrm{kw}}(\hat{Y},Y^*)
= \frac{2|K(\hat{Y}) \cap K(Y^*)|}
{|K(\hat{Y})| + |K(Y^*)| + \epsilon}.
$$

Together, IFR prioritizes visual faithfulness while RCR supports clinically
coherent narration under retrieved context.
