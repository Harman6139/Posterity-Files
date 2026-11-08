# Universal first-stress / sharp-valuation flag alignment and arithmetic denominator obstruction

**2026-11-07. PROVED for arbitrary dense PSD measurement maps.** Fix uniquely recoverable PSD target X* of rank r>=1, nullity nu, sharp exponent alpha<1, and let K=ker L. Let s1 be the rank of a maximal-rank first PSD exposing stress Z0 in K^perp, with Z0>=0 and <Z0,X*>=0. Assume the finite dense weighted-flag extraction theorem from the parent project's completed memorandum (so the sharp exponent admits an exact orthogonal null-space weight flag). This result does **not** assert that sparse network peeling preserves facial depth.

## Theorem A: first-stress alignment holds for every actual sharp PSD arc

Suppose X(t)>=0, X(t)->X*, and ||L(X(t)-X*)||=O(t^Q), and take its orthogonal PSD diagonal-leading weight flag
\[
\mathbb R^n=U_0\oplus U_1\oplus\cdots\oplus U_k,\quad
0=w_0<w_1<\cdots<w_k=Q.
\]
On each U_i the leading positive diagonal coefficient at order w_i is positive definite, and every (i,j) block of X(t) has order at least (w_i+w_j)/2. Then, for **every** first exposing stress Z>=0 in K^perp with <Z,X*>=0,
\[
\boxed{\operatorname{range} Z\ \subseteq U_k.}
\]

**Proof.** Write Z as a positive combination of rank-one terms \(\sum_\ell c_\ell v_\ell v_\ell^\top\), with c_l>0. Since Z∈K⊥ and pairs to zero with X*, the residual assumption gives
    tr(Z X(t))=O(t^Q).
Every summand c_l v_l^T X(t)v_l is nonnegative. Fix l. If v_l had a nonzero component on a block U_i with w_i<Q, choose the least such w_i. The asymptotic quadratic form is
    v_l^T X(t)v_l = (v_{l,i}^T A_i v_{l,i}) t^{w_i}+o(t^{w_i}),
where A_i>0 on U_i; cross terms involve strictly larger powers by the PSD order inequalities, and other diagonal terms have larger weights. This is not O(t^Q), contradiction. Therefore every v_l is supported on U_k, proving the inclusion. QED.

The alignment is with the **terminal valuation block**, not generally with every stage of the facial-reduction flag. It is a genuine geometric restriction on how sharp primal flags and dual exposing stresses can meet, independent of sparsity.

## Theorem B: rank-sensitive universal denominator bound

Let alpha be the exact non-Lipschitz exponent, \(0<\alpha\le1/2\), and let \(b=\operatorname{den}(2\alpha)\) denote the reduced denominator of \(2\alpha\). Then
\[
\boxed{ b\le 2^{\nu-s_1}. }
\]
This strictly improves the universal dimension-only bound \(b\le2^{\nu-1}\) whenever s1>=2.

**Proof.** Extract an orthogonal sharp flag with k positive null weight blocks as in Theorem A, rescale orders so the terminal weight equals 1. By Theorem A, the highest-order block U_k contains the s1-dimensional range of Z0, so dim U_k>=s1. All preceding blocks have positive dimension; their number h=k-1 satisfies
    h<=nu-s1.
The dense weighted-flag midpoint reduction yields a harmonic midpoint network on h internal scalar levels, with boundary 0,1 and with \(2\alpha\) among its internal levels or equal to 1. Its h-by-h integer Laplacian \(M\) has diagonal 2 and two parent incidences in each row. Expanding each row as the sum of two rooted edge incidences shows 1<=det(M)<=2^h. Cramer's rule gives that the denominator of every harmonic weight (in particular 2alpha) divides det(M). Thus
    b<=det(M)<=2^h<=2^{nu-s1},
as claimed. QED.

**Equality rigidity.** If \(b=2^{\nu-s_1}\), then h=nu-s1 and \(\det M=2^h\). The full parent network is acyclic (all 2^h parent choices terminate in the boundary) and has exclusively dyadic weights. Every preceding null valuation block has dimension exactly one and the last one dimension exactly s1. This applies to arbitrary dense matrices without any sparse-conversion assumption.

## Meaning for joint exponent-depth classification

For any prescribed **first facial rank drop s1**, the denominator of 2alpha obeys a universal arithmetic obstruction depending only on nu-s1. At nullity 4, exponents with denominator(2alpha)>=7 necessarily have a rank-one first exposing stress. This reduces the dual rank-profile cases to consider in the unresolved (nu=4,d=3,4) catalogue.

It is **not** claimed that the rank of the first stress by itself determines d or alpha. The theorem supplies one rigorous compatibility rule, not a complete formula for all nu,d. Dimension-independent barrier and general Sturm lower bounds remain distinct.

## Audit of assumptions and prior art

The first alignment argument is a direct positivity and valuation proof. The harmonic determinant bound uses the prior weighted-flag->mediated-network theorem; its combinatorics overlaps with established mediated-graph theory and should not be presented as wholly new. No literature priority claim beyond the mathematically verified implications.