# Milestone 38 — Randomized and parallel minimax complexity without minimizers

Date: 2026-11-14. Branch: `laa-track02-gptpro-analytic-frontier-20261112`.
Parent snapshot: `85a80462e382b5e28c706d24a2e7257c021eb402`.
Manuscript III continuation of 26–27; independent of the other project proofs.

## Status and contribution

This proves the proposed randomized strengthening of 27, not merely a conditional reduction or a resisting oracle chosen after the random seed. A single Haar-frame distribution, fixed before the algorithm starts, defeats EVERY measurable randomized adaptive exact value-and-gradient method at the matching power. Queries, outputs, and computation between queries are unrestricted. The functions are globally convex C2 and globally smooth on the full space; their finite infimum zero is known and unattained. The escape-profile constants and accuracy onset are uniform over the entire hard family, dimensions, and horizons. For rational escape exponent, every function is semialgebraic.

A batch version gives the same dimension-uniform round exponent with any finite number B of simultaneous queries per round. The ambient dimension is allowed to grow, explicitly as O(T^3 log(BT/zeta)). This is NOT a fixed-dimensional lower bound, a stochastic/noisy-gradient result, or a projection-oracle lower bound for explicitly supplied conic programs. Real coefficient bit heights of Haar frames are not bounded.

Random rotations, hidden affine maxima, oracle coupling, and randomized/parallel convex lower bounds are classical. The sparse simplex regularizer is the known 3/2-power (Tsallis/entmax) regularizer, not a newly invented smoothing. All properties used are proved below. The asserted result is the precise nonattainment minimax theorem with uniform escape geometry, exact C2 locality, unrestricted queries, and the parallel extension. Historical priority for this combination has not been comprehensively certified. No named conjecture resolution or publication guarantee is claimed.

## 1. Same normalized escape classes as manuscript 27

Fix beta>0. Put

    theta=2/(2beta+1), nu=2-theta=4beta/(2beta+1),
    p=1/beta,
    b_beta=min(1/4, 1/[4p(p+1)]),
    c_beta=b_beta^beta/2,
    C_beta=1+3/sqrt(nu),
    s_beta=min(1/64, b_beta 2^(-1/beta)).

These are exactly the constants used to define the class in 27. Let F_beta(D) consist of convex C2 functions f:R^D->R with 1-Lipschitz gradient, f(0)<=1, inf f=0 not attained, and

    c_beta s^(-beta)<=rho_f(s)<=C_beta s^(-beta)
                  for EVERY 0<s<=s_beta,                 (1)
    rho_f(s)=min{||x||:f(x)<=s}.

The minimum exists because its feasible set is nonempty and closed and the norm is coercive. All constants in (1) depend only on beta. The class does not allow a horizon-dependent onset or hidden worsening of the profile constants.

An algorithm queries (f(x),grad f(x)) at arbitrary finite points, adapts to past answers and an independent random seed, and returns any finite point, not necessarily queried. Algorithms are assumed measurable, as needed for expectations. The algorithm may know beta, all constants, the exact infimum, and the hard-function template. It does not receive the hidden frame as explicit input.

### Theorem A — randomized minimax exponent

Let E_T^rand be the infimum, over randomized algorithm families indexed by dimension and using at most T queries, of the supremum over all dimensions D and f in F_beta(D) of the expected returned objective gap. Then, for sufficiently large T,

    c (T+1)^(-theta)<=E_T^rand<=C'_beta (T+1)^(-theta),  (2)

where c>0 is absolute. Equivalently the dimension-uniform randomized query complexity for expected gap epsilon is

    Theta_beta(epsilon^(-(beta+1/2))).                  (3)

The same exponent holds for a uniform fixed success probability such as 2/3. It also lower-bounds expected stopping time of algorithms with that uniform success guarantee, as proved in Section 10.

### Theorem B — a fixed high-probability hard distribution

For any integers T>=1 and B>=1 and any 0<zeta<1/2, put m=T+1 and choose

    d >= m+ceil(2^19 m^3 log(8B m^2/zeta)).             (4)

There is one distribution over F_beta(d+1), independent of the algorithm and its seed, such that EVERY randomized algorithm using T rounds and at most B simultaneous queries in each round has

    Prob{f(output)>=2^(-13)(T+1)^(-theta)} >= 1-zeta.   (5)

The probability is jointly over the initially chosen function and the algorithm's seed. Points in a batch are selected before its answers are returned; adaptive sequential queries count as distinct rounds. For rational beta the support consists entirely of semialgebraic functions.

In particular some single fixed function has failure probability at least 1-zeta over that algorithm's own random seed. There is no selection of a function after observing the realized seed. With B=1,zeta=1/4, the expectation lower constant in (2) can be c=3/32768.

## 2. A C2 sparse maximum with exact inactive coordinates

For lambda>0 and a finite vector l define

    S_lambda(l)=max_{w>=0, sum w_i=1}
                   [sum_i w_i l_i-lambda sum_i w_i^(3/2)].   (6)

The maximizer is unique. There is a unique scalar eta such that

    sum_i (l_i-eta)_+^2=(3lambda/2)^2,
    w_i=[(l_i-eta)_+/(3lambda/2)]^2.                   (7)

The formula follows from simplex KKT equations. The left side is continuous, strictly decreasing in eta below max l_i, tends to infinity as eta tends to minus infinity, and tends to zero at max l_i.

The function S_lambda has these properties:

    max_i l_i-lambda <= S_lambda(l) <= max_i l_i;       (8)
    grad S_lambda(l)=w(l), ||w(l)||_2<=1;              (9)
    Lip(grad S_lambda)<=4/(3lambda).                  (10)

For (8), use a maximizing coordinate vertex for the lower bound and nonnegativity of the regularizer for the upper bound. For (10), t^(3/2) has second derivative 3/(4sqrt(t))>=3/4 on (0,1]; its sum is 3/4-strongly convex in Euclidean norm on the simplex, including boundary points by continuity. Conjugacy therefore gives (10).

Importantly S_lambda is C2, not merely C1. The equation in (7) is C1 in (l,eta), and its eta derivative is -2 sum_i(l_i-eta)_+<0. The implicit function theorem gives a C1 threshold eta(l). Each w_i is C1 because positive-part squared is C1. Equation (9) then gives C2 regularity. All these functions are semialgebraic.

Exact locality: the threshold obeys

    eta >= max_i l_i-3lambda/2.                       (11)

Thus any extra coordinate more than 3lambda/2 below the maximum is exactly inactive. Appending any such coordinates changes neither S_lambda nor its derivatives on any neighborhood where the strict inequality persists. This exact inactivity, rather than numerical smallness, is necessary for an exact real oracle.

## 3. A C2 smooth maximum of two functions

For e>0 define the even convex C2 function

    psi_e(t)=|t|,                            |t|>=e,
    psi_e(t)=3e/8+3t^2/(4e)-t^4/(8e^3),     |t|<=e.

The pieces match through second derivatives at +/-e, and

    |psi'_e|<=1, 0<=psi''_e<=3/(2e),
    0<=psi_e(t)-|t|<=3e/8.

Set

    M_e(a,b)=[a+b+psi_e(a-b)]/2.                      (12)

It is convex, C2, semialgebraic, and nondecreasing in each argument. Moreover

    max(a,b)<=M_e(a,b)<=max(a,b)+3e/16,
    M_e(a,b)=max(a,b) whenever |a-b|>=e.              (13)

For C2 convex H,W the Hessian of F=M_e(H,W) is

    omega Hess H+(1-omega)Hess W
           +(psi''_e(H-W)/2)(grad H-grad W)(...)^T,   (14)
    omega=(1+psi'_e(H-W))/2 in [0,1].

This identity gives the global smoothness bound used next.

## 4. The hidden-frame core and the exterior mask

Fix m>=2 and put

    R=m^(beta theta), gamma=R/(16m^(3/2)),
    a=gamma/128=R/(2048m^(3/2)),
    lambda=16a^2, e=64a^2, r0=R/4,
    Delta=aR/sqrt(m)=2^(-11)m^(-theta).               (15)

Let U=[u_1,...,u_m] have orthonormal columns in R^d. For 1<=j<=m set

    l_i(x)=a[<u_i,x>-(i-1)gamma],
    H_(U,j)(x)=S_lambda(l_1(x),...,l_j(x)),
    W(x)=2a[sqrt(||x||^2+r0^2)-R],
    F_(U,j)(x)=M_e(H_(U,j)(x),W(x)).                  (16)

Write F_U=F_(U,m). The radial term W is known and independent of U. It makes F_U coercive and masks every hidden direction sufficiently far from the origin.

### Global regularity and smoothness

The matrix taking x to its j scores has operator norm a, since its normals are orthonormal. Therefore

    ||grad H_(U,j)||<=a,
    0<=Hess H_(U,j)<= (1/12)I.

Also

    ||grad W||<=2a,
    0<=Hess W<= (8a/R)I <=(1/256)I.

Using (14), ||grad H-grad W||<=3a, and e=64a^2,

    0<=Hess F_(U,j)
           <=[1/12+27/256]I=(145/768)I<(1/4)I.       (17)

Every core is globally convex C2 and semialgebraic. The bounds are uniform in all dimensions, m, and the chosen frame.

### The common minimum and a small initial gap

Let mu_m=min_x F_U(x). This minimum exists by coercivity. It is the same for every frame: any two frames in dimension d are related by an orthogonal map, and the rest of the construction is radial. In fact projecting x onto span U cannot increase F_U, so mu_m equals the minimum of the reference m-dimensional coordinate-frame core. It is independent of d as well.

The following uniform estimates hold:

    -(5/2)Delta <= mu_m <= -(15/32)Delta <0;           (18)
    0<=F_U(0)-mu_m<3Delta;                            (19)
    every minimizing point has norm <2R.              (20)

Proof. Write g_U=max_i l_i. For ||x||<=2R, averaging the scores gives

    g_U(x)>=-a||x||/sqrt(m)-a gamma(m-1)/2
             >=-2Delta-Delta/32.

Equations (8), (13) give F_U>=g_U-lambda. Since

    lambda/Delta=16/(2048m)<=1/256,

this is greater than -(5/2)Delta. For ||x||>=2R, F_U>=W>=2aR>0. This proves the lower bound and (20), once the negative comparison below is supplied.

At xbar=-(R/(2sqrt(m)))sum_i u_i, the norm is R/2 and g_U=-Delta/2. Also W(xbar)=aR(sqrt(5)/2-2)<-aR/2<=-Delta/2. Therefore

    F_U(xbar)<=-Delta/2+3e/16=-Delta/2+12a^2
                   <=-(15/32)Delta.

At zero g_U(0)=0 and W(0)<0, so F_U(0)<=12a^2<=Delta/32. This and the lower bound in (18) give (19). QED.

The offset mu_m need not be computed by the algorithm. It is a fixed orientation-independent scalar and can even be supplied as side information. All simulated oracles below subtract this SAME scalar, not the separate minima of their truncated cores. No hidden direction is encoded in the normalization.

## 5. Add an explicit nonattained tail and verify ALL escape scales

With p=1/beta and b=b_beta from Section 1, let

    phi(z)=b(1+z)^(-p),                         z>=0,
    phi(z)=b[1-pz+p(p+1)z^2/2],                z<0.   (21)

This positive function is convex C2 on the whole real line, has second derivative between zero and 1/4, and tends to zero only as z tends to plus infinity. The value and first two derivatives agree at zero. It is semialgebraic for rational beta.

Define the objective on R^(d+1) by

    f_U(x,z)=F_U(x)-mu_m+phi(z).                       (22)

It is convex C2, globally 1/4-smooth and hence 1-smooth. Its infimum is zero and unattained. Taking a core minimizer and letting z tend to infinity establishes the value of the infimum. Also

    f_U(0,0)<=3Delta+b<1.

We verify (1) with constants independent of m and U.

If f_U(x,z)<=s<=s_beta, then phi(z)<=s<b. Thus z>=0 and

    z>=(b/s)^beta-1 >= (b^beta/2)s^(-beta).

This proves the lower profile bound c_beta s^(-beta).

For the upper bound take z=(2b/s)^beta-1>=0. Then phi(z)=s/2 and z<=s^(-beta), since 2b<=1.

If s>=6Delta, take x=0; (19) gives the other gap at most s/2. If s<6Delta, take a core minimizer. Its norm is at most 2R. Since

    6Delta=(6/2048)m^(-theta)<m^(-theta),
    R=m^(beta theta)<=s^(-beta),

the resulting point has total norm at most sqrt(5)s^(-beta). Hence

    rho_fU(s)<=sqrt(5)s^(-beta)<C_beta s^(-beta),       (23)

because C_beta=1+3/sqrt(nu)>3 for nu<2. Thus EVERY instance belongs to the SAME F_beta class as 27. No asymptotic threshold depends on T.

## 6. Exact oracle locality and safe arbitrary-size queries

### Exterior locality

For every j, H_(U,j)(x)<=a||x||. If ||x||>=3R,

    W(x)-H_(U,j)(x)>=a(||x||-2R)>=aR>e.

Thus F_(U,j)=W in a neighborhood of x. The function value and full gradient there contain no information about U, regardless of how large the query is. This is why no artificial query-radius restriction is needed.

### Interior prefix locality

Suppose ||x||<=3R and, at round j,

    |<u_i,x>|<=gamma/8 for EVERY i>=j.                (24)

For any i>j,

    l_j(x)-l_i(x)>=a gamma(i-j-1/4)>=3a gamma/4.

This difference remains at least a gamma/2 throughout the ball of radius gamma/8 about x. But

    3lambda/2=24a^2=(24/128)a gamma<a gamma/2.

The threshold in the j-prefix maximization is at least l_j-3lambda/2. Every later score is strictly below it. Setting their weights to zero satisfies the full simplex KKT system, so

    H_(U,m)=H_(U,j), and F_U=F_(U,j)

on that entire neighborhood. Their values, gradients, and Hessians agree exactly at x. This is an equality of functions on a neighborhood, not an appeal to finite numerical precision.

### A hidden last direction forces objective loss

If ||x||<=3R and |<u_m,x>|<=gamma/8, then

    F_U(x)>=H_(U,m)(x)>=l_m(x)-lambda
                       >=-a gamma m-lambda
                       =-Delta/16-lambda.

By (18), and lambda/Delta<=1/256,

    F_U(x)-mu_m
        >=[15/32-1/16-1/256]Delta>Delta/4.            (25)

If ||x||>=3R, F_U(x)>=W(x)>0 and (18) gives the same lower bound. Adding the strictly positive tail never weakens it. Thus any output with an unrevealed small last coordinate, or any exterior output, has

    f_U(output)>=Delta/4=2^(-13)m^(-theta).            (26)

## 7. The fixed distribution and its concentration estimate

Draw U uniformly from orthonormal m-frames in R^d, ONCE, before the algorithm starts and independently of its random seed. Everything else in (22) is fixed by beta and m.

For a unit vector v uniformly distributed on the sphere of a D-dimensional subspace and any fixed w,

    Prob{|<v,w>|>t}<=2 exp(-D t^2/(2||w||^2)).         (27)

One elementary proof uses moments. In a unit direction the odd moments vanish and

    E<v,w>^(2l)=||P w||^(2l)(2l-1)!!
                         /[D(D+2)...(D+2l-2)]
                   <=||w||^(2l)(2l-1)!!/D^l.

Hence its moment generating function is at most exp(s^2||w||^2/(2D)); optimize the exponential Markov bound in both signs. This also treats an ambient w with a component outside the subspace.

Conditioned on u_1,...,u_(j-1), every remaining u_i is marginally uniform on the sphere in their orthogonal complement, of dimension d-j+1. Their mutual independence is NOT assumed or required. For a query with norm at most 3R, (27) gives

    Prob{|<u_i,x>|>gamma/8 | prefix}
       <=2 exp(-(d-m)/(294912 m^3)).                 (28)

The query may depend arbitrarily on the revealed prefix and the fixed algorithm seed. The bound is uniform over all such choices.

## 8. Transcript coupling: no seed-adaptive choice of the function

First fix the algorithm's random seed. Construct an auxiliary transcript as follows. At round j, answer every point in its batch using

    (x,z) -> F_(U,j)(x)-mu_m+phi(z).

After round j these answers depend only on u_1,...,u_j. Thus the queries in that round depend only on u_1,...,u_(j-1), which makes (28) applicable. This prefix simulation is an ANALYTICAL coupling device, not the real oracle and not a later change to the sampled true function.

For queries outside 3R the answers equal the true ones automatically. For every other query, impose (24). There are at most BTm<=B m^2 query/direction pairs.

After the last round, the simulated output depends only on u_1,...,u_T. If its x component has norm at most 3R, also impose |<u_m,x_out>|<=gamma/8. The last direction is still uniform conditioned on the entire prefix. This adds one event.

Dimension (4) makes each bad-event bound in (28) at most zeta/(4B m^2), since 2^19>294912. There are at most B m^2+1<=2B m^2 events. A union bound therefore gives total failure probability at most zeta/2, in particular at most zeta. Events need not be independent.

On the good event, induction over rounds and Section 6 show that all auxiliary answers exactly equal the answers of the ORIGINAL fixed function f_U. Therefore the actual and simulated queries and outputs coincide. The output bound (26) holds on that event.

This proves (5) for every fixed seed, uniformly. Integrate over an independent algorithm seed to prove it for randomized algorithms. U was sampled in advance from the same distribution for every algorithm; no query-dependent or seed-dependent rotation was selected. QED, Theorem B.

The proof allows an output that was never queried, arbitrarily large finite queries or tail coordinates, nonlinear processing of the complete exact transcript, and knowledge of all class constants. It does not assume a span restriction or finite precision.

## 9. Matching upper bound and minimax equality

For completeness use the standard accelerated comparator sequence with L=1, x_0=z_0=0,A_0=0:

    a=(1+sqrt(1+4A_k))/2, A'=A_k+a=a^2,
    y=(A_k x_k+a z_k)/A',
    z'=z_k-a grad f(y), x'=(A_k x_k+a z')/A'.

For every finite comparator u,

    A_k[f(x_k)-f(u)]+||z_k-u||^2/2<=||u||^2/2.        (29)

To prove it, write v=grad f(y). Smoothness, a^2=A' and x'-y=(a/A')(z'-z_k) give

    A'f(x')<=A'f(y)+a<v,z'-z_k>+||z'-z_k||^2/2.

Convexity gives A_k f(x_k)+a f(u)>=A'f(y)+a<v,u-z_k>. Finally z'=z_k-av gives the exact square identity for a<v,z'-u>. Combining and telescoping proves (29).

The weight recurrence yields A_T>=(T+1)^2/4. Choose a comparator attaining rho_f(s); then

    f(x_T)<=s+2rho_f(s)^2/(T+1)^2.

For s=(T+1)^(-theta)<=s_beta,

    f(x_T)<=(1+2C_beta^2)(T+1)^(-theta).              (30)

The updates do not know beta, the profile, or the infimum. The constants are used only in this bound. This deterministic algorithm is also an admissible randomized algorithm.

With B=1,zeta=1/4, Theorem B gives for every randomized method an instance with expected gap at least

    (3/4)2^(-13)(T+1)^(-theta)
                   =(3/32768)(T+1)^(-theta).

Together with (30), this proves Theorem A with NO logarithmic loss in T or epsilon. The logarithm appears only in sufficient dimension (4).

For fixed B, the same comparison establishes the identical minimax ROUND exponent: one sequential accelerated query per round attains (30), and allowing B parallel queries per round does not improve the exponent when dimension is large enough as in (4). This is not a no-parallel-speedup claim in a fixed low dimension or for free explicit knowledge of f.

## 10. Fixed confidence and expected stopping times

For a fixed query budget, (5) already gives a probability lower bound, stronger than a lower bound only on expectation. It implies the usual fixed-confidence query exponent in (3).

For a precise stopping-time statement, suppose a randomized algorithm stops after N oracle calls and succeeds with probability at least 1-alpha on EVERY function in the class. Fix T and its hard distribution, and choose an accuracy epsilon<2^(-13)(T+1)^(-theta). Truncate the algorithm after T calls, returning zero if it has not stopped. This is an admissible T-query algorithm. On {N<=T}, its output is the original output. By (5),

    Prob{success and N<=T}<=zeta,
    Prob{N>T}>=1-alpha-zeta.

Hence the average over the fixed hard distribution satisfies

    E N >= T(1-alpha-zeta).

Some fixed instance therefore has expected query count at least that large. Taking alpha=1/3,zeta=1/4 and T a sufficiently small constant times epsilon^(-1/theta) proves an expected stopping-time lower bound Omega_beta(epsilon^(-(beta+1/2))). The constants may depend on beta; no uniform bound as beta tends to zero or infinity is asserted.

## 11. Interpretation, antecedents, and boundaries

The result is a complete randomized strengthening of the specific deterministic minimax theorem in 27, including high-probability and parallel versions. Uniform escape profiles are verified at every accuracy up to the SAME s_beta. The proof is independent of the two-basis normal forms, CP/COP work, cosmic convergence, and proposed higher-order DRS statements.

The construction does not make a classical attained-minimum lower bound disappear by a free choice of a huge near-minimizer. Its core has initial gap below 3Delta and an attained minimizer of radius below 2R, while Delta is proportional to m^(-theta) and R=m^(beta theta). The known scalar tail supplies the uniform lower escape profile; the small initial core gap and bounded core minimizer supply its uniform upper profile at both larger and smaller accuracies. This scale coordination is the substantive connection between the oracle construction and nonattainment.

The lower-bound family depends on the requested horizon, as is standard in minimax oracle complexity. It is not one fixed finite-dimensional function hard at every horizon. Haar frame coefficients need not be rational or have short encodings. The theorem is about black-box values and gradients, not runtime when an explicit formula or hidden frame is supplied. It proves no projection-oracle lower bound, no randomized noisy-gradient complexity law, no higher-order oracle law, and no optimal dimension threshold.

The returned test code uses floating point to illustrate the core and sparse weights. It does not certify a numerical minimum or use a numerical estimate of mu_m as an exact shift. The mathematical normalization is its orientation-independent exact minimum, and the proof only needs the explicit inequalities (18)–(20).

Relevant primary antecedents:

1. B. Woodworth and N. Srebro, Lower Bound for Randomized First Order Convex Optimization, arXiv:1709.03594v2 (2017). Fixed random hard instances, adaptive-query concentration, and the distinction from deterministic resisting rotations. https://arxiv.org/abs/1709.03594
2. J. Diakonikolas and C. Guzman, Lower Bounds for Parallel and Randomized Convex Optimization, JMLR 21(5), 1–31 (2020). Randomized/parallel lower-bound frameworks. https://jmlr.org/papers/v21/19-771.html
3. A. Garg, R. Kothari, P. Netrapalli, S. Sherif, Near-Optimal Lower Bounds for Convex Optimization for All Orders of Smoothness, NeurIPS (2021), arXiv:2112.01118. Smooth locality constructions and broader oracle-complexity antecedents. https://arxiv.org/abs/2112.01118
4. M. Simchowitz, On the Randomized Complexity of Minimizing a Convex Quadratic Function, arXiv:1807.09386v7 (2019). Randomized arbitrary-query smooth-convex lower bounds; not a premise for the present proof. https://arxiv.org/abs/1807.09386
5. M. Blondel, A. F. T. Martins, V. Niculae, Learning Classifiers with Fenchel-Young Losses: Generalized Entropies, Margins, and Algorithms, AISTATS/PMLR 89 (2019). The 3/2-power sparse prediction regularizer is established, not claimed invented here. https://proceedings.mlr.press/v89/blondel19a.html
6. Project manuscripts 26–27 at the parent branch: existing deterministic theorem and comparator energy. The needed upper argument is reproduced in Section 9, and the randomized lower bound does not use their deterministic lower proof.

The exact historical novelty of the normalized nonattainment/parallel synthesis requires scholarly comparison; a targeted literature search is not an exhaustive priority certificate. The work is not represented as a new general randomized lower bound for ordinary smooth convex minimization, which is classical.
