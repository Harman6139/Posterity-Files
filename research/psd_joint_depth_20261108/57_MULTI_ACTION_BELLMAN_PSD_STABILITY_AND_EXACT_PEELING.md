# Milestone 57 — exact Bellman stability exponent and facial peeling for multi-action PSD incidence systems

Date: 2026-11-08. **PROVED for a strictly larger class than single-action harmonic midpoint pencils**, with complete upper bounds against every ambient PSD competitor and an exact minimal facial-degree/rank-profile rule. This is a NEW candidate combinatorial normal-form family, NOT a claim that all arbitrary dense kernels reduce to it.

## The finite controlled midpoint data

Vertices are 0 (source of weight 0), 1,...,h (internal) and T=h+1 (terminal of weight 1). Each internal vertex i has a nonempty finite set A_i of *actions*, each action being an unordered parent pair (a,b) with
    0<=a<i<b<=T.
Require all action parent edges across all i to be pairwise distinct. An optional additional independent leading edge (0,t) may be used if distinct from every action edge.

For fixed rational lambda>0, let K⊂S^(h+2) be the span of the following independent matrices:
    H_(i,a,b)=E_ii-E_00+lambda F_ab  for (a,b)∈A_i,
and, if applicable, G=lambda F_(0,t).
Here F_ab=E_ab+E_ba. Let L be orthogonal projection onto K-perp and X*=E_00. Every generator has trace zero and terminal diagonal zero, so the identity belongs to the measurement span; L is trace controlled.

Define the **controlled harmonic/Bellman weights** by
    w_0=0, w_T=1,
    w_i=min_{(a,b)∈A_i} (w_a+w_b)/2.
The operator is a strict contraction after at most h steps: from each internal state a fair parent random walk can reach the terminal by choosing the higher-index parent at each step, an event of probability ≥2^-h, regardless of adaptive actions. Hence its value function is unique. It is rational, because an optimal deterministic stationary policy exists and its values solve a nonsingular rational harmonic system. For the statements below assume the solution is STRICT:
    0<w_1<...<w_h<1.
(If Bellman solutions are non-monotone or have ties, the present positive-definite exposing-stress construction requires refinement and no depth conclusion is claimed there.)

Let alpha=w_1 if no optional edge, and alpha=min(w_1,w_t/2) if an optional (0,t) edge is included.

## Theorem A — exact full ambient PSD recovery exponent

X* is uniquely recoverable among all PSD matrices, and
\[
\boxed{\omega_{\mathcal L,X_*}(\delta)=\Theta(\delta^\alpha)}.
\]

**Proof of global upper bound.** For any PSD X with residual ||P_(K-perp)(X-X*)||_F<=delta, set Y=X*+P_K(X-X*), E=X-Y. Then ||E||_F<=delta, Y+delta I≽0, tr(Y)=1, Y_TT=0, and tr X<=1+sqrt(n)delta, so all matrix diagonals and Y's diagonal coordinates are bounded. Write
    Y_ii=x_i=sum_(a,b∈A_i)y_(i,a,b)
and Y_ab=lambda*y_(i,a,b) for every distinct action edge. The optional leading edge has Y_(0,t)=lambda*z. Principal two-by-two minors of Y+delta I give, for U_i=|Y_ii|+delta (source U_0 bounded, terminal U_T=delta),
    |y_(i,a,b)|<=C sqrt(U_a U_b).
Consequently
    U_i<=delta+C sum_(a,b∈A_i)sqrt(U_aU_b).                (1)
The Bellman equation says w_i<= (w_a+w_b)/2 for EVERY action. Choose constants M_v>0 (source and terminal fixed larger than their residual-independent bounds) satisfying
    M_i>=2+2C sum_(a,b∈A_i)sqrt(M_a M_b).                 (2)
Such finite positive constants exist: solve the *maximizing* stochastic shortest-path equation for logarithms,
    v_i>=log(2+2C|A_i|)+max_actions (v_a+v_b)/2,
with finite boundary log M_0, log M_T; uniform terminal hitting-time bounds ensure a finite supersolution v, then set M_i=e^(v_i).

For 0<delta<=1, the quantities Ubar_v=M_v delta^(w_v) satisfy
    Ubar_i>=2delta+2C sum_actions sqrt(Ubar_aUbar_b)
because every action's weight average is >=w_i. Suppose R=max_v U_v/Ubar_v>1, attained at an internal vertex (boundary ratios<=1). At that vertex (1) and the doubled supersolution imply
    R Ubar_i <=delta+R C sum sqrt(Ubar_aUbar_b)
            <=(1+R) Ubar_i/2,
which contradicts R>1. Thus U_i<=M_i delta^(w_i) for every i. The individual action variables obey
    |y_(i,a,b)|<=C delta^((w_a+w_b)/2)<=C delta^(w_i),
and the optional variable z<=C delta^(w_t/2). Tr(Y)=1 controls Y_00-1. Every off-pattern entry of X is O(delta) through E. Therefore ||X-X*||_F<=C' delta^alpha, proving uniqueness as delta->0.

**Matching strictly positive-definite curve.** Choose one Bellman-optimal action (a_i,b_i) per internal i and set y_(i,a_i,b_i)=t^(w_i), with all other actions zero; set terminal diagonal X_TT=t, and optional z=t^(w_t/2). The resulting matrix is
    X(t)=E00+sum_i t^(w_i)H_(i,a_i,b_i)+t E_TT+[t^(w_t/2)G].
Its diagonal source entry is 1-sum_i t^(w_i)>0 for small t. Congruence by the inverse square roots of diagonal entries yields a matrix with diagonal one and selected offdiagonal entries lambda (or lambda divided by sqrt of the source diagonal). Since action parent edges are distinct, taking lambda<1/(8(h+2)) makes this normalized matrix strictly diagonally dominant, hence PD. Every generator H and G lies in K and E_TT∈K-perp, so the measurement residual is exactly t. A diagonal internal coordinate of magnitude t^(w_1), or the optional edge of magnitude lambda t^(w_t/2), gives displacement Omega(t^alpha). This proves the sharp exponent.

## Theorem B — exact canonical minimal facial degree and profile

Start with all non-source vertices remaining. At each stage remove the unique **largest** set C of remaining non-source vertices obeying the *all-actions closure*:
    whenever i∈C and an action (a,b)∈A_i has both a,b still remaining, then a,b∈C.
The terminal is unconstrained. Then the successive sets C_1,...,C_d are exactly the supports removed by the canonical maximum-rank PSD facial-reduction chain. In particular the minimal degree is d and its exact exposed-rank profile is
    \boxed{(|C_1|,...,|C_d|)}.

**Necessity of closure.** On a current coordinate face, an exposing stress Z∈K-perp has PSD compression S and annihilates source, so Z_00=0 and the within-face source row vanishes. The kernel generator for each action implies
    Z_ii+2lambda Z_ab=0.
If an internal i has positive stress diagonal and both parents are still present, then Z_ab<0; PSD implies both parent stress diagonals are positive. Thus the exposed diagonal support is an all-actions closed set. Every PSD matrix's range is contained in its positive-diagonal support, so no exposing stress can remove vertices outside the largest closed set.

**Sufficiency for any closed C.** On C assign strictly positive stress diagonals S_ii=eta^(-w_i²), zero on other currently remaining vertices, and set each active parent-edge stress entry
    S_ab=-S_ii/(2lambda)
when i∈C and both parents remain; set it zero when i∉C. For actions whose parent edge has an already removed endpoint, use a freely adjustable OFF-FACE entry of the ambient dual stress to enforce the equation. Distinct action edges ensure consistency, and the independent optional leading edge enforces only a source-row zero relation. The closure property ensures both active parent endpoints belong to C. After diagonal normalization the magnitude of an active within-face offdiagonal is
    (1/(2lambda))eta^[(w_a²+w_b²)/2-w_i²].
Since w_i<= (w_a+w_b)/2 and w_a!=w_b (strictly increasing weights and a<i<b), the exponent is at least (w_a-w_b)²/4>0. For sufficiently small rational eta>0, all normalized offdiagonal row sums are <1/2; hence the compressed stress is positive definite on C and zero on the remaining coordinates. This realizes the full rank |C| with one stress. Greedy maximal-rank exposure is known to give minimal facial-reduction degree; induction proves the stated profile.

## Why the family is genuinely broader

A single-action midpoint pencil is the special case |A_i|=1 for all internal i. Adding an action at an existing vertex can preserve the Bellman weights if its parent average is greater than the old minimum (a *slack action*), while it changes the all-actions closure, delaying an exposing step. Thus **recovery exponent and facial depth respond to different combinatorial operations**, even though both are still exactly computable.

For an explicit six-by-six example that disproves simple one-action graph universality for full fixed-(nullity,degree) spectra, see checkpoint 58.

## Exact arithmetic and provenance

The Bellman problem is a finite proper stochastic-shortest-path problem; no numerical optimizer is needed. Both stability and facial degree have direct analytic proofs above. The companion exhaustive Fraction checker enumerates every collision-free multi-action selection on five internal/boundary vertices through target nullity five and verifies the novel exponent–degree triples. The program is reproducibility evidence rather than a substitute for the proof.

**Scope limitation:** This is a complete theorem for the **multi-action incidence family**, not a proof that *all dense PSD maps* admit an exponent/degree-preserving multi-action model. Its correctness already suffices to refute a smaller proposed combinatorial normal form. Standard Markov decision processes, facial reduction, and PSD principal-minor techniques are established tools; bibliographic priority of this precise normal form has not been audited.