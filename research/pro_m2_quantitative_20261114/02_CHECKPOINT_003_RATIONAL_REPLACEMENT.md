# Checkpoint 003 — universal precision-polynomial replacement

Date: 2026-11-14. This checkpoint supplies a dimension-general replacement for the disproved local-pivot complexity claim. Its ingredients (face-stationarity enumeration and the ellipsoid method) are classical. Their use here is NOT claimed as a historically new fixed-dimensional tractability theorem. The new explicit obstruction in checkpoint 002 and this replacement must not be conflated with an independently established upper-quintile publication claim.

## Main replacement theorem

Let A be rational symmetric, ||A||_F<=1, n>=2, d=n(n+1)/2, and let rho=2^(-p)<=dist_F(A,CP_n), with p>=0. There is an exact rational algorithm returning a rational W such that

    ||W||_F<=1,
    <A,W><=-rho/4,
    W[x]>=rho/(16n^2) ||x||_2^2  for every x>=0.

Put

    K=p+ceil(log2(32n^2))+1,
    T=8d(d+1)K,
    ell=ceil(log2(1000(d+1)^4)).

The algorithm uses fewer than T ellipsoid updates and at most T(2^n-1) bordered linear-system tests. Each linear system has order at most n+1. A final independently verifiable support transcript uses another 2^n-1 tests. Every output entry is dyadic with denominator dividing 2^(4T+ell); its numerator has at most 4T+ell+1 bits. The total output matrix encoding is O(n^6(p+log n)).

All arithmetic is rational or integer, including root enclosures and outward ellipsoid rounding. No lattice grid, Ryshkov neighbor enumeration, boundary copositivity oracle, or algebraic-number oracle is assumed.

With input bit length L, the elementary implementation has a conservative bit-cost bound

    O(2^n n^24 (L+p+log n+1)^4),

under classical integer multiplication/division; the displayed exponent is deliberately not optimized. Exact oracle-call, linear-system-size, and output-height bounds above are the more informative resource counts.

When rho is not supplied, start p0=max(1,ceil(log2(32n^2))) and double p after each unsuccessful stage. The algorithm terminates for every nonmember, with the same asymptotic bound replacing p by ceil(log2(1/delta))+O(log n). A failed stage means ONLY that its scale search was unsuccessful; it does not certify exact membership. No finite termination on every CP boundary input is asserted.

## 1. Exact simplex quadratic minimum, including degeneracy

For any rational Q let

    m(Q)=min{x^TQx:x>=0,1^Tx=1}.

For every nonempty support S solve the bordered system

    Q_SS x - mu 1=0,
    1^T x=1.

Discard singular systems and nonsingular systems whose solution has a nonpositive coordinate. Among all retained solutions, take the least mu. Singleton systems always give candidates.

This returns m(Q) exactly. Indeed choose a global minimizer with inclusion-minimal support S. It is positive on S, and first-order stationarity holds. If the bordered matrix were singular, there would be a nonzero pair (z,t) satisfying Q_SS z=t1 and 1^Tz=0. Multiplication by x^T, using Q_SS x=mu1, gives t=0. Hence z!=0, Q_SS z=0, and the objective is constant on x+alpha z. Because z sums to zero, the nonnegative line segment has an endpoint with strictly smaller support, contradicting minimality. Thus at least one global minimizer is in a retained nonsingular system. Every retained point is feasible, so none has value less than the global minimum.

The calculation requires exactly 2^n-1 systems. If Q has dyadic entries of height B, clearing their common denominator and using Cramer's rule bounds solution heights by O(n(B+log n)). Fraction-free elimination supplies a polynomial-bit implementation. For an arbitrary rational Q the same conclusion holds with its total encoding length.

Consequences:

- Q is copositive iff m(Q)>=0; this is a TOTAL exact test, including the boundary.
- If m(Q)<eta, a rational minimizer x gives the violated linear inequality <Q,xx^T><eta.
- If m(Q)>=eta>0, then Q[z]>=eta(1^Tz)^2>=eta||z||^2 for every z>=0.

The complete support transcript can be verified independently by recomputing the bordered systems. Its length is O(2^n n^2(B+log n)); it is exponential in dimension, not in binary accuracy. This does not give a polynomial-time arbitrary-dimension COP test.

## 2. A quantitatively thick separating body

Identify Sym_n with its d upper-triangular coordinates w, WITHOUT square-root scaling. Then ||w||_2<=||W||_F<=sqrt(2)||w||_2. Set eta=rho/(16n^2) and consider

    F_rho={W:||W||_F<=1, <A,W><=-rho/4, m(W)>=eta}.

For delta=dist_F(A,CP_n), conic projection duality gives Z in COP_n with ||Z||_F=1 and <A,Z>=-delta. One direct proof: if B is the nearest CP point, Z=(B-A)/delta; the projection variational inequality gives Z in COP, <Z,B>=0, and the stated pairing.

Let W*=Z/2+2n eta I. Since delta>=rho and delta<=1,

    ||W*||_F<=1/2+rho/(8sqrt(n))<=5/8,
    <A,W*><=-delta/2+rho/(8sqrt(n))<=-3rho/8,
    m(W*)>=2eta.

The Euclidean upper-coordinate ball of radius eta/2 about W* is contained in F_rho: matrix perturbations have Frobenius norm at most eta/sqrt(2), change the target pairing by at most that amount, and change each simplex quadratic value by at most that amount. The norm constraint also retains strict slack. Thus F_rho contains a ball of radius

    r=rho/(32n^2)

and is contained in the coordinate Euclidean unit ball.

## 3. A rational central separation oracle

For a rational center W:

1. If ||W||_F^2>1, use the linear functional X -> <W,X>. Every X in F_rho satisfies <W,X><<W,W>, so its central halfspace is valid. No irrational norm is computed.
2. Otherwise, if <A,W>>-rho/4, cut with the linear functional X -> <A,X>.
3. Otherwise compute m(W). If it is below eta, a rational minimizing x gives the central cut in the direction -xx^T.
4. Otherwise W itself is the required separator.

In ordinary upper-triangular coordinates a matrix functional has coefficient A_ii on a diagonal coordinate and 2A_ij on an off-diagonal coordinate. This factor of two is included in the implementation.

## 4. Completely rational outward-rounded ellipsoids

Use E(c,Q)={w:(w-c)^T Q^(-1)(w-c)<=1}, starting c=0,Q=I_d. Suppose a!=0 is a central cut direction, retaining a^T(w-c)<=0. Set v=Qa and q=a^TQa>0. The exact central update is

    c*=c-v/((d+1)sqrt(q)),
    Q*=d^2/(d^2-1) [Q-(2/(d+1))vv^T/q].

The shape Q* is already rational. Only the center involves a square root.

At iteration t>=0 choose

    theta=1/[100(d+1)^2],
    b_t=4(t+1)+ell,
    h_t=2^(-b_t).

Obtain a rational approximation to c* with coordinate error at most h_t/2 by integer-square-root enclosures; round to the nearest h_t-grid point to get c_hat with coordinate error at most h_t. Let M=(1+theta)^2Q*. Round each symmetric entry of M to the nearest h_t-grid point, then add d h_t I. Call the resulting shape Q_hat.

Inductively,

    lambda_min(Q_t)>=4^(-t),
    lambda_max(Q_t)<=2^t.

For the exact update, Q*>=(d/(d+1))^2Q>=(1/4)Q and Q*<=(4/3)Q. Our precision implies

    ||c_hat-c*||_(Q*)^(-1)<=theta,
    2d h_t<=theta lambda_min(M).

The first inequality makes E(c*,Q*) a subset of E(c_hat,M). Entrywise nearest rounding has spectral error at most d h_t/2, so

    M <= Q_hat <= M+2d h_t I <= (1+theta)M.

Consequently the rounded ellipsoid contains the exact one and retains the eigenvalue bounds, since (1+theta)^3(4/3)<2. This proves containment at every step, not merely numerical stability.

The exact central-update log volume ratio is

    (d/2)log[d^2/(d^2-1)] +(1/2)log[(d-1)/(d+1)]
      = -sum_(j>=0) 1/[2(j+1)(2j+1)d^(2j+1)]
      <= -1/(2d).

Rounding adds at most (3d/2)log(1+theta), which is small enough that the total log ratio is at most -1/[4(d+1)]. After T unsuccessful updates the volume would therefore be less than that of the contained r-ball, a contradiction. This proves the stage bound.

The root enclosure can be generated without iterative numerical floating-point operations. If e=floor(log2 q) and f=floor(log2 max_i |v_i|/(d+1)), choose

    k=max(0,b_t+f+4-e,ceil(-e/2)+2).

Let l=floor(sqrt(floor(q*2^(2k))))/2^k and u=l+2^(-k). Then l>0, l<=sqrt(q)<=u, and the reciprocal interval [1/u,1/l] gives the required center accuracy. Integer comparisons compute e,f, and integer square root computes l. Perfect-square cases can be handled exactly.

## 5. Height and bit-cost accounting

The rounded centers and shapes at time t are dyadic with denominator dividing 2^(4t+ell). The step norm and eigenvalue bounds give ||c_t||_2<=2^(t+1); hence their entry numerator and denominator lengths are at most 5t+ell+O(1).

Support solutions have O(n(t+log n)) bits, and their rank-one cut coefficients have the same order. Input-objective cuts have O(L) bits. Clearing the single common denominator for each cut and using the displayed rank-one ellipsoid update bounds all temporary arithmetic heights by O(n(L+t+log n)). Integer root enclosures retain polynomial height. With fraction-free linear solves and classical integer arithmetic, a conservative per-update cost is O(2^n n^8 (L+t+log n+1)^3). Since T=O(n^4(p+log n)), summing gives the advertised, looser O(2^n n^24 (L+p+log n+1)^4) bound.

At acceptance the norm is at most one, so all matrix entries have absolute value at most one. The output-height bound follows directly from the dyadic denominator, without a coefficient-growth assumption.

For the doubling schedule, choose p0>=ceil(log2(32n^2)). The first stage with p>=ceil(log2(1/delta)) must succeed; its precision is at most twice max(p0,ceil(log2(1/delta))). Geometric summation of stage costs preserves the polynomial bound.

## 6. Implementation and current tests

A pure-standard-library Fraction implementation has been written locally with:

- fraction-free bordered-system elimination;
- exact support enumeration including singular/boundary cases;
- dyadic rounding and integer-square-root center enclosures;
- outward-rounded ellipsoid updates;
- explicit stage budgets and caps that raise exceptions instead of making false membership claims;
- independent exact output checks and support transcripts.

Initial exact runs: four simplex-minimum tests (including zero and singular boundary cases); the n=2,N=3 obstruction input separated in 13 ellipsoid updates; the normalized order-five matrix (I+(3/5)Adj(C5))/3 separated in 84 updates, with positive exact copositivity margin and negative exact target pairing. The latter is doubly nonnegative and non-CP, so the replacement is not limited to the PSD-detectable obstruction family. Full code, regression suite, JSON certificates and manuscript are to be committed next.

## Status

PROVED: a universal rational, polynomial-in-binary-precision replacement with explicit oracle/height bounds; it bypasses rather than accelerates adjacent Ryshkov edges.

NOT CLAIMED: a new historical discovery of fixed-dimensional polynomial tractability, a polynomial-time variable-dimension algorithm, a finite exact membership algorithm for every CP boundary input, or a defensible top-20% venue comparison. The classical face-based/ellipsoid antecedents must be cited explicitly in the manuscript.
