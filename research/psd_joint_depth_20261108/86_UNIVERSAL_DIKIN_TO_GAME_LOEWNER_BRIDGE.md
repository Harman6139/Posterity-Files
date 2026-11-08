# Milestone 86 — a rigorous Dikin–Bellman Loewner bridge and an exact weighted-kernel-rank formula

Date: 2026-11-08. **PROVED.** Part I is a general theorem for arbitrary uniquely solvable PSD inverse problems **whenever a fixed monomial Loewner chart exists**. Part II proves that EVERY strict tied-edge min–max incidence system of checkpoint 74 admits such a chart, with exponents equal to its finite Shapley game values. This is a direct and nontrivial bridge between the *intrinsic arbitrary-dense Dikin–Hessian classifier* (checkpoint 10) and the *explicit incidence-game combinatorics*. It is NOT a proof that every dense problem has a chart of this form.

## 1. General Dikin sandwich and weighted support filtration

Let L:S^n→R^m have a unique PSD solution X*≽0. Let K=ker L and q=||L(I)||>0. The canonical shifted maxdet center is
\[
C_\epsilon=\arg\max\{\log\det X:\ X\succ0,\ X-X_*-\epsilon I\in K\}.
\]
Its restricted barrier metric and Dikin radius are
\[
g_\epsilon(H)=\mathrm{tr}(C_\epsilon^{-1}H C_\epsilon^{-1}H),
\qquad
\rho_\epsilon=\max\{\|H\|_F:H\in K,\ g_\epsilon(H)\le1\}.
\]
By the previously established universal Dikin theorem (checkpoint 10),
\[
\omega_{\mathcal L,X_*}(q\epsilon)\asymp \epsilon+\rho_\epsilon.
\]

### Sandwich principle

Fix nonnegative rational weights \(\theta_1,\ldots,\theta_n\) and put
\[
D_\epsilon=\operatorname{diag}(\epsilon^{\theta_1/2},
\ldots,\epsilon^{\theta_n/2}).
\]
Assume for fixed constants a,b,B>0 and all small ε:
(A) EVERY PSD Y with ||L(Y-X*)||<=qε obeys Y≼B Dε²;
(B) there exists PSD Yε with ||L(Yε-X*)||<=bε and Yε≽a Dε².

**Theorem A.** Then
\[
\boxed{cD_\epsilon^2\preceq C_\epsilon\preceq CD_\epsilon^2}
\tag{1}
\]
with positive constants independent of ε.

**Proof.** Cε itself has residual qε, yielding the upper inequality from (A). The universal Loewner analytic-center envelope, proved in checkpoint 09, states that for any PSD Y of residual δ,
\[
Y\preceq n(1+\kappa\delta/\epsilon)C_\epsilon,
\]
where κ is a fixed norm of a right inverse of L* on K⊥. Apply it to the Yε from (B), obtaining
\[
aD_\epsilon^2\preceq Y_\epsilon
\preceq n(1+\kappa b)C_\epsilon.
\]
This is the lower inequality in (1). QED.

Define the **weighted support filtration** of the fixed measurement kernel:
\[
\eta_{ij}=\frac{\theta_i+\theta_j}{2},\quad
V_{\le u}=\{H\in\mathbb S^n:\ H_{ij}=0\text{ when }\eta_{ij}>u\}.
\]
For K≠0 define the finite invariant
\[
\boxed{\tau(K,\theta)=\min\{u:\ K\cap V_{\le u}\ne\{0\}\}.}
\tag{2}
\]
The candidate set has at most n(n+1)/2 entries η_ij. Every test is an **ordinary linear rank calculation**, namely whether the coordinate projection of K onto entries with η_ij>u has nonzero kernel. Thus (2) is an exact finite, basis-invariant (for the given chart) algebraic-matroid rank invariant.

**Theorem B.** Under the sandwich assumptions,
\[
\boxed{\rho_\epsilon\asymp\epsilon^{\tau(K,\theta)},\quad
\alpha=\min\{1,\tau(K,\theta)\}.}
\tag{3}
\]

**Proof.** From (1) and positive-semidefinite Kronecker-product comparison,
\[
c_0\|D_\epsilon^{-1}HD_\epsilon^{-1}\|_F
\le \sqrt{g_\epsilon(H)}
\le C_0\|D_\epsilon^{-1}HD_\epsilon^{-1}\|_F
\quad(H\in\mathbb S^n).
\tag{4}
\]
Write \(N_\epsilon(H)^2=\sum_{i,j}|H_{ij}|^2\epsilon^{-(\theta_i+\theta_j)}\).

Let u*=τ(K,θ). By definition the coordinate projection
\[
P_{\ge u_*}:K\to\{H_{ij}:\eta_{ij}\ge u_*\}
\]
is injective: otherwise a nonzero H∈K would be supported only on entries with η_ij<u*, contradicting the minimality of u*. Finite-dimensional injectivity gives ||P_{\ge u*}H||≥c||H||, whence
\[
N_\epsilon(H)\ge c\epsilon^{-u_*}\|H\|_F.
\]
Conversely K∩V_{\le u*} contains nonzero H0, and every entry of H0 has η_ij≤u*, so
\[
N_\epsilon(H_0)\le C\epsilon^{-u_*}\|H_0\|_F.
\]
These yield the two-sided radius estimate via (4). The Dikin modulus formula now proves (3). QED.

**Scope of Theorem B.** It applies to ANY dense kernel if (and only if needed in the proof) the assumed fixed monomial Loewner sandwich is available. It does **not** assume a graph construction, sparsity, diagonal kernel matrices, or a fixed analytic-center eigenbasis beyond the explicitly stated sandwich hypothesis.

## 2. Every strict tied-edge Shapley PSD incidence system has the sandwich

Consider the complete finite tied-edge generator family of checkpoint 74: source 0, internal vertices 1,...,h, terminal T=h+1; one or more modes at each internal vertex with edge-disjoint parent supports, plus an optional independent leading source-to-vertex edge. Let w be the unique strict Shapley value
\[
0=w_0<w_1<\cdots<w_h<w_T=1,\qquad
w_i=\min_{\mathrm{mode}\ a}\max_{(u,v)\in E_{i,a}}
       \frac{w_u+w_v}{2}.
\]
Fix a sufficiently small offdiagonal generator constant λ. Put
\[
D_\epsilon^2
=\operatorname{diag}(1,\epsilon^{w_1},\ldots,\epsilon^{w_h},\epsilon).
\]

**Theorem C — exact canonical center Loewner chart.** There are fixed c,C>0 such that
\[
\boxed{
cD_\epsilon^2\preceq C_\epsilon\preceq C D_\epsilon^2
}
\tag{5}
\]
for the canonical shifted maximum-determinant center of the *actual incidence measurement map* L=P_(K⊥).

**Proof, upper:** The global PSD competitor analysis in checkpoint 74 controls, at measurement residual δ=O(ε), every diagonal coordinate:
\[
Y_{00}=O(1),\quad Y_{ii}=O(\epsilon^{w_i}),\quad
Y_{TT}=O(\epsilon).
\]
For PSD Y, \(D_\epsilon^{-1}Y D_\epsilon^{-1}\succeq0\) and has trace O(1), hence is ≼C I. Thus every such Y≼C Dε², including Cε at residual ε||L I||.

**Proof, lower:** Select a minimizing mode at every internal vertex and build the matching PSD monomial curve
\[
Y_\epsilon=X_*+\sum_i\epsilon^{w_i}H_{i,a_i}
          +\epsilon E_{TT}
          +[\epsilon^{w_t/2}G].
\]
It has residual exactly ε||L E_TT||=ε, and all diagonal entries are (1−Σ ε^{w_i},ε^{w_1},...,ε^{w_h},ε). By the min–max equalities, EVERY offdiagonal tied edge of each selected mode has parent-average ≤w_i; its normalized entry after Dε congruence is at most λ times a bounded source factor. For sufficiently small fixed λ, the normalized matrix is uniformly strictly diagonally dominant, with least eigenvalue bounded below by a positive constant. Therefore Yε≽c Dε². The general sandwich principle now gives (5). QED.

### Recover the game exponent from the Dikin kernel filtration

Every mode generator H_(i,a) has its unique internal diagonal entry (i,i) at weight w_i, and has at least one globally unique edge of pair weight
\[
\max_{e\in E_{i,a}}\tfrac12(w_u+w_v)\ge w_i
\]
since w_i is a minimum over modes. Therefore any nonzero combination of mode generators has at least one noncancellable edge of weight ≥w_i≥w_1. The unique edge guarantee is essential. Conversely a minimizing generator at vertex 1 has every edge pair weight ≤w1, source-diagonal weight zero, and its own diagonal weight w1; hence its maximal support weight equals w1.

If there is no optional independent leading edge G, (2) therefore gives
\[
\tau(K,w)=w_1.
\]
If an independent G=λF_(0,t) is added, its support weight is w_t/2 and, because it occupies an unused edge, its coordinate cannot be cancelled by any other generator. Thus
\[
\boxed{\tau(K,w)=\min(w_1,w_t/2).}
\tag{6}
\]
Combining (3),(5),(6) recovers the exact Shapley exponent of checkpoint 74 **solely from the intrinsic Dikin metric plus a finite weighted linear rank test**. No direct nonlinear-competitor inequalities are required at this stage (they are used once to prove the center's Loewner chart).

## 3. Why this is a genuine bridge rather than a general dense-to-game proof

The invariant τ(K,w) is determined by coordinate support **relative to a monomial Loewner chart of the canonical center**. For a generic arbitrary dense kernel it is not yet established that such a chart can be chosen in a fixed orthogonal basis with weights and independent parent-edge semantics. A moving Puiseux eigenframe or exact determinant cancellations can make the matrix noncomparable to a *fixed* diagonal power matrix; one then needs the full valuated linear subspace of the *moving-frame whitened kernel*, captured by the exterior-minor Dikin invariant of checkpoint 37.

Thus (5) is proved for EVERY tied-edge incidence construction but is **not a claimed universal theorem for arbitrary dense PSD maps**. Its key implication is that the candidate dense-to-game reduction would have to preserve both: (i) a Loewner metric weight filtration and (ii) deeper PSD exposing-stress cones, which need not be determined by the weight filtration alone. See checkpoint 87 for a rigorous same-valuation/different-depth obstruction.

## Reproducibility and provenance

A companion exact rational script enumerates the finite weighted kernel coordinate supports in the six-by-six α=3/22 tied-edge construction and its independent-edge deletion, verifying that their Dikin support-rank threshold is the same even though the exact facial degrees differ. A direct proof in checkpoint 87 shows that even the complete spectra of central-path matrix and restricted barrier Hessian have matching exponent lists in those two systems.

No claim of publication novelty for maxdet analytic centers or Dikin ellipsoids, which are established prior techniques. The new contribution here is the exact Loewner/Bellman bridge and weighted kernel rank interpretation, proved with its precise hypotheses.
