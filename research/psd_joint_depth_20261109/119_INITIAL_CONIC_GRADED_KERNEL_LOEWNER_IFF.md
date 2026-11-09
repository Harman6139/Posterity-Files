# Milestone 119 — exact graded-conic primal–dual certificate for ANY proposed dense PSD monomial stability chart

**2026-11-09. New, self-contained necessity-and-sufficiency theorem for arbitrary dense real PSD linear inverse problems**, not restricted to midpoint graphs or independent/tied parent modes. This gives a FINITE linear-algebra plus strict-SDP test of whether a proposed rational diagonal power chart is compatible with the ORIGINAL kernel and has a matching full-rank PSD arc. It directly diagnoses the valuation merging caused by shared edges (milestones 116/118). It does NOT yet give a closed list of all (n,r,d,alpha) at all dimensions: the exact minimal facial depth is still additional data.

## Definitions

Let \(L:\mathbb S^n\to\mathbb R^m\) uniquely recover \(X_*\succeq0\), \(K=\ker L\), rank \(r\). Fix a CONSTANT orthogonal basis with \(U_0=\operatorname{range}X_*\), and a nonnegative rational **candidate weight vector** \(\theta_1,\ldots,\theta_n\) equal to zero on \(U_0\), with \(0<\theta_i\le1\) on its nullspace. Put
\[
D_\epsilon=\operatorname{diag}(\epsilon^{\theta_i/2}),\qquad
K_\epsilon=D_\epsilon^{-1}K D_\epsilon^{-1}\subset\mathbb S^n.
\]
The linear subspaces \(K_\epsilon\) have a well-defined Grassmannian limit
\[
\mathcal I_\theta(K):=\lim_{\epsilon\downarrow0}K_\epsilon.
\]
This is the **associated-graded initial linear subspace**: take a constant basis of K, multiply its matrix-entry rows by \(\epsilon^{-(\theta_i+\theta_j)/2}\), perform Gaussian elimination over the Laurent–Puiseux rational-function field, and retain the leading row-echelon coefficients. It has dimension \(\dim K\). An equivalent construction is the limit of the Frobenius orthogonal projectors onto \(K_\epsilon\); each projector entry is a bounded rational function in a common integer power of \(\epsilon^{1/q}\) and hence has a limit.

## THEOREM (monomial Loewner chart iff graded conic separation plus a thick primal arc)

The following two assertions are equivalent.

**(A) Canonical center has the proposed chart.** For the unique shifted maxdet center
\[
C_\epsilon=\arg\max\{\log\det X:
X\succ0,\ X-X_*-\epsilon I\in K\},
\]
there are constants \(0<c<C<\infty\) with
\[
\boxed{cD_\epsilon^2\preceq C_\epsilon\preceq CD_\epsilon^2}
\qquad(\epsilon\downarrow0).
\tag{119.1}
\]

**(B) Two finite-type primal–dual properties hold.**

1. **Graded Gordan separation**:
\[
\boxed{
\mathcal I_\theta(K)\cap\mathbb S^n_+=\{0\}
\quad\Longleftrightarrow\quad
\exists\,W\succ0:\ W\perp\mathcal I_\theta(K).}
\tag{119.2}
\]
2. **A thick near-feasible primal family:** there are constants \(c_0,C_0>0\) and PSD matrices \(Y_\epsilon\) for all sufficiently small epsilon such that
\[
Y_\epsilon\succeq c_0D_\epsilon^2,\qquad
\|L(Y_\epsilon-X_*)\|\le C_0\epsilon.
\tag{119.3}
\]
A sufficient explicit certificate for (119.3), requiring no optimization over epsilons, is a FINITE generalized polynomial
\(Y_\epsilon=X_*+\sum_{0<e<1}\epsilon^e H_e+\epsilon T\),
where \(H_e\in K\), \(T\succeq0\) (or arbitrary with finite measurement), every nonzero coefficient block \((i,j)\) obeys \(\theta_i+\theta_j\le 2e\), and the first diagonal coefficient at exponent \(\theta_i\) on each equal-weight null block is positive definite. After multiplying coefficients by \(\exp(\sigma e^2)\) for sufficiently large fixed σ, the coefficient-rescaling lemma makes \(Y_\epsilon\) positive definite and uniformly \(\succeq c_0D_\epsilon^2\).

**Furthermore:** Condition (119.2) ALONE supplies the universal PSD upper bound
\[
\boxed{
Y\succeq0,\quad\|L(Y-X_*)\|\le C_0\epsilon
\quad\Longrightarrow\quad
Y\preceq C_1D_\epsilon^2,
}
\tag{119.4}
\]
independent of (119.3). Conversely (119.3) establishes that the upper chart rate is actually attained in all grades. Thus (119.2) and (119.3) form an exact primal–dual conic criterion, not merely necessary tropical inequalities.

## Complete proof

**Grassmannian convergence.** Choose a common integer \(q\) clearing denominators of \(\theta_i/2\), and set \(t=\epsilon^{1/q}\). In a fixed symmetric coordinate basis, the entries of the column matrix representing \(K_\epsilon\) are monomials in t multiplied by fixed real numbers. Its orthogonal projector is \(A(t)[A(t)^\top A(t)]^{-1}A(t)^\top\), a matrix of rational functions in t. It is uniformly bounded in operator norm (all projectors have norm one), so every rational entry has a finite limit as t↓0. The limit is again a symmetric idempotent projector of the SAME rank because \(\mathrm{tr}P(t)=\dim K\) identically. This defines the limiting subspace \(\mathcal I_\theta(K)\).

**(A) implies (B).** If (119.1) holds, the center \(Y_\epsilon=C_\epsilon\) itself satisfies (119.3) with residual \(\epsilon\|L I\|\). Define the positive dual central matrix
\[
Z_\epsilon=\epsilon C_\epsilon^{-1}\in K^\perp.
\]
Its normalized version is
\[
W_\epsilon=D_\epsilon C_\epsilon^{-1}D_\epsilon
=\epsilon^{-1}D_\epsilon Z_\epsilon D_\epsilon.
\]
By Loewner comparison, \(C^{-1}I\preceq W_\epsilon\preceq c^{-1}I\). Moreover, for any H∈K,
\[
\langle W_\epsilon,D_\epsilon^{-1}HD_\epsilon^{-1}\rangle
=\langle C_\epsilon^{-1},H\rangle=0.
\]
Thus \(W_\epsilon\in K_\epsilon^\perp\). A convergent subsequence has positive-definite limit \(W\), and continuity of the limiting subspaces yields \(W\in\mathcal I_\theta(K)^\perp\). This proves (119.2). The equivalence of (119.2)'s two forms is the homogeneous semidefinite Gordan–Stiemke alternative on the linear subspace \(\mathcal I_\theta(K)\).

**(B) implies the UNIFORM UPPER bound (119.4).** Choose W≻0 orthogonal to \(\mathcal I_\theta(K)\). Let \(P_\epsilon\) be the orthogonal projector onto \(K_\epsilon\), with \(P_\epsilon\to P_0\) and \(P_0W=0\). Put
\[
W_\epsilon=(I-P_\epsilon)W\in K_\epsilon^\perp.
\]
Then \(W_\epsilon\to W\succ0\), so it is positive definite with a fixed eigenvalue lower bound for small epsilon. Define
\[
Z_\epsilon=\epsilon D_\epsilon^{-1}W_\epsilon D_\epsilon^{-1}.
\]
It belongs to K⊥, is PSD, and \(\|Z_\epsilon\|=O(1)\) because \(0\le\theta_i\le1\). Also
\(\langle Z_\epsilon,X_*\rangle=O(\epsilon)\) because the target support has weight zero.

Let Y≽0 have residual \(\|L(Y-X_*)\|\le C_0\epsilon\), and choose any fixed bounded right inverse of L on its range. Write Y−X*=H+E with H∈K and \(\|E\|_F\le C'\epsilon\). Since Zε∈K⊥,
\[
0\le\langle Z_\epsilon,Y\rangle
=\langle Z_\epsilon,X_*+E\rangle=O(\epsilon).
\]
Consequently
\[
0\le
\langle W_\epsilon,D_\epsilon^{-1}YD_\epsilon^{-1}\rangle
=\epsilon^{-1}\langle Z_\epsilon,Y\rangle
\le C''.
\]
Both matrices on the left are PSD and \(W_\epsilon\succeq c'I\), hence
\(\operatorname{tr}(D_\epsilon^{-1}YD_\epsilon^{-1})\le C''/c'\).
For a PSD matrix, operator norm ≤trace; multiplying by Dε gives
\[
Y\preceq(C''/c')D_\epsilon^2.
\]
This proves (119.4) against EVERY ambient PSD competitor, regardless of the structure of K.

**(B) implies the canonical CHART (A).** Condition (119.4) applied to the actual shifted maxdet center \(C_\epsilon\), whose residual is exactly ε||L I||, gives the upper chart \(C_\epsilon\preceq CD_\epsilon^2\). For the lower chart, (119.3) gives a thick near-feasible PSD family of residual Oε. The universal maxdet-center Loewner envelope (checkpoint09) states that every such family satisfies \(Y_\epsilon\preceq C'C_\epsilon\) with constant C' independent of ε, since its residual is Oε. Hence
\[
C_\epsilon\succeq(C')^{-1}Y_\epsilon
\succeq(c_0/C')D_\epsilon^2.
\]
This completes equivalence.

## Important application — valuation locking is a GRADED cone obstruction

Suppose two kernel generators have distinct null diagonals Eii,Ejj but share an edge F_ab as in milestone118. If a proposed weight vector has \(\theta_i\ne\theta_j\), the fixed-chart theorem of milestone118 rules it out. Here there is an *algebraic* certificate: the weighted initial linear subspace \(\mathcal I_\theta(K)\) intersects \(\mathbb S^n_+\) nontrivially, so no positive-definite graded dual stress W exists. The candidate power chart is IMPOSSIBLE even if its individual harmonic midpoint inequalities are satisfied. This is the exact obstruction that the globally-edge-distinct Shapley game model avoids, and that future dimension-preserving shared-edge constructions must control.

## Analytical value for the all-n classification

1. Given ANY fixed dense rational measurement kernel K and rational chart weights θ, \(\mathcal I_\theta(K)\) is computable by exact rational polynomial Gaussian elimination; checking \(W\succ0,\ W\perp\mathcal I_\theta(K)\) is a finite strict LMI feasibility problem. Thus (119.2) is a finite **oriented conic-matroid** test, not a long Puiseux optimization.
2. A proposed constructive kernel with a matching grade-positive polynomial arc satisfies (119.3) by elementary diagonal rescaling. Therefore the pair of tests yields a FULL rigorous, dimension-independent proof of its sharp recovery exponent via the Dikin weighted coordinate-rank theorem (93), even when many parent edges collide and coefficient cancellations prevent the simpler Bellman bounds.
3. However, the MINIMAL facial depth still depends on the successive compressed-dual stress cones; the initial graded cone test alone does not determine d (cf. milestones 87–88).
4. The fixed-nullity all-degree **closed arithmetic spectrum** remains open beyond completed small ν. The theorem supplies the missing *primal* cancellation test that a future full dense-to-tied-game normal form must preserve.

**Proof audit:** The only external ingredients are standard Gordan–Stiemke separation, finite-dimensional linear algebra and the previously established maxdet Loewner envelope. Crucially, no illegal zero-extension of a compressed dual stress is made, and no moving-eigenvector assumption is used. The matrix Wε is a genuine orthogonal projection into the current scaled-kernel complement, converging to W≻0.
