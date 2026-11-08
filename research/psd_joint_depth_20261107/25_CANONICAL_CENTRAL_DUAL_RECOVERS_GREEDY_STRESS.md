# Canonical maxdet dual stress automatically exposes the largest possible first PSD face

**2026-11-07. PROVED for arbitrary dense maps.** This connects the universal Dikin–Hessian exponent curve (checkpoint 10) to the **canonical maximal-rank facial-reduction chain** (checkpoint 01) using the *same* central matrix curve. It is a new structural observation; bibliographic novelty of analytic-center stress limits is NOT asserted.

Let L:S^n→R^m be real linear, X*≥0 uniquely feasible and rank r>=1, K=ker L. For epsilon>0 let
\[
X_\epsilon=\arg\max\{\log\det X:X>0,\ X-X_*-\epsilon I\in K\}.
\]
Define the canonical positive dual matrix
\[
Z_\epsilon=\epsilon X_\epsilon^{-1}\in K^\perp,\quad Z_\epsilon\succeq0.
\]

## Theorem (first-exposure saturation from the canonical center)

The limit \(Z_0=\lim_{\epsilon\downarrow0}Z_\epsilon\) exists in S^n, is PSD and lies in K^\perp, annihilates X*, and has **maximum rank** among all PSD exposing stresses \(Z\in K^\perp\) satisfying \(\langle Z,X_*\rangle=0\). Equivalently, its range equals the span of the ranges of every such exposing stress. Therefore its kernel is precisely the **canonical largest feasible face after one greedy facial-reduction step**.

This statement holds with arbitrary real coefficients (no algebraicity assumption on L); the central curve is semialgebraic over those coefficients.

### Complete proof

By strict PSD trace control and logdet stationarity (checkpoint 10), X_epsilon is unique and semialgebraic; \(X_\epsilon^{-1}\in K^\perp\). The exact trace identity
\[
n=\langle X_\epsilon^{-1},X_\epsilon\rangle
 =\langle X_\epsilon^{-1},X_*\rangle
  +\epsilon\operatorname{tr}(X_\epsilon^{-1})
\]
shows \(Z_\epsilon\succeq0\), \(\operatorname{tr}Z_\epsilon\le n\), and
\(\langle Z_\epsilon,X_*\rangle\le n\epsilon\). Thus Z_epsilon is bounded. Every bounded real semialgebraic curve has a finite limit as epsilon→0+, so \(Z_0\) exists, is in \(K^\perp\cap S^n_+\), and \(\langle Z_0,X_*\rangle=0\).

Let
\[
\mathcal C=\{Z\succeq0:Z\in K^\perp,\ \langle Z,X_*\rangle=0\}
\]
and choose a relative-interior element \(\bar Z\in\mathcal C\) of maximal rank s, with support R=range \bar Z. (Positive semidefinite sums have kernel intersection, so any ri element has the span of all ranges.) On R, \(\bar Z\succeq c P_R\) for some c>0.

Because \(\bar Z\in K^\perp\) and pairs to zero with X*, the affine central identity gives
\[
\langle\bar Z,X_\epsilon\rangle
=\langle\bar Z,X_*+\epsilon I\rangle
=\epsilon\operatorname{tr}\bar Z.
\]
It follows that
\[
0\preceq P_R X_\epsilon P_R
\preceq \frac{\epsilon\,\operatorname{tr}\bar Z}{c}\, I_R
=: C\epsilon I_R.
\]
For every positive definite matrix X and every orthogonal projector P_R, the principal compression inverse inequality holds:
\[
P_RX^{-1}P_R\succeq(P_RXP_R)^{-1}
\quad\hbox{on }R.
\]
This is the Schur-complement inverse inequality. Therefore
\[
P_R Z_\epsilon P_R
=\epsilon P_R X_\epsilon^{-1}P_R
\succeq\epsilon(P_R X_\epsilon P_R)^{-1}
\succeq C^{-1}I_R.
\]
Passing to the limit, \(P_R Z_0 P_R\succeq C^{-1}I_R\), so Z0 is positive definite on R.

But \(Z_0\in\mathcal C\), and every element of \(\mathcal C\) has range contained in R, by the definition of the maximum-rank relative-interior stress. Thus range(Z0)=R and rank(Z0)=s. QED.

## Corollary (recursive intrinsic analytic-center facial reduction)

Start with W0=R^n and K0=K. On each current face W_j containing range X*, solve the restricted maximum-determinant shifted section with kernel
    K_j=K∩S(W_j)
and identity projector P_Wj. Its positive dual central limit exposes *the maximal possible rank* on that face. Put W_(j+1)=kernel of the limit within W_j and repeat. This gives the exact canonical greedy chain and hence the **minimal** singularity degree, without choosing arbitrary exposing stresses. The exponent of the original inverse problem is simultaneously determined by the original (unrestricted) central Hessian valuation from checkpoint 10.

This is a unified primal–dual **canonical center normal form** for arbitrary dense PSD stability, although the simple arithmetic realization spectrum for all fixed (n,r,d) remains open.

## Interpretation

The limit dual stress is forced to saturate every null direction that **any** first stress can expose. This is stronger than convergence to some arbitrary dual certificate. It supplies a direct constructive link between logdet analytical centers, maximal facial reduction and recovery Hessians.

This does not prove that the full chain can be obtained by taking only the first nonzero Puiseux coefficient of the *single* original dual curve: on later faces multiple eigenvalue scales may appear and require separate restricted-center calculations. It also does not establish sparse-network degree preservation.

Analytic centers and facial reduction have substantial established prior literature; the result is stated with a complete proof but its bibliographic priority should be checked before novelty claims.