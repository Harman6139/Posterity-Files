# Milestone 24 — an explicit Boolean-moment polynomial with large SDP approximation complexity

Date: 2026-11-13.
Branch: laa-track02-gptpro-analytic-frontier-20261112.
Parent research snapshot: 14ab02b502c1eecced43dad2d5bf58bb9ecac445.

## Status, advance, and limitations

This manuscript replaces the existential selection of a hard body in 21 with a single deterministic polynomial formula. The defining polynomial has polynomial degree, rational coefficients of polynomial bit length, and a polynomial-time individual-coefficient oracle. Its sublevel is centrally symmetric, compact, globally strongly convex, and has nonsingular analytic boundary with explicit polynomial curvature bounds. It even has a finite rational SOC representation. Every inverse-polynomial-accuracy SDP approximation nevertheless has stretched-exponential order.

This is NOT the full stronger target proposed in the conversation. The polynomial formula contains a sum over 2^n Boolean assignments; no polynomial-size expanded list or ordinary arithmetic circuit is proved. Curvature/roundness bounds are polynomial rather than dimension-independent, and the hardness tolerance is inverse-polynomial rather than fixed. These distinctions are part of the theorem, not hidden qualifications.

The foundational lower bound is IMPORTED from James R. Lee, Prasad Raghavendra, and David Steurer (LRS), *Lower bounds on the size of semidefinite programming relaxations*, arXiv:1411.6317v1, Theorem 3.8 (equation 3.11) and Theorem 5.3. The new work here is the explicit symmetry, robust-slack, polarity, and polynomial-smoothing transfer with all parameters specified. It is a proved consequence of the cited LRS theorem, not a claimed new proof or improvement of LRS, not a named conjecture resolution, and not a historical-priority certificate. It does not depend on the counting proof in project milestones 20–23.

Primary source:
https://arxiv.org/html/1411.6317

## 1. Completely explicit statement

For n>=2 let

    D = 1+n+binom(n,2) = 1+n(n+1)/2.

Index R^D by the empty set, the singletons, and unordered pairs in [n]. For s in {-1,1}^n define

    w(s) = (1, (s_i)_i, (s_i s_j)_(i<j)).

Let p be the least power of two with p>=2^16 n^4. Define the RATIONAL polynomial

    P_n(x) = ||x||_2^2/(4D)
                + sum_(s in {-1,1}^n) <w(s),x>^(2p),
    C_n = {x in R^D : P_n(x)<=1},
    eps_n = 2^(-20) n^(-4).                         (1)

There are absolute constants c>0 and n0 such that for every n>=n0:

(A) If a convex body A satisfies d_H(A,C_n)<=eps_n, then

    sxc_R(A) >= 2^(c n^(1/8))
              = 2^(Omega(D^(1/16))).                (2)

Here sxc_R counts ONE real PSD block and charges for scalar inequalities. Competitors can have arbitrary real coefficients, arbitrary auxiliary variables, singular feasible faces, and arbitrary affine projections. The same exponential order holds for complex Hermitian lifts by realification. A product-PSD lift must have sum of its block orders, and therefore total cone-coordinate dimension, at least this lower bound. We do NOT deduce a lower bound on the number of arbitrarily high-dimensional SOC factors from this statement.

(B) Put

    a = 2^(-(n+1)/(2p)).

Then

    (a/sqrt(D)) B_2 subset C_n subset sqrt(D) B_2,
    a>=1/2.                                         (3)

The set is centrally symmetric. Its boundary is a nonsingular real-analytic algebraic hypersurface. On C_n,

    (1/(2D)) I <= Hess P_n <= 9 p^2 D I.             (4)

Its principal curvatures kappa satisfy

    1/(10 p D^(3/2)) <= kappa <= 6 p D^(3/2).        (5)

These bounds are polynomial in n and D, not absolute constants. Every nonzero linear objective has a unique optimizer; the resulting objective-growth and optimizer-Lipschitz constants can be bounded polynomially using (5).

(C) P_n is globally SOS-convex. There is an explicit finite rational SOC formulation using at most

    2^n log_2(2p) + D

three-dimensional rotated Lorentz constraints and one scalar inequality. Therefore C_n has a finite exact SDP lift, without invoking a nonconstructive representability theorem.

(D) deg(P_n)=2p=O(n^4)=O(D^2). Its individual rational coefficients have O(n+p log D) bits. Given any multi-index alpha, its coefficient can be computed exactly in time polynomial in n and the output bit length, by the parity formula in Section 7. This does not bound the NUMBER of nonzero coefficients. Direct evaluation of the defining Boolean sum uses exponential work in n.

For the finitely many n<n0, the formula and all geometric/representation claims remain valid; only the asymptotic lower bound (2) is not asserted.

## 2. The explicit source polytope and its roundness

Let

    K_n = conv{+w(s),-w(s):s in {-1,1}^n},
    T_n = K_n^polar
        = {x: |<w(s),x>|<=1 for every s}.             (6)

Distinct squarefree Boolean characters are orthogonal, so

    2^(-n) sum_s w(s) w(s)^T = I_D,
    ||w(s)||^2 = D.                                  (7)

Thus K_n is full-dimensional and centrally symmetric. Its radius is at most sqrt(D).

For any y with ||y||<=1/sqrt(D), assign the following nonnegative weights to signed vertices:

    lambda_(e,s) = 2^(-n-1)[1+e <y,w(s)>], e=+/-1.

They sum to one, and their weighted vertex sum is y by (7). Consequently

    (1/sqrt(D)) B_2 subset K_n subset sqrt(D) B_2.

The polar has the same inclusions:

    (1/sqrt(D)) B_2 subset T_n subset sqrt(D) B_2.     (8)

Everything in K_n is deterministic and explicitly indexed. No random polytope, unknown hard bit string, or search over candidate SDP formulations is involved.

## 3. Robust hardness of this explicit source

Set

    delta_n = 1/(256 n^2).

**Lemma 1.** For all sufficiently large n, every convex body A with d_H(A,K_n)<=delta_n has real PSD extension order at least 2^(c n^(1/8)), for an absolute c>0.

### 3.1 The exact published input

For any odd m>=3, LRS Theorem 5.3 provides a degree-m pseudo-density D_m on {0,1}^m satisfying

    E D_m = 1,
    E D_m (sum_i b_i-m/2)^2 = 0,
    ||D_m||_infinity <= m^(3/2).

For a function f:{0,1}^m->[0,1] with E D_m f < -epsilon, equation (3.11) of LRS gives the following for its pattern matrix M_n^f(S,b)=f(b|S), |S|=m, n>=2m:

    psdrank(M_n^f)
     >= [c0 epsilon n/(m^3 ||D_m||_infinity log n)]^(m/4)
           [epsilon/||D_m||_infinity]^(3/2) sqrt(E f), (9)

with absolute c0>0. This statement is quoted as an input; the manuscript does not reprove it. Changing Boolean coordinates between b_i and s_i=2b_i-1 preserves the identities and the low-degree property.

For 0<=Delta<=1/64 define

    f_(m,Delta)(s)
       = [(sum_i s_i)^2/4 -1/8 +Delta]/m^2.          (10)

Because m is odd, the squared sum is at least one, so this function is positive. Its values lie in [0,1]. Moreover

    E D_m f_(m,Delta) = (-1/8+Delta)/m^2
                         < -1/(16m^2),
    E f_(m,Delta) = (m/4-1/8+Delta)/m^2 >=1/(8m).

Substitution in (9) yields absolute constants c1,c2>0 such that

    psdrank(M_n^(f_(m,Delta)))
       >= c2 m^(-23/4)
                [c1 n/(m^(13/2) log n)]^(m/4).     (11)

This is uniform over the whole indicated shift interval. Choose m as the largest odd integer at most n^(1/8). For sufficiently large n it is at least n^(1/8)/2 and n>=2m. The bracket in (11) is at least n^(1/8) for all sufficiently large n, since n/m^(13/2)>=n^(3/16). Hence (11) is at least

    2^(c3 n^(1/8) log_2 n),                          (12)

after increasing the absolute threshold n0. We use the weaker stretched-exponential bound in the main theorem to absorb polynomial formulation overheads cleanly. No numerical value of the universal constant in the published LRS bound is presumed.

### 3.2 The corresponding inequalities on K_n

For an m-subset S, set

    a_S = (m/4-1/8)e_empty
              +(1/2) sum_(i<j, i,j in S) e_{ij},
    H=m^2/4,
    b_S=a_S-H e_empty,
    ell_S(y)=H+<b_S,y>.

At a positive vertex w(s),

    ell_S(w(s)) = (sum_(i in S) s_i)^2/4-1/8.

Its value lies in [1/8,H-1/8]. At the negative vertex -w(s), the value is 2H-ell_S(w(s)) and is also positive. Thus ell_S is nonnegative on K_n. Also ||b_S||<=m^2, by its displayed coordinates.

### 3.3 Arbitrary Hausdorff approximants

Suppose d_H(A,K_n)<=delta_n and sxc_R(A)=d. Enlarge it by a Euclidean ball:

    A_plus=A+delta_n B_2.

Then

    K_n subset A_plus subset K_n+2delta_n B_2,
    sxc_R(A_plus)<=d+D+1.                            (13)

The second inequality is the block-diagonal product lift, using the standard order-(D+1) ball LMI; it does not assume any representation symmetry.

Every ell_S+2delta_n m^2 is nonnegative on A_plus. Its values at the points w(s) form, up to the positive scalar m^2, the matrix in (10) with

    Delta=2delta_n m^2<=1/128<1/64.

A lift of A_plus of order d+D+1 gives a PSD factorization of this table of order at most d+D+2. To justify the extra scalar and singular cases: compress a supplied lift to its maximum PSD support. It has a relative Slater point. Minimizing any of the displayed affine inequalities has a finite nonnegative minimum, so SDP duality gives a PSD slack plus that nonnegative constant. Append one common scalar coordinate to the point factors to represent all those constants. Free auxiliary directions are eliminated by dual stationarity. No positivity of the projection is required.

Thus (11) applies and forces

    d+D+2 >= c2 m^(-23/4)
                    [c1 n/(m^(13/2)log n)]^(m/4).

Equation (12) absorbs D+2=O(n^2) and proves Lemma 1. The same proof applies to all real coefficients and all nonunique/singular lifted fibres. The Minkowski ball is only used inside this lower-bound argument, not in the returned polynomial's description.

## 4. A quantitative polarity lemma

**Lemma 2.** Let C,A be convex bodies, r B_2 subset C, and d_H(A,C)<=epsilon<r/2. Then A contains (r-epsilon)B_2 and

    d_H(A^polar,C^polar) <= 2epsilon/r^2.             (14)

Proof. Support functions differ by at most epsilon. For y in C^polar and any x in A choose c in C within epsilon of x. Since ||y||<=1/r, y.x<=1+epsilon/r. Thus y/(1+epsilon/r) is in A^polar, giving dist(y,A^polar)<=epsilon/r^2.

Conversely, for z in A^polar, ||z||<=1/(r-epsilon). Choosing nearby A-points for points of C gives h_C(z)<=1+epsilon||z||. Hence z/(1+epsilon||z||) is in C^polar. The distance is at most

    epsilon ||z||^2/(1+epsilon||z||)
        <=epsilon/[r(r-epsilon)]<=2epsilon/r^2.

This proves (14). Polarity preserves exact PSD extension order for full-dimensional bodies containing zero in their interior, by transposing their slack factorizations. This classical fact can alternatively be proved with minimum-face SDP duality. QED.

## 5. Explicit algebraic smoothing and transfer

Write

    S(x)=sum_s <w(s),x>^(2p), Q(x)=||x||^2/(4D).

If x belongs C_n, then each summand of S is at most one, so C_n subset T_n. If x belongs a T_n, with a from Section 1, then

    S(x)<=2^n a^(2p)=1/2,
    Q(x)<=a^2/4<=1/4.

Therefore

    a T_n subset C_n subset T_n.                    (15)

Together with (8) this proves the roundness bounds (3), and polarizing gives

    K_n subset C_n^polar subset a^(-1) K_n.

Since u=(n+1)log(2)/(2p)<1/2, e^u-1<=2u<=(n+1)/p. Consequently

    d_H(C_n^polar,K_n)
       <=(a^(-1)-1)sqrt(D)
       <=2n^2/p <=1/(2^15 n^2).                     (16)

We used D<=n^2 for n>=2 and n+1<=2n.

Now let A approximate C_n within eps_n. Since r=a/sqrt(D)>=1/(2sqrt(D)), Lemma 2 applies and gives

    d_H(A^polar,C_n^polar)
       <=8D eps_n<=1/(2^17 n^2).                    (17)

Equations (16)–(17) imply

    d_H(A^polar,K_n)
       <=5/(2^17 n^2) <1/(256 n^2)=delta_n.

By Lemma 1 and polarity invariance,

    sxc_R(A)=sxc_R(A^polar)>=2^(c n^(1/8)).

This proves (2). It is a deterministic transfer from an explicit LRS pattern matrix, not a count over possible smooth bodies.

Complex Hermitian lifts of order d realify to real lifts of order 2d. Thus the complex lower bound differs by at most that factor and has the same exponential order. Combining several real PSD blocks into one block diagonal cone shows that sum of their orders is at least the single-order lower bound; the sum of their real dimensions is no smaller.

## 6. Convexity, analytic boundary, curvature, and finite exact SOCP

The Hessian is explicitly

    Hess P_n(x)=(1/(2D))I
       +2p(2p-1) sum_s <w(s),x>^(2p-2) w(s)w(s)^T.  (18)

It is positive definite everywhere. It is also a polynomial Gram sum, so P_n is SOS-convex. P_n is even, P_n(0)=0, and its positive quadratic term makes it coercive. Thus C_n is compact, centrally symmetric, and has nonempty interior. The only critical point of P_n is its unique minimizer zero. In particular grad P_n is nonzero on P_n=1, and that level is the entire nonsingular analytic boundary.

On C_n, S<=1. Holder's inequality gives

    sum_s |<w(s),x>|^(2p-2)
       <=2^(n/p) S^((p-1)/p)<=2,

since p>=n. Using ||w(s)||^2=D proves (4) from (18).

On the boundary, (15) gives ||x||<=sqrt(D), so Q<=1/4 and S>=3/4. Euler's homogeneous identities yield

    <x,grad P_n>=2p S+2Q>=3p/2,
    ||grad P_n||>=3p/(2sqrt(D)).                      (19)

Again by Holder,

    ||grad P_n||
       <=2p sqrt(D) sum_s |<w(s),x>|^(2p-1)
                       +||x||/(2D)
       <=4p sqrt(D)+1/(2sqrt(D))<=5p sqrt(D).         (20)

The second fundamental form on tangent vectors is Hess P_n divided by ||grad P_n||. Equations (4), (19), and (20) prove (5).

A lower curvature bound kappa_min gives a polynomial optimizer-Lipschitz bound pi/(2 kappa_min), by integrating the inverse Gauss map along a great circle. It also gives global quadratic objective growth at least (kappa_min/2)||x-x(u)||^2 using the tangent enclosing-ball argument. These constants are polynomial in n, not uniform absolute constants.

For an exact rational SOCP formulation let L=log_2(2p), an integer. For each s introduce y_(s,1),...,y_(s,L) and impose

    [[y_(s,1),<w(s),x>],[<w(s),x>,1]]>=0,
    [[y_(s,j),y_(s,j-1)],[y_(s,j-1),1]]>=0,
                                            2<=j<=L.

These enforce y_(s,L)>=<w(s),x>^(2p). For each coordinate introduce z_i and impose [[z_i,x_i],[x_i,1]]>=0. Finally require

    sum_s y_(s,L)+(1/(4D))sum_i z_i<=1.

The PSD blocks are all order two and all coefficients are rational. Conversely equality choices along the chains and z_i=x_i^2 lift every point of C_n. This proves exact representability with L 2^n+D SOC blocks and one scalar inequality. The formulation is finite but exponential in n, consistent with the lower bound.

## 7. Coefficient-level explicitness: exact formula, no hidden hard selection

Index the coordinates by subsets A of [n] with |A|<=2, including empty. For a multi-index alpha=(alpha_A) with |alpha|=2p, let

    parity(alpha)= symmetric difference of all A,
                     each repeated alpha_A times.

Then the degree-(2p) coefficient is exactly

    [x^alpha] P_n =
       2^n (2p)! / product_A alpha_A!     if parity(alpha)=empty,
       0                                 otherwise.    (21)

Additionally [x_i^2]P_n=1/(4D), since 2p>2. Equation (21) follows by expanding each linear-form power and summing each Boolean character; no lower-bound certificate search is needed to compute a coefficient.

The sum of absolute coefficients of the homogeneous part is at most 2^n D^(2p). Each integer coefficient therefore has O(n+p log D) bits. Formula (21) can be evaluated with exact integer arithmetic in time polynomial in n,p and its output bit length. The degrees and bit lengths are polynomial in n, and p itself is computable in O(log n)-bit arithmetic.

But a coefficient oracle is NOT an ordinary polynomial-size arithmetic circuit. The direct formula contains 2^n powers; the expanded polynomial can have far more monomials. We do not claim polynomial-time evaluation of P_n in n, or polynomial total coefficient-list length. The present theorem supplies deterministic explicitness without supplying the stronger succinctness originally sought.

## 8. What has been gained and what is still missing

Compared with the existential 21 construction:

- There is one displayed rational polynomial for every n, not a hard member selected by counting.
- Its degree is polynomial in ambient dimension, and each coefficient is generated by a simple parity rule with polynomial bit length.
- The lower bound is independent of earlier counting claims: it uses the exact cited LRS theorem and explicit slack transfer.
- The boundary is analytic and strictly curved, with polynomial quantitative bounds, and a finite rational SOC lift is displayed.
- The loss is explicit: only inverse-polynomial precision is established, and near-sphericity/curvature are not bounded by absolute constants.

Still not proved:

1. A polynomial-size ordinary arithmetic circuit or polynomial-length coefficient list for a comparably hard polynomial family.
2. A fixed positive approximation threshold with dimension-independent near-sphericity and principal-curvature bounds for such a succinct explicit family.
3. A new improvement to LRS, a new complexity-class separation, or a named open conjecture resolution.

There is no justification for calling that stronger target closed. This result establishes a concrete bridge toward it, with no conflation of coefficient explicitness, succinct description, and efficient evaluation.

## 9. Attribution and reproducibility

The lower-bound input is LRS 2015 (arXiv version specified above); the parity moment identity, high-even-power approximation, polarity stability, and SOC repeated-squaring steps are elementary or classical ingredients. The contribution asserted here is the particular quantitative deterministic transfer and the resulting polynomial family. Independent priority for this synthesis is not asserted.

A related current theorem of Scheiderer, *Smooth hyperbolicity cones are second-order cone representable*, arXiv:2509.17121v2, proves SOC representability of general compact Nash-smooth strictly curved bodies. The present SOC upper bound is direct and quantitative; it neither reproves that theorem nor contradicts it. Our resource is total representation size, not maximum block order.

The accompanying explicit_moment_smoothing.py implements the coefficient formula, Boolean vectors, evaluations, derivatives, and repeated-square witnesses. test_explicit_moment_smoothing.py checks exact finite identities and records results. Small tests do not prove the all-dimensional SDP lower bound; that proof is Sections 3–5 and explicitly imports LRS.
