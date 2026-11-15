# Checkpoint 11 — radial spectral masks conceal thresholds, not their centers

Date: 2026-11-15. Continuation from verified branch HEAD 580e879643c81266a378194583b037b1e753cb2c. Checkpoints 01–10 remain unchanged.

## Scope

This is a structural and arithmetic theorem for positive sums of squared distances to Euclidean balls, realized EXACTLY by affine PSD arrow blocks. It addresses a proposed extension of checkpoint 08. It is NOT a universal theorem about arbitrary affine PSD pencils and does not close the dimension-growing rational minimax frontier.

The new invariant is the list of distinct centers with their positive first radius moments, together with one aggregate quadratic polynomial. A single exact scalar exterior value identifies this invariant in a declared rational class. Matching exterior moments can conceal individual radii, but cannot conceal a new rational center or a hidden rational rotation of the center configuration.

## 1. Natural conic class and its exterior invariant

Let d>=2, and let

    F(x) = (1/2) sum_{j=1}^J w_j (||x-c_j||-r_j)_+^2,

where w_j>0, r_j>0 and c_j in R^d. Combine repeated centers. For each distinct center c put

    a_c = sum_{j:c_j=c} w_j,
    b_c = sum_{j:c_j=c} w_j r_j > 0,
    e_c = sum_{j:c_j=c} w_j r_j^2.

Define

    A=sum_c a_c,
    B=sum_c a_c c,
    C=sum_c (a_c ||c||^2+e_c),
    P(x)=(A/2)||x||^2-B.x+C/2.

Outside all the balls, expansion gives the exact expression

    F_ext(x)=P(x)-sum_c b_c ||x-c||.                    (1)

Its invariant is I(F)=(P,{(c,b_c)}), with centers unordered.

For rational w,r,c the objective is a natural rational PSD-distance objective. Express each w_j as a sum of at most four rational squares w_j=sum_l s_jl^2, taking s_jl>=0, and use the blocks

    s_jl [[r_j,(x-c_j)^T], [x-c_j,r_j I_d]].

A block has only one potentially negative eigenvalue, s_jl(r_j-||x-c_j||). Summing its negative-square energies gives F exactly. The coordinate Gram matrix is 2A I_d. Thus A=1/2 makes the x chart Frobenius isometric. A separate fixed rational isometric weak-infeasibility tail may be appended with disjoint matrix support.

This block construction is not an epigraph transfer. Zero infimum of F means the balls intersect: F is coercive because A>0 and J is finite, so its nonnegative minimum is attained. The appended zero-infimum infeasible tail then makes the complete pencil genuinely weakly infeasible.

## 2. Exact classification of exterior equality

THEOREM A. Two functions of the displayed form in the same dimension d>=2 agree on some nonempty open set exterior to every ball of BOTH functions if and only if their invariants I(F) agree. In particular agreement on every sufficiently large x is equivalent to invariant equality.

PROOF (valid even for real coefficients). Subtract their exterior expressions and combine centers:

    Q(x)-sum_{c in S} gamma_c ||x-c||=0               (2)

on a nonempty open set avoiding the finite set S. The left side is real analytic on R^d minus S. That domain is connected when d>=2, so the identity theorem extends (2) throughout it. Continuity extends the equality to all R^d. At a chosen c0, Q and all norm functions with centers different from c0 are differentiable in a neighborhood. The function ||x-c0|| is not differentiable at c0. Equation (2) therefore forces gamma_c0=0. Repeat for every center; the remaining polynomial Q is zero. Thus every b_c and P agree. Since b_c>0, the two lists have exactly the same centers. Conversely identical invariants give identical expressions (1) wherever both expansions apply. QED.

Individual a_c and e_c are NOT always determined. Only their aggregates A,B,C are. If the centers are affinely independent, A and B determine the a_c by an affine linear system; even then the e_c are generally only known through their total. No unsupported full-radius recovery is claimed.

Strict positivity of the radii and weights ensures b_c>0. A zero-radius term is a polynomial quadratic and can disappear into P; this theorem deliberately excludes such invisible sites. In d=1, norm functions become affine on either exterior ray and the conclusion is false. The earlier univariate moment-matching examples are consistent with this boundary.

## 3. Rational arithmetic turns exterior observability into one scalar query

Assume all parameters are rational, there are at most M distinct centers, and a KNOWN bound B0>=1 satisfies

    ||c_j|| <= B0,   r_j <= B0.

No bound on coefficient heights or on J is required for the following information theorem. A finite binary input cap also supplies a computable B0, so the assertion applies to every proposed finite polynomial-encoding hard prior of this radial type.

THEOREM B. There is an explicit algebraic query q, chosen using only d,M,B0, such that one exact value F(q) identifies I(F) uniquely in the entire declared rational class. Neither gradients nor a germ oracle are required. The query is exterior to all candidate balls. It can be decoded by terminating rational enumeration and exact equality tests; no efficient bit-runtime claim is made.

### 3.1 A bounded-degree separation polynomial

Work over K=Q(x_1,...,x_d). For a rational center c define

    Q_c(x)=sum_i (x_i-c_i)^2.

For d>=2 this is irreducible over Q[x]: after a rational translation it is the sum of d squares, a quadratic with no real linear factor. Different centers give nonassociate irreducibles (the common normalized quadratic part fixes the scalar multiple). Unique factorization therefore makes their square classes independent in K*/K*^2. The resulting multiquadratic extension has independent sign automorphisms for the sqrt(Q_c). In particular 1 and these individual square roots are linearly independent over K. These are standard elementary multiquadratic-field facts, not a new Galois theorem.

Consider two different invariants, each with at most M centers. Their exterior-expression difference has the form

    E(x)=Q(x)+sum_{i=1}^k gamma_i sqrt(Q_ci(x)),
    k<=2M, deg Q<=2,

after equal centers and zero coefficients are removed. It is a nonzero algebraic element by the preceding independence (or Theorem A). Form its norm by multiplying the 2^k expressions obtained by independently changing all square-root signs. The result N(x) is a NONZERO rational polynomial. Sign invariance removes all odd root powers, so no denominators in x are introduced. Each factor has weighted total degree at most two, and hence

    deg N <= 2^(k+1) <= D:=2^(2M+1).                 (3)

If the positive-real exterior expressions agree at an ordinary real x, then one factor is zero there, and N(x)=0. This implication does not presume that every conjugate is a physically positive square root.

### 3.2 One common algebraic point avoids every such accidental equality

Set L=D+1, N0=L^d, and let alpha be the positive root of z^N0-2. Eisenstein's criterion gives degree N0 over Q. Put

    v=(alpha,alpha^L,...,alpha^(L^(d-1))).

No nonzero rational polynomial of total degree at most D vanishes at v. Indeed substituting v maps distinct monomials to distinct powers of alpha, by base-L expansion of the coordinate exponents; the maximum exponent is at most L^d-1. The resulting nonzero polynomial has degree below alpha's minimal degree.

Choose the integer K0=ceil(B0), set eta=1/(4d), and define

    q=4 K0 e_1+eta v.                                (4)

Translation and rational scaling preserve the nonvanishing property. Every entry of v is between 1 and 2. Thus ||eta v||<1/2 and ||q||>4K0-1/2>2B0. Consequently ||q-c_j||>r_j for EVERY candidate, as required. If two invariants had the same value at q, (3) would contradict the nonvanishing property. This proves uniqueness.

For an effective decoder enumerate unordered finite lists of at most M distinct rational centers within the envelope, positive rational b_c, and rational polynomials P of degree at most two; evaluate P(q)-sum b_c ||q-c|| exactly and stop at a match. The true invariant occurs at a finite enumeration index. Any matching list must be that invariant by the same norm argument. The enumerator need not decide whether every candidate list admits a particular radius decomposition. Exact algebraic comparisons, which the original model permits, suffice.

The degree N0=(2^(2M+1)+1)^d can be enormous. The bound concerns oracle CALLS only. It does not assign free finite-precision robustness to this encoding. At d=1 the square-class argument fails for exactly the same reason as Theorem A.

## 4. Hidden rotations and a limit of the compact-mask architecture

Checkpoint 08 uses two centers +/-e and exchanges moment-matched radius lists. Theorem A explains exactly why those labels can be concealed outside a bounded region: their centers, first moments and aggregate quadratic coincide. If a rational orthogonal rotation changes the center configuration, Theorem B recovers the new configuration from one sufficiently exterior scalar query. Only rotations preserving that configuration are unobservable; such rotations do not create new center geometry.

Thus a rational hidden rotation cannot simply be added to a finite collection of ball-distance blocks and assumed to remain hidden outside the masks. What remains unknown after the exterior query is threshold information (individual radius lists), not the entire center geometry. This conclusion is global and exact; it is not based on discarding small exterior terms.

A matching optimization reduction using the recovered centers is proved in checkpoint 12. Neither theorem covers general noncommuting affine PSD factors, variable diagonal shifts, arbitrary ellipsoidal metrics, or all rational PSD-distance functions.

## 5. Attribution and frontier status

Linear independence and interpolation of radial kernels have substantial classical antecedents, including C. A. Micchelli, Interpolation of scattered data: distance matrices and conditionally positive definite functions, Constructive Approximation 2 (1986), 11–22. The analytic-identity/cusp proof and the multiquadratic norm device here are elementary; no claim of inventing radial-basis independence, Galois norms, or algebraic query coding is made. A full priority determination for their stated conic-oracle combination is not certified.

The original required polynomial-threshold lower distribution, or a universal faster algorithm for ALL rational pencils, is still not proved. This checkpoint supplies an exact observable invariant for a natural proposed masking architecture and is kept separate from the unresolved all-pencil target.
