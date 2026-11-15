# Milestone 39 — General escape profiles determine oracle complexity, noise sensitivity, and precision limits

Date: 2026-11-14.
Manuscript III; parent snapshot `5499f4d9be637982be342c2e34b941b677ab4256`.
Branch: `laa-track02-gptpro-analytic-frontier-20261112`.

## Status and interpretation

This proves a functional-profile extension of the power-law result in 38, together with matching stochastic-gradient and systematic-bias bounds. The theorem characterizes, up to constants, sample complexity, parallel round complexity, and the largest tolerable absolute gradient bias. It covers logarithmic and power-law escape, rather than assuming a power at the outset.

The oracle is a noisy GRADIENT oracle. Exact values of the unknown population objective are not supplied. The noiseless sequential/round lower bound remains valid even if exact values and Hessians are supplied. The stochastic lower bound also holds in a stronger sampling model that reveals the entire sampled convex loss, but that statement concerns the stochastic term, NOT the sequential lower bound for that stronger model.

Known accelerated stochastic comparison bounds, information-theoretic testing, and random local-oracle constructions are ingredients, not claimed inventions. The hidden-core construction from 38 is restated and proved with free scale parameters here. No correctness premise is taken from the SDP, cosmic-convergence, copositive, or deterministic lower-bound manuscripts. This proves the specified mathematical statements, not historical priority, a named conjecture resolution, or a journal outcome.

## 1. Admissible profiles and one fixed function class

Let phi:R->(0,infinity) be convex, C2, strictly decreasing, with phi(z)->0 as z->infinity, phi(0)<=1/4, and 0<=phi''<=1/4. Let s0<=1/64 be so small that

    r(s)=phi^(-1)(s)>=1  for 0<s<=s0.

Here r is the inverse on the positive half-line. It is continuous, decreasing, and tends to infinity as s decreases to zero. Assume a fixed doubling constant D>=1 satisfies

    r(s/2)<=D r(s),  0<s<=s0.                           (1)

Set C=D+2. In each finite dimension d, let F_phi(d) be the class of convex C2 functions f:R^d->R satisfying

    Lip(grad f)<=1, f(0)<=1, inf f=0 not attained,
    r(s)<=rho_f(s)<=C r(s),  0<s<=s0,                  (2)
    rho_f(s)=min{||x||:f(x)<=s}.

All constants, the tail phi, and r are fixed BEFORE any query budget or dimension is chosen. The minimum in rho exists: its constraint set is nonempty and closed, and norm minimization is coercive. The class is nonempty: f(x,z)=phi(z) has rho_f=r for s<=s0. The objective has finite values on the whole space; no unknown feasible-set membership oracle is present.

Condition (1) is substantive. It includes all positive regularly varying power profiles and many slower profiles, including logarithmic ones. It does not cover arbitrary functions such as r(s)=exp(1/s). No conclusion at a fixed scaled accuracy is silently extended to profiles lacking (1).

The convention r is known concerns an oracle-complexity model, not an algorithm for extracting an escape profile from arbitrary input. For a fixed accuracy it is enough to know the specified upper comparison radius. No bit-complexity statement for arbitrary real r is asserted.

## 2. Oracle and resources

At a query x, conditional on all previous information, a sample G obeys

    E[G | history]=grad f(x)+b,
    ||b||<=nu,
    E[||G-E[G|history]||^2 | history]<=sigma^2.         (3)

The bias can depend on history and the query. The centered noise is a martingale difference. Within a batch, the same requirements hold conditionally as samples are generated; independence is sufficient but not necessary. Merely bounding marginal variances while permitting an arbitrary common batch noise would NOT suffice for averaging.

Algorithms may randomize, query arbitrary finite points, perform unlimited computation between queries, and return a point never queried. In B-parallel rounds, at most B query points are selected before the round's answers are returned. The dimension is unrestricted in the worst case. The algorithms may know phi, all class constants, sigma, nu, and the exact unattained infimum zero. They do not receive an explicit representation of the unknown f.

N_phi(epsilon;sigma,nu) is the least fixed sample budget that guarantees E f(output)<=epsilon uniformly over dimensions, functions in (2), and oracles (3). T_phi,B is the analogous fixed round budget. Constants in asymptotic comparisons below depend only on the fixed profile data, never on dimension, B, sigma, nu, or epsilon.

## 3. Main theorem: three sharp resource scales

For all sufficiently small epsilon>0 define

    S(epsilon)=r(epsilon)/sqrt(epsilon),
    V(epsilon)=sigma^2 r(epsilon)^2/epsilon^2,
    bcrit(epsilon)=epsilon/r(epsilon).                (4)

### Theorem A

There are positive constants c_b,C_b,c_N,C_N, depending only on the class, such that:

1. If nu<=c_b bcrit(epsilon), then

       N_phi(epsilon;sigma,nu)
          =Theta_phi(S(epsilon)+V(epsilon)),          (5)

   and for every integer B>=1,

       T_phi,B(epsilon;sigma,nu)
          =Theta_phi(S(epsilon)+V(epsilon)/B).        (6)

   One algorithm attains both upper bounds simultaneously.

2. If nu>=C_b bcrit(epsilon), no algorithm can guarantee expected gap epsilon, regardless of its number of samples, rounds, or query magnitudes. This already holds for two explicit two-dimensional functions and a deterministic oracle that is the gradient of one fixed convex surrogate function.

3. The stochastic lower bound in (5) is a two-dimensional statistical lower bound. It holds even if each sample discloses its entire convex smooth loss function, not just a gradient at the chosen point. The sample losses need not be bounded below individually; their population means are the functions in (2). Exact population values are not disclosed.

4. The S lower bound in (5)--(6) uses one fixed random function distribution chosen independently of the algorithm's seed. It holds even if each noiseless query returns f, grad f and Hess f exactly. No Lipschitz-Hessian bound is imposed by the class, and no higher-order oracle conclusion under such an additional modulus is inferred.

The critical bias is specified up to fixed multiplicative constants. This is not an exact universal constant at the transition. The term S is a sequential information barrier; parallelism can divide the variance cost by B but does not divide S in the dimension-uniform model.

The following sections prove all assertions.

## 4. Upper bound: accelerated comparison with variance and bias

Fix an accuracy epsilon with epsilon/4<=s0, and put

    R=C r(epsilon/4), Q={x:||x||<=R}.

There is a deterministic comparator u in Q with f(u)<=epsilon/4. Initialize x_0=z_0=0,A_0=0. Choose K outer iterations, each using a batch of M oracle samples. For j=0,...,K-1, set

    a=(1+sqrt(1+8A_j))/4,
    A'=A_j+a=2a^2,
    y=(A_j x_j+a z_j)/A',
    Gbar=average of M fresh samples at y,
    z'=Proj_Q(z_j-a Gbar),
    x'=(A_j x_j+a z')/A'.                            (7)

Both x_j and z_j remain in Q. Projection onto this declared Euclidean ball is an elementary computation, not an oracle for the unknown function or a hidden cone.

Write the averaged error as Gbar-grad f(y)=bbar+xi. Conditional sample centering and the variance bound imply

    ||bbar||<=nu,
    E[xi | outer history]=0,
    E||xi||^2<=sigma^2/M.                             (8)

The average bbar may itself be random. This does not matter for its norm bound. Cross terms between distinct centered sample errors vanish by conditional expectation, justifying the variance reduction even for the stated martingale model.

### Exact one-step energy inequality

Let d=z'-z_j. Smoothness, x'-y=(a/A')d, and A'=2a^2 give

    A'f(x')<=A'f(y)+a<grad f(y),d>+||d||^2/4.

Convexity gives

    A_j f(x_j)+a f(u)>=A'f(y)+a<grad f(y),u-z_j>.

Projection optimality yields

    a<Gbar,z'-u>
       <= (||z_j-u||^2-||z'-u||^2-||d||^2)/2.

Combining them, bounding the bias using ||z'-u||<=2R, and using

    -a<xi,d><=||d||^2/4+a^2||xi||^2,

gives

    A'[f(x')-f(u)]+||z'-u||^2/2
      <= A_j[f(x_j)-f(u)]+||z_j-u||^2/2
            +2aRnu+a^2||xi||^2-a<xi,z_j-u>.           (9)

After expectation and telescoping,

    E f(x_K)<=f(u)+R^2/(2A_K)
                    +(sigma^2/(M A_K)) sum_(j=1)^K a_j^2
                    +2Rnu.

The weights obey A_K>=(K+1)^2/8 and a_j^2=A_j/2<=A_K/2. Therefore

    E f(x_K)<= f(u)+4R^2/(K+1)^2
                         +sigma^2 K/(2M)+2Rnu.        (10)

The proof does not use or estimate f_* in an update and does not presume a minimizer.

### Parameter choices and simultaneous sample/round budgets

Choose

    K=ceil(4R/sqrt(epsilon)),
    M=max(1,ceil(2 sigma^2 K/epsilon)).                (11)

If nu<=epsilon/(8R), the four terms in (10) are each at most epsilon/4. Thus E f(x_K)<=epsilon.

Since R<=C D^2 r(epsilon), a sufficient bias condition is

    nu<=epsilon/[8 C D^2 r(epsilon)].                 (12)

The total sample count is

    KM<=K+2sigma^2 K^2/epsilon
       <=5R/sqrt(epsilon)+50sigma^2 R^2/epsilon^2.    (13)

A batch of M samples can be collected in ceil(M/B) rounds, repeating the SAME query while that batch is collected. The outer sequence is updated only after the batch is complete. The total rounds are at most

    K ceil(M/B)<=K+KM/B
        <=10R/sqrt(epsilon)+50sigma^2 R^2/(B epsilon^2). (14)

These are the upper halves of (5)--(6). This simple batching proof is not a new acceleration algorithm; its purpose is to retain exact dependence on the escape radius and absolute bias.

## 5. A scale-free local-oracle hard core

This section supplies the noiseless sequential obstruction used in Theorem A. It re-proves the core from 38 without linking its scales to a power law.

Fix m>=2,R>0 and an orthonormal m-frame U=(u_1,...,u_m) in R^d. Set

    gamma=R/(16m^(3/2)), a=gamma/128,
    lambda=16a^2, e=64a^2,
    Delta=aR/sqrt(m)=R^2/(2048m^2).                   (15)

For a score vector l define

    S_lambda(l)=max_{w>=0, sum w_i=1}
                  [sum_i w_i l_i-lambda sum_i w_i^(3/2)]. (16)

The unique maximizer satisfies

    w_i=[(l_i-eta)_+/(3lambda/2)]^2,
    sum_i(l_i-eta)_+^2=(3lambda/2)^2.                 (17)

The left-hand equation defining eta is C1 with strictly negative eta derivative. Hence eta and every w_i are C1, and S_lambda is C2 with gradient w. Strong convexity of lambda sum w_i^(3/2), whose scalar second derivative is at least 3lambda/4 on (0,1], gives

    Lip(grad S_lambda)<=4/(3lambda),
    max l_i-lambda<=S_lambda(l)<=max l_i.              (18)

Moreover eta>=max l_i-3lambda/2. Every coordinate more than 3lambda/2 below the maximum is identically inactive on any neighborhood preserving that strict gap. Appending inactive scores changes the value AND all derivatives through order two exactly.

Use the even C2 convex smoothing

    psi_e(t)=|t| if |t|>=e,
    psi_e(t)=3e/8+3t^2/(4e)-t^4/(8e^3) otherwise,
    M_e(a,b)=[a+b+psi_e(a-b)]/2.

It obeys |psi'_e|<=1, 0<=psi''_e<=3/(2e),

    max(a,b)<=M_e(a,b)<=max(a,b)+3e/16,

and equals max(a,b) where |a-b|>=e. Its partial derivatives are nonnegative. Thus composing it with convex functions preserves convexity.

Define

    l_i(x)=a[<u_i,x>-(i-1)gamma],
    H_(U,j)=S_lambda(l_1,...,l_j),
    W(x)=2a[sqrt(||x||^2+(R/4)^2)-R],
    F_(U,j)=M_e(H_(U,j),W), F_U=F_(U,m).             (19)

All these functions are globally C2 and semialgebraic. Since the score map has operator norm a,

    ||grad H_(U,j)||<=a, 0<=Hess H_(U,j)<=I/12,
    ||grad W||<=2a, 0<=Hess W<=I/256.

The Hessian chain rule for M_e gives

    Hess F=omega Hess H+(1-omega)Hess W
                +(psi''_e(H-W)/2)(grad H-grad W)(...)^T,

with omega in [0,1]. Therefore

    0<=Hess F_(U,j)<=(1/12+27/256)I=(145/768)I<I/4. (20)

The core is coercive. Let mu_m,R=min F_U. Its value does not depend on the orientation U: rotate one frame into another, and observe that W is radial. It also does not depend on the ambient dimension, since projecting onto span U cannot increase F_U.

The estimates needed are

    -(5/2)Delta<=mu_m,R<=-(15/32)Delta,
    0<=F_U(0)-mu_m,R<3Delta,
    every minimizer has norm <2R.                     (21)

For ||x||<=2R, average the scores to get

    max l_i>=-a||x||/sqrt(m)-a gamma(m-1)/2
               >=-2Delta-Delta/32.

Subtracting lambda, with lambda/Delta=1/(128m)<=1/256, proves the lower bound. Outside 2R, W>2aR>0. At xbar=-(R/(2sqrt(m)))sum_i u_i, the score maximum is -Delta/2 and W<=-Delta/2. Thus F_U(xbar)<=-Delta/2+12a^2<=-15Delta/32. At zero F_U(0)<=12a^2<=Delta/32. These establish (21).

### Locality, including arbitrarily large queries

If ||x||>=3R, then W-H_(U,j)>=a(||x||-2R)>=aR>e. Thus F_(U,j)=W on a neighborhood, for every j. No hidden-frame information is present at such a query.

If ||x||<=3R and |<u_i,x>|<=gamma/8 for all i>=j, then for every i>j,

    l_j(x)-l_i(x)>=3a gamma/4.

On the ball of radius gamma/8 about x this gap is at least a gamma/2. But 3lambda/2=(24/128)a gamma<a gamma/2. All scores after j are inactive in (17), so F_U=F_(U,j) on that neighborhood. In particular the exact value, gradient and Hessian agree.

Finally, if ||x||<=3R and |<u_m,x>|<=gamma/8, then

    F_U(x)-mu_m,R>=Delta/4.                            (22)

Indeed F_U>=l_m-lambda>=-Delta/16-lambda, whereas mu_m,R<=-15Delta/32. Outside 3R the same lower bound follows from W>0.

### Fixed random frame and adaptive transcripts

Draw U from Haar measure before the algorithm starts. In an auxiliary transcript, round j is answered by F_(U,j)-mu_m,R plus the known scalar tail. The shift is the SAME full-core minimum at every round, not the minimum of the prefix core. It carries no orientation information. The j-th batch of queries depends only on the previous prefix and the algorithm's seed.

For any such query of norm at most 3R, conditioned on the previous prefix, a future u_i is marginally uniform in a subspace of dimension at least d-m. A spherical-moment bound gives

    Prob{|<u_i,x>|>gamma/8 | prefix}
       <=2 exp(-(d-m)/(294912m^3)).                   (23)

For clarity, E<v,x>^(2l)<=||x||^(2l)(2l-1)!!/(d-m)^l for a uniform unit vector v in that subspace. Its moment generating function is at most exp(t^2||x||^2/[2(d-m)]), giving (23) by exponential Markov in both signs.

There are at most Bm^2 query/direction events and one output event. The output is conditioned on the first m-1 frame vectors, leaving u_m uniform. If

    d>=m+ceil(2^19 m^3 log(8Bm^2/zeta)),               (24)

a union bound gives simultaneous success probability at least 1-zeta. Queries outside 3R need no event. On success, prefix locality proves inductively that every answer is exactly the true fixed-function answer; the actual and auxiliary outputs coincide. Equation (22) applies to the output.

The argument holds for every fixed seed, with a common frame distribution. Integrating over a seed independent of U therefore proves a randomized lower bound, not a seed-dependent resisting oracle. It also covers any output not queried earlier. Adding the positive known tail cannot weaken (22).

## 6. The sequential lower bound for a general profile

Choose epsilon small enough that 256epsilon<=s0 and epsilon<=2^-20. Set

    R=r(256epsilon),
    m=floor(R/[128sqrt(epsilon)]).

Then m>=2 and, with Delta from (15),

    8epsilon<=Delta<=32epsilon,
    6Delta<=192epsilon<256epsilon.                   (25)

Define

    f_U(x,z)=F_U(x)-mu_m,R+phi(z).                    (26)

Its Hessian is block diagonal, with both blocks bounded by I/4; its infimum zero is unattained. Also f_U(0,0)<3Delta+1/4<=1 for the declared small accuracies.

If f_U(x,z)<=s<=s0, then z>=r(s), proving the lower profile bound. For the upper bound set z=r(s/2)<=D r(s). If s>=6Delta, x=0 has core gap <=s/2. If s<6Delta, choose a core minimizer; it has norm <2R, and (25) plus monotonicity gives R<=r(s). Thus

    rho_fU(s)<=sqrt(D^2+4)r(s)<=(D+2)r(s).

This holds for EVERY s<=s0, not only s near the testing accuracy. Hence all f_U belong to one fixed class (2).

With T=m-1 rounds and zeta=1/4, Sections 5 and (25) give output gap at least 2epsilon with probability at least 3/4. Its expected gap is therefore at least 3epsilon/2. So no uniform epsilon guarantee is possible within this budget.

By iterating (1) eight times,

    r(256epsilon)>=D^-8 r(epsilon).

Also m>=R/[256sqrt(epsilon)]. This proves the lower bound Omega_phi(S(epsilon)) for rounds with any finite B; for sequential queries take B=1. Exact values and Hessians in the replies do not affect the proof because the prefix functions agree on a neighborhood.

The sufficient lower-bound dimension is O(m^3 log(Bm)); it is not fixed independently of the horizon or B. The profiles, in contrast, ARE fixed independently of those quantities.

## 7. A two-dimensional statistical lower bound

Put kappa=2sqrt(3)-3, so 0<kappa<1/2. For 0<delta<=min(s0,1/8), let R_delta=r(delta) and a_delta=delta/R_delta. For theta in {-1,+1}, define

    h_theta(x)=delta[2sqrt((x/R_delta)^2+3)
                          -theta x/R_delta-3],
    f_theta(x,z)=h_theta(x)+phi(z).                   (27)

The core is nonnegative, with unique minimum zero at x=theta R_delta. Its value at zero is kappa delta and

    h_theta''(x)=6delta/[R_delta^2((x/R_delta)^2+3)^(3/2)]
                 <=2delta/(sqrt(3)R_delta^2)<1/4.

Thus the population functions are convex C2 and 1-smooth, with f_theta(0,0)<=1, known infimum zero not attained.

They belong to (2). The tail gives rho>=r. For an upper bound choose z=r(s/2)<=D r(s). If s>=2kappa delta, take x=0. Otherwise s<delta, so R_delta<=r(s), and x=theta R_delta gives zero core. The radius is at most sqrt(1+D^2)r(s)<=C r(s).

Returning a point on the wrong side of zero costs at least kappa delta:

    theta x<=0 => h_theta(x)>=kappa delta.            (28)

### A sampling problem even stronger than a gradient oracle

Let Z be a scalar Gaussian with mean theta a_delta and variance sigma^2. A sampled loss is

    L_Z(x,z)=delta[2sqrt((x/R_delta)^2+3)-3]
                         -Z x+phi(z).                (29)

Every sampled loss is convex C2 and globally smooth, since its random part is affine. Its expectation is f_theta. Its gradient has conditional variance exactly sigma^2 in its first coordinate. Individual sample losses may be unbounded below; no nonnegativity or attained-minimum assumption on each sample is part of this oracle class.

Grant the algorithm the entire function L_Z, equivalently the scalar Z, on each sample. This is more information than the allowed gradient oracle. Arbitrary queries cannot improve on observing Z directly. After N samples, the two experiments are the Gaussian product distributions with means +/-a_delta. Their Kullback--Leibler divergence is

    KL(P_+^N || P_-^N)=2N a_delta^2/sigma^2.           (30)

Internal randomization independent of theta contributes no information. Data processing applies to every adaptive transcript and output. If

    N<=sigma^2 R_delta^2/(16delta^2),                 (31)

Pinsker gives total variation at most 1/4. The average error in deciding the sign theta is therefore at least 3/8. Infer the sign from the first output coordinate, breaking zero arbitrarily. By (28), every algorithm has average expected objective at least

    (3/8)kappa delta.                                (32)

Take delta=16epsilon. Then (32)=6kappa epsilon>epsilon. Doubling gives r(16epsilon)>=D^-4 r(epsilon). Consequently any epsilon-guaranteeing algorithm needs

    N=Omega_phi(sigma^2 r(epsilon)^2/epsilon^2).       (33)

If the numerical bound in (31) is less than one, the claimed scale is bounded and the sequential lower bound already dominates. For sigma=0 there is no stochastic term.

For B-parallel rounds, at most BT samples are available, so (33) becomes a lower bound Omega_phi(V(epsilon)/B) on the number of rounds. Combining it with Section 6 proves (5)--(6), since max of two nonnegative quantities is at least half their sum.

### Exact confidence interpretation for the hard pair

The best average sign error for the N-sample Gaussian pair is exactly

    Phi(-a_delta sqrt(N)/sigma),                     (34)

where Phi is the standard normal distribution function. Thus any guarantee of objective gap less than kappa delta with probability at least 1-alpha for BOTH signs requires

    N >= (sigma^2 R_delta^2/delta^2)
                              [Phi^(-1)(1-alpha)]^2. (35)

This gives the usual logarithmic high-confidence statistical cost as alpha tends to zero. The main theorem matches EXPECTED-error complexity; no matching all-term high-confidence upper bound under only conditional second moments is being asserted here.

## 8. The systematic-bias lower bound needs no randomness

Use the same pair (27), and define the fixed convex surrogate

    f_0(x,z)=(f_+(x,z)+f_-(x,z))/2.

Their gradients differ only by their constant first-coordinate terms. Therefore

    ||grad f_0-grad f_theta||=a_delta                  (36)

at every point. The oracle G=grad f_0 is a deterministic admissible oracle for either population objective whenever nu>=a_delta. The entire transcript is then IDENTICAL for both signs, at every query magnitude and for any number of calls.

For every output point,

    (f_+(x,z)+f_-(x,z))/2
       =delta[2sqrt((x/R_delta)^2+3)-3]+phi(z)
       >=kappa delta.                                (37)

Hence at least one true objective has expected gap at least kappa delta, even for an algorithm using unlimited information from the surrogate. Knowledge of the exact true infimum zero or of the common initial value does not identify the sign.

Take delta=8epsilon. Then kappa delta>epsilon. Since r(8epsilon)>=D^-3 r(epsilon), the sufficient bias condition is

    nu>=8D^3 epsilon/r(epsilon).                     (38)

Equations (12) and (38) establish the sharp ORDER of the critical bias in Theorem A. This is an indistinguishability theorem, not just a bias term in the analysis of one method. It remains true when the erroneous vector field itself is the gradient of a globally convex smooth surrogate.

This does not claim that every physical rounding error is adversarial or necessarily reaches this worst case. It identifies the accuracy that can be guaranteed from the oracle specification alone.

## 9. Power-law and logarithmic consequences

### 9.1 Power-law escape

For beta>0 let p=1/beta, b=min(1/4,1/[4p(p+1)]), and use

    phi(z)=b(1+z)^(-p), z>=0,
    phi(z)=b[1-pz+p(p+1)z^2/2], z<0.

This is convex C2 with 0<=phi''<=1/4. On a suitable fixed interval,

    r(s)=(b/s)^beta-1=Theta_beta(s^-beta),
    r(s/2)<=2^(beta+1)r(s).

Theorem A yields

    optimal samples
      =Theta_beta(epsilon^(-beta-1/2)
                       +sigma^2 epsilon^(-2beta-2)),  (39)
    optimal B-parallel rounds
      =Theta_beta(epsilon^(-beta-1/2)
                    +(sigma^2/B)epsilon^(-2beta-2)), (40)
    critical absolute gradient bias
      =Theta_beta(epsilon^(beta+1)).                 (41)

The constructions also fit the original constants in 38 when its particular power tail is used: lower radius is at least b^beta s^-beta/2; for the upper witnesses, r(s/2)<=(2b)^beta s^-beta<=s^-beta and core radius at most 2b^beta s^-beta, so the previously declared C_beta remains sufficient. The upper proof needs only that original radius bound. Thus (39)--(41) hold on that original normalized power class as well, not only on an arbitrarily enlarged class.

Equivalently, for T rounds of B queries, in the dimension-uniform model the expected-error minimax law is, up to beta-dependent constants,

    min{1,
         T^(-2/(2beta+1))
          +(sigma^2/(BT))^(1/(2beta+2))
          +nu^(1/(beta+1))}.                         (42)

To justify (42), choose a sufficiently large constant multiple of the displayed sum as the target epsilon in (11)--(14). The sequential and variance round costs are at most T, and (12) holds. If the sum is not small, output zero, whose gap is at most one; this changes only a class-dependent constant. Conversely apply the three lower constructions at a sufficiently small fixed multiple of each corresponding error scale, truncating the constructed delta at a small class-dependent constant when necessary. The largest lower scale is at least one third of the sum, up to saturation. Constants and the small-accuracy threshold depend on beta, not on sigma,nu,B or T.

Fixed nonzero bias therefore creates the unavoidable population-error floor Theta_beta(nu^(1/(beta+1))). Averaging suppresses the variance term, not this floor.

### 9.2 Logarithmic escape

Let b=1/4 and

    phi(z)=b exp(-z), z>=0,
    phi(z)=b(1-z+z^2/2), z<0.

It meets the same C2 convex smoothness requirements. For small s,

    r(s)=log(b/s)=Theta(log(1/s)),
    r(s/2)<=2r(s).

Thus

    optimal samples =Theta(epsilon^-1/2 log(1/epsilon)
                     +sigma^2 epsilon^-2 log^2(1/epsilon)),
    optimal rounds =Theta(epsilon^-1/2 log(1/epsilon)
                  +(sigma^2/B)epsilon^-2 log^2(1/epsilon)),
    critical bias =Theta(epsilon/log(1/epsilon)).      (43)

The bias floor has order nu log(1/nu) as nu decreases to zero. More precisely, inverting nu=epsilon/log(b/epsilon) uses epsilon=nu W(b/nu), with W the positive Lambert W function; the theorem concerns orders, not the exact transition coefficient.

The statement is about the declared class of convex objectives with logarithmic escape. It does NOT assert a matching lower bound for every individual logistic-regression problem or for a specific statistical model. The functions in this example are not semialgebraic, so this consequence genuinely goes beyond the positive-power semialgebraic regime.

### 9.3 Useful parallelism and gradient-accuracy bits

From (6), the order of the batch size beyond which additional parallelism no longer improves the minimax round order is

    Bcrit(epsilon)=sigma^2 r(epsilon)/epsilon^(3/2).   (44)

When this number is below one, the sequential term already dominates at B=1. Otherwise, the variance term dominates below this scale and the sequential term dominates above it. This is an asymptotic worst-case crossover, not a hardware-runtime model.

If an implementation guarantees an absolute VECTOR-bias norm at most 2^(-b), the critical number of accuracy bits is

    bcrit_accuracy(epsilon)=log_2(r(epsilon)/epsilon)+O_phi(1).

For power escape this is (beta+1)log_2(1/epsilon)+O_beta(1). For logarithmic escape it is log_2(1/epsilon)+log_2 log(1/epsilon)+O(1). The statement counts a declared vector-error budget, not per-coordinate floating-point mantissa bits or a model of every rounding implementation. The necessity comes from the indistinguishable pair, and sufficiency from (12).

## 10. A precise geometric application, with its boundary stated

Let U be a known affine subspace and K a closed convex cone, disjoint at zero distance, and minimize

    f(u)=dist(u,K)^2/2 over u in U.

In orthonormal coordinates on U, its gradient is the tangential projection of u-Proj_K(u), and is 1-Lipschitz. If its feasibility radius satisfies R_feas(delta)=Theta(delta^-a), its objective-radius profile is Theta(s^-a/2). The U-coordinate version of the upper energy proof needs no other change; the comparison ball is taken inside U.

If a possibly randomized approximate cone-projection routine supplies a tangential gradient with conditional variance sigma^2 and bias norm at most nu, then expected squared feasibility error at most delta^2 is guaranteed using

    O(delta^(-(a+1))+sigma^2 delta^(-(2a+4))) samples,
    O(delta^(-(a+1))+(sigma^2/B)delta^(-(2a+4))) rounds,

provided nu<=c delta^(a+2), with fixed-instance constants and a suitable known radius upper bound.

These are UPPER bounds for the specified approximate-projection interface. The general smooth-objective lower construction is not automatically a cone-projection lower bound. Nor is an arbitrary noisy matrix claimed to give an unbiased projection estimate. This application explains how oracle accuracy must scale in weakly infeasible systems without conflating an information model with a particular floating-point implementation.

## 11. What changes in Manuscript III and what does not

The organizing quantity is now a full near-optimal-radius function, not merely one exponent. It controls three different resources simultaneously:

    sequential information: r(epsilon)/sqrt(epsilon),
    stochastic samples: sigma^2 r(epsilon)^2/epsilon^2,
    admissible systematic error: epsilon/r(epsilon).

The classwise conclusions are matching upper/lower bounds. They do not say that every individual function with the profile is equally hard. The statistical and precision lower bounds already hold in dimension two, whereas the sequential randomized/parallel lower bound uses a growing dimension. The noisy oracle does not provide exact true values. The hard statistical samples are convex smooth losses but may be individually unbounded below. None of these model distinctions may be omitted in a submission.

No polynomial-bit SDP solver, randomized lower bound for supplied conic matrices, or finite stopping certificate for weak infeasibility has been obtained. We also do not claim a new general theory of stochastic acceleration, biased oracles, or Gaussian testing; those are established. The result supplied here is the uniform nonattainment profile classification with matching constructions and the stated parallel/precision consequences. An independent novelty comparison remains a separate scholarly task.

## Primary antecedents

1. G. Lan, An optimal method for stochastic composite optimization, Mathematical Programming 133 (2012), 365--397. DOI 10.1007/s10107-010-0434-y. Earlier author manuscript: https://optimization-online.org/2008/08/2061/ . Accelerated stochastic upper bounds are established; Section 4 proves the particular comparator version used here.
2. A. Agarwal, P. L. Bartlett, P. Ravikumar, M. J. Wainwright, Information-theoretic lower bounds on the oracle complexity of stochastic convex optimization, IEEE Transactions on Information Theory 58 (2012), 3235--3249. https://arxiv.org/abs/1009.0571 . Statistical testing is a classical lower-bound tool.
3. O. Devolder, F. Glineur, Y. Nesterov, First-order methods of smooth convex optimization with inexact oracle, Mathematical Programming 146 (2014), 37--75. https://optimization-online.org/2010/12/2865/ . Their inexact-function-model oracle should not be conflated with the absolute conditional gradient-bias model (3).
4. B. Woodworth, N. Srebro, Lower Bound for Randomized First Order Convex Optimization, arXiv:1709.03594. https://arxiv.org/abs/1709.03594 . Fixed random instances and adaptive local-oracle lower bounds.
5. J. Diakonikolas, C. Guzman, Lower Bounds for Parallel and Randomized Convex Optimization, JMLR 21(5) (2020), 1--31. https://jmlr.org/papers/v21/19-771.html . Parallel local-oracle antecedents.
6. M. Blondel, A. F. T. Martins, V. Niculae, Learning Classifiers with Fenchel--Young Losses: Generalized Entropies, Margins, and Algorithms, AISTATS/PMLR 89 (2019). https://proceedings.mlr.press/v89/blondel19a.html . The 3/2-power sparse simplex regularizer is not invented here.
7. Project manuscript 38 at parent snapshot stated above supplies the prior power-class core. Sections 5--6 reproduce the facts used and extend the scaling to general r; the noise and bias lower bounds are independent of it.
