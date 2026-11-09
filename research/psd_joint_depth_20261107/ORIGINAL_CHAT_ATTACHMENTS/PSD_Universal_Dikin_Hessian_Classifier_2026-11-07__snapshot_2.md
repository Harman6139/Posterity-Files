# A universal Dikin–Hessian classifier of sharp PSD recovery

Research memorandum — 7 November 2026. A complete self-contained proof of an **instance-wise universal structural theorem**. The theorem applies to every finite-dimensional uniquely solvable PSD inverse problem, arbitrary dense measurements, any target rank, and every facial-reduction degree. It replaces optimization over competitor curves with a canonical algebraic central path and a smallest eigenvalue on the fixed measurement kernel. No claim of bibliographic novelty is made for analytic centers, Dikin ellipsoids, or log-determinant Hessians in isolation.

## Definition

Let \(\mathcal L:\mathbb S^n\to\mathbb R^m\) be linear and \(X_*\succeq0\) uniquely determined by \(\mathcal L X_*\) among PSD matrices. Write \(K=\ker\mathcal L\), \(b=\mathcal L X_*\), and \(q=\|\mathcal L I\|_2>0\).

For \(\varepsilon>0\), let \(X_\varepsilon\) denote the unique positive-definite maximum-determinant matrix in the *shifted affine fibre*
\[
X_\varepsilon=\operatorname*{argmax}\{\log\det X:X\succ0,\ X-X_*-\varepsilon I\in K\}.
\]
This is a single intrinsic algebraic curve, determined by the finite equations
\[
X_\varepsilon-X_*-\varepsilon I\in K,\qquad
\operatorname{adj}(X_\varepsilon)\in K^\perp,\qquad X_\varepsilon\succ0.
\tag{1}
\]
Equip the fixed vector space \(K\) with the log-determinant barrier Hessian form
\[
\mathfrak g_\varepsilon(H,J)
=\operatorname{tr}(X_\varepsilon^{-1}H X_\varepsilon^{-1}J).
\tag{2}
\]
If \(K\ne\{0\}\), let its smallest Frobenius-metric eigenvalue be
\[
\lambda_\varepsilon
=\min_{\substack{H\in K\\\|H\|_F=1}}
\operatorname{tr}(X_\varepsilon^{-1}H X_\varepsilon^{-1}H)>0,
\qquad \rho_\varepsilon=\lambda_\varepsilon^{-1/2}.
\tag{3}
\]
If \(K=\{0\}\), set \(\rho_\varepsilon=0\).

## Theorem — exact Frobenius modulus from one central curve and one Hessian eigenvalue

There exist constants \(0<c\le C<\infty\) depending only on the fixed measurement operator and matrix size such that for **every** \(\varepsilon>0\),
\[
\boxed{
 c(\varepsilon+\rho_\varepsilon)
 \le\omega_{\mathcal L,X_*}(q\varepsilon)
 \le C(\varepsilon+\rho_\varepsilon).
}
\tag{4}
\]
Here the modulus is the supremum over **all PSD competitors**, not only over matrices in the shifted affine fibre. The constants may be chosen uniformly in \(\varepsilon\), including small \(\varepsilon\).

Equivalently, the entire sharp recovery exponent is determined by the Puiseux valuation of a **single eigenvalue**:
\[
\boxed{\alpha=\min\{1,s\},\quad \rho_\varepsilon\asymp\varepsilon^s}\qquad(K\ne\{0\}).
\tag{5}
\]
With algebraic input data, \(s\in\mathbb Q\) is computable by exact real algebraic methods from equations (1)–(3). The formula applies at every singularity degree and does not require a sparse or midpoint realization.

The positive-observable Loewner envelope is a companion theorem: for every PSD \(Y\) with \(\|\mathcal L(Y-X_*)\|_2\le\delta\),
\[
0\preceq Y\preceq n\left(1+\kappa\frac\delta\varepsilon\right)X_\varepsilon,
\tag{6}
\]
where \(\kappa\) is the norm of any fixed right inverse of \(\mathcal L^*\) onto \(K^\perp\). In particular, \(X_\varepsilon\) and all such competitors at residual \(q\varepsilon\) are comparable in every PSD linear observable, up to a fixed multiplicative constant.

### Proof, part 1: canonical center and uniform spectral bounds

Uniqueness implies \(K\cap\mathbb S_+^n=\{0\}\). Strict separation of the compact image of the unit-trace PSD cone from zero provides \(W\succ0\) in \(K^\perp\), so the shifted affine PSD section is compact and contains \(X_*+\varepsilon I\succ0\). The strictly concave log determinant has a unique interior maximizer, and its stationarity is \(X_\varepsilon^{-1}\in K^\perp\), giving (1).

Set \(Z_\varepsilon=\varepsilon X_\varepsilon^{-1}\). Since \(X_\varepsilon-X_*-\varepsilon I\in K\) and \(X_\varepsilon^{-1}\perp K\),
\[
n=\langle X_\varepsilon^{-1},X_\varepsilon\rangle
=\langle X_\varepsilon^{-1},X_*\rangle
+\varepsilon\operatorname{tr}(X_\varepsilon^{-1}).
\]
Both terms are nonnegative. Therefore
\[
\operatorname{tr}Z_\varepsilon\le n,
\quad \|Z_\varepsilon\|_F\le n,
\quad\langle Z_\varepsilon,X_*\rangle\le n\varepsilon,
\quad X_\varepsilon\succeq(\varepsilon/n)I.
\tag{7}
\]
Let \(R:K^\perp\to\mathbb R^m\) be a fixed linear right inverse of \(\mathcal L^*\), with norm \(\kappa\). For any PSD \(Y\) at residual \(\delta\), put \(y=R(Z_\varepsilon)\), so \(\|y\|_2\le\kappa n\). Then
\[
\begin{split}
\varepsilon\operatorname{tr}(X_\varepsilon^{-1}Y)
 &=\langle Z_\varepsilon,X_*\rangle+
   \langle y,\mathcal L(Y-X_*)\rangle\\
 &\le n\varepsilon+\kappa n\delta.
\end{split}
\]
Since \(X_\varepsilon^{-1/2}YX_\varepsilon^{-1/2}\succeq0\), its operator norm is at most its trace. Undoing congruence proves (6). In particular
\[
X_*\preceq nX_\varepsilon,
\qquad Y\preceq C_0X_\varepsilon
\quad\text{when}\quad\|\mathcal L(Y-X_*)\|_2\le q\varepsilon,
\tag{8}
\]
where \(C_0=n(1+\kappa q)\).

### Proof, part 2: Dikin radius and lower modulus bound

Define the linear congruence \(T_\varepsilon H=X_\varepsilon^{-1/2} H X_\varepsilon^{-1/2}\). By (2)–(3), \(\|T_\varepsilon H\|_F^2=\mathfrak g_\varepsilon(H,H)\), so
\[
\rho_\varepsilon
=\max\{\|H\|_F:H\in K,\ \|T_\varepsilon H\|_F\le1\}.
\tag{9}
\]
For every such \(H\), the operator norm of \(T_\varepsilon H\) is at most one. Hence
\[
Y_\pm=X_\varepsilon\pm H
=X_\varepsilon^{1/2}(I\pm T_\varepsilon H)X_\varepsilon^{1/2}\succeq0.
\]
Their measurement residuals are exactly \(\varepsilon\mathcal LI\), of norm \(q\varepsilon\). Since \(Y_+-Y_-=2H\),
\[
\max\{\|Y_+-X_*\|_F,\|Y_--X_*\|_F\}\ge\|H\|_F.
\]
Taking suprema gives \(\omega(q\varepsilon)\ge\rho_\varepsilon\). Independently \(X_*+\varepsilon I\succeq0\) has residual \(q\varepsilon\) and displacement \(\sqrt n\varepsilon\). Therefore
\[
\omega(q\varepsilon)\ge\max\{\rho_\varepsilon,\sqrt n\varepsilon\}
\ge \tfrac12(\rho_\varepsilon+\varepsilon).
\tag{10}
\]
This also covers \(K=\{0\}\).

### Proof, part 3: uniform upper modulus bound for every ambient competitor

Fix a bounded linear right inverse \(J:\operatorname{range}\mathcal L\to\mathbb S^n\) of \(\mathcal L\), with norm \(j\). Let \(Y\succeq0\) have residual at most \(q\varepsilon\). Set
\[
E=J(\mathcal L(Y-X_\varepsilon)),\qquad
H=Y-X_\varepsilon-E\in K.
\]
The triangle inequality on measurement residuals gives
\[
\|E\|_F\le 2jq\varepsilon.
\tag{11}
\]
By \(X_\varepsilon\succeq(\varepsilon/n)I\),
\[
\|T_\varepsilon E\|_F
\le\frac n\varepsilon\|E\|_F\le 2njq.
\tag{12}
\]
By (8), \(0\preceq T_\varepsilon Y\preceq C_0 I\); hence
\[
\|T_\varepsilon H\|_F
\le\|T_\varepsilon Y\|_F+\|I\|_F+\|T_\varepsilon E\|_F
\le\sqrt n(C_0+1)+2njq=:A.
\tag{13}
\]
Equation (9) implies \(\|H\|_F\le A\rho_\varepsilon\).

The center's displacement decomposes as
\[
X_\varepsilon-X_*=H_0+\varepsilon I,
\qquad H_0=X_\varepsilon-X_*-\varepsilon I\in K.
\]
Using (7) and (8),
\[
\begin{split}
\|T_\varepsilon H_0\|_F
&\le\|I\|_F+\|T_\varepsilon X_*\|_F+
  \varepsilon\|X_\varepsilon^{-1}\|_F\\
&\le\sqrt n+n\sqrt n+n=:B.
\end{split}
\tag{14}
\]
Thus \(\|H_0\|_F\le B\rho_\varepsilon\). Combining \(Y-X_*=H+H_0+E+\varepsilon I\) with (11) yields
\[
\|Y-X_*\|_F
\le (A+B)\rho_\varepsilon+(2jq+\sqrt n)\varepsilon.
\]
Taking the supremum proves the upper bound in (4). QED.

## Exact algorithmic invariant

Choose any Frobenius-orthonormal basis \(H_1,\dots,H_k\) of \(K\), \(k=\dim K\). Form the \(k\times k\) positive-definite matrix
\[
G_{ij}(\varepsilon)
=\operatorname{tr}(X_\varepsilon^{-1}H_i X_\varepsilon^{-1}H_j).
\tag{15}
\]
Then \(\lambda_\varepsilon=\lambda_{\min}(G(\varepsilon))\). The entire recovery exponent is given by (5), with \(\rho_\varepsilon=\lambda_\varepsilon^{-1/2}\). This invariant is intrinsic up to orthogonal change of basis of \(K\). It requires:

1. solving the unique PD branch of a **finite polynomial system** of degree at most \(n-1\), (1);
2. computing the lowest eigenvalue of the finite Hessian restriction (15);
3. extracting one rational order of vanishing.

No search over arbitrary PSD recovery arcs, no unknown facial sequence, and no midpoint-network hypothesis is involved. The same kernel also has a canonical minimal facial-reduction depth obtained by iterating maximum-rank PSD exposing stresses. Thus the pair \((\alpha,d)\) of every dense instance is determined by two finite intrinsic algebraic objects **for all degrees**. This is a complete *instance-wise* structural classifier; it is distinct from an explicit combinatorial list of which pairs occur for each fixed \((n,r,d)\).

## Proof audit and limitations

- The upper bound compares every ambient PSD competitor to the center by a Loewner envelope, and subtracts a bounded right-inverse correction to land **exactly in the kernel**. This correction is harmless in the barrier metric because of the crucial lower bound \(X_\varepsilon\succeq(\varepsilon/n)I\).
- The lower bound uses perturbations \(X_\varepsilon\pm H\) within the same shifted affine fibre, automatically PSD by the Hessian unit ball. These are **actual residual competitors**, not merely tangent formalities.
- Neither the determinant center by itself nor its positive-observable exponents determine signed off-diagonal recovery rates. The additional smallest Hessian eigenvalue is essential.
- If \(K=0\), the Dikin radius is defined as zero and the exponent is one.
- The theorem does not assert efficient computational complexity. Algebraic quantifier elimination, real algebraic curve following, and Puiseux extraction may be costly.
- The theorem does not itself prove that every arbitrary dense instance has a sparse midpoint representation with the same singularity degree, nor provide an elementary closed-form spectrum at each prescribed \((n,r,d)\). The conjectural endpoint \(\alpha=1/2,\ d\ge3\) remains open here.
- Analytic centers, self-concordant logarithmic barriers, Dikin ellipsoids, Puiseux expansions, and greedy facial reduction are established theory. The novel *mathematical consequence of the argument* is the exact recovery-modulus comparison (4); bibliographic priority has not been established and should be audited before claims of publication novelty.

## Corollary: a single polynomial determinant-ratio invariant (no eigenvalue optimization)

Let \(k=\dim K\ge1\), choose Frobenius-orthonormal \(H_1,\ldots,H_k\in K\), and define a **polynomial Gram matrix**
\[
A_{ij}(X)=\operatorname{tr}(\operatorname{adj}(X)H_i\operatorname{adj}(X)H_j),
\qquad 1\le i,j\le k.
\]
For \(X\succ0\), the matrix \(A(X)\) is positive definite. Write \(e_{k-1}(A)\) for the sum of its principal minors of order \(k-1\), with \(e_0=1\). Set
\[
\mathscr R(X)=\det(X)\sqrt{\frac{e_{k-1}(A(X))}{\det A(X)}}.
\tag{16}
\]
Then for the unique canonical center \(X_\varepsilon\),
\[
\boxed{\omega(q\varepsilon)\asymp\varepsilon+\mathscr R(X_\varepsilon).}
\tag{17}
\]
Indeed \(G=\det(X)^{-2}A\), so
\[
\operatorname{tr}G^{-1}
=\det(X)^2\operatorname{tr}A^{-1}
=\det(X)^2\frac{e_{k-1}(A)}{\det A}
=\mathscr R(X)^2.
\]
For positive eigenvalues \(\lambda_i(G)\),
\[
\frac1{\lambda_{\min}(G)}\le\operatorname{tr}G^{-1}
\le\frac{k}{\lambda_{\min}(G)},
\]
so \(\rho_\varepsilon\le\mathscr R(X_\varepsilon)\le\sqrt{k}\rho_\varepsilon\). Combining with (4) gives (17).

Thus the **sharp exponent** is the order of one explicit *rational expression in polynomial invariants* of a unique finite-degree algebraic central branch:
\[
\boxed{
\alpha=\min\Big\{1,\;\operatorname{ord}_\varepsilon\det(X_\varepsilon)
+\frac12\operatorname{ord}_\varepsilon e_{k-1}(A(X_\varepsilon))
-\frac12\operatorname{ord}_\varepsilon\det A(X_\varepsilon)\Big\}.
}
\tag{18}
\]
The formula is basis-independent under orthonormal changes of \(K\): \(A\mapsto Q^\top A Q\), leaving its determinant and elementary symmetric polynomials invariant. This exhibits *finite intrinsic barrier-curvature contact data* explaining the sharp exponent, not merely restating it as a recovery optimization. No claim that this specific ratio is novel to the semidefinite optimization literature is made without a priority search.