# A universal canonical Loewner envelope for semidefinite inverse problems

**Research memorandum — 7 November 2026.** This establishes a self-contained theorem for *every bounded nonempty PSD measurement fibre*, with arbitrary dense measurements and possibly nonunique feasible matrices. It needs no midpoint-network assumption and no semialgebraic curve-selection argument. The basic maximum-determinant centrality principle is well known; the residual-ball transfer and rate consequences below are presented as mathematical findings, not a bibliographic priority claim.

## Theorem 1 (canonical maximum-determinant envelope)

Let \(\mathcal L:\mathbb S^n\to\mathbb R^m\) be linear, and suppose
\[
F=\{X\succeq0:\mathcal LX=b\}
\]
is **nonempty and bounded**. Choose any \(X_0\in F\), and put \(K=\ker\mathcal L\). For \(\varepsilon>0\), let
\[
X_\varepsilon=\operatorname*{argmax}_{X\succ0}\{\log\det X:X-X_0-\varepsilon I\in K\}.
\tag{1}
\]
Then \(X_\varepsilon\) exists, is unique, and is characterized entirely by the intrinsic algebraic equations
\[
\boxed{X_\varepsilon-X_0-\varepsilon I\in K,\quad X_\varepsilon\succ0,\quad X_\varepsilon^{-1}\in K^\perp.}
\tag{2}
\]
Set \(q=\|\mathcal LI\|_2>0\). Fix any bounded linear right inverse \(R:K^\perp\to\mathbb R^m\) of \(\mathcal L^*\), and write \(\kappa=\|R\|_{F\to2}\). **For every \(\varepsilon>0\), every \(\delta\ge0\), and every \(Y\succeq0\) with \(\|\mathcal L Y-b\|_2\le\delta\), one has**
\[
\boxed{0\preceq Y\preceq n\left(1+\kappa\frac{\delta}{\varepsilon}\right)X_\varepsilon.}
\tag{3}
\]
In particular at the canonically matched residual \(\delta=q\varepsilon\), the matrix \(X_\varepsilon\) itself belongs to the residual sublevel and
\[
\boxed{X_\varepsilon\in\mathcal R_{q\varepsilon}\subseteq
\{Y:0\preceq Y\preceq n(1+\kappa q)X_\varepsilon\},\quad
\mathcal R_\delta=\{Y\succeq0:\|\mathcal LY-b\|\le\delta\}.}
\tag{4}
\]
The constant \(n(1+\kappa q)\) is independent of \(\varepsilon,\delta\) and of any positive observable. It depends only on the measurement operator and matrix order, not on the chosen feasible \(X_0\).

**Equivalent sharp observable formulation.** For every \(C\succeq0\), including every rank-one \(C=vv^\top\), define
\[
h_C(\delta)=\sup\{\langle C,Y\rangle:Y\in\mathcal R_\delta\}.
\]
Then simultaneously for all \(C\succeq0\) and every \(\varepsilon>0\),
\[
\boxed{\langle C,X_\varepsilon\rangle\le
h_C(q\varepsilon)\le n(1+\kappa q)\langle C,X_\varepsilon\rangle.}
\tag{5}
\]
Thus *one uniquely defined positive-definite algebraic curve* determines, up to universal multiplicative constants, the optimal value of **every positive-semidefinite linear observable** on the entire approximate-feasibility set. In particular all null-space energy exponents are determined by the diagonal/spectral valuations of this one curve, not by optimizing over arbitrary PSD perturbation curves.

### Proof

The recession cone of \(F\) is \(K\cap\mathbb S_+^n\), hence boundedness yields \(K\cap\mathbb S_+^n=\{0\}\). Strict separation of zero from the compact set \(\mathcal L\{H\succeq0:\operatorname{tr}H=1\}\) gives a positive-definite matrix \(W\in K^\perp\). The affine slice \(X_0+\varepsilon I+K\) has \(\langle W,X\rangle=\langle W,X_0+\varepsilon I\rangle\), so its PSD intersection is compact. It contains \(X_0+\varepsilon I\succ0\). Strict concavity of \(\log\det\) gives a unique positive-definite maximizer, and differentiation along every \(H\in K\) gives \(\langle X_\varepsilon^{-1},H\rangle=0\), proving (2). Conversely, strict concavity makes this stationarity sufficient.

Set \(Z_\varepsilon=\varepsilon X_\varepsilon^{-1}\). It is PSD and belongs to \(K^\perp\). Since \(X_\varepsilon-X_0-\varepsilon I\in K\), stationarity yields the **exact trace identity**
\[
 n=\langle X_\varepsilon^{-1},X_\varepsilon\rangle
  =\langle X_\varepsilon^{-1},X_0\rangle+
  \varepsilon\operatorname{tr}(X_\varepsilon^{-1}).
\tag{6}
\]
Both terms on the right are nonnegative, because \(X_0\succeq0\) and \(X_\varepsilon^{-1}\succ0\). Consequently
\[
\operatorname{tr}(Z_\varepsilon)\le n,\quad
\|Z_\varepsilon\|_F\le n,\quad
0\le\langle Z_\varepsilon,X_0\rangle\le n\varepsilon.
\tag{7}
\]
Let \(y_\varepsilon=R(Z_\varepsilon)\), so \(\mathcal L^*y_\varepsilon=Z_\varepsilon\) and \(\|y_\varepsilon\|_2\le\kappa n\). For any PSD \(Y\) with measurement residual \(\le\delta\),
\[
\begin{aligned}
\varepsilon\operatorname{tr}(X_\varepsilon^{-1}Y)
 &=\langle Z_\varepsilon,Y\rangle\\
 &=\langle Z_\varepsilon,X_0\rangle+
 \langle y_\varepsilon,\mathcal L(Y-X_0)\rangle\\
 &\le n\varepsilon+\kappa n\delta.
\end{aligned}
\tag{8}
\]
The matrix \(X_\varepsilon^{-1/2}YX_\varepsilon^{-1/2}\) is PSD, so its maximum eigenvalue is bounded by its trace, which by (8) is at most \(n(1+\kappa\delta/\varepsilon)\). Undoing the congruence proves (3). As \(\mathcal L(X_\varepsilon-X_0)=\varepsilon\mathcal LI\), we have \(X_\varepsilon\in\mathcal R_{q\varepsilon}\), giving (4). Pairing the Loewner inequalities in (4) with arbitrary \(C\succeq0\), and taking suprema, proves (5). QED.

## Corollary 2 (finite polynomial equations for all positive-observable exponents)

The center curve is equivalently the unique positive-definite solution of
\[
X-X_0-\varepsilon I\in K,
\qquad \operatorname{adj}(X)\in K^\perp,
\tag{9}
\]
with \(\operatorname{adj}(X)=\det(X)X^{-1}\). These are **polynomial equations of degree at most \(n-1\)** in the entries of \(X\) and \(\varepsilon\), together with a positive-definiteness condition. With algebraic data, this defines a unique semialgebraic algebraic-function branch. If \(C\succeq0\) is supported on the common kernel of the feasible set, the nonnegative scalar function \(\langle C,X_\varepsilon\rangle\) has a rational Puiseux leading exponent \(\beta_C>0\). By (5), that is the *exact sharp power* of its worst-case positive observable on all PSD residual competitors.

This is a PSD-specific universal structural classifier for the **positive-observable stability problem**, without unrestricted quantifier elimination over the recovery competitors. It is **not** yet a full classifier of the signed cross-block or Frobenius displacement modulus.

## Corollary 3 (canonical-path interval for full-state sharp exponents)

Now assume \(F=\{X_*\}\) with \(0<r=\operatorname{rank}X_*<n\). Write \(U=\operatorname{range}X_*\), \(V=U^\perp\), \(C=P_V\). Let
\[
b_\varepsilon=\langle P_V,X_\varepsilon\rangle\asymp\varepsilon^\beta.
\]
Then \(0<\beta\le1\), and if \(\alpha\) denotes the optimal **full Frobenius** recovery exponent, then
\[
\boxed{\beta/2\le\alpha\le\beta.}
\tag{10}
\]

**Proof.** Since \(\varepsilon\operatorname{tr}(X_\varepsilon^{-1})\le n\), every eigenvalue of \(X_\varepsilon\) is at least \(\varepsilon/n\), hence \(b_\varepsilon\ge (n-r)\varepsilon/n\) and \(\beta\le1\). Compactness and singleton uniqueness imply \(X_\varepsilon\to X_*\), so \(\beta>0\). The center is a residual competitor at tolerance \(q\varepsilon\), so \(\omega(q\varepsilon)\ge\|X_\varepsilon-X_*\|_F\ge b_\varepsilon/\sqrt{n-r}\), implying \(\alpha\le\beta\).

Conversely, Theorem 1 bounds the null compression of every residual competitor \(Y\) as \(0\preceq P_VYP_V\preceq C_0 P_VX_\varepsilon P_V\), so \(\operatorname{tr}(P_VYP_V)=O(b_\varepsilon)\). Boundedness of the support block of \(Y\) and PSD Cauchy–Schwarz give \(\|P_UYP_V\|_F=O(\sqrt{b_\varepsilon})\). Finally, uniqueness implies \(K\cap\mathbb S(U)=\{0\}\). The linear map \(\mathcal L\) restricted to \(\mathbb S(U)\) is therefore injective, so finite-dimensional inverse bounds control the remaining support-to-support difference by \(O(\varepsilon+\sqrt{b_\varepsilon})\). Hence \(\omega(q\varepsilon)=O(\sqrt{b_\varepsilon})=O(\varepsilon^{\beta/2})\), proving \(\alpha\ge\beta/2\). QED.

**Both endpoints occur.** In the basic \(2\times2\) example \(X_*=E_{11}\) with measurements \((X_{11},X_{22})\), the center is \(\operatorname{diag}(1+\varepsilon,\varepsilon)\), so \(\beta=1\), whereas feasible competitors with \(X_{12}\sim\sqrt\varepsilon\) give \(\alpha=1/2=\beta/2\). In the sparse feedback block family attaining exponent \(1/3\), a diagonal null coordinate of a feasible sharpness curve is \(\asymp\varepsilon^{1/3}\); Theorem 1 forces the center's null trace to have \(\beta=1/3\), and the full exponent is \(\alpha=\beta\). Thus the sandwich is quantitatively sharp.

## Consequence for the remaining high-depth endpoint question

This theorem reduces the conjecture that degree \(d\ge3\) cannot coexist with full-state exponent \(1/2\) to a more focused **canonical eigenvalue-rate problem**: prove that the maximum-determinant central curve \(X_\varepsilon\) necessarily has some null-space energy exponent \(\beta<1/2\) whenever \(d\ge3\). This would imply \(\alpha\le\beta<1/2\) by (10). Existing central-path/facial-reduction work by Sremac–Woerdeman–Wolkowicz proves other rate separations and is relevant prior art, but the stated universal threshold is **not established here**.

## Adversarial audit and novelty boundary

- The theorem covers **all PSD competitors**, not just members of the shifted affine slice.
- The maximum-determinant matrix is uniquely determined by polynomial stationary equations and is a feasible residual competitor at exactly the paired scale.
- Positive-definite trace control follows from **boundedness of the feasible set**. No target singleton assumption is used in Theorem 1.
- The uniform Loewner comparison controls positive-semidefinite observables, but it does **not** control signed cross-block deviations sharply; the \(2\times2\) example makes that limitation explicit.
- Maximum-determinant analytic centers, log-determinant KKT stationarity, self-concordant barriers, and their same-fibre matrix domination principles are established optimization theory. The conceptual result here is the elementary **residual-ball Loewner transfer**, its uniformity over all PSD observables, and the sharp exponent consequences. Bibliographic novelty remains unverified.