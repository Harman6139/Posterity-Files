# Checkpoint 12 — proof audit, model boundaries, and reading completion

Date: 2026-11-14. Parent: f822db1f4a3f0677bbe3ddc55af8a3b83a784abb.

## 1. Original target remains distinct

The handoff requires rationally described oracle inputs, unrestricted finite queries, exact natural conic values and coordinate gradients, a fixed hard prior independent of the algorithm's seed, and a dimension-uniform escape profile. Checkpoints 07–11 do not prove or disprove that combined statement. The real-coefficient exact theorem, rational radius-charged theorem, and rational positive-error theorem are separate results. None is silently relabeled as the original target.

There is an additional coordinate-model distinction worth making explicit. In checkpoint 09, C_U=C_0 U^T and S_U=S_0 U^T. Since U is invertible, varying U changes the hidden isometric coordinate chart but not the affine matrix image of the x block. The geometric slice itself can therefore be fixed and rational. Nevertheless the oracle-input chart has real coefficients. Calling the underlying slice rational is NOT enough to claim a polynomial rational encoding of the hidden oracle problem. We count the chart among the input data. This prevents an artificial resolution of the rational requirement by concealing nonrational information in coordinate names.

## 2. Clarification to checkpoint 11: prior over admissible deterministic pairs

The sequential lower proof in checkpoint 11 samples U first and sets V=Q_delta(U). It uses the rational true objective f_V and the fixed deterministic measurement field grad f_U. For EACH fixed pair (V,U), the measurement noise variance is exactly zero and the pointwise input-relative bias bound holds. Thus every sampled pair is an admissible problem-plus-oracle pair for every variance allowance tau>=0.

The prior is used only to lower-bound the supremum over admissible pairs. If one conditions on V alone and integrates out U, the resulting latent mixture need not have zero conditional variance. That mixture is NOT being claimed as a zero-variance oracle. The proof does not require it to be one: averaging the failure probabilities of admissible deterministic pairs already gives the minimax lower bound, and the pair is sampled before the algorithm's seed. This wording replaces the potentially misleading latent-randomness sentence in checkpoint 11, Section 4.

## 3. Audited algebra and quantifiers

* The spectral calculation in checkpoint 07 is exact: a star has negative-eigenvalue energy ||Cx-d||^2/2; the positive-offset arrow contributes (||Sx||-M)_+^2/2. Their coordinate Gram matrices sum to I. Forward and reverse oracle simulations hold at every finite query, not only in a comparison ball.
* The repeated-eigenspace argument in checkpoint 09 retains at least half of every squared b-component with probability at least 7/8. The intended equation in its Section 2 is simply min_{w in W} q_0(p(A_0)b_0+w) >= q_0(p(A_0)b_0)/2. The intermediate text 'min-free-expression' is a typographical artifact, not a mathematical operation; it is removed from the standalone manuscript.
* The Haar argument reveals at most one new query direction and one image direction per call. Fresh Gaussian reference directions enlarge the available information; they are not a linear-span restriction on the algorithm. An additional Gaussian direction accounts for an unqueried output. The distribution is fixed before the seed.
* In checkpoint 08, M=2 ceil(sqrt(T)) R_N is necessary: a constant multiple of R_N would not suppress the padding for every allowed charged query. Under the declared budget, all query paddings and their gradients vanish exactly. The output padding supplies a separate norm bound; no output charge is imposed.
* The reference-process union bound in checkpoint 08 conditions only on the revealed index prefix, never on previous good events. Its bound is 257/1024, leaving success probability 767/1024. Locality is exact inactivity, not a numerical smallness argument.
* The relative-noise upper proof in checkpoint 10 controls the variance at the actual extrapolated points through a_j^2 E f(y_j) <= A_K s+5D_j. The induction gives D_j<=3R^2/4 and KM<=K+48 sigma^2 K^2. It therefore retains the small-noise deterministic term rather than the slower projected-gradient term.
* The input-relative curvature pair in checkpoint 11 has k(x)=x-2min(x+2R_0,0), with |k(x)|<=|x| globally. Consequently its Gaussian statistical experiment is valid even at arbitrarily large queries. The midpoint bias field is also globally admissible.

The results still require independent mathematical review. Finite tests will be supplied as diagnostics, not as substitutes for these proofs.

## 4. Exact rational obstruction: what has and has not been proved

The rational quadratic-lift subclass is identified by one sufficiently small algebraic query, because its inactive padding leaves a rational linear gradient map and 1,alpha,...,alpha^D are linearly independent over Q. This invalidates a simple rationalization of the real hard family.

It does not identify every rational PSD-distance function. Piecewise spectral formulas can agree on open regions and differ elsewhere; the scalar-hinge examples in checkpoint 03 explicitly preclude a blanket analytic-identification argument. A universal disproof would need to handle this inactive-branch ambiguity. A positive exact rational theorem would instead need exact global masking that survives arbitrary queries without losing the required normalization and escape scales.

A potential radial spectral masking route was examined but not completed. Duplicating a radial Clifford block for every hidden constraint expends a direction-Gram budget proportional to the number of constraints. Normalizing it suppresses the local chain curvature and loses the desired rate. No theorem is claimed from this attempt, and no impossibility result for all conic masking constructions follows from it.

## 5. Required source reading completed

At baseline 22ed4becd320695b41f8a11f1223ea090ef89ecf, the complete contents of milestones 12, 26, 27, 38, 39, 40 and 00_MANUSCRIPT3_NOISE_PROFILE_STATUS.md have now been read, including continuation chunks omitted by the first truncated fetches. The complete flagship handoff has been reread. The older continuation-status file is a historical checkpoint, not the current reading ledger.

The compiler files 11 and 02 are not correctness premises: no universality or epigraph compiler is used in any new lower proof. Source milestones remain unchanged.

## 6. Novelty and benchmark status

The arbitrary-query-to-block-Krylov reduction is established prior methodology. In particular, Dereziński–Epperly–Meyer, arXiv:2602.04842, Appendix A.2, credits Chewi–de Dios Pont–Li–Lu–Narayanan, Query Lower Bounds for Log-Concave Sampling, Journal of the ACM 71(4), 2024, DOI 10.1145/3673651, Lemma 5.16. The standalone proof here is included for the fixed linear term and arbitrary-output accounting, not as a claim that the general reduction is new.

The predeclared twenty-paper journal sample remains fixed. Publisher full-text links often return abstract pages; accessible author manuscripts are being used where available, with version and proof-access limits recorded. Neither a top-quintile judgment nor an acceptance probability is established. The unresolved original rational/exact gate alone rules out claiming that the handoff's full success criterion has been met.
