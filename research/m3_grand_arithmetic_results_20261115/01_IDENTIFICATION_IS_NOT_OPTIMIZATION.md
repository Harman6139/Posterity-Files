# Checkpoint 01 — exact spectral identification and near-feasibility can have opposite complexity

Date: 2026-11-15. Independent branch, based on 4dd59027dda0e5c5501b79d68248affdcf663e1e. All preceding checkpoints and original milestones are preserved.

## Status

This is a proved separation inside the ORIGINAL rational, free-radius, exact-value/coordinate-gradient conic model. It does not prove an optimization lower bound. In particular it prevents substituting hardness of full spectral/function identification for hardness of returning a near-feasible point. The requested exact-rational optimization frontier remains unresolved.

## Theorem

For every integer n>=1 there is an explicitly known family of 2^n rational, isometrically parametrized, genuinely weakly infeasible PSD pencils with TWO query coordinates, matrix order O(n), and polynomial total rational encoding length, such that:

1. Every member has the identical exact escape profile

   rho_f(s)=(2s)^(-1/2)-sqrt(2s), 0<s<=1/2.

   Thus f(0)=1/2 and the beta=1/2 profile constants and onset are independent of n and the hidden instance.
2. Under the fixed uniform prior, any randomized adaptive algorithm making T<=n arbitrary finite exact value/gradient queries has probability at most 2^(T-n) of identifying the entire objective. Arbitrary exact arithmetic, algebraic or transcendental queries, query magnitudes, and unqueried output descriptions are allowed.
3. Exactly n queries identify the objective. Therefore n queries are necessary and sufficient for identification with success probability at least 2/3.
4. ZERO queries suffice to return a point of objective at most any prescribed epsilon>0, uniformly over this same family.
5. If the richer oracle returns the full PSD projection matrix in the declared matrix coordinates, one query at the origin identifies the hidden member. This is an identification separation, not an optimization lower bound for that richer oracle.

## 1. Moment-matched scalar modules

Write t_+=max(t,0), and set

   h_0(t)=t_+^2+2(t-3)_+^2,
   h_1(t)=2(t-1)_+^2+(t-4)_+^2.

These are sums of squared affine hinge violations, hence convex C1. They are equal for t<=0 (both zero), and for t>=4 (both 3t^2-12t+18). Their first derivatives also agree there, including the endpoints 0 and 4. The identities follow from equality of the number, sum, and sum of squares of the threshold multisets

   A_0=(0,3,3), A_1=(1,1,4):
   |A_0|=|A_1|=3, sum A_0=sum A_1=6,
   sum A_0^2=sum A_1^2=18.

At t=1/2, h_0(t)=1/4 and h_1(t)=0. Thus the two functions differ, but their value AND first derivative can differ only inside (0,4).

This elementary three-threshold moment identity is already used in old checkpoint 03. The new point here is its all-order independent-bit construction and exact information/optimization separation, not invention of the identity.

## 2. Rational isometric pencil

For j=0,...,n-1 set a_j=5j+1. The open intervals I_j=(a_j,a_j+4) are pairwise disjoint. Let

   M=ceil(sqrt(3n)), r=M^2-3n, B=5n+2.

Draw theta=(theta_0,...,theta_(n-1)) uniformly from {0,1}^n BEFORE the algorithm's seed. For each j append three scalar blocks

   (a_j+A_(theta_j,k)-x)/M, k=1,2,3.

Append r further scalar blocks (B-x)/M and the known 2x2 block

   W(z)=[[0,1],[1,z]].

Call the resulting block-diagonal affine pencil X_theta(x,z). Its order is m=M^2+2. All its coefficients are rational. There are exactly M^2 scalar direction entries -1/M in the x direction, so its squared Frobenius norm is one. The z direction is the bottom diagonal entry of W and has norm one. Their supports are disjoint. The coordinate chart is therefore rational and Frobenius isometric.

Its exact natural objective is

   f_theta(x,z) = [sum_j h_(theta_j)(x-a_j)
                     +r(x-B)_+^2]/(2M^2) + phi(z),
   phi(z)=(sqrt(z^2+4)-z)^2/8.

The W block excludes every PSD point: its first diagonal is zero while its off-diagonal is one. At x=0 all scalar blocks are strictly positive; as z->+infinity, W approaches the PSD cone. Thus the affine space is genuinely weakly infeasible. At (0,0), the objective is 1/2.

All coefficients have O(log(n+1)) bits. The sparse description has O(n log(n+1)) bits, and even a dense encoding of the three coefficient matrices has polynomial size. The query dimension stays TWO as n grows.

## 3. Exact common escape profile

Every scalar contribution is nonnegative, and every scalar contribution vanishes at x=0. Hence f_theta(x,z)>=phi(z), with equality at x=0.

Put u=(sqrt(z^2+4)-z)/2>0. Then phi(z)=u^2/2 and z=1/u-u. For 0<s<=1/2, phi(z)<=s implies

   z >= z_s=(2s)^(-1/2)-sqrt(2s)>=0.

Consequently sqrt(x^2+z^2)>=z_s. Equality is achieved by (x,z)=(0,z_s), which has objective exactly s. This proves the asserted exact profile. For example, on 0<s<=1/8,

   (1/2)s^(-1/2) <= rho_f(s) <= s^(-1/2).

The onset and constants do not depend on n, theta, or coefficient heights.

## 4. Exact transcript reduction to inspecting one bit

Grant a stronger oracle: at query (x,z), if x lies in I_j, reveal theta_j; if x lies in no I_j, reveal nothing. This oracle can simulate the natural exact value and full coordinate gradient.

Indeed, there is at most one such interval. Every other module is on an exterior region where its value and derivative are independent of its bit. The padding and phi are known. With the possibly revealed theta_j, the entire natural reply is computable exactly. This simulation is valid at every finite real x,z, including interval endpoints and arbitrarily large or algebraically complicated queries.

A T-query adaptive procedure using the stronger oracle inspects at most T distinct independent fair bits. Conditional on its seed and transcript, the uninspected bits remain independent and fair: at each step the choice of the next inspected index depends only on previously revealed bits and the seed. Thus conditional probability of correctly producing the whole vector is at most 2^(-(n-T)), even when the output is an arbitrary randomized description. Averaging proves the bound.

Different theta give different objective functions: if only bit j is changed, the values at x=a_j+1/2 differ by 1/(8M^2), whereas all other modules have bit-independent values there. Therefore identifying the objective up to global equality requires determining all the bits, not merely choosing a matrix representation among equivalent pencils.

For T=n-1, success is at most 1/2, so success at least 2/3 requires n queries. Conversely query (a_j+1/2,0) for every j. Subtract the known contributions of other modules and the tail. The remaining value is either 1/(8M^2) or zero and determines theta_j. This proves the sharp n-query identification law.

## 5. Zero-query optimization and the stronger spectral observation

For any epsilon>0, put delta=sqrt(2epsilon), x=0, z=1/delta-delta. All scalar contributions are zero and phi(z)=epsilon. This point is known without theta or any query. The exact feasibility residual is delta. There is no optimization information barrier in this family.

If the oracle returns the FULL PSD projection matrix at (0,0), the scalar block entries are unchanged because all are positive. They therefore reveal each threshold triple and hence every bit. This does not contradict the natural oracle lower bound: the full matrix reply contains information discarded by the scalar distance and the coordinate gradient.

Replacing W by any fixed rational isometric tail from old checkpoint 05 gives the same identification/optimization separation for its prescribed positive rational beta. The exact displayed profile formula is asserted only for W; the all-beta extension inherits the fixed tail's profile and constants.

## 6. What this settles and what it does not

This rules out a uniformly constant-query GLOBAL IDENTIFICATION theorem for all rational natural PSD-distance objectives, even with only two coordinates, the same escape profile, and a fixed known rational linear chart. It does NOT rule out a uniformly small-query OPTIMIZATION theorem, because optimization on the example is trivial.

It also shows why a spectral branch count alone cannot be the sought optimization invariant. Branch ambiguity must be related to the location of small-objective sets. Inferring the original Omega(epsilon^(-beta-1/2)) optimization lower bound from these n independent hidden bits would be invalid.

No full frontier resolution, independent refereeing, priority certification, or upper-quintile publication claim is made.