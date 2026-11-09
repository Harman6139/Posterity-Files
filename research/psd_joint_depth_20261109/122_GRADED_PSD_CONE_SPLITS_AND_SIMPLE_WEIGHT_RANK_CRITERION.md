# Milestone 122 — graded PSD-cone obstruction splits into equal-weight blocks; scalar grades reduce to PURE RANK

**2026-11-09. New proved structural theorem for arbitrary dense PSD kernels.** This is a rigorous strengthening of the analytic graded-cone route in checkpoints 119–120. In a fixed monomial chart the weighted initial kernel is a **graded linear space**. Positivity forces at least one positive homogeneous component supported on a *single equal-valuation diagonal block*. Thus the global PSD conic obstruction decomposes into independent smaller grade tests. For **one-dimensional positive grades**, every such test is an ordinary linear **rank condition** on weighted off-diagonal coordinate rows. No SDP or real quantifier elimination is needed to check the initial-cone obstruction in that case.

This does **not** resolve the minimal facial-reduction stress tower at nonmaximal degree. Its significance is a rigorous reduction of the *primal valuation/graded dual* part of the uniform all-n analytic certificate, and a short alternative proof of the universal harmonic-midpoint necessity.

## Setup

Fix distinct scalar weights \(t_0<\cdots<t_k\), with a fixed orthogonal block decomposition \(V=U_0\oplus\cdots\oplus U_k\); write \(\theta_a=t_i\) for coordinates \(a\in U_i\). For each symmetric matrix-entry basis element \(E_{ab}\) (including \(a=b\)) assign
\[
\eta_{ab}=\frac{\theta_a+\theta_b}{2}.
\]
Let \(K\subseteq\mathbb S^n\) be an arbitrary real subspace, \(D_\epsilon=\operatorname{diag}(\epsilon^{\theta_a/2})\), and
\[
I=\mathcal I_\theta(K)=\lim_{\epsilon\downarrow0}D_\epsilon^{-1}KD_\epsilon^{-1}
\]
be its fixed-coordinate Grassmannian initial subspace.

Let \(\mathcal H_\beta\) be the linear subspace of symmetric matrices supported only on entry coordinates with \(\eta_{ab}=\beta\). The weighted row-pivot construction in checkpoint 120 proves, by an exact rational-monomial basis limit, that
\[
\boxed{I=\bigoplus_\beta I_\beta,\qquad I_\beta=I\cap\mathcal H_\beta.}
\tag{122.1}
\]
Indeed every limiting pivot column has support only at its single pivot weight \(\beta_j\); the columns are linearly independent, and columns at different weights have disjoint supports.

## Theorem A (positive graded obstruction must live in ONE equal-weight diagonal block)

For every such graded \(I\), one has
\[
\boxed{
I\cap\mathbb S_+^n\ne\{0\}
\iff
\exists\,i\in\{0,\ldots,k\}:\;
 I_{t_i}\cap\mathbb S_+(U_i)\ne\{0\},
}
\tag{122.2}
\]
where \(\mathbb S_+(U_i)\) is embedded as a matrix supported only on the \(U_i\times U_i\) block.

**Proof.** The backward implication is immediate. Conversely choose nonzero PSD \(X\in I\), and let \(t_i\) be the **largest coordinate weight** for which \(P_{U_i}XP_{U_i}\ne0\). Such a grade exists because a nonzero PSD matrix has a nonzero diagonal. For every \(j>i\), the PSD compression \(P_{U_j}XP_{U_j}=0\), so the entire \(U_j\) row and column of \(X\) vanish, by \(X\succeq0\) and the matrix Cauchy–Schwarz inequality.

Take the weight-\(t_i\) homogeneous component \(X_{t_i}\). An entry of weight \(t_i\) either has both endpoints of weight \(t_i\), or one endpoint above \(t_i\) and one below it; in the latter case it vanishes because its higher-weight row vanishes in \(X\). Entries joining two grades below \(t_i\) have weight below \(t_i\). Thus
\[
X_{t_i}=P_{U_i}XP_{U_i}\in I_{t_i}
\]
by (122.1). This is nonzero and PSD. QED.

**Important:** This is not true for an *arbitrary* ungraded linear subspace. The direct sum property (122.1) is decisive.

## Corollary B (ONE-DIMENSIONAL null grades: a finite PURE-RANK criterion)

Assume \(U_0\) is the target support and that source uniqueness enforces \(K\cap\mathbb S(U_0)=\{0\}\). Assume each positive-grade block \(U_i\), \(i\ge1\), is ONE dimensional, with diagonal coordinate \(e_i e_i^\top\) at weight \(t_i\).

Let \(B\) be the weighted initial pivot matrix from checkpoint 120, with columns grouped by pivot weight \(\beta\). Let \(J_i\) index all pivot columns of weight \(t_i\). Let \(\mathcal E_i\) be the offdiagonal symmetric entries \((a,b)\), \(a<b\), with \((\theta_a+\theta_b)/2=t_i\).

Then
\[
\boxed{
I\cap\mathbb S_+^n=\{0\}
\iff
\operatorname{rank}B[\mathcal E_i,J_i]=|J_i|
\quad\text{for EVERY }i\ge1.
}
\tag{122.3}
\]

**Proof.** For positive grade \(t_i\), the only diagonal entry of weight \(t_i\) is \((i,i)\). Any homogeneous PSD matrix supported on entries of that weight must vanish on every other diagonal; PSD then forces all offdiagonal entries to vanish. Therefore the only nonzero homogeneous PSD matrices of grade \(t_i\) are positive multiples of \(E_{ii}\).

The restriction map from \(I_{t_i}\) to all offdiagonal rows of weight \(t_i\) has a nonzero kernel iff an initial vector has zero offdiagonal entries, hence is a multiple of \(E_{ii}\). The pivot columns \(B[:,J_i]\) form a basis of \(I_{t_i}\), so that restriction is injective iff the displayed row matrix has full column rank. Together with Theorem A this proves the claim for positive grades.

At source grade zero, the initial space has no nonzero element: an initial homogeneous vector supported entirely on \(U_0\times U_0\) would arise from a nonzero kernel matrix supported there, because zero is the **minimum** entry weight; this contradicts \(K\cap\mathbb S(U_0)=\{0\}\). Hence no separate source-grade cone test is necessary. QED.

**New capacity obstruction.** At any simple positive grade \(t_i\),
\[
\boxed{
\dim I_{t_i}\ \le\
\#\{(a,b):a<b,\ (\theta_a+\theta_b)/2=t_i\}.
}
\tag{122.4}
\]
This is a purely combinatorial upper bound on how many independent graded kernel directions can occupy that level while preserving positive separation. It is often strictly stronger than checking each generator's weight-order inequality separately.

## Corollary C (universal harmonic necessity from graded positivity, no downshift)

Work with the **canonical** maxdet chart of an arbitrary uniquely solvable dense PSD problem, as established in checkpoint 89. Let \(U_i\) be any internal positive-grade block (\(0<t_i<1\)), of arbitrary dimension. The true center's first Puiseux coefficient \(T_i\in K\) at order \(t_i\) has
\[
P_{U_i}T_iP_{U_i}\succ0
\quad\text{and}\quad
(T_i)_{ab}=0\ \text{when }\eta_{ab}>t_i.
\]
Thus its scaled top-weight initial form \(\operatorname{in}_{t_i}(T_i)\) belongs to \(I_{t_i}\) and has a PD \(U_i\) diagonal block.

If there were NO two **different** valuation grades \(U_a,U_b\) with \(a<i<b\) and
\[
\frac{t_a+t_b}{2}=t_i,
\]
every entry of homogeneous weight \(t_i\) would lie within \(U_i\times U_i\): other cross-grade pairs cannot have that average, and strict grade ordering prevents same-side pairs from averaging to \(t_i\). Hence \(\operatorname{in}_{t_i}(T_i)\) would be a nonzero PSD matrix supported on \(U_i\), contradicting the canonical positive-definite graded dual stress \(W\perp I\) from checkpoint 119.

Therefore **every internal canonical valuation grade must be a genuine harmonic midpoint**
\[
\boxed{2t_i=t_a+t_b,\qquad a<i<b.}
\]
This is a shorter independent proof of the harmonic necessity in checkpoint 91 that avoids its geometric downshift perturbation. It uses only conic separation of the actual canonical graded kernel and its genuine grade-positive Puiseux coefficient.

## Example: detect the Milestone-116 collision by a single rank failure

In the explicit shared-edge kernel of checkpoint 116, two generators differ by \(E_{33}-E_{22}\). Under the *proposed* original weights \(\theta_2=7/24<\theta_3=1/3\),
\[
\epsilon^{1/3}D_\epsilon^{-1}(E_{33}-E_{22})D_\epsilon^{-1}
\longrightarrow E_{33}\in I_{1/3}\cap\mathbb S_+^n.
\]
The offdiagonal-row restriction of that homogeneous graded direction is ZERO, violating (122.3). Thus the proposed chart is impossible by a **plain rank test**, with no PSD optimization needed.

## Limitations, novelty, and relation to the requested frontier

- This milestone completely removes the **initial-cone strict LMI** from the all-n certificate of checkpoint 120 whenever all null grades are simple. The grade-positive primal condition is likewise a finite linear rank/nonvanishing test in the simple-grade case, since a scalar diagonal coefficient's sign may be reversed. The remaining challenging part is the **successive minimal facial-reduction PSD cone tower**, which cannot be inferred from scalar weights alone (cf. checkpoint 87).
- When a grade has multiplicity \(>1\), the criterion still reduces to a PSD cone check only inside that smaller block; the full n×n conic check is not needed.
- The theorem does **not** assert every all-n exponent/depth pair is realized by a system with all simple grades, or that the signed facial-stress tower can be represented by a tied-edge graph. The desired *compact arithmetic all-value spectrum and optimal dimensions* remain open.
- Mathematical priority relative to established tropical PSD and hyperbolic-polynomial methods has not been independently checked. The proofs above are self-contained finite linear algebra once the canonical-center results are granted.