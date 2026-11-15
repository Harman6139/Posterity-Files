# Checkpoint 002 — all-order shear obstruction

Date: 2026-11-14. This is a mathematical proof checkpoint, not a flagship-success or priority claim. The corrected universal algorithm, independent source comparison, executable certificates, and venue audit remain unfinished.

## Theorem (explicit exponential paths in every fixed order)

Let n>=2, r=n-1, and N>=3. Let 1 denote the all-ones column in R^r and J=11^T. Use the fixed initial vertex

    P_1 = [[J, -(3/2)1], [-(3/2)1^T, 3]].

The initial vertex depends only on n, not on N. Set

    B_N = [[((N^2-2)/r) I_r, (N/r)1], [(N/r)1^T, 1]],
    A_N = B_N/N^2.

Use the exact prescribed shadow rule and the anchor C0 equal to the sum of ALL minimal-vector rank-one matrices of P_1. The path is exactly

    P_1,P_2,...,P_(N-1),
    P_k = [[J, -(k+1/2)1], [-(k+1/2)1^T, k^2+k+1]],

and makes N-2 adjacent-vertex pivots before the vertex separator test succeeds. Every chosen minimum-ratio ray is unique, although the higher-order vertices are degenerate. The objective-dependent corrected-ray test of milestone 37 cannot stop the path early, for ANY permitted grid size q.

The matrices satisfy ||A_N||_F<=1 and

    dist_F(A_N,CP_n) >= 2/[N^2(N^2+r)].

For every fixed n the total input length and log reciprocal distance are O_n(log N). Therefore the proposed polynomial-in-H pivot bound is false. This uses a fixed admissible initial vertex and anchor, not an input-dependent expensive initialization.

For n=2, the same obstruction also starts at the handoff's canonical P_0=[[1,-1/2],[-1/2,1]], with exactly N-1 pivots and no choice of descending extreme ray at all before termination (proof below).

## 1. Exact minima and perfectness

For x=(u,y)>=0 integral, write s=sum_i u_i and t=s-ky. Then

    P_k[x]=t^2-ty+y^2=(t-y/2)^2+3y^2/4.

If y=0, the minimum one occurs exactly at the r vectors (e_i,0). If y=1, it occurs exactly at all (u,1) with nonnegative integer u and sum u=k or k+1. If y>=2 the value is at least three. Consequently

    Min(P_k)={e_i:i<=r} union {(u,1):u>=0 integral, sum u in {k,k+1}}.

The form is strictly copositive because (sum u,y) is nonzero whenever (u,y)>=0 is nonzero and the displayed binary form is positive definite.

These equalities determine every matrix entry. The e_i fix the top diagonal at one. Comparing (k e_i,1) and ((k+1)e_i,1) fixes each last-column entry to -(k+1/2) and the last diagonal to k^2+k+1. Then (k e_i+e_j,1), for i!=j, fixes each top off-diagonal to one. Thus P_k is a Ryshkov vertex for every k>=1.

## 2. The exact adjacent ray

Define

    R_k=P_(k+1)-P_k=[[0,-1],[-1^T,2k+2]],

where the top-right -1 is the all-minus-one column. It vanishes on e_i and on every (u,1) with sum u=k+1, and is positive (value two) on every active vector with sum u=k.

The linear equalities D[e_i]=0 and D[(u,1)]=0 for all compositions of k+1 force D to be a multiple of R_k: concentrated compositions make all last-column entries equal and determine the last diagonal; compositions k e_i+e_j make every top off-diagonal zero. Hence R_k is an extreme feasible tangent ray.

Convexity makes the entire segment P_k+tR_k, 0<=t<=1, feasible. A vector ((k+2)e_i,1) has value 3-2t, so t>1 is infeasible. Thus the exact neighbor is P_(k+1) and the edge length is one. No oracle assumption is used.

## 3. Anchor and unique minimum-ratio comparison

Direct summation of the active vectors at P_1 gives

    C0_top=(r+4)I_r+J,
    C0_cross=(r+2)1,
    C0_last=r(r+3)/2.

Write

    a0=sum of all top entries=2r(r+2),
    b0=sum of cross-column entries=r(r+2),
    c0=C0_last=r(r+3)/2.

For s=2,...,N-1 set

    lambda_s=(s c0-b0)/(N-s),
    d_s=c0+lambda_s,
    chi_s=a0+lambda_s(N^2-2)-s^2 d_s.

These parameters refer to B_N. For normalized A_N the shadow parameter is N^2 lambda_s; the ratios and chosen rays are unchanged.

We claim C_s=C0+lambda_s B_N is a strictly positive combination of the rank-one normals e_i e_i^T and (u,1)(u,1)^T with sum u=s. The latter are exactly the active normals retained by R_(s-1).

First, lambda_s>0 and

    chi_2=r[N-2/(N-2)]>0,
    chi_(s+1)-chi_s=(N c0-b0)[1-2/((N-s-1)(N-s))]>=0.

The difference formula applies when 2<=s<=N-2; its final value may be zero. Thus every chi_s is positive.

For r>=2, let U_s be the uniform distribution on all weak compositions of s into r parts, and V_s the uniform distribution on s e_1,...,s e_r. Counting by generating functions gives

    E_U[u_i]=s/r,
    E_U[u_i u_j]=s(s-1)/[r(r+1)] for i!=j.

Set tau=r(r+1)/[d_s s(s-1)]. Since d_s>=c0>r(r+1)/2 and s>=2, we have 0<tau<1. Use the mixture tau U_s+(1-tau)V_s, multiply its rank-one expectation by d_s, and add (chi_s/r) sum_i e_i e_i^T. This gives C_s exactly: its bottom entry is d_s, cross entries are s d_s/r (the defining equation for lambda_s), top off-diagonal entries are one, and top diagonal entries are r+5+lambda_s(N^2-2)/r. Every composition receives strictly positive weight. For r=1 the same identity uses the single composition and the positive coefficient chi_s.

For any feasible tangent ray T at P_(s-1), <C_s,T>>=0, with equality only if T annihilates all the retained active normals. Section 2 then forces T to be the ray R_(s-1). Therefore for every A-descending extreme ray T,

    <C0,T>/(-<B_N,T>) >= lambda_s,

with equality uniquely at R_(s-1). This proves the precise minimum-ratio rule, including its behavior at degenerate vertices.

## 4. No early stopping

For k=1,...,N-2,

    <B_N,P_k>=(N-k)(N-k-1)-1>=1,
    <B_N,R_k>=-2(N-k-1)<0.

At k=N-1 the vertex pairing is -1. Every selected R_k is noncopositive: R_k[((k+2)e_i,1)]=-2. Thus the unmodified algorithm takes exactly N-2 pivots.

For the milestone-37 ray correction, put s=k+1, beta=(N-s)/(N^2-1), alpha=beta/(2s). Indeed g=2(N-s) and h=2s(N^2-1), so alpha=g/(2h). The proposed corrected matrix is W=R_k+beta I_n. Its principal (i,n) block has determinant

    beta(2s+beta)-1 < 0,

because 2s(N-s)<=N^2/2 and (N-s)^2<=(N-1)^2 imply

    beta(2s+beta) <= N^2/[2(N^2-1)]+1/(N+1)^2 <= 7/9 < 1.

It has positive diagonal and negative off-diagonal, so it is not copositive. More explicitly, 4s^2 alpha(1+alpha)<1. Every allowed grid q obeying 4q^2 alpha(1+alpha)>=1 therefore has q>s, and its outer shell contains the explicit negative witness (q e_i,1), with R_k value 2(s-q)<0. The corrected-ray procedure must descend rather than stop.

## 5. Normalization, separation distance, and encoding

    ||B_N||_F^2=(N^4-2N^2+4)/r+1<=N^4.

For z=(1,...,1,-N), we have z^T B_N z=-2. The PSD matrix Z=zz^T is copositive, ||Z||_F=N^2+r, and <A_N,Z>=-2/N^2. Duality and Cauchy-Schwarz imply the displayed distance lower bound. Rational entries have bit length O(log N+log n), so L=O(n^2(log N+log n)); for fixed n, H=O_n(log N). Taking N=2^m gives exponential pivot growth in H.

Every visited P_k and R_k has entries bounded in absolute value by N^2+N+1, with denominators at most two. Thus object bit heights remain logarithmic while the pivot count grows exponentially. Height control alone cannot prove the desired bound.

## 6. Active-set output obstruction

Exactly

    |Min(P_k)|=r+binom(k+r-1,r-1)+binom(k+r,r-1).

For each fixed n>=3 this is Theta_n(k^(n-2)), exponentially large in the O_n(log k)-bit encoding of P_k. Therefore even an accelerated algorithm cannot explicitly materialize every minimal vector in polynomial bit complexity on all these strictly copositive vertices. Any general repair must permit compressed active sets or bypass that interface.

## 7. Canonical order-two start: stronger rule-independent obstruction

For n=2, P_k=[[1,-(2k+1)/2],[-(2k+1)/2,k^2+k+1]] is perfect also at k=0. The complete tangent cone has exactly three extreme rays, up to positive scaling:

    R_plus=[[0,-1],[-1,2k+2]],
    R_minus=[[0,1],[1,-2k]],
    S=[[1,-(2k+1)/2],[-(2k+1)/2,k(k+1)]].

For B_N=[[N^2-2,N],[N,1]] and 0<=k<=N-2 their objective pairings are

    2(k+1-N)<0,
    2(N-k)>0,
    (N-k)(N-k-1)-2>=0.

So EVERY rule restricted to A-descending extreme tangent rays is forced to take P_0,...,P_(N-1), hence N-1 pivots. Changing the local pivot tie-breaker cannot fix this family. The same grid-test argument prevents early corrected-ray separation.

## Scope and remaining work

PROVED IN THIS CHECKPOINT: exact explicit paths, unique shadow choices, survival under the stated corrected-ray test, distance and height bounds, and exponential active-set cardinality.

NOT CLAIMED: historical novelty; a polynomial bound for a modified adjacent rule (the order-two result rules out that strategy without extra tests/jumps); completion of the requested general replacement or the 80th-percentile comparison.

An ordinary PSD pretest catches these nonmembers immediately. Thus this is a rigorous obstruction to the specified algorithm/interface, not a lower bound on intrinsic CP separation complexity. A worthwhile repaired method must address all inputs, including doubly nonnegative nonmembers, and must be compared honestly with existing exact fixed-dimensional algorithms.
