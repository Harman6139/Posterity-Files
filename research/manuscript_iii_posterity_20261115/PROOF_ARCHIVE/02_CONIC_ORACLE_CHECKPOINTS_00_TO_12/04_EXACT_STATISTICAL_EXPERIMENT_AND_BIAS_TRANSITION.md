# Checkpoint 04 — exact statistical minimax risk and bias transition

This completely solves the fixed known-template two-point experiment from checkpoints 01--02. It is not a solution of the full noiseless dimension-uniform conic class.

Use f_theta(x,y)=g(y)+(a^2/2)(x-theta R)^2+(c^2/2)min(x+2R,0)^2, theta in {-1,+1}, Delta=a^2R^2/2, eta=a^2R. The known tail has infimum zero, unattained. Let bar_f=(f_++f_-)/2. The exact noisy coordinate-gradient oracle is

    G(q)=grad bar_f(q)-Y e_x, Y=theta eta+xi,

with independent xi~N(0,sigma^2). The template and all scales are supplied; only theta is hidden. Arbitrary query locations, adaptation, computation and output are allowed. No exact population value is returned.

## Theorem 1 — exact fixed-budget expected risk

For sigma>0, after N samples the infimum minimax expected objective is

    Delta E[sech^2(gamma+sqrt(gamma) Z)],
    gamma=N eta^2/sigma^2, Z~N(0,1).

At N=0 this equals Delta. For sigma=0 and N>=1 its value is zero. These are infima, not attained risks, because the tail is strictly positive at every finite output.

Proof. Every transcript is equivalent to the N observations Y_j; queries cannot change their law. Under the equal prior the posterior mean of theta is

    m=tanh(eta sum_j Y_j/sigma^2).

Conditional on the observations, the quadratic term is minimized at x=Rm, which lies in [-R,R], where the filler vanishes. Its conditional Bayes risk is Delta(1-m^2). The nonnegative filler cannot improve it, and the known tail can be made arbitrarily small with a deterministic finite output. The distribution of the log-likelihood half-ratio conditional on theta=+1 is gamma+sqrt(gamma)Z; symmetry of sech^2 makes the mixture expectation equal to that conditional expectation. The symmetric rule x=Rm has equal risks for the two signs, so its Bayes risk is also minimax in the infimum sense. The lower bound follows from the same equal prior. With noiseless Y, one sample identifies theta. QED.

## Theorem 2 — exact fixed-confidence failure probability

For every 0<epsilon<Delta, the minimax probability of f_theta(output)>epsilon is exactly

    Phi(-eta sqrt(N)/sigma)

for sigma>0, with the natural noiseless convention. For N=0 the value is 1/2, allowing randomized algorithms.

Proof. Success requires theta*x>0, because the wrong half-line has objective at least Delta. Therefore failure is bounded below by the optimal binary testing error, the displayed Gaussian error. Conversely decide theta by sign(sum Y_j), choose x=R times that decision, and choose the known tail below epsilon. Correct decisions succeed; incorrect decisions incur core value 4Delta and fail. The two conditional error probabilities are equal, so the Bayes testing error is minimax. QED.

## Theorem 3 — exact critical bias for the known pair

Now permit arbitrary history-dependent bias vectors of norm at most nu and conditionally centered gradient errors of second moment at most sigma^2. For the known pair the exact threshold is eta:

(a) If nu>=eta, the deterministic common oracle G=grad bar_f is admissible under both signs. For any number of calls, the infimum minimax expected risk is at least Delta, and the minimax failure probability for epsilon<Delta is at least 1/2. The lower expected bound is attained in the infimum sense by x=0 and tail tending to zero. The failure bound is attained by a fair sign guess and the two corresponding core minimizers.

(b) If nu<eta, put d=eta-nu>0. From a gradient reply form the scalar Y_j=partial_x bar_f(q_j)-G_{j,x}. Then, conditioned on history, theta E[Y_j|history]>=d. Writing Y_j=E[Y_j|history]+zeta_j gives a martingale-difference sequence with E zeta_j^2<=sigma^2 and E(sum zeta_j)^2<=N sigma^2. The sign of the average is incorrect only if theta sum zeta_j<=-Nd. Cantelli's one-sided variance inequality yields error at most

    sigma^2/(sigma^2+N d^2).

Thus a fixed failure probability alpha in (0,1/2) is achieved with O_alpha(1+sigma^2/d^2) calls, followed by the corresponding core minimizer and a sufficiently accurate known tail. With sigma=0, one call suffices.

For necessity choose the admissible bias b_theta=theta nu e_x and independent Gaussian centered errors in the x coordinate. Then Y_j has mean theta(eta-nu) and variance sigma^2. Theorem 2's testing argument gives the lower bound

    N >= (sigma^2/d^2)[Phi^(-1)(1-alpha)]^2.

Zero calls cannot achieve failure below 1/2. Hence the fixed-confidence minimax sample complexity for this known pair is Theta_alpha(1+sigma^2/(eta-nu)^2) below the threshold, and impossible below failure 1/2 at or above it. QED.

## Consequences and limitations

For the rational carrier at scale Delta=Theta(epsilon), eta=Theta_beta(epsilon^(beta+1)). The exact pair transition supplies the conic absolute-bias scale without any appeal to a generic smooth surrogate construction. It also quantifies the blow-up as a specified pair's bias budget approaches its precise threshold from below.

The statistical query model intentionally omits exact true values: f_+(x,y)-f_-(x,y)=-2eta x, so a noiseless true value at nonzero x would reveal the sign. A covariance/bias guarantee on a coordinate-gradient measurement is not the same as a guarantee on a PSD-valued projection sample. The exact confidence theorem is for Gaussian testing; the robust upper bound needs only conditional second moments and therefore has the stated alpha dependence rather than an unproved logarithmic high-confidence claim.
