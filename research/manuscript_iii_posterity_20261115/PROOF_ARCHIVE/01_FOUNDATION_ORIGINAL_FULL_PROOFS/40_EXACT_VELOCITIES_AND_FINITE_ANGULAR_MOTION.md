# Milestone 40 — Exact velocities and finite angular motion of convex splittings at infinity

Date: 2026-11-14. Manuscript I.
Parent snapshot: ba7fdf3457b990e61fb22592248503f35b8eb250.
Branch: laa-track02-gptpro-analytic-frontier-20261112.

## Scope

This proves an exact last-step theorem for every finite-dimensional proper closed convex semialgebraic objective with a finite unattained infimum, under constant-step forward–backward splitting. The leading state, velocity, objective gap, and objective decrement depend on the TOTAL objective, not the chosen convex smooth/nonsmooth splitting, after conversion to physical time. Only the total objective must be semialgebraic: the pieces and update map need not be definable. A quantitative remainder proves finite total angular motion of the radially normalized discrete orbit.

The feasibility specialization covers alternating projections on every pair of closed convex semialgebraic sets disjoint at distance zero, including every weakly infeasible SDP of arbitrary order. It is NOT the unresolved all-order plain Douglas–Rachford last-step theorem. The generic analytic firmly nonexpansive counterexample in 35 does not contradict the present theorem: a single convex objective supplies cyclic subgradient and energy inequalities absent for general monotone resolvents.

The proof is self-contained apart from classical proximal existence, convex gradient cocoercivity and one-variable semialgebraic Puiseux asymptotics. No previous project theorem is a correctness premise. Originality, external refereeing and journal acceptance are not certified. Classical and current antecedents are identified at the end.

## 1. Exact theorem

Let F:R^d -> R union {+infinity} be proper, lower semicontinuous, convex and semialgebraic, with

    F_* = inf F > -infinity,       argmin F = empty.

For an arbitrary anchor a define

    y(s)=argmin_x {F(x)+||x-a||^2/(2s)}, s>0.

There exist an anchor-independent nonzero c and rational p in (0,1/2) such that

    y(s)-a=c s^p+o(s^p).

Put

    V=p^(-p)c,       B=p^2||V||^2/(1-2p).

For ANY splitting F=g+h with g finite convex C1 and globally L-Lipschitz gradient, and h proper closed convex, take a fixed 0<eta<2/L and run

    x_(k+1)=prox_(eta h)(x_k-eta grad g(x_k)),
    tau_k=eta k.

For L=0, any eta>0 is allowed. Every x0 in R^d is allowed; x_k belongs dom F after the first step. Neither g nor h needs to be semialgebraic.

### Theorem A

    x_k=V tau_k^p+o(tau_k^p),
    tau_k^(1-p)(x_(k+1)-x_k)/eta -> pV,
    F(x_k)-F_* ~ B tau_k^(2p-1),
    [F(x_k)-F(x_(k+1))]/eta
                   ~p^2||V||^2 tau_k^(2p-2).

Consequently the last-step direction tends to V/||V|| and

    [F(x_k)-F(x_(k+1))]/[||x_(k+1)-x_k||^2/eta] ->1.

The SAME p,V,B work for every starting point, permissible stepsize and convex splitting of the given F. They depend on the objective and Euclidean metric. No equality of trajectories or computational costs is asserted.

### Theorem B: asymptotic efficiency

For rho_a(delta)=min{||x-a||:F(x)<=F_*+delta},

    ||x_k-a||/rho_a(F(x_k)-F_*) ->1,
    sum_(j<k)||x_(j+1)-x_j|| / ||x_k-x0|| ->1.

Thus the orbit has asymptotically minimum radius at its achieved objective level, and its travel has asymptotically no excess over net displacement.

### Theorem C: finite angular motion

There is zeta>0 such that

    tau_k^(1-p)(x_(k+1)-x_k)/eta=pV+O(tau_k^(-zeta)).

For any fixed anchor a, normalized states n_k=(x_k-a)/||x_k-a|| are defined on a tail and obey

    sum_(k>=K)||n_(k+1)-n_k|| <= C0 K^(-zeta)

for all sufficiently large K. Their total chordal and geodesic variation on the sphere is finite. The radially projected piecewise-linear orbit has finite length there as well. This is proved quantitatively below, not inferred from direction convergence alone.

## 2. The quadratic regularization path

The proximal objective defining y is coercive and strongly convex. Its unique minimizer satisfies

    u(s)=(a-y(s))/s in partial F(y(s)).                  (1)

The graph of y is semialgebraic by quantified minimization or the subgradient graph. For every w in dom F,

    F(y(s))-F_*+||y(s)-a||^2/(2s)
       <=F(w)-F_*+||w-a||^2/(2s).                      (2)

Taking limsup and then letting F(w) decrease to F_* proves F(y(s))->F_* and ||y(s)-a||^2/s->0. The path diverges: a bounded subsequence would converge to a minimizer by lower semicontinuity. Puiseux growth therefore gives

    y(s)-a=c s^p+o(s^p),
    y'(s)=pc s^(p-1)+o(s^(p-1)),                       (3)

with c!=0 and rational 0<p<1/2. The strict upper inequality follows from the little-o conclusion in (2), not merely an O(sqrt(s)) bound. The path is smooth on a sufficiently late tail.

Resolvent nonexpansiveness gives ||y_a(s)-y_b(s)||<=||a-b||, so c,p are independent of the anchor.

Subgradient inequalities at s and s+h squeeze the difference quotient of F(y(s)), since u(s) is continuous. Hence

    dF(y(s))/ds=<u(s),y'(s)>
               =-p||c||^2 s^(2p-2)+o(s^(2p-2)).        (4)

Integrating to infinity gives

    F(y(s))-F_* ~ A s^(2p-1),
    A=p||c||^2/(1-2p).                                (5)

At s=tau/p, the coefficient is A p^(1-2p)=B.

## 3. Splitting-independent state tracking

For convex L-smooth g, the classical cocoercivity inequality is

    ||grad g(x)-grad g(y)||^2
       <=L<grad g(x)-grad g(y),x-y>.                   (6)

One proof applies the descent lemma to g minus its tangent at y, which has a minimum at y, and then interchanges x,y and adds. Equation (6) makes I-eta grad g nonexpansive for eta<=2/L. The prox is firmly nonexpansive, so their composition T_eta is nonexpansive.

Write b(s)=grad g(y(s)). The convex sum rule gives u(s)-b(s) in partial h(y(s)). Monotonicity of partial h and (6) imply, for positive v,

    ||b(s+v)-b(s)||^2
       <=L<b(s+v)-b(s),y(s+v)-y(s)>
       <=L<u(s+v)-u(s),y(s+v)-y(s)>.                  (7)

Since u'=O(s^(p-2)) and y'=O(s^(p-1)), uniformly for v in any bounded positive interval,

    ||b(s+v)-b(s)||=O(v s^(p-3/2)).                   (8)

No definability of b,g,h is used.

Take s_k=s_c+eta k/p and y_k=y(s_k), on a late tail. The point y_(k+1) is the prox of

    y_(k+1)+eta[u(s_(k+1))-b(s_(k+1))].

Consequently

    ||T_eta(y_k)-y_(k+1)||
      <=||y_k-y_(k+1)-eta u(s_(k+1))
                         +eta[b(s_(k+1))-b(s_k)]||
      =o(k^(p-1)).                                    (9)

The leading terms cancel by (1),(3), and (8) is of smaller order. Nonexpansiveness yields

    ||x_k-y_k||<=constant+sum_(j<k)o(j^(p-1))=o(k^p).

This proves the state term, without presuming an asymptotic expansion of the actual orbit.

## 4. Coarse energy and subgradient bounds

Subtract F_* for the remaining proof. Define

    F_k=F(x_k), G_k=(x_k-x_(k+1))/eta, q_k=||G_k||^2,
    e_k=grad g(x_(k+1))-grad g(x_k).

Proximal optimality gives

    v_(k+1)=G_k+e_k in partial F(x_(k+1)).              (10)

Let d_eta=1-eta L/2>0. Descent and the comparator inequality give

    F_k-F_(k+1)>=eta d_eta q_k,                        (11)
    2eta[F_(k+1)-F(w)]
       <=||x_k-w||^2-||x_(k+1)-w||^2
                     -(1-eta L)||x_(k+1)-x_k||^2.     (12)

For eta L>1 the positive remainder after summing (12) is bounded by (11) and the initial gap. Otherwise it is dropped. Thus, after one initial step if necessary, for a finite E independent of w,k,

    F_k<=F(w)+[||x_1-w||^2+E]/[2eta(k-1)].             (13)

Choose w=y(tau_k). Equations (3),(5) give

    F_k=O(tau_k^(2p-1)),       F_k->0.                (14)

Nonexpansiveness of T_eta makes q_k nonincreasing. Sum (11) from about k/2 to k-1 to obtain

    q_k=O(tau_k^(2p-2)).                              (15)

Since ||e_k||<=eta L||G_k||, (10) also gives ||v_k||=O(tau_k^(p-1)). These are only coarse bounds; no last-step conclusion has yet been used.

## 5. Exact objective coefficient

Convexity at x_k and y(s_k) gives

    <u(s_k),x_k-y(s_k)>
       <=F(x_k)-F(y(s_k))
       <=<v_k,x_k-y(s_k)>.

The subgradients have norm O(tau_k^(p-1)); the state difference is o(tau_k^p). Therefore the objective difference is o(tau_k^(2p-1)). Equation (5) proves

    F_k~B tau_k^(2p-1).                                (16)

It would still be invalid to differentiate this sequence or the state expansion directly. The next two sections supply the missing argument.

## 6. An asymptotically exact tail-energy identity

The forward contraction and nonexpansiveness of prox imply

    ||x_(k+1)-x_(k+2)||^2
       <=||x_k-x_(k+1)||^2-eta(2/L-eta)||e_k||^2.

Thus, for L>0,

    sum_(j>=k)||e_j||^2<=C_eta q_k,
    C_eta=eta/(2/L-eta)<infinity.                       (17)

When L=0 all e_j vanish. Let I_k=eta sum_(j>=k)q_j. It is finite and at most F_k/d_eta. Consecutive subgradient inequalities give

    eta(q_j+<e_j,G_j>)
       <=F_j-F_(j+1)
       <=eta(<G_(j-1),G_j>+<e_(j-1),G_j>).             (18)

Sum them. The upper quadratic terms differ from I_k by at most eta q_(k-1), by monotonicity and telescoping. Cauchy–Schwarz and (17) control each remaining sum of inner products. In particular

    |F_k-I_k|<=eta q_(k-1)
                   +sqrt(eta C_eta q_(k-1) I_k).       (19)

A larger fixed constant would suffice as well. From (15),(16), the two errors are respectively O(tau_k^(2p-2)) and O(tau_k^(2p-3/2)), both o(F_k). Hence

    eta sum_(j>=k)||G_j||^2~B tau_k^(2p-1).             (20)

For a nonincreasing sequence q_k, a tail asymptotic

    eta sum_(j>=k)q_j~B(eta k)^(-alpha), alpha>0,

implies

    q_k~alpha B(eta k)^(-alpha-1).                     (21)

Proof: forward and backward secants of the tail over indices k to floor(lambda k) and floor(k/lambda) to k bound eta q_k. Substitute the asymptotic and then let lambda decrease to one. Floors have vanishing relative effect. This monotone-density proof requires no differentiability of a sequence.

Taking alpha=1-2p in (20) gives

    q_k~p^2||V||^2 tau_k^(2p-2).                       (22)

In particular q_(k+1)/q_k->1. The one-step version of (17) now yields

    e_k=o(tau_k^(p-1)),
    v_(k+1)=G_k+o(tau_k^(p-1)).                        (23)

## 7. Identifying the actual vector

Consider any subsequential limit W of tau_k^(1-p)v_k. It exists along a further subsequence by the coarse bound. Equations (22),(23) give ||W||=p||V||.

For fixed lambda>0 take j(k)/k->lambda and use convexity at x_k:

    F_(j(k))-F_k >= <v_k,x_(j(k))-x_k>.

The state and objective limits give

    B(lambda^(2p-1)-1)>=<W,V>(lambda^p-1).             (24)

Divide by the positive denominator for lambda>1 and the negative denominator for lambda<1. Sending lambda to one from both sides proves

    <W,V>=B(2p-1)/p=-p||V||^2.

Together with ||W||=p||V||, equality in Cauchy–Schwarz forces W=-pV. Every subsequential limit agrees. Thus tau_k^(1-p)G_k->-pV and the last velocity limit is proved.

Finally (18), (23) and the vector limit squeeze each individual objective decrement to eta p^2||V||^2 tau_k^(2p-2). This proves the remaining conclusions of Theorem A. In particular a single-step energy identity emerges asymptotically despite the globally weaker descent constant 1-eta L/2.

## 8. Minimum radius and length

Let delta_s=F(y(s))-F_*. A point with objective at most F(y(s)) and strictly smaller radius about a would contradict the defining regularized minimum. Therefore

    rho_a(delta_s)=||y(s)-a||.

The path objective has an eventually strictly negative derivative by (4), so these levels cover all sufficiently small positive gaps. Equations (3),(5) give

    rho_a(delta)~K delta^(-beta),
    beta=p/(1-2p), K=||c||[p||c||^2/(1-2p)]^beta.      (25)

Combine this with the state and objective constants to obtain Theorem B's radius ratio. The velocity magnitude is asymptotic to eta p||V|| tau_k^(p-1); its sum is ||V|| tau_k^p because p>0. This equals the leading displacement magnitude, proving the path-length ratio.

Equivalently, if rho_a(delta)~K delta^(-beta), then

    p=beta/(2beta+1),
    B=[beta^2 K^2/(2beta+1)]^(1/(2beta+1)).              (26)

Thus the entire leading objective constant is determined by the minimum-radius profile, while the vector direction comes from the regularized path.

## 9. Positive-power remainder and finite spherical variation

Choose a rational kappa with 0<kappa<p<1/2 small enough that the Puiseux path has

    y(s)-a=c s^p+O(s^(p-kappa)),
    y'(s)=pc s^(p-1)+O(s^(p-1-kappa)).                 (27)

Such a kappa exists; taking kappa<p absorbs bounded subleading terms. The local tracking defect (9) is O(k^(p-1-kappa)): its gradient-splitting correction is O(k^(p-3/2)) and its finite-difference correction is O(k^(p-2)), both smaller. Since p-kappa>0, summation gives

    x_k=V tau_k^p+O(tau_k^(p-kappa)).                  (28)

The subgradient comparison and integrated path expansion then give

    F_k=B tau_k^(2p-1)[1+O(tau_k^(-kappa))].            (29)

The relative energy-tail error (19) is O(tau_k^(-1/2)); it is smaller because kappa<1/2. Thus (29) also holds for I_k.

For a quantitative version of (21), use multiplicative secant widths h_k=tau_k^(-kappa/2). The relative tail remainder divided by the width is O(tau_k^(-kappa/2)), the power-law secant error is O(h_k), and integer rounding costs O((k h_k)^(-1)), which is smaller. Hence

    q_k=p^2||V||^2 tau_k^(2p-2)
                             [1+O(tau_k^(-kappa/2))].  (30)

Using separate remainder bounds at k,k+1 (not differentiating them), the one-step contraction implies

    ||e_k||^2<=C_eta(q_k-q_(k+1))
                 =O(tau_k^(2p-2-kappa/2)),
    e_k=O(tau_k^(p-1-kappa/4)).                        (31)

Apply the convex secant inequality with indices whose time ratios are 1+h_k and 1-h_k. Equations (28),(29) and the coarse subgradient bound give

    <tau_k^(1-p)v_k,V>
                   =-p||V||^2+O(tau_k^(-kappa/2)).     (32)

Indeed the two endpoint remainders before division are O(tau_k^(-kappa)), while the secant Taylor error is O(h_k). Transfer (32) from v_(k+1) to G_k using (31). Combine it with (30) and expand the squared distance to -pV:

    ||tau_k^(1-p)G_k+pV||^2=O(tau_k^(-kappa/4)).

Thus zeta=kappa/8 is one valid exponent in Theorem C.

For n_k=(x_k-a)/||x_k-a||, (28) gives n_k=V/||V||+O(tau_k^(-kappa)). The differential of radial normalization is its tangential projector divided by the radius. The quadratic remainder over a step d is O(||d||^2/||x_k-a||^2). Consequently

    n_(k+1)-n_k
       =(I-n_kn_k^T)(x_(k+1)-x_k)/||x_k-a||
                     +O(||x_(k+1)-x_k||^2/||x_k-a||^2),
    ||n_(k+1)-n_k||=O(k^(-1-zeta))+O(k^-2).            (33)

The projector annihilates the leading radial velocity; only the state-direction and velocity remainders remain. Summing proves the tail bound in Theorem C. Geodesic distance between two sphere points is at most pi/2 times their chord. On late orbit segments the origin relative to a is avoided, and the radial projection follows the shorter great-circle arc. Hence the interpolated spherical length is finite too.

No uniform lower bound on zeta or uniform onset is asserted. Nor does this prove finite total variation of normalized VELOCITIES; the spherical-length conclusion concerns the STATES.

## 10. Alternating projections: all semialgebraic zero-distance disjoint pairs

Let U,V be nonempty closed convex semialgebraic sets with empty intersection and distance zero. Set

    g(x)=dist(x,V)^2/2, h=indicator_U.

The squared-distance gradient is x-P_V x and is 1-Lipschitz. The total objective is proper closed convex semialgebraic with finite unattained infimum zero. The eta=1 update is x_(k+1)=P_U P_V x_k.

There are rational 0<p<1/2 and W!=0 such that, for EVERY start,

    x_k=W k^p+o(k^p),
    k^(1-p)(x_(k+1)-x_k)->pW,
    k^(1/2-p)dist(x_k,V)->p||W||sqrt(2/(1-2p)).        (34)

The state and velocity also have positive-power remainders, so the normalized AP trajectory has finite spherical length. W belongs to rec U intersect rec V: scaling the diverging U-points and their nearby V-projections yields the same nonzero closed-convex horizon direction.

The projected-gradient relaxation

    x_(k+1)=P_U((1-eta)x_k+eta P_V x_k), 0<eta<2,

has the same constants at physical time eta k. This iteration is not DRS.

### Weakly infeasible SDPs of every matrix order

For U={Z:A(Z)=b}, V=S_+^m, all formulas (34) hold at every m; W is nonzero PSD and A(W)=0. Let Y_k=P_V x_k and r_k=x_k-Y_k. Then

    x_(k+1)-x_k=-P_(ker A)r_k,
    dist(Y_k,U)^2=||r_k||^2-||x_(k+1)-x_k||^2.

The second term is smaller by order k^-1. Thus dist(Y_k,U) has the same exact leading constant as dist(x_k,V). For arbitrary, possibly redundant equalities,

    dist(Y_k,U)=||(AA*)^(dagger/2)(A(Y_k)-b)||.         (35)

This canonical whitened residual therefore has the exact constant in (34). The unwhitened Euclidean equation residual is only asserted to have the same power, unless an additional residual-direction argument is supplied.

If R_b(delta)=min{tr X:X>=0,||A(X)-b||<=delta}=Theta(delta^-a0), a fixed right inverse and PSD norm/trace equivalence give rho_F(s)=Theta(s^(-a0/2)). Hence

    p=a0/[2(a0+1)].

No sharp dimension-only bound on a0 from an earlier project manuscript is a premise here.

For the order-two slice U={[[0,1],[1,t]]}, the scalar recurrence

    t_next=t+(sqrt(t^2+4)-t)^2/[4sqrt(t^2+4)]

gives t_k~(4k)^(1/4). Thus p=1/4,W=sqrt(2)E_22 and

    k^(3/4)(x_(k+1)-x_k)->E_22/(2sqrt(2)),
    k^(1/4)dist(x_k,S_+^2)->1/sqrt(2),
    k^(1/2)F(x_k)->1/4.

## 11. Flow and variable pure steps

For a standard strong convex subgradient-flow trajectory x'(t)+partial F(x(t)) contains 0, the same V,B satisfy

    x(t)=Vt^p+o(t^p),
    t^(1-p)x'(t)->pV,
    F(x(t))-F_*~Bt^(2p-1).

The velocity statement is along differentiability times, or for the usual right/minimal-subgradient representative. The existence/regularity hypotheses of the convex subgradient semigroup are understood; no trajectory outside its domain is asserted.

Proof: track y(s_c+t/p). Its differential defect y'(s)/p+u(s)=o(t^(p-1)) has integral o(t^p); monotonicity controls the tracking distance. The comparator inequality (1/2)d||x-w||^2/dt<=F(w)-F(x) gives the coarse gap bound with w=y(t). Nonincreasing speed, by semigroup contraction, and the energy identity -dF/dt=||x'||^2 give the coarse speed bound. Subgradient comparison with y(t/p) proves the exact objective constant. Integrating the energy identity and using the monotone-density secants gives the exact speed constant. Convex secants as in (24) identify its vector. This uses classical subgradient-flow energy identities, not a new qualitative gradient-direction theorem.

For variable-step PPA, 0<lambda_k<=Lambda with tau_k=sum_(j<k)lambda_j->infinity gives

    x_k=V tau_k^p+o(tau_k^p),
    tau_k^(1-p)(x_(k+1)-x_k)/lambda_k->pV,
    F(x_k)-F_*~B tau_k^(2p-1).

The same holds for variable-step GD on a finite L-smooth F when lambda_k<=Lambda<2/L. No positive lower stepsize bound is needed; adaptive schedules are included pathwise.

Here are the details for these extensions. Local regularized-curve defects are o(lambda_k(s_c+tau_k)^(p-1)) uniformly on bounded increments, so integral comparison proves the state term. Weighted comparator/descent inequalities yield the coarse objective and speed bounds. PPA subgradients v_(k+1)=(x_k-x_(k+1))/lambda_k have nonincreasing norm; GD gradients do by cocoercivity. Summing descent over a physical-time interval comparable to tau_k/2 gives their O(tau_k^(p-1)) bound. Convex comparison with the path proves the exact objective constant.

For PPA the objective decrement lies between lambda_k||v_(k+1)||^2 and lambda_k||v_k||^2; their tail sums differ by at most Lambda||v_k||^2, negligible relative to the gap. For GD it lies between lambda_k<grad F(x_(k+1)),grad F(x_k)> and lambda_k||grad F(x_k)||^2. Cocoercivity gives

    ||grad F(x_k)||^2-||grad F(x_(k+1))||^2
      >=[2/(Lambda L)-1]||grad F(x_(k+1))-grad F(x_k)||^2.

Thus those tail sums also differ by at most a fixed multiple of Lambda||grad F(x_k)||^2. A piecewise-constant speed-squared function on [tau_k,tau_(k+1)) is nonincreasing and has bounded mesh. The monotone-density secant proof applies in physical time and determines the speed. Convex secants then determine the vector. This does NOT claim arbitrary varying steps for general composite splits, whose gradient-mapping norms need not be monotone.

## 12. Sharp boundaries and nondefinable splittings

The allowance of nontame pieces is nonvacuous. For a convex semialgebraic positive power tail phi, take

    F(x,y)=phi(x)+y^2,
    g(x,y)=y^2/2+sin(y)/4,
    h(x,y)=phi(x)+y^2/2-sin(y)/4.

Both pieces are convex; grad g is globally 5/4-Lipschitz. Neither piece is globally o-minimal definable, since it would define unrestricted sine. Their sum is semialgebraic, and all the fixed-step results including finite spherical variation apply.

The endpoint eta=2/L cannot be included. For a convex semialgebraic tail phi with derivative Lipschitz constant at most one, let F(t,y)=phi(t)+y^2/2. With eta=2, GD has y_k=(-1)^k y0. For y0!=0 the objective gap stays at least y0^2/2, and transverse steps do not decay. The strict stepsize restriction is material.

The analytic firmly nonexpansive map in project manuscript 35 has rotating leading residuals; it is not a subgradient resolvent covered by these energy arguments. Likewise plain affine/PSD DRS is not automatically forward–backward for a convex objective with a finite unattained infimum. Its arbitrary-order last-step vector limit remains unproved here. The unrestricted matrix-order conclusion actually proved is for AP and its displayed projected-gradient relaxation.

All results are finite-dimensional and exact-arithmetic. There is no uniform onset, universal leading vector for changed metrics, floating-point stopping certificate, general inertial/stochastic conclusion or efficient algorithm for recovering the Puiseux data. A fixed positive-definite metric can be handled by a linear isometry, but it generally changes the regularized path and V.

## 13. Diagnostics, antecedents and manuscript role

The accompanying script tests twelve scalar tail/splitting/stepsize combinations, two splittings of one coupled nonsmooth objective, a nondefinable trigonometric splitting, a two-power angular example, and weakly infeasible order-two and order-three AP instances. It also checks exact symbolic constants and the excluded critical stepsize. Recorded floating-point runs illustrate the identities and transients, not universal asymptotic proofs.

The mathematical gain is not another cosmic direction alone: it is the exact last velocity, leading objective and dissipation constants, asymptotic minimum-radius efficiency and finite total angular motion of the discrete trajectory, with invariance under convex splitting. This supplies a potential new main theorem for Manuscript I, separate from the unresolved plain-DRS question.

Primary antecedents:

- Bauschke–Combettes, The Baillon–Haddad Theorem Revisited, arXiv:0906.0807: classical gradient cocoercivity.
- Combettes–Pesquet, Proximal Splitting Methods in Signal Processing, arXiv:0912.3522: classical proximal and forward–backward tools.
- Ji–Dudik–Schapire–Telgarsky, Gradient descent follows the regularization path for general losses, COLT/PMLR 125 (2020), 2109–2136: directional regularization-path agreement for linear-predictor empirical risks. Regularization-path implicit bias is not invented here.
- Grandjean, On the limit set at infinity of a gradient trajectory of a semialgebraic function, Journal of Differential Equations 233 (2007), 22–48: continuous gradient directions at infinity.
- Do–Jentzen–Kuckuck, On the gradient conjecture at infinity: Finite spherical length for gradient trajectories of definable potentials, arXiv:2610.29211v2, revised 9 November 2026: a current continuous-flow spherical-length theorem. No new resolution of that continuous-flow conjecture is claimed. The present argument concerns convex nonsmooth DISCRETE splitting, exact velocities and leading constants, including potentially nondefinable split maps.
- Drusvyatskiy–Li–Wolkowicz, A note on alternating projections for ill-posed semidefinite feasibility problems, Mathematical Programming 162 (2017), 537–548: relevant semidefinite AP background.

Standard one-variable semialgebraic growth and convex subgradient-flow facts are used with their hypotheses stated. The tail-density argument is proved directly. A targeted literature comparison is not comprehensive originality certification. The mathematical results above have not undergone external refereeing; no journal outcome is promised.
