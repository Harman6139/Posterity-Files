# Milestone 28 — exact escape-controlled rates for Halpern iteration and anchored Douglas–Rachford

Date: 2026-11-13. Parent research snapshot: 415ac86b4a6031e73e37a320f305fb20a921bdce.

## Status and scope

This establishes matching residual and iterate-growth powers for a specified anchored fixed-point iteration whenever approximate fixed points have a power-law minimum radius. For semialgebraic nonexpansive maps with no fixed point and infimal displacement zero, such a positive rational power always exists. An exact geometric identity connects the Douglas–Rachford fixed-point radius to the primal feasibility radius when one set is affine. This gives two-sided rates for anchored Douglas–Rachford on EVERY weakly infeasible SDP.

The Halpern algorithm, its potential, and upper residual comparison are established ingredients. Park–Ryu, Accelerated Infeasibility Detection of Constrained Optimization and Fixed-Point Iterations, arXiv:2303.15876, Theorems 7–8, proves closely related explicit bounds. They must not be represented as newly invented here. The argument below is self-contained: the classical potential plus an elementary comparison-radius inequality yields BOTH bounds from a static escape profile. The specific primal/operator profile equality is proved in Section 4.

These results do NOT prove exact rates for plain, unanchored Douglas–Rachford, every ADMM variant, or stochastic/inexact projections. Exploratory floating-point agreement for unanchored DRS is not a proof and is not used. No named open-conjecture resolution or guarantee about publication is asserted.

## 1. The fixed-point escape profile

Let T:R^d->R^d be nonexpansive:

    ||T(x)-T(y)||<=||x-y||.

Assume Fix T is empty but inf_x ||x-T(x)||=0. For an anchor x0 define

    R_T(epsilon)=min{||u-x0||:||u-T(u)||<=epsilon}.

The minimum is finite and attained for every epsilon>0. Continuity makes the feasible set closed; norm coercivity gives attainment. If the minima stayed bounded along epsilon->0, a subsequence would give a fixed point. Therefore R_T diverges.

Suppose

    c epsilon^(-a)<=R_T(epsilon)<=C epsilon^(-a)

for sufficiently small epsilon, where a>0. If T is semialgebraic this hypothesis holds for some positive rational a: the profile is semialgebraic by quantifier elimination, and its divergence gives the negative leading rational power. Changing the anchor changes the profile by at most a constant, so the exponent does not change.

## Theorem A — exact anchored rates

Starting from x0, run

    x_(k+1)=[x0+(k+1)T(x_k)]/(k+2),  k>=0.            (1)

Then, for EVERY anchor x0,

    ||x_k-T(x_k)||=Theta(k^(-1/(a+1))),
    ||x_k-x0||=Theta(k^(a/(a+1))).                     (2)

The constants and asymptotic onset are instance dependent. The updates do not use a or any approximate-fixed-point oracle. Only one T evaluation is needed per step.

This is not a claim that every nonexpansive map has a power profile, or that its iterates are themselves a semialgebraic sequence. The profile hypothesis is automatic in the finite-dimensional semialgebraic case described above.

## 2. A classical potential, proved directly

Put d_k=x_k-T(x_k), v_k=x_k-x0, and

    W_k=(k+1)[k||d_k||^2+2<d_k,v_k>].

Then W_0=0 and W_(k+1)<=W_k for every k. To verify it, put m=k+1 and Delta=x_(k+1)-x_k. The update gives

    v_(k+1)=m(v_k-d_k)/(m+1),
    v_k=-(m+1)Delta-m d_k.

Let e=d_(k+1)-d_k. A direct expansion gives

    W_(k+1)-W_k=m(m+1)(||e||^2-2<Delta,e>).

Nonexpansiveness gives

    ||Delta-e||^2=||T(x_(k+1))-T(x_k)||^2<=||Delta||^2,

so the displayed difference is nonpositive. Therefore, for k>=1,

    k||d_k||^2<=-2<d_k,v_k><=2||d_k||||v_k||,
    ||d_k||<=2||v_k||/k.                             (3)

The last division is harmless: d_k cannot vanish because T has no fixed point.

## 3. Approximate comparators give both rate directions

For any u with ||u-T(u)||<=epsilon, put R=||u-x0||. Nonexpansiveness and (1) imply

    ||x_(k+1)-u||
      <=R/(k+2)+(k+1)(||x_k-u||+epsilon)/(k+2).

Induction gives

    ||x_k-u||<=R+k epsilon/2.

Thus, for every epsilon>0,

    ||x_k-x0||<=2 R_T(epsilon)+k epsilon/2,             (4)
    ||d_k||<=4 R_T(epsilon)/k+epsilon.                 (5)

These finite-horizon inequalities do not need a power law. In the power case choose epsilon=k^(-1/(a+1)). They give

    ||x_k-x0||<=C1 k^(a/(a+1)),
    ||d_k||<=C2 k^(-1/(a+1)).

The lower bounds follow from the defining geometric constraint

    R_T(||d_k||)<=||x_k-x0||.                         (6)

Use the lower profile estimate with the upper iterate bound to obtain the residual lower bound. Use it with the residual upper bound to obtain the iterate lower bound. This proves (2).

The method is therefore automatically power-adaptive on this class. It does not imply minimax optimality for all nonexpansive-oracle algorithms; the deterministic minimax theorem in 27 concerns a different, smooth objective-value oracle model.

## 4. Douglas–Rachford has exactly the primal radius profile

Let U be a nonempty closed affine subspace, V a nonempty closed convex set, and assume

    U intersect V is empty, dist(U,V)=0.

Define the Douglas–Rachford map

    T(z)=z+P_V(2P_U z-z)-P_U z.                       (7)

It is nonexpansive: write it as (I+R_V R_U)/2, where R_U=2P_U-I is an affine isometry and R_V=2P_V-I is nonexpansive by the projection inequality. A fixed point would make P_U z=P_V R_U z lie in U intersect V, so none exists.

Fix x0 in U and define the primal radius profile

    R_(U,V)(epsilon)=min{||u-x0||:u in U,
                                     dist(u,V)<=epsilon}.

## Theorem B — exact identity

    R_T(epsilon)=R_(U,V)(epsilon) for every epsilon>0.  (8)

Proof: if u belongs U then R_U u=u and T(u)=P_V u. Thus every primal comparator is an operator comparator at the identical radius and residual, giving R_T<=R_(U,V).

Conversely, from any z with ||z-Tz||<=epsilon, put u=P_U z and v=P_V R_U z. Then

    u in U, v in V, ||u-v||=||z-Tz||<=epsilon,
    ||u-x0||<=||z-x0||

because x0 is in U. Hence R_(U,V)<=R_T. QED.

If the anchor is outside U, comparing to its projection changes the inequalities by at most the fixed distance dist(x0,U), so the escape exponent is still identical.

If U,V are semialgebraic, their projections and T are semialgebraic (their graphs are described by unique metric minimization). A positive rational exponent a therefore exists, and Theorem A yields

    fixed-point residual=Theta(k^(-1/(a+1))),
    state norm=Theta(k^(a/(a+1))).                      (9)

This identity uses the AFFINENESS of U. It is not asserted for arbitrary pairs of nonlinear convex sets.

## 5. The actual feasibility shadows have the same rates

Let z_k be the anchored iterates for (7), and set

    u_k=P_U z_k,
    v_k=P_V(2u_k-z_k).

Their discrepancy is exactly

    ||u_k-v_k||=||z_k-Tz_k||.

Thus dist(u_k,V)<=||z_k-Tz_k||. Also ||u_k-x0||<=||z_k-x0|| when x0 in U. By the primal profile lower bound,

    c dist(u_k,V)^(-a)<=R_(U,V)(dist(u_k,V))
                            <=||u_k-x0||
                            <=C k^(a/(a+1)).

Therefore dist(u_k,V)=Theta(k^(-1/(a+1))). Applying the same profile to the residual upper bound shows ||u_k-x0||=Theta(k^(a/(a+1))). Since ||u_k-v_k||->0, v_k has the same diverging norm order. The nearest point P_V u_k has it as well.

Hence the theorem is not only a fixed-point-residual statement: it controls the actual primal feasibility error and primal size.

## 6. Every weakly infeasible SDP and SOCP

Let A:S^m->R^p and b define a weakly infeasible SDP. Put U={Z:A(Z)=b}, V=S_+^m. The affine set is nonempty because b lies in the closed linear space range A. The problem is disjoint at distance zero.

If

    R_b(delta)=min{tr X:X>=0,||A(X)-b||<=delta}
               =Theta(delta^(-a)),

then R_(U,V) has the same exponent. To prove this, choose a right inverse L of A on its range. A PSD X of equation residual delta gives the affine point X+L(b-A(X)), within ||L||delta of the PSD cone and with norm at most trX+O(delta). Conversely project an affine point onto PSD; its equation residual is at most ||A|| times the projection distance and its trace is at most sqrt(m) times its Frobenius norm. These comparisons are uniform up to fixed factors and additive constants, which do not alter a diverging power.

The anchored algorithm, using one affine and one PSD projection per iteration, therefore satisfies

    ||z_k-Tz_k||=Theta(k^(-1/(a+1))),
    dist(u_k,S_+^m)=Theta(k^(-1/(a+1))),
    ||A(v_k)-b||=Theta(k^(-1/(a+1))),
    tr v_k=Theta(k^(a/(a+1))).                        (10)

For the original equation residual, the upper bound follows from ||A(v_k)-b||<=||A|| ||v_k-u_k||. The lower bound follows from R_b(||A(v_k)-b||)<=tr v_k and the established upper trace-growth rate. This argument does not assume that a small fixed-point residual alone certifies infeasibility.

Project manuscript 12 proves the sharp order-m escape envelope

    1/(2^(m-1)-1)<=a<=2^(m-1)-1, m>=2,

with rational endpoint examples. Subject to that explicitly identified theorem, the exact residual exponent gamma of anchored DRS has sharp interval

    2^(-(m-1))<=gamma<=1-2^(-(m-1)).                  (11)

Both endpoints occur at every m. In particular EVERY order-two weakly infeasible SDP has anchored residual Theta(k^(-1/2)) and state/PSD trace growth Theta(k^(1/2)).

For a product of PSD blocks of orders d_j, h nonpolyhedral Lorentz cones, and scalar cones, manuscripts 15–16 use B=sum_j(d_j-1)+h and give the same formula with m-1 replaced by B. With one Lorentz factor and any finite number of scalar inequalities, a=1 and the half-power residual/state laws follow independently of Lorentz dimension.

All constants and thresholds are instance dependent. The iteration count to reach residual delta is Theta(delta^(-(a+1))) for a fixed instance. This is not a polynomial-bit decision algorithm for weak infeasibility, or a lower bound on every possible solver.

## 7. What this changes and what remains open here

The original comparison in 26 was ordinary alternating projections versus a particular accelerated gradient projection method. The new conclusion gives the SAME improved powers to the simple anchor iteration of the standard Douglas–Rachford map, and controls its fixed-point residual, actual primal shadows and divergence.

Infeasibility work by Liu–Ryu–Yin (arXiv:1706.02374; Mathematical Programming 177, 2019) shows that vanishing displacement and diverging states identify weak infeasibility asymptotically. Park–Ryu (arXiv:2303.15876) establishes accelerated residual bounds using approximate displacement points. The radius identity (8) and two-sided use of (6) give the precise geometric power in this weakly infeasible, zero-displacement regime.

Nothing here proves that the plain DRS iterates z_(k+1)=Tz_k have the same exponent. Experiments suggest that for the particular endpoint systems, but that conjectural extension is explicitly excluded. ADMM equivalence also requires specifying the reformulation and the corresponding anchoring; no blanket assertion about every ADMM implementation is made.

Likewise there is no randomized lower bound, finite-precision stopping certificate, uniform source conditioning, or publication guarantee. The proof establishes the displayed exact-arithmetic rate laws.

## References

1. J. Park and E. K. Ryu, Accelerated Infeasibility Detection of Constrained Optimization and Fixed-Point Iterations, arXiv:2303.15876, especially Theorems 7–8 and the Halpern potential in Appendix B.2. https://arxiv.org/html/2303.15876
2. Y. Liu, E. K. Ryu, and W. Yin, A New Use of Douglas–Rachford Splitting and ADMM for Identifying Infeasible, Unbounded, and Pathological Conic Programs, arXiv:1706.02374. https://arxiv.org/html/1706.02374
3. Project manuscripts 12, 15–16 and 26 at the parent snapshot: declared dependencies for the sharp dimensional envelopes, not premises for Theorems A and B.

The source potential is attributed, not claimed new. Historical priority for the full profile formulation and its particular SDP consequences has not been exhaustively established.
