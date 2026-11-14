# Milestone 31 — A common leading trajectory for monotone optimization and plain Douglas–Rachford

Date: 2026-11-13 (America/Toronto).
Repository: Harman6139/Posterity-Files.
Branch: laa-track02-gptpro-analytic-frontier-20261112.
Parent snapshot: eb3b8b9aceb29d7a534216b46a4855524d0693ad.

## Scope

This manuscript applies the independently proved tame cosmic-convergence theorem in 30. It identifies a single leading vector and power shared by regularization, proximal iteration, monotone flow, and, when available, gradient descent. It also proves a common direction and exact leading power for PLAIN, unanchored Douglas–Rachford on every weakly infeasible SDP. This strengthens the earlier norm-order and anchored-method results without claiming an unproved universal last-iterate residual rate for unanchored DRS.

The classical tools are Minty's resolvent theorem, monotone-semigroup contractivity, one-variable semialgebraic asymptotics, and nonexpansiveness of proximal/gradient/projection maps. The new conclusions stated here are consequences of the comparison theorem proved in 30. Gradient-trajectory directions at infinity have established antecedents (Grandjean; Loi; see Daniilidis–Salas–Tapia-Garcia, arXiv:2504.07259, Section 2.2); that qualitative continuous-gradient conclusion is not being claimed as newly discovered. The unrestricted cosmic-convergence conjecture was disproved by Ryu. Neither that false conjecture nor the separate nonsmooth slope-determination conjecture is being claimed resolved here.

## 1. Maximal-monotone regularization at infinity

Let A:R^d ->> R^d be maximal monotone, with semialgebraic graph, and assume

    0 not in range A.

For s>0 write J_s=(I+s A)^(-1). The classical maximal-monotone resolvent theorem makes J_s single-valued, defined on all R^d, and firmly nonexpansive. Its graph is semialgebraic because

    y=J_s(a) iff (y,(a-y)/s) belongs graph A.

Fix any anchor a and put y(s)=J_s(a).

### Theorem A — a universal first vector term

There are p in Q intersect (0,1] and a nonzero c in R^d, independent of the anchor, such that

    y(s)=c s^p+o(s^p).                                  (1)

For every fixed lambda>0 and every initial x,

    J_lambda^k(x)=c (lambda k/p)^p+o(k^p).               (2)

Every locally absolutely continuous solution of

    x'(t)+A(x(t)) contains 0, for almost every t,

on a positive-time tail satisfies

    x(t)=c (t/p)^p+o(t^p).                              (3)

The assertion about flows applies to the usual maximal-monotone semigroup trajectories when they have the stated strong-solution regularity, in particular the subgradient flows discussed in Section 3. No existence is asserted for an arbitrary initial point outside the appropriate closure of the domain.

Thus the regularized points, all fixed-step proximal orbits, and monotone flows have the same limiting normalized direction c/||c|| and the SAME leading vector at the corresponding physical time. This is stronger than convergence of normalized directions alone.

### Proof of (1)

Choose (x_bar,u_bar) in graph A. Since J_s(x_bar+s u_bar)=x_bar, nonexpansiveness gives

    ||y(s)-x_bar||<=||a-x_bar-s u_bar||.

Therefore y(s)=O(s). If y(s_j) were bounded for s_j->infinity, a subsequence would converge to y_* and (a-y(s_j))/s_j->0. Closedness of the graph would give 0 in A(y_*), a contradiction. Hence ||y(s)||->infinity.

The definable curve is eventually smooth and has a first nonzero Puiseux term c s^p with rational p>0. The linear bound gives p<=1. This proves (1), together with

    y'(s)=p c s^(p-1)+o(s^(p-1)).                       (4)

For two anchors, ||J_s(a)-J_s(b)||<=||a-b||, so c,p are independent of the anchor.

### Proof of (2): an exact relation of the two resolvents

Let T=J_lambda and let q(t) be its discounted path with anchor a as in 30:

    q(t)+t(q(t)-Tq(t))=a.

There is the exact identity

    q(t)=[a+t J_(lambda(1+t))(a)]/(1+t).                (5)

Indeed put b=J_(lambda(1+t))(a). Then (a-b)/(lambda(1+t)) belongs A(b). For the right side q of (5), q-b=(a-b)/(1+t) belongs lambda A(b), so Tq=b and q+t(q-b)=a.

By (1), the first term of q(t) is lambda^p c t^p. Theorem B of 30 therefore gives (2).

### Proof of (3): contractive tracking of a time-changed resolvent

On a sufficiently late tail, define b(t)=y(s_0+t/p). It is continuously differentiable, and

    u_b(t)=[a-b(t)]/(s_0+t/p) belongs A(b(t)).

Equation (4) gives

    e(t):=b'(t)+u_b(t)=o(t^(p-1)).                     (6)

For a strong trajectory x choose u_x(t)=-x'(t) in A(x(t)). Monotonicity yields

    (1/2)d||x-b||^2/dt
       =-<x-b,u_x-u_b>-<x-b,e>
       <=||x-b|| ||e||.

Regularizing the norm at zero, or integrating its upper derivative, gives

    ||x(t)-b(t)||<=constant+integral ||e(s)|| ds=o(t^p).

Since p>0, integrating o(s^(p-1)) gives o(t^p). Combining with (1) proves (3). QED.

## 2. Arbitrarily varying bounded proximal steps

Let 0<lambda_k<=Lambda<infinity, with

    tau_k=sum_(j<k)lambda_j ->infinity.

The schedule need not be definable, converge, or be chosen independently of the iterates. Run

    x_(k+1)=J_(lambda_k)(x_k).

Then

    x_k=c (tau_k/p)^p+o(tau_k^p).                      (7)

### Proof

Put s_k=s_0+tau_k/p and b_k=y(s_k). Since u_(k+1)=(a-b_(k+1))/s_(k+1) belongs A(b_(k+1)),

    J_(lambda_k)(b_(k+1)+lambda_k u_(k+1))=b_(k+1).

Nonexpansiveness gives

    ||J_(lambda_k)(b_k)-b_(k+1)||
       <=||b_k-b_(k+1)-lambda_k u_(k+1)||.

The leading terms cancel by (1) and (4): over the bounded increment lambda_k/p,

    b_(k+1)-b_k=lambda_k c s_k^(p-1)
                                      +o(lambda_k s_k^(p-1)),
    -lambda_k u_(k+1)=lambda_k c s_k^(p-1)
                                      +o(lambda_k s_k^(p-1)).

The little-o is uniform on increments at most Lambda/p. Summing the local defects and using bounded-mesh comparison with the integral of s^(p-1) gives o(tau_k^p). Nonexpansiveness then proves ||x_k-b_k||=o(tau_k^p), and (1) gives (7).

If iterate errors are added, the same conclusion holds under the sufficient condition sum_(j<k)||error_j||=o(tau_k^p). No fixed-precision robustness is inferred without that condition.

## 3. Convex optimization: proximal, gradient, and flow select one leading vector

Let f:R^d->R union {+infinity} be proper, lower semicontinuous, convex and semialgebraic, and suppose argmin f is empty. Its subdifferential is a maximal-monotone semialgebraic operator. Thus

    y(s)=argmin_x [f(x)+||x-a||^2/(2s)]

is uniquely defined. Theorems A and (7) apply to proximal iterations and to its standard subgradient flow. No smoothness of f is needed for those conclusions; the trajectory statement uses the usual positive-time absolute continuity of the subgradient flow.

If, in addition, f is finite differentiable and its gradient is globally L-Lipschitz, then for any 0<eta<=2/L the map T_eta=I-eta grad f is nonexpansive. Its discounted point satisfies

    q(t)+eta t grad f(q(t))=a,
    q(t)=J_(eta t subdiff f)(a).

Consequently ALL fixed-step gradient iterations in that range satisfy

    x_k=c (eta k/p)^p+o(k^p).                           (8)

All choices of starting point, positive fixed proximal step, and admissible fixed gradient step have the same direction. At equal physical time t=eta k=lambda j, their first vector terms equal c(t/p)^p, also equal to that of the subgradient flow. This does not identify their subleading terms, objective leading constants, or last-step residuals.

Variable gradient steps in (0,2/L] with divergent sum obey the physical-time version of (8) by the variable-relaxation theorem in 30. Arbitrary adaptive preconditioning is NOT covered: a fixed non-Euclidean metric changes the norm defining the regularized path and may change its leading direction.

### Finite infimum and the earlier radius exponent

Assume f_*=inf f is finite and unattained, and write

    rho(delta)=min{||x-a||: f(x)-f_*<=delta}
                =Theta(delta^(-beta)), beta>0.

Semialgebraicity guarantees this positive rational exponent. Then the resolvent exponent in (1) is

    p=beta/(2beta+1), in (0,1/2).                       (9)

To prove it, compare the regularized optimum to a radius-minimizing point of gap delta. With delta=s^(-1/(2beta+1)),

    [f(y(s))-f_*]+||y(s)-a||^2/(2s)
                  <=C s^(-1/(2beta+1)).

The two summands are nonnegative. Thus the gap is O(s^(-1/(2beta+1))) and the norm is O(s^(beta/(2beta+1))). Applying the lower bound for rho to that gap gives the matching norm lower bound. Comparing with (1) proves (9).

This refines the earlier norm-order results to an EXACT LEADING VECTOR. It does not solve the separate slope-determination conjecture: equality of gradient/subgradient norms is not one of the hypotheses here and does not, without another argument, identify two different regularized paths.

## 4. Plain Douglas–Rachford on every weakly infeasible SDP

Let A:S^m->R^q be linear, with b in closure A(S_+^m) but b not in A(S_+^m). Define

    U={Z:A(Z)=b}, V=S_+^m,
    T(Z)=Z+P_V(2P_U Z-Z)-P_U Z.                         (10)

The affine space U is nonempty because b belongs range A. The map T is semialgebraic and nonexpansive (indeed firmly nonexpansive). It has no fixed point: a fixed point would give P_U Z=P_V(2P_U Z-Z) in U intersect V. Its infimal displacement is zero: affine points approaching V give displacements approaching zero.

Choose a in U and let z(t) be the discounted path of T. Then there are a rational p in (0,1) and a nonzero symmetric matrix C such that

    z(t)=C t^p+o(t^p).

The plain unanchored orbit Z_(k+1)=T(Z_k), from EVERY symmetric initial matrix, satisfies

    Z_k=p^(-p) C k^p+o(k^p).                            (11)

In particular Z_k/||Z_k||_F converges to one initial-condition-independent direction, including the weakly infeasible, zero-linear-drift case.

### The power is determined by source escape

Let

    R_b(delta)=min{tr X:X>=0,||A(X)-b||<=delta}
                  =Theta(delta^(-a0)).

This exponent exists and is positive rational by semialgebraic growth and trace compactness, without using the sharp dimensional envelope of manuscript 12. Then

    p=a0/(a0+1).                                      (12)

Here is the full comparison. For anchor a in U, the fixed-point radius for (10) is EXACTLY

    R_T(epsilon)=min{||u-a||:u in U,dist(u,V)<=epsilon}. (13)

A primal u in U satisfies Tu=P_V u. Conversely from Z with ||Z-TZ||<=epsilon, put u=P_U Z and v=P_V(2u-Z). Then ||u-v||<=epsilon and ||u-a||<=||Z-a||. This proves (13).

A fixed linear right inverse L of A on its range maps a PSD approximate solution X to X+L(b-A(X)) in U, changing norm and cone distance by O(||A(X)-b||). Conversely projecting u in U to V gives equation residual at most ||A|| dist(u,V), and its trace is bounded by sqrt(m) times its norm. Thus R_T and R_b have the same divergent power a0. Section 5 of 30 yields (12).

### The actual primal shadows have a nonzero common leading term

Let L0=ker A and let P_L0 be its Frobenius-orthogonal projector. Put

    H=P_L0 C.

Then H is NONZERO and

    H>=0, A(H)=0.                                     (14)

Moreover the affine and PSD shadows

    U_k=P_U Z_k, V_k=P_V(2U_k-Z_k)

satisfy

    U_k=p^(-p) H k^p+o(k^p),
    V_k=p^(-p) H k^p+o(k^p).                            (15)

To prove H>=0, apply the projections to the discounted path. Its affine shadow u(t) has leading term H t^p. Its PSD shadow v(t) differs from u(t) by Tz(t)-z(t)=O(t^(p-1)), which tends to zero. Thus their scaled limits are equal, and v(t)>=0 implies H>=0. Clearly A(H)=0.

For nonzeroness, dist(u(t),V)<=||Tz(t)-z(t)||=O(t^(p-1)). The lower primal radius profile in (13) then gives

    ||u(t)-a||>=c t^(a0(1-p))=c t^p.

Therefore H cannot be zero. Now apply the affine projection to (11) to get the first limit in (15). The PSD projection is continuous and positively homogeneous. Applying it to 2U_k-Z_k, and using the already identified discounted limit P_V(2H-C)=H, gives the second. QED.

This yields a genuine PSD recession direction from plain DRS after normalization. It is an ASYMPTOTIC conclusion, not a finite stopping certificate or an algorithm for detecting weak infeasibility in polynomial bit time. It also does NOT prove a universal rate for the last difference ||Z_(k+1)-Z_k||; subtracting two o(k^p) remainder terms would not justify that inference.

### Anchoring and relaxation

The gamma-anchor iteration of 30 has state leading coefficient (p+gamma)^(-p) C and primal-shadow leading coefficient (p+gamma)^(-p) H. In particular gamma=1 (Halpern) and gamma=0 (plain DRS) have the SAME power and direction, but different leading magnitudes.

A fixed relaxation theta in (0,1] multiplies the plain leading coefficient by theta^p. These statements concern the states and their shadows. Earlier exact residual estimates for the anchored variant remain separate results.

## 5. An exactly solvable weakly infeasible two-by-two system

Let

    U={[[0,1],[1,s]]:s in R}, V=S_+^2,
    a=[[0,1],[1,0]].

The exact discounted path of (10) is, for t>0,

    z(t)=[[h(t),b(t)],[b(t),h(t)]],
    h(t)=t sqrt(t+1)/(t+2), b(t)=2/(t+2).              (16)

To verify it without numerical eigenvalue decisions, put

    u=[[0,1],[1,h]], R_U z=[[-h,2-b],[2-b,h]],
    v=[[h/t,1+(b-1)/t],[1+(b-1)/t,(1+1/t)h]],
    N=v-R_U z.

The matrices v,N have positive diagonals, determinant zero and vN=0. Thus v,N are the orthogonal positive and negative parts of R_U z, and v=P_V(R_U z). Also v-u=(z-a)/t. Therefore Tz-z=(z-a)/t, proving (16) by uniqueness of the contraction solution.

As t->infinity, z(t)/sqrt(t)->I_2. Thus p=1/2,C=I_2, and the theorem predicts

    plain Z_k/sqrt(k)->sqrt(2) I_2,
    Halpern Z_k/sqrt(k)->sqrt(2/3) I_2.                (17)

The actual feasible shadows divided by sqrt(k) converge to the same constants times E_22.

For an independent scalar check, starting the plain iteration at a preserves the form [[h_k,b_k],[b_k,h_k]], with

    b_k=2^(-k), h_0=0,
    h_(k+1)=[h_k+sqrt(h_k^2+(2-b_k)^2)]/2.             (18)

Hence h_k grows to infinity and h_(k+1)^2-h_k^2->2, so h_k/sqrt(k)->sqrt(2), agreeing with (17). The matrix computations in (16) and the first recurrence in (18) are included as exact symbolic checks in the accompanying code.

## 6. Relation to established results and precise limits

Pazy/Crandall–Pazy describe the linear drift. When that drift is zero, linear normalization alone loses the nonzero sublinear leading vector. The preceding results recover that vector for all the semialgebraic maps considered here.

Ryu disproved the cosmic-convergence conjecture for general nonexpansive maps, including a firmly nonexpansive example. The tameness hypothesis is substantive and excludes such oscillatory counterexamples. Bolte–Gaubert–Vigeral proved asymptotic average behavior for definable nonexpansive operators using discounted paths; the time-changed unnormalized tracking proof here establishes the first nonzero vector term and direction at sublinear scales.

Continuous semialgebraic gradient-trajectory directions at infinity were studied by Grandjean and Loi, and the determination paper of Daniilidis–Salas–Tapia-Garcia discusses them. The present paper does not claim to be the first directional-convergence theorem for that subclass. It supplies a common leading coefficient shared across the methods above and extends the discrete conclusion to general tame nonexpansive maps.

No randomized oracle lower bound, direction-selection theorem for arbitrary nondefinable operators, infinite-dimensional cosmic convergence, universal unanchored-DRS residual exponent, or general nonsmooth slope-determination proof follows here. No polynomial-time claim is made for discovering the minimum face, computing the Puiseux leading term, or extracting a useful finite infeasibility certificate. A specific ADMM conclusion requires an explicit DRS equivalence and metric; no blanket statement about all implementations is made.

## References

1. E. K. Ryu, Cosmic Divergence, Weak Cosmic Convergence, and Fixed Points at Infinity, arXiv:1709.02838v2. https://arxiv.org/html/1709.02838
2. J. Bolte, S. Gaubert, G. Vigeral, Definable zero-sum stochastic games, arXiv:1301.1967v2, especially one-variable tameness and Theorem 3 on nonexpansive maps. https://arxiv.org/html/1301.1967
3. A. Daniilidis, D. Salas, S. Tapia-Garcia, Determination of (unbounded) convex functions via Crandall-Pazy directions, arXiv:2504.07259, especially Section 2.2 and the classical monotone-flow background. https://arxiv.org/html/2504.07259v1
4. Project manuscript 30: independent discounted-path comparison proof. Manuscript 28: earlier anchored residual rates and the exact profile identity, which is reproved in Section 4 here.

Historical priority for the full synthesis is not certified by the targeted literature search. The mathematical conclusions and their limitations are stated explicitly instead of equating this with guaranteed publication.
