# Checkpoint 10 — the sharp relative-noise crossover

This closes the small-relative-noise crossover left open in checkpoint 06, for the unrestricted REAL-data conic class of checkpoint 09 and the radius-charged RATIONAL-data class of checkpoint 08. It does not close the original free-radius rational exact-oracle question.

## Model and theorem

For each natural conic objective f, a gradient measurement at q has conditional mean grad f(q)+b and conditional centered variance at most sigma^2 f(q), where

    ||b|| <= nu sqrt(f(q)).

The error specification concerns coordinate gradients; no exact population values or PSD-valued projection samples are supplied. The variance/bias conditions hold conditionally on all previous samples, including within batches. Fix a positive rational beta and common escape-profile constants.

In either of the two declared classes/models, for sufficiently small epsilon and nu <= c_beta epsilon^(beta+1/2), the optimal expected-error sample/charged cost is

    Theta_beta(epsilon^(-beta-1/2)
                    +sigma^2 epsilon^(-2beta-1)).       (1)

Constants are uniform in sigma>=0. If nu>=C_beta epsilon^(beta+1/2), an epsilon guarantee is impossible. Fixed-confidence versions with any fixed success probability strictly above 1/2 have the same powers; the three-sign construction below gives failure greater than 2/3 for a suitable fixed hard prior. For the charged model each measurement is charged 1+epsilon^(2beta)||q||^2; output is uncharged.

Thus the useful batching crossover is sigma^2 approximately epsilon^(beta+1/2). For a feasibility residual delta, epsilon=delta^2/2, and the terms are delta^(-(2beta+1)) and sigma^2 delta^(-(4beta+2)); the relative-bias scale is delta^(2beta+1).

## 1. A self-contained accelerated upper bound

The proof is valid for every nonnegative convex 1-smooth f with f(0)<=1 and a known comparison radius. Fix epsilon<=1. Choose u with

    f(u)<=s=epsilon/128,
    ||u||<=R, R>=1,

and work on Q={q:||q||<=R}. For the profile class one may take R=max(1,C_beta(epsilon/128)^-beta).

Use the accelerated batch algorithm with x_0=z_0=0,A_0=0 and

    a_j=(1+sqrt(1+8A_j))/4,
    A_(j+1)=A_j+a_j=2a_j^2,
    y_j=(A_j x_j+a_j z_j)/A_(j+1),
    Gbar_j=average of M fresh samples at y_j,
    z_(j+1)=Proj_Q(z_j-a_j Gbar_j),
    x_(j+1)=(A_j x_j+a_j z_(j+1))/A_(j+1).

Let r=sigma^2/M. The averaged centered error xi_j has conditional mean zero and conditional second moment at most r f(y_j). The averaged bias has norm at most nu sqrt(f(y_j)), even when it depends on preceding samples in the batch.

The smoothness, convexity and projection calculation gives

    E[A_(j+1)(f(x_(j+1))-s)+||z_(j+1)-u||^2/2]
      <=E[A_j(f(x_j)-s)+||z_j-u||^2/2]
          +2a_j R nu E sqrt(f(y_j))+r a_j^2 E f(y_j).  (2)

Here one uses -a_j<xi_j,z_(j+1)-z_j> <= ||z_(j+1)-z_j||^2/4+a_j^2||xi_j||^2, and the remaining term -a_j<xi_j,z_j-u> has expectation zero. No minimizer is presumed to exist.

Define the deterministic nondecreasing majorant

    D_0=R^2/2,
    D_(j+1)=D_j+2a_j R nu E sqrt(f(y_j))
                          +r a_j^2 E f(y_j).

Then (2) implies E f(x_j)<=s+D_j/A_j for j>=1.

### Control of the variance at the actual extrapolated queries

Nonnegative 1-smoothness implies ||grad f(x)||<=sqrt(2f(x)). The descent lemma therefore gives

    f(y) <= (sqrt(f(x))+||y-x||/sqrt(2))^2
          <=2f(x)+||y-x||^2.

Since x_j,z_j are in Q and A_(j+1)=2a_j^2,

    a_j^2 E f(y_j)
      <=A_(j+1) E f(x_j)+R^2
      <=A_(j+1)s+[A_(j+1)/A_j]D_j+R^2, j>=1.

The ratio A_(j+1)/A_j is at most 3 for j>=1. Also R^2<=2D_j. At j=0, a_0=1/2, y_0=0, and a_0^2 f(0)<=1/4<=D_0/2. Consequently, for all j<K,

    a_j^2 E f(y_j) <= A_K s+5D_j.                    (3)

Jensen's inequality and (3) yield

    D_(j+1) <= D_j+2Rnu sqrt(A_K s+5D_j)
                            +r(A_K s+5D_j).          (4)

This is the step missing from a naive conversion of relative variance into a global absolute variance bound.

### Parameters and finite-budget induction

Set

    K=ceil(8R/sqrt(epsilon)),
    M=max(1,ceil(48 sigma^2 K)),
    nu<=1/(16sqrt(6) K).

The weight recurrence gives (K+1)^2/8<=A_K<=K^2/2. Since K<=9R/sqrt(epsilon), A_K s<=81R^2/256<R^2. If D_j<=R^2, equation (4) increases it by at most

    2sqrt(6) R^2 nu+6rR^2.

Over all K steps this increase is at most R^2/8+R^2/8=R^2/4, because Knu<=1/(16sqrt(6)) and Kr<=1/48. Starting from R^2/2 proves by induction that D_j<=3R^2/4 for every j<=K. Therefore

    E f(x_K)<=epsilon/128+6R^2/(K+1)^2<epsilon.

The total samples satisfy

    KM <= K+48sigma^2 K^2
       =O(R/sqrt(epsilon)+sigma^2 R^2/epsilon).        (5)

The sufficient bias bound is nu<=c sqrt(epsilon)/R. Substituting R=Theta_beta(epsilon^-beta) proves the upper half of (1) and the sufficient bias exponent. All queries remain in Q, so their radius-charged cost is O_beta(1) per sample.

## 2. Fixed rational conic lower distribution for relative variance

Use the rational testing carrier at scale Delta=Theta_beta(epsilon), with a^2=Theta_beta(epsilon^(2beta+1)), and THREE independent hidden signs theta in {-1,+1}^3 drawn uniformly before algorithm randomness. Write

    f_theta(x,y)=h(x,y)+(a^2/2)sum_(i=1)^3(x_i-theta_i R0)^2,
    h=g_beta(y)+(c^2/2)sum_(i=1)^3 min(x_i+2R0,0)^2.

This is the same rational isometric natural PSD-distance pencil as checkpoint 06. The scale R0 denotes the carrier displacement, not the comparison radius R in the upper proof. Put

    v_theta(x)=a^2(x-theta R0),
    p=2a^2/(sigma^2+2a^2).

For sigma>0, draw an independent Bernoulli(p) variable B on each sample and return

    G(q)=grad h(q)+(B/p)(v_theta(x),0).

It is unbiased, and

    E||G-grad f_theta||^2
      =(1/p-1)||v_theta||^2
      =sigma^2 (a^2/2)sum_i(x_i-theta_i R0)^2
      <=sigma^2 f_theta(q).

The same Bernoulli variable is used for all three carrier coordinates in a sample. On the event of N consecutive zeros, all replies equal the common grad h, irrespective of every query and every output rule. This event is independent of theta and has probability

    (1-p)^N=(1+2a^2/sigma^2)^(-N)
             >=exp(-2a^2N/sigma^2).

If epsilon<Delta, success requires all three output signs to be correct. Conditional on the no-reveal event, the success probability is at most 1/8. Thus, whenever N<=sigma^2/(16a^2),

    Pr{f_theta(output)>epsilon}
       >=(7/8)exp(-1/8)>2/3.                         (6)

This proves Omega_beta(sigma^2 epsilon^(-2beta-1)) samples against arbitrary adaptive randomized queries of arbitrary finite magnitude. If this numerical scale is less than one, the sequential term dominates; no discontinuous claim at sigma=0 is needed.

## 3. Noiseless term and systematic bias

Zero noise is permitted by the relative variance upper bound. Therefore checkpoint 09 supplies the exact sequential lower term for the real-data unrestricted class, and checkpoint 08 supplies it for the rational radius-charged class. The maximum of the two lower terms is comparable to their sum, yielding (1) uniformly in sigma.

For relative bias, the common deterministic oracle grad h has error norm

    ||v_theta(x)||<=sqrt(2)a sqrt(f_theta(x,y)).

It is admissible for every sign when nu>=sqrt(2)a. Its transcripts are identical for all eight signs, so for epsilon<Delta average success is at most 1/8, regardless of the number or magnitude of queries. Since a=Theta_beta(epsilon^(beta+1/2)), this gives the matching impossibility exponent.

The variance/bias lower families are rational of fixed matrix order for each beta; their data have O_beta(log(1/epsilon)) bits. Exact population values would distinguish the signs and are not part of this stochastic oracle.

## 4. Scope and attribution

Acceleration, batching, nonnegative smoothness self-bounds and Gaussian/Bernoulli testing are standard techniques. The proof above makes their combination explicit for nonattained conic objectives and closes the joint noise crossover, rather than only treating a fixed positive relative-noise level. The lower bound is realized by the actual natural PSD-distance function, not by an unspecified representable surrogate.

No claim is made that a floating-point PSD projection implementation necessarily has this error distribution, or that coordinate-gradient noise can automatically be realized by an unbiased PSD-valued projection sample. The free-radius RATIONAL exact-oracle problem remains unresolved here.
