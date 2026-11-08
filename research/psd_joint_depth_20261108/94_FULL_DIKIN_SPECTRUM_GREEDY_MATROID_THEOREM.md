# Milestone 94 — COMPLETE spectrum of Dikin–Hessian valuations from one weighted linear-matroid greedy basis

**2026-11-08. Proved for every arbitrary dense uniquely solvable finite-dimensional real PSD inverse problem, conditional on the general Dikin–Hessian modulus comparison and fixed monomial maxdet chart in checkpoints 10 and 89.** This strictly strengthens checkpoint 93, which identified only the last greedy row weight and hence the sharp recovery exponent. It also states precisely which metric data cannot determine facial-reduction degree.

## Theorem

Let X_*≽0 be uniquely recovered by a real linear measurement map L:S^n→R^m, and let K=ker L have dimension k≥1. Let C_ε be its canonical shifted maximum-determinant center. By checkpoint 89, in one **constant orthogonal coordinate frame**, there exist rational weights θ_1,...,θ_n≥0 and constants c,C>0 such that
\[
c D_\epsilon^2\preceq C_\epsilon\preceq C D_\epsilon^2,\qquad
D_\epsilon=\operatorname{diag}(\epsilon^{\theta_i/2}).
\]
Choose any constant Frobenius-orthonormal basis H_1,...,H_k of K, and the canonical orthonormal symmetric coordinate-entry basis E_a (a=1,...,N=n(n+1)/2). Define the **constant** N×k coordinate matrix A by A_(a,j)=<E_a,H_j>. Give the row indexed by symmetric entry (i,j) weight η_a=(θ_i+θ_j)/2.

Sort the rows by descending η_a, retaining a row precisely when it increases the rank of previously retained rows. Since A has column rank k, this returns exactly k independent rows, with accepted weights
\[
\beta_1\ge\beta_2\ge\cdots\ge\beta_k\ge0.
\]
Let \(\lambda_1(\epsilon)\ge\cdots\ge\lambda_k(\epsilon)>0\) be **all** eigenvalues of the restricted logdet-Hessian operator on K,
\[
g_\epsilon(H,H)=\operatorname{tr}(C_\epsilon^{-1}H C_\epsilon^{-1}H).
\]
Then, for every j=1,...,k,
\[
\boxed{\lambda_j(\epsilon)=\Theta(\epsilon^{-2\beta_j}).}
\tag{94.1}
\]
The constants may depend on the fixed measurement map but **not** on ε.

Consequently:
- the whole Dikin curvature spectrum is determined by ONE finite rank-filtration matroid;
- its smallest eigenvalue exponent yields the exact full-PSD recovery exponent \(\alpha=\min(1,\beta_k)\), as in checkpoint 93;
- for every j, \(\det_j\) sums and exterior-power volumes satisfy \(e_j(g_\epsilon)=\Theta(\epsilon^{-2(\beta_1+\cdots+\beta_j)})\);
- the multiset \(\{\beta_1,\ldots,\beta_k\}\) depends **only** on the rank function \(u\mapsto\operatorname{rank}(A_{\{a:\eta_a\ge u\},:})\), not on coefficients' magnitudes or signs once the weighted chart is fixed.

## Proof

**Step 1 (Loewner-to-weighted Gram equivalence).** Write \(C_\epsilon=D_\epsilon M_\epsilon D_\epsilon\), with \(cI\preceq M_\epsilon\preceq CI\). For H∈S^n,
\[
g_\epsilon(H,H)
=\operatorname{tr}\!\left[
 M_\epsilon^{-1}(D_\epsilon^{-1}H D_\epsilon^{-1})
 M_\epsilon^{-1}(D_\epsilon^{-1}H D_\epsilon^{-1})
\right].
\]
Since the eigenvalues of \(M_\epsilon^{-1}\) lie in [1/C,1/c], its squared congruence Frobenius norm is uniformly equivalent to \(\|D_\epsilon^{-1}H D_\epsilon^{-1}\|_F^2\). In the orthonormal K basis this is \(x^\top G_\epsilon x\), where
\[
G_\epsilon=A^\top\operatorname{diag}(\epsilon^{-2\eta_a})A .
\]
The min–max principle for generalized eigenvalues therefore gives two-sided constant-factor comparisons between corresponding eigenvalues of the true restricted Hessian and \(G_\epsilon\). Thus it suffices to determine the asymptotic eigenvalue orders of \(G_\epsilon\).

**Step 2 (exact Cauchy–Binet valuation, no cancellation).** For 1≤j≤k let
\[
M_j=\max\left\{\sum_{a\in I}\eta_a:
  |I|=j,\ \operatorname{rank} A[I,:]=j\right\},\qquad M_0=0.
\]
The j-th elementary symmetric polynomial \(e_j(G_\epsilon)\) is the sum of its j×j principal minors. For any fixed principal column set J, Cauchy–Binet gives
\[
\det G_\epsilon[J,J]
 =\sum_{|I|=j} (\det A[I,J])^2\epsilon^{-2\sum_{a\in I}\eta_a}.
\]
Summing over J and observing that at least one j×j column minor is nonzero exactly when the selected j rows have rank j, we obtain
\[
e_j(G_\epsilon)=\Theta(\epsilon^{-2M_j}).
\tag{94.2}
\]
Every coefficient is a **nonnegative square**, eliminating all possible leading-order cancellation.

**Step 3 (recover EACH eigenvalue).** Order the positive eigenvalues \(\mu_1(\epsilon)\ge\cdots\ge\mu_k(\epsilon)\) of \(G_\epsilon\). For any j,
\[
\prod_{i=1}^j\mu_i\ \le\ e_j(G_\epsilon)\
 \le {k\choose j}\prod_{i=1}^j\mu_i.
\]
The left inequality holds because the top-j product is a summand, and the right because every other j-product is at most the top-j product. Therefore
\[
\prod_{i=1}^j\mu_i=\Theta(\epsilon^{-2M_j})
\quad(j=1,\ldots,k).
\]
Dividing the j and j−1 relations yields
\[
\mu_j(\epsilon)=\Theta(\epsilon^{-2(M_j-M_{j-1})}).
\]

**Step 4 (greedy matroid).** The rows of A represent an ordinary linear matroid; sorting them by decreasing η and retaining rank-increasing rows maximizes the sum of weights among all j-element independent sets, for each j simultaneously, by the standard matroid exchange theorem. Thus \(M_j=\beta_1+\cdots+\beta_j\), whence \(M_j-M_{j-1}=\beta_j\). The uniform eigenvalue equivalence from Step 1 proves (94.1). QED.

## What this DOES and DOES NOT classify

Every distinct Dikin curvature growth rate is now fixed by the sorted coordinate rank filtration (in the canonical chart). This is a finite **combinatorial** invariant and is valid for the arbitrary dense problem itself, without any reduction to graph incidence.

However, **the same entire list of β_j need not determine singularity degree**. Checkpoints 87–88 provide explicit rational six-by-six kernels with identical canonical center eigenvaluation spectra, identical **complete** Dikin curvature valuation lists, and even the same normalized leading center/Hessian matrices, while their canonical minimal facial-reduction degrees are three and four. Hence a full joint (n,r,d,α) combinatorial classification needs strictly more information: conic orientation/dual face-compression relations, not just a weighted matroid rank function.

This theorem makes the missing datum mathematically precise. An oriented/positive **conic matroid tower** supplementing the curvature matroid could in principle be universal; the specific bounded tied-edge game realization of that tower remains UNPROVED for arbitrary dense kernels at nonmaximal depth.

## Prior-art and reproducibility

Cauchy–Binet, the spectral min–max comparison and matroid greedy theory are established mathematics. The theorem here is their exact combination with the universal PSD maxdet center Dikin metric; novelty/priority must be externally audited before publication. No numerical test is required for the proof. The explicit six-by-six counterexample in checkpoint 87 already checks the sharp distinction between the two invariant types.