# Milestone 89 — UNIVERSAL fixed-orthogonal monomial Loewner normal form for EVERY canonical PSD maxdet center

**Date: 2026-11-08. PROVED for arbitrary dense linear maps and all uniquely solvable real PSD targets; no harmonic incidence or sparse-representation hypothesis.** This upgrades the conditional Dikin-to-weighted-support bridge in checkpoint 86 to a genuinely **universal instance-wise intrinsic classifier**. It does NOT claim that the facial-reduction rank profile is determined by the weights alone; checkpoint 87/88 is a rigorous obstruction to that.

## Theorem — positive-definite monomial normalization of the UNIQUE central path

Let L:S^n→R^m be any real linear map and X*≽0 its unique PSD solution for b=L X*. Let
\[
C_\epsilon=\arg\max\{\log\det X:X\succ0,\ X-X_*-\epsilon I\in K\},
\qquad K=\ker L.
\]
Then there exist:
- one **constant** orthogonal matrix Q∈O(n) whose first r columns span range(X*), r=rank X*;
- rational numbers \(0<w_1\le\cdots\le w_\nu\le1\), \(\nu=n-r\) (with repetitions allowed);
- a fixed positive-definite symmetric matrix M0≻0,

such that with
\[
D_\epsilon=\operatorname{diag}(I_r,\epsilon^{w_1/2},\ldots,\epsilon^{w_\nu/2})
\]
one has the strong asymptotic matrix limit
\[
\boxed{
D_\epsilon^{-1}Q^\top C_\epsilon QD_\epsilon^{-1}
\ \longrightarrow\ M_0\succ0 \quad(\epsilon\downarrow0).
}
\tag{1}
\]
In particular for fixed c,C>0,
\[
\boxed{
c\,QD_\epsilon^2Q^\top
\preceq C_\epsilon
\preceq C\,QD_\epsilon^2Q^\top.
}
\tag{2}
\]
No moving/ε-dependent orthogonal eigenbasis is required.

This is **special to the canonical maximum-determinant path**. An arbitrary positive-definite semialgebraic path can have a moving dominant eigendirection and a singular limit under every constant orthogonal monomial normalization.

## Self-contained proof (key rescaling and Dikin domination)

**A. Existence, convergence and Puiseux expansion of the center.** Unique PSD recovery implies K∩S_+^n={0}; separation gives a positive definite W∈K⊥, uniformly bounding the shifted PSD affine sections by trace control. The shifted section contains X*+εI≻0. Strict concavity of logdet gives a unique center Cε. The finite polynomial KKT system
\[
C_\epsilon-X_*-\epsilon I\in K,\quad
\operatorname{adj}(C_\epsilon)\in K^\perp,\quad C_\epsilon\succ0
\]
makes Cε a semialgebraic function of ε. Every limit point as ε→0 is PSD and lies in X*+K, so uniqueness forces Cε→X*. A one-variable semialgebraic function admits a convergent real Puiseux series after ε=t^N for some finite positive integer N.

**B. Extract a CONSTANT orthogonal quadratic-form valuation flag.** Put U0=range X* and N0=ker X*. On N0, take the smallest positive Puiseux exponent a1 at which the compression \(P_{N0}C_\epsilon P_{N0}\) has a nonzero coefficient. Since the compression is PSD for ε>0, its first coefficient A1 is PSD nonzero. Let U1=range A1, N1=ker A1 inside N0. On N1 repeat the procedure, finding the first nonzero PSD compression coefficient and taking its positive-eigenspace U2. Continue. Because
\[
C_\epsilon\succeq(\epsilon/n)I
\]
from logdet stationarity, the remaining null compression always has its first nonzero order at most one; the process terminates after at most ν steps. It produces a **fixed orthogonal decomposition**
\[
\mathbb R^n=U_0\oplus U_1\oplus\cdots\oplus U_k,
\quad 0=w_0<w_1<\cdots<w_k\le1,
\]
with each first diagonal coefficient on U_i at exponent w_i strictly positive definite. Repeated w's in (1) are the dimensions of these blocks. At any vectors u∈U_i,v∈U_j, PSD Cauchy–Schwarz gives
\[
|u^\top C_\epsilon v|^2
\le(u^\top C_\epsilon u)(v^\top C_\epsilon v)
=O(\epsilon^{w_i+w_j}).
\]
Consequently every Puiseux coefficient H_e of Cε has zero (i,j) block whenever
\[
2e<w_i+w_j.                                      \tag{3}
\]

**C. Construct a THICK full-PSD competitor using only ORIGINAL K coefficients.** Write
\[
C_\epsilon=X_*+\sum_{0<e<1}\epsilon^eH_e
                     +O(\epsilon)
\]
(the sum is FINITE because the Puiseux denominator is fixed). From \(C_\epsilon-X_*-\epsilon I\in K\) identically, each H_e∈K for 0<e<1. For σ>0 define the finite polynomial
\[
Y_\epsilon^{(\sigma)}
=X_*+\sum_{0<e<1}e^{\sigma e^2}\epsilon^eH_e
       +e^\sigma\epsilon I.
\tag{4}
\]
Its measurement residual is **exactly**
\[
\|L(Y_\epsilon^{(\sigma)}-X_*)\|
=e^\sigma\epsilon\,\|L I\|,
\tag{5}
\]
because each H_e belongs to K. Let \(D_\epsilon\) be the diagonal weight scaling in the statement, in the fixed Q basis. Normalize (4) by the slightly reweighted diagonal blocks
\[
\widetilde D_\epsilon^{(\sigma)}
=\bigoplus_i e^{\sigma w_i^2/2}\epsilon^{w_i/2} I_{U_i}.
\]
By (3), all normalized coefficients converge as ε→0. Their diagonal blocks have strictly positive limits: the first positive diagonal coefficient on U_i appears at w_i<1 and is PD, or, if w_i=1, the final e^σ εI is PD. For distinct blocks i≠j, the only surviving coefficients are those with e=(w_i+w_j)/2. Their normalized multiplier is
\[
e^{\sigma(e^2-(w_i^2+w_j^2)/2)}
=e^{-\sigma(w_i-w_j)^2/4}.
\]
Thus taking σ sufficiently large makes every limiting offdiagonal arbitrarily small relative to the fixed PD diagonal blocks; the limiting normalized matrix is PD. Fix such a finite σ. Then for all small ε,
\[
\boxed{Y_\epsilon^{(\sigma)}\succeq c D_\epsilon^2}
\tag{6}
\]
for some c>0, while (5) is O(ε). This is an actual full-matrix PSD competitor **in the ORIGINAL measurement problem**, not a formal arc nor a sparse replacement.

**D. Maximum-determinant Loewner domination gives the LOWER chart bound.** The universal envelope (checkpoint09) states
\[
Y\succeq0,\quad\|L(Y-X_*)\|\le\delta
\quad\Longrightarrow\quad
Y\preceq n(1+\kappa\,\delta/\epsilon)C_\epsilon
\]
for a constant κ depending only on L. Apply it to Yε^(σ) from (4) with δ=e^σ ε||LI||. Combining with (6) yields
\[
C_\epsilon\succeq c' D_\epsilon^2.
\tag{7}
\]
This is the crucial step that makes the normal form UNIVERSAL for maxdet centers; it fails for arbitrary noncentral PSD paths.

**E. PSD Cauchy–Schwarz gives the UPPER chart bound.** By construction the diagonal blocks of Cε on U_i have operator norm O(ε^{wi}), with weight zero on U0. PSD Cauchy–Schwarz bounds every cross block by O(ε^{(wi+wj)/2}). Hence the normalized matrix \(D_\epsilon^{-1}Q^\top C_\epsilon QD_\epsilon^{-1}\) has bounded entries and operator norm, giving
\[
C_\epsilon\preceq C'QD_\epsilon^2Q^\top.
\tag{8}
\]

**F. A positive-definite normalized LIMIT.** All normalized entries are semialgebraic Puiseux functions; (7)–(8) bound them uniformly, so every entry has a finite limit. The lower bound (7) ensures the limiting matrix M0 is strictly positive definite. This proves (1)–(2). QED.

## Corollary — EXACT universal weighted-KERNEL-RANK formula for sharp exponent

With weights \(\theta_i=0\) on U0 and \(\theta_i=w_j\) on each repeated null-space grade, and writing \(\widehat K=Q^\top KQ\), define
\[
V_{\le u}(\theta)
=\{H\in\mathbb S^n:H_{ij}=0
\text{ if }(\theta_i+\theta_j)/2>u\}.
\]
If K≠0, let
\[
\boxed{\tau=\min\{u:\widehat K\cap V_{\le u}(\theta)\ne0\}.}
\]
Then by the two-sided restricted Dikin metric comparison (2), the finite-dimensional coordinate-projection rank proof of checkpoint86 and the universal Dikin–Hessian modulus theorem (checkpoint10),
\[
\boxed{\alpha(\mathcal L,X_*)=\min\{1,\tau\}.}
\tag{9}
\]
If K={0}, alpha=1. Every candidate u belongs to the finite set of pairwise half-sums of the rational central valuation grades. Thus once the canonical center's fixed orthogonal Puiseux filtration has been determined, the exact exponent is obtained by **ordinary linear rank tests on K**, without further PSD competitor optimization or eigenvalue-asymptotic root selection.

This is a **genuinely universal dense-kernel structural normal form**, strictly stronger than a graph-only formula for the exponent. It does NOT, by itself, assign the minimal facial rank profile: checkpoints87–88 give two 6×6 kernels with identical complete central/Hessian leading valuations (even the same normalized leading matrix) and different exposing degrees.

## A necessary graded-dual balance condition (bridge toward signed matroids)

Let \(M_0\succ0\) be the normalized limit in (1), \(W=M_0^{-1}\succ0\). For any nonzero H∈\(\widehat K\), define its highest weighted support level
\[
u(H)=\max\{(\theta_i+\theta_j)/2:H_{ij}\ne0\}
\]
and its initial weighted matrix \(\operatorname{in}_\theta(H)\) by retaining exactly the entries with half-sum u(H). The exact maxdet stationarity \(\mathrm{tr}(C_\epsilon^{-1}H)=0\), multiplied by ε^{u(H)} and normalized, yields
\[
\boxed{\langle W,\operatorname{in}_\theta(H)\rangle=0
\quad\text{for every }H\in\widehat K.}
\tag{10}
\]
Equivalently the finite associated-graded kernel initial subspace
\[
\operatorname{in}_\theta(K)
=\operatorname{span}\{\operatorname{in}_\theta(H):H\in\widehat K\setminus0\}
\]
has a strictly PD orthogonal stress:
\[
\boxed{
\operatorname{in}_\theta(K)^\perp\cap\mathbb S_{++}^n\ne\varnothing,
\qquad
\operatorname{in}_\theta(K)\cap\mathbb S_+^n=\{0\}.
}
\tag{11}
\]
The final implication uses the PSD Gordan–Stiemke alternative or simply <W,H> >0 for every nonzero PSD H. The initial subspace is determined by a finite filtered linear-algebra structure (the realizable valuated matrix matroid), but the PD condition retains SIGNED/ORIENTED conic information invisible to scalar game weights alone.

This supplies a precise route for future dense-to-game work: a universal reduction must represent not merely the game weights \theta and the sharp support threshold τ, but also the positive-definite orthogonal *initial* stress (10) and the sequence of positive compressed stresses defining the exposing-depth tower.

## Boundary and caveats

- This theorem does not assert that any rational weight vector satisfying (11) is realizable; it is a NECESSARY graded-dual condition, not a full inverse characterization of possible weight patterns.
- A fixed orthogonal chart Q exists for the **canonical center**, but that does not imply the kernel is equivalent to independent or tied parent-edge generators in that chart. Generic dense signed initial forms and cancellation remain.
- The theorem concerns *instance-wise* sharp exponents and does not supply an explicit closed arithmetic list of all attainable (n,r,d,alpha) triples; the dense-to-tied-game spectrum equality is still OPEN.
- Ordinary Puiseux theory, PSD facial reduction, logdet analytic centers and Dikin ellipsoids are established methods; bibliographic priority of this particular universal monomial-center normal form and graded-dual consequence has not been independently verified.

## Illustrative symbolic audit

An explicit 3×3 dense quarter-power example has a nontrivial algebraic central path
\[
C_\epsilon=
\begin{pmatrix}
1+\epsilon-s&0&s\\0&\epsilon+s&0\\s&0&\epsilon
\end{pmatrix},
\qquad
s=\frac{\sqrt{4\epsilon^2+3\epsilon}-2\epsilon}{3}.
\]
The monomial scaling with weights (0,1/2,1) is \(D_\epsilon=\operatorname{diag}(1,\epsilon^{1/4},\epsilon^{1/2})\), and exactly
\[
D_\epsilon^{-1}C_\epsilon D_\epsilon^{-1}
\to
\begin{pmatrix}
1&0&1/\sqrt3\\
0&1/\sqrt3&0\\
1/\sqrt3&0&1
\end{pmatrix}\succ0.
\]
The restricted Hessian radius has exponent 1/4, as in checkpoint11. This is a concrete nontrivial test of the fixed-chart theorem beyond graph incidence systems.
