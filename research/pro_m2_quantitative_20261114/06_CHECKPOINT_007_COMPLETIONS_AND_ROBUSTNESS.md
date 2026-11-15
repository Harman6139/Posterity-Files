# Checkpoint 007 — robustness and algorithmic completions

Date: 2026-11-14 project date. This checkpoint supplements the already saved proofs; it does not supersede their priority qualifications.

## A. The exponential family can have every entry strictly positive

Use the notation and assumptions of checkpoint 006. Put

    epsilon=1/[2^20 n^6 N^4],
    B'_N=B_N+epsilon J_n,
    A'_N=B'_N/(2nN^2).

Then A'_N is positive definite, every entry is strictly positive, it is outside CP_n, and the same first m_N-1 shadow pivots are uniquely forced. The corrected-grid ray test still cannot terminate that prefix. Moreover

    ||A'_N||_F<=1,
    dist_F(A'_N,CP_n)>=gamma^2/(20nN^2).

### Proof of persistence of the normal certificates

For 2<=s<=m_N let D=2tN-s>=N and u=sc0-b0>0. The perturbed shadow parameter is

    lambda'=u/[D+epsilon(r-s)],

whereas lambda=u/D. Since r+s<=N and epsilon<=1/2,

    lambda'<=2lambda,
    |lambda'-lambda|<=2lambda epsilon(r+s)/N.

All entries of B_N have magnitude at most N^2. With C=C0+lambda B_N and C'=C0+lambda'B'_N, this gives

    max_ij |C'_ij-C_ij|
       <=4 c0 s(r+s)epsilon
       <=4n^2N^2 epsilon
       =1/[2^18 n^4 N^2]=Delta.

Apply exactly the pair-atom construction of checkpoint 006 to C'. Each row's pair-mean functional has sum of absolute coefficients at most r-1, so every remaining-mean coefficient changes by at most r Delta. Every diagonal-completion coefficient changes by at most (s+r)Delta<=N Delta. Before perturbation the remaining means are at least 1/[(r+3)s], and every diagonal-completion coefficient is greater than one. The displayed Delta is less than half these respective margins after multiplication by r or N. All off-diagonal entries also remain positive. Thus every coefficient in the retained-normal representation remains positive, and the unique-ray proof is unchanged.

Positive definiteness is preserved because J_n is positive semidefinite. The inverse-congruence Horn separator W_N satisfies ||W_N||_F<=5/gamma^2, and

    |<epsilon J_n,W_N>|<=5n epsilon/gamma^2<1/2.

(The elementary bound gamma>=2/n is enough.) Hence <B'_N,W_N><=-1/2. The norm and distance claims follow. For the ray correction, beta'=[2tN+r epsilon-s(1+epsilon)]/tr(B'_N)<=1/N, so beta'(2s+beta')<=2/5+1/N^2<1. The same negative shell vector applies.

This removes zeros in the input as well as failure of PSD. The construction is not a claim about canonical tridiagonal initialization in higher order; its fixed start remains P_1.

## B. Quantitative Interior Ryshkov property for rational polyhedral cones

Let K=cone{g_1,...,g_m} be a full-dimensional pointed rational polyhedral cone, with nonzero integral generators satisfying ||g_i||<=R, R>=1. Suppose

    P[v]>=1 for every nonzero v in K intersect Z^n,
    ||P||_F<=M, M>=1.

Then

    P[x]>= ||x||^2 / [8n^2 R^2 (16n^2 R^2 M)^(n-1)]  for every x in K.

To prove this, express any x in K using at most n linearly independent generators: x=B alpha, alpha>=0. For every nonzero nonnegative integer z, Bz is a nonzero integer point in K, so B^T P B belongs to the orthant Ryshkov set of order s<=n. Also ||B||_2^2<=nR^2 and ||B^T P B||_F<=nR^2M. Apply checkpoint 005 in dimension s, enlarge constants to n, and use ||alpha||^2>=||x||^2/(nR^2). The exponent n-1 is already necessary for K equal to the nonnegative orthant.

This is a quantitative finite-generation corollary of the orthant theorem. It is not a claim to replace Oertel–Schürmann's more general qualitative result for all rationally generated closed cones.

## C. A total finite-precision primal-or-separator alternative

The rational ellipsoid stage in checkpoint 003 can be made into a terminating alternative for EVERY normalized rational A and EVERY requested rho=2^(-p)>0:

- return a rational strict copositive W with ||W||_F<=1, <A,W><=-rho/4, and W[x]>=rho/(16n^2)||x||^2 for x>=0; OR
- return rational nonnegative weights lambda_i and rational simplex vectors x_i, with at most d=n(n+1)/2 terms, such that C=sum_i lambda_i x_i x_i^T satisfies ||A-C||_F<rho.

A nearby factor C is NOT a factorization or membership proof for A. Both branches have exact independently checkable rational certificates. At fixed n the entire alternative is polynomial in the input and requested binary precision. No unperturbed rational boundary-factorization assertion is involved.

### Finite cut cone

Retain every simplex atom x used in a copositivity cut, and include the coordinate vectors e_i. There are at most n+T such atoms, where T=8d(d+1)[p+ceil(log2(32n^2))+1]. Let K_T be their finitely generated rank-one cone.

If the ellipsoid stage exhausts T updates without a separator, then dist_F(A,K_T)<rho. Otherwise project A onto K_T and take the norm-one separating normal Z in K_T^* with <A,Z>=-dist_F(A,K_T)<=-rho. The same point Z/2+2n eta I and the same coordinate ball of radius rho/(32n^2), eta=rho/(16n^2), satisfy every atom inequality, every objective inequality and the norm constraint used in the run. Every central cut contains this ball. After T outward-rounded updates the ellipsoid volume is too small to contain it, a contradiction. This proves the strict distance bound to the ACTUAL finite cut cone, not just to CP.

### Exact rational recovery

Enumerate all subsets of at most d atoms. For a subset with linearly independent rank-one matrices G_i=x_i x_i^T, solve

    sum_j <G_i,G_j> lambda_j=<G_i,A>.

Discard singular systems and solutions with nonpositive coefficients. Check the rational squared error exactly. Also test C=0. The orthogonal projection of A onto K_T is represented by a minimal conic set of at most d independent generators with positive coefficients; stationarity in those coefficients gives exactly this system. Hence one enumerated candidate has error strictly below rho. At most

    sum_(k=0)^d binom(n+T,k) <= (n+T+1)^d

systems of order at most d are needed. This is a genuine fixed-dimensional polynomial bound, not enumeration exponential in p.

If each atom is x_i=r_i/D_i with a common integer denominator and height at most B, solve instead using the integer matrices r_i r_i^T. Their Gram entries have O(B+log n) bits, and Cramer's rule gives coefficient heights O(L+d(B+log n)). Thus all intermediate and certificate sizes are polynomial. With the stage bound and ordinary exact linear algebra, a conservative total bit bound is

    O(2^n n^24 (L+p+log n+1)^4
      +(n+T+1)^d n^12 [L+n^2 T+n^2 log n+1]^3).

The dimension dependence is exponential and the recovery exponent depends on d; no variable-dimensional polynomial-time claim is made.

### Rational Gram columns without an integer-factorization assumption

For a positive rational weight lambda=a/b, write the binary expansion of the integer ab. A set bit in an even position 2j is the square (2^j)^2; a set bit in an odd position 2j+1 is the sum of two such squares. Therefore lambda is a sum of O(log(ab)) rational squares with denominator b, obtainable deterministically by bit operations. Multiplying each rational simplex vector by those rational coefficients converts the weighted factor to an ordinary nonnegative rational Gram factor with polynomially many columns and polynomial encoding length.

This does not claim the optimal four-square column count in polynomial deterministic discovery time. The weighted factor with at most d terms is already the compact certificate.

## D. Complete resource accounting for the original adjacent algorithm

The following explicit counts complement checkpoint 005. Put

    M=48n^5/delta,
    U=U_n(M), K=(floor(sqrt(U))+1)^n-1,
    d=n(n+1)/2,
    E=d![2 ceil(U)]^d,
    F=(n+1)! E^(n+1),
    M'=M(1+n^2 E F^2),
    K'=K_n(nM').

There are at most binom(K,d) pivot departures. At a departure vertex one may enumerate at most K integer candidates to recover its complete active set. Enumerating all (d-1)-subsets of active equations, computing one-dimensional nullspaces and checking both orientations against all active inequalities finds every extreme tangent ray, including degenerate cases. The selected ray can be classified by 2^n-1 exact support systems of order at most n+1. If it is not copositive, the bounded neighbor algorithm in checkpoint 005 requires at most K' integer quadratic tests, since the entrywise-sum norm bound along the candidate segment is at most nM'.

Thus a fully elementary implementation has an arithmetic-operation bound of the form

    O( binom(K,d) [ K n^2
       +binom(K,d-1)(d^3+Kd)
       +2^n n^3+K' n^2 ] ),

with rational operation heights polynomial in n,L,log(1/delta). The displayed finite formulas, rather than a hidden copositivity or neighbor oracle, specify every resource. A coarse simplification is single-exponential in a polynomial of n and H. This is intentionally slower than the precision-polynomial replacement; its purpose is to close the exact implementation and bit-height accounting for the original rule.

## Status

PROVED here: persistence for strictly positive PD inputs; a rational-polyhedral-cone margin corollary; a finite precision primal-or-separator algorithm with exact recovery; explicit elementary resource counts for original shadow pivots.

NOT CLAIMED: a new historical discovery of ellipsoid factorization (Dickinson's 2013 thesis already discusses the Anstreicher–Burer–Dickinson ellipsoid approach); a complete priority certification; or a completed journal percentile benchmark. These qualifications will remain in the manuscript's related-work and scope statements.
