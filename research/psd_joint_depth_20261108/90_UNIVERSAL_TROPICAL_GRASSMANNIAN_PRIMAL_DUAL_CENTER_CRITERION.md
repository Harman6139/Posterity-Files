# Milestone 90 — UNIVERSAL strict primal–dual tropical-Grassmannian criterion for canonical PSD center weight flags

**2026-11-08. FULLY PROVED for ANY finite-dimensional uniquely solvable real PSD inverse problem, arbitrary dense measurement kernel.** No stochastic-game assumption, harmonic incidence representation, weighted-flag-to-midpoint theorem, or nonlinear Puiseux coefficient search is needed. This is an exact necessary-and-sufficient *FINITE conic and matroidal test for a given proposed rational weight/orthogonal flag*. It strengthens the universal monomial-center theorem of checkpoint 89 and provides the rigorous bridge to "signed/valuated matroid" models beyond tied-edge games. It is NOT a closed arithmetic enumeration of all joint (nullity,degree,exponent) spectra; facial depth still requires original conic compression data.

## 1. Exact algebraic setup

Let L:S^n→R^m have a uniquely determined PSD target X*, with kernel K=ker L, and let
\[
C_\epsilon=\arg\max\{\log\det X:X\succ0,\
                         X-X_*-\epsilon I\in K\}.
\]
Fix an orthogonal matrix Q whose first r columns span U=range X*, r=rank X*. Fix any *candidate rational* positive null weights \(0<\theta_{r+1},\ldots,\theta_n\le1\) and zero weights on U. Work in the Q coordinate basis and set
\[
D_\epsilon=\operatorname{diag}(\epsilon^{\theta_1/2},
\ldots,\epsilon^{\theta_n/2}),\qquad
\theta_i=0 \text{ on U}.
\]
Write \(\widehat K=Q^\top KQ\). Define the rescaled Grassmannian family
\[
K_\epsilon
=\{D_\epsilon^{-1} H D_\epsilon^{-1}:H\in\widehat K\}
\subseteq\mathbb S^n,
\tag{1}
\]
and the rescaled affine base
\[
B_\epsilon
=D_\epsilon^{-1}Q^\top(X_*+\epsilon I)QD_\epsilon^{-1}
\longrightarrow
B_0=(Q^\top X_*Q)|_U
       \oplus0_{\{0<\theta_i<1\}}
       \oplus I_{\{\theta_i=1\}}.
\tag{2}
\]
The normalized affine fibers are exactly \(B_\epsilon+K_\epsilon\).

### A FINITE maximum-weight-Plücker construction of the limit kernel \(K_0\)

Represent \(\widehat K\) by a fixed full-column-rank N×k coordinate matrix A, k=dimK, N=n(n+1)/2, using the Frobenius-normalized symmetric coordinate basis. Give coordinate e=(i,j), i≤j, weight \(\eta_e=(\theta_i+\theta_j)/2\).

For every k-element row index set I for which \(\det A_I\ne0\), put
\[
m_I=\sum_{e\in I}\eta_e,\qquad M=\max_{\det A_I\ne0}m_I.
\]
Define the **INITIAL PLÜCKER DATA**
\[
p_I^{(0)}=
\begin{cases}
\det A_I,&m_I=M,\\
0,&m_I<M.
\end{cases}
\tag{3}
\]
The nonzero vector of k-minors \(p^{(0)}\) is decomposable (it is the limit of the scaled decomposable Plücker vector of Kε), so it determines a unique k-dimensional real linear subspace
\[
\boxed{K_0=\lim_{\epsilon\downarrow0}K_\epsilon
       \quad\text{in the Grassmannian}.}
\tag{4}
\]
The limit exists for EVERY candidate rational flag, and requires ONLY finite rank/minor and rational-weight comparisons. If k=0 set K0={0}. The full numerical Plücker coefficients at maximum weight are retained; merely knowing their signs or supports can be inadequate for PSD conic feasibility.

## 2. UNIVERSAL IFF criterion for the canonical center's full monomial chart

### Theorem

The following are equivalent:

**(A)** The candidate Q and θ provide a positive-definite normalized canonical central limit:
\[
\boxed{D_\epsilon^{-1}Q^\top C_\epsilon QD_\epsilon^{-1}
       \ \longrightarrow\ M_*\succ0.}
\tag{5}
\]

**(B)** The finite *initial affine pencil* \(B_0+K_0\) satisfies **strict primal and dual semidefinite Slater conditions**:
\[
\boxed{
\exists H_0\in K_0:\ B_0+H_0\succ0,
\qquad
\exists W_0\succ0:\ W_0\perp K_0.
}
\tag{6}
\]
In that case the limit M* in (5) is **exactly the unique maximum-determinant center of the compact limiting spectrahedron**
\[
\{M\succeq0:M\in B_0+K_0\},
\]
and its inverse M*^-1 is a positive-definite dual witness in K0⊥.

This is an exact necessary-and-sufficient **real-algebraic conic test on one finite Plücker-initial subspace**, not a generic-only tropical approximation.

### Proof of (A) ⇒ (B)

Set \(M_\epsilon=D_\epsilon^{-1}Q^\top C_\epsilon QD_\epsilon^{-1}\). By the affine constraint, \(M_\epsilon\in B_\epsilon+K_\epsilon\). If Mε→M*≻0, Bε→B0 and Kε→K0 in the Grassmannian, then \(M_*-B_0\in K_0\), proving strict primal feasibility.

The maxdet stationarity is \(C_\epsilon^{-1}\in K^\perp\). Under congruence, this becomes **exactly**
\[
M_\epsilon^{-1}=D_\epsilon Q^\top C_\epsilon^{-1}Q D_\epsilon
\ \in K_\epsilon^\perp
\tag{7}
\]
for all ε>0. Since Mε^-1→M*^-1≻0 and Kε→K0, taking limits gives \(M_*^{-1}\in K_0^\perp\). This is the strict dual witness, proving (B).

### Proof of (B) ⇒ (A)

Choose B0+H0≻0 with H0∈K0. Since Kε→K0, the orthogonal projections \(P_{K_\epsilon}\) converge to \(P_{K_0}\), and
\[
H_\epsilon=P_{K_\epsilon}H_0\to H_0.
\]
Together with Bε→B0, this gives strictly PD competitors
\(B_\epsilon+H_\epsilon\succ0\) for all small ε, with determinant bounded below by a fixed positive constant.

Next choose W0≻0 with W0∈K0⊥ and put
\[
W_\epsilon=P_{K_\epsilon^\perp}W_0.
\]
Then Wε→W0≻0, so Wε≽cI for small ε. Every PSD M∈Bε+Kε satisfies
\[
c\,\operatorname{tr}M
\le\langle W_\epsilon,M\rangle
=\langle W_\epsilon,B_\epsilon\rangle
\le C,
\]
with fixed C because Bε is bounded. Hence the normalized feasible PSD sections are **uniformly compact**.

The unique shifted maxdet center Mε belongs to this section. Its determinant is at least that of the constructed PD competitor, which has a uniform positive lower bound; its spectral norm is uniformly bounded by compactness. Therefore Mε≽c'I uniformly and Mε≼C'I. Every subsequence has a PD limit in B0+K0. Such a limit is the maxdet center of the limiting section: for any PD candidate B0+H∈B0+K0, choose Hε=P_{Kε}H→H; comparing determinants at ε and passing to the limit shows the limiting center maximizes det among all PD points, hence on the compact PSD section. Strict concavity of logdet on the affine space implies the maximizer is UNIQUE. Consequently the full sequence Mε converges to that unique M*≻0. This is (A), and (7) yields M*^-1∈K0⊥. QED.

## 3. Exact exponent from initial matroid rank + rational weights

When the equivalent tests (5)/(6) hold, the universal Dikin–Hessian weighted-support theorem (checkpoint 86, upgraded universally by checkpoint 89) gives the optimal full recovery exponent
\[
\boxed{
\alpha=\min\left\{1,\;
   \min\left\{u:\operatorname{rank}
       A_{\{e:\eta_e>u\},:}<k\right\}\right\}}
\tag{8}
\]
for k>0; if k=0, alpha=1.

Here A_{rows,:} is the FIXED original kernel coordinate matrix in the Q basis; its rank condition is the existence of a nonzero kernel matrix with all entries above weight u zero. The possible u belong to the finite set of pairwise weight half-sums. This is an EXACT **weighted linear matroid bottleneck test**, not an asymptotic eigenvalue optimization.

The initial Grassmannian Plücker data (3), strict primal/dual PSD feasibility (6), and rank test (8) together give a **complete intrinsic finite signed-matroid/conic classifier for any candidate central weight flag**, applicable to arbitrary dense matrices. The extra dual facial compression rank profile is not determined by these static data alone, as the explicit checkpoint 87/88 examples show.

## 4. Direct bridge to tied-edge games

For every strict tied-edge incidence PSD system, its Shapley weights furnish the chart Q=I and θ=(0,w1,...,wh,1) by checkpoint86, so the conic tests (6) automatically hold. Conversely, arbitrary dense K yield an initial Plücker subspace K0 with a positive-definite primal point B0+H0 and a positive-definite dual stress W0. In the *incidence-game subclass*, the mode/edge constraints make this conic pair explicit and elementary: Bellman min–max balances the exponents while small λ and diagonal dominance provide strict primal/dual certificates.

**What is NOT proved:** Every arbitrary initial signed Plücker subspace satisfying (6) need not be isomorphic (or numerically exponent/depth equivalent) to a tied-edge incidence game with the SAME target nullity. The previous counterexamples in checkpoints 63,65,75 show that entrywise support/sign-only reductions can fail. The exact complete numerical dense-to-tied-game inclusion remains an open problem. The general conic matroid (3)/(6) is a strictly richer **universal normal form for the central valuation stage**, not yet a complete simple all-exponent/dimension arithmetic list.

## 5. Example: 3×3 quarter-power case

Let X*=E00, K=span(H1,H2), H1=−E00+E11+F02 and H2=F01. The exact central weights are θ=(0,1/2,1). Its candidate B0=diag(1,0,1), and the initial weighted kernel is
\[
K_0=\operatorname{span}\{E_{11}+F_{02},\,F_{01}\}.
\]
A strict primal point is \(M=B_0+\tfrac12(E_{11}+F_{02})\), which is PD (2×2 source/terminal block has offdiagonal 1/2 and diagonal 1). A strict dual stress is
\[
W=2E_{00}+E_{11}+2E_{22}-\tfrac12 F_{02}\succ0.
\]
It satisfies <W,E11+F02>=1+2(-1/2)=0 and <W,F01>=0. Thus (6) holds by direct calculation. The fixed-weight kernel rank threshold is min(max(weight(H1)=1/2),max(weight(H2)=1/4))=1/4; (8) recovers the sharp exponent \(\alpha=1/4\) exactly.

This example is fully dense in the sense the kernel is not assumed to be an incidence graph; it validates both conic tests symbolically. The original 3×3 analytic center and its exact positive-definite limiting normalization are recorded in checkpoint 89.

## Scope, limitations, and prior art

Plücker coordinates, matroid base polytopes, initial degenerations of Grassmannians, PSD Slater conditions, and logdet analytic centers are established mathematical tools; no claim of originality is made for those concepts. This checkpoint's contribution is their exact *PSD stability bridge* with a complete proof, without genericity assumptions. Computational complexity of enumerating all Q,θ or all possible (ν,d,α) is not bounded here. This is an **instance-wise candidate-flag iff criterion**, not a closed necessary-and-sufficient arithmetic spectrum for each (ν,d).
