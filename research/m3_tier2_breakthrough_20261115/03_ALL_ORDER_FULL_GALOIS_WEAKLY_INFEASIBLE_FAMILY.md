# Checkpoint 03 — an explicit all-order family in the two-query observability class

Date 2026-11-15. The construction and full Galois-group proof below make checkpoint 02's recovery class nonvacuous in EVERY matrix order, with the ORIGINAL uniform beta=1/2 escape normalization. Every possible mixed inertia is exhibited. The universal all-pencil minimax question remains distinct.

## 1. The pencil

For n>=1 put m=n+1 and a_i=2^(-(i-1)), i=1,...,n. For t in R^n define the symmetric arrow

    X_n(t) = [[0, a^T], [a, diag(t_1,...,t_n)]].      (1)

Every coefficient is rational. The n coordinate direction matrices are E_ii on the leaf block and are Frobenius orthonormal. Allow an arbitrary hidden rational orthogonal coordinate rotation U in O(n,Q):

    X_(n,U)(x)=X_n(U^T x).                            (2)

The rotated direction matrices remain rational and Frobenius orthonormal. Rational ambient orthogonal congruences may also be included; they do not change the natural objective. The coordinate chart is part of the input and stays rational.

The first diagonal is zero and X_01=1, so no affine point is PSD. These systems are genuinely weakly infeasible, as shown by the explicit approximants in Section 2. Unlike adding an unrelated weak-infeasibility tail to a hard core, the ENTIRE arrow is the weakly infeasible object whose spectrum is identified.

## 2. Dimension-independent normalization and full escape bounds

Write f_(n,U)(x)=dist_F(X_(n,U)(x),PSD)^2/2. Then for every n,U,

    f_(n,U)(0)=(1/2)sum_i a_i^2 < 2/3,
    ||X_(n,U)(0)||_F^2=2sum_i a_i^2 < 8/3.          (3)

The x coordinate displacement has Frobenius norm exactly ||x||. For EVERY 0<s<=1/8,

    (1/2)s^(-1/2) <= rho_f(s) <= 2s^(-1/2).         (4)

PROOF OF LOWER BOUND. If dist_F(X_n(t),PSD)<=delta, then X_n(t)+delta I>=0: the negative spectral norm is no larger than the Frobenius residual. Its principal minor on indices 0,1 gives

    delta(t_1+delta)>=1,
    t_1>=1/delta-delta.

For delta<=1/2 this is at least 3/(4delta). Take delta=sqrt(2s). Orthogonal coordinate rotation preserves radius, and 3/(4sqrt(2))>1/2, proving the lower half of (4) for every approximate point.

PROOF OF UPPER BOUND. Put S=sum_i a_i<2 and choose

    t_i=S a_i/delta>0.

The matrix X_n(t)+delta E_00 is PSD by the Schur-complement identity

    sum_i a_i^2/t_i = (delta/S)sum_i a_i = delta.

The Frobenius change is exactly delta, not sqrt(m)delta. Thus the residual is at most delta. Moreover

    ||t||=(S/delta)||a||_2 < 4/(sqrt(3)delta).

With delta=sqrt(2s), this is below 2s^(-1/2), establishing (4). It also proves that the infeasibility is weak. QED.

Constants and accuracy onset are independent of matrix order, rational coefficient height, and the hidden orthogonal chart. The unrotated data have polynomial encoding in m; any polynomial-bit rational U preserves a polynomial total encoding. No bound on real-valued Haar-chart encodings is being claimed.

## 3. The generic characteristic polynomial has FULL symmetric Galois group

The following stronger algebraic fact holds for ANY fixed nonzero rational a_1,...,a_n, not just the geometric sequence above.

THEOREM A. Over F_n=Q(t_1,...,t_n), the characteristic polynomial of (1) is irreducible and has Galois group S_(n+1).

The proof is elementary using independent leaf variables and formal power series at t_n=infinity. It does not infer a generic Galois group from a numerical test or a probabilistic assumption.

### 3.1 Irreducibility

The characteristic polynomial is

    p_n(lambda)=lambda product_(i=1)^n(lambda-t_i)
              -sum_(i=1)^n a_i^2 product_(j!=i)(lambda-t_j). (5)

For n=1, lambda^2-t_1 lambda-a_1^2 is primitive as a polynomial in t_1 over Q[lambda], because gcd(lambda,lambda^2-a_1^2)=1. It is linear in t_1, hence irreducible over Q(t_1)[lambda] by Gauss's lemma.

For n>1 write K=Q(t_1,...,t_(n-1)) and Q_(n-1)(lambda)=product_(i<n)(lambda-t_i). Then

    p_n=(lambda-t_n)p_(n-1)-a_n^2 Q_(n-1).           (6)

For every i<n,

    p_(n-1)(t_i)=-a_i^2 product_(j<n,j!=i)(t_i-t_j)

is nonzero in K. Therefore gcd(p_(n-1),Q_(n-1))=1 in K[lambda]. The two coefficients of the degree-one polynomial (6) in t_n are coprime. It is primitive, and hence irreducible in K[lambda,t_n] and then in K(t_n)[lambda], since it is monic in lambda. This proves irreducibility by induction.

### 3.2 A stabilizer subgroup inherited from infinity

Suppose inductively that p_(n-1) has Galois group S_n over K. Let L/K be its splitting field, and put z=1/t_n. Multiplying (6) by z gives

    (z lambda-1)p_(n-1)(lambda)-z a_n^2 Q_(n-1)(lambda)=0. (7)

At z=0 its finite simple roots are the n roots r of p_(n-1). For each such r there is a UNIQUE formal series lambda_r(z) in L[[z]] with lambda_r(0)=r solving (7). One can prove existence and uniqueness directly: insert lambda=r+sum_{j>=1}b_j z^j; at each degree the new coefficient b_j is multiplied by the nonzero number -p'_(n-1)(r), with all remaining terms already determined. Thus the coefficients are recursively in L.

These give n distinct roots. The remaining root is obtained from the trace:

    lambda_infty(z)=z^(-1)+sum_(i<n)t_i-sum_r lambda_r(z).

It is a Laurent series in K((z)), since the sum of the finite series is invariant under Gal(L/K). It is the final root of the degree-(n+1) polynomial (6), by Vieta, and diverges as z^(-1).

Each sigma in Gal(L/K) acts coefficientwise on L((z)), sends lambda_r(z) to lambda_(sigma r)(z), and fixes lambda_infty(z). It restricts to an automorphism of the splitting field of p_n over K(z) embedded in L((z)). This restriction is injective, because a nontrivial permutation of the roots r changes their constant terms. Consequently Gal(p_n/K(t_n)) contains a subgroup S_n which fixes the infinite root and permutes all other n roots.

Irreducibility makes the full Galois action transitive on n+1 roots. By orbit-stabilizer, a transitive subgroup of S_(n+1) containing S_n in the stabilizer of one root has order at least (n+1)n!=(n+1)!, and so is S_(n+1). The n=1 base has group S_2. This completes the induction and Theorem A. QED.

This formal-series argument is a proof in the rational-function field. It does not assume that an arbitrary rational numerical specialization has the same Galois group.

## 4. The squared characteristic polynomial has the same Galois group

THEOREM B. R_n(z,t)=det(zI-X_n(t)^2) is irreducible of degree m over F_n, has distinct roots, and has Galois group S_m.

PROOF. The irreducible p_n has nonzero trace sum_i t_i. Hence p_n(-lambda) is not (-1)^m p_n(lambda). For any root lambda let E=F_n(lambda) and E0=F_n(lambda^2). The degree [E:E0] is at most two. If it were two, its nontrivial automorphism would take lambda to -lambda and fix F_n, so -lambda would also be a root of p_n. Irreducibility would force the excluded parity identity. Therefore E=E0. The squared root has degree m, making R_n its irreducible minimal polynomial. It has no repeated roots in characteristic zero.

For every conjugate lambda_i, lambda_i belongs to F_n(lambda_i^2). Thus the splitting field generated by all squared roots already contains every signed root, and is the splitting field of p_n. The Galois permutation action on roots is preserved by the bijection lambda_i -> lambda_i^2. Theorem A therefore gives S_m. QED.

An invertible rational change of the coordinate variables, in particular the hidden chart U, induces an automorphism of the rational-function field and preserves these conclusions.

## 5. All mixed inertia cases, including the previous exceptional ones

Choose any positive q_i with b<q_i<2b for a fixed b>0, as can be done by the algebraic probe construction with a common rational scale. Let U be a diagonal rational sign matrix with the first sign +1; write t_i=+/-q_i according to U. Then

    sum_i a_i^2/t_i >= 1/(2b)-(sum_(i>=2)a_i^2)/b
                      > (1/2-1/3)/b=1/(6b)>0.

The leaf block is nonsingular. Its Schur complement at the top is -sum_i a_i^2/t_i<0. By congruence elimination, the number of negative eigenvalues of X_n(t) equals

    k=1 + number of negative leaf signs.              (8)

Choosing any k-1 of leaves 2,...,n negative gives EVERY k=1,...,m-1.

In particular, for m=4 the signs (+,+,-) give balanced inertia k=2. For m=8, choosing one negative leaf gives k=2, including an order/inertia pair where the older Moser-coefficient test failed. All these cases have full symmetric squared-spectrum Galois group by Theorem B; no inference from a local sign pattern to a Galois group is used.

## 6. Exact-information consequence

Combine Theorem B with checkpoint 02. For every order m, every rational hidden orthogonal chart U, and every positive target epsilon, the original exact scalar oracle permits optimization of f_(n,U) with AT MOST TWO calls. Unbalanced observed inertia uses one call. This is true despite genuine weak infeasibility, uniform rho(s) comparable to s^(-1/2), bounded f(0) and bounded origin matrix norm, and arbitrarily growing dimension.

This shows explicitly that the new two-query theorem includes natural high-dimensional rational weakly infeasible systems and every mixed inertia, not merely a small exceptional example or a stronger oracle. It does not disprove the desired worst-case power law over ALL rational pencils, because the target hard prior may be supported on algebraically exceptional spectral structures.

The exact polynomial, field, and Schur identities above are suitable for symbolic checks, but the all-order conclusions follow from the proofs. No journal benchmark or external-refereeing claim is being made in this mathematical continuation.
