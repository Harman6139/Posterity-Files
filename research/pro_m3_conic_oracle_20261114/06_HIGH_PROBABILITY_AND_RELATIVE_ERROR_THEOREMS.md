# Checkpoint 06 — high-probability lower bounds and residual-relative errors

These are additional proved consequences of the rational carrier. None supplies the missing noiseless sequential term.

## 1. Failure probability at least 2/3 with a fixed conic distribution

Append THREE independent copies of the carrier in checkpoint 02 to a fixed tail g. Draw theta uniformly from {-1,+1}^3 before algorithm randomness. The population objective is

    f_theta(x,y)=g(y)+sum_(i=1)^3 [(a^2/2)(x_i-theta_i R)^2
                                  +(c^2/2)min(x_i+2R,0)^2].

The matrix order is m_tail+9, the direction matrices remain rational and orthonormal, and f_theta(0)<=1/2+3Delta<1. The uniform escape upper constant is sqrt(3+2^(2beta)C0^2): use x=0 if s>=6Delta, and x_i=theta_i R otherwise, with a tail comparator at s/2. In the second case 6Delta R^(1/beta)<=3/4, so R<=s^-beta. The tail gives the same lower escape bound as before.

Each sample supplies independent Gaussian coordinates Y_i=theta_i eta+xi_i with xi_i~N(0,sigma^2/3), through the natural gradient plus the corresponding centered noise. Total gradient-noise variance is sigma^2. Every adaptive transcript is equivalent to N such three-dimensional samples, independently of query magnitudes. If epsilon<Delta, successful output requires all three signs to be correct. The maximal success probability under the fixed prior is

    [Phi(eta sqrt(3N)/sigma)]^3.

When N<=sigma^2/(48eta^2), this is at most Phi(1/4)^3<0.6^3<1/3. Therefore

    Pr_{theta,algorithm,oracle}{f_theta(output)>epsilon}>2/3.

Accuracy selection Delta=Theta_beta(epsilon) gives N=Omega_beta(sigma^2 epsilon^(-2beta-2)) with the 2/3 failure constant, not just an expected-risk bound. This is a fixed finite distribution over rational weakly infeasible SDPs of fixed order for each beta. For beta=1/2 the tail order can be 2, so the high-probability construction has order 11 and four coordinates.

For systematic absolute bias, the common midpoint gradient has distance sqrt(3)eta from each true gradient. At that budget all eight instances give identical transcripts. Their epsilon-success regions are disjoint when epsilon<Delta, so any algorithm has average failure at least 7/8, even after infinitely many queries. With exact gradients one query reveals all three signs; this is not an exact-oracle sequential hard family.

## 2. A noisy VALUE-and-gradient extension with exact transcript control

For the one-sign pair, f_theta(q)=bar_f(q)-theta eta x. Let each independent sample be the entire random convex function

    ell_Y(q)=bar_f(q)-Y x, Y=theta eta+xi.

Supplying its value and gradient at any query, or even supplying the whole sampled function, is equivalent to supplying Y. The expected function is exactly the natural conic objective f_theta. The gradient variance is sigma^2 and the value variance is sigma^2 x^2. Arbitrarily large queries do not improve the experiment because they amplify signal and value noise by the same factor.

This extends the lower theorem to a precisely specified joint stochastic value/gradient model. It is NOT a lower bound when true population values are supplied, nor for a fixed query-independent absolute value-noise bound. In the latter case, the difference f_+-f_-=-2eta x can be amplified without limit by a large x.

## 3. Residual-relative coordinate-gradient bias: sharp exponent

Consider a relative measurement model

    G(q)=grad f(q)+b(q)+xi(q),
    ||b(q)||<=nu sqrt(f(q)),
    E[xi|history]=0, E[||xi||^2|history]<=sigma^2 f(q).

The factor sqrt(2) converting sqrt(f) to the feasibility residual is immaterial, but must be included when an implementation uses delta(q)=sqrt(2f(q)). This remains a coordinate-gradient model, not a claim about PSD-valued projection samples.

For the pair, write h(x,y)=g(y)+(c^2/2)min(x+2R,0)^2. The common deterministic oracle grad h has error magnitude a^2|x-theta R|<=sqrt(2)a sqrt(f_theta(x,y)). Hence it is admissible for both signs whenever nu>=sqrt(2)a. Its identical transcripts imply average objective at least Delta, and average failure at least 1/2 for epsilon<Delta. Since

    a=Theta_beta(Delta^(beta+1/2)),

this proves a conic impossibility at relative-bias scale nu>=C_beta epsilon^(beta+1/2).

Here is a matching universal sufficient scale, with a complete elementary proof. Let Q be the ball of radius R=C(epsilon/8)^-beta and take u in Q with f(u)<=epsilon/8. Projected stochastic gradient descent starts at x_0=0 and updates x_(j+1)=Proj_Q(x_j-h G_j). Nonnegative 1-smoothness gives ||grad f||^2<=2f. Put C1=4+2nu^2+sigma^2 and h=1/(2C1). Conditional second moments imply E||G_j||^2<=C1 f(x_j). Projection, convexity and ||x_j-u||<=2R yield

    E_j||x_(j+1)-u||^2
      <=||x_j-u||^2-2h(f(x_j)-f(u))
         +4hRnu sqrt(f(x_j))+h^2 C1 f(x_j).

Use 4Rnu sqrt(f)<=f/2+8R^2nu^2. Since h C1=1/2, this gives

    E_j||x_(j+1)-u||^2
      <=||x_j-u||^2-h f(x_j)+2h f(u)+8hR^2nu^2.

Telescoping and convexity of the average x_bar give

    E f(x_bar)<=2C1 R^2/N+2f(u)+8R^2nu^2.

Thus nu<=sqrt(epsilon)/(8R) and N>=4C1R^2/epsilon suffice for expected objective at most epsilon. The relative-bias exponent is therefore SHARP:

    nu_critical=Theta_beta(epsilon^(beta+1/2)).

For residual tolerance delta, this is Theta_beta(delta^(2beta+1)); beta=1/2 gives Theta(delta^2). Absolute gradient error instead has threshold Theta(delta^(2beta+2)), as proved earlier. These are adversarial error-budget statements, not automatic lower bounds for a specified rounding rule.

## 4. Relative-variance stochastic lower bound

In the same relative model with zero bias, let p=2a^2/(sigma^2+2a^2) and draw independent B_j~Bernoulli(p). Return

    G_j(q)=grad h(q)+(B_j/p)a^2(x-theta R)e_x.

It is unbiased. Its variance is

    (1/p-1)a^4(x-theta R)^2
      =sigma^2 (a^2/2)(x-theta R)^2
      <=sigma^2 f_theta(q).

On the event B_1=...=B_N=0 the full transcript is identical for both signs, no matter where the algorithm queries. This event has probability (1-p)^N. Therefore the average expected objective is at least Delta(1-p)^N and the average epsilon-failure probability is at least (1-p)^N/2 when epsilon<Delta. Querying at x=0 reveals theta whenever a nonzero Bernoulli response occurs, so both bounds are exact in the same infimum sense as checkpoint 04.

For fixed sigma>0 and Delta=Theta_beta(epsilon), this gives Omega_beta(sigma^2 epsilon^(-2beta-1)) samples. The projected-gradient upper bound above is O_beta((1+sigma^2)epsilon^(-2beta-1)) for bounded small bias. Thus the epsilon exponent is minimax sharp for every fixed positive relative-noise level; constants may depend on that fixed level. Bounds match uniformly in sigma>=1. The sharper JOINT small-sigma/noiseless crossover is NOT established by this argument, and must not be inferred from it.
