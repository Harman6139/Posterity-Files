# Consolidated Manuscript III research — mathematical development and full-proof navigation

**Purpose:** a continuous research account joining original source milestones, all conic-oracle results, grand arithmetic observability, the exact-rational minimax result, sharp oracle separations and invalid routes. This file summarizes results with exact equations and proof skeletons; the **COMPLETE ORIGINAL PROOFS** are preserved without abridgment in the four content-addressed [PROOF_ARCHIVE](PROOF_ARCHIVE) folders, indexed individually in [01_FULL_PROOF_MAP_AND_PROVENANCE.md](01_FULL_PROOF_MAP_AND_PROVENANCE.md). Never cite only this synthesis for a delicate proof step.

## Mathematical object and exact information interface

For a rational symmetric affine pencil X(x)=X0+sum_{i=1}^d x_i Hi, with <Hi,Hj>_F=delta_ij, natural conic loss is

    f(x)=1/2 dist_F(X(x),S_+^m)^2
    grad_i f(x)=<Hi,X(x)-P_+(X(x))>_F.

We require genuine weak infeasibility X(R^d)cap S_+^m=empty, dist(X(R^d),S_+^m)=0, f(0)<=1 and a fixed common rho_f(s) comparable to s^(-beta). The **original central question** permits each arbitrary finite real x, exact f and coordinate-gradient replies, unrestricted computation/randomization, and unqueried output. The hidden input is the rational chart as well as the affine matrix image. A full PSD matrix projection, an explicit coefficient list, positive-noise oracle, or radius-charged query is a DIFFERENT model.

For beta=1/2 the correct current normalized all-dimension bracket is

    Omega(log(1/epsilon)) <= worst-case exact rational calls <= O(1/epsilon).

The right-hand side follows from accelerated comparison with a finite near-optimal point, not a minimizer. The left-hand side is the exact rational prior described below. No claimed universal matching power bound.

## I. Origin: static escape and generic smooth nonattainment

- **Original milestone 12** [complete proof](PROOF_ARCHIVE/01_FOUNDATION_ORIGINAL_FULL_PROOFS/12_RECIPROCAL_ESCAPE_LAW_AND_SHARP_DIMENSIONAL_BOUNDS.md) relates approximate primal size R_b(delta) and normalized dual certificate size Q_b(epsilon) by an exact support profile identity. For weakly infeasible semidefinite systems, escape exponents range within sharp order-m envelopes involving 2^(m-1)-1. The classical facial-reduction antecedents are identified in the original proof.
- **Original milestone 26** [complete proof](PROOF_ARCHIVE/01_FOUNDATION_ORIGINAL_FULL_PROOFS/26_ESCAPE_CONTROLLED_PROJECTION_DYNAMICS.md) proves a comparator energy estimate for a genuine unattained infimum. If rho(s)<=C s^(-beta), projected/accelerated schemes yield upper rates from finite comparator u with f(u)<=s, no minimizing point required:
  
      f(x_T)<=s+2rho(s)^2/(T+1)^2.

  Optimizing s gives f(x_T)=O(T^(-2/(2beta+1))). For beta=1/2, O(T^-1). Feasibility residual is sqrt(2f), hence O(T^-1/2). The exact alternating-projection dynamics and leading motion constants of original 40 are method-specific, not all-oracle lower bounds.
- **Original 27, 38, 39** [full text in foundation archive](PROOF_ARCHIVE/01_FOUNDATION_ORIGINAL_FULL_PROOFS/) prove deterministic, fixed-Haar randomized, and noise/general profile lower bounds for engineered black-box smooth convex losses. They do not claim that generic hidden function itself equals a natural squared PSD distance. This gap motivated the later Track III research.

## II. Direct natural conic embeddings, escape tails and statistical information

- **Conic checkpoint 01** [full proof](PROOF_ARCHIVE/02_CONIC_ORACLE_CHECKPOINTS_00_TO_12/01_RATIONAL_FIVE_BY_FIVE_NOISE_AND_BIAS_THEOREM.md) constructs the explicit rational 5x5 block pencil with 2x2 weak-infeasibility tail, isometric coordinates, exact f_theta and constant gradient separation. Its stochastic experiment is N iid Gaussian observations with means +/-eta independent of queries, yielding Omega(sigma^2 epsilon^-3) for beta=1/2 under the *noise-gradient oracle with no exact population values*. Absolute gradient bias critical order epsilon^(3/2).
- **Conic 02/05** [direct tail proof](PROOF_ARCHIVE/02_CONIC_ORACLE_CHECKPOINTS_00_TO_12/05_EVERY_RATIONAL_ESCAPE_EXPONENT.md) produce rational isometric weakly infeasible tails with prescribed rational beta. Their binary geometric-mean root products are adjusted to match all-perturbation PSD-distance escape, not just one feasible approach curve.
- **Conic 07** [complete global lift](PROOF_ARCHIVE/02_CONIC_ORACLE_CHECKPOINTS_00_TO_12/07_GLOBAL_ISOMETRIC_QUADRATIC_ORACLE_LIFT.md) takes q(x)=1/2||Cx-d||^2 with 0<=C^T C=A<=I/2 and rational/real S^T S=I/2-A. Star(Cx-d), offset arrow(M,Sx), and W(z) block give

      f(x,z)=q(x)+(||Sx||-M)_+^2/2+phi(z).

  All directions are orthonormal by Gram balance 2A+2S^T S=I. For every finite x the natural (f,grad f) and one matrix product Ax simulate one another (with fixed known side data), including unbounded excursions; this is not a generic epigraph compiler.
- **Conic 09** [fixed Haar real-coefficient theorem](PROOF_ARCHIVE/02_CONIC_ORACLE_CHECKPOINTS_00_TO_12/09_UNRESTRICTED_REAL_CONIC_RANDOMIZED_FRONTIER.md) uses a random chart U and repeated eigenspace dimensions to force a T-query lower bound with probability >=7/8 at c_beta(T+1)^(-2/(2beta+1)). The coefficients of U are generally real, NOT rational. The matrix order and coordinate dimension are O_beta(T^3); arbitrary unqueried outputs are handled by a deferred Haar/Gaussian augmentation.
- **Conic 08, 10, 11** [exact models and full proofs](PROOF_ARCHIVE/02_CONIC_ORACLE_CHECKPOINTS_00_TO_12/) respectively give (a) matching rational *charged-radius* complexity, (b) a small-relative-noise crossover, and (c) rational *positive input-relative error* complexity

      N=Theta_beta(epsilon^(-beta-1/2)+tau^2 epsilon^(-4beta-2))

  for 0<zeta<=c_beta epsilon^(2beta+1), with bias threshold of order epsilon^(2beta+1). The positive-zeta prior depends on zeta and coefficient height. Exact population values are not supplied in the noisy lower experiment. None supplies the original zeta=0 uncharged rational power lower.

## III. Arithmetic and spectral observability: stronger recovery in subclasses

- **Grand arithmetic checkpoint 01–02** [full proof archive](PROOF_ARCHIVE/03_ARITHMETIC_SPECTRAL_CHECKPOINTS_01_TO_08/) separates full objective identification from optimization; a bound-height rational quadratic is recoverable in one exact algebraic gradient query, but rational natural PSD-distance functions may coincide on open spectral regions and yet differ elsewhere. A selected bounded algebraic point can fingerprint local algebraic germs under fixed format and degree bound. Such exact oracle calls may have enormous algebraic degree and unlimited offline computation.
- **Grand arithmetic checkpoint 07** [complete proof](PROOF_ARCHIVE/03_ARITHMETIC_SPECTRAL_CHECKPOINTS_01_TO_08/07_ALGEBRAIC_SPECTRAL_OBSERVABILITY_AND_SHARP_ESCAPE.md): if R(z,x)=det(zI-X(x)^2) is irreducible over Q(x), the local algebraic germ h=2f determines the negative count k through

      Tr(P_h)/deg(P_h) = (k/m) tr(X(x)^2),

  where P_h is the minimal polynomial of h over Q(x). Since isometry makes the quadratic part of tr(X^2) equal ||x||^2, k is identifiable. If k=1 or m-1, one scalar value at the specified common algebraic probe identifies the entire signed characteristic polynomial despite rank transitions elsewhere. The result is a **subclass** theorem with explicit irreducibility/inertia assumptions. Generic full S_m subset-sum recovery has exceptional pairs; classical Moser subset-sum combinatorics must be credited.
- **Grand arithmetic 05** [regular chamber continuation](PROOF_ARCHIVE/03_ARITHMETIC_SPECTRAL_CHECKPOINTS_01_TO_08/05_SPECTRAL_CHAMBERS_AND_CODIMENSION_TWO_RECOVERY.md) proves one-query objective recovery when candidate maximal-rank-drop sets do not separate the regular locus (including codimension >=2), not for all rational pencils.

## IV. Exact rational minimax in the ORIGINAL oracle — true optimization-relevant hiding

- **Exact-rational checkpoint 01** [complete construction](PROOF_ARCHIVE/04_EXACT_RATIONAL_MINIMAX_CHECKPOINTS_01_TO_13/01_MOMENT_MATCHED_OPTIMIZATION_HARD_PENCILS.md): recursively choose hidden word w in {+/-1}^n, spatial scale h=1/8, mass scale lambda=1/64 and energy scale eta=lambda h^2=1/4096. Moment matching of positive rational atomic measures through quadratic order yields nonnegative C1 convex core

      H_w(t)=1/2 int(s-t)_+^2 dmu_w^-(s)+1/2 int(t-s)_+^2 dmu_w^+(s)

  with the SAME exterior value and derivative for all w. Different hidden words have disjoint near-zero intervals I_w. The rational scalar PSD blocks from four-square atom weights plus fixed W(z)=[[0,1],[1,z]] give an exact isometric, genuinely weakly infeasible pencil of order 24(n+1)+2, with O(n^2) bits, ||X0||_F^2=125/48, and for every s<=1/8,

      (1/2)s^(-1/2)<=rho_f(s)<=s^(-1/2).

  For epsilon_n=(5/384)4096^(-n), every epsilon_n-successful unqueried output identifies w.
- **Exact-rational checkpoint 02** [complete minimax game proof](PROOF_ARCHIVE/04_EXACT_RATIONAL_MINIMAX_CHECKPOINTS_01_TO_13/02_EXACT_BINOMIAL_MINIMAX_AND_LOGARITHMIC_FRONTIER.md) proves for any 0<epsilon<=epsilon_n

      sup_alg inf_w Pr[f_w(output)<=epsilon]
       = 2^(-n) sum_{j=0}^{min(n,T)} binom(n,j).

  Natural oracle replies at arbitrary real points are simulated by a stronger first-mismatch word oracle; single natural gradient query at a bounded irrational Q(sqrt(2)) point realizes a word probe. A fixed uniform prior is chosen before algorithm randomness. The exact minimax expected objective infimum is also computed in the original file. Choosing n=4(T+1) forces failure >2/3 at *exponentially small* epsilon_n, not at c/T. Ordinary two-dimensional central-cut ellipsoids give an O(log(1/epsilon)) upper bound across the ENTIRE normalized rational two-coordinate class. Hence the fixed-two-coordinate minimax is Theta(log(1/epsilon)), even with arbitrary PSD order.
- **Exact-rational checkpoint 04–05** [proved limitation](PROOF_ARCHIVE/04_EXACT_RATIONAL_MINIMAX_CHECKPOINTS_01_TO_13/04_WHY_THIS_FAMILY_CANNOT_SUPPLY_THE_POWER_LAW.md) shows the known moment-nesting family always admits deterministic error O(4096^-T) uniformly in depth; increasing n or taking rotated equal-scale separable copies cannot produce the desired c/T objective threshold. A rotation-blind signed gradient recurrence gives an explicit uniform fast optimizer on the latter subclass.
- **Exact-rational 08,11,12** [full subfamilies](PROOF_ARCHIVE/04_EXACT_RATIONAL_MINIMAX_CHECKPOINTS_01_TO_13/12_CENTER_DIMENSION_AND_COMPACT_MASK_MINIMAX.md) realize genuinely compact noncommuting PSD arrow masks with disjoint zero sets and uniformly hidden exteriors. One huge exterior *scalar* probe identifies center geometry via algebraic multiquadratic radical independence; if their recovered center affine-hull dimension is r, a centroid cutting-plane method needs O(1+r log(1/epsilon)) queries. A fixed-center budget gives Theta(log(1/epsilon)); not all PSD pencils.
- **Exact-rational 09,10** [stronger oracle theorem](PROOF_ARCHIVE/04_EXACT_RATIONAL_MINIMAX_CHECKPOINTS_01_TO_13/09_FULL_PSD_PROJECTION_OBSERVABILITY.md): for any known FINITE candidate class of rational approximately feasible pencils, TWO antipodal *matrix-valued projection* replies identify all coefficients via positive spectral visibility. Checkpoint 10 shows one such full projection of the explicit n-bit family can require Theta(n) exact value/gradient calls to simulate. Therefore this is a meaningful oracle interface separation, NOT a collapse of the original model.
- **Exact-rational 13** [global PLQ theorem](PROOF_ARCHIVE/04_EXACT_RATIONAL_MINIMAX_CHECKPOINTS_01_TO_13/13_SPECTRAL_JUMP_PROPAGATION_AND_PLQ_OBSTRUCTION.md): for a natural PSD-distance objective which is quadratic on every cell of a finite polyhedral partition,

      F(x)=Q(x)+(1/2)sum_j kappa_j (ell_j(x))_+^2.

  Across the whole hyperplane ell_j=0 the Hessian jump coefficient is constant (it cannot stop at a facet endpoint); the number of nonzero distinct jump hyperplanes is at most the maximal rank of X(x). The proof uses first-order zero-eigenvalue compression, rational continuation of kernel projections along lines, discrete Hessian-jump values and polynomial factor divisibility. Hence squared Euclidean distance to a simplex with nonorthogonal adjacent facets cannot be *equal* to natural affine PSD distance up to positive scaling and global quadratic. This blocks a previously plausible exact oracle-preserving SDP epigraph shortcut.

## V. Reproducibility, priority and what cannot be claimed

Exact verification scripts and saved JSON results live alongside the original proof files in the archive; summary ledger [05_VERIFICATION_AND_OPEN_TASKS.md](05_VERIFICATION_AND_OPEN_TASKS.md). The 9,964 rational tests and 286 grand arithmetic symbolic checks were rerun on 2026-11-15. They validate algebraic instances and finite recurrences, not universal information lower bounds. All material still requires external mathematical review and complete priority assessment. The published-paper [32-article benchmark](03_PUBLISHED_PAPER_BENCHMARK_2025.md) rejects an unsupported ">=80th percentile" assertion.

**Outright open:** for rational isometric weakly infeasible PSD pencils of arbitrarily growing dimension, free-radius exact (f,grad f), either prove a fixed rational distribution producing Pr[f(output)>=c/(T+1)]>=2/3 for polynomial-size coefficient encoding (beta=1/2) OR prove a universally faster optimizer/identification theorem handling all rank strata. No archived proof establishes either. The current bracket remains logarithmic lower versus epsilon^-1 upper.

All unabridged proofs and their source histories are preserved in the linked subtree archive. Do not infer any missing result by removing its model qualifiers.
