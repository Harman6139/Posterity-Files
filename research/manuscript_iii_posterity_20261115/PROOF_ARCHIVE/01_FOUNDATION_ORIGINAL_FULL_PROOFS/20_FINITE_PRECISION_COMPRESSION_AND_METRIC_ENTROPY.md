# Milestone 20 — finite-precision compression and metric entropy of SDP shadows

Date: 2026-11-13. This develops the finite-slack machinery of 17–18 into a quantitative approximation theorem. The original lift can have arbitrary real coefficients, an unbounded or singular feasible fibre, and arbitrarily ill-conditioned equations. None of those quantities enters the output-length or approximation bound.

The conclusion is not that the original exact representation can always be made rational at the SAME size. It is that every small exact lift admits a bounded, strictly feasible, rational OUTER approximation, with a controlled quadratic overhead and a description-length bound. This gives a coefficient-independent metric-entropy bound for the class of all small SDP shadows, not only polytopes. Milestone 21 uses it to prove approximation lower bounds for uniformly curved, nearly spherical, real-analytic semialgebraic bodies that themselves admit finite SDP lifts.

Attribution: slack factorization and bounded PSD-factor normalization are classical ingredients, proved in the forms used here in 17. Counting/rounding lower bounds have major antecedents in Briet–Dadush–Pokutta, arXiv:1305.3268, and Averkov–Kaibel–Weltge, arXiv:1605.08538. The latter explicitly treats families of polytopes. The derivation below covers arbitrary compact shadows and supplies the stated rational, strict-feasibility, and product-block bounds. It does not claim historical priority for the general counting method.

## 1. Resources and assumptions

Let C be a convex body in R^n with 0 in C and C contained in R B_2, where R>=1 is an integer. A product-PSD lift uses the cone

    K=product_(h=1)^s S_+^(d_h),  d_h>=1,

an arbitrary affine slice, and an affine projection. Free variables and affine equalities are allowed. EVERY scalar inequality counts as an order-one PSD factor. In particular, arbitrarily many uncharged scalar inequalities are NOT allowed in the resource below.

Put

    q=sum_h d_h(d_h+1)/2,
    ell=sum_h d_h,
    dmax=max_h d_h,
    M=q+n+1,
    K0=ell+nR+1.

Thus q is the total real dimension of the conic matrix variables, not the sum of their orders or the largest block order. For a single block of order d, q=d(d+1)/2.

A compact full-dimensional shadow can always be expressed in the above model despite initially supplied free variables: a direction leaving all conic variables unchanged cannot change the output, or it would give an affine line in C. Compressing to the minimum product face when using duality does not increase the block orders.

## 2. Rational compression theorem

Fix 0<epsilon<=1. Let delta be the largest integral power of two satisfying

    delta <= epsilon/(3 M K0),

and put e=delta K0. Therefore

    epsilon/(6M) < e <= epsilon/(3M).

**Theorem A.** If C has the indicated product-PSD lift, there exist rational symmetric matrices Qtilde_i^h, rational vectors utilde_i and rational scalars htilde_i, for 1<=i<=M, such that the set

    Chat={ x in [-R,R]^n : there exist Z_h>=0 with
              tr Z_h<=1 for every h,
              |sum_h tr(Qtilde_i^h Z_h)+utilde_i.x-htilde_i|
                    <=2e for every i }

satisfies

    C subset Chat subset C+epsilon B_2.                       (1)

All displayed row coefficients lie on the delta grid and have absolute value at most 2 dmax R+delta. The coefficients can be stored in

    O(M^2 log(2+dmax R M K0/epsilon))                          (2)

bits, apart from the elementary encoding of the block profile. No original coefficient magnitude, original Slater margin, or inverse singular value appears.

The representation retains the original PSD blocks and adds s+2M+2n scalar inequalities. As one block-diagonal LMI its order is

    ell+s+2M+2n.

For one original order-d block this is at most

    d+d(d+1)+4n+3.

The returned LMI has a strictly feasible point at x=0 for which every PSD/scalar block has minimum eigenvalue or slack at least

    gamma > epsilon/(48 M s R dmax).                         (3)

All latent matrices have trace at most one and every output coordinate is bounded by R. The construction is an existence/encoding theorem; it does NOT give a polynomial-time algorithm to discover a minimum lift or its slack factors from an arbitrary description of C.

### 2.1 Uniformly bounded supporting-slack factors

For u in the unit sphere let h_C(u)=max_(x in C) u.x. The supporting slack is

    h_C(u)-u.x in [0,2R].

Cone factorization gives factors with

    h_C(u)-u.x=sum_h tr(P_x^h Q_u^h),
    P_x^h,Q_u^h>=0.

For any finite row/column set each individual block contribution is between zero and 2R, because every summand is nonnegative. Apply the bounded normalization lemma of 17 to each block contribution. It gives

    tr(P_x^h)<=1,  tr(Q_u^h)<=2 d_h R.                       (4)

These trace bounds are uniform in the number of sampled points and directions. Compactness and the finite intersection property give one global factorization satisfying (4) for every x and u. This does not assume that one congruence normalizes an arbitrary initially given infinite factorization. Alternatively, take countable dense sets and a diagonal subsequence, and extend the finite equations by compactness.

For completeness, the finite normalization is obtained by maximizing log det T subject to tr(A_i T)<=1 on the common row support. At its positive maximizer, T^{-1}=sum_i lambda_i A_i with lambda_i>=0 and sum_i lambda_i equal to the support dimension. Conjugating row and column factors by T^{1/2} and T^{-1/2} gives row trace at most one and column trace at most dimension times the largest entry. This is the only balancing ingredient.

### 2.2 A maximum-volume basis controls every supporting equation

Form the coefficient vectors

    v_u=( (Q_u^h)_(h), u, -h_C(u) ) in R^M,

using upper-triangular entries for symmetric matrices. The corresponding variable vector uses twice the offdiagonal entries of Z, so the pairing is exactly the matrix trace pairing. Each coefficient has absolute value at most 2 dmax R.

Take the closure V of these coefficient vectors. It is compact. Every limit vector still has PSD matrix components, a unit normal u, scalar -h_C(u), and the same pairing identities with every fixed P_x, because the support function is continuous.

Let k=dim span V<=M. Choose v_1,...,v_k from V maximizing their k-dimensional parallelepiped volume in span V. The maximum is attained and positive. For every v in V, its unique expansion

    v=sum_(i=1)^k lambda_i v_i

satisfies |lambda_i|<=1. Otherwise replacing v_i by v would multiply the volume by |lambda_i|>1. Thus

    sum_i |lambda_i|<=k<=M.                               (5)

The selected basis may have an arbitrarily small smallest singular value. That does not enter (5): the maximum-volume replacement argument controls precisely the coefficient vectors that are needed.

Append zero rows to have M rows. Round every selected coefficient to the nearest delta-grid point, forming Qtilde_i^h, utilde_i, htilde_i. These matrices need not remain PSD; they are coefficients of affine inequalities, not new cone variables.

### 2.3 Exact rounding-error bounds

For x in [-R,R]^n and Z_h>=0 with tr Z_h<=1, the difference between a true selected affine row and its rounded row has absolute value at most

    delta sum_h d_h + delta nR + delta =delta K0=e.          (6)

Indeed a symmetric matrix whose entries have magnitude at most delta has operator norm at most d_h delta, and positivity gives

    |tr((Qtilde_i^h-Q_i^h)Z_h)|
          <=d_h delta tr Z_h<=d_h delta.

For x in C choose Z_h=P_x^h. All true rows vanish, so every rounded row has magnitude at most e. This proves C subset Chat.

Conversely, for any x,Z feasible for Chat, every true selected row has magnitude at most 3e. Equation (5) implies, for every unit u,

    |sum_h tr(Q_u^h Z_h)+u.x-h_C(u)|<=3Me<=epsilon.

The matrix pairing sum is nonnegative. Therefore u.x<=h_C(u)+epsilon for every u. The support-function characterization of a Minkowski sum gives x in C+epsilon B_2. This proves (1).

All feasible pairs (x,Z) lie in a fixed compact product of boxes and PSD trace balls, so Chat is a compact convex set. It is nonempty since it contains C. There is no unclosed-projection step.

### 2.4 Strict feasibility and a genuine margin

Because 0 belongs to C, its row factors satisfy

    sum_h tr(Q_i^h P_0^h)=h_C(u_i),  0<=h_C(u_i)<=R.

Take

    eta=e/(4sR),
    Z_h^0=(1-eta)P_0^h+eta I_(d_h)/(2d_h),  x^0=0.

Then

    Z_h^0 >= eta I/(2d_h),
    tr Z_h^0 <=1-eta/2.

The true row changes by at most eta sR=e/4: the original total is in [0,R], and sum_h tr(Q_i^h)/(2d_h) is in [0,sR]. Rounding adds at most e. Hence every rounded slab has magnitude at most 5e/4, strictly less than 2e, with slack at least 3e/4. Box slacks equal R. The smallest PSD-block eigenvalue is at least

    eta/(2dmax)=e/(8sR dmax)
                 >epsilon/(48 M sR dmax).

This proves (3). The point is not asserted to be efficiently available from C; its uniformly controlled existence is part of the approximation theorem. Since coefficients, variable bounds and this margin are controlled, no hidden original conditioning parameter is needed to describe the approximate SDP.

### 2.5 Bit count

Each rounded coordinate has at most

    T=3+24 dmax R M K0/epsilon                            (7)

possible grid values. This uses delta>epsilon/(6 M K0). There are M rows of M coordinates, including padding. Grid denominators are dyadic, with bit length O(log(2+M K0/epsilon)); all remaining constants are rational with the same controlled length. This proves (2).

## 3. Metric entropy for every PSD block profile

Let H_dvec(n,R) be the class of convex bodies containing zero, contained in R B_2, and admitting the specified block profile. The preceding encodings give a Hausdorff epsilon-net with at most

    T^(M^2)                                              (8)

members. Centers of the net are the rounded sets Chat; they may have the larger order from Theorem A. That is sufficient for a covering-number bound on the original class. Invalid or empty grid descriptions are simply discarded.

Now permit ANY finite product profile with total real cone dimension at most Q. Padding with scalar factors fixed to zero gives total dimension exactly Q. The number of ordered block profiles is at most 2^Q: their total matrix orders are at most Q, and ordered positive-integer compositions with total at most Q number less than 2^Q.

Therefore the union class has a Hausdorff epsilon-net of cardinality at most 2^F, where

    M_Q=Q+n+1,
    F(n,Q,R,epsilon)
       =Q+M_Q^2 log_2(3+24 Q R M_Q (Q+nR+1)/epsilon).     (9)

This is the main coefficient-independent entropy bound. In particular a single order-d PSD lift has Q=d(d+1)/2, giving entropy at most O((n+d^2)^2 log(poly(n,d,R)/epsilon)).

An arbitrary number of scalar inequalities cannot be made free in (9). If a model uses u linear inequalities, it contributes at least u to Q. This is essential: unlimited polyhedral descriptions can approximate every compact convex body.

## 4. A direct approximation-counting consequence

Suppose C_1,...,C_H are convex bodies with pairwise Hausdorff distances strictly larger than 4 epsilon. Suppose each has a Hausdorff epsilon-approximant K_i containing zero and contained in R B_2, with total PSD cone dimension at most Q. Encode each K_i by Theorem A at radius epsilon. Two different targets cannot share one net center: triangle inequality would give target distance at most 4 epsilon.

Consequently

    log_2 H <= F(n,Q,R,epsilon).                         (10)

More generally at most 2^F targets in any such separated family can possess those small approximants. This is a lower bound for arbitrary real-coefficient approximate lifts; rounding is a proof tool, not an assumption placed on competitors.

Milestone 21 constructs H doubly exponential in the ambient dimension while every target is centrally symmetric, nearly spherical, positively curved, real analytic and basic semialgebraic. It yields exponential approximate SDP dimension lower bounds without using weak infeasibility, corners, flat boundary pieces, or nonattained optimization.

## 5. Scope and references

The result is an existence and description-length theorem, not a polynomial-time discovery algorithm for optimal lifts. The original exact body need not have a rational exact lift. Its rational epsilon-approximation uses additional scalar constraints and a quadratic order overhead. No claim of an order-preserving rationalization is made.

The entropy bound is for standard charged SDP resources. The earlier curvature resource, which grants scalar inequalities for free, has completely different approximation behavior.

Classical inputs and related primary sources:

- Gouveia, Parrilo and Thomas, Lifts of convex sets and cone factorizations, Math. Oper. Res. 38 (2013), arXiv:1111.3164.
- Fawzi, Gouveia, Parrilo, Robinson and Thomas, Positive semidefinite rank, arXiv:1407.4095.
- Briet, Dadush and Pokutta, On the existence of 0/1 polytopes with high semidefinite extension complexity, arXiv:1305.3268.
- Averkov, Kaibel and Weltge, Maximum semidefinite and linear extension complexity of families of polytopes, arXiv:1605.08538.

The supporting-slack normalization is rederived rather than treated as a new theorem. The explicit max-volume compression, rational approximation, Slater margin and compact-shadow entropy statements are the claims proved here. No comprehensive historical-priority claim or named open-conjecture resolution is asserted.