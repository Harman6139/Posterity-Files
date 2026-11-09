# Milestone 118 — shared-edge DUAL STATIONARITY locks two canonical Dikin valuations together

**2026-11-09. PROVED for arbitrary real PSD inverse problems containing the displayed simple shared-edge kernel generators, using the universal maxdet Loewner chart.** This gives a precise algebraic reason why adding a supposedly Bellman-safe edge that collides with another child's tight edge can *change the sharp exponent*. No choice of constant nonzero edge coefficients repairs the valuation collision; a genuine new measurement support, a changed kernel circuit, or a different harmonic realization is required.

## General valuation-locking theorem

Let \(X_*=E_{00}\in\mathbb S^n\) be uniquely recovered by a real linear map \(L\), with measurement kernel K and canonical shifted maximum-determinant center \(C_\epsilon\). Suppose for two DISTINCT null coordinates i≠j and one offdiagonal edge e=(a,b), the kernel contains
\[
H_i=E_{ii}-E_{00}+\lambda F_e,\qquad
H_j=E_{jj}-E_{00}+\mu F_e,
\tag{118.1}
\]
where \(\lambda,\mu\in\mathbb R\setminus\{0\}\) are fixed, and \(F_e=E_{ab}+E_{ba}\). Other arbitrary dense kernel generators may also be present.

Assume \(C_\epsilon\) has a fixed-coordinate monomial Loewner chart in which coordinates 0,i,j have weights \(\theta_0=0\), \(0<\theta_i,\theta_j\le1\):
\[
cD_\epsilon^2\preceq C_\epsilon\preceq CD_\epsilon^2,
\quad D_\epsilon=\mathrm{diag}(\epsilon^{\theta_a/2}).
\]
(The existence of SOME fixed orthogonal chart is universal by checkpoint 89, but requiring i,j to be separate coordinate directions of that chart is an explicit assumption.)

Then
\[
\boxed{\theta_i=\theta_j.}
\tag{118.2}
\]
In particular NO such kernel can have a fixed-coordinate monomial center chart with STRICTLY distinct \(\theta_i,\theta_j\), even when those distinct weights solve all the midpoint inequalities for the individual generators.

**Proof.** The central dual \(Z_\epsilon=\epsilon C_\epsilon^{-1}\) lies in \(K^\perp\cap S_+^n\) by logdet stationarity. Pairing it with the TWO actual generators (118.1) yields the exact identities
\[
(Z_\epsilon)_{ii}-(Z_\epsilon)_{00}
      +2\lambda(Z_\epsilon)_{ab}=0,
\]
\[
(Z_\epsilon)_{jj}-(Z_\epsilon)_{00}
      +2\mu(Z_\epsilon)_{ab}=0.
\]
Eliminate the SAME offdiagonal coordinate:
\[
\boxed{
\frac{(Z_\epsilon)_{ii}-(Z_\epsilon)_{00}}{\lambda}
=
\frac{(Z_\epsilon)_{jj}-(Z_\epsilon)_{00}}{\mu}.}
\tag{118.3}
\]
From the two-sided Loewner chart and inversion order,
\[
(Z_\epsilon)_{ii}\asymp\epsilon^{1-\theta_i},
\quad
(Z_\epsilon)_{jj}\asymp\epsilon^{1-\theta_j},
\quad
(Z_\epsilon)_{00}\asymp\epsilon.
\]
Since \(\theta_i,\theta_j>0\), the source term is negligible compared with both null diagonal terms. Their differences are therefore strictly positive and comparable to their respective leading powers. Equation (118.3) forces their ratio to approach a finite nonzero constant; distinct rational exponents would make that ratio tend to zero or infinity. Thus \(\theta_i=\theta_j\). QED.

The conclusion is independent of how small (or large) the fixed coefficients λ and μ are. If λ and μ have opposite signs, equation (118.3) actually rules out such a unique PSD recovery configuration with positive null diagonal asymptotics, because the two differences have the same positive sign. With same-sign coefficients the valuation locking above is unavoidable.

## Exact renamed canonical center weights in the Milestone-116 example

For the seven-by-seven positive target and rational measurement kernel of checkpoint 116, a tight generator at null vertex 3 and a Bellman-safe generator at vertex 2 share \(F_{14}\). Both use coefficient λ=1/100. The general stationarity equation gives
\[
(Z_\epsilon)_{22}-(Z_\epsilon)_{00}
=
(Z_\epsilon)_{33}-(Z_\epsilon)_{00}.
\]
The ACTUAL sharp rate is α=1/7, rather than the intended preaugmentation w1=1/6.

More strongly, its genuine canonical center has the following two-sided Loewner chart:
\[
\boxed{
C_\epsilon\asymp
\operatorname{diag}\!
(1,\epsilon^{1/7},\epsilon^{2/7},
 \epsilon^{2/7},\epsilon^{1/2},
 \epsilon^{4/7},\epsilon).
}
\tag{118.4}
\]
Here \(\asymp\) means fixed positive constants for Loewner lower and upper comparison, NOT entrywise equality.

**Proof of (118.4):** The global PSD competitor analysis in checkpoint 116 proves, for EVERY PSD residual-O(ε) matrix X, the diagonal estimates
\[
X_{11}=O(\epsilon^{1/7}),\quad
X_{22},X_{33}=O(\epsilon^{2/7}),\quad
X_{44}=O(\epsilon^{1/2}),\quad
X_{55}=O(\epsilon^{4/7}),\quad
X_{66}=O(\epsilon).
\]
For PSD X, diagonal congruence by the right-hand monomial matrix produces a PSD matrix with trace O(1), so X is Loewner-bounded ABOVE by a constant multiple of that matrix. The shifted center Cε is itself a residual-O(ε) competitor, so it obeys the upper bound.

The exact PD witness (116.4) with ε=s^14 has precisely the corresponding positive diagonal powers and normalized offdiagonal entries uniformly ≤2λ, hence its normalized matrix is bounded BELOW by a fixed PD multiple of I. It is an actual residual-ε competitor satisfying \(X(s)\succeq cD_\epsilon^2\). The general analytic-center Loewner envelope from checkpoint09 gives \(X(s)\preceq C'C_\epsilon\); thus \(C_\epsilon\succeq c' D_\epsilon^2\). This proves both sides of (118.4). The source weight zero follows from X*; the two equal weights 2/7 are forced independently by the stationarity identity.

## Consequence for the all-dimension analytic classification

Any proposed fixed-nullity interpolation argument that makes an independent safe action share a harmonic anchor must first check the resulting **dual valuation-locking relations**. Edge sharing is NOT a free combinatorial operation: it creates new linear dependencies in the orthogonal stress system and can coarsen the canonical valuation filtration, changing the sharp recovery exponent even when the added edge's original midpoint average was safe.

A correct dimension-preserving universal realization could:
1. find an edge-disjoint alternative harmonic parent policy at the same nullity;
2. use different signed/determinantal circuits with enough dual degrees of freedom to avoid locking; or
3. explicitly characterize and control the new coarsened weighted kernel matroid while preserving the desired exponent.

The theorem is a NECESSARY structural rule, not a proof that any one of these three approaches always succeeds. It explains one concrete obstruction to upgrading the clone-assisted all-depth construction (110) into a fixed-dimension theorem.

The Dikin/maxdet and PSD linear-algebra ingredients are prior tools. The particular valuation-locking observation and its full-PSD witness are proved in this packet, without an external novelty claim.