# Milestone 121 — an exact conic-matroid obstruction from a shared parent edge

**2026-11-09. Self-contained elementary lemma.** This is a concrete proof-level audit of the initial-cone condition in checkpoints 119–120, explaining the valuation locking from checkpoint 118. It does not provide the missing purely arithmetic all-degree spectrum.

## Theorem

Let \(K\subseteq\mathbb S^n\) contain
\[
H_i=E_{ii}-E_{00}+\lambda F_{ab},\qquad
H_j=E_{jj}-E_{00}+\mu F_{ab},
\]
with \(i\ne j\), \(0<\theta_i,\theta_j\le1\), nonzero real \(\lambda,\mu\), and source weight \(\theta_0=0\). Work in a proposed **fixed coordinate** diagonal-power chart \(D_\epsilon=\operatorname{diag}(\epsilon^{\theta_\ell/2})\). Write the scaled-kernel initial subspace as
\[
\mathcal I_\theta(K)=\lim_{\epsilon\downarrow0}
 D_\epsilon^{-1}KD_\epsilon^{-1}.
\]

If \(\theta_i\ne\theta_j\), then
\[
\boxed{\mathcal I_\theta(K)\cap\mathbb S^n_+\ne\{0\}.}
\]
Therefore that candidate chart cannot satisfy the strictly positive-definite graded dual stress criterion from checkpoint 119, and in particular **cannot** be the canonical maximum-determinant center's fixed-coordinate monomial Loewner chart.

### Proof

The shared edge cancels in the following genuine invisible kernel vector:
\[
H=\frac1\lambda H_i-\frac1\mu H_j
=\frac1\lambda E_{ii}-\frac1\mu E_{jj}
  +\left(\frac1\mu-\frac1\lambda\right)E_{00}.
\]
Assume \(\theta_i>\theta_j\). Multiplying the scaled matrix by \(\lambda\epsilon^{\theta_i}\) yields
\[
\lambda\epsilon^{\theta_i}D_\epsilon^{-1}HD_\epsilon^{-1}
=E_{ii}
 -\frac\lambda\mu\epsilon^{\theta_i-\theta_j}E_{jj}
 +\left(\frac\lambda\mu-1\right)\epsilon^{\theta_i}E_{00}
\longrightarrow E_{ii}\succeq0,
\]
and \(E_{ii}\ne0\). Every matrix on the left belongs to the scaled linear subspace \(D_\epsilon^{-1}KD_\epsilon^{-1}\), so its finite nonzero limit belongs to the Grassmannian initial subspace. Hence \(E_{ii}\in\mathcal I_\theta(K)\cap\mathbb S^n_+\). If \(\theta_j>\theta_i\), change signs and multiply by \(\mu\epsilon^{\theta_j}\) instead to obtain \(E_{jj}\). QED.

### Concrete \(7\times7\) audit

In checkpoint 116, the two invisible generators
\[
H_3=E_{33}-E_{00}+\lambda F_{14},
\qquad B_2=E_{22}-E_{00}+\lambda F_{14}
\]
share the parent edge (1,4). The proposed original harmonic chart had
\(\theta_2=7/24,\ \theta_3=1/3=8/24\). The exact difference
\(H_3-B_2=E_{33}-E_{22}\in K\) satisfies
\[
\epsilon^{1/3}D_\epsilon^{-1}(H_3-B_2)D_\epsilon^{-1}
=E_{33}-\epsilon^{1/24}E_{22}\longrightarrow E_{33}.
\]
Thus the graded initial kernel contains a nonzero rank-one PSD matrix, explicitly certifying the failure of the proposed chart *before* computing any canonical center. The actual recovered exponent was shown in checkpoint 116 to change from the originally intended \(1/6\) to \(1/7\).

### Interpretation

This is a dimension-independent **signed circuit** obstruction, not a support-counting rule. Parent-edge collisions can create diagonal kernel differences whose highest-weight initial terms are PSD. Positive-definite dual separation is then impossible, so the desired monomial chart cannot survive.

A legitimate graph-free analytic classifier must carry the oriented initial-cone condition; weighted support inequalities alone cannot prevent this failure. This precise obstruction is included in the uniform finite signed-conic-matroid certificate of checkpoint 120.

**Scope:** The lemma concerns fixed coordinate charts in which both diagonal coordinates have declared weights. It does not rule out a different orthogonal valuation basis, nor prove that every dense kernel admits a tied-edge game preserving facial degree at fixed nullity.