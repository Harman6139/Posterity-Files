# Checkpoint 07 — necessary coordinate dimension and the Clifford mask obstruction

Date: 2026-11-15. These are upper bounds and necessary conditions, not a matching minimax theorem for the entire rational class.

## 1. A dimension-explicit information upper bound

Let f:R^d->R be nonnegative, convex and 1-smooth, with inf f=0 and a known bound

    rho_f(s)<=C s^(-beta), 0<s<=s0,

where beta,C,s0 are fixed. No minimizer or rational representation is assumed. Exact values and gradients are supplied, and computation between queries is uncharged.

THEOREM A. For 0<epsilon<=min(1,4s0), a deterministic measurable algorithm returns f(x)<=epsilon using at most

    2 + floor( d log((R+r)/r) / [-log(1-e^(-1))] ),  (1)
    R=max(1,C(epsilon/4)^(-beta)), r=sqrt(epsilon)/4,

queries. In particular the bound is O_{beta,C}(d[1+log(1/epsilon)]). The classical accelerated method also gives O_{beta,C}(epsilon^(-beta-1/2)), so the better of these two guarantees is available when the dimension and profile constants are supplied.

PROOF. There is a finite u with f(u)<=epsilon/4 and ||u||<=R. Nonnegative 1-smoothness gives ||grad f(u)||<=sqrt(2f(u)). For ||v-u||<=r, the descent inequality implies

    f(v)<=epsilon/4+epsilon/(4sqrt(2))+epsilon/32<epsilon/2.

Thus the epsilon/2-sublevel contains the full ball B(u,r), and that ball is contained in K0=B(0,R+r). Its location is not known or needed.

At each iteration query the centroid c of the current convex body K. If f(c)<=epsilon, return c. Otherwise grad f(c)!=0, since a zero gradient of a convex function would attain its zero infimum. For every v with f(v)<=epsilon/2, convexity gives

    <grad f(c),v-c> <= f(v)-f(c)<0.

Keep the central halfspace with this nonpositive inner product. It preserves B(u,r). Grunbaum's centroid inequality says that either central halfspace of a convex body retains at least e^(-1) of its volume. Thus the retained body has at most (1-e^(-1)) times the preceding volume. After k unsuccessful cuts,

    vol K_k <= vol(B(0,R+r))(1-e^(-1))^k,
    vol K_k >= vol B(u,r).

These are incompatible once k exceeds the ratio in (1), proving the query bound (with a conservative one-call allowance). All queried centroids lie in the initial ball and are finite. QED.

The centroid operation is a measurable function of finitely many halfspaces and the initial ball. The theorem uses the question's unrestricted measurable computation model; it is not a polynomial bit-runtime claim for computing exact centroids. An explicitly arithmetic ellipsoid implementation gives the familiar O(d^2 log((R+r)/r)) alternative without exact centroid computation.

Attribution: the centroid volume inequality and cutting-plane mechanism are classical. The particular comparison ball above is just their specialization to a nonattained smooth objective with an escape bound. Source: B. Grunbaum, "Partitions of mass-distributions and of convex bodies by hyperplanes," Pacific Journal of Mathematics 10(4) (1960), 1257–1261, DOI 10.2140/pjm.1960.10.1257, Theorem 2 and its centroid proof; https://msp.org/pjm/1960/10-4/pjm-v10-n4-p18-s.pdf . The relevant original pages were inspected. This is not claimed as a new cutting-plane algorithm.

## 2. Necessary dimension for the requested polynomial-threshold lower bound

Suppose a proposed hard prior lives in one known coordinate dimension d(T), has the SAME fixed profile constants, and after T exact queries is claimed to force positive failure probability at objective threshold

    ell_T=c (T+1)^(-2/(2beta+1)), c>0 fixed.

Run Theorem A to accuracy ell_T/2. Its query count is at most

    K_{beta,C,c,s0} d(T) log(T+2)

for all sufficiently large T. It succeeds on EVERY instance with no randomness. Therefore a prior satisfying the proposed failure statement must have

    d(T) >= k_{beta,C,c,s0} T/log(T+2)               (2)

on a sufficiently late tail, for a positive fixed k.

For an isometric order-m affine symmetric pencil, d<=m(m+1)/2. Consequently any such lower-bound family also necessarily satisfies

    m(T)=Omega(sqrt(T/log(T+2))).                    (3)

These are necessary, not sufficient, dimension conditions. They do not exclude polynomial-sized constructions. They do exclude attempts that keep the effective unknown dimension fixed or logarithmic while asking for the original power-law threshold.

If a model has additional KNOWN separable tail coordinates of fixed number, they add only that fixed number to the dimension. If an unknown high-dimensional coordinate chart is introduced, that dimension must be counted rather than silently discarded.

## 3. An elementary size bound for exact Clifford radial blocks

Suppose real symmetric M-by-M matrices Gamma_1,...,Gamma_r satisfy

    Gamma_i Gamma_j + Gamma_j Gamma_i = 2 delta_ij I_M. (4)

Then the linear pencil C(y)=sum_i y_i Gamma_i satisfies C(y)^2=||y||^2 I_M, so all its eigenvalues have magnitudes exactly ||y||. Such blocks are a natural attempted way to avoid the additional zero eigenvalues of an arrow representation when building a radial spectral mask.

LEMMA B. Every representation (4) has

    M >= 2^floor(r/2).                               (5)

PROOF. Let s=2 floor(r/2), so s is even. For each subset S of {1,...,s}, let Gamma_S be the increasing ordered product of its generators, with Gamma_empty=I. If S is nonempty and |S| is even, conjugation by any Gamma_j with j in S changes Gamma_S to -Gamma_S. If |S| is odd, choose j outside S; such a j exists because s is even. This conjugation again changes its sign. Trace is invariant under conjugation, so tr Gamma_S=0 for every nonempty S. Anticommutation shows

    Gamma_S^T Gamma_T = +/- Gamma_(S symmetric_difference T).

Thus the 2^s real matrices Gamma_S are mutually Frobenius orthogonal, and each has squared Frobenius norm M (it is an orthogonal matrix). They are linearly independent in the M^2-dimensional real matrix space. Hence M^2>=2^s and M>=2^(s/2). QED.

This is an elementary version of the classical Clifford representation dimension bound. The argument is reproduced to avoid relying on an imprecise representation-size claim; its representation-theoretic content is not claimed new.

## 4. Consequence for one proposed global masking architecture

If an attempted construction uses a block of the form (4) on ALL r unknown optimization coordinates and its total matrix order is polynomial in T, then (5) forces r=O(log T). With only a fixed number of additional known tail coordinates, Theorem A solves every member to the requested polynomial objective threshold in O(log^2 T) exact calls. For large T this is fewer than T.

Therefore this full-coordinate Clifford masking architecture CANNOT satisfy the original polynomial-encoding, polynomial-order, T-query lower-bound target. This conclusion does not depend on whether its coefficients are real or rational.

It is NOT true that every radial PSD expression needs exponential order. The ordinary arrow [[0,y^T],[y,0]] has order r+1 and spectrum +/-||y|| together with r-1 zero eigenvalues. It does not satisfy C(y)^2=||y||^2 I. Shifted-arrow ball-distance constructions are likewise not excluded by (5). Nor does the argument cover a Clifford block on a small known subspace plus genuinely high-dimensional unknown couplings elsewhere. Those additional variables cannot be ignored in applying the information upper bound.

## 5. Current endpoint bracket

At beta=1/2, the previously proved two-coordinate lower family and acceleration still give, for the class allowing arbitrary coordinate dimension and PSD order,

    c log(1/epsilon) <= N_Q(epsilon) <= C/epsilon.

For a specified dimension d, the upper side can be sharpened to

    O(min{epsilon^(-1), d[1+log(1/epsilon)]}).

No matching dimension-dependent lower theorem is proved here. The same-model original lower prior at polynomial-in-T error, or a universal better dimension-independent optimizer, remains the missing theorem. The restricted obstructions in checkpoints 05–07 do not settle that dichotomy.
