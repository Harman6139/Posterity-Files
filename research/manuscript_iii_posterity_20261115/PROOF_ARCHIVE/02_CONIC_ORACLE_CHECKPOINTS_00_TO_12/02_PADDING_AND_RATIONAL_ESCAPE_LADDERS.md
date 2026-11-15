# Checkpoint 02 — a conic testing carrier and two infinite rational escape ladders

All statements below concern the natural objective one half of squared Frobenius distance to a PSD cone. They do not use SDP epigraph universality. The noiseless randomized sequential lower bound remains open in this work.

## A. Rational isometric testing carrier

Let g(y)=dist_F(Y0+sum_j y_j G_j,S_+^m)^2/2 be a fixed rational affine pencil with Frobenius-orthonormal direction matrices. Suppose its affine space is weakly infeasible, g(0)<=1/2, and

    c0 s^-beta <= rho_g(s) <= C0 s^-beta, 0<s<=s0,

for a fixed rational beta>0. For integers k>=1 set R=2^k, p=1/(2beta), ell=ceil((1+p)k)+2, t=2^-ell,

    a=2t/(1+2t^2), c=(1-2t^2)/(1+2t^2).

Then a,c are rational and 2a^2+c^2=1. For theta in {-1,1} append the three-by-three block

    diag( [[0,a(x-theta R)],[a(x-theta R),0]], c(x+2R) ).

The resulting (m+3)-by-(m+3) affine pencil has rational orthonormal directions and objective

    f_theta(x,y)=g(y)+(a^2/2)(x-theta R)^2
                       +(c^2/2)min(x+2R,0)^2.

It is weakly infeasible, because the tail is; the carrier is PSD at x=theta R. Write Delta=a^2R^2/2 and eta=a^2R. Direct bounds on the rational parametrization give

    (2/81) R^(-1/beta) <= Delta <= (1/8) R^(-1/beta),
    eta=2Delta/R=Theta_beta(Delta^(beta+1)).

For all 0<s<=s0 the new profile has the common bounds

    c0 s^-beta <= rho_f_theta(s)
        <= sqrt(1+2^(2beta) C0^2) s^-beta.

Indeed take a g-comparator at s/2. If s>=2Delta use x=0. Otherwise use x=theta R; since 2Delta R^(1/beta)<=1/4, one has R<=s^-beta. Also f_theta(0)<=1/2+Delta<=1. All constants and the onset are independent of k and theta.

The two gradients differ globally by 2eta e_x, and their midpoint vector field is a deterministic surrogate at distance eta from either gradient. A uniform sign drawn before algorithm randomness and independent Gaussian observations with means +/-eta produce EXACTLY the same testing experiment as in checkpoint 01. Therefore the conic class realizes the stochastic term

    Omega_beta(sigma^2 epsilon^(-2beta-2))

and the adversarial absolute-gradient-bias impossibility scale

    nu >= C_beta epsilon^(beta+1).

To select the scale, let j be the FIRST index with Delta_j<K epsilon, with any sufficiently large fixed K, and use k=j-1. For sufficiently small epsilon, j>=2. The displayed two-sided estimates show Delta_j tends to zero and give Delta_j/Delta_(j-1)>=(16/81)2^(-1/beta). Thus K epsilon<=Delta_k<[(81/16)2^(1/beta)]K epsilon. No monotonicity is needed: dyadic rounding can produce small upward steps in Delta_k. All added coefficients have O_beta(log(1/epsilon)) encoding length.

The projected accelerated conic-gradient method proves the matching upper terms

    O_beta(epsilon^(-beta-1/2)+sigma^2 epsilon^(-2beta-2)),

when nu<=c_beta epsilon^(beta+1). Thus the bias exponent is sharp, and the sample bound is matching whenever sigma^2>=epsilon^(beta+3/2). This last condition is the noise-dominated regime, not a resolution of the missing noiseless term.

## B. Fast rational isometric tails at every matrix order

Let m=n+1>=2 and use coordinates 0,...,n. For y in R^n define an arrow pencil Y(y):

    Y00=0, Y01=1,
    Yii=y_i/3 and Y0,i+1=2y_i/3 for 1<=i<n,
    Ynn=y_n,
    Yij=0 for 1<=i<j<=n.

All other entries follow by symmetry. For n=1, this is [[0,1],[1,y_1]]. The first n-1 direction matrices have squared norm 1/9+2(4/9)=1, and the last has squared norm 1. Their supports are pairwise disjoint. All data are bounded rationals.

There is no PSD point because Y00=0 and Y01=1. Put E_i=2^i-1 and E=E_n. Its natural distance objective satisfies

    rho_g(s)=Theta_m(s^(-E/2)).

Here are direct proofs, with no inherited escape theorem.

Lower bound: if dist(Y,S_+^m)<=delta<=1/2, then Y+delta I is PSD. Let t_i=Yii. The two-by-two principal minors imply

    t_1+delta >= 1/delta,
    t_i+delta >= 4t_(i-1)^2/delta, 2<=i<=n.

Induction gives t_i >= (1/2)delta^(-E_i). At the induction step the preceding lower bound gives t_i+delta>=delta^(-E_i), and delta<=delta^(-E_i)/2. Thus ||y||>=t_n>=(1/2)delta^-E.

Upper bound: for 0<e<=1 set t_1=n/e and t_i=4n t_(i-1)^2/e. Set y_i=3t_i for i<n and y_n=t_n. The Schur sum for Y+e I is

    sum_i Y0i^2/(t_i+e) <= sum_i Y0i^2/t_i=e.

Its top diagonal is e, so Y+e I is PSD. Hence dist(Y,S_+^m)<=sqrt(m)e. The recursion gives t_i=C_i e^(-E_i), with positive fixed C_i. Thus ||y||<=C_m e^-E. Set e=delta/sqrt(m) and delta=sqrt(2s). This proves both bounds on a common small interval. Also g(0)=1/2.

Accordingly beta_m^+=(2^(m-1)-1)/2 is realized by a bounded-rational isometric pencil of order m. The carrier yields the stochastic and bias lower bounds in order m+3.

## C. Slow rational isometric tails at every matrix order

For the same n=m-1, use variables (z,y_1,...,y_(n-1)). Define an arrow pencil Z by

    Z00=z, Z01=-1, Znn=0,
    Zii=y_i/3 and Z0,i+1=-2y_i/3 for 1<=i<n,
    Zij=0 for 1<=i<j<=n.

The directions are again rational, pairwise orthogonal and unit norm. Exact PSD feasibility is impossible: the final zero diagonal forces the preceding leaf diagonal to zero, and induction contradicts Z01=-1. Its natural objective satisfies

    rho_g(s)=Theta_m(s^(-1/(2E))), E=2^n-1.

Upper bound: let q>0, t_1=q, t_i=4q t_(i-1)^2 for 2<=i<=n, and set z=n/q. Let S have the same arrow entries as Z, but leaf diagonals t_1,...,t_n. Every term of its Schur sum equals 1/q, so S is PSD. The affine point is Z=S-t_n E_nn, with distance at most t_n. Since

    t_i=4^(2^(i-1)-1)q^(2^i-1),

the residual is delta=t_n=C_n q^E, whereas the affine coordinate norm is O_m(1/q) for q<=1. This gives the upper bound.

Lower bound: if dist(Z,S_+^m)<=delta<=1/4, then Z+delta I is PSD. Put M=z+delta. For n=1 its determinant gives M delta>=1. For n>=2 the minors give

    t_1+delta >=1/M,
    t_i+delta >=4t_(i-1)^2/M, 2<=i<n,
    delta>=4t_(n-1)^2/M.

Necessarily M>=1: if M<1, the first lower bound and induction give every t_i>=1/2, contradicting the last inequality. If delta M^E<=1/4, then delta<=M^(-E_i)/4 for all i<n. Induction gives t_i>=(1/2)M^(-E_i), and the last inequality implies delta>=M^-E, a contradiction. Therefore M>(4delta)^(-1/E). Since z=M-delta>=M/2, the affine coordinate norm is at least (1/2)(4delta)^(-1/E). Substitute delta=sqrt(2s).

Thus beta_m^- = 1/[2(2^(m-1)-1)] is also realized by bounded-rational isometric data. The two ladders include beta=1/2 and approach respectively infinity and zero as matrix order grows. This does not classify every attainable exponent or assert a whole interval at fixed order.

## D. Scope

These proofs strengthen the conic realization beyond one illustrative 5x5 example: a rational isometric carrier transfers statistical testing and absolute-bias indistinguishability to every fixed tail satisfying the displayed hypotheses, and explicit tails supply two infinite exponent ladders. The transfer is a complete query-level simulation for the noisy gradient experiment, not a claim about exact value-gradient sequential hardness. Exact population values at nonzero x reveal the sign. Each two-point family needs only one exact gradient query. No full randomized noiseless minimax lower bound is claimed.
