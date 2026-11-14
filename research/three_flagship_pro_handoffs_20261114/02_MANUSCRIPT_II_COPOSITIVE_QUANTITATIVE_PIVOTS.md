# PRO RESEARCH HANDOFF 02 — QUANTITATIVE FINITE COPOSITIVE SEPARATION AND A STRONGER SHADOW-PIVOT THEOREM
**Prepared 2026-11-14.** Independent fresh Pro chat. Research Track II of three. **Read this complete handoff and sources before research.**

## A. The precise publication-changing problem

Manuscript II presently proves finite termination of a rational shadow-pivot algorithm for separating a matrix outside the completely positive cone and sharp finite-lattice certificate corrections. Finite termination by itself is weaker than a useful complexity theorem.

Your ONE central problem is to turn that qualitative theorem into a quantitative and mathematically consequential **shadow-pivot complexity theory**. For rational \(A\in\mathbb S^n\), assume \(A\notin\mathcal{CP}_n\), normalize \(\|A\|_F\le1\), let \(L\) be the total binary input length, and set
\[
\delta=\operatorname{dist}_F(A,\mathcal{CP}_n)>0,\qquad
H=L+\lceil\log_2(1/\delta)\rceil+2.
\]
The original algorithm moves among vertices of the infinite Ryshkov polyhedron
\[
\mathcal R_n=\{P\in\mathbb S^n:v^TPv\ge1\ \forall v\in\mathbb Z_{\ge0}^n\setminus\{0\}\}.
\]
At vertex \(P\), \(\operatorname{Min}(P)=\{v\ne0:v^TPv=1\}\) and \(\mathcal V(P)=\operatorname{cone}\{vv^T:v\in\operatorname{Min}(P)\}\). Choose an initial vertex \(P_0\), set the strictly interior CP anchor \(C_0=\sum_{v\in\operatorname{Min}(P_0)}vv^T\), and among extreme feasible tangent rays \(R\) with \(\langle A,R\rangle<0\), choose the minimum ratio
\[
\boxed{R_* \in \arg\min_{\langle A,R\rangle<0}
       \frac{\langle C_0,R\rangle}{-\langle A,R\rangle}.}\tag{II-rule}
\]
If a tested ray is copositive, it separates \(A\); if not, traverse the bounded edge to its adjacent vertex. A sharp finite-grid theorem now lets one replace total copositivity classification by a finite rational descent-or-certificate test.

### Target Theorem II (quantitative frontier)

Prove, for **every fixed matrix order \(n\)**, an explicit polynomial-in-binary-precision bound on the number of pivots of this *specified rule*, for arbitrary rational nonmembers and arbitrary degeneracies:
\[
\boxed{\#\mathrm{adjacent\ vertex\ pivots}
\ \le\ C(n)\,H^{c(n)}.}\tag{II}
\]
Give meaningful, explicitly bounded \(C(n),c(n)\), an exact bound on intermediate vertex/ray bit heights and practical certificate length, and a corresponding *complete* rational arithmetic implementation of the ray test and neighboring-vertex subroutine. Ideally obtain \(C(n)\le2^{\mathrm{poly}(n)}\), \(c(n)\le\mathrm{poly}(n)\), plus a matching lower-bound family or optimality mechanism. This would make the initial conjecture-resolution paper substantially stronger. Distinguish complexity in fixed \(n\) from polynomial time in **variable** \(n\): arbitrary-dimension polynomial separation would run into known CP/COP decision hardness, and should not be claimed without confronting that implication.

This precise polynomial-in-\(H\) pivot bound is a **proposed new theorem**, NOT an established fact. It might be false. If so, construct an explicit rational family of inputs and prove a superpolynomial pivot lower bound for (II-rule), then develop and prove an analytically motivated improved pivot rule or a sharp alternative complexity invariant yielding a comparably consequential general theorem. Simply giving a slow numerical run or a small counterexample is NOT flagship success. A proof with dependency \(\delta^{-O(n)}\) rather than \(\mathrm{poly}(\log1/\delta)\) does not resolve (II).

The desired organizing insight is an arithmetic/convex-geometric Lyapunov function controlling **face transitions and integer-vector heights**, not another volume-count of all possible visited Ryshkov vertices in a large Euclidean ball. Existing compactness gives finiteness only; its crude finite-region vertex count can grow exponentially in \(H\).

## B. Current exact results to build upon

GitHub repository: Harman6139/Posterity-Files.
Baseline source commit: **22ed4becd320695b41f8a11f1223ea090ef89ecf**.
Branch: laa-track02-gptpro-analytic-frontier-20261112.
Research directory:
https://github.com/Harman6139/Posterity-Files/tree/22ed4becd320695b41f8a11f1223ea090ef89ecf/research/laa_two_basis_track02_20261112

Read all of **37_SHARP_CUBICAL_CERTIFICATES_AND_RATIONAL_CP_REGULARIZATION.md**, **00_MANUSCRIPT2_SHARP_GRID_STATUS.md**, and the original primary article:
Dutour Sikirić–Schürmann–Vallentin, *A simplex algorithm for rational cp-factorization*, Mathematical Programming 187 (2021), 25–45, Conjecture 3.2; DOI 10.1007/s10107-020-01467-4, arXiv:1807.01382.
The uncommitted earlier Milestone **34_SHADOW_PIVOT_AND_COPOSITIVE_TERMINATION.md** was distributed as a conversation file; if not found in connected GitHub, do NOT pretend it is there. The key exact mathematical content is fully restated here and in milestone 37, and the user can additionally attach the original 34 proof if needed. The self-contained paper must not rely on an inaccessible file.

### Already obtained but not historically priority-certified

1. A minimum-ratio continuation invariant: each visited \(P_k\) minimizes \(C_0+\lambda_k A\) over \(\mathcal R_n\), with \(\lambda_k\) nondecreasing. Separation gives a finite bound \(\lambda_k\le\Lambda\). Before returning a separator, \(\langle A,P_k\rangle\ge0\). Interior anchor coercivity \(\langle C_0,P\rangle\ge\kappa_n\|P\|_F\) bounds all nonterminal vertices. Local polyhedral finiteness and strict objective descent imply finite termination. This is the core finite-path proof; verify the exact normal-cone and degeneracy assumptions against the published algorithm.
2. Explicit starting tridiagonal perfect matrix \(P_0\) with diagonal 1, adjacent offdiagonal \(-1/2\), otherwise 0; active vectors are consecutive-interval indicators. The anchor has \((C_0)_{ij}=\min(i,j)(n+1-\max(i,j))\).
3. Sharp cubical-shell approximation. Let \(V_{n,q}=\{v\in\{0,\ldots,q\}^n:\max_i v_i=q\}\), \(K_{n,q}=\operatorname{cone}\{vv^T:v\in V_{n,q}\}\), and \(D_{n,q}=K_{n,q}^*\). The exact least correction constant for both
\[
 A+\eta_q\operatorname{tr}A\,I\in K_{n,q}\quad(A\in CP_n),\qquad
 Q+\eta_q\operatorname{tr}Q\,I\in COP_n\quad(Q\in D_{n,q})
\]
is \(\eta_q=(\sqrt{1+q^{-2}}-1)/2\), with a dimension-two sharpness example. Existing literature has grid hierarchies and second-order convergence; novelty is NOT the first \(O(q^{-2})\) rate.
4. For every rational CP \(A\), adding any positive rational \(\epsilon I\) or \(\epsilon\operatorname{Diag}A\) permits rational nonnegative Gram factors preserving all offdiagonal entries; at most \(2n(n+1)\) factor columns and polynomial-size arithmetic certificates are claimed. NOT polynomial discovery time or universal unperturbed rational factoring.
5. Every finite grid level gives exact rational primal factor of the corrected matrix OR a true copositive separator of the uncorrected target. Refinement terminates on every nonmember but naïvely enumerates exponentially many grid points.
6. Objective-dependent finite test: for a candidate \(R\) with \(g=-\langle A,R\rangle>0\), \(h=\operatorname{tr}(A)\operatorname{tr}(R)\), set \(\eta=g/(2h)\) if \(h>0\), otherwise \(\eta=1/4\); choose \(q\) with \(4q^2\eta(1+\eta)\ge1\). A negative integer quadratic value yields a noncopositivity witness; otherwise \(W=R+\eta\operatorname{tr}(R)I\) is a true separator. It may not decide whether \(R\) itself lies on COP boundary, and need not. Milestone 37 also proves strict margin and exact neighbor existence and includes test code.

### Crucial external 2026 and earlier priority context

- Oertel–Schürmann, *Generalized Perfect Matrices* (2026): general rational cone certificates and perfect-matrix theory. Verify whether its finite certificates or pivot argument already imply the proposed theorem.
- Yıldırım (2012), de Klerk–Laurent–Sun (2015), de Klerk–Laurent–Sun–Vera (2017): finite lattice/polyhedral approximation rates and coefficient comparisons.
- Dutour Sikirić–Schürmann–Vallentin (2017, 2021): rational interior factorization and Ryshkov simplex context.
- Two **September 2026 reported counterexamples** to unrestricted rational boundary CP factorization: Holden (integer order-444 example; proof on repository ajt60gaibb/OpenProblemsInNLA) and Shitov (reported order-308 construction, Zenodo Nov 2026). Do not claim the old universal rational factorization conjecture positively or as still open; audit these first if relevant. Our new complexity theorem is independent of their correctness.

## C. How to make this an upper-quintile paper rather than more machinery

**Journal ladder:** First choice **Linear Algebra and its Applications** (best current editorial fit, user wants an eight-month decision); prestige-level upgrades **Mathematical Programming Series A** or **Mathematics of Operations Research**, if a genuinely useful algorithmic complexity/structural theorem is established. **Advances in Applied Mathematics** is a preference but its 2025 output is mostly algebraic combinatorics; target it ONLY if a substantial new discrete lattice or algebraic cone theorem with outside applications emerges. JOTA is an optimization alternative but its reviewed timing is not favorable to a strict eight-month deadline.

The user's "80%+" requirement must be operationalized as a *top-20%-of-recent-published-paper substance* target, not invented editorial probability. Do a new preregistered **10+ published-paper comparison PER candidate venue** (two or more actual issues, reproducible random or consecutive selection plus closest-topic controls). Compare full theorem and proofs, not article abstracts, along independent axes: correctness, genuine novelty, theorem depth, broad relevance, fit, constructive usefulness, exposition. Certify an 8/10 comparative pass ONLY if the result truly warrants it and priority is independently established. Report DOIs, sample protocol, actual mathematical differences, limitations, and reliable current journal handling times. Do not equate this with an 80% acceptance chance or guarantee an eight-month result.

The mathematical win should be strong enough that an editor sees one new high-consequence theorem, not a stitched collection of unrelated CP lemmas. Supply a polished manuscript with all prerequisites and exact pseudocode.

## D. Nonnegotiable research discipline and deliverables

- Attack the full quantitative frontier analytically. First check for fast hidden paths at faces, rational vertex-height growth, cycling under degeneracy, and whether the minimum-ratio pivot objective has a discrete potential with increments bounded below by inverse-polynomial \(H\). If false, find a universal obstruction and a mathematically superior corrected rule; do not just tabulate dimensions \(n=2,3,4,\ldots\).
- State all complexity resources separately: pivot count, bit length of visited objects, number and size of integer oracle tests, arithmetic cost, and dependence on \(n,L,\delta\). An exponential number of finite tests is not polynomial complexity.
- Prove the exact original conjecture's statement, if cited, from the original primary source, and fully distinguish milestone 37's known facts from genuinely new output. Be open to finding a proof error; correct it.
- Deliver the complete theorem or a decisive formal disproof plus a sharp general replacement, self-contained paper-quality proofs, exact rational tests with reproducible inputs, source comparison, and a final journal-and-percentile decision. Do not claim historic novelty without checking the 2026 literature.
- Commit to an **independent research branch**, e.g. research/pro-m2-copositive-quantitative-20261114, never overwrite source milestones; include a structured PROVED/UNRESOLVED status. If connector writes are unavailable, provide uploadable files and say so.
- Work toward complete closure within the attempt, not a series of small numerical cases. If the proposed quantitative theorem remains unresolved, say explicitly so; never relabel another grid refinement as the required breakthrough or imply asynchronous continuation.

**Success means a fully rigorous complexity-changing theorem (or sharp disproof with genuinely consequential replacement) PLUS a defensible upper-quintile venue comparison. Nothing less should be marketed as the flagship breakthrough.**
