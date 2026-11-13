# Milestone 21 — exponentially hard SDP approximations of uniformly regular convex bodies

Date: 2026-11-13. Uses the coefficient-independent metric-entropy theorem in 20. The hard targets have no corners, flat directions, unbounded fibres in their original description, nonattained linear optima, or nonsemialgebraic boundary obstruction. They are centrally symmetric, nearly spherical, real-analytic, rational basic semialgebraic bodies with uniformly bounded positive principal curvatures. Each target DOES admit a finite exact SDP lift. Nevertheless even fixed-error approximations require exponentially large SDP resources.

This is a representation-complexity statement, not a complexity-class separation and not a claimed solution of a named conjecture. Counting lower bounds and slack-factorization methods are classical; 20 explains their antecedents. The finite exact representability of the polynomial targets uses Helton–Nie's published sufficient theorem. The combination and all quantitative claims used below are proved explicitly. Historical priority for the combined statement is not certified.

## 1. Main theorem

Let epsilon_star=2^(-19). For every integer n>=16 there exists an even rational polynomial P_n in n variables for which

    C_n={x in R^n : P_n(x)<=1, ||x||_2^2<=4}

has all the following properties.

(a) It is a centrally symmetric convex body and

    B_2 subset C_n subset (1+2^(-14)) B_2.                  (1)

(b) Its entire boundary is the nonsingular real-analytic hypersurface P_n=1 inside the ball of radius two. Every principal curvature is in [1/2,2]. In addition the defining polynomial can be chosen with

    (1/4) I <= Hess P_n(x) <= 17 I   for ||x||<=2.          (2)

(c) C_n has some finite EXACT semidefinite lift.

(d) Let K be ANY convex body with d_H(K,C_n)<=epsilon_star. Every real product-PSD lift of K, using blocks of orders d_1,...,d_s, satisfies

    sum_h d_h(d_h+1)/2 > floor(2^(n/2)).                   (3)

Arbitrary real coefficients, affine couplings, free auxiliary variables and singular lifted faces are allowed. Scalar inequalities count as order-one blocks. In particular, every SINGLE PSD lift of K has order

    d > floor(2^(n/4)),                                  (4)

and every LP lift has more than floor(2^(n/2)) scalar inequalities.

(e) Every nonzero linear objective on C_n has a unique optimizer. For a unit maximizing direction u and its optimizer x(u),

    h_Cn(u)-u.x >= (1/4)||x-x(u)||^2   for every x in C_n,
    ||x(u)-x(v)|| <= pi ||u-v||       for unit u,v.         (5)

The quantitative regularity in (1), (2), (5), and the curvature bounds is independent of n. The degree and total coefficient-description length of P_n are NOT asserted polynomial in n. A computable but potentially enormous exact selection procedure is described below; no efficient explicit standard combinatorial hard instance is claimed.

The theorem rules out any universal polynomial SDP-size bound based only on ambient dimension, constant Hausdorff accuracy, roundness, curvature bounds, and the displayed optimization stability. It does not rule out bounds that also depend on polynomial degree, input length, or more restrictive function classes.

## 2. An explicit large family of smooth support functions

Define for t>=0

    phi(t)=exp(-t/(1-t)) for 0<=t<1,
    phi(t)=0 for t>=1.

This is smooth at t=1, with phi(0)=1 and 0<=phi<=1. Direct differentiation, putting s=1/(1-t)>=1, gives

    |phi'(t)|=s^2 exp(1-s)<=4/e<2,
    |phi''(t)|<= (s^4+2s^3)exp(1-s)
                   <=256/e^3+54/e^2<21.                  (6)

Fix 0<r<=1/8. There exist unit vectors u_1,...,u_M such that all 2M points +/-u_i have pairwise chordal distance at least 2r, and

    M >= 1/[2(2r)^(n-1)].                                (7)

Proof: choose a maximal 2r-separated set in real projective space with distance min(||u-v||,||u+v||). The antipodal chordal caps of radius 2r cover the sphere. A chordal cap of radius t<=1/4 has area fraction at most t^(n-1). Indeed project to the equatorial (n-1)-ball: the surface Jacobian is at most two, while total sphere area is at least twice the unit (n-1)-ball volume. Covering by 2M caps proves (7).

Put a=1/512 and for each binary string sigma in {0,1}^M define on the unit sphere

    h_sigma(u)=1+(a r^2)/2
       +a r^2 sum_i sigma_i [phi(||u-u_i||^2/r^2)
                            +phi(||u+u_i||^2/r^2)].        (8)

The open bump supports are disjoint. Each h_sigma is even and smooth, lies between 1+a r^2/2 and 1+3a r^2/2, and different strings satisfy

    ||h_sigma-h_tau||_infinity >= a r^2.                  (9)

The support-function Hessian is uniformly controlled independently of the number of bumps and of n. For f(u)=||u-u_i||^2, on its radius-r support,

    ||grad_S f||<=2r,   ||Hess_S f||_op<=2.

Hence, using (6),

    ||Hess_S(a r^2 phi(f/r^2))||_op
         <=a(2*2+4*21)=11/64.                            (10)

At most one bump is active at any point. Adding the h_sigma I term, (10) shows

    (4/5)I <= Hess_S h_sigma+h_sigma I <= (6/5)I.          (11)

For the upper inequality, use r<=1/8, so the total constant and bump correction beyond one is at most 3/(2*512*64), much smaller than 1/5-11/64. The lower bound follows from 1-11/64>4/5.

A positive smooth function with Hess_S h+hI positive definite is the support function of a smooth strictly convex body. To verify the relevant criterion, extend h positively homogeneously to R^n; its Hessian on tangent directions is (Hess_S h+hI)/||x|| and vanishes in the radial direction. The extension is convex, and its gradient parametrizes the supporting boundary. Here evenness and positivity also ensure convexity across the origin. Thus (8) defines a centrally symmetric C-infinity body B_sigma. Its principal radii are the eigenvalues in (11), so its principal curvatures lie in [5/6,5/4].

The Hausdorff distance between compact convex bodies equals the sup norm distance of their support functions. Therefore the 2^M bodies B_sigma have pairwise Hausdorff distance at least a r^2.

## 3. Rational polynomial smoothing without losing positive curvature

We need the hard bodies to be genuinely semialgebraic and SDP representable, rather than exploiting nonsemialgebraic smooth bump functions.

**Lemma.** Every B_sigma in Section 2 can be approximated arbitrarily closely in boundary C^2 topology, and hence Hausdorff distance, by a centrally symmetric body

    C={P<=1, ||x||^2<=4},

where P is an even rational polynomial, Hess P lies between I/4 and 17I on the radius-two ball, P(0)<1, and P>1 on the radius-two sphere. The approximants can be chosen with principal curvatures in [1/2,2]. Every such sufficiently accurate approximant has a finite exact SDP lift.

### Proof of approximation and the Hessian bounds

Let g(x) be the square of the Minkowski gauge of B_sigma. It is even, homogeneous of degree two, C-infinity away from zero, and C^1 at zero. Its unit level is the boundary of B_sigma.

On that unit level, let nu be the unit outer normal, let h=x.nu, and note

    1<=h, ||x||<1.01, grad g=2nu/h.

On the tangent space nu^perp the Hessian of g is ||grad g|| times the positive second fundamental form. By (11) its quadratic form there lies between (3/2)||v||^2 and 3||v||^2. Euler's identity gives

    Hess g x=grad g,   x^T Hess g x=2.

Write an arbitrary w as w=t x+v with nu.v=0. The mixed Hessian term is zero, and |t|<=||w||, ||v||<2.01||w||. Therefore

    w^T Hess g w=2t^2+v^T Hess g v <=16||w||^2.

Also ||w||^2<=2(1.01)^2(t^2+||v||^2), so

    w^T Hess g w >=(3/2)(t^2+||v||^2)>(1/2)||w||^2.

Homogeneity extends these bounds to every nonzero point. They extend in the distributional sense across zero, since g is C^1 there and its gradient is locally Lipschitz. In particular g-(1/4)||x||^2 is convex.

Convolve g with an even smooth compactly supported probability mollifier of sufficiently small radius. The resulting even smooth function g_rho has Hessian between I/2 and 16I. It converges to g in C^2 on an annulus containing the boundary, has g_rho(0)<1, and is greater than one on the radius-two sphere for sufficiently small rho.

Approximate g_rho, together with derivatives through order two, by a polynomial on a cube containing the radius-two ball. Such approximation follows, for example, by the derivative convergence of multivariate Bernstein polynomials for smooth functions. Approximate its finitely many coefficients by rationals and average P(x),P(-x) to enforce evenness. The error can be made arbitrarily small. In particular Hess P lies between I/4 and 17I, P(0)<1, and P>1 on the radius-two sphere.

The sublevel inside that ball is convex. Its boundary is wholly inside the ball and has grad P nonzero: P is strictly convex there, even, and has its unique minimum at zero with value below one. The implicit function theorem applied to the radial level equation shows that its boundary is arbitrarily C^2-close to that of B_sigma. Therefore it has the asserted curvature and Hausdorff bounds. The polynomial nonvanishing-gradient level set is real analytic.

### Why each approximant is exactly SDP representable

The two defining polynomials are g_1=1-P and g_2=4-||x||^2. On C, g_1 is strictly concave, hence strictly quasi-concave; g_2 is SOS-concave. The set is compact, convex and has nonempty interior. Helton–Nie, Semidefinite Representation of Convex Sets, arXiv:0705.4068v5, Theorem 1.2, therefore gives a finite exact SDP lift. Their Theorem 1.1 also applies: the ball constraint is inactive at the boundary, and the positive multiplier of P produces a positive-definite Lagrange Hessian.

This invocation proves finite existence, not a small upper bound. Polynomial degree and representation order may be large. All other claims in the lemma were established directly. QED.

## 4. Exponential lower bound at one fixed accuracy

Take

    r=1/8,
    epsilon=epsilon_star=2^(-19),
    a r^2=2^(-15)=16 epsilon.

By (7), choose exactly

    M=2^(2n-3)

antipodal bump pairs. The original B_sigma are 16 epsilon separated. Apply Section 3 to each, with Hausdorff error less than epsilon and sufficiently small C^2 error. The resulting rational polynomial bodies C_sigma are pairwise more than 14 epsilon separated, have the Hessian and curvature bounds, and satisfy

    B_2 subset C_sigma subset (1+2^(-14))B_2.

Indeed their support functions are between 1+7 epsilon and 1+25 epsilon, and 25 epsilon<2^(-14). Every C_sigma admits a finite exact SDP lift.

Let Q=floor(2^(n/2)). Any epsilon-approximating convex body K_sigma contains zero and is contained in 2B_2: support functions differ by at most epsilon, and the target contains B_2. Therefore the union-profile entropy bound (9) of 20 applies with R=2.

Put m0=Q+n+1. For n>=16 we have m0<=2Q and Q+2n+1<=2Q. The base inside its logarithm is bounded by

    3+24 Q*2*m0*(Q+2n+1)*2^19
       <=3+192 Q^3 2^19 <=2^27 Q^3.

Consequently the binary logarithm of the net cardinality is at most

    F <= Q+4Q^2(27+3n/2)
      <= (109+6n)2^n
      <= 2^(2n-4)=M/2.                                  (12)

The last inequality holds at n=16 and persists by induction, since the right hand factor 2^(n-4) doubles while 109+6n increases by six.

If a target C_sigma has an epsilon-approximant of cone dimension at most Q, assign that approximant a net center at distance at most epsilon. Two different targets cannot share a center: their distance would be at most 4 epsilon, whereas it exceeds 14 epsilon. Thus at most

    2^F <=2^(M/2)

of the 2^M targets can have such an approximant. At least one, indeed a fraction at least 1-2^(-M/2), has no such small approximant. Select it as C_n. This proves (3).

If a single block has order d<=floor(2^(n/4)), then d(d+1)/2<=d^2<=floor(2^(n/2)), contradicting (3). This proves (4). For LP lifts, cone dimension equals the number of scalar inequalities, giving the LP assertion.

This counting argument permits arbitrary real coefficients and arbitrarily complicated auxiliary equations in competing lifts. The only resource restriction is the counted PSD cone dimension; the finite coefficient grid is supplied by the theorem, not assumed of competitors.

## 5. Uniformly stable linear optimization on every hard body

Let C be any of the final bodies, let u be a unit vector, and let x(u) be the unique supporting point. Positive curvature gives uniqueness and a smooth inverse Gauss map

    x(u)=h_C(u)u+grad_S h_C(u).

Its tangential derivative is Hess_S h_C+h_C I, whose eigenvalues are the principal radii. Since curvature is at least 1/2, these radii are at most two. Along a shortest great-circle arc of length theta between u and v,

    ||x(u)-x(v)||<=2 theta<=pi ||u-v||.

This proves the second assertion in (5).

There is also a global quadratic objective-growth bound. Let v be another unit direction at angle theta in [0,pi], and follow the great circle from u to v. Along it, h''+h<=2. Variation of constants gives

    h_C(v)<=x(u).v+2(1-cos theta)
            =2+(x(u)-2u).v.

Thus C lies in the radius-two ball centered at x(u)-2u. For x in C,

    ||x-x(u)+2u||^2<=4,

which rearranges to

    h_C(u)-u.x >= ||x-x(u)||^2/4.

This proves (5). In particular objective error eta forces distance at most 2 sqrt(eta), uniformly in n and the selected body. The lower-bound construction has no degeneracy or nonattainment in target linear optimization.

## 6. Fixed-dimensional precision lower bounds

The construction also works as epsilon tends to zero with n>=2 fixed. Choose

    r=sqrt(8192 epsilon),  0<epsilon<=2^(-19).

Then a r^2=16 epsilon and the number of disjoint pairs satisfies

    M >= c_pack(n) epsilon^(-(n-1)/2),
    c_pack(n)=2^(-1-(15/2)(n-1)).                         (13)

The same algebraic smoothing gives rational polynomial bodies between B_2 and (1+32 epsilon)B_2, with curvature in [1/2,2], Hessian bounds (2), and finite exact SDP lifts.

The entropy bound in 20 implies that, for sufficiently small epsilon, some such body requires

    total real PSD cone dimension
       >= c_n epsilon^(-(n-1)/4)/sqrt(log(1/epsilon)),     (14)

where c_n>0 depends only on n. For a single matrix this gives

    PSD order >= c'_n epsilon^(-(n-1)/8)
                              /(log(1/epsilon))^(1/4).   (15)

To justify the powers explicitly, put Q=floor(c epsilon^(-(n-1)/4)/sqrt(log_2(1/epsilon))). For small epsilon, Q dominates n, m0<=2Q, and the logarithm in (9) of 20 is at most C_n log_2(1/epsilon). Thus F<=C'_n Q^2 log_2(1/epsilon). Choose c small enough that this is at most half the lower bound for M in (13). The separated-family argument proves (14); q<=d^2 gives (15).

The targets in this statement depend on epsilon. It does not assert that one fixed semialgebraic planar body requires unbounded order as accuracy improves: that would contradict its finite exact lift. Nor are the exponents in (14)–(15) claimed optimal.

Consequently no size bound polynomial only in log(1/epsilon), with constants depending just on n and the displayed curvature/roundness bounds, can cover all such regular bodies. This is a uniform-family impossibility, not a lower bound on optimizing any one explicitly short input polynomial.

## 7. Exact selection is computable, but not efficiently so

The proof is existential through packing and counting. It can be turned into a terminating, generally impractical selection procedure for rational P_n:

1. Enumerate even rational polynomials.
2. Check the compact-body, ball-inclusion, Hessian and curvature conditions by real quantifier elimination.
3. For every product-PSD profile of cone dimension at most Q, decide whether any real-coefficient lift of that profile represents a convex body within epsilon_star of the candidate.
4. Return the first candidate for which all such approximation tests fail.

Step 3 is a finite first-order formula over the real numbers. A lift can be written with variables (x,Z), and at most n+q+1 affine equalities, since only the coefficient span matters. Positivity is expressible by principal minors. Closedness, containment and Hausdorff distance between the represented sets are also first-order properties. The finitely many profiles and the real quantifier-elimination theorem therefore give decidability of each test. Existence established above ensures eventual termination.

No polynomial bound on this search, polynomial degree, coefficient length, or initial combinatorial description is claimed. This does not give an efficient explicit family comparable to the matching or correlation polytopes.

## 8. Operational consequence and exact limits

Hausdorff distance between compact convex bodies equals

    sup_(||u||=1) |max_(x in K)u.x-max_(x in C)u.x|.

Thus (3) rules out a single small SDP formulation that approximates the optimal value of EVERY unit linear objective to epsilon_star. If K is an outer relaxation, some objective overestimates by more than epsilon_star; for an inner approximation, some objective underestimates by more than epsilon_star. The formulation is fixed across objectives. This is not a lower bound for arbitrary objective-dependent algorithms or separation-oracle methods.

Each target is exactly SDP representable, and its own optimization is uniformly stable. Therefore the obstruction is formulation size rather than nonrepresentability, poor target geometry, or weak infeasibility. Infinite coefficient precision cannot circumvent it because 20 normalizes and rounds arbitrary lifts automatically.

A complex Hermitian order-d lift can be realified to real order 2d, so the exponential single-block conclusion also holds for complex lifts up to a factor of two in order. No stronger complex dimension formula is asserted here.

The proof extends classical counting ideas and uses Helton–Nie's existence theorem; it is not a claim that smoothness-based lift complexity was a named previously open conjecture. The main proven statements are the explicit robust lower bound (3), its coexistence with (1), (2), (5) and finite exact lifts, and the uniform precision consequence (14)–(15).

Primary antecedents: Gouveia–Parrilo–Thomas, arXiv:1111.3164; Briet–Dadush–Pokutta, arXiv:1305.3268; Averkov–Kaibel–Weltge, arXiv:1605.08538; Helton–Nie, Semidefinite Representation of Convex Sets, arXiv:0705.4068v5, Theorems 1.1–1.2. The bounded-factor and compression details used here are proved in 17 and 20.