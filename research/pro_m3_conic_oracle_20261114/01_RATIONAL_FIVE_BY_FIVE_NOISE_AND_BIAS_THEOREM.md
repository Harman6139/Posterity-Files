# Checkpoint 01 — genuine rational 5x5 conic noise and bias barriers

Date: 2026-11-14. This is a direct conic construction, not an epigraph-universality transfer. It proves the stochastic lower term and the critical systematic-bias scale at beta=1/2. It does NOT yet prove the noiseless sequential Omega(1/epsilon) lower bound of the full handoff.

## 1. Exact rational, isometric affine pencil

For a dyadic integer R>=2 define

    a=2R^2/(2R^4+1), c=(2R^4-1)/(2R^4+1).

Then 2a^2+c^2=1, c>0, and 2/3 <= aR^2 <1. For theta in {-1,+1}, set

    X_theta(x,z)=diag( B_theta(x), c(x+2R), W(z) ),
    B_theta(x)=[[0,a(x-theta R)],[a(x-theta R),0]],
    W(z)=[[0,1],[1,z]].

This is a 5x5 symmetric affine pencil with rational data. Its two direction matrices have Frobenius inner products delta_ij: the x-direction has squared norm 2a^2+c^2=1, the z-direction has squared norm 1, and their supports are disjoint. The coefficient encoding length is O(log R).

The affine space never meets S_+^5: the last block has a zero first diagonal and a nonzero off-diagonal. Nevertheless, at x=theta R, z->+infinity the distance to S_+^5 tends to zero. Thus every instance is genuinely weakly infeasible.

Spectral clipping gives its EXACT natural objective

    f_theta(x,z)= (a^2/2)(x-theta R)^2
                 +(c^2/2) min(x+2R,0)^2 + phi(z),
    phi(z)=(sqrt(z^2+4)-z)^2/8.

It is convex, C1, and 1-gradient-Lipschitz by the isometry and nonexpansiveness of the cone residual map. No C2 assertion is made at x=-2R. Its infimum is zero, unattained, and f_theta(0,0)<=5/8.

## 2. Uniform escape geometry at every scale

For every R>=2, either sign, and 0<s<=1/8,

    (1/2)s^(-1/2) <= rho_f_theta(s) <= sqrt(2)s^(-1/2).

Proof. Write r(z)=(sqrt(z^2+4)-z)/2, so phi=r^2/2 and z=1/r-r. If phi(z)<=s, then

    z >= (2s)^(-1/2)-sqrt(2s)
       >= [3/(4sqrt(2))]s^(-1/2) > (1/2)s^(-1/2).

For the upper bound choose z=s^(-1/2)-sqrt(s), so phi(z)=s/2 and z<=s^(-1/2). Let Delta=a^2R^2/2. If s>=2Delta, choose x=0. If s<2Delta, choose x=theta R. In the second case sR^2<a^2R^4<1, so the resulting norm is less than sqrt(2)s^(-1/2). In either case the scalar filler is nonnegative and the total objective is at most s. This proves the common onset and constants, independently of R and theta.

## 3. Globally constant gradient separation

Define

    eta=a^2R,
    f_bar=(f_++f_-)/2
         =(a^2/2)(x^2+R^2)+(c^2/2)min(x+2R,0)^2+phi(z).

Then, for EVERY finite (x,z), including arbitrarily large queries,

    grad f_theta = grad f_bar - theta eta e_x.

Also theta*x<=0 implies f_theta(x,z)>=Delta, and f_bar(x,z)>=Delta for all (x,z). Finally

    2sqrt(2) Delta^(3/2) < eta <= 3sqrt(2) Delta^(3/2).

Indeed eta/Delta^(3/2)=2sqrt(2)/(aR^2). The weak inequality version at the lower endpoint is also valid.

These are global identities, not local or asymptotic oracle approximations. The filler ensures the affine directions are isometric while cancelling identically in the two-instance comparison. This is the important construction device.

## 4. Fixed hard distribution and exact noisy-oracle experiment

Draw theta uniformly BEFORE the algorithm's random seed. At the j-th adaptive query let Y_j=theta eta+xi_j with independent xi_j~N(0,sigma^2), and return

    G_j(x,z)=grad f_bar(x,z)-Y_j e_x.

This is an unbiased natural conic-gradient oracle with E||G_j-grad f_theta||^2=sigma^2. Granting the entire Y_j is at least as informative as the oracle transcript; conversely the known-template algorithm can extract Y_j from the answer. Thus, independently of query magnitudes and adaptation, the transcript experiment is exactly N independent Gaussian observations with means +/-eta. Exact true population values are NOT supplied.

Its KL divergence is 2N eta^2/sigma^2. If N<=sigma^2/(16eta^2), Pinsker's inequality bounds total variation by 1/4, so every sign test has average error at least 3/8. Inferring theta from the output's x-coordinate therefore gives

    average E f_theta(output) >= (3/8)Delta.

The exact optimal sign error is Phi(-eta sqrt(N)/sigma). In particular, when epsilon<Delta, a guarantee f_theta(output)<=epsilon with probability >=1-alpha for both signs requires

    N >= (sigma^2/eta^2)[Phi^(-1)(1-alpha)]^2.

This is a fixed two-point distribution over rational weakly infeasible SDPs. It is not a resisting oracle, a seed-adaptive matrix choice, or a generic smooth objective represented by an unspecified SDP.

## 5. Accuracy selection and epsilon^-3 lower term

Delta_R is decreasing for R>=2 and Delta_(2R)/Delta_R>=1/4. For every sufficiently small epsilon choose the largest dyadic R>=2 with Delta_R>=16epsilon. Then

    16epsilon <= Delta_R <64epsilon,
    R=Theta(epsilon^(-1/2)), eta=Theta(epsilon^(3/2)).

The matrix order and coordinate dimension stay 5 and 2, respectively; the rational coefficient encoding length is O(log(1/epsilon)). Section 4 gives

    N=Omega(sigma^2 epsilon^-3)

for expected objective <=epsilon, and the corresponding fixed-confidence lower bound. This applies against arbitrary randomized adaptive algorithms with arbitrary finite query locations and arbitrary unqueried outputs.

## 6. Sharp systematic-bias scale

The deterministic oracle G=grad f_bar is admissible for either sign whenever the absolute Euclidean gradient bias budget nu is at least eta. Both instances then produce the IDENTICAL transcript for every query and every number of calls. For any random output with this common transcript,

    (E f_+(output)+E f_-(output))/2 >= Delta.

With the preceding accuracy selection, no uniform expected-epsilon guarantee is possible when nu>=C epsilon^(3/2), for an absolute constant C. The statement concerns an adversarial absolute-error oracle. It does NOT automatically imply impossibility for a specified deterministic nearest-grid rounding rule, relative-error arithmetic, exact population values, or cone-valued approximate projection outputs.

## 7. Matching conic upper terms and the remaining gap

Consider ALL natural affine PSD-distance objectives with orthonormal affine coordinates, f(0)<=1, inf f=0 unattained, and rho_f(s)<=sqrt(2)s^-1/2 for 0<s<=1/8. They are 1-smooth. A projected accelerated stochastic method on the known ball of radius 2sqrt(2)epsilon^-1/2, using a comparator with f(u)<=epsilon/4, satisfies

    E f(output) <= f(u)+4R_ball^2/(K+1)^2
                   +sigma^2 K/(2M)+2R_ball nu.

Take K=ceil(4R_ball/sqrt(epsilon)) and M=max(1,ceil(2sigma^2 K/epsilon)). Under nu<=epsilon/(8R_ball), its sample cost is

    O(epsilon^-1 + sigma^2 epsilon^-3).

The energy proof is already given in source milestone 39 and will be reproduced self-contained in the manuscript; it uses no conic lower-bound transfer. Thus the conic critical-bias scale is Theta(epsilon^(3/2)). In the noise-dominated regime sigma^2>=epsilon^2, the lower and upper sample costs match as Theta(sigma^2 epsilon^-3). With B-parallel samples, the same construction gives the variance round lower term sigma^2 epsilon^-3/B; the upper bound is O(epsilon^-1+sigma^2 epsilon^-3/B).

The missing exact-oracle lower term Omega(epsilon^-1), especially with rational inputs, is NOT proved here. The displayed hard pair itself is solved by ONE exact gradient query, because the sign is then revealed. Consequently this checkpoint is not a full resolution of the handoff.

## 8. Feasibility and precision translation

A feasibility residual tolerance delta corresponds to epsilon=delta^2/2. Therefore the established conic stochastic lower term is Omega(sigma^2 delta^-6), the sufficient upper cost is O(delta^-2+sigma^2 delta^-6), and the adversarial absolute-gradient-bias threshold is Theta(delta^3). The affine coordinate escape and the norm of the displayed matrices are of order delta^-1 at the testing scale.

An absolute gradient error bound proportional to 2^-b translates to the scale b=(3/2)log_2(1/epsilon)+O(1), or 3log_2(1/delta)+O(1), in the adversarial error-budget model only. A lower bound for a specified floating-point rounding implementation requires a separate proof.
