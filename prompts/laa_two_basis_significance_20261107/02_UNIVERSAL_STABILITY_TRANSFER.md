# PRO RESEARCH BRIEF 02 — A sharp stability-transfer principle from PSD graph completion to two orthonormal bases

## North-star theorem

Convert the existing **exact-feasible-fibre graph-completion embedding** into a general theorem about **noisy recovery rates**. The editor rightly noted that an embedding of exact solutions and specially chosen obstruction curves does not automatically explain the behavior of other inverse problems. Your task is to close that gap as generally and sharply as mathematics permits.

Ideally prove a universal transfer principle:

> Given any real PSD graph-completion instance \((G,C_*)\) uniquely determined by its known diagonal/edge entries, with optimal graph recovery exponent \(\alpha_G\), construct two orthonormal bases and a uniquely recoverable PSD target \(X_*\) with positive observations and no zero basis overlaps, such that the **optimal local two-basis exponent** is determined by a sharp explicit law in terms of the original graph problem and any necessary geometric invariant. Prove both directions against **every ambient PSD competitor**, not only perturbations lying in the embedded subspace.

A particularly strong outcome is **exact exponent preservation** across a general class, or a necessary-and-sufficient criterion for preservation versus loss. Do **not** presume exact preservation is possible for all graph problems; identify and prove the correct universal law if an extra square-root loss is inevitable.

## Exact starting interfaces

For graph \(G\) with \(m\) vertices and \(e\) edges, define \(\pi_G(B)=((B_{ii}), (B_{ij})_{ij\in E})\). The manuscript claims an explicit \(F\in\mathbb R^{(m+1)\times(3m+2e+2)}\) with \(FF^\top=I\), \(U=2F^\top F-I\), and \(X_*=F^\top(C_*\oplus[1])F\). Its exact-data fibre is \(\{F^\top(B\oplus[1])F:B\succeq0,\pi_G(B)=\pi_G(C_*)\}\). A measured dual certificate \(S_0=D+UDU\succeq2Q\) forces exact feasible competitors into \(V=\operatorname{ran}F^\top\), and depth transforms as \(k\mapsto\max\{1,k\}\). Inside the embedded space, \(\|\cdot\|_F\) is preserved and residuals are comparable. The missing interface is **quantitative control of noisy off-subspace competitors**.

## Required research steps

1. **Define the graph exponent cleanly** using \(\|B-C_*\|_F\le C\|\pi_G(B)-\pi_G(C_*)\|_2^{\alpha}\) for all \(B\succeq0\). Do not confuse exact uniqueness with numerical conditioning. Determine precisely how the two-basis exponent can depend on \(\alpha_G\), facial-reduction depth, dual stress rank/gaps, geometry of \(C_*\), and measurement constants.
2. **Prove a quantitative near-fibre decomposition.** Given arbitrary \(Y\succeq0\) with small \(\delta=\|\mathcal A_U(Y)-\mathcal A_U(X_*)\|\), use \(S_0\) to bound the mass on \(V^\perp\), off-diagonal blocks, and the error of compression into \(V\). Produce an explicit *PSD repair/retraction* or comparable surrogate \(B\succeq0\) for the graph model, with rigorous residual and distance estimates. This is where many plausible transfer assertions silently fail.
3. **Search for an exact transfer exponent.** Test hypotheses such as a formula \(\alpha_{\rm lifted}=\min\{\alpha_G,\beta\}\) for a universal transversality exponent \(\beta\), or a more refined law using dual certificates. **These are conjectural probes, not facts.** Prove or refute them on explicit examples. Determine whether embedded graph curves exhaust the worst ambient perturbations.
4. **If the present reflection is too restrictive, invent a stronger embedding.** The current construction has \(U X_* U=X_*\), so its two measured lists coincide on the embedded target. Explore non-reflection orthogonal changes of basis, measurements that are genuinely distinct on the target, quantitative near-identity/nonzero-overlap bounds, or additional redundant frame data. Preserve exact target uniqueness and meaningful rank/depth behavior. Provide full construction, not a hand-waving dilation.
5. **Realize diverse natural graph-completion phenomena** in two bases: universal rigidity/stress-matrix examples, framework rigidity, sparse chordal versus nonchordal completion, high singularity degree, and cases with known sharp exponents. Determine what *new theorems about two-basis recovery* follow and whether any sharp rates or structural classifications transfer.
6. **Prove optimality and scope** by constructing matching arbitrary-ambient curves or proving they cannot dominate embedded ones. Check exact normalization, all-rank competitors, \(k=0,1,2\), positive measurements, algebraicity of \(U\), and every dimension formula.

## Acceptable final theorem strength

**A (ideal):** A **universal bi-Hölder equivalence / sharp exponent law** between uniquely completable PSD graph problems and two-basis recovery, with explicit transformation of ranks, dimensions, depth, and constants.

**B (strong):** A sharp transfer theorem for a **broad, checkably defined class** of graph instances (e.g., strict stresses or a specified family of singularity chains), proving both universal upper bounds and matching worst-case curves.

**C (valuable if A/B false):** An explicit no-go theorem identifying the exact obstruction to general exponent preservation, followed by a corrected quantitative transfer theorem that is genuinely stronger than the current one-way curve transfer. Mere restatement of the existing exact-fibre identity is insufficient.

## Hostile audit requirements

Attempt an off-subspace PSD perturbation that has very small data residual but destroys the expected graph exponent. Track all quadratic cross terms and whether a compressed matrix retains the fixed anchor block and its PSD property. Distinguish *comparable residuals on the embedded image* from *uniform error bounds over the entire ambient cone*. Cite prior SDP error-bound and completion theory accurately; verify this is new rather than a repackaged metric-regularity statement.

The objective is a general mathematical tool usable by researchers with other PSD recovery problems, not just one new example.

# Shared mathematical setting and proof standard

The project concerns the 25-page research manuscript *Unique Rank-Two Recovery in Two Bases Can Be Arbitrarily Unstable*, previously submitted to *Linear Algebra and its Applications*. Editorial feedback: the sharp examples are understood, but their broader significance beyond specially constructed degenerate instances and the implications of the graph-completion embedding are not sufficiently established. Your mandate is **a new mathematical result**, not an exposition rewrite.

Let \(\mathbb S^n_+\) denote the real symmetric positive-semidefinite matrices and \(U\in O(n)\). The measured data are
\[
\mathcal A_U(X)=(\operatorname{diag}X,\operatorname{diag}(U^\top XU))\in\mathbb R^{2n}.
\]
For a pointwise uniquely recoverable target \(X_*\succeq0\), meaning \(\{X\succeq0:\mathcal A_U(X)=\mathcal A_U(X_*)\}=\{X_*\}\) **among all PSD competitors of unrestricted rank**, define its optimal local exponent \(\alpha_*(U,X_*)\) as the supremum of \(\alpha>0\) for which some \(C,\varepsilon>0\) satisfy
\[
\|X-X_*\|_F\le C\|\mathcal A_U(X)-\mathcal A_U(X_*)\|_2^\alpha
\]
for every \(X\succeq0\) with residual below \(\varepsilon\). When claiming an *attained optimal* exponent, prove the inequality **at** that exponent and disprove every larger exponent; do not equate a supremum with attainment without proof. Constants may depend on the fixed instance unless a theorem explicitly states uniformity.

**Draft baseline (claimed results, not automatically independently verified):** For every \(n\ge3\), an explicit rank-two trace-one \(X_*\), orthogonal \(U\) with no zero entry, and strictly positive observations give pointwise uniqueness and sharp exponent \(1/[2(n-2)]\), with facial-reduction depth \(n-2\). The mechanism converts the two diagonal lists to values of \(p(z)=z^{2(n-2)}(1+z^2)\) at positive nodes. A second theorem starts from *any* uniquely solvable real PSD graph-completion problem on \(m\) vertices and \(e\) edges, and lifts it to dimension \(N=3m+2e+2\), with an orthogonal reflection \(U=2F^\top F-I_N\), strictly positive data and nonzero entries of \(U\). It identifies the **exact feasible fibre**, preserves positive facial-reduction depth (zero becomes one), and preserves Frobenius distances and measurement residuals up to constants **along embedded curves**. It does **not** already prove a sharp two-sided transfer law for arbitrary ambient noisy competitors. A separate family reaches exponent \(2^{-k}\) at facial-reduction depth \(k\).

**Research discipline:** Work as though a major theorem is obtainable; pursue multiple *genuinely different* routes and push each through its hardest technical obstruction. Exhaust direct proofs, structural reductions, and counterexample attempts before conceding a route. Do not declare victory using numerical tests, handwaving, hidden extra assumptions, an equivalent unproved lemma, or a literature reference whose hypotheses are unchecked. Explicitly check real-versus-complex, exact data versus noisy data, pointwise uniqueness versus global injectivity, fixed rank of target versus arbitrary-rank competitor, varying \(n\), normalization, and the meaning of “generic” or “robust”. If an ambitious target is false, prove a meaningful no-go theorem and continue toward the strongest true replacement. Never fabricate a proof because the task asks for a breakthrough.

**Deliver one standalone research memorandum**, not a progress log or manuscript rewrite: precise best theorem(s); complete proofs; nontrivial examples/counterexamples; comparison with baseline; hostile self-audit; and a brief priority/novelty check with verifiable bibliographic references (including recent literature, as far as available). Clearly label theorems that are proved, conjectures, and unresolved gaps. The objective is results capable of materially changing the publication significance of this paper.