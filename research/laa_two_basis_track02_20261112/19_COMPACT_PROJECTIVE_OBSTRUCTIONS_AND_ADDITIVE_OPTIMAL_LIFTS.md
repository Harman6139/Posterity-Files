# Milestone 19 — compact projective obstructions and additive exact extension complexities

Date: 2026-11-13. This puts the escape theorem of 15 into the general slack-factorization framework of 17–18. The outcomes are lower bounds for compact convex bodies, exactly computed single-PSD and SOC resources for compact families and their joins, and fixed-order robust approximation gaps.

Attribution and scope. Slack factorization and block-diagonal PSD-rank additivity are classical; see Gouveia–Parrilo–Thomas, arXiv:1111.3164, and Fawzi et al., arXiv:1407.4095, Theorem 2.10. They are used openly, with proofs of the forms needed here. The sharp escape theorem and power-cone lower bound are inherited from milestone 15. No claim is made to have evaluated extension complexity for every convex set or to have replaced the classical factorization characterization by a closed-form scalar invariant.

## 1. Compact bodies can be homogenized without increasing PSD order

Let C be a non-singleton compact convex set, in its affine span, and define the closed pointed cone

    H(C)={ (t x,t): t>0, x in C } union {(0,0)}.        (1)

**Theorem A.** The minimum single-PSD lift order of H(C) equals sxc(C). A lift of C of any fixed product-cone type (PSD/SOC/scalar) also gives a homogeneous lift of H(C) using faces of those same factors, with no additional conic factor. Conversely any lift of H(C) restricts to a lift of C by setting its last output coordinate to one.

### Proof of the nontrivial direction

Take a lift C={pi(Y)+c:Y in K,A(Y)=b}, where K is the chosen product cone. As C contains no affine line, any free auxiliary direction in the kernel of the conic matrix coordinates is invisible to the output, so this form loses no generality.

Compress K to the minimum face of its feasible fibre, so there is a feasible Y0 in int K relative to its span. Faces of the relevant cones are again smaller PSD cones, full Lorentz cones, scalar rays, or zero factors. This compression does not increase any of the claimed resources. Also b!=0: a homogeneous slice would give a bounded cone image plus c, hence only a singleton.

Choose a linear functional h with h(b)=1. Set

    t(Y)=h(A(Y)),
    L={Y:A(Y)=t(Y)b},
    Pi(Y)=(pi(Y)+t(Y)c, t(Y)).                         (2)

L is a LINEAR subspace. We show that Pi(K intersect L)=H(C), without inserting the inequality t>=0 as an extra cone constraint.

First, every Z in K intersect ker A has pi(Z)=0. Otherwise Y0+sZ for s>=0 would give an unbounded ray in C.

Suppose Y in K intersect L had t(Y)<0. Then Z=Y0+Y/(-t(Y)) is interior to K and lies in ker A. For each T in ker A, both Z+epsilon T and Z-epsilon T belong K for sufficiently small epsilon. Their images under pi vanish by the preceding paragraph, so pi(T)=0. Differences of any two feasible lifted points belong ker A; their outputs would all coincide, contradicting that C is not a singleton. Therefore t(Y)>=0.

If t(Y)=0, pi(Y)=0 and Pi(Y)=0. If t(Y)>0, Y/t(Y) is a feasible lift of a point of C, so Pi(Y) belongs H(C). Conversely scaling a feasible lift of any x in C by t>0 gives (tx,t), and zero is lifted by zero. This proves exact equality.

The reverse direction is the slice t=1, which adds only an affine equality. Single-matrix order is therefore unchanged. The same holds for the minimum mixed curvature resource of 15. QED.

The theorem deliberately excludes singleton bases: a ray needs one scalar cone, while a point can be described by affine equalities alone in the size-zero convention.

## 2. An intrinsic projective escape bound for every compact body

Take ANY affine section S=H(C) intersect L. Suppose some affine objective ell on S has finite unattained infimum v and, for all small eta>0,

    inf{||z||:z in S, ell(z)<=v+eta} >= c eta^(-a),
                                         a>0.         (3)

Theorem A makes S a section of a lift of the SAME PSD order as C. Milestone 15 then gives

    sxc(C)>=1+ceil(log_2(1+a)).                        (4)

More generally every mixed PSD/SOC/scalar lift of C with resource

    B=sum_j(d_j-1)+number of nonpolyhedral Lorentz factors

satisfies B>=ceil(log_2(1+a)). Arbitrarily many scalar inequalities may be allowed for this latter resource, exactly as in 15.

This applies to arbitrary compact bodies for which such a section can be exhibited. It is independent of the coefficients, auxiliary variables, decoder positivity, or singular support of a competing lift. It is a NECESSARY obstruction, not a sufficient characterization. One may optimize it over sections, objectives, affine changes, and also the polar body: sxc(C)=sxc(C^polar) follows from transposing the slack factorization.

This addresses the elementary obstruction that direct linear optimization on a compact body always attains its minimum. One changes the affine chart of its homogeneous cone, not the resource count of its lift.

## 3. Exact complexities of compact planar bodies

For k>=1 set q=2^k and define

    C_k={ (x,z): 0<=x<=1,
                    |z|^q<=x^(q-1)(1-x) }.            (5)

This is a full-dimensional compact planar convex body. Its homogeneous cone is linearly isomorphic to

    P_k={ (x,t,z): x,t>=0, |z|^q<=x^(q-1)t }

under t=s-x, where s is the homogenizing coordinate. Convexity also follows directly from the PSD lift below.

**Theorem B.**

    sxc_R(C_k)=sxc_C(C_k)=k+1,                         (6)

where sxc_C permits arbitrary complex Hermitian lifts. The minimum number of nonpolyhedral Lorentz factors, of unrestricted dimensions and with arbitrary extra scalar inequalities, is k. The minimum mixed curvature resource is also k.

### Lower bound

If C_k had a smaller lift, Theorem A would give a lift of P_k with the same resources. Intersect P_k with z=1. Minimizing x over that section has infimum zero and forces

    t>=x^(-(q-1)).

Its escape exponent is q-1=2^k-1. Milestone 15, or (4), forces single PSD order at least k+1 and mixed resource at least k. No restriction on competing representations has been introduced.

### Matching rational single-PSD lift

Take Y>=0 of order k+1, indexed by 0,...,k. Impose

    Y_ii=Y_(0,i+1)       for 1<=i<=k-1,
    Y_00+Y_kk=1,                                        (7)

and project to x=Y_00,z=Y_01. Every unspecified matrix entry is free. The principal 2-by-2 inequalities give

    Y_11>=z^2/x,
    Y_ii>=Y_(i-1,i-1)^2/x,

when x>0, hence 1-x>=|z|^q/x^(q-1). At x=0 the zeroth PSD row vanishes, so z=0.

For completeness, set t=1-x. If x>0 put a_0=x,a_1=z and a_(i+1)=a_i^2/x, and use

    Y=aa^T/x+(t-a_k^2/x)e_k e_k^T.                    (8)

The second coefficient is nonnegative by (5), every copy equation holds, and the output is (x,z). If x=0, use Y=e_k e_k^T. All witnesses (8) have rank at most two; no reverse-direction rank restriction is made.

The SOC upper lift uses k blocks [[x,a_(i-1)],[a_(i-1),a_i]]>=0, with a_0=z and a_k=1-x. These attain the same resource lower bounds. All defining coefficients are rational. QED.

The compact bodies have exactly known standard SDP complexity at every k in FIXED target dimension. Their semidefinite extension degree is only two, since arbitrarily many order-two blocks are allowed in that DIFFERENT resource. This is consistent with the classical planar extension-degree result.

## 4. They are not direct spectrahedra for k>=2

A direct spectrahedral representation would use an affine PSD pencil in the two coordinates (x,z), with no projected auxiliary variables. Such a representation does not exist for C_k when k>=2, at ANY matrix order.

Proof. The polynomial

    p(x,z)=x^(q-1)(1-x)-z^q

is irreducible over R: as a polynomial in z over R[x] it is Eisenstein at the prime 1-x (up to an overall sign). Assume C_k={M(x,z)>=0}. At the interior point (1/2,0), remove the common kernel to have M(1/2,0)>0. Kernel removal is valid because small positive and negative perturbations in both coordinates remain feasible and force every coefficient to annihilate the interior kernel.

Every point on the nontrivial curved boundary has det M=0. Irreducibility and the boundary's nonempty real algebraic arc imply p divides det M. This can also be seen by division over R(x) followed by the infinitely many analytic boundary values and primitive polynomial divisibility.

Set x=1/2 and vary z. The factor p(1/2,z)=2^(-q)-z^q has nonreal roots for q>=4. But M(1/2,0)>0 means det M(1/2,z), after positive congruence, is a positive scalar times det(I+z B) with B symmetric or Hermitian. All its roots are real, a contradiction. QED.

Thus (6) is genuinely a statement about projected SDP lifts, not a disguised direct LMI.

## 5. Additivity for products of arbitrary proper cones

Let K_1,...,K_s be closed pointed full-dimensional cones, each of dimension at least two. Write p(K) for minimum single-PSD lift order, and B(K) for minimum mixed curvature resource, allowing arbitrarily many scalar inequalities. Infinite values are allowed.

**Theorem C.**

    p(K_1 times ... times K_s)=sum_i p(K_i),            (9)
    B(K_1 times ... times K_s)=sum_i B(K_i).           (10)

For SOC-only representations with arbitrary free scalar inequalities, their minimum nonpolyhedral factor counts are likewise additive.

The PSD-order additivity is the cone-slack counterpart of the classical block-diagonal PSD-rank theorem. The mixed-resource proof below records why a high-dimensional Lorentz factor cannot share its nonlinear contribution across two independent cone components.

### 5.1 Slack factors are available for arbitrary competing lifts

Every proper cone has a non-singleton compact base. Restrict an arbitrary affine lift to such a base, compress to its minimum product face, and apply Theorem A. It gives a homogeneous lift of the original cone with no greater resources and an interior point relative to the chosen product face.

For a homogeneous lift pi(K_lift intersect L), conic duality for each nonnegative linear output functional gives a factorization of the pairing slack

    <x,y>=<A(x),B(y)>,       x in K, y in K*.

Conversely these factors reconstruct a homogeneous lift by the finite-span argument of 17. This is the standard cone-factorization principle, not a new positivity assumption.

### 5.2 PSD-block splitting

For two output cone factors, restrict source rays to (x_1,0) or (0,x_2), and dual rays similarly. The off-diagonal pairing slacks are zero. Since each conic factor contributes a nonnegative amount, every individual factor has zero off-diagonal pairings.

In a PSD factor of order d, let U be the span of the ranges of all first-cone source factors. Every second-cone dual factor is supported in U^perp. Compress the first-cone source and dual factors to U, and the second-cone factors to U^perp. This retains both diagonal slack factorizations, with orders r=dim U and d-r.

The total PSD order is unchanged. Its allocated curvature resources obey

    max(r-1,0)+max(d-r-1,0)<=d-1.                     (11)

Zero-dimensional pieces are discarded. This splitting is valid for infinitely many slack rows, since U still has finite dimension. It also works for complex Hermitian factors.

### 5.3 Lorentz-factor splitting

In one Lorentz factor consider the smallest face containing all first-cone source factors. There are only three possibilities:

- Face zero: the first contribution is zero; retain the whole factor for the second cone.
- Full cone: a finite positive sum of first source factors is interior, so every second dual factor must be zero. Retain the factor only for the first cone.
- A boundary ray R_+ u: every first source factor is alpha(x)u, and every second dual factor lies in the complementary boundary ray R_+ v with <u,v>=0. The first diagonal contribution equals alpha(x)<u,B_1(y)>, a scalar nonnegative factorization. The second equals beta(y)<A_2(x),v>, also scalar. Replace this one Lorentz factor by one scalar factor for each output component. Neither needs nonlinear resource.

Thus a Lorentz factor allocates total nonlinear resource at most one across the two cones. Scalar factors similarly split without nonlinear cost. After splitting every original factor, each output cone has an exact finite product-cone factorization, and the sum of its allocated resources is no greater than that of the original lift.

This proves the lower bound in (10); the direct product of minimizing lifts gives the upper bound. For (9), the PSD splitting gives p(K_1)+p(K_2)<=d for any single order-d lift; block-diagonal combination proves equality. Repeating proves all s. Restricting the mixed proof to Lorentz and scalar factors gives SOC-count additivity. QED.

One must use the full slack operator, not finite tables with an unbounded number of free scalar factors: every finite nonnegative table has a scalar factorization. A fixed competing lift has a finite factor list, which is what the splitting argument uses. This prevents an invalid compactness argument for free polyhedral complexity.

## 6. Exact complexity of joins: a large compact family

For compact non-singleton bodies C_1,...,C_s define their convex join by

    J={ (lambda_1 x_1,...,lambda_s x_s,lambda_1,...,lambda_s):
               lambda_i>=0, sum_i lambda_i=1, x_i in C_i }.        (12)

At lambda_i=0 its scaled x_i coordinate is zero. This is a compact convex body in its affine span. Its homogeneous cone is linearly isomorphic to the product of H(C_i). Theorems A and C give

    sxc(J)=sum_i sxc(C_i).                             (13)

The mixed curvature resource and SOC count are also additive in their respective models. The proof does not make any assertion about Cartesian PRODUCT additivity for arbitrary compact convex bodies; a JOIN and a Cartesian product are distinct operations.

For the explicit compact power bodies C_(k_i) of (5), the join therefore has EXACT resources

    minimum single PSD order = sum_i(k_i+1),
    minimum number of Lorentz factors = sum_i k_i,
    minimum mixed curvature resource = sum_i k_i.       (14)

These lower bounds permit arbitrary competing auxiliary variables and affine couplings. The upper lifts are obtained by rational block-diagonal copies of (7), with their normalization right-hand sides replaced by lambda_i and sum_i lambda_i=1.

For example the join of C_2 and C_3 is a five-dimensional compact convex body with minimum single PSD order seven and minimum SOC count five. The two-dimensional factors separately have minimum orders three and four. The target is not a polytope and the proof does not require a symmetry assumption.

## 7. Robust standard-order consequences

For each k, manuscript 18 gives a positive number epsilon_k such that EVERY compact convex body K with sxc(K)<=k obeys

    d_H(K,C_k)>=epsilon_k.                             (15)

Similarly every join in (14) has a positive approximation floor for each single PSD order below its exact minimum. The lower bound permits coefficients varying arbitrarily with accuracy, because bounded PSD-factor normalization is automatic.

The number epsilon_k is instance- and order-dependent. A finite slack witness together with the complete SOS certificate in 17–18 produces an explicit lower bound, but no polynomial bound on its size or on epsilon_k^{-1} is asserted here. No analogous claim is made for curvature resource with unlimited free scalar inequalities: polygons and polytopes already approximate compact bodies with curvature resource zero.

## 8. What this adds to the general characterization

Manuscript 17 supplies the exact necessary-and-sufficient slack characterization and complete finite SOS obstructions for any proposed matrix order. Manuscript 18 supplies finite approximants and robust standard-order gaps. This manuscript extends the asymptotic escape tool to compact sets at NO additional PSD order and evaluates the general complexity exactly for compact power bodies and their additive joins.

The general minimum for an arbitrary convex body is still evaluated through the full slack problem, not a universal formula involving only escape exponents, ambient dimension, or boundary degree. None of the statements claims to solve that stronger computational/classification task or a longstanding open conjecture. The contribution is the stated rigorous synthesis and its exact compact-family consequences, with classical antecedents explicitly identified.
