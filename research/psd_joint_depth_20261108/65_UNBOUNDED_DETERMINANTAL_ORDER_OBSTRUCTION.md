# Milestone 65 — NO bounded-order principal-minor or entry-sign classifier can capture universal PSD stability

**2026-11-08. Fully proved, explicit rational family in every dimension.** This is a mathematically precise obstruction to universal classification by bounded-size local combinatorial motifs. It does **not** exclude all richer global combinatorial normal forms or the previously proved finite real-algebraic decision procedure.

## Theorem — any fixed minor-size test fails

For every integer k>=1 there exist two rational symmetric matrices H_- and H_0 of order n=k+2, both with:
- identical entrywise zero/nonzero and sign patterns;
- **every principal minor of order at most k strictly positive**, hence identical sign data for all such minors;
- the same rank-one PSD target X*=E00 and one-dimensional invisible kernel K_-=span H_-, K_0=span H_0;

such that orthogonal-projection measurements L_±=P_(K_±^perp) uniquely recover X* among all PSD matrices, but have
\[
\boxed{(\alpha_-,d_-)=(1,1),\qquad
       (\alpha_0,d_0)=(1/2,2).}
\]
The first determinant distinguishing the null-compression geometry has order k+1. Therefore no classifier depending only on entry signs and principal-minor signs of some fixed bounded order k (uniform in n) can correctly determine the sharp exponent or facial degree for all PSD inverse problems.

## Explicit construction

Put p=k+1≥2, n=p+1. Let J_p=1_p1_p^T and choose rational
\[
C_\theta=I_p-\frac{1-\theta}{p}J_p,\quad
\theta_-=-\frac1{2p},\quad\theta_0=0,\quad
\varepsilon=\frac{1}{10p^2}.
\]
Set B=epsilon*1_p^T and
\[
H_\theta=\begin{pmatrix}1&B\\B^\top&C_\theta\end{pmatrix},
\quad
K_\theta=\operatorname{span}\{H_\theta\},\quad
\mathcal L_\theta=P_{K_\theta^\perp}.
\]
All coefficients are rational. Every diagonal entry of C_theta is strictly positive, every offdiagonal entry strictly negative, and B has strictly positive entries for both theta values. Thus the entire entrywise sign pattern of H_- and H_0 is identical.

For a principal submatrix C_theta[S,S] indexed by s<=p-1 null coordinates, its eigenvalues are 1 (multiplicity s-1) and
\[
1-\frac{(1-\theta)s}{p}
\ge 1-\frac{(1+1/(2p))(p-1)}p
=\frac{p+1}{2p^2}>0.
\]
Thus every *proper* null principal submatrix is positive definite. If a principal submatrix of H_theta also contains the source coordinate 0, its Schur complement is C_theta[S,S]-B_S^TB_S. Since
\[
\|B_S^\top B_S\|_{\rm op}
=s\varepsilon^2\le\frac1{100p^3}
<\frac{p+1}{2p^2},
\]
it too is positive definite whenever s<=p-1. Therefore all principal minors of H_± of orders <=p=k+1 **except possibly the null-only p-minor** are strictly positive. In particular, ALL principal minors of orders <=k are positive for both generators.

The complete p×p null compression C_theta has eigenvalues 1 (multiplicity p-1) and theta. Thus its determinant first distinguishes theta_- from theta_0:
\[
\det C_{\theta_-}=-1/(2p)<0,\qquad \det C_{\theta_0}=0.
\]

## Sharp exponent and degree for theta_-

Since C_theta_- is indefinite, no nonzero scalar multiple of H_theta_- has PSD null compression. Thus X*+tH_theta_- is not PSD for any t≠0, proving uniqueness. Moreover the kernel line misses the PSD tangent cone at X*, so the standard tangent criterion yields sharp **Lipschitz exponent alpha=1**. Because C_theta_- is indefinite, there exists a positive definite null-space matrix Z with trace(Z C_theta_-)=0. Extending by zero on the support coordinate yields a PSD exposing stress in K_-^perp positive definite on the full p-dimensional target nullspace. Therefore d=1.

## Sharp exponent and degree for theta_0

C_theta0 is PSD of rank p-1 with kernel span(v), v=1_p/sqrt(p), and Bv=epsilon sqrt(p)≠0. If X*+tH_theta0 were PSD for t>0, its null compression t C_theta0 would vanish on v and hence PSD would force its source-to-v cross entry tBv to vanish, contradiction; for t<0 its null compression is negative semidefinite and nonzero. Thus the PSD solution is unique.

For arbitrary PSD recovery competitor X=X*+aH_theta0+E, ||E||<=delta, the null quadratic v^T X v = v^T E v=O(delta), while the source cross 0-to-v entry is a Bv+O(delta). Boundedness of residual sublevel sets and PSD Cauchy-Schwarz give
   |aBv+O(delta)|²<=C delta,
so |a|=O(sqrt(delta)) and ||X-X*||=O(sqrt(delta)). Conversely,
\[
X(t)=X_*+tH_{\theta_0}+M t^2(0\oplus vv^\top)
\]
is PSD for all sufficiently small t>0 if M is a sufficiently large fixed constant: Schur complement of its positive source block is tC_theta0 +t²(M vv^T - B^TB/(1+t)), positive by splitting into v and v^perp and using C_theta0|v^perp=I. Its residual is O(t²) and displacement Θ(t). Hence the exact exponent is alpha=1/2.

Any *first* PSD exposing stress in K_0^perp pairs to zero with C_theta0, so PSD complementarity forces its range into span(v), of rank one. This stress exposes v. On the reduced face U⊕v^perp, the kernel K_0 intersects the supported symmetric space trivially because H_theta0 has nonzero source-to-v cross entry Bv. Thus a second exposing stress removes the remaining p−1 null directions. The minimal facial degree is exactly d=2.

## Consequence and scope

This constructs, for **arbitrarily large** k, two geometrically distinct uniquely solvable PSD recovery problems invisible to every test of entrywise sign data and principal-minor signs up to order k, despite opposite stability regimes and different exposing degrees. Any universal purely combinatorial classifier must encode **global determinantal rank degeneracies of unbounded order** (or equivalent information, e.g. full oriented conic matroid dependencies). There cannot be a dimension-independent rule based solely on fixed-size signed edge motifs or bounded principal minors.

This obstruction does not rule out finite combinatorial classifications whose object size and determinantal order grow with dimension. It does not prove the two-policy incidence model is universal for arbitrary dense kernels.

Classical tangent error bounds, PSD complementation and facial reduction are not presented as novel. The explicit hierarchy of indistinguishability instances and its consequence for bounded-order classifiers are directly proved here.