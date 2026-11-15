# Sharp examples and necessary obstructions

All proofs are in the manuscript. This file identifies exactly what each example proves; finite verification is supplementary.

## 1. Real feasible, rationally infeasible affine Gram completion

Let

A(t) = diag([[t,2],[2,2t]], [[2,t],[t,1]]).

Positive semidefiniteness forces t=sqrt(2). Nonnegative real columns are (2^(1/4),2^(3/4),0,0) and (0,0,sqrt(2),1). Thus the real fiber is feasible but contains no rational matrix.

The positive semidefinite exposer

W = diag([[2,-sqrt(2)],[-sqrt(2),1]], [[sqrt(2),-2],[-2,2sqrt(2)]])

pairs to zero with the entire affine line. In W=W0+sqrt(2)W1, det(W0)=-8. A rational zero must lie in both coefficient kernels, hence is zero. One arithmetic reduction proves absence of any rational permitted Gram completion. A separator from the original real cone cannot prove this, because that fiber is nonempty.

The first block also equals sqrt(2)*(1,sqrt(2))*(1,sqrt(2))^T. That weight is positive at the chosen embedding but negative at the other embedding. This explains the totally-positive-weight qualification in the descent theorem.

## 2. Strong infeasibility does not ensure a positive cone margin

On CP(R_+^2), observe only L(X)=X_11 and take b=-1. The image is [0,infinity), so infeasibility is strong. Every observation-supported separator is diag(y,0), which vanishes at e_2. A strictly positive margin on all permitted unit vectors is impossible.

The exact correction is observation coercivity: beta=min{||L(X)||:X in C(P), tr(X)=1}>0. It is equivalent to ker(L) intersect C(P)={0} and gives the optimal lift bound tr(X)<=||L(X)||/beta. It is sufficient, not necessary, for closedness of the image.

## 3. Weakly infeasible partial observations

On CP_2, L(X)=(X_11,X_12), b=(0,1). No PSD lift exists, but the rank-one matrices [[epsilon,1],[1,1/epsilon]] approach those observations. Hence the image is nonclosed and no strict separator exists. This differs from both examples above.

## 4. Exact angular grid constant and rational extremizers

For adjacent scalar nodes a<b in [-1,1], the least mean-preserving normalized variance correction is

[1-a*b-sqrt((1-a^2)(1-b^2))]/2.

It equals sin^2 of half the angular gap in arccos coordinates. The rational quadratic (z-a*t)(z-b*t) is nonnegative on the entire grid. At any coefficient below the displayed threshold, a rational y in (a,b) makes its pairing with the corrected atom strictly negative. This proves sharpness with rational inputs, not merely an irrational limiting example.

For m grid intervals the real optimum is sin^2(pi/(2m)); equality requires equal angular gaps. For m>=4 this grid is not rational, because 2*cos(pi/m) would otherwise be a rational algebraic integer strictly between one and two. Rational grids have the same infimum without attaining it. The rational stereographic grid +/- (q^2-j^2)/(q^2+j^2), 0<=j<=q, has exactly 2q+1 nodes and exact correction 1/(q^2+1).

## 5. Fixed nonsimplicial carrier, exponential local walk

For r>=2 and n=r+2, take

K={(t,z,y):t,y>=0, |z_i|<=t}.

It has 2^r+1 rays and is not simplicial. The perfect forms are

P_k=t^2-(2k+1)t*y+(k^2+k+1)y^2.

Their active integer base pairs are (1,0),(k,1),(k+1,1), with z in the corresponding integer boxes. Let T=N+1/2, U=N^2+N+1. Take A_N with (t,y) block [[U,T],[T,1]], z block (U/2)I, and zero remaining entries.

An explicit full-span factorization uses the base vectors (1,0),(N,1),(N+1,1), each with weight 1/2, and independent z_i=-t,0,t with probabilities 1/4,1/2,1/4. Thus A_N is interior and has at most 6*3^r rational Gram columns of O_n(log N) height. The carrier is the full fixed K, the reduction depth is zero, and beta(K,identity)=1/sqrt(n).

From P_1 with its sum-of-all-minima anchor, the exact minimum-ratio rule uniquely follows P_1,...,P_N: exactly N-1 pivots. Positive normal decompositions at every crossing prove this analytically. For N=2^64, the exact number is 18,446,744,073,709,551,615. The code checks compressed certificates, not that trajectory.

After dividing A_N by [2n(N+1)]^2, its norm is at most one and its interior distance is at least

2^(-(2r+4)) / [n^2 * d! * (N+1)^(2d)], d=n(n+1)/2.

The fixed integral map (t,z,y)->(t,z+2t*1,y+t) makes every matrix entry strictly positive. This is a genuine nonsimplicial example before and after the congruence. It disproves a polynomial bound from the stated arithmetic and conditioning resources for the specified rule, not an every-local-rule theorem.

## 6. Sharp lattice exponent in every fixed rational polyhedral cone

For span dimension r>=2 choose a lattice basis B inside the cone, the canonical tridiagonal T_r, and V_q=I-qS. Define P_q[Bz]=z^T V_q^T T_r V_q z. The positive interval vectors transformed by V_q^-1 and B prove relative perfection. The form norm is O_K(q^2), while B(q^(r-1),...,1) is a minimal vector of length Omega_K(q^(r-1)). Therefore the unit-vector margin is O_K(q^(-2(r-1))), making the norm exponent r-1 optimal.

This last mechanism extends an earlier project theorem and known shear geometry. It is credited rather than advertised as independently new.
