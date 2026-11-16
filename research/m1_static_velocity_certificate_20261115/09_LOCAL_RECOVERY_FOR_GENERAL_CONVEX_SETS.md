# Checkpoint 09 — the local recovery theorem does not require a cone

Date: 2026-11-15. This strengthens Checkpoint 01 to an arbitrary closed convex semialgebraic set paired with an affine space. The new observation is that the central-path balance follows from projection normality, not cone complementarity. No claim that all raw last steps converge is made.

## 1. General convex-set theorem

Let C be a nonempty closed convex semialgebraic subset of a finite-dimensional Euclidean space. Let U=a+L, a perpendicular to L, satisfy U intersect C empty and dist(U,C)=0. Run the ORIGINAL plain affine-first iteration

    Tz=z+P_C(2P_Uz-z)-P_Uz, z_(k+1)=Tz_k.

Set P=P_L, Q=I-P, x_k=Pz_k, y_k=Qz_k-a, v_k=P_C(a+x_k-y_k). There exist nonzero H,G and rational 0<p<1, independent of the start, such that V=H+G, H=PV, G=QV and

    z_k=V k^p+O(k^(p-eta)), eta>0,
    ||H||^2=(1-p)||V||^2, ||G||^2=p||V||^2.         (1.1)

The static distance profile, finite for all sufficiently large r, is

    D_C(r)=min{||Qv-a||: v in C, ||Pv||<=r}.

It satisfies

 D_C(r)=p||G|| ||H||^((1-p)/p) r^(-(1-p)/p)
                                      (1+O(r^(-kappa))), kappa>0. (1.2)

For h/n~1/log n, define the centered positive average of the ACTUAL C-shadows

    vbar_n=(1/(2h))sum_(j=n-h)^(n+h-1)v_j in C.

Then

    n^(-p)P vbar_n -> H,
    n^(1-p)(Q vbar_n-a) -> pG,
    (log n)^2 [||Q vbar_n-a||/D_C(||P vbar_n||)-1]
                                                ->(1-p)/6.       (1.3)

The centered mean velocity has limit pV at scale n^(1-p). All quantitative secant expansions, the constant-storage block implementation, and the redundant-equation residual conclusions in Checkpoint 01 remain valid, with C in place of K. Neither self-duality nor homogeneity of the constraint set is required.

## 2. The common state and the one identity that changes

The map T is firmly nonexpansive and semialgebraic. A fixed point would give a point of U intersect C. Approximate affine points approaching C give arbitrarily small displacements. Hence the inherited tame fixed-point theorem applies and supplies the first state in (1.1), including a positive-power remainder.

Let z(t) be the unique discounted point with anchor a:

    Tz(t)-z(t)=(z(t)-a)/t.

Write z(t)=a+x(t)+y(t). Its reflected point is a+x-y and its C-projection is

    v(t)=a+(1+1/t)x(t)+y(t)/t.

Put

    s(t)=x(t)/t+(1+1/t)y(t).

Projection optimality says -s(t) belongs to N_C(v(t)). For fixed t and every small positive or negative h,

    <s(t),v(t+h)-v(t)> >= 0.

The one-variable semialgebraic path is smooth on a tail, so differentiating this function AT ITS MINIMUM gives

    <s(t),v'(t)>=0.                                (2.1)

Unlike the cone case, <v(t),s(t)> need not vanish, and <a,y(t)>=-E(t)/t is generally FALSE. That cone-specific identity is not used here.

Let E(t)=||x(t)||^2+||y(t)||^2. Direct substitution into (2.1), using P/Q orthogonality, gives EXACTLY

    t(t+1)E'(t)/2=E(t)+t||y(t)||^2.                (2.2)

The discounted-path leading coefficient is p^p V. Comparing the leading Puiseux terms in (2.2) proves the two norm balances in (1.1), and in particular H,G are both nonzero. Only the smooth central path, never the actual orbit remainder, has been differentiated.

## 3. The same static optimizer

For fixed t, the point v(t) uniquely minimizes over C

    F_t(v)=||Pv||^2/[2(t+1)^2]+||Qv-a||^2/2.

Indeed its gradient at v(t) is s(t)/(t+1), and (2.1)'s underlying normal inclusion gives -grad F_t(v(t)) in N_C(v(t)). This is the convex optimality condition. Positive weights make F_t strictly convex and coercive.

Consequently

    D_C(||Pv(t)||)=||Qv(t)-a||.

A smaller residual at no larger P-radius would contradict the quadratic minimization. The radius ||Pv(t)|| has a positive leading power and is eventually strictly increasing by one-variable semialgebraic regularity; its values cover a tail. Eliminating t gives the leading coefficient in (1.2). Semialgebraicity supplies the positive-power remainder.

For completeness, the profile minima exist whenever finite: bounding its objective and P-radius bounds both orthogonal components, so a minimizing sequence is bounded. A zero minimum at finite radius would yield a feasible point. Its limit is zero as r tends to infinity because dist(U,C)=0. There is no need to define it as finite at radii smaller than the minimum P-radius of C.

## 4. Local averaging

The exact identity

    v_k=a+x_(k+1)+(y_(k+1)-y_k)

is valid for every affine–convex pair, with no cone assumption. Therefore its centered mean has the same primal mean and normal secant as in Checkpoint 01. The quantitative state remainder, scalar Taylor expansion and the exact profile coefficient prove (1.3), word for word. Convexity of C makes the positive average feasible for C itself.

Thus the algorithm recovers asymptotically best radius-versus-equation-distance points for nonlinear convex constraints as well as conic constraints. This is a statement about genuine local shadow outputs of plain DRS, not an anchored iteration or alternating projections.

## 5. Nonconic application: every inverse-power epigraph

Fix a positive rational q and consider in R^2

    C_q={(x,y): x>0, y>=x^(-q)},
    U={(x,0):x real}.

C_q is closed, convex and semialgebraic: x^(-q) is convex on the positive axis and diverges at zero. The pair is disjoint at distance zero. Its exact profile is

    D_C(r)=r^(-q), r>0.

The theorem implies p=1/(q+1). The positive leading coefficients satisfy h^2=q g^2 and p g h^q=1, hence

    h=[sqrt(q)(q+1)]^(1/(q+1)),
    g=h/sqrt(q), V=(h,g).

For this entire nonconic family the RAW last-step law also follows directly from the projection equations, rather than from averaging. After one step the state has x>0 and y>=0. To see y_next>=0, note that a projection onto an upward-closed epigraph cannot have vertical coordinate smaller than that of the point being projected. Thereafter the reflected point (x,-y) lies below the epigraph, and its projection is a boundary point (x_next,x_next^(-q)). First-order minimization yields exactly

    y_next-y=x_next^(-q),
    x_next-x=q y_next/x_next^(q+1).

Inserting the PROVED state limits, not differentiating them, gives

    k^(1-p)(z_(k+1)-z_k)->p(h,g)

from every start. The local-averaging efficiency constant in (1.3) is q/[6(q+1)].

This is an actual nonlinear convex-set projection problem in dimension two, not a substitution of alternating projections for the required DRS map. It illustrates the broader reach of the central-profile balance and output-recovery theorem.

## 6. Scope boundary

The raw general last-step problem is not solved for all affine–convex pairs. The static excess/kinetic identity of the earlier CONIC checkpoints is also not asserted unchanged for nonconic sets: its cross-complementarity energy uses structure absent here. What transfers is the common state, central-path norm balance, exact static profile and sharp local recovery. These are enough for the algorithmic conclusion in (1.3).
