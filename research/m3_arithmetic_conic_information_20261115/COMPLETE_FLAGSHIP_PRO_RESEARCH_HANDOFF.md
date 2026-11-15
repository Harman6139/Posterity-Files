# MANUSCRIPT III — GRAND UNIFYING PRO RESEARCH HANDOFF
## Arithmetic information at infinity: rational versus real conic oracle complexity, exact identification, and sharp precision limits

**Research handoff prepared 2026-11-15.** For a NEW independent high-effort Pro research chat. Research target is NOT an achieved theorem. Read all pinned checkpoints and primary references before attempting a proof.

## One-sentence flagship mission

Discover and prove ONE **arithmetic–information principle** explaining how matrix coefficient fields, active spectral branches, coordinate charts, unrestricted exact-real queries, finite arithmetic precision, and near-feasibility escape geometry interact to determine the true randomized oracle complexity of **genuine weakly infeasible semidefinite programs**.

The requested outcome is not merely a better lower bound for an engineered black-box convex function. It must resolve the **still-open rational-coefficient, free-radius, exact-value-and-gradient frontier** or provide a complete mathematical characterization of its failure and an equally consequential corrected theorem, while incorporating the already established REAL-coefficient minimax law and RATIONAL positive-error/charged-query laws as sharply distinguished cases of the SAME overarching insight.

A long collection of old separate sample/round/noise/precision formulas does NOT count as a grand unification. A renamed oracle, an arbitrary cap on query radii, or positive numerical noise silently substituted for exact information is not acceptable.

# I. Exact matrix and oracle objects

Fix a rational \(\beta>0\), preferably begin with \(\beta=1/2\), but aim for all rational \(\beta>0\). For matrix order \(m\), let
\[
X(x)=X_0+\sum_{i=1}^d x_i H_i\in\mathbb S^m,\quad
\langle H_i,H_j\rangle_F=\delta_{ij},
\tag{1}
\]
where all \(X_0,H_i\) are RATIONAL symmetric matrices for the central rational version, and \(x\in\mathbb R^d\) is the algorithm's coordinate query. The affine slice \(U=X_0+\operatorname{span}\{H_i\}\) must be **genuinely weakly infeasible**:
\[
U\cap\mathbb S_+^m=\varnothing,\quad
\operatorname{dist}(U,\mathbb S_+^m)=0.
\tag{2}
\]
Define the natural, coordinate-normalized objective
\[
\boxed{f(x)=\frac12\operatorname{dist}_F(X(x),\mathbb S_+^m)^2,\qquad
\nabla_i f(x)=\langle H_i,X(x)-P_{\mathbb S_+^m}(X(x))\rangle.}
\tag{3}
\]
It is globally convex and \(C^1\) with 1-Lipschitz gradient. It need NOT be globally \(C^2\). Distinguish the geometry of the affine slice from the **coordinate chart**, which is itself part of the input: a geometrically rational image with real hidden chart coefficients is NOT a rational-encoding oracle instance.

Normalize
\[
f(0)\le1,\quad \inf f=0\ \text{unattained},\quad
c_\beta s^{-\beta}\le\rho_f(s)\le C_\beta s^{-\beta}
\quad(0<s\le s_\beta),
\tag{4}
\]
with \(\rho_f(s)=\min\{\|x\|:f(x)\le s\}\). Constants and onset are fixed independently of query horizon, dimension, coefficient height and sampled instance.

**Exact natural oracle:** Given ANY finite real \(x\) (possibly an algebraic vector of very high degree and/or enormous norm), return the exact real pair \((f(x),\nabla f(x))\), and allow unlimited computation, randomness, exact equality tests and arbitrary unqueried output. Algorithm may know the entire input family, bit-height bounds, \(\beta\), oracle rules and profile constants, but not the hidden rational coefficients or chart. No charge for query size or real-number information under this base model.

If FULL rational matrix coefficients are explicitly supplied, the problem is a DIFFERENT input model: with unlimited computation the algorithm can solve the finite-dimensional rational semialgebraic instance from the supplied data without oracle queries. Never confuse black-box hidden coefficients and explicit SDP computation.

## II. Grand Theorem III — the central exact-rational frontier

Determine definitively which of the following is correct.

### Positive target: true rational exact-oracle hardness

Find, for at least one \(\beta>0\), a fixed prior over RATIONALLY ENCODED instances of (1)–(4), chosen BEFORE and independently of algorithm randomness, having dimension, PSD order and TOTAL coefficient bit length polynomial in the horizon \(T\), such that EVERY measurable randomized adaptive algorithm making \(T\) exact natural value-and-coordinate-gradient queries at arbitrary finite locations and returning an arbitrary point obeys
\[
\boxed{
\Pr_{\omega,\mathrm{alg}}\!
\left\{f_\omega(\hat x_T)\ge c_\beta(T+1)^{-2/(2\beta+1)}\right\}\ge2/3.
}
\tag{5}
\]
All constants uniform in \(T\). Prove exact oracle locality/indistinguishability, not an approximation at machine precision, and match with accelerated upper bound. For the strongest theorem, prove (5) for every rational \(\beta>0\), and quantify arithmetic height dependence.

### Equally valid negative target: information-theoretic exact rational collapse

Prove that the proposed fixed-distribution lower bound (5) is IMPOSSIBLE for the entire rational PSD-distance class under its declared strong exact-real oracle, by constructing a *uniformly budgeted identification/optimization procedure*, not merely one successful query on the known quadratic subclass. If full universal collapse is false, prove the sharp **spectral-stratification/identification theorem** characterizing the rational families for which it holds, and exhibit a genuinely hard family outside the characterization with sharp complexity.

A universal negative claim requires handling the PSD projection's **piecewise analytic eigenvalue branches**, including different rational instances that share an open set of exactly identical value/gradient responses. One generic algebraic query identifies a rational QUADRATIC, but not necessarily every rational PSD-distance function. One-query identification of a subfamily is NOT a universal disproof.

### The grand unifying principle

A flagship resolution should express an explicit, non-tautological **arithmetic spectral observability invariant or theorem**, not just an oracle decision tree definition. It should explain when an exact real-valued query functions as a fingerprint of hidden RATIONAL matrix coefficients, when inactive PSD spectral branches mask the fingerprint, and how the needed number/precision of queries is governed by cone geometry. It must connect this to the fixed escape profile (4), **not just to ordinary rational matrix recovery**.

The theorem must explain the **real vs rational vs positive-error** transition: the real-data hard family below works at zero noise, while its naive rationalization collapses under one exact query; for every POSITIVE error allowance a different rational hard prior has been proved. Determine what is universally true across this discontinuity, in the declared models. If sharp behavior depends on bit height \(L\), expose that dependence and prove a phase diagram \(N(\varepsilon,L,\zeta,\tau)\) or the correct information invariant. Do not assert continuity as \(\zeta\downarrow0\) without proving it; a minimax family may itself depend on the positive error budget.

# III. Current mathematical progress already proved in research checkpoints

Connected GitHub: **Harman6139/Posterity-Files**.

### Latest independent Manuscript III results branch

**Branch:** research/pro-m3-conic-oracle-frontier-20261114
**Verified HEAD:** 4dd59027dda0e5c5501b79d68248affdcf663e1e
**Directory:**
https://github.com/Harman6139/Posterity-Files/tree/4dd59027dda0e5c5501b79d68248affdcf663e1e/research/pro_m3_conic_oracle_20261114

READ ALL checkpoints 00–12, especially:

1. **01_RATIONAL_FIVE_BY_FIVE_NOISE_AND_BIAS_THEOREM.md**: exact rational low-dimensional PSD-distance family matching stochastic statistical or biased-gradient obstacles; never call this a noiseless sequential lower bound.
2. **02_PADDING_AND_RATIONAL_ESCAPE_LADDERS.md**: rational PSD isometry and escape-profile constructions with careful normalization.
3. **03_EXACT_ORACLE_MODEL_OBSTRUCTIONS.md**: four crucial facts:
   - antipodal quadratic budget: for any Frobenius-isometric linear coordinate map H, \( \lim_{t\to\infty}[f(tv)+f(-tv)]/t^2=\|v\|^2/2 \);
   - a rational quadratic \(q(x)=x^\top Ax/2+b^\top x+c\) is exactly recovered from one algebraic-gradient query with \(\alpha=2^{1/(d+1)}\) and inputs \((\alpha,\ldots,\alpha^d)\), by \(\mathbb Q\)-linear independence;
   - a complete rational affine embedding/projection oracle is even stronger and collapses the intended problem;
   - **counterexamples to universal one-query analytic-germ identification**: distinct rational PSD-distance objectives can agree on an OPEN region or even all exterior points, yet have disjoint core zero sets. This blocks false global extrapolations from the quadratic case.
4. **04_EXACT_STATISTICAL_EXPERIMENT_AND_BIAS_TRANSITION.md**: two-point and testing lower bounds; distinguish noise from exact values.
5. **05_EVERY_RATIONAL_ESCAPE_EXPONENT.md**: rational isometric conic tails with prescribed \(\beta\), uniform constants; no arbitrary tailoring of onset to T.
6. **06_HIGH_PROBABILITY_AND_RELATIVE_ERROR_THEOREMS.md**: relative variance and bias conic constraints.
7. **07_GLOBAL_ISOMETRIC_QUADRATIC_ORACLE_LIFT.md**: a globally exact query-by-query equivalence from a bounded-curvature quadratic matrix-vector oracle to a natural isometric PSD-distance oracle. Construction:
\[
X(x,z)=\operatorname{diag}\left(
\begin{bmatrix}0&(Cx-d)^\top\\Cx-d&0\end{bmatrix},
\begin{bmatrix}M&(Sx)^\top\\Sx&M I\end{bmatrix},
\begin{bmatrix}0&1\\1&z\end{bmatrix}\right),
\tag{6}
\]
with \(C^\top C=A\), \(S^\top S=I/2-A\). Then
\[
f(x,z)=\tfrac12\|Cx-d\|^2+\tfrac12(\|Sx\|-M)_+^2+\phi(z),
\quad\phi(z)=(\sqrt{z^2+4}-z)^2/8.
\tag{7}
\]
One matrix-vector product recovers natural value/gradient and vice versa FOR EVERY finite query, no comparison-ball qualification. The padding isometry is a key algebraic result, not a generic epigraph argument. Rational factorization and bit-height conditions must be independently checked.
8. **08_RADIUS_CHARGED_RATIONAL_MINIMAX.md**: a FIXED rational, polynomial-encoding hard distribution under explicit excursion charge \(w_\varepsilon(q)=1+\varepsilon^{2\beta}\|q\|^2\), with matching randomized complexity \(\Theta_\beta(\varepsilon^{-\beta-1/2})\). This is NOT free-radius unit-cost oracle complexity.
9. **09_UNRESTRICTED_REAL_CONIC_RANDOMIZED_FRONTIER.md**: full REAL-coefficient \(\mathbb S_+^m\)-distance randomized minimax lower bound:
\[
\Pr\left\{f(\hat x_T)\ge c_\beta(T+1)^{-2/(2\beta+1)}\right\}\ge7/8,
\tag{8}
\]
for all rational \(\beta>0\), arbitrary finite queries and arbitrary unqueried outputs, \(m,d=O_\beta(T^3)\). Fixed Haar frame before the algorithm seed; repeated eigenspaces and deferred orthogonal sampling prevent arbitrary exploratory queries from helping. The real orthogonal chart has genuinely NONRATIONAL coefficients; pretending the geometrically fixed rational slice supplies rational oracle input is a category error.
10. **10_SHARP_RELATIVE_NOISE_CROSSOVER.md**: matching relative-gradient noise and bias scales in both REAL free-radius and RATIONAL charged models:
\[
N=\Theta_\beta\left(\varepsilon^{-\beta-1/2}+\sigma^2\varepsilon^{-2\beta-1}\right),
\quad
\nu_{\rm critical}\asymp_\beta\varepsilon^{\beta+1/2}.
\tag{9}
\]
Do not equate gradient measurements with unbiased PSD-valued projection samples; PSD positivity imposes almost-sure kernel support constraints.
11. **11_RATIONAL_PRECISION_DISCONTINUITY.md**: RATIONAL polynomial-encoding hard family with unrestricted query radii and input-relative gradient measurement error
\[
\|b(q)\|\le\zeta(1+\|q\|),\quad
\mathbb E\|\xi(q)\|^2\le\tau^2(1+\|q\|)^2.
\tag{10}
\]
For EVERY positive \(0<\zeta\le c_\beta\varepsilon^{2\beta+1}\), a genuine fixed rational prior gives
\[
N=\Theta_\beta\left(
\varepsilon^{-\beta-1/2}+\tau^2\varepsilon^{-4\beta-2}
\right);
\quad \zeta_{\rm critical}\asymp_\beta\varepsilon^{2\beta+1}.
\tag{11}
\]
At \(\zeta=0\) the statistical term persists, but the original rational/noiseless sequential lower bound is NOT established. Its hard prior is allowed to depend on positive \(\zeta\) and encoding height. Exact population values are not returned.
12. **12_PROOF_AUDIT_AND_MODEL_BOUNDARIES.md**: most up-to-date scope and corrections. In 11, the lower distribution is over admissible FIXED problem–oracle pairs \((V,U)\) with deterministic field \(\nabla f_U\), each biased relative to true \(f_V\). Conditioning only on rational V to form a latent mixture may introduce conditional variance; the actual lower-bound quantifiers do NOT require that mixture to be a zero-variance oracle. Also confirms original 07–11 do not close the rational exact frontier, and 09's coordinate chart is real even if its affine image is rational. Review the independent proof audit and its open radial/Clifford spectral masking route.

**Beware:** 00_CONTINUATION_STATUS.md is a HISTORICAL initial checkpoint and not a current status summary. Do not overwrite current 12 with old 00.

### Original source / previous generic Manuscript III

Source branch: laa-track02-gptpro-analytic-frontier-20261112
Pinned source commit: 22ed4becd320695b41f8a11f1223ea090ef89ecf
Directory:
https://github.com/Harman6139/Posterity-Files/tree/22ed4becd320695b41f8a11f1223ea090ef89ecf/research/laa_two_basis_track02_20261112

Mandatory full reads:

- **12_RECIPROCAL_ESCAPE_LAW_AND_SHARP_DIMENSIONAL_BOUNDS.md**: semidefinite trace radius and general escape exponents; not oracle lower bounds.
- **26_ESCAPE_CONTROLLED_PROJECTION_DYNAMICS.md**: accelerated upper bounds and alternating projections.
- **27_MINIMAX_ORACLE_COMPLEXITY_WITHOUT_MINIMIZERS.md**: deterministic generic convex-function lower bound with uniform profile and full adaptive oracle.
- **38_RANDOMIZED_AND_PARALLEL_MINIMAX_NONATTAINMENT.md**: fixed Haar randomized and parallel generic \(C^2\) smooth-function hard distribution. NOT a genuine natural PSD-distance instance.
- **39_GENERAL_ESCAPE_PROFILES_NOISE_BIAS_AND_PARALLELISM.md**: broad regular-varying/doubling escape-profile classification, matching sample, round, absolute-bias scales. Exact population values absent in its noisy model. These claims are already established in the project; copying them alone is NOT a new breakthrough.
- **40_EXACT_VELOCITIES_AND_FINITE_ANGULAR_MOTION.md**: exact all-order SDP alternating-projection last-step/objective constants. An upper-bound transfer, not a conic oracle lower bound.
- **11_UNRESTRICTED_RATIONAL_TWO_BASIS_COMPILER.md**, **02_UNIVERSAL_QUADRATIC_TWO_BASIS_NORMAL_FORM.md**, only if needed. Their exact representation of feasible sets does not by itself preserve oracle transcripts; never invoke them as magical hardness compilers.

This handoff branch **research/m3-arithmetic-conic-information-grand-theorem-20261115** inherits the latest independent results commit **4dd59027dda0e5c5501b79d68248affdcf663e1e**.

## IV. Mandatory literature and priority work

Read actual theorem/proof statements, not just abstracts, and seek 2026 additions.

- Nemirovski–Yudin and Nesterov: first-order oracle models, resisting oracles, fixed-dimension and precision caveats.
- Woodworth–Srebro, Carmon–Duchi–Hinder–Sidford, Guzmán–Nemirovski: randomized hard functions and higher-order oracles.
- Dereziński–Epperly–Meyer, *The matrix-vector complexity of Ax=b*, arXiv:2602.04842 **version 4 (July 2026)**; read Appendix A.2 and the full randomized matrix-vector lower-bound mechanisms. The generic arbitrary-query-to-Krylov Gaussian augmentation was already known; checkpoint 12 cites related Chewi–de Dios Pont–Li–Lu–Narayanan, *Query Lower Bounds for Log-Concave Sampling*, JACM 71(4), 2024, DOI 10.1145/3673651, Lemma 5.16. Do not claim first invention of this reduction.
- Drori and later exact first-order performance estimation; Lan stochastic acceleration; Devolder–Glineur–Nesterov inexact oracle models and error floors. Noise statistics and corresponding information models must be checked.
- Pataki and weak SDP infeasibility/facial reduction; semialgebraic parametric spectral projection; rational matrix pencil identification and real algebraic decision tree/Blum–Shub–Smale models.
- Literature on algebraic real-number query encoding, bit/height bounded arithmetic, identifiability from gradients and spectral measurements. Our "rational quadratic one-query" lemma may be mathematically elementary but materially limits all lower-bound claims.
- Recent 2025–2026 results on finite-precision matrix–vector products and PSD projection oracle models. A lower bound for a value-and-coordinate-gradient oracle is not automatically one for a more informative full projection matrix oracle.

You MUST map novelty against each major known result; do not rebrand generic exact-real arithmetic or classic random-frame lower bounds as a new discovery.

## V. The unification: arithmetic spectral observability at the boundary

Attack these FIVE connected questions as one mathematical problem.

### Q1. Exact rational identification versus inactive spectral regions

For rational affine PSD-distance objectives (3), determine how many probes, what algebraic field/degree, and which spectral regions are needed to identify the function up to a globally sufficient accuracy. A countable set of rational inputs does not imply 1-query identification: two objectives can agree on an open ball and disagree elsewhere. Equally, the existence of inactive masks does not prove ANY dimension-growing fixed-prior lower bound against arbitrary adaptivity.

Seek a **nontrivial facial-stratification invariant**, e.g. algebraic continuation of PSD spectral branches, finite sign-pattern complexity, or an observability index defined by ranks of rational spectral derivatives and branch transitions, with a theorem bounding identification effort or proving information masking. Do not simply define it to equal the optimal query complexity.

### Q2. Zero versus arbitrarily small positive error

In exact real arithmetic a single answer may carry unbounded rational coefficient information. Under positive input-relative bias, the rationalized hard family can be indistinguishable from a real hard rotation at EVERY query because the difference is bounded by \(\zeta(1+\|x\|)\). Rigorously characterize how bit height \(L\), algebraic query degree, coefficient field and precision \(\zeta\) interact. If there is a critical \(\zeta_{\mathrm{crit}}(\varepsilon,L)\) or a phase transition in support size, derive it sharply with upper/lower constructions.

The checkpoint 11 statement uniform in all POSITIVE \(\zeta\) does not establish the \(\zeta=0\) endpoint or uniformity at a fixed bit-height cap. Treat those as hard issues, not notation.

### Q3. Genuine conic escape and algorithmic conditioning

The difficulty must come from the natural weakly infeasible \(f=\tfrac12\operatorname{dist}_{PSD}^2\) with uniform \(s^{-\beta}\) escape, not an unrelated quadratic plus a free unbounded coordinate that merely creates nonattainment without being part of a valid isometric pencil. Use checkpoint 07's *exact* isometric padding or derive a genuinely new spectral masking architecture preserving the oracle transcript and escape radius. Prove what information a huge query can reveal; unbounded probes are not allowed to be silently ignored.

### Q4. Algorithmic/precision alternatives

Provide matching constructive algorithms under the SAME information model that reaches the lower bound. If you prove a universal rational exact identification theorem, make it effective under declared computation/bit assumptions and explain the cost in bit height. If you prove positive rational hardness, compare with real-coefficient Haar and rational positive-error laws, including explicit coefficient encoding. If neither literal version holds uniformly, prove the sharp corrected classification by data class, bit budget or observation type, with a reasonable universal guarantee.

### Q5. Additional consequences beyond the single conic oracle model

A grand theorem should yield at least TWO independent consequences in mathematical optimization/information theory:
1. a concrete insight about exact arithmetic vs finite precision for rational **matrix-vector, spectral or matrix-sketch recovery** with proof of a new bound or distinction not already in existing literature; and
2. a true consequence for **PSD feasibility/ADMM/projection algorithms** in a carefully stated access model, e.g. exact versus inexact projected-gradient complexity, information leakage from full matrix projections, or a sharp structured measurement uncertainty threshold.

Do NOT assert implications for full explicit-input SDP solvers, deterministic polynomial bit complexity, or actual floating-point PSD projection noise that are not justified by the model.

## VI. Hard constraints — prevent beautiful but invalid proofs

1. A single exactly known **real** Haar rotation is not a rational encoding; even if its geometric slice/image is rational the coordinate chart can be real. A rational support claim must include the chart and its coefficient height.
2. A naive rationalization of the **quadratic** hard family is EXACTLY identifiable by one algebraic query. It cannot inherit the real lower bound under free-radius exact-real oracles.
3. Distinct rational PSD-distance objectives can coincide on nonempty OPEN regions, or even on all large-radius regions; a rational countable analytic-class argument does not yield universal 1-query recovery.
4. Do not choose hidden \(\omega\) AFTER seeing the algorithm's random seed. Fixed-prior high-probability lower bounds must survive randomized adaptive queries and unqueried outputs.
5. The natural \(f\) is generally \(C^1\) but not \(C^2\); do not apply exact-Hessian techniques without defining their domain and strong oracle properly.
6. An SDP representation of a generic smooth function does NOT automatically simulate its value/gradient oracle, preserve constant Lipschitz metrics or preserve radius geometry.
7. No hidden restriction on query norm. If you propose a radius charge or bounded-radius instrument, call it a **distinct corrected physical model** and prove why it is natural; it does NOT satisfy the original free-radius exact target.
8. No exact objective values in the stochastic/biased-gradient models unless explicitly declared. Exact \(f(x)\) could expose hidden parameters that noisy gradients cannot.
9. A deterministic oracle field \(\nabla f_U\) approximating true rational \(\nabla f_V\) with bounded bias is admissible; do not quietly mix out latent U and claim conditional variance zero unless justified.
10. Distinguish additive absolute bias, input-relative bias \(\zeta(1+\|x\|)\), relative-residual bias \(\nu\sqrt{f(x)}\), and PSD-valued projection samples. Different scaling laws are NOT contradictions.
11. If a "new" identification method relies on arbitrarily high algebraic degree or infinite exact equality tests, disclose it; it is NOT a polynomial-bit algorithm. Conversely, a bit-model lower bound cannot be applied to unrestricted exact-real oracle count without proof.
12. Explicitly verify weak infeasibility, uniform onset of the escape profile, isometry, correct dimensions, quantifier order, and both directions of any claimed oracle simulation.

## VII. Publication-quality target and upper-quintile test

**First level-up target:** *SIAM Journal on Optimization* (SIOPT) or *Mathematical Programming A*, but ONLY if the full exact-rational arithmetic frontier is closed by a substantive new structural insight. *Mathematics of Operations Research* (MOR) suits a broad conic information-model theory with a recognizable optimization interpretation; *Journal of Convex Analysis* (JCA) is a fit-first alternative. *Advances in Nonlinear Analysis* might fit if the result is genuinely broad convex/nonlinear asymptotic theory; *Advances in Applied Mathematics* needs a real algebraic/combinatorial application. Do not pick prestige while ignoring readership.

One flagship contribution, not a collection of technical lemmas: the new arithmetic–observability theorem must explain **why exact oracle complexity at infinity can differ discontinuously from arbitrarily accurate finite measurement**, or rigorously prove no such broad discontinuity survives after correct class/model normalization. It must have quantitative predictions for natural matrix classes.

The author's "80%+" means **defensible upper-20%-of-published-papers mathematical substance**, not ≥80% actual acceptance or desk-pass probability. To claim this goal passed:

- complete proof or exact counterexample + comparably consequential correct universal theorem, genuinely beyond milestones 38–39 and checkpoints 07–12;
- independently checked priority and mathematical validity, especially against 2026 randomized Krylov literature;
- at least **12 article-level published-paper benchmarks from SIOPT** and **10 each from MOR/JCA or any other proposed venue**, preregistered reproducible selection across two or more 2024–2026 issues and close topical controls; compare theorem content and proofs, not just abstracts, give DOI and access limitations;
- clear mathematical rubric: originality, depth, theorem strength, technical difficulty, breadth beyond matrix-cone specialists, relevance to optimization algorithms, and tractability of exposition. An 8/10 comparison must be actually substantiated; no automatic quality badge.
- realistic current submission-to-final-acceptance figures, if verified, and disclosure that an eight-month acceptance/no-revisions requirement cannot be promised. SIAM-wide historical mean acceptance has been reported around 10.5 months; verify venue-specific dates before making any timeline claim.
- self-contained main article aiming 20–30 pages with detailed technical supplement, including a complete explicit rational or real hard family, a single main theorem, a matching upper algorithm, and the exact conic oracle model.

## VIII. Concrete research plan and GitHub deliverables

### Priority 1 — decide the original rational exact frontier

Do not start by extending another stochastic theorem. Attack the **free-radius exact rational** formulation. The sharp obstacle is spectral identifiability: rational quadratics collapse by an algebraic probe, but natural PSD projection objectives may hide differences on open spectral strata. Find the structural distinction. Derive a rigorous theorem about whether a full rational PSD-distance family can hide against arbitrary real probes in high dimension.

### Priority 2 — one arithmetic-information invariant

Prove or refute a non-tautological characterization of exact spectral observability from value/gradient data in rational affine charts; relate it to the arithmetic and geometric scale in (4). Seek a theorem simultaneously explaining the real Haar hard family, the positive-error rational hard family, and any actual exact-rational complexity law.

### Priority 3 — broader consequence and manuscript

Derive a meaningful corollary beyond the original lower-bound construction. Build a small exact rational example demonstrating the predicted branch or precision phenomenon and an all-order family giving sharpness. Write the paper.

**Work on an INDEPENDENT results branch**, recommended research/pro-m3-grand-arithmetic-observability-20261115, created from checkpoint 12's commit **4dd59027dda0e5c5501b79d68248affdcf663e1e**. Preserve source checkpoints and do NOT overwrite them.

Required output files:

1. **ARITHMETIC_SPECTRAL_OBSERVABILITY_THEOREM.md** — full exact structural theorem, including possible counterexample and correct replacement.
2. **RATIONAL_EXACT_CONIC_FRONTIER.md** — complete positive lower-bound proof OR universal disproof/classification with exact quantifiers; not a model-switched proxy.
3. **REAL_RATIONAL_PRECISION_PHASE_DIAGRAM.md** — unify actual proved outcomes (real, rational-precision, rational-charged) and any new endpoint theorem, with constants, coefficient bit-height and correct assumptions.
4. **CONIC_APPLICATIONS_AND_SHARPNESS.md** — two independently meaningful applications, exact spectral examples and matching bounds.
5. **HISTORICAL_PRIORITY_AND_2026_LITERATURE.md**, **PUBLISHED_PAPER_BENCHMARK.md**, **STATUS_PROVED_FALSE_OPEN.md**, and a submission-ready **main.tex** with full technical source and reproducibility scripts. Commit checkable proofs incrementally; code is supporting evidence, never mathematical proof.
6. Exact GitHub results branch and verified commit SHA; no false claims of background work or inability to access an unuploaded local file.

### Final success criterion

**Resolve the complete rational/real oracle arithmetic frontier at infinity with one new structural mathematical principle** that connects natural semidefinite distance functions, exact spectral information, fixed-prior randomized complexity, coefficient arithmetic and sharp finite-precision limits.

If the original rational exact lower bound is FALSE, a rigorous universal disproof plus a sharp useful corrected theorem is a full mathematical success. If it is TRUE, the exact rational construction and proof are required. If neither is proved, preserve all valid progress and say explicitly that the flagship goal remains open.

**Possible target abstract, NOT currently established:**

> "A new arithmetic spectral observability invariant determines the randomized query complexity of weakly infeasible semidefinite systems, explaining the sharp transition between exact rational information and finite-precision matrix measurements and yielding optimal complexity laws in natural conic models."

Do not report that abstract as a result unless the entire theorem, applications, and novelty gates are really proved.
