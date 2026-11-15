# Checkpoint 12 — center dimension controls a natural compact-mask conic class

Date: 2026-11-15. Uses new checkpoint 11 and the explicit rational measures in checkpoints 01–02. This is a complete subclass theorem in the original exact value/coordinate-gradient oracle. The arbitrary-pencil dimension-growing power-law frontier is NOT resolved.

## 1. Declared class and exact information model

The objective is

    f(x,z)=F(x)+phi(z),
    F(x)=(1/2) sum_j w_j (||x-c_j||-r_j)_+^2,
    phi(z)=(sqrt(z^2+4)-z)^2/8,

where d>=2, x in R^d, all w_j,r_j are positive rational numbers, c_j are rational, and sum_j w_j=1/2. The balls have a nonempty intersection. Use the rational PSD arrow realization of checkpoint 11 and the separate W(z)=[[0,1],[1,z]] block. This gives rational Frobenius-orthonormal coordinates and genuine weak infeasibility.

Assume f(0,0)<=1 and the same all-scale profile as before:

    (1/2)s^(-1/2) <= rho_f(s) <= s^(-1/2), 0<s<=1/8.

There are at most M distinct centers. An envelope B0>=1 with ||c_j||,r_j<=B0 is supplied. Equivalently a known finite candidate family or a binary input cap supplies such a bound. This is relevant to the requested hard-prior quantifiers, where the algorithm may know the entire finite prior and its encoding bound. No assertion is made about a height-free algorithm when neither a candidate family nor an envelope is supplied.

The oracle remains precisely (f,grad f) at arbitrary finite real points, with exact responses, unrestricted computation and arbitrary unqueried output. No query-radius charge, matrix-projection answer or positive measurement error is added.

## 2. A one-query geometric reduction

THEOREM A. One exact scalar value query identifies all distinct centers and hence their affine hull L. Let

    r=dim L <= min(d,M-1), a=Proj_L(0).

Thereafter approximate optimization is reducible to an r-dimensional problem, preserving a comparison-radius bound with constants independent of the ambient d, number of radius atoms, and envelope B0.

PROOF. Query (q,0), where q is the algebraic exterior probe of checkpoint 11; subtract the known phi(0)=1/2. That theorem recovers the exterior invariant and all centers. Their rational affine hull and a are then exactly computable. Orthogonal coordinates on L may be real algebraic; the ORIGINAL input matrices and chart are unchanged and rational. The model permits such query coordinates.

For any center c in L and any x,

    ||x-c||^2=||Proj_L x-c||^2+||x-Proj_L x||^2.

Every radial loss is nondecreasing in the center distance. Therefore

    F(Proj_L x)<=F(x).                                (1)

For any u with ||u||<=R,

    ||Proj_L u-a||=||Proj_(L-L) u||<=R.               (2)

Thus if f(u,v)<=s and ||(u,v)||<=R, the point Proj_L u has F<=s and radius at most R about a. No bound on ||a|| in terms of B0 is inserted into the comparison cost. Equations (1)–(2) are the reason the ambient dimension and distant centers do not appear in the optimization-call estimate. QED.

When r=0, all balls have the same center a and F(a)=0. After the first query one can return a and an accurate known tail point immediately.

## 3. Dimension-explicit upper bound in the SAME oracle

THEOREM B. For 0<epsilon<=1/2, after the one recovery query, at most

    2 + floor( r log((R+t)/t) / [-log(1-exp(-1))] )

further natural queries suffice, where R=sqrt(8/epsilon) and t=sqrt(epsilon)/8. In particular the total is

    O(1+(M-1)[1+log(1/epsilon)]),                     (3)

uniformly in d, B0, matrix order, coefficient heights, and number of radii.

PROOF. The profile supplies (u,v) with f(u,v)<=epsilon/8 and ||(u,v)||<=R. Put u0=Proj_L u. Then F(u0)<=epsilon/8 and ||u0-a||<=R. The core F is nonnegative and 1-smooth, so ||grad F(u0)||<=sqrt(2F(u0))<=sqrt(epsilon)/2. The same bound applies to the tangential gradient. For w in L with ||w-u0||<=t, smoothness gives

    F(w)<=epsilon/8+epsilon/16+epsilon/128
         =25epsilon/128<epsilon/4.

Hence the ball B_L(u0,t) lies in the epsilon/4-sublevel and in the initial ball B_L(a,R+t). Query the centroid of the current body in L at z=0; subtract phi(0) and project the x-gradient tangentially. If F(c)<=epsilon/2, stop. Otherwise convexity makes the central gradient halfspace contain the entire comparison ball. The classical centroid inequality removes at least exp(-1) of the current r-dimensional volume at each failed query. The displayed count follows by comparing the initial ball volume to that of B_L(u0,t). This is the same unrestricted-computation cutting-plane argument as checkpoint 07, not a new centroid algorithm.

At termination append any finite z with phi(z)<=epsilon/2, for example z=epsilon^(-1/2)-sqrt(epsilon). Then f<=epsilon. If r=0 use the preceding immediate optimizer. An arithmetic ellipsoid implementation instead gives O(1+r^2 log(1/epsilon)) calls and is also sufficient for the fixed-M conclusion. QED.

The outer query in checkpoint 11 uses potentially enormous algebraic degree and requires exact equality tests. Formula (3) is an information bound, not an efficient finite-precision SDP algorithm.

A fixed rational beta-tail may replace phi. The same proof uses R=C(epsilon/8)^(-beta), while t is proportional to sqrt(epsilon), giving O(1+r[1+(beta+1/2)log(1/epsilon)]) calls. This extension presumes the fixed tail and the displayed normalized comparison radius are available; no new tail theorem is claimed here.

## 4. A matching compact, noncommuting rational hard family

This converts the earlier scalar moment construction into a genuinely compact masking construction in the ENTIRE x-space, while retaining disjoint optimization regions.

Fix d>=2, a known unit coordinate vector e, and C0=2. For each word w in {-1,1}^n let mu_w^-,mu_w^+ be the positive rational measures of checkpoint 01, supported on [-1,1], with mass 1/2 each and common moments through degree two. Define their one-sided losses

    L_w(t)=(1/2) integral (s-t)_+^2 dmu_w^-(s),
    U_w(t)=(1/2) integral (t-s)_+^2 dmu_w^+(s),
    H_w=L_w+U_w.

Define the d-dimensional radial core

    K_w(x)=(1/4) integral (||x-C0 e||-(C0-s))_+^2 dmu_w^-(s)
           +(1/4) integral (||x+C0 e||-(C0+s))_+^2 dmu_w^+(s). (4)

It has exactly TWO fixed centers, +/-2e, and all radii lie in [1,3]. Its weights w_j are half the corresponding measure atom weights, so sum w_j=1/2.

### Genuine rational isometry and weak infeasibility

If an original atom weight is sum_{l=1}^4 b_l^2 with b_l>=0 rational, represent its half-weight by TWO copies of each square (b_l/2)^2. Use the resulting eight rational scaled arrow blocks with the indicated center and radius, and append W(z). There are 6(n+1) unmerged atoms. Retaining zero factors gives matrix order

    m=48(n+1)(d+1)+2.

For every x-coordinate the sum of squared coefficient entries is 2 times the total half-weight, hence one. Different coordinates are orthogonal. The z direction is unit and disjoint. The data have polynomial binary description length in n,d; for fixed d the ordinary dense encoding is O_d(n^2). No irrational square-root factors are used.

Let c_w be the hidden scalar center from checkpoint 01, with |c_w|<=2/7. For -2<=t<=2,

    K_w(te)=H_w(t)/2.                                (5)

This follows by substituting ||te-2e||=2-t and ||te+2e||=2+t. In particular K_w(c_w e)=0. The W block has determinant -1, but tends to the PSD cone as z tends to infinity, so each full pencil is weakly infeasible.

At x=0, K_w(0)=H_w(0)/2<=1/4, so f_w(0,0)<1. The lower escape bound follows from the W tail as before. Choosing x=c_w e and the standard tail point gives the upper radius bound rho_f(s)<=s^(-1/2), on 0<s<=1/8. Constants are independent of n and d.

### Exact compact exterior equality

If ||x||>=5, each center distance is at least 3 and therefore every radius atom is active. Expansion depends only on the three moments of mu_w^- and mu_w^+, which are independent of w. Thus ALL values and gradients agree on this entire x-exterior for every z. The x-disagreement set is bounded, unlike a scalar ridge embedded as an unbounded slab. The arrow direction matrices do not commute when d>=2.

### Every successful arbitrary output identifies the word

For every x, put s=e.x. The inequalities ||x-2e||>=2-s and ||x+2e||>=2+s imply

    K_w(x)>=H_w(s)/2.                                (6)

These remain true even when s lies outside [-2,2], since the right linear bounds on distances may then be negative and positive parts are monotone.

With eta=1/4096 and

    eps_tilde_n=(5/768) eta^n,

checkpoint 01 and (6) show that f_w(x,z)<=eps_tilde_n requires s in the disjoint interval I_w. Thus optimization success still names w, including for arbitrary off-axis unqueried outputs.

## 5. Query-level lower bound for arbitrary off-axis probes

One radial query can be simulated by at most TWO calls to the stronger first-mismatch word oracle of checkpoint 02. Define

    a(x)=2-||x-2e||,   b(x)=||x+2e||-2.

Then

    K_w(x)=(L_w(a(x))+U_w(b(x)))/2.                   (7)

For each one-sided loss separately, a first-mismatch word query at its scalar argument determines its value and derivative: outside a selected child interval the remaining measure contributes either zero or its fixed degree-two moment polynomial. The selected reservoir weights depend only on the revealed prefix. This is the same exact recursive locality used for H_w, now checked for each of its two positive components rather than assumed from an equality of their sum.

The chain rule applied to (7) gives the full x-gradient. If x equals one of the centers, the corresponding distance term is inactive on a neighborhood because every radius is at least one, so its gradient is zero; there is no division-by-zero exception. The tail is known. Consequently any adaptive T-query natural transcript, with arbitrary finite x,z and internal randomness, is simulated by at most 2T word queries to the SAME initially sampled w.

The optimal word-identification probability after 2T queries is already proved to be

    S(n,2T)=2^(-n) sum_{j=0}^{min(2T,n)} binom(n,j).

Combining with (6), every T-query natural algorithm has uniform-prior success probability at most S(n,2T) at any 0<epsilon<=eps_tilde_n. The prior is uniform before the independent algorithm seed. This is not an assertion that the exact optimal probability of the radial oracle equals S(n,2T); the simulation is an upper information bound only.

For n=8(T+1), Chebyshev gives

    S(n,2T)<= (T+1)/(2(T+2)^2)<=1/8,

so the failure probability is at least 7/8 at the exponentially small displayed accuracy. PSD order and encoding remain polynomial in T for fixed or polynomially growing d.

For a matching query ORDER, axis probes te from checkpoint 02 lie in [-2,2], so (5) simulates a scalar H_w gradient query by one radial query. In particular O(log(1/epsilon)) calls suffice uniformly in n,d, including via the general upper theorem.

## 6. Sharp fixed-center minimax law and the remaining gate

For every fixed M>=2, in the declared radial-arrow-plus-known-tail class with supplied envelope, taking the worst case over ambient dimensions, finite matrix orders and finite encoding bounds gives

    N(epsilon; success 2/3)=Theta_M(log(1/epsilon)).   (8)

The lower construction already has d=2, two centers and B0=3, and depth n=Theta(log(1/epsilon)). It therefore needs an encoding allowance growing as O(log^2(1/epsilon)); (8) is NOT a joint lower theorem at a fixed finite input cap as epsilon tends to zero. The upper bound is uniform in the supplied cap and envelope. The lower and upper use the same unrestricted exact natural oracle.

For a proposed polynomial-threshold T-query hard prior built from this architecture with M(T) centers, theorem B excludes it whenever M(T)log(T+2)=o(T). More sharply use the recovered affine-hull dimension r(T). Such a prior requires r(T)=Omega(T/log(T+2)), hence M(T) of at least this order. Increasing the ambient dimension, adding more radius atoms at existing centers, or hiding a rational rotation cannot evade that conclusion.

This is a substantive extension beyond the fixed-two-coordinate theorem: it handles unknown rational geometry in arbitrarily large ambient dimension and genuine compact noncommuting masks, and its effective dimension is recoverable from one scalar observation. Nevertheless many-center architectures and general irreducible/coupled PSD pencils remain outside the fixed-M resolution. The original all-pencil Omega(epsilon^-1) lower bound at beta=1/2, or a universal better upper bound, is still unproved.
