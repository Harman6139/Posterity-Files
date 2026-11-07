# PRO RESEARCH BRIEF 01 — Is extreme two-basis instability structurally robust?

## North-star theorem

Prove the strongest **structural/naturality theorem** showing that arbitrarily poor local recovery is not merely a lone engineered PSD matrix. Ideally establish:

> For every \(\eta>0\), there is \(n\) and a **positive-dimensional, nontrivial family** of pairs \((U,X_*)\), with \(U\in O(n)\), \(X_*\succeq0\) rank two and trace one, such that (i) \(X_*\) is uniquely determined by the two measured diagonals among **all** PSD matrices, (ii) all observations are strictly positive, (iii) every entry of \(U\) is nonzero, and (iv) \(\alpha_*(U,X_*)<\eta\). The family must genuinely vary measurement geometry, not merely apply sign flips, simultaneous permutations, scalar rescalings, or basis relabelings to a single example.

That would establish a substantial **non-isolated** phenomenon. Stronger versions, if true, would prove relative openness inside a natural uniqueness stratum, quantitative parameter stability, an interval of target matrices for a fixed \(U\), or uniform nontrivial lower bounds on observation/basis-entry magnitudes. Investigate whether the instability persists under **arbitrary small ambient perturbations** of \(U\) and \(X_*\) *while exact pointwise uniqueness is retained*. Do not silently assume that this unusually high singularity degree can survive generic perturbations.

## Mathematical tasks

1. **Decide what robustness can honestly mean here.** Analyze the geometry and dimension of the exactly identifiable rank-two locus inside \(O(n)\times\{X_*\succeq0:\operatorname{rank}X_*=2,\operatorname{tr}X_*=1\}\). Determine which open-set statements are plausible, which fail for structural reasons, and the precise topology (full ambient, relative/algebraic stratum, positive-dimensional family, or quantitative near-uniqueness).
2. **First seek a parameterized theorem** by varying the distinct interpolation nodes \(d_1,\ldots,d_n\) in the existing Cauchy-eigenbasis/polynomial Gram construction. Derive the measurement-evaluation identities, exact PSD uniqueness, preserved multiple-root mechanism, sharp upper bound against all PSD competitors, and matching instability curve **uniformly over a nontrivial parameter region**. Prove that the family is genuinely inequivalent, ideally with an invariant distinguishing pairs.
3. **Then go beyond that structured family.** Explore transversality, semialgebraic stratification, dual facial certificates, coordinate-free perturbations of the measurement subspace, and deformations of PSD Gram representations. Pursue a theorem under nondegenerate bases satisfying explicit entry bounds (for example \(\min_{ij}|U_{ij}|\ge c_n>0\)), and if possible a natural dimension-controlled incoherence or condition-number assumption. Quantify the constants rather than hiding deteriorating conditioning in \(n\).
4. **Distinguish qualitative exponent instability from operational instability**: near a singular exactly identifiable instance, ordinary Lipschitz recovery may be restored after perturbation, yet its optimal Lipschitz constant may diverge. If exact exponent robustness fails, try proving a *robust neighborhood theorem* giving unavoidable recovery error at specified finite noise scales for many nearby identifiable pairs. Quantify neighborhood size, noise scale, and reconstruction displacement.
5. Establish whether extreme behavior arises in a **natural class**, rather than a single tuned polynomial: e.g., sufficiently high-order real-zero constraints, structured phase-retrieval/tomography measurements, explicit Gram spectrahedra, or a well-defined semialgebraic subset of two-basis pairs. State invariant hypotheses that other researchers can check.

## Proof targets, in decreasing order of ambition

**A (ideal):** An open or relatively open family of uniquely recoverable pairs with rank two, positive data and nonzero overlaps, possessing arbitrarily small sharp exponents, with a proof of exact uniqueness and all-rank stability estimates.

**B (strong):** A positive-dimensional family genuinely varying \(U\), with parameter-uniform sharp exponent and quantitative observation/overlap bounds, plus a theorem explaining which perturbations retain or destroy the pathology.

**C (still valuable):** A theorem proving extreme exponents are necessarily nongeneric in the full parameter space, *together with* rigorous, quantitatively robust near-pathology for identifiable neighboring pairs. A stand-alone genericity slogan without a strong positive result does not meet the objective.

## Falsification obligations

Attack any claim of ambient openness with dimension arguments and small counterexamples \(n=3,4,5\). Check all-rank competitors, trace-one target versus unrestricted-trace competitors, positivity of both data lists, fixed \(U\) versus varying \(U\), and exact versus approximate recoverability. A family generated only by trivial symmetries does **not** count as meaningful robustness. Do not use simulation as a proof of an exponent.

Aim for an independently publishable theorem that changes the editor's “specially constructed degenerate instances” assessment.

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