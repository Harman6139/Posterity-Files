# PRO RESEARCH BRIEF 03 — Sharp, checkable sufficient conditions for stable recovery from two bases

## North-star theorem

Find a **natural and verifiable structural criterion** that explains when unique recovery from two orthonormal bases is actually stable, and when high-order degeneracy can cause weak Hölder exponents. A complete positive theory would directly answer the editorial concern that the existing paper presents only negative examples.

Aim for a theorem of the form:

> For a meaningful class of pointwise uniquely recoverable PSD targets \((U,X_*)\), explicit geometric/spectral conditions on the two measurement bases, the target range, and/or a dual certificate guarantee a sharp recovery estimate (ideally Lipschitz, or provably optimal square-root/Hölder), with quantitative constants. Conversely, characterize why the exceptional rank-two constructions violate these conditions. When feasible, provide necessary-and-sufficient conditions or a sharp stability classification.

**Do not assume Lipschitz recovery is generically possible** at an isolated boundary point of the PSD cone with only two bases; investigate whether tangent-cone dimension or positivity constraints rule out the strongest proposed statement.

## Research program

1. **Start from an exact local geometry formulation.** Define the feasible cone near \(X_*\), appropriate tangent/contingent directions, and the measurement kernel. Investigate whether a quantitative separation \(\|\mathcal A_U(H)\|\ge c\|H\|\) on feasible tangent directions is necessary/sufficient for a local Lipschitz error bound against **all** PSD competitors. If true, prove it with correct cone definitions, closure issues, and norm constants; if false, give an explicit counterexample. A bare appeal to an abstract inverse-function theorem does not count.
2. **Develop certifiable PSD dual-stress criteria.** Look for \(S=\mathcal A_U^*(y)\succeq0\) with \(SX_*=0\), quantitative spectral gap on \((\operatorname{ran}X_*)^\perp\), and sufficient injectivity of measured forms restricted to the exposed face. Determine exactly whether this yields exponent \(1/2\), Lipschitz under additional transversality, or a deeper hierarchical exponent. Derive explicit error constants from stress gaps and singular values. Avoid the common mistake of claiming Lipschitz where PSD cross-block leakage only admits a square-root estimate.
3. **Find a natural broad class.** Investigate strict complementarity/nondegenerate dual certificates, rank-restricted phase retrieval, PSD matrix completion, low-rank Gram estimation, or structured two-basis tomography. Specify which objects are measured and whether uniqueness is pointwise or global. Seek a class where your criterion is *satisfiable and nontrivial* with **positive measurements and an entrywise-nonzero orthogonal basis change**.
4. **Pursue a sharp dichotomy or hierarchy.** Can a finite facial-reduction chain, its certificate gaps, and the restricted measurement map determine a sharp exponent? The draft gives examples of the same depth with exponents \(1/(2k)\) and \(2^{-k}\), so depth alone cannot work. Identify an additional invariant (e.g., order of contact, polynomial vanishing multiplicity, error-bound modulus, stratified transversality) and prove both a sufficient estimate and matching examples. A necessary-and-sufficient criterion for the local Hölder exponent would be outstanding.
5. **Explore probabilistic/generic consequences carefully.** If a Haar-random second basis plus a natural target distribution has pointwise uniqueness, investigate whether a quantitative stability condition holds with high probability and what constants depend on \(n\). First check that the stated uniqueness event is actually possible under the measurement count; do not assert it by intuition. Alternatively prove a deterministic impossibility for generic pairs and derive the sharp result on an appropriate identifiable stratum.
6. **Use the two existing families as discriminating tests**: one has rank-two, maximal depth \(n-2\), sharp exponent \(1/[2(n-2)]\); another has depth \(k\) and sharp exponent \(2^{-k}\). Show the criterion diagnoses both correctly. Add at least one genuinely natural **positive example** with proven stable rate, ideally one not reverse-engineered from the pathology.

## Prioritization of ambitious deliverables

**A (ideal):** A useful **necessary-and-sufficient geometric criterion** for Lipschitz or specified Hölder recovery under two-basis measurements, including quantitative bounds, an exact genericity/rarity theorem, and concrete cases satisfying the criterion.

**B (strong):** A sharp, checkable **sufficient-condition theorem** guaranteeing at least square-root or Lipschitz recovery, plus matching examples and a proof that the current pathological family violates its hypotheses.

**C (valuable):** If the strongest rates are impossible with two bases, prove the corresponding impossibility theorem and the **maximal achievable** positive stability guarantee for a natural nondegenerate class. A generic “assuming a positive stability constant” rephrasing is not an advance.

## Critical literature and proof tests

Audit metric subregularity, strong regularity, facial reduction, restricted injectivity, nullspace/tangent-cone conditions, phase retrieval, semidefinite completion, and quantitative PSD perturbation bounds. Precisely separate known variational-analysis criteria from any new theorem here; the result must contribute more than repackaging a textbook condition. For every proposed condition, provide a finite-dimensional check/certificate and estimate, prove all-rank competitor coverage, and state whether the constant is instance-dependent or uniform in dimension. Attack your own theorem using singular PSD blocks and directions with quadratic contact.

Deliver a mathematically deep positive theory that places the extreme-instability examples in a broader landscape.

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