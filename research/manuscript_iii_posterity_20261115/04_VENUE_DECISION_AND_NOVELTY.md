# Venue decision and 2024–2026 novelty audit — research-grade, no percentile inflation

**Dated:** 2026-11-15. This is an authors' journal-fit decision grounded in the saved full proofs and the [32-paper article benchmark](03_PUBLISHED_PAPER_BENCHMARK_2025.md). Not a claim to have been externally reviewed, accepted or independently replicated.

## Bottom-line recommendation

**Journal of Convex Analysis (JCA) is the strongest currently defensible *fit-first* journal target** for a focused, genuinely complete paper extracted from the results. It covers convex/variational analysis, nonsmooth analysis, projection, exact cone geometry and optimization. A coherent candidate could center on (a) exact rational moment-matched conic minimax, the complete fixed-two-coordinate Theta(log 1/epsilon) lower/upper theorem and sharpened projection-information separation; or independently (b) PLQ affine PSD-distance rigidity, global hyperplane jump propagation and nonrepresentability of simplex distances. Do NOT submit a single all-checkpoints anthology.

**SIAM Journal on Optimization (SIOPT) is the strongest *nearby prestige/optimization-theory ambition***, not the present recommendation. It wants substantially new results of interest to a large part of optimization, normally <=25 typeset pages, and it does not generally publish supplementary materials except requested during review. The current flagship problem — whether ALL rational hidden PSD-distance objectives in growing dimension have an Omega(epsilon^-1) exact value-gradient minimax lower bound or a substantially faster universal algorithm — is OPEN. The current mixed archive would not pass our top-quintile gate.

**Mathematical Programming, Series A**, would be an ambitious flagship target after a complete original all-dimensional conic arithmetic-information theorem plus recognizable optimization consequences and external proof audit. The present work does not reach that bar. **Mathematics of Operations Research (MOR)** is an alternative if future work develops genuinely robust OR models (decision systems, matrix learning with explicit operational costs, risk/control/robust optimization) from the exact-information results; currently its 2025 sample puts applied/decision motivation in sharper relief. **Journal of Convex Analysis** is mathematically plausible *without falsely claiming the original grand theorem resolved*.

**Important 2026 operational update:** official [JCA journal site](https://journalofconvexanalysis.com/) and [volume archive](https://journalofconvexanalysis.com/archive/32/) are active under Banach Press LLC, following transfer of publishing rights in July 2026 (the old Heldermann publisher announcement). Check submission instructions and article charges at the CURRENT journal site before submission; do not direct an author exclusively to the legacy publisher.

## What kind of paper should actually be prepared?

### Candidate A: best immediate research paper, JCA

**Provisional title:** *Exact Rational Oracle Information at Infinity: Moment-Matched Semidefinite Distance and Two-Dimensional Minimax Complexity.*

Core complete theorem is

    N_C2(epsilon; fixed confidence) = Theta(log(1/epsilon))

for rational weakly infeasible isometric affine PSD-distance objectives with exactly TWO coordinate variables, arbitrary matrix order and common rho_f(s) comparable to s^(-1/2). The lower has the genuinely fixed rational n-bit distribution, exact success law

    S(n,T) = 2^(-n) sum_{j=0}^{min(T,n)} binom(n,j),

full exterior equality at any finite query, explicit rational scalar PSD blocks and a W(z) weak-infeasibility block. The upper is a central-cut ellipse proof. Matrix-order and encoding length grow polynomially with n; the best lower objective threshold is exponentially small in T. Do not suppress this scale.

Augment with one or two compelling cross-interface results: one single full PSD projection can recover the hidden word, while value/gradients need Theta(n) queries; full PSD projection in any KNOWN FINITE rational approximate-feasibility class needs at most two antipodal queries. These are distinctly *stronger-oracle* results. A full paper needs a precise title/abstract stating BOTH interfaces separately, a full proof of fixed-prior quantifiers, history of LeadingOnes prefix-search priority, and a clear reason why this matters to conic algorithms. Strongest if submitted separately as two papers: optimization minimax vs matrix projection observability.

### Candidate B: geometry/structural paper, also JCA; potential higher standalone novelty

**Provisional title:** *Hyperplane Propagation of Spectral Curvature Jumps and Limits of Semidefinite Distance Representations.*

Complete key theorem: any finite-polyhedral-piecewise-quadratic natural PSD-distance objective of a finite symmetric affine pencil is a global quadratic plus signed squared affine hinges with full-hyperplane jumps; finite nonzero hyperplane count <= maximal rank. Hence (scaled distance squared to a nonorthogonal simplex)+global quadratic cannot be a natural affine PSD distance, no matter the matrix order. This addresses the common but invalid inference "a convex function has an SDP representation, therefore its natural affine PSD-distance oracle has the same replies." Strong JCA fit; SIOPT possible only after independently verified originality, breadth, additional sharp converses/applications and a focused 25-page self-contained article.

### What not to submit as currently written

- The entire four-branch posterity archive is too sprawling and covers incompatible oracles; it is excellent research history, not one well-formed paper.
- The grand theoretical abstract that says "complete rational/real precision phase diagram" or "dimension-uniform rational exact minimax closed" is FALSE relative to the saved proofs.
- The very strong **real** chart theorem must be labeled real; its Haar chart is nonrational. The rational positive-error theorem requires strictly positive bias and does not pass to zero by continuity. The rational radius-charged theorem changes the unit query cost. The full projection two-query result is not for a scalar gradient oracle. None can be relabeled as the original all-rational exact answer.

## Attribution ledger: prior ingredients versus claims needing new priority verification

| Topic | Established antecedent | What saved work ACTUALLY adds / claims | Specific novelty risk |
|---|---|---|---|
| Randomized arbitrary-query smooth lower bounds | Nemirovski–Yudin, Woodworth–Srebro, Diakonikolas–Guzman; Dereziński–Epperly–Meyer COLT 2026 and Chewi et al. JACM 2024 | Fully explicit **natural** PSD-distance simulation, plus real-Haar conic distribution; prior Gaussian/Krylov augmentation is reused | High: no general "invented Krylov reduction" claim |
| Escape geometry at infinity and weak SDP infeasibility | Lourenço–Muramatsu–Tsuchiya 2016, Pataki–Touzov 2024 | Exact conic escape-profile constructions and original-project comparator dynamical statements | Medium/high: qualitative facial support/rapid growth classical |
| Gaussian testing / inexact gradients / stochastic acceleration | Agarwal–Bartlett–Ravikumar–Wainwright 2012, Lan 2012, Devolder–Glineur–Nesterov 2014 | Rational five-by-five genuine PSD distance produces *exact* gradient statistical experiment and bias indistinguishability | Medium: identity of information model matters, not Gaussian-test invention |
| Scalar hidden word oracle | Droste–Jansen–Wegener, Theory of Computing Systems 2006, DOI 10.1007/s00224-004-1177-z | Positive rational moment-matched PSD realization with fixed-prior exact optimization, matching two-coordinate conic minimax | High for abstract combinatorics; new contribution is exact conic realization |
| Radial kernels, center recovery | Micchelli, Constructive Approximation 1986 | Exact exterior invariant of radius-weighted ball PSD arrow pencils; single algebraic probe and center-hull minimax law | High: classical radial basis identifiability / rational function fields must be checked |
| Eigenvalue and spectral Hessian formulas | Lewis, MOR 1996 DOI 10.1287/moor.21.3.576; Lewis–Sendov, SIAM J Matrix Anal Appl 2001 DOI 10.1137/S089547980036838X | PLQ global full-hyperplane Hessian jump propagation and triangle-distance natural-PSD nonrepresentability | Medium: most promising new structural theorem, but external priority review required |
| Galois subset sums and moment inversion | Classical multiset recovery / Moser's problem | Field-trace inertia in rational isometric conic chart, one-value spectral identification for extreme inertia | Medium/high: classical subset-sum triangular coefficients not invented |
| Rational exact coefficient encoding | Kronecker substitution, Eisenstein irreducibility, real algebraic geometry | Height-independent exact germ fingerprint under fixed format/degree assumptions and finite-precision comparison for chosen classes | High: encoding itself classical; geometry application must bear novelty |
| Complete PSD projection | Matrix spectral projectors + Galois transitivity + analytic identity | Two-antipodal full projection recovery for known finite rational approximately feasible pencil class | Medium: check inverse spectral and LMI identification work; not a universal value-gradient theorem |

## Essential 2026 research comparator

- Michał Dereziński, Ethan N. Epperly, Raphael A. Meyer, *The matrix-vector complexity of Ax=b*, COLT 2026 / PMLR 336, [arXiv:2602.04842v4](https://arxiv.org/html/2602.04842v4). In particular the arbitrary-query/Krylov augmentation appears as previously known in their technical appendix (and they acknowledge earlier Chewi–de Dios Pont–Li–Lu–Narayanan, JACM 2024 [DOI 10.1145/3673651](https://doi.org/10.1145/3673651)). Any novel manuscript must precisely state what the conic embedding adds beyond that machinery.
- SIOPT 2025 Kolmogorov–Naldi–Zapata, *Certifying Solutions of Degenerate Semidefinite Programs*, [DOI 10.1137/24M1664691](https://doi.org/10.1137/24M1664691). Their explicit-input exact algebraic certification and our unknown-pencil black-box information are different.
- SIOPT 2025 Klingler–Netzer *Homotopy Methods for Convex Optimization*, [DOI 10.1137/24M1693416](https://doi.org/10.1137/24M1693416). A true SDP algorithm with hyperbolic program reach.
- SIOPT 2025 Liang et al. *Understanding the Influence of Digraphs on Decentralized Optimization*, [DOI 10.1137/24M1657341](https://doi.org/10.1137/24M1657341). Their lower bound and matching method in one complete application model give an especially instructive completeness benchmark.

## Audit status and 80% rule

The 32-paper [DOI sample](03_PUBLISHED_PAPER_BENCHMARK_2025.md) includes 12 SIOPT, 10 MOR, and 10 JCA. FULL proof inspection was obtained for two JCA papers; selected author preprints and theorem statements for SIOPT and 2026 control. For many papers, the publisher shows only metadata/abstract without full proof access. **Therefore no 8-of-10 proof-level advantage and no >=80th-percentile rating are certified**.

Conservative present readiness diagnostic is 4.9/10 for the unedited all-milestone anthology, NOT an acceptance probability, NOT a scientific quantitative estimate of citation impact, and NOT an 80th percentile. It must not be confused with the probable readiness of an extracted and externally reviewed JCA paper.

## Timing and author instructions

There is no guaranteed acceptance window, and certainly not a promise of revision-free acceptance within eight months. A 2025 SIOPT example (Klingler–Netzer) lists submission 13 Sep 2024, acceptance 26 Mar 2025 (about six and a half months); another 2025 SIOPT topical example lists 27 May 2024–22 Apr 2025 (about eleven months). Those are individual historical cases, not a journal-level acceptance-rate or timeline distribution. Verify venue-specific current dates and JCA publisher workflow before submission.

**Decision:** finish **one** 20–30 page JCA-targeted, complete-scope article, obtain external mathematical audit; do not submit the archive as a journal paper. If original rational all-pencil frontier is closed later, reconsider SIOPT or Mathematical Programming A.
