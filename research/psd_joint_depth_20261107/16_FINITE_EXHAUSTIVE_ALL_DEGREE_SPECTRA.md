# Fully terminating exact enumeration of every joint PSD exponent spectrum Σ_(n,r,d)

**PROVED 2026-11-07.** Extends checkpoint 14 from membership of a proposed rational exponent to a **complete finite enumeration** of the full joint spectrum for every fixed (n,r,d). It is algebraic and terminating, not a short arithmetic description. Does not assume weighted-flag completeness or sparse depth preservation. Relies only on the proven universal Dikin–Hessian determinant-ratio theorem and standard real-algebraic quantifier elimination.

## Theorem

For fixed integers n>=2 and rank 0<=r<=n, one can effectively compute an integer D=D(n,r) such that EVERY optimal recovery exponent at that n,r is either 1 or of form p/(2q)<1 for integers 1<=p,q<=D. For each minimal facial reduction degree d, exact polynomial membership tests from checkpoint 14 evaluated on this FINITE rational set return precisely all attainable exponents Σ_(n,r,d). Thus each fixed triple has a necessary-and-sufficient fully terminating exact spectrum-enumeration algorithm, for ALL degrees d.

## Proof of finite uniform exponent candidate set

Normalize X*=diag(I_r,0), let N=n(n+1)/2. Parameterize all kernels K⊂S^n by their N×N Frobenius orthogonal projectors Pi; disjoin over k=dim K=0,...,N. When k=0 the exponent is 1.

For k>=1, choose existentially a Frobenius-orthonormal kernel basis H1,...,Hk, and define the polynomial Gram matrix
    A_ij(X)=tr(adj(X) Hi adj(X) Hj);
    Numerator(X)=(det X)^2 e_(k-1)(A(X)),
    Denominator(X)=det A(X)>0.
For every Pi with unique target, the canonical central matrix X_t is the UNIQUE positive-definite solution of the finite polynomial equations
    Pi(X-X*-t I)=X-X*-t I;
    Pi(adj X)=0; X>0.
The scalar u_Pi(t)=Numerator(X_t)/Denominator(X_t) is a unique positive semialgebraic function, and by the universal Dikin–Hessian theorem
    omega(t||L I||)=Theta(t+sqrt(u_Pi(t))).
Uniqueness and compactness imply u_Pi(t)->0. The parametric graph {(Pi,t,u):u=u_Pi(t),t>0,Pi uniquely feasible} is semialgebraic, being the projection of the explicit polynomial equations for (Pi,X,H_i,u). Apply effective quantifier elimination to obtain a finite Boolean combination of polynomial signs P_j(Pi,t,u); choose D>=1 greater than the degree of every resulting polynomial, uniformly over k.

Fix any admissible Pi0. For every sufficiently small t, some specialized polynomial P_j(Pi0,t,u_Pi0(t)) must vanish AND be nonzero as a polynomial in (t,u). Otherwise all nonzero specialized P_j retain their signs on a neighborhood of (t,u(t)), all identically zero specializations impose no restriction, and the same Boolean formula would hold on an open neighborhood, contradicting that its solution set is the graph of a single-valued function.

There are finitely many j, and each zero-set along the semialgebraic graph is a semialgebraic subset of the positive t-line. A finite union covering (0,eta) forces some j to vanish on a full interval (0,eta') (semialgebraic subsets of R have finitely many components). Therefore u(t) satisfies one nonzero real bivariate polynomial P(t,u) of degree <=D for all small t.

By elementary semialgebraic growth, u(t)~c t^s for c>0 and rational s>0. Write P(t,u)=sum_{i,j}a_ij t^i u^j, with i,j<=D. Substitution of u~c t^s into P=0 forces at least two distinct nonzero monomials to have equal smallest exponent i+s j (otherwise no leading coefficient cancellation is possible). Hence s=(i2-i1)/(j1-j2)>0 has reduced numerator and denominator <=D. Since alpha=min(1,s/2), every non-Lipschitz alpha has the form p/(2q) with 1<=p,q<=D. QED.

## Full all-degree algorithm

1. Construct the finite polynomial central graph uniformly for n,r,k and obtain QE polynomials and degree bound D.
2. Form the finite rational candidate set {1} union {p/(2q)<1:1<=p,q<=D}.
3. For each candidate beta and any prescribed d, apply the NECESSARY-AND-SUFFICIENT polynomial first-order compatibility predicate in checkpoint 14: quantify a projector Pi, an exact d-step exposing-stress chain with no shorter chain, and the central determinant-ratio valuation inequalities.
4. Keep the true cases, discard the false ones. The resulting list is EXACTLY Σ_(n,r,d), and every step terminates by first-order theory of real closed fields.

## Boundaries

This gives a complete *effective algebraic* answer for EVERY fixed triple (n,r,d), not a computationally efficient or closed combinatorial formula. Its D may be astronomically large. It does NOT settle a statement uniformly quantified over all matrix orders, such as whether alpha=1/2 occurs at some degree d>=3, without an additional dimension-uniform theorem. It also does not determine a minimal nullity in a simple fraction formula beyond previously proved special families.

The method's structural content is the universal exact Dikin–Hessian modulus and polynomial determinant-ratio invariant. Quantifier elimination, semialgebraic Puiseux rationality, and Newton polygons are established tools and are not credited as novel.