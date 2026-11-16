# Checkpoint 10 — primary context, contribution boundaries and the editorial gap now filled

Date: 2026-11-15. This records the primary-source checks made during the mathematical continuation. It is a targeted priority comparison, NOT an exhaustive novelty certification or a published-paper percentile assessment.

## 1. What this continuation actually adds

The strongest new result is the data-only regular-escape characterization in Checkpoints 02–03. An attained strictly feasible convex quadratic SDP determines a unique coefficient pair. Interior positivity is equivalent to an interior common leading state of the ORIGINAL affine-first DRS algorithm. A finite primal–dual gap certifies the coefficient to error 2sqrt(gap), and strict gap/eigenvalue inequalities certify exact last steps for every start. The proof constructs an approximate orbit from the STATIC optimizer and then obtains two orders of normal tracking. It does not assume that an unknown orbit has the desired spectrum.

The same program induces a norm on the coupling block. Checkpoints 04–05 show that the algorithm implicitly selects a minimum of this norm and that its value is simultaneously the squared escape speed and the sharp static size/accuracy coefficient. Explicit cases give Frobenius, Schatten-four, and l^(4/3) selection. Checkpoint 08 solves a larger free-upper-block class even with singular leading spectra, using an explicit good orbit and all-start transfer. These are input-specified theorems, not another simulation of the old seven-by-seven candidate.

Checkpoints 01, 06 and 09 supply the algorithmic output consequence: a positive local average of actual constraint-set shadows, over a vanishing-relative window, attains the optimal radius/accuracy profile with an exact second-order inefficiency constant. The implementation requires no escape exponent, no spectral phase, no extra projections and only constant vector storage at block output times. The general version allows arbitrary closed convex semialgebraic sets, not only cones. This is postprocessing, not a raw last-step theorem or a new anchored algorithm.

## 2. Close primary antecedents checked

### Liu–Ryu–Yin: pathological conic splitting

Primary text: https://arxiv.org/html/1706.02374v3 .

The paper explicitly analyzes divergent DRS/ADMM iterates for infeasible, unbounded and pathological conic programs. Its introduction and Sections 2.2–2.3 explain the zero-minimal-displacement difficulty and the information available from divergent iterates. Therefore neither 'DRS divergence can carry useful information' nor the DRS–ADMM connection is new here. Our additional statements concern the first nonzero coefficient at its sublinear scale, a finite convex coefficient program, implicit norm selection, and the sharp local shadow-efficiency law.

Reading boundary: the relevant introductory, displacement and feasibility statements were inspected in primary HTML. This continuation does not claim a new independent audit of every proof in that paper. The v3 source record is dated 15 October 2017; a generated HTML display date must not be mistaken for a new 2026 theorem.

### Banjac–Lygeros: asymptotic displacement and infeasibility

G. Banjac and J. Lygeros, On the asymptotic behavior of the Douglas–Rachford and proximal-point algorithms for convex optimization, Optimization Letters 15 (2021), 2719–2732, DOI 10.1007/s11590-021-01706-3.
Primary full text: https://link.springer.com/article/10.1007/s11590-021-01706-3 .

Their propositions identify limiting displacement certificates of strong infeasibility; Remark 5.5 states that weak infeasibility instead gives a zero unscaled displacement. The current finite coefficient theorem addresses what that zero limit does not specify: the nonzero rescaled vector, its exact magnitude and the bounded matrix block selected by the divergent algorithm. It does not contradict the unscaled displacement theorem or solve general finite-time infeasibility detection.

### Ryu–Taylor–Bergeling–Giselsson: operator splitting performance estimation

E. K. Ryu, A. B. Taylor, C. Bergeling and P. Giselsson, Operator Splitting Performance Estimation: Tight Contraction Factors and Optimal Parameter Selection. Primary preprint: https://arxiv.org/abs/1812.00146 ; publisher DOI 10.1137/19M1304854.

Their work reformulates optimal operator-class contraction factors as finite SDPs and uses them for proof discovery and parameter selection. Consequently 'using an SDP to analyze DRS' is emphatically NOT a novelty claim for this project. The present program is an instance-specific static description of a fixed-point-free, weakly infeasible escape coefficient and the norm selected by bounded cross blocks. It is not an operator interpolation performance-estimation program.

The introduction, stated scope and methodology were inspected. No exhaustive comparison with every later performance-estimation extension is claimed.

### Abbaszadehpeivasti–Zamani: recent exact rate analysis

H. Abbaszadehpeivasti and M. Zamani, On the convergence rate of the Douglas–Rachford splitting algorithm, arXiv:2509.06676v2. Primary text: https://arxiv.org/html/2509.06676v2 .

The explicit standing assumption in its introduction is that the DR operator has a fixed point. Theorem 3.1 and the sharpness construction concern worst-case finite-horizon residual bounds in that setting. Our weakly infeasible instance has no fixed point, and its statements are exact fixed-instance asymptotics and static selection laws. Neither the old gamma=2 construction nor the present positive certificate should be advertised as resolving that paper's distinct conjectures.

A targeted search also surfaced the public, unrefereed AI-assisted repository https://github.com/ipitchford/douglas-rachford-residual-counterexamples . Its README was retrieved from the primary repository. It concerns a different uniform worst-case residual conjecture and horizon-dependent scalar/planar examples, not the affine–PSD fixed-instance spectral coefficient or the norm-selection results here. Its claims were not independently verified in this continuation.

### Bolte–Gaubert–Vigeral: tame discounted curves

J. Bolte, S. Gaubert and G. Vigeral, Definable zero-sum stochastic games, Mathematics of Operations Research 40 (2015), 171–191, DOI 10.1287/moor.2014.0666. Primary text: https://arxiv.org/html/1301.1967v2 .

Tame discounted-curve and Puiseux arguments have substantial classical antecedents, including those described in this paper. They are not new proof techniques invented here. The local-averaging theorem explicitly depends on the project's prior quantitative common-state theorem, which uses that general strategy. By contrast, the core finite-certificate/raw-velocity proof of Checkpoint 03 builds its own approximate orbit and does not depend on the old seven-by-seven argument or on an assumed cosmic state theorem.

### Classical ADMM equivalence

S. Boyd, N. Parikh, E. Chu, B. Peleato and J. Eckstein, Distributed Optimization and Statistical Learning via the Alternating Direction Method of Multipliers, Foundations and Trends in Machine Learning 3(1) (2011), 1–122.
Primary author page: https://web.stanford.edu/~boyd/papers/admm_distr_stats.html .

The ADMM/DRS relationship is classical. Checkpoint 06 derives the precise affine-isometry conjugacy and index/sign conventions only so that the NEW coefficient and local-recovery statements transfer correctly. It does not claim a new equivalence or a new ADMM algorithm.

## 3. Other classical ingredients and current literature boundaries

The Schur complement, matrix fractional convexity, Slater duality, firm nonexpansiveness, Sylvester derivatives of matrix functions, Fenchel conjugacy of squared norms, and analytic implicit-function theorem are standard. The variational formulas for familiar norms should not be promoted as independently new identities merely because they occur in the proof. The contribution is the exact dynamical selection and finite certificate linking them to divergent DRS.

Primary searches also checked contemporary work on inconsistent DRS shadows and on weak-versus-strong convergence in infinite-dimensional convex feasibility. These concern different questions from weak infeasibility in finite-dimensional PSD spaces. No claim of exhaustive priority coverage follows from not finding an identical theorem in these searches.

Queries included combinations of Douglas–Rachford with 'implicit selection', 'implicit bias', 'weakly infeasible', 'leading coefficient', '4/3', 'four-thirds', 'Schatten', and 'minimum norm'. The exact finite certificate and l^(4/3) selection statement were not located in the primary results inspected. This is a search report, not a proof that no earlier source exists.

## 4. Relation to the user's requested substantive upgrade

The prior editorial memo asked for an input-checkable spectral certificate or a useful algorithmic consequence beyond an isolated counterexample. Those specific mathematical objectives are now addressed:

- Checkpoints 02–03 give a finite convex program, exact dual, rigorous coefficient-error bound and all-start raw velocity theorem.
- Checkpoints 04–05 turn the result into an implicit norm-selection theory with explicit general families and sensitivity.
- Checkpoint 08 handles a broad singular-leading-spectrum class without the interior assumption.
- Checkpoints 01/06/09 give implementable near-optimal shadow and ADMM residual recovery even where no raw natural-scale bound is assumed.
- Checkpoint 07 gives invariance under arbitrary-strength affine couplings and records why singular limits cannot be interchanged without proof.

These are new mathematical statements and full derivations in this branch, not merely a proposed future research plan. My substantive assessment is that they materially strengthen the SIOPT-facing contribution. That judgment does not establish an acceptance probability or a measured upper-quintile rank.

The unrestricted raw bound ||d_k||=O(k^(p-1)) for every singular affine–PSD system, the original gamma=1 switching orbit, and a robust universal resonance classification beyond conic splitting remain unresolved. A broad JNS resonance claim would still need the relevant additional theorem. No general frontier closure is claimed.

## 5. Manuscript focus implied by the new mathematics

The new standalone organizing question is: 'Can a finite convex problem predict the speed and implicit selection of a divergent splitting algorithm?' The finite certificate and norm-selection theorem should lead the optimization manuscript. The old resonance work is a contrast and scope boundary, not a correctness dependency of this positive theory.

A suitable working title is 'Static certificates and implicit norm selection for diverging Douglas–Rachford iterations'. A focused proof sequence is: exact problem and result; reduced affine geometry and convex certificate; raw all-start dynamics; norm-selection corollaries including singular spectra; ADMM and local output recovery; limitations and related work. Do not force every historical checkpoint or the long gamma=2 proof into the same short paper. All nonclassical proof dependencies used for its headline result must still be included or cited to an actual complete accessible proof, not hidden behind a promotional summary.
