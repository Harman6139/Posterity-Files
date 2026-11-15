# Milestone 27 — sharp deterministic first-order oracle complexity without minimizers

Date: 2026-11-13. Parent research snapshot: 415ac86b4a6031e73e37a320f305fb20a921bdce.
Branch: laa-track02-gptpro-analytic-frontier-20261112.

## Status, model, and attribution

This proves a matching worst-case oracle lower bound for the accelerated upper exponent in 26. The lower bound applies to arbitrary deterministic adaptive first-order methods, not just linear-span or zero-respecting methods. The output need not be a queried point. Queries and computation between oracle calls are unrestricted. The oracle supplies exact values and full gradients. The dimension is allowed to grow with the query horizon, as stated explicitly below.

The upper energy estimate, zero-chain method and resisting orthogonal-basis construction are classical first-order-complexity techniques. They are not new algorithm inventions. The particular result proved here uses a dyadically weighted quadratic chain to realize a prescribed escape exponent uniformly across dimensions and accuracy scales, and a smooth nonattained scalar tail. No historical-priority claim, named-conjecture resolution, randomized lower bound, or editorial acceptance claim is made. The proof is independent of the earlier SDP representation and geometric counting results. The upper-bound proof is included rather than assumed from 26.

The theorem is about first-order BLACK-BOX information, not explicit-input computation. A formula exposing the hidden quadratic matrix is additional information and falls outside this oracle lower bound. Second derivatives, proximal oracles, and arbitrary exact optimization subroutines are also different oracles.

## 1. Uniform escape classes

Fix beta>0. For a smooth convex f on R^d with finite unattained infimum f_*, define, at x_0=0,

    rho_f(s)=min{||x||_2:f(x)-f_*<=s}, s>0.

The minimum exists by closedness and boundedness of a minimizing sequence. Nonattainment implies rho_f(s)->infinity as s decreases to zero.

There exist constants 0<c_beta<C_beta<infinity and s_beta>0, depending ONLY on beta, for which the following class is nonempty in arbitrarily high dimensions:

    F_beta(d) = {f:R^d->R : f convex C^2,
                 ||grad f(x)-grad f(y)||<=||x-y||,
                 f_*=0 is not attained, f(0)<=1,
                 c_beta s^(-beta)<=rho_f(s)<=C_beta s^(-beta)
                                  for ALL 0<s<=s_beta}.

Fix the explicit constants supplied in Section 4, or larger upper/smaller lower constants. They are uniform over the functions used in the lower bound, their dimensions, and the query budget. Giving the algorithm beta, these constants, the smoothness bound, and the exact infimum zero does not change the lower bound.

Let E_T be the infimum over deterministic algorithm families (one algorithm for each input dimension) of the supremum, over all d and f in F_beta(d), of the gap at the returned point after at most T first-order oracle calls. The output must be finite. The algorithm can otherwise use arbitrary adaptive queries and unlimited computation.

## Theorem A — exact minimax exponent

For all sufficiently large integers T,

    c'_beta (T+1)^(-2/(2beta+1))
        <= E_T <= C'_beta (T+1)^(-2/(2beta+1)).           (1)

Equivalently, the deterministic dimension-uniform oracle complexity of reaching gap epsilon is

    Theta_beta(epsilon^(-(beta+1/2))).                  (2)

The lower-bound instance can be chosen in dimension 2T+3. For rational beta, every constructed instance is semialgebraic. Before an adversarial orthogonal rotation, its quadratic core has rational coefficients from a fixed finite bounded set. The rotation may have arbitrary real entries; rational coefficient-height bounds for that rotation are NOT asserted.

The accelerated method achieving the upper bound does not use beta or f_* in its updates. Knowledge of class constants is only needed to turn a budget into a guaranteed stopping accuracy.

This is not an assertion that any single fixed-dimensional instance defeats every method at every horizon. In particular, a fixed quadratic matrix can be recovered from finitely many sufficiently informative gradient queries. The quantifiers are: FOR EACH deterministic algorithm and finite horizon T, THERE EXISTS one consistent function in dimension 2T+3 giving the stated lower bound. All answers in that transcript come from that one final function.

## 2. Upper bound without assuming a minimizer exists

Use the accelerated sequence from 26 with L=1 and Q=R^d. Initialize x_0=z_0=0 and A_0=0. For k>=0,

    a=(1+sqrt(1+4A_k))/2, A_{k+1}=A_k+a=a^2,
    y=(A_k x_k+a z_k)/A_{k+1},
    z_{k+1}=z_k-a grad f(y),
    x_{k+1}=(A_k x_k+a z_{k+1})/A_{k+1}.

For every finite comparator u and every k,

    A_k(f(x_k)-f(u)) + ||z_k-u||^2/2 <= ||u||^2/2.     (3)

Proof: put v=grad f(y), x'=x_{k+1}, z'=z_{k+1}, A'=A_k+a. Smoothness and a^2=A' give

    A'f(x') <= A'f(y)+a<v,z'-z_k>+||z'-z_k||^2/2.

Convexity and A'y=A_k x_k+a z_k give

    A_k f(x_k)+a f(u) >= A'f(y)+a<v,u-z_k>.

The update z'=z_k-a v implies

    a<v,z'-u> = (||z_k-u||^2-||z'-u||^2-||z'-z_k||^2)/2.

Combining and telescoping proves (3). No exact minimizer was used.

The recurrence gives A_k>=(k+1)^2/4 for k>=1. Choose u with f(u)<=s and ||u||=rho_f(s). Dropping the nonnegative norm in (3) gives

    f(x_k) <= s+2 rho_f(s)^2/(k+1)^2.

Let theta=2/(2beta+1) and s=(k+1)^(-theta). For all sufficiently large k (a threshold depending only on s_beta),

    f(x_k) <= (1+2 C_beta^2)(k+1)^(-theta).

This proves the upper bound in (1), uniformly over dimension and function.

## 3. A weighted quadratic chain with a tunable escape scale

Set

    theta=2/(2beta+1) in (0,2),
    nu=2-theta=4beta/(2beta+1),
    t=(1-theta)/2=(2beta-1)/(2(2beta+1)),
    c0=1/64.

Thus -1/2<t<1/2 and nu/(2theta)=beta. For i>=1 set

    sigma_i=2^(floor(t log_2 i)), q_i=sigma_i/sigma_(i+1).

These are positive rational dyadic numbers, even when t is not rational. They satisfy

    (1/2)i^t < sigma_i <= i^t,
    q_i in {1/2,1,2}, sigma_1=1.                       (4)

The ratio assertion follows because |t log_2((i+1)/i)|<1/2; successive floors differ by at most one. For fixed rational beta, the floors can be computed by exact integer comparisons, without floating-point logarithms.

For N>=2 define

    h_N(x)=c0[(x_1-1)^2+
                   sum_(i=1)^(N-1)(x_i-q_i x_(i+1))^2].       (5)

This is a nonnegative convex quadratic. Its unique zero is sigma=(sigma_1,...,sigma_N).

Its gradient has Lipschitz constant at most 20 c0=5/16. Indeed, the squared norm of the difference operator x_i-q_i x_(i+1) is at most 9||x||^2, since q_i<=2. Adding x_1^2 raises this to at most 10||x||^2; the Hessian has the extra factor 2c0. In particular all final examples are 1-smooth independently of N.

The zero-chain property is exact: if x is supported on coordinates 1,...,k, then grad h_N(x) is supported on 1,...,k+1. Function values at such x and these gradient coordinates are unchanged by any choice of basis directions beyond k+1.

### Lemma 1 — exact prefix minimum

For 0<=k<N, set

    R_k=1+sum_(i=1)^k sigma_i^(-2).

Then

    min{h_N(x):x_(k+1)=...=x_N=0}=c0/R_k.              (6)

For k>=1 the unique minimizer on that prefix has

    x_i=sigma_i [sum_(j=i)^k sigma_j^(-2)]/R_k, i<=k;
    x_i=0, i>k.                                       (7)

Proof: write y_i=x_i/sigma_i, y_0=1, y_(k+1)=0. The energy divided by c0 is

    (y_0-y_1)^2+sum_(i=1)^k sigma_i^2(y_i-y_(i+1))^2.

The drops sum to one. Weighted Cauchy-Schwarz gives energy>=1/R_k, with equality precisely when the drops are proportional to the resistances 1,sigma_1^(-2),...,sigma_k^(-2). This yields (7). The k=0 case is h_N(0)=c0. QED.

### Lemma 2 — uniform estimates

For k>=1,

    R_k >= (1/4) k^theta,
    R_k <= (1+4/theta)(k+1)^theta,                     (8)
    sum_(i=1)^k sigma_i^2 <= (k+1)^nu/nu.              (9)

Proof: (4) makes sigma_i^(-2) lie between i^(theta-1) and 4 i^(theta-1), and sigma_i^2<=i^(nu-1). For any alpha>0, sum_(i=1)^k i^(alpha-1)<=(k+1)^alpha/alpha, by integrating over [0,k] when alpha<=1 and over [1,k+1] otherwise. This proves both upper bounds. For the lower bound, the last at least k/2 terms give at least 2^(-max(1,theta))k^theta>=(1/4)k^theta, since theta<2. QED.

The prefix point (7) has |x_i|<=sigma_i, so its radius is at most (k+1)^(nu/2)/sqrt(nu). Its gap is O(k^(-theta)). Thus its radius-versus-gap exponent is nu/(2theta)=beta. The weights tune this relation without making the smoothness constant grow.

## 4. Enforcing genuine nonattainment, with dimension-uniform profiles

Put p=1/beta and

    A=min(1/4, 1/[4p(p+1)]).

Define a globally C^2 convex, strictly positive scalar function

    phi(z)= A(1+z)^(-p)                          for z>=0,
    phi(z)= A[1-pz+p(p+1)z^2/2]                 for z<0.   (10)

The value, first derivative and second derivative match at zero. Everywhere 0<=phi''<=1/4. The function is strictly decreasing, tends to zero at +infinity, and tends to +infinity at -infinity. For rational beta it is semialgebraic. Its epigraph on the positive half-line is a rational-power epigraph, but no conic-representation oracle is assumed.

Define, on ALL of R^(N+1),

    f_N(x,z)=h_N(x)+phi(z).                            (11)

It is convex C^2, globally 1-smooth, f_N(0)=c0+A<=1, and its infimum is zero but is never attained. Taking x=sigma and z->infinity proves the value of the infimum.

Here are explicit common profile constants:

    c_beta=A^beta/2,
    C_beta=1+3/sqrt(nu),
    s_beta=min(c0,A*2^(-1/beta)).                      (12)

For EVERY N>=2 and EVERY 0<s<=s_beta,

    c_beta s^(-beta)<=rho_fN(s)<=C_beta s^(-beta).      (13)

Lower bound: f_N(x,z)<=s<A implies z>=0 and (1+z)>=(A/s)^beta. Since s<=A 2^(-1/beta), z>=A^beta s^(-beta)/2. This lower-bounds the full norm.

Upper bound: set z=(2A/s)^beta-1>=0, so phi(z)=s/2 and z<=(2A)^beta s^(-beta)<=s^(-beta). Let

    k=ceil((8c0/s)^(1/theta)).

If k<N use the prefix point (7); (8) gives h_N<=4c0 k^(-theta)<=s/2. If k>=N use the exact zero sigma of h_N. In either case (9) gives

    ||x|| <= (k+1)^(nu/2)/sqrt(nu)
            <= [3/sqrt(nu)] s^(-beta).

For the last inequality, s<=c0 implies (8c0/s)^(1/theta)>=1; hence k+1<=3(8c0/s)^(1/theta), 3^(nu/2)<=3 and (8c0)^beta<=1. The triangle bound for (x,z) proves (13).

These common constants are essential. An asymptotic profile with an onset depending arbitrarily on N or T would not support the minimax statement.

Every orthogonal rotation of the x coordinates leaves (13), smoothness, C^2 regularity and nonattainment unchanged.

## 5. Arbitrary deterministic algorithms: a consistent resisting rotation

Fix any deterministic first-order algorithm with at most T queries. It may know beta, all class constants, f_*=0, and even the full template (11), except for the orthogonal basis of its N-dimensional x-block. Choose N=2T+2. The extra scalar z-coordinate and its function phi are known and are not hidden.

We construct orthonormal directions e_1,...,e_N incrementally. Initially none are fixed. At query j (j=1,...,T), at most e_1,...,e_(2j-2) have been fixed. Write the algorithm's x-query as its projection on their span plus an orthogonal component. Choose e_(2j-1) along that component if it is nonzero; if it is zero, choose any new orthogonal direction. Then choose one further orthogonal direction e_(2j).

The query lies in span(e_1,...,e_(2j-1)). By the exact zero-chain property, its gradient is in span(e_1,...,e_(2j)). Return the value and gradient of (11) in those coordinates, including the known scalar tail's value and derivative. All as-yet-unassigned coordinates of this query are exactly zero.

Later choices are orthogonal to all preceding fixed directions and hence all preceding queries. No later choice can change a previous function value or gradient: the largest direction a previous gradient uses has already been assigned. This proves transcript consistency inductively, rather than changing the problem retroactively.

After the last query the algorithm produces an arbitrary output (x_out,z_out). Choose e_(2T+1) along its component orthogonal to the existing span, or any new direction if that component is zero. Complete by e_(2T+2). The returned x_out is supported on the first 2T+1<N chain coordinates.

Now fix this final orthogonal matrix U once and for all. The single function

    f(x,z)=h_N(U^T x)+phi(z)

belongs to F_beta(N+1), supplies every response in the observed transcript, and has

    f(x_out,z_out) >= c0/R_(2T+1)
       >= [c0/(1+4/theta)](2T+2)^(-theta).             (14)

The positive scalar tail cannot weaken this lower bound. The algorithm may make enormous queries, use nonlinear transformations of past responses, or output a point it never queried. All those possibilities were included when choosing the next direction and final output direction. Exact real function values do not reveal unassigned directions, because the value of each queried point is literally independent of them.

This proves the lower half of (1). Early-stopping algorithms can be padded with unused repeated queries, without changing their output, or the argument can be run at their actual number of queries. QED.

Randomized algorithms are not covered by choosing the rotation after seeing a realized random seed: that would not establish a fixed distributional lower bound. No such inference is made.

## 6. Consequences and correct interpretation

1. The accelerated nonattainment exponent of 26 is optimal in this dimension-uniform deterministic first-order model. One cannot improve it uniformly by a different deterministic gradient/value strategy, even with unrestricted query locations and exact knowledge of the infimum.
2. For rho(s)~s^(-beta), the optimal number of calls is Theta(epsilon^(-beta-1/2)). For beta=1/2 this is Theta(1/epsilon); for beta=1 it is Theta(epsilon^(-3/2)); for beta=2 it is Theta(epsilon^(-5/2)).
3. The upper algorithm is the same for all beta. It is automatically order-adaptive; it never estimates the exponent in its updates.
4. The lower examples can be semialgebraic for every positive rational beta, so the theorem is not driven by oscillatory or nondefinable pathologies.
5. The lower proof is not an oracle lower bound for a SPECIFIED SDP represented by explicit coefficient matrices, a lower bound for arbitrary cone-projection algorithms, or a randomized/minimax theorem in fixed dimension. It concerns values and gradients of a black-box smooth convex objective.
6. The hard core is quadratic. Its hidden orthogonal basis is essential for the arbitrary-query theorem; publishing that matrix as input changes the computational model. The scalar tail makes the objective genuinely nonattained without creating an unknown membership problem.
7. This proves rates and their optimal powers, not optimal leading constants. The proof does not predict editorial decisions or certify historical priority.

## 7. Established background and research contribution

Classical first-order complexity, quadratic chains, and orthogonal resisting oracles are the antecedents. Relevant primary sources include:

- Y. Drori, The exact information-based complexity of smooth convex minimization, Journal of Complexity 39 (2017), 1–16; arXiv:1606.01424; DOI 10.1016/j.jco.2016.11.001. This concerns the classical attained-minimum framework, not a source of a new algorithm claimed here.
- C. Guzman and A. Nemirovski, On lower complexity bounds for large-scale smooth convex optimization, Journal of Complexity (2015); DOI 10.1016/j.jco.2014.08.003. General black-box lower-bound context.
- Project manuscript 26, parent snapshot stated above: comparator-energy proof without minimizers and exact fixed-instance power laws. The needed upper argument is fully reproduced in Section 2.

The extra work in the present proof is the uniform-in-N multiscale chain construction (4)–(9), profile verification (13), and its use in the unrestricted deterministic transcript argument (14). A search of these antecedents is not a comprehensive novelty certificate. The mathematical claim is the precisely quantified theorem (1)–(2), not resolution of a named classical conjecture.
