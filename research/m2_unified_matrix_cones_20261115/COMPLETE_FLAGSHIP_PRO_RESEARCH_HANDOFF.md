# MANUSCRIPT II — GRAND UNIFYING PRO RESEARCH HANDOFF
## Arithmetic geometry of rank-one matrix cones: a structural factorization–separation–complexity theorem

**Research date:** 2026-11-15. **Role:** independent fresh high-effort mathematical researcher, Manuscript II flagship upgrade. **Read this entire prompt and every primary proof below.** This is a prospective research target, **not** a claim that the grand theorem has already been proved.

### Executive assignment: one unifying breakthrough, not a longer specialist appendix

The author's complaint is that Manuscript II remains a sophisticated but *specialized* study of copositive shadow pivots. Your assignment is to discover and rigorously establish a single mathematical principle in **linear algebra of rank-one matrix cones** that explains and extends ALL four of its achievements:

1. Real completely positive / copositive duality and exact rational **nonnegative Gram factorization**;
2. sharp quantitative **lattice conditioning** and arithmetic height/margin bounds;
3. **finite rational primal–dual certificates** that survive boundary, structural zeros and restricted observations;
4. the exponential **local adjacent-pivot barrier** versus polynomial-in-binary-precision **global certification** in fixed dimension.

These must arise from a **common face-aware, arithmetic rank-one invariant or equivalence**, and produce a genuinely NEW matrix-theoretic conclusion substantially **beyond ordinary CP/COP of the nonnegative orthant**. Reprinting four independent propositions and saying they are unified does not count. Nor does a change of variables \(K=G\mathbb R_+^r\), a routine push-forward of the orthant results, or the generalized-perfect-matrix theory already published in 2026.

The objective is a flagship theorem with a substantial chance of meeting a defensible **upper-quintile (top 20%) mathematical-content comparison** against papers actually published by *Linear Algebra and its Applications*, and with enough true breadth to justify assessing *Mathematical Programming A*, *Mathematics of Operations Research*, or even a broader mathematics journal. **80%+ is a comparative mathematical quality target, not an asserted 80% editorial acceptance probability.** No proof can guarantee acceptance, no revisions, or an eight-month editorial timeline.

# I. The exact matrix framework: what must be unified

Let \(K\subset\mathbb R^n\) be a **full-dimensional pointed rational polyhedral cone** supplied by rational inequalities or primitive integral extreme rays. Define the rank-one matrix cone and its dual
\[
\mathcal{CP}(K)=\operatorname{cone}\{xx^\top:x\in K\},\qquad
\mathcal{COP}(K)=\{W\in\mathbb S^n:x^\top W x\ge0\text{ for every }x\in K\}.
\tag{1}
\]
The familiar \(\mathcal{CP}_n,\mathcal{COP}_n\) are exactly \(K=\mathbb R_+^n\). Graph-constrained, structured-zero, and partially observed Gram matrix problems are obtained by prescribing a **rational linear measurement** \(\mathcal L:\mathbb S^n\to\mathbb R^m\), and either fixing \(\mathcal L(X)=b\) or requiring \(\mathcal L(X)\) to approximate rational data.

The genuinely **new** problem is to characterize, with sharp arithmetic and geometric bounds, how rational rank-one decompositions and rational separation certificates behave **relative to the facial geometry of the cone and to a measurement subspace**. This cannot simply use the known interior theorem, because rational CP boundary matrices without rational nonnegative factors have been reported in 2026.

For any rational \(A\in\mathcal{CP}(K)\) and rational linear subspace \(E\subseteq\mathbb S^n\) of *allowed perturbations* (often \(E=\ker\mathcal L\)), let
\[
\mathcal{CP}_{\mathbb Q}(K)
=\left\{\sum_{j=1}^r u_ju_j^\top:
  r<\infty,\ u_j\in K\cap\mathbb Q^n\right\}
\tag{2}
\]
and define the **structured robust rationalization set**
\[
\mathscr R_{K,E}(A)=
\left\{D\in E\cap\mathbb S^n(\mathbb Q):
\begin{array}{l}
\exists\varepsilon_0>0\quad\forall\,\varepsilon\in\mathbb Q\cap(0,\varepsilon_0),\\[-1mm]
A+\varepsilon D\in\mathcal{CP}_{\mathbb Q}(K)
\end{array}\right\}.
\tag{3}
\]
Here \(D\) must keep the required measurements EXACTLY unchanged and may be required to preserve a specified structural zero pattern. The case \(D=0\) is included only when A itself factors rationally. The set (3) is defined mathematically, not asserted decidable; an important obstacle is that unperturbed rational factorability on arbitrary boundary faces may be arithmetically difficult. An assertion of a simple finite algorithm here requires an honest decision-complexity proof.

### Grand Theorem U — precise demanding research target

Develop and prove a **non-tautological, intrinsic arithmetic facial criterion** (or a rigorous obstruction followed by the sharp corrected criterion) for existence and quantitative size of \(\mathscr R_{K,E}(A)\), together with an *equivalent or tightly linked quantitative dual certificate theorem*. The criterion must be expressed in substantive terms such as rational rank-one directions of minimal faces, exposed/non-exposed faces, lattice conditioning, copositive zeros, or a newly discovered invariant; it cannot merely restate "there exists a rational factorization."

It must yield ALL of the following as rigorous consequences of ONE principle:

**U1 — structured factorization and rationality.** Determine exactly which rational affine measurements/zero patterns permit arbitrarily small rational \(K\)-rank-one regularizations of every prescribed rational \(A\in CP(K)\) (or a sharp characterization classifying exceptional A). Where regularization is possible, construct factors with effective width and **binary height polynomial in input length and \(\log(1/\varepsilon)\) for fixed n**, with geometry/condition parameters declared. Prove a sharp dependence or a matching obstruction. The published-project orthant theorem
\[
A+\varepsilon\operatorname{Diag}(A)\in CP_{\mathbb Q}(\mathbb R_+^n),\quad
\text{all offdiagonals and zeros preserved},
\tag{4}
\]
is a **previous result**, not the grand theorem. Your theorem must give a genuinely new non-simplicial \(K\), or an important nontrivial measurement/partial-Gram family whose conclusion is not obtained from (4) by congruence.

**U2 — intrinsic sharp primal–dual lattice approximation.** For a meaningful explicit family of finite rational projective grids \(G_q(K)\subset K\cap\mathbb Q^n\), set
\[
C_{K,q}=\operatorname{cone}\{vv^\top:v\in G_q(K)\},\qquad
D_{K,q}=C_{K,q}^*.
\tag{5}
\]
Find the **exact best face-aware / measurement-compatible correction** needed to pass from \(CP(K)\) to \(C_{K,q}\), and dually from \(D_{K,q}\) to \(COP(K)\). Specify the geometry/norm used and prove the sharp rate *and constant* (or a sharp matrix-valued correction theorem), with rational extremizers. If one universal rate fails, classify the correct dependence on face, lattice shape, and measurement constraints instead of stating a false \(q^{-2}\) universality. The orthant cubical-shell constant \(\eta_q=(\sqrt{1+q^{-2}}-1)/2\) from Milestone 37 is already known within this project. Do not re-announce it. Do not claim the first grid hierarchy or the first quadratic grid rate: pre-2026 sources already have these.

**U3 — explicit arithmetic Farkas alternative under partial observations.** Derive a **total finite-precision** algorithm for rational input data that outputs either (a) a finite rational rank-one decomposition satisfying the declared structural measurements to the declared tolerance while preserving required exact entries, or (b) an exact rational \(K\)-copositive separating form with a computed strictly positive cone margin and a negative target pairing. Explain how the alternative changes on weakly infeasible affine images where no strict separator exists. Give exact bit-height, support-length, and arithmetic-time bounds for each fixed dimension. Claims must respect that nonmembers of a closed cone are strongly separable but points outside a NONCLOSED linear image may be weakly infeasible. A near-factor certificate is **not** an exact membership proof. Do not give a spurious polynomial algorithm for all variable n.

**U4 — a sharp LOCAL versus GLOBAL complexity law, not a detached example.** Show how the SAME intrinsic arithmetic/facial invariant in U1–U3 governs—or provably fails to govern—the separation between (i) adjacent-vertex minimum-ratio perfect-form shadow walks and (ii) nonlocal rational certificate generation. Extend the M2 lower/upper complexity picture to a **genuinely new matrix class**, preferably non-simplicial rational K or an important structured/partial-Gram family. A strong version would prove an exponential lower bound for **every objective-descending local adjacent rule** on a robust family of strictly positive/positive-definite nonmembers, with a matching fixed-dimension precision-polynomial nonlocal algorithm. That "every rule" claim is NOT known from current M2 work except in a special n=2 construction; treat it as a prospective conjecture, not a fact. If false, give an explicit constructive obstruction and a sharp replacement (such as a precise classification of permissible local rules or a globally optimal alternative).

These components should be **deduced from the common invariant**, not stapled together. An honest conclusion that no single invariant can control U1–U4, supported by a decisive matrix-theoretic counterexample and a stronger corrected structural theorem, can be an acceptable scientific resolution if it is comparably consequential.

## II. What would genuinely elevate linear algebra, not just this algorithm?

You must get a result with at least TWO independent matrix-theoretic consequences outside the original copositive shadow pivot. Choose the strongest genuine consequences you can prove from the new master principle, for example:

- new support- and measurement-preserving results for **rational Gram matrix completion**, graph-sparse completely positive matrices, or nonnegative matrix factorizations with prescribed entries;
- a sharp criterion detecting **arithmetic obstructions on non-exposed boundary faces** of cone-constrained Gram matrices, including implications for rational versus real factor width;
- a new sharp **intrinsic numerical condition invariant** for rank-one matrix cones, which controls both optimal dual certificate height and stability under data perturbation, with examples not congruent to the orthant;
- a sharp **face/flag theorem** for generalized perfect matrix cones with corresponding complexity consequences in a second non-simplicial cone (not just the 2026 qualitative IR property);
- a theorem for rational **affine matrix sketches** that strictly generalizes ordinary CP membership and distinguishes exact, approximate, and weakly infeasible solutions with an optimal quantitative rate.

Do not pick an application just for marketing. It must genuinely follow from your main theorem and improve on primary literature. If a claimed exact statement is contradicted by a 2026 counterexample or non-exposed face, revise the statement and prove the precise obstruction.

### Rigorous no-cheating conditions for a flagship result

1. A linearly transformed orthant \(K=G\mathbb R_+^n\), or the elementary pushforward \(CP(K)=G CP_r G^\top\) with \(K=\operatorname{cone}(G)\), does not by itself raise significance; identify what the naive pushforward **cannot** prove (intrinsic dimension rather than number of generators, sharp perturbation, face preservation, or a real new partial-measurement theorem).
2. No unqualified rational Gram factorization for **every rational boundary** CP matrix. Audit the reported September 2026 Holden and Shitov counterexamples before making rationality claims, with exact width quantifiers. If these reported examples survive verification, characterize rather than deny the arithmetic obstruction.
3. Non-exposed faces exist in CP cones. An argument that implicitly assumes every minimal face is exposed, or that one copositive witness captures all facial obstructions, is not valid.
4. The exact optimal \(q^{-2}\) constant in Milestone 37 is specific to its cubical-shell correction. Do not extrapolate its optimality to all grids, norms, or cones.
5. Known fixed-dimensional ellipsoid/support enumeration, rational interior factorization, classical Carathéodory, and Dirichlet simultaneous approximation are **antecedents**, not automatically new mathematics.
6. Polyhedral-cone IR was already generalized in **Oertel–Schürmann (2026)**. A rerun of that qualitative theorem does not pass this task.
7. The current M2 theorem refutes polynomial precision in the NUMBER of adjacent pivots for the **specified rule**. It does NOT prove all local rules are exponential, and it does NOT establish variable-dimensional separation hardness.
8. The original 2021 DSV Conjecture 3.2 was about **termination with a suitable pivot**, not a polynomial complexity guarantee. State it accurately.
9. Paper-quality math means exact quantifiers, separation of Euclidean vs projective vs lattice norms, full rank/degeneracy handling, rational height calculations, testable examples and correct primal–dual polarity.

## III. Mandatory existing project research: read BEFORE theorem design

**Repository:** Harman6139/Posterity-Files. Your results branch MUST branch from the checked quantitative M2 snapshot **98740002955f5bd9763137fc583a8d897b136ffe** (branch research/pro-m2-quantitative-checkpoints-20261114). An independent handoff branch **research/m2-unified-matrix-cones-grand-theorem-20261115** already inherits that snapshot. This baseline includes the source branch's M2 work; do not overwrite its files.

**Central M2 checkpoints** in:
https://github.com/Harman6139/Posterity-Files/tree/98740002955f5bd9763137fc583a8d897b136ffe/research/pro_m2_quantitative_20261114

Read **all nine numbered checkpoints** 00–09, specifically:

- 01_CHECKPOINT_002_SHEAR_OBSTRUCTION.md — fixed-initialization exponential paths \(N=2^{\Omega(H)}\), normal cone decomposition, grid early-stop resistance and n=2 every-descending-ray rigidity. Input formula \(P_k\), \(A_N\) provided.
- 02_CHECKPOINT_003_RATIONAL_REPLACEMENT.md — rational support-stationarity and precision-polynomial alternative, exact separating margins, ellipsoid accounting; note classical antecedents.
- 03_CHECKPOINT_004_PRIORITY_AND_SCOPE.md — DSV 2021, Dannenberg–Schürmann 2023, 2026 geometric context.
- 04_CHECKPOINT_005_SHARP_MARGIN_AND_COMPLEXITY.md — quantitatively SHARP \(\min_{x\ge0,\|x\|=1} x^\top Px \gtrsim_n M^{-(n-1)}\), matching perfect positive-definite unimodular-shear examples, height and pivot upper bounds.
- 05_CHECKPOINT_006_DNN_EXPONENTIAL_PATHS.md — strongly improved exponential pivot instances that are **positive definite and entrywise nonnegative**, so simple PSD pretesting fails.
- 06_CHECKPOINT_007_COMPLETIONS_AND_ROBUSTNESS.md — strictly entrywise-positive perturbations, a quantitative **rational-polyhedral K cone** IR bound already proved, fixed-dimensional precision-polynomial primal/separator completion and exact bit resources. THIS PREVENTS treating a simple K-bound as new.
- 07_BENCHMARK_PROTOCOL.md — preregistered ten-paper samples for LAA and Mathematical Programming, not yet a completed 8/10 full-paper audit.
- 08_CHECKPOINT_008_MANUSCRIPT_AND_INDEPENDENT_TESTS.md — local 20-page complete manuscript reported compiled, exact and independently checked certificates; online .tex package only partially uploaded.
- 09_CHECKPOINT_009_CANONICAL_START.md — **canonical tridiagonal** initial vertex has exponentially long forced unmodified shadow paths on strictly positive PD nonmembers, with an exact normal-cone parameter interval. The corrected-grid test is forced to descend **within** the window, but its early behavior before the window is not fully excluded. This distinction is essential.

Also read the independent older M2 branch research/pro-m2-copositive-quantitative-20261114, especially STATUS.md and its source data, to detect proof or scope conflicts rather than taking one branch as automatically authoritative.

**Original project results** in:
https://github.com/Harman6139/Posterity-Files/tree/22ed4becd320695b41f8a11f1223ea090ef89ecf/research/laa_two_basis_track02_20261112

- **37_SHARP_CUBICAL_CERTIFICATES_AND_RATIONAL_CP_REGULARIZATION.md:** optimal shell coefficient \(\eta_q\), independent coordinate rounding and exact preservation of every offdiagonal, \(\varepsilon I\) and \(\varepsilon\operatorname{Diag}(A)\) rational factorization preserving zero pattern, polynomial certificate length, exact objective-aware dual test.
- **12_RECIPROCAL_ESCAPE_LAW_AND_SHARP_DIMENSIONAL_BOUNDS.md** and related SDP universality results if analyzing weakly infeasible affine Gram sections; avoid presenting their classical semialgebraic Puiseux consequences as new CP theorems without proof.
- **34_SHADOW_PIVOT_AND_COPOSITIVE_TERMINATION.md** was an earlier conversation artifact reportedly not fully committed to the source repository. The finite termination argument is restated in 37 and M2. DO NOT claim you retrieved a nonexistent file.

Read all proof files and source code, including saved rational checkers and the canonical certificate, before deciding which theorem is actually new. Confirm which full LaTeX sections are still missing online, and package complete verified results.

## IV. Primary literature and historical priority — mandatory

Use primary publications and **current 2026** developments, not generic descriptions or old manuscript abstracts:

1. Dutour Sikirić, Schürmann, Vallentin, *Rational factorizations of completely positive matrices*, **LAA 523 (2017), 46–51**, DOI 10.1016/j.laa.2017.02.017. Rational interior result.
2. Same authors, *A simplex algorithm for rational cp-factorization*, **Mathematical Programming 187 (2021), 25–45**, DOI 10.1007/s10107-020-01467-4, arXiv:1807.01382. Exact Conjecture 3.2 and Ryshkov rule.
3. Dannenberg–Schürmann, 2023 perfect copositive matrices and shear/adjacency (full Communications in Mathematics article, including all propositions). Structural shear vertices are prior art.
4. Oertel–Schürmann, *Generalized Perfect Matrices*, arXiv:2602.05841 (2026), **full v2**. Extends qualitative IR and rational certificates to rationally generated cones; the exact novelty boundary.
5. Yıldırım (2012), de Klerk–Laurent–Sun (2015), de Klerk–Laurent–Sun–Vera (2017): polyhedral grids, convergence rates and concentration methods. Pin exact optimal constants and assumptions.
6. Nishijima–Lourenço, *Facial structure of copositive and completely positive cones over a second-order cone*, **LAA 743 (2026), 211–249**, DOI 10.1016/j.laa.2026.04.019. A serious **non-orthant** structural benchmark.
7. Kostyukova (2025), *Non-exposed polyhedral faces of the completely positive cone*, **Linear and Multilinear Algebra 73 (2025), 368–395**, DOI 10.1080/03081087.2024.2346313. Do not assume facial exposedness.
8. Holden (13 Sept 2026), *A rational completely positive matrix with no rational nonnegative factor*, reported order 444/rank 7, repository https://github.com/ajt60gaibb/OpenProblemsInNLA ; and Shitov (Sept–Nov 2026), another reported finite-width obstruction. They require critical audit; do not treat unrefereed computational manuscripts as automatically settled history, but don't ignore them.
9. Original 2017–2026 articles on matrix completion, graph-completely-positive matrices, factor-width restrictions, nonnegative/PSD matrix factorizations, and Hilbert bases. Find new sources through current search.
10. Klee–Minty, Zadeh-pivot lower bounds, parametric LP, arithmetic complexity and real-algebraic algorithms for comparison ONLY; a transfer to those models requires an actual reduction preserving pivot rules.

**Historical priority is a hard gate.** An already known fact, an invented implication, or an uncited generalization is grounds to reject the proposed manuscript upgrade.

## V. Publication standard and sample protocol

The manuscript's **current most credible target** remains *Linear Algebra and its Applications*. If your NEW master theorem really links arithmetic Gram factorization, duality, and sharp local/global complexity in a framework relevant to other matrix classes, assess whether **Mathematical Programming A**, **Mathematics of Operations Research**, **Advances in Applied Mathematics**, or **Bulletin of the London Mathematical Society** is justified. AAM needs genuine structural/combinatorial matrix applications; an abstract copositive algorithm is not enough. Do not sacrifice subject fit to name prestige.

User's practical preference: ideally a decision/acceptance within eight months after submission, with no revisions. These are NOT controllable; report genuinely sourced 2025–2026 submission-to-final-acceptance data where possible and note revisions uncertainty.

**Upper-20% ("80%+") publication gate**:
- Independently review correctness with adversarial proof checking.
- Show novel theorem and at least TWO substantive applications outside the original orthant shadow-pivot problem.
- Obtain a registered comparison against at least **12 real published papers for LAA** (two issues across 2024–2026 plus 4 near-topic comparator papers) and at least **10 per each aspirational venue**. Read full theorems and proofs when accessible; supply DOI, exact distinguishing feature and a substantive multidimensional rubric. Do not infer 80% acceptance probability or cherry-pick a weak issue.
- Require a defensible >=80th-percentile mathematical **substance** result, with uncertainty and no claim of calibrated editorial probabilities. Prior ten-paper source check was incomplete; completing it honestly is mandatory.
- Target a coherent self-contained 20–30-page manuscript with main theorem, nontrivial matrix consequences, proof, sharp examples, counterexamples at necessary assumptions, and a minimal reproducibility supplement. Move routine prior orthant proofs or long computational implementation details to appendices.
- Editor should see **one high-consequence structural theorem that future matrix theorists can invoke**, not an omnibus collection of separate algorithm lemmas.

## VI. Attack protocol — maximum analytical focus

**First**, derive the exact framework of rational rank-one rays on *minimal faces* and formulate a quantitative candidate invariant. Test its invariance under rational congruence, behavior under non-simplicial cones, preservation of zeros, and dual separation. Be especially careful with exposed vs non-exposed faces and arithmetic rank-one rays. Treat the Holden example as a potential adversarial test.

**Second**, seek the decisive "primal factorization if and only if quantitative facial dual certificate" mechanism; it might be a **conditional theorem requiring a rationally generated facial cone**, or an obstruction via an irrational extreme-ray face. Make the exact necessary/sufficient condition non-tautological. Use Puiseux or Diophantine height estimates only with declared dependence.

**Third**, derive the optimal grid and bit-certificate bounds and the *local/global* complexity dichotomy from that invariant, not from unrelated sources. Test on the orthant baseline and at least one nonsimplicial cone + actual graph/partial Gram measurement.

**Fourth**, aggressively search for counterexamples to your general formulation. If it fails, PROVE failure, identify exactly why (arithmetic obstruction, nonexposedness, nonclosed image, NP-hardness, or deficient input model), and derive the strongest corrected, truly reusable theorem. Do not retreat to one more small example.

**Fifth**, write the complete paper-level proof and run independent exact arithmetic checks. Keep the central proof analytical; numerical experiments cannot certify an all-dimensional statement. Explicitly separate proved, conditional, conjectured, false, and historically anticipated facts.

You have freedom to abandon the proposed invariant or reformulate the framework if a more profound connection emerges. But the resulting theorem **must truly unify rank-one factorization, dual separation, sharp arithmetic conditioning, and local/global algorithmic geometry**, or else the goal remains unmet. No case-by-case strategy or brute-force search over proof routes.

## VII. Exact deliverables and GitHub preservation

1. Inherit the complete source baseline and latest M2 checkpoints from commit **98740002955f5bd9763137fc583a8d897b136ffe**. Work on an independent RESULTS branch named, for example, research/pro-m2-grand-arithmetic-matrix-cones-20261115, not this handoff branch. Never overwrite original checkpoints. Commit all advances and explicit failed routes as numbered milestones.
2. Produce **MASTER_THEOREM.tex** (submission-quality), **COMPLETE_PROOFS.md**, **SHARP_EXAMPLES_AND_COUNTEREXAMPLES.md**, **NOVELTY_AND_PRIORITY_AUDIT.md**, **ARTICLE_LEVEL_VENUE_BENCHMARK.md**, and **STATUS_PROVED_NOT_PROVED.md**. Include independent exact verifier scripts for arithmetic claims, tests and saved results; preserve working code in the results branch. A local PDF without uploaded source is not full delivery.
3. State exact complexity by matrix order n, number of cone generators/facets, input bit length, distance gap, requested precision and measurement size, distinguishing query count / arithmetic operations / bit operations / output certificate height.
4. Verify eventual GitHub commits and supply exact branch and SHA. No silent background research promises.
5. **Do not declare success** if the result is only another special-pivot lower bound, simple qualitative generalized perfectness, a transformed orthant, or a restatement of the old grid correction. An honest unresolved result is better than a false flagship theorem.

## VIII. The ultimate target

A future paper that can accurately claim something like:

> *A sharp arithmetic matrix-cone duality theorem characterizes when rational rank-one Gram representations persist under structural observations, provides optimal primal and dual lattice certificates, and explains the exponential complexity gap between local face walks and nonlocal conic certification. It applies to completely positive matrices and genuinely broader structured matrix families.*

**This is a TARGET ABSTRACT, not an achieved result. Prove it in a form that is true, or rigorously replace it with a comparably deep statement after discovering the obstruction.**

Your research contribution is measured by a correct, novel, general master theorem and its proven consequences—not how forcefully the conclusion is described.
