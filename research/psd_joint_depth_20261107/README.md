# Universal PSD stability / joint exponent-depth research (2026-11-07)

**Current deliverables**
- [01_CANONICAL_GREEDY_DEPTH.md](01_CANONICAL_GREEDY_DEPTH.md): self-contained proof of the **previously known** maximal-rank/relative-interior stress method for minimal facial reduction; included to define a canonical depth test, not claimed novel.
- [02_ALL_DEPTHS_INTERIOR_REALIZATION.md](02_ALL_DEPTHS_INTERIOR_REALIZATION.md): explicit sparse PSD midpoint graphs realizing every rational \(2^{-d}\le\alpha<1/2\) with **exact** minimal singularity degree \(d\ge2\) in finite (not necessarily optimal) dimension; rank \(r\ge1\).
- [03_FINITE_JOINT_ALL_DEGREES_DECISION.md](03_FINITE_JOINT_ALL_DEGREES_DECISION.md): necessary-and-sufficient **finite real-algebraic** decision procedure for occurrence of every sharp exponent at fixed \((n,r,d)\), via finite weighted flags combined with the canonical depth predicate on the **same dense kernel**. Not a closed arithmetic formula and no efficient complexity claim.
- [04_EXACT_LADDER_CHECK.py](04_EXACT_LADDER_CHECK.py): exact-rational reproducibility test; no floating-point evidence used as proof.

## Results vs unresolved

**Proved in this packet** (conditional only on the previously proved weighted-flag structural theorem recorded in the parent project): a universal terminating decision algorithm for all fixed triples, and a new unrestricted-dimension all-depth constructive realization theorem below one-half.

**Not proved**: the stronger equivalence mapping each dense instance into a sparse midpoint network preserving exponent, nullity *and* exact minimal facial depth; a closed arithmetic/combinatorial formula for every fixed triple; optimal nullity for a general prescribed \((\alpha,d)\); and whether exponent exactly \(1/2\) is possible at \(d\ge3\). Do not infer absence from unsuccessful sparse search.

**Prior-art attribution**: maximal-rank greedy facial reduction is standard (see Sremac–Woerdeman–Wolkowicz, *Error Bounds and Singularity Degree in Semidefinite Programming*, SIAM J. Optim. 31 (2021), doi:10.1137/19M1289327; see also literature on relative-interior exposing vectors). Semialgebraic quantifier elimination, Puiseux selection and Sturm's depth error bound are also established, not novel.

**Safeguard**: these are research proofs requiring independent specialist review before declaring a journal-level new theorem or priority. The decision theorem avoids the unproved dense-to-sparse depth preservation, but uses exact-algebraic feasibility and therefore may be expensive.
## 2026-11-07: universal extremal structural breakthrough
- [05_UNIVERSAL_DYADIC_RIGIDITY.md](05_UNIVERSAL_DYADIC_RIGIDITY.md): universal feedback-cycle necessity for non-dyadic sharp exponents; extremal `alpha=2^(-nullity)` forces unique dyadic kernel-weight spine and maximal singularity degree; every odd-numerator dyadic `a/2^nu` has a **simultaneously dimension-minimal and facial-degree-minimal** explicit PSD realization, for arbitrary target rank.
- [06_DYADIC_BISECTION_CHECK.py](06_DYADIC_BISECTION_CHECK.py): exact Fraction construction and peeling audit (511 cases, nullity 2..10).
- These are structural results for **all dense kernels on the necessity side**, but they DO NOT prove the general sparse-network/dense-depth equivalence for every rational exponent. The endpoint alpha=1/2 at depth >=3 remains unresolved. No novelty claim is made for determinant combinatorics or generic facial reduction in isolation.


## 2026-11-07: universal canonical Dikin–Hessian classifier — main breakthrough

- [07_DAG_PEELING_RECURRENCE.md](07_DAG_PEELING_RECURRENCE.md): exact recurrence for minimal singularity degree of acyclic sparse midpoint-network realizations; not a dense-depth preservation theorem.
- [08_QUADRATIC_DUAL_JET_DEPTH2.md](08_QUADRATIC_DUAL_JET_DEPTH2.md): a polynomial dual stress jet characterization of depth at most two; its application to the alpha=1/2 high-depth endpoint remains open.
- [09_CANONICAL_LOGDET_LOEWNER_ENVELOPE.md](09_CANONICAL_LOGDET_LOEWNER_ENVELOPE.md): for every bounded PSD affine fibre, one canonical maximum-determinant center yields a *uniform Loewner upper envelope* for all residual competitors, with matching values for every PSD observable.
- [10_UNIVERSAL_DIKIN_HESSIAN_CLASSIFIER.md](10_UNIVERSAL_DIKIN_HESSIAN_CLASSIFIER.md): **PROVED UNIVERSAL STRUCTURAL THEOREM.** For any uniquely recoverable PSD pair (L,X*), with K=ker L, let X_e be the unique maximum-determinant point in X*+e I+K and lambda_e the smallest logdet-barrier Hessian eigenvalue on K. Then the exact full Frobenius recovery modulus obeys
      omega(||L I|| e) = Theta(e + lambda_e^(-1/2)).
  Valid for arbitrary dense maps, all target ranks, all minimal facial-reduction degrees, and all ambient PSD competitors; two-sided bounds have a complete proof. The exponent is the order of this single eigenvalue along an algebraic curve. This avoids the open depth-preserving sparse reduction.
- [11_SYMBOLIC_DIKIN_TESTS.py](11_SYMBOLIC_DIKIN_TESTS.py): exact symbolic checks recovering exponents 1, 1/2 and 1/4, including a nontrivial quarter-power algebraic center.
- [12_DETERMINANT_RATIO_INVARIANT.md](12_DETERMINANT_RATIO_INVARIANT.md): stronger **single scalar polynomial contact formula**: omega(||L I|| e) = Theta(e + det(X_e)*sqrt(e_(k-1)(A(X_e))/det(A(X_e)))), where A_ij(X)=tr(adj(X) H_i adj(X) H_j) for a Frobenius-orthonormal basis of K. Thus no Hessian eigenvalue optimization is needed in the final algebraic invariant.

**Careful scope:** The canonical Dikin–Hessian theorem *does solve the instance-wise universal structural classification*, for every dense pair and every singularity degree, with complete arbitrary-competitor bounds and matching constructive Dikin perturbations. The **different problem** of a simple closed arithmetic list of all simultaneous (n,r,d,alpha) realizations, including potential alpha=1/2 at depth >=3, is NOT resolved by this theorem. The general joint existence question remains decidable by the real-algebraic algorithm of checkpoint 03. Novelty/priority of the analytic-center/Dikin methods themselves is not claimed; the specific modulus formula needs specialist literature review.


## 2026-11-07: general cone extension and complete algebraic joint compatibility

- [13_ALL_SYMMETRIC_CONES_DIKIN_STABILITY.md](13_ALL_SYMMETRIC_CONES_DIKIN_STABILITY.md): complete proof that the universal Dikin–Hessian sharp recovery-modulus theorem extends to **every symmetric cone**, via Euclidean Jordan algebra quadratic representations. Covers Lorentz cones, real/complex/quaternionic PSD, the exceptional Jordan cone, and direct products. This is beyond PSD and does not assume sparsity.
- [14_ALL_DEGREE_JOINT_ALGEBRAIC_COMPATIBILITY.md](14_ALL_DEGREE_JOINT_ALGEBRAIC_COMPATIBILITY.md): **complete all-degree joint membership theorem**, using only the canonical center/determinant ratio and exact facial-reduction chain polynomial predicates. For any integers (n,r,d) and rational alpha, a finite real-algebraic sentence decides whether such a uniquely solvable PSD recovery instance exists. No weighted-flag or sparse-depth conversion assumptions needed. It is a **finite terminating decision procedure**, not a closed arithmetic list of the spectra.

**Final mathematical status:** An exact intrinsic structural classifier of the sharp Frobenius exponent for every individual arbitrary dense PSD problem is now established, as well as its extension to every symmetric cone, constructive lower-spectrum realizations, and an all-degree exact algebraic joint membership procedure. Explicit optimal-dimension arithmetic formulas *simultaneously* conditioned on every d, and the sparse-network depth-preservation equivalence, are not proved. Bibliographic priority must be separately audited; standard self-concordant barrier and Dikin facts are not new.


## 2026-11-07: bounded nonsingleton feasible sets — exact extension
- [15_NONSINGLETON_SET_DISTANCE_AND_DEPTH.md](15_NONSINGLETON_SET_DISTANCE_AND_DEPTH.md): chooses the relative-interior maximal-rank feasible X0, gauges away N=ker L∩S(range X0), proves the augmented singleton problem has **identical sharp set-distance exponent AND identical minimal facial-reduction degree**. Explicit two-sided modulus comparisons are proved for every ambient PSD competitor. Applying checkpoint 10 to the gauged problem gives a universal canonical Dikin–Hessian structural classifier for all bounded nonsingleton PSD feasibility problems.


## 2026-11-07: exhaustive exact all-degree spectrum enumeration
- [16_FINITE_EXHAUSTIVE_ALL_DEGREE_SPECTRA.md](16_FINITE_EXHAUSTIVE_ALL_DEGREE_SPECTRA.md): **proved** a computable finite rational candidate set at fixed (n,r), using a bounded-degree polynomial description of the unique canonical center determinant-ratio graph and an elementary two-monomial/Newton-polygon valuation bound. Running the checkpoint 14 real-algebraic compatibility test on the finite candidates yields the **entire** joint spectrum Σ_(n,r,d) for each fixed n,r,d. It is fully terminating and exact but may be astronomically expensive; it does not give a simple closed arithmetic list or resolve questions uniformly over unbounded n.


## 2026-11-07 — new closed combinatorial milestones (do not extrapolate to dense kernels)

- [17_MAXIMAL_DEPTH_RECIPROCAL_SPECTRUM.md](17_MAXIMAL_DEPTH_RECIPROCAL_SPECTRUM.md): **proved** the exact closed arithmetic exponent spectrum for sparse harmonic midpoint PSD systems at maximal singularity degree d=nu: all reciprocals 1/q and 1/(2q) for nu<=q<=2^(nu-1). Necessity via one-vertex-per-step peeling and positive integer gap recurrence; sufficiency via an explicit binary-halving induction producing every denominator. Applies to all positive target ranks (append a fully measured positive block). Does NOT prove dense necessity.
- [18_MAX_DEPTH_RECIPROCAL_GENERATOR.py](18_MAX_DEPTH_RECIPROCAL_GENERATOR.py): exact rational generator and peeling verification for 4,028 constructions (nu=2..12). Independent exhaustive comparison with the prior generic sparse enumerator matches through nu=6.
- [19_SHARP_DEPTH3_NULLITY_GAP.md](19_SHARP_DEPTH3_NULLITY_GAP.md): **proved** a sharp fixed-nullity gap for *all sparse harmonic systems at depth >=3*: alpha <= (2^(nu-2)-1)/(2^(nu-1)-1)<1/2 for nu>=3, attained at exact depth 3 by the feedback ladder. Equivalently, sparse degree >=3 iff the minimum internal harmonic weight is <1/2. A probabilistic source-absorption path supplies the sharp bound. Not yet a theorem for arbitrary dense PSD systems.

**Current unsolved universal upgrade:** show a dense PSD instance of degree d>=3 must have a sharp harmonic certificate with a genuinely sub-1/2 internal weight (or derive another dense stress-flag obstruction). The earlier exponent-preserving weighted-flag extraction does not automatically preserve degree.


## 2026-11-07: universal **dense** joint-depth classification at nullity three

- [20_UNIVERSAL_DENSE_NULLITY3_DEPTH3.md](20_UNIVERSAL_DENSE_NULLITY3_DEPTH3.md): NEW theorem holding for **all arbitrary dense** PSD measurement kernels: if target nullity nu=3 and minimal singularity degree d=3, then the optimal full-state recovery exponent satisfies alpha<=1/3. Proof requires only the two exposing stress stages plus elementary primal–dual linear-algebra; constructs a genuine cubic-residual PSD arc using two kernel modes. Combined with established nullity-three unconditional exponent spectrum and degree-two classification, derives **complete dense joint spectra**: d1={1,1/2}, d2={1/2,3/8,1/4}, d3={1/3,1/4,1/6,1/8}. No unproved dense-to-sparse depth preservation is invoked for the new upper bound. Includes an explicit 4x4 nonsparse kernel and sharp PSD curve.
- [21_DENSE_NULLITY3_SYMBOLIC_AUDIT.py](21_DENSE_NULLITY3_SYMBOLIC_AUDIT.py): passed exact SymPy validation of that curve's principal minors, kernel relations and three dual exposing stresses.

**Precise frontier:** the corresponding closed joint spectrum at nu>=4, arbitrary d, remains unsolved; the sparse maximal-degree formula and sparse high-degree gap are not yet universal necessity results. This checkpoint *does* validate dense compatibility in the first nontrivial case, rather than relying on sparse peeling.


## 2026-11-07: universal dense maximal-depth theorem in **all dimensions**

- [22_UNIVERSAL_MAXIMAL_DEPTH_INVERSE_NULLITY_BOUND.md](22_UNIVERSAL_MAXIMAL_DEPTH_INVERSE_NULLITY_BOUND.md): NEW THEOREM for every arbitrary dense uniquely solvable PSD inverse problem with positive target rank and nullity nu≥2. If the minimal facial-reduction degree is maximal, d=nu, then **alpha≤1/nu**. The bound is universally sharp, attained by explicit rank-one sparse chains at every nu. The proof builds, for each nested face, a kernel matrix with a positive new diagonal and a vanishing adjacent cross-block, forced by maximal minimal facial degree; a coefficient-rescaling lemma produces a genuine positive definite polynomial perturbation of displacement t and residual t^nu. This proves the *exact largest possible exponent* at fixed (nu,d=nu) for all dense maps, without any unproved depth-preserving network equivalence. It does not yet prove the entire reciprocal arithmetic set of sparse exponents is universal.


## 2026-11-07: universal primal–dual alignment and rank-sensitive arithmetic obstruction

- [23_FIRST_STRESS_ALIGNMENT_DENOMINATOR.md](23_FIRST_STRESS_ALIGNMENT_DENOMINATOR.md): **PROVED for every dense PSD map**: the range of each first PSD exposing stress is contained in the *terminal (highest-order) null valuation block* of any sharp PSD arc. Thus if s1 is the rank of the maximal first exposing stress, the reduced denominator b of 2alpha obeys the improved necessary bound **b<=2^(nu-s1)**. Equality forces an acyclic dyadic harmonic network, unit-dimensional earlier null weight blocks and terminal dimension exactly s1. This is a joint geometric/arithmetic constraint; it does not prove complete dense depth-preserving sparse universality.


## 2026-11-07: full dual–primal dyadic stress filtration for arbitrary dense maps

- [24_ALL_STAGES_DUAL_PRIMAL_DYADIC_FILTRATION.md](24_ALL_STAGES_DUAL_PRIMAL_DYADIC_FILTRATION.md): NEW universal structural theorem for **every** exposing step of **every** PSD facial-reduction chain. Along a sharp orthogonal null-valuation flag (weights 0<wi<=1), the total subspace F_j removed by the first j stresses must lie in the sum of primal valuation blocks with weights >=2^{-(j-1)}. Consequently, if s1,...,sd are the ranks removed at successive steps, then for each j the number of null coordinates with weight <2^{-(j-1)} is at most nu-(s1+...+sj). This is a finite **rank-profile/valuation-weight combinatorial obstruction** valid for dense maps without sparse reduction, refining the usual depth-only constraint and the first-stress denominator bound. It is necessary, not sufficient, for a full joint classification.


## 2026-11-07: canonical central dual stress **automatically** recovers greedy facial reduction

- [25_CANONICAL_CENTRAL_DUAL_RECOVERS_GREEDY_STRESS.md](25_CANONICAL_CENTRAL_DUAL_RECOVERS_GREEDY_STRESS.md): NEW self-contained theorem: along the unique shifted maximum-determinant center X_epsilon for ANY dense PSD recovery map, the bounded dual matrix Z_epsilon=epsilon X_epsilon^-1 converges to a **maximum-rank** PSD first exposing stress in K^perp. Proof uses the exact logdet trace stationarity identity, a maximal-rank stress's O(epsilon) compression bound, and the inverse-compression inequality. Recursively applying the same construction on restricted faces recovers the entire canonical minimal facial-reduction chain. This bridges **the same canonical barrier geometry** controlling the exact exponent (checkpoint 10) with its intrinsic facial depth. It remains distinct from the unresolved closed arithmetic characterization at fixed (n,r,d); analytic-center/stress limits may have substantial prior literature and priority is unverified.


## 2026-11-07: COMPLETE **universal dense** reciprocal spectrum at maximal depth

- [26_UNIVERSAL_MAXIMAL_DEPTH_RECIPROCAL_SPECTRUM.md](26_UNIVERSAL_MAXIMAL_DEPTH_RECIPROCAL_SPECTRUM.md): **proved necessary and sufficient arithmetic formula for all arbitrary dense PSD problems** at prescribed target nullity nu≥2, minimal degree d=nu, and reciprocal sharp exponent alpha=1/q. Attainability holds **iff** q≥nu and q/gcd(q,2)≤2^(nu-1). Every allowable value is achieved by the explicit rank-one midpoint pencils, so dense kernels cannot enlarge the reciprocal part of the maximal-depth spectrum. Provides the exact minimum dimension subject to maximal depth for each 1/q. The only unresolved dense maximal-degree candidates at nu=4 are nonreciprocals 3/16 and 3/14. This is a complete *subclass* classification, not a proof of the full nonreciprocal spectrum.


## 2026-11-07: first two explicit unresolved tests for dense sparse-depth universality

- [27_FIRST_UNRESOLVED_DENSE_MAXDEPTH_TESTS.md](27_FIRST_UNRESOLVED_DENSE_MAXDEPTH_TESTS.md): combines **complete universal dense reciprocal maximal-depth classification** (checkpoint 26), universal maximal-depth alpha<=1/nu (checkpoint 22), and the previously proved unconditional nu4 midpoint exponent catalogue to show that the **only** unclassified dense sharp exponents at (nu,d)=(4,4) are exactly **3/16 and 3/14**. Three finite harmonic weight patterns could support them, and all three have sparse peeling depth3. A dense realization at depth4 of either would refute sparse network depth universality. This is an exhaustive reduction, not a theorem excluding them.


## 2026-11-07: closed optimal dimension and exact ν4 exhaustive audit

- [26_UNIVERSAL_MAXIMAL_DEPTH_RECIPROCAL_SPECTRUM.md](26_UNIVERSAL_MAXIMAL_DEPTH_RECIPROCAL_SPECTRUM.md) now includes the **closed exact dimension formula** for arbitrary dense PSD maps with reciprocal exponent alpha=1/q, under maximal depth d=nu>=2:
  nu_min=max{2,1+ceil(log2(q/gcd(q,2)))} and n_min=r+nu_min. The q=2 rank-one-nullity-one boundary is stated separately.
- [28_EXACT_NU4_FRONTIER_AUDIT.py](28_EXACT_NU4_FRONTIER_AUDIT.py): independently executable, self-contained standard-library Fraction program enumerating every h=3 mediated graph, computing its exact sparse peeling degree and checking that the *only* unresolved universal nu4,d4 fractions are 3/16,3/14. Local run passed all assertions. This is an exhaustive small-case audit **conditional on** the previously established universal dense fixed-nullity exponent catalogue and new upper bound; sparse peeling by itself is not a dense necessity theorem.


## 2026-11-08: rigorous multi-action obstruction at first dense frontier
- [29_MULTI_ACTION_NU4_OBSTRUCTION.md](29_MULTI_ACTION_NU4_OBSTRUCTION.md): **PROVED** that starting from any of the three sharp nullity-4 networks for 3/16 or 3/14, *no arbitrary collection of independent extra edge kernel generators* can increase minimal depth from 3 to 4 while retaining that exponent and unique PSD recovery. A safe edge leaves a three-step exposing chain; every unsafe edge either yields an explicit stronger PSD arc or destroys uniqueness. This is a new exact stability/depth incompatibility theorem for an enlarged multiaction network family, but NOT a dense-kernel impossibility theorem.
- [30_NU4_MULTI_ACTION_EXACT_AUDIT.py](30_NU4_MULTI_ACTION_EXACT_AUDIT.py): fully self-contained Fraction-rational enumeration of all 29 possible extra edge cases and explicit verifying of safe 3-layer schedules and unsafe strictly worse exponents. All assertions passed in a local independent execution.
