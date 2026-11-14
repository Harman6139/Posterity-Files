# PRO RESEARCH HANDOFF 03 — OPTIMAL ORACLE COMPLEXITY FOR GENUINELY CONIC FEASIBILITY AT INFINITY
**Prepared 2026-11-14.** Independent fresh Pro chat. Research Track III of three. Read the full source packet before inventing a proof.

## A. The exact proposed breakthrough, beyond an abstract smooth oracle

Manuscript III has already obtained sharp dimension-uniform lower and upper bounds for arbitrary unknown smooth convex objectives with unattained minima, including randomized algorithms, exact Hessian locality, parallel round bounds, stochastic sampling, and systematic gradient bias. Its publication bottleneck is that the hard objectives are engineered black-box convex functions, **not a natural class of actual semidefinite feasibility problems**.

Your hard target is a sharp **conic-realizability / oracle-hardness theorem**. For every horizon \(T\) build, or prove impossible in the declared model, a fixed distribution over rationally described weakly infeasible semidefinite feasibility problems whose squared-distance objectives are genuinely hard to optimize by randomized adaptive local information.

Let the conic data be
\[
U_\omega=X_{0,\omega}+\mathcal L_\omega\subseteq\mathbb S^{m(T)},\qquad
K=\mathbb S_+^{m(T)},\qquad
U_\omega\cap K=\varnothing,\quad\operatorname{dist}(U_\omega,K)=0.
\]
Parametrize \(U_\omega\) isometrically by \(X_\omega(x)=X_{0,\omega}+\sum_{i=1}^{d(T)}x_i H_{\omega,i}\), where the \(H_{\omega,i}\) are Frobenius orthonormal, and define the **natural conic distance objective**
\[
\boxed{f_\omega(x)=\tfrac12\operatorname{dist}_F(X_\omega(x),\mathbb S_+^{m(T)})^2.}\tag{III-function}
\]
This is convex \(C^1\), 1-gradient-Lipschitz in the orthonormal affine coordinates; its infimum is zero and unattained. The gradient is the affine-coordinate projection of \(X-P_K(X)\). It need not be \(C^2\) at eigenvalue multiplicities; do not assert unsupported \(C^2\) regularity or freely insert a smooth surrogate that is no longer conic.

### Target Theorem III (conic oracle lower bound)

For at least **one fixed rational \(\beta>0\)** (preferably \(\beta=1/2\), the natural order-two weak-infeasibility exponent, and ultimately for a useful range), construct such a distribution with:

1. **Uniform escape geometry:** the minimum near-optimum radius
\[
\rho_{f_\omega}(s)=\min\{\|x\|: f_\omega(x)\le s\}
\]
satisfies \(c_\beta s^{-\beta}\le\rho_{f_\omega}(s)\le C_\beta s^{-\beta}\) for all \(0<s\le s_\beta\), with constants and onset independent of \(T\), dimension and sampled instance. Normalize \(f_\omega(0)\le1\).
2. **Genuine fixed-distribution randomized hardness:** for every randomized adaptive algorithm given only exact queries \((f_\omega(x),\nabla f_\omega(x))\), with arbitrary finite query locations, unrestricted computation and an arbitrary unqueried output, after \(T\) queries,
\[
\boxed{\Pr_{\omega,\mathrm{alg}}\{f_\omega(\widehat x_T)\ge cT^{-2/(2\beta+1)}\}\ge2/3.}\tag{III}
\]
The hard \(\omega\) is drawn before the algorithm's seed. A resisting rotation chosen after observing the seed is NOT a randomized lower bound.
3. **Matching conic upper bound** from an actual stated first-order / projection procedure, at the same oracle strength. Derive exactly how \(f_\omega=\frac12\mathrm{dist}_K^2\) translates into feasibility residual and matrix escape.
4. **A meaningful model interpretation:** distinguish a black-box **unknown** conic instance from an explicitly supplied matrix input. With unrestricted computation and FULL explicit input, an oracle-call lower bound may be vacuous, since the algorithm can algebraically solve the given finite-dimensional system without calls. If you include full explicit input, use a real computational bit/complexity model and prove a nonvacuous assertion. State dimension and bit lengths of the distribution; polynomial rational encodings would be especially significant.
5. **Noise/precision extension, if the central theorem is proved:** show whether the same CONIC class realizes the sharp sample and bias scales \(\varepsilon^{-\beta-1/2}+\sigma^2\varepsilon^{-2\beta-2}\) and \(\nu_{\rm crit}\asymp\varepsilon^{\beta+1}\) under a precisely defined noisy **conic-gradient/projection oracle**, with exact oracle indistinguishability constructions. Do not import the unconstrained noise lower bound without a conic realization.

A complete result for one nontrivial fixed \(\beta\) with truly uniform constants and a fixed random distribution would already be a major bridge from abstract oracle information theory to recognized semidefinite algorithms. A universal theorem for an interval of attainable escape exponents or a finite-precision phase diagram would be a further journal-level upgrade.

The model itself may make the full conjecture false: e.g. spectral gradients at a single large query could reveal hidden affine directions, or even make the oracle minimax problem trivial because query magnitudes are free. **Check this obstacle analytically.** If a universal conic lower bound of form (III) is impossible under the specified access, exhibit the exact algorithmic disproof and then fully solve the corrected natural conic oracle frontier (for instance a properly charged radius, bit, or projection-access model). Do not re-label a counterexample to the abstract class as the desired conic result. Do not weaken arbitrarily bounded query magnitudes without introducing a justified physical cost model and explaining what changes.

## B. Existing full source packet

Connected GitHub: Harman6139/Posterity-Files.
Immutable baseline source commit **22ed4becd320695b41f8a11f1223ea090ef89ecf**.
Branch laa-track02-gptpro-analytic-frontier-20261112; source directory:
https://github.com/Harman6139/Posterity-Files/tree/22ed4becd320695b41f8a11f1223ea090ef89ecf/research/laa_two_basis_track02_20261112

Mandatory complete reading:

- **27_MINIMAX_ORACLE_COMPLEXITY_WITHOUT_MINIMIZERS.md**: deterministic all-query lower bound with weighted quadratic zero-chain + positive decreasing tail. Uniform escape radius \(\rho(s)\asymp s^{-\beta}\), and exact achievable exponent \(2/(2\beta+1)\).
- **38_RANDOMIZED_AND_PARALLEL_MINIMAX_NONATTAINMENT.md**: stronger fixed Haar-frame distribution chosen before algorithm randomness; hidden C2 sparse max with exact locality, radial exterior hiding huge queries, high-probability randomized and parallel round lower bounds for arbitrary query/output. Important: its hard function is NOT shown to be a squared PSD distance.
- **39_GENERAL_ESCAPE_PROFILES_NOISE_BIAS_AND_PARALLELISM.md**: normalized classes with a fixed doubling escape profile \(r(s)\), and matching generic smooth-gradient oracle costs:
\[
\begin{aligned}
N_{\rm samples}(\varepsilon)&=\Theta(r(\varepsilon)/\sqrt\varepsilon+\sigma^2r(\varepsilon)^2/\varepsilon^2),\\
T_{\rm rounds}(\varepsilon,B)&=\Theta(r(\varepsilon)/\sqrt\varepsilon+\sigma^2r(\varepsilon)^2/(B\varepsilon^2)),\\
\nu_{\rm critical}(\varepsilon)&=\Theta(\varepsilon/r(\varepsilon)).
\end{aligned}
\]
Stochastic and bias lower bounds use explicit **two-dimensional** Gaussian-testing/convex-surrogate pairs. No exact true population values in its noisy oracle. The sequential lower bound even tolerates exact Hessians because unrevealed functions agree on a neighborhood, but no uniform Lipschitz Hessian is assumed. These generic results must not be misattributed as new conic lower bounds.
- **26_ESCAPE_CONTROLLED_PROJECTION_DYNAMICS.md** and **40_EXACT_VELOCITIES_AND_FINITE_ANGULAR_MOTION.md**: the already established exact alternating-projection rates for all weakly infeasible SDP orders, and last-step/objective leading terms when the total convex objective is semialgebraic. In the affine PSD squared-distance setting, minimum trace escape \(R_b(\delta)\asymp\delta^{-\alpha}\) gives \(\rho_f(s)\asymp s^{-\alpha/2}\). There is a 2x2 example with \(\alpha=1\), hence \(\beta=1/2\).
- **12_RECIPROCAL_ESCAPE_LAW_AND_SHARP_DIMENSIONAL_BOUNDS.md**: static conic profile / approximate Farkas duality, hyper-feasible recession support, sharp dimensional envelopes. Useful structural control, but NOT an oracle lower bound.
- **11_UNRESTRICTED_RATIONAL_TWO_BASIS_COMPILER.md** and **02_UNIVERSAL_QUADRATIC_TWO_BASIS_NORMAL_FORM.md** if attempting a universality embedding: verify whether their quotient transformations preserve the required black-box oracle complexity, noise and normalization. A lift equality alone does not preserve query information.
- **00_MANUSCRIPT3_NOISE_PROFILE_STATUS.md**: precise claimed scope and exclusions.

Relevant primary literature (research the current as-of-submission state): Nemirovski–Yudin and Nesterov on oracle lower bounds; Drori's exact complexity; Guzmán–Nemirovski; Carmon/Duchi/Hinder/Sidford on lower bounds and randomized high-order oracles; Woodworth–Srebro randomized lower bounds; Lan on accelerated stochastic optimization; Devolder–Glineur–Nesterov inexact oracle; Liu–Ryu–Yin on pathological conic programs; Pataki and facial-reduction/weak-infeasibility theory. Do a novelty matrix, particularly distinguishing "smooth hidden function represented by SOME SDP epigraph" from the REQUIRED **natural PSD-distance squared** objective. No artificial representation that leaks the hidden frame is allowed to count without proof of preserved information restrictions.

## C. Publication and >=80th-percentile quality gate

The ambition is to move Manuscript III from a legitimate convex-analysis paper to an optimization-theory flagship. **SIAM Journal on Optimization (SIOPT)** is the level-up target; **Mathematics of Operations Research (MOR)** is an alternative if the conic instance is a recognizable OR model. **Journal of Convex Analysis (JCA)** is the current fit-first fallback, and **Advances in Nonlinear Analysis** is relevant only if the result is a broad nonlinear-analysis theorem beyond black-box optimization. **Advances in Applied Mathematics** should not be targeted without a genuine discrete/combinatorial structural application. SIOPT typically targets 25-page manuscripts and SIAM-wide mean acceptance time has been reported around 10.5 months, so the user's strict eight-month preference creates a conflict; explicitly state it rather than promising an impossible timing guarantee.

The user wants a defensible **top-quintile published-paper benchmark** ("80%+") NOT an invented ≥80% desk-acceptance probability. A success claim requires:

* A new exact conic theorem with rigorous hypotheses and proof, fixed distribution and correct random-seed quantifiers, matching achievability, and honest access/complexity model; if impossible, a complete precise negative resolution and corrected nontrivial universal frontier.
* A primary-source novelty comparison, including all recent 2024–2026 oracle and conic literature, separating existing stochastic acceleration, spectral projection, random rotations, testing and error-bound results from genuinely new math.
* For each proposed journal, a **predeclared reproducible sample of at least 10 published papers** from two or more recent issues plus nearest-neighbor topical papers; read full results and technical proofs where possible, supply DOIs and math-level comparisons. Compare correctness, genuine novelty, breadth, depth, direct applications, and exposition. Only assign provisional upper-quintile status if the manuscript earns a defensible ≥8/10 comparison AND passes proof/priority gates. This is not a statistical editorial acceptance rate.
* A coherent standalone manuscript with a clear abstract, exact theorem hierarchy, a motivating weakly infeasible SDP example, proof of the hardest oracle lower-bound step, matching algorithm, an exact scope table, and reproducible code. If 25 pages is unrealistic, supply a clean main text and rigorous online supplement.
* Current venue fit and sourced real submission-to-acceptance evidence; honor user's eight-month preference, without a false assurance of revisions-free acceptance.

## D. Mathematical attack instructions

Focus on an ANALYTICAL invariant, not brute-force testing small SDPs. Think about which Euclidean projections onto PSD retain or destroy the exact "inactive hidden coordinates" locality of the 38 construction; whether matrix spectral gaps can implement a smooth hidden max; whether unbounded query radii necessarily leak information; whether a controlled lifted affine image can preserve \(\rho_f\) and the oracle transcript up to exact scaling. For every candidate reduction, prove query-level simulation both ways if claiming an oracle lower bound.

Avoid these false shortcuts: (i) "the two-basis compiler is universal, so oracle hardness transfers"; (ii) "randomized means choose a hard rotation after observing the seed"; (iii) "black-box lower bound rules out explicit-data SDP solvers"; (iv) "gradient-noise impossibility follows from exact-value oracles"; (v) "a high-order lower bound survives C2 smoothing without checking eigenvalue multiplicities." Explicitly confront them.

Do not stop after a smaller theorem or extra SDP example. Try to solve the full conic-oracle frontier in the current research effort. If genuinely unresolved, report the exact obstruction and do not claim the 80th-percentile goal was met.

## E. Required final artifacts

Create an independent results branch, e.g. research/pro-m3-conic-oracle-frontier-20261114. Deliver a fully proved positive theorem or a complete rigorous negative/characterization theorem, comparison of oracle models, a self-contained submission-quality .tex paper, code and exact test data that support (not replace) proofs, DOI-based originality audit, at least two ten-paper journal benchmarks, and a transparent final status. Keep source milestones 01–40 immutable. If writes are not possible, create uploadable files.

**Success criterion: a major optimization theorem that REALLY applies to a natural conic algorithm model, with a defensible journal-level top-quintile comparison. Abstract generic smooth hard functions alone do not pass.**
