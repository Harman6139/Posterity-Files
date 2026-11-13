# Current results — regular-body approximation hardness, PSD rank and conic universality

Date: 2026-11-13.
Repository: Harman6139/Posterity-Files.
Branch: laa-track02-gptpro-analytic-frontier-20261112.

This index now records milestones 20–22. The complete earlier index through 19 is preserved at commit e29fa80741fda419c6f066b7798888a178af7dc9, in this same path. The earlier index through 16 is at a4318f6ca7561b4b9018bd495eba140a9c29f76e. MASTER_INDEX.md retains the original trace-controlled normal forms and their strengthening through 09. No historical proof, script or result file is removed by this index update.

## 1. Main new result: well-behaved bodies can require exponentially large approximate SDPs

**21_EXPONENTIAL_APPROXIMATION_HARDNESS_OF_SMOOTH_SDP_BODIES.md**
Proof commit: 345536fd2437ab86a78961c5104cf07bdd05857b.

Let epsilon_star=2^(-19). For every n>=16 there is an even rational polynomial P_n such that

    C_n={x:P_n(x)<=1, ||x||^2<=4}

is centrally symmetric, convex and satisfies

    B_2 subset C_n subset (1+2^(-14)) B_2.

Its boundary is nonsingular real analytic, all principal curvatures lie in [1/2,2], and I/4<=Hess P_n<=17I on the radius-two ball. Every C_n admits a FINITE EXACT SDP lift by the published Helton–Nie sufficient theorem. Nevertheless, if a convex body K satisfies d_H(K,C_n)<=epsilon_star, every real product-PSD lift of K has

    sum_h d_h(d_h+1)/2 > floor(2^(n/2)).

In particular a single PSD matrix must have order greater than floor(2^(n/4)). Scalar inequalities count as order-one blocks; arbitrary real coefficients, singular faces, free variables and affine couplings are allowed.

Every unit linear objective on C_n has a unique optimizer x(u), with

    h_Cn(u)-u.x >= ||x-x(u)||^2/4,
    ||x(u)-x(v)||<=pi ||u-v||.

Thus representation hardness coexists with uniform target geometry and stable target optimization. There is no weak infeasibility or nonattained target optimum involved. The result concerns one formulation approximating ALL linear objective values; it is not an algorithmic lower bound for arbitrary objective-dependent methods.

For fixed n>=2 and small epsilon, there are such regular algebraic bodies, depending on epsilon, whose epsilon-approximate total PSD cone dimension is at least

    c_n epsilon^(-(n-1)/4)/sqrt(log(1/epsilon)),

and whose single-matrix order is at least

    c'_n epsilon^(-(n-1)/8)/(log(1/epsilon))^(1/4).

No optimality of these precision powers is claimed. The bodies change with epsilon, consistently with each body's finite exact lift.

The proof constructs 2^M disjoint-bump support functions, M=2^(2n-3), with fixed C^2 control; smooths their squared gauges to even rational strongly convex polynomials; and applies the coefficient-independent entropy theorem in 20. Polynomial degree and total input length are NOT asserted polynomial in n. The family is existential and computably selectable by expensive real quantifier elimination, not an efficient explicit combinatorial family. Historical novelty of the complete synthesis is not certified, and no named open conjecture is claimed solved.

## 2. Finite-precision compression of arbitrary compact SDP shadows

**20_FINITE_PRECISION_COMPRESSION_AND_METRIC_ENTROPY.md**
Proof commit: 198be435dd913f6f8d7108e076cbda558ddc2541.

Let C contain zero and lie in R B_2, R>=1 integer. If it has a product-PSD lift with total real matrix-coordinate dimension

    q=sum_h d_h(d_h+1)/2,

then it has a rational OUTER epsilon-approximation obtained with the same PSD blocks, bounded trace-one variables, and O(q+n) additional scalar inequalities. Its description length is

    O((q+n+1)^2 log(poly(q,n,R)/epsilon)).

The approximate lift has a displayed strict-feasibility margin polynomial in epsilon and inverse dimensions. No original coefficient bound, original Slater margin or inverse singular value is assumed. For a single order-d original block, the rational approximate block-diagonal LMI order is at most d+d(d+1)+4n+3. This is approximation with controlled overhead, NOT same-order exact rationalization.

For all profiles with q<=Q, the class has a Hausdorff epsilon-cover of size at most 2^F, where

    F=Q+(Q+n+1)^2 log_2(3+24 Q R (Q+n+1)(Q+nR+1)/epsilon).

The proof balances all supporting-slack factors in compact trace balls, selects a maximum-volume basis of their affine coefficient vectors, and rounds its bounded coefficients. Every other support equation is a linear combination with coefficient magnitude at most one, so no small singular value appears. The resulting approximate shadow is compact and uniformly strictly feasible.

This extends the counting argument to arbitrary compact SDP shadows. Slack-factor rescaling and counting/rounding have classical antecedents, particularly Gouveia–Parrilo–Thomas, Fawzi et al., Briet–Dadush–Pokutta and Averkov–Kaibel–Weltge; these are cited and not claimed as discoveries here. No efficient algorithm to find an unknown minimum lift is asserted.

## 3. Optimal exponential-order PSD rank with uniformly positive bounded entries

**22_BOUNDED_DYNAMIC_RANGE_EXPONENTIAL_PSD_RANK.md**
Proof commit: 71a6f4572cb6559007fd6317529bf10d7eb17e5e.

Fix the absolute constant K_star=3*2^24. For every r>=17 there is a finite rational matrix M_r with

    rank M_r=r,
    1<=M_ij<=K_star,
    rank_psd,R M_r>floor(2^((r-1)/4)).

Row and column counts are at most 2^(30(r-1)), and every entry has O(log r) rational bit length. Duplication permits square matrices. The construction uses rational nets in C_(r-1) and its polar, shrunk slightly to make every sampled slack uniformly positive. A small PSD factorization would produce a forbidden close intermediate convex body through the classical slack-sandwich theorem.

Conversely EVERY matrix of ordinary rank r and entries in [1,K] obeys

    rank_psd,R(M)<=rank_+(M)<=(45K)^r.

An elementary covering of its r-dimensional row span expresses every row as a convex combination of at most [5(1+8K)]^r fixed nonnegative vectors. Hence, at the ONE fixed entry-ratio bound K_star, the worst PSD rank is exactly 2^(Theta(r)) in exponential order. No sharp exponential base or claim for every K near one is made.

After normalizing M_r to a joint distribution, every probability is within a constant factor of the uniform table, and mutual information is at most log_2 K_star. Yet exact no-communication local-measurement generation of this distribution requires local quantum dimension greater than (1/2)floor(2^((r-1)/4)) on BOTH sides, even allowing a mixed shared state. The lower follows by forming PSD factors from conditional states and realifying complex factors. Additional uncounted shared randomness is not allowed. These are exact-generation bounds, not approximate-generation or communication bounds.

Bounded dynamic range is an ENTRYWISE property, not a spectral condition-number claim. The matrix theorem is about exact PSD rank. Constant Hausdorff hardness of the body does NOT silently imply constant entrywise approximate-factorization hardness. The family is existential/inefficiently selectable, not a short efficient explicit construction. Historical priority is not asserted.

## 4. Dependencies and prior results retained

The arguments in 20–22 do not require any earlier claimed escape-rate or optimal power-cone theorem. Their dependencies are classical slack factorization/bounded rescaling, the proofs in 20, elementary differential convex geometry, polynomial C^2 approximation, Helton–Nie's published sufficient theorem, and the finite slack-sandwich argument. They therefore form a logically separable continuation.

The prior research remains available in the following files:

- 17_GENERAL_EXTENSION_COMPLEXITY_FINITE_SLACK_AND_SOS.md: the classical slack-factorization framework in finite-obstruction form, complete fixed-order SOS certificates, product-block profiles; no efficient universal rank algorithm claimed.
- 18_ROBUST_FINITE_WITNESSES_AND_HAUSDORFF_CHARACTERIZATION.md: finite sandwich factors, quantitative fixed-order approximation gaps and Hausdorff lower semicontinuity.
- 19_COMPACT_PROJECTIVE_OBSTRUCTIONS_AND_ADDITIVE_OPTIMAL_LIFTS.md: same-order compact homogenization, projective escape obstructions, exact compact dyadic power-body sizes and join additivity. A join is not a Cartesian product.
- 15_ESCAPE_LOWER_BOUNDS_AND_OPTIMAL_POWER_CONE_LIFTS.md: the intrinsic escape obstruction and exact dyadic power-cone PSD/SOC resources in the declared model.
- 16_MIXED_CONE_ESCAPE_AND_REGULARIZATION_UNIVERSAL_LAW.md: mixed PSD/SOC/polyhedral escape and regularization laws.
- 14_SHARP_NONATTAINMENT_AND_REGULARIZATION_PHASE_LAWS.md: exact-feasible near-optimization and regularization asymptotics.
- 13_UNIFORM_IMAGE_GEOMETRY_AND_FINITE_ESCAPE_RESERVOIR.md: uniform image lifting geometry, finitely many escape directions and homogeneous error-bound duality.
- 12_RECIPROCAL_ESCAPE_LAW_AND_SHARP_DIMENSIONAL_BOUNDS.md: exact general-cone profile duality and semidefinite escape bounds.
- 10_ALL_RATIONAL_TWO_BASIS_COMPILER.md and 11_OPTIMAL_ONE_SCALE_UNRESTRICTED_UNIVERSALITY.md: rational quadratic-size two-basis representation of arbitrary rational SDPs using one common free observation scale, including feasibility regimes and exact objective identities. A normal-form reduction is not a polynomial-time feasibility decision algorithm.
- Files 01–09 and MASTER_INDEX.md: original trace-controlled universality, conditioning, CP/facial/dual strengthening, explicit constructors, and recorded diagnostic outputs.

The complete detailed indices at the immutable commits cited in the opening paragraph preserve every previous theorem summary and proof-commit reference. All original historical milestones and corrections are inherited on the branch. No proof file or numerical result is deleted or silently replaced.

## 5. Scope of the continuation

The latest results are analytic theorems, not extrapolations from finite experiments. Their full proofs, resource conventions, antecedents and limitations are in 20–22. They establish no named-conjecture priority, polynomial-time optimal-lift search, polynomial-degree explicit hard family, or general exact-SDP feasibility algorithm. They do establish a coefficient-independent quantitative description bound, exponentially hard approximations despite uniform geometric regularity and finite exact representability, and a matching exponential-order bounded-entry PSD-rank separation.