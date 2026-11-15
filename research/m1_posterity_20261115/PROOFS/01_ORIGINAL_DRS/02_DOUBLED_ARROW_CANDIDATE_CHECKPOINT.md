# Checkpoint 02 — a rational order-seven transverse-mode candidate

Date: 2026-11-14. Status: the affine construction and escape exponent below are proved. The proposed oscillatory last-step behavior is a NUMERICAL OBSERVATION AND RESEARCH HYPOTHESIS, NOT an established counterexample. The universal theorem remains unresolved at this checkpoint.

## Exact rational affine space

Use indices 0,...,6. Fix a positive rational gamma (the diagnostic uses gamma=1). Define U_gamma in S^7 by the following parametrization, with A,B,c,d,r,u arbitrary real numbers:

    X00=A, X33=B, X11=c, X44=d, X66=r,
    X02=X20=-c/2+gamma*r,
    X35=X53=-d/2-gamma*r,
    X01=X10=X34=X43=-1/2,
    X06=X60=u,
    all other entries zero.

Thus U_gamma=a+L_gamma, where a=-(F01+F34)/2, Fij=Eij+Eji, and L_gamma is spanned by

    E00, E33, E11-F02/2, E44-F35/2,
    E66+gamma(F02-F35), F06.

All projections in the proposed example are the original Frobenius orthogonal projections. No nonorthogonal change of metric or algorithm is intended.

## Proved: weak infeasibility

An exact PSD member would have X22=X55=0. PSD zero-row propagation gives X02=X35=0, hence c=2gamma*r and d=-2gamma*r. Since c,d,r are nonnegative, they all vanish. Then X11=0 forces X01=0, contradicting X01=-1/2. Thus U_gamma is disjoint from S_+^7.

For t>0, use two identical 3-by-3 blocks on indices (0,1,2) and (3,4,5), with

    Y00=1/(2t), Y11=t, Y22=t^3,
    Y01=-1/2, Y02=-t/2, Y12=0,

and zero row/column 6. The leaf Schur sum is (1/4)/t+(t^2/4)/t^3=1/(2t), so both blocks are PSD. All defining equations hold except the two final-diagonal equations, whose residuals are t^3. Therefore distance to U_gamma tends to zero.

## Proved: escape exponent alpha=1/3

The displayed path has trace 1/t+2t+2t^3, proving R_b(delta)=O(delta^(-1/3)) for any fixed norm on the equality residual space.

For the converse, use an equality description containing X55=0, X34=-1/2, and X44+2X35+2gamma*X66=0. If a PSD competitor has all these residuals at most delta, then with B=X33, d=X44, r=X66,

    0<=X55<=delta,
    |X34|>=1/4 for delta<=1/4,
    d+2gamma*r<=2|X35|+delta<=2sqrt(B delta)+delta.

Since r>=0, PSD of the (3,4) principal minor gives

    1/16 <= B d <= 2 B^(3/2) sqrt(delta)+B delta.

For sufficiently small delta this implies B>=c0 delta^(-1/3), with a fixed positive c0 (choose c0 small enough that 2c0^(3/2)+c0<1/16). Hence trace is at least that large. Norm equivalence handles any other fixed equality residual norm. Thus alpha=1/3 exactly.

By the inherited semialgebraic common-state theorem, plain DRS for this system has p=alpha/(1+alpha)=1/4, from every start.

## Invariant doubled-arrow orbit

The subspace consisting of two identical 3-by-3 state blocks and a zero seventh row/column is invariant under the affine projection and PSD projection. The added direction E66+gamma(F02-F35) has zero pairing with equal blocks, and its mixed Gram terms with the two symmetric arrow directions cancel. Thus the unperturbed orbit reduces to two identical order-three slow-arrow DRS problems.

Any other orbit is at bounded distance from this invariant orbit, by nonexpansiveness. It therefore has the same leading state. This does NOT by itself control the leading last step.

## Diagnostic and candidate mechanism

The diagnostic starts from the rational matrix

    Z0=a+(1/10)F06+(3/100)F26,

with gamma=1. It runs exactly the specified plain DRS formula, implemented with floating-point eigendecomposition and Frobenius projection onto the displayed six-dimensional direction space.

At k=200000 it recorded approximately:

    ||Z_k||/(k+1)^(1/4) = 1.5097779615,
    ||d_k||*(k+1)^(3/4) = 0.3786908955,
    ||(Z_k)_[0:6,6]||*(k+1)^(1/4) = 0.0280149490,
    ||(d_k)_[0:6,6]||*(k+1)^(3/4) = 0.0184457127.

The scaled off-diagonal state vector rotates, and its scaled amplitude changes little over the recorded late window. These are NOT exact-arithmetic certificates, asymptotic proofs, or guarantees against a longer transient. The vector norms here count one off-diagonal column, not both symmetric copies; the corresponding Frobenius contribution has an extra factor sqrt(2).

The candidate mechanism is a moving principal angle between a primal off-diagonal direction and the positive spectral subspace of a diverging arrow block, coupled to a degenerate zero eigenvalue. The antisymmetric diagonal direction is intended to keep the added diagonal at zero on the invariant orbit and allow quadratic feedback under perturbation. A rigorous nonlinear asymptotic normal form, remainder control, and a nonzero limiting transverse amplitude are still missing.

## Required next verification

1. Independently check affine projections, complementarity identities, and numerical stability.
2. Derive the invariant order-three orbit's exact coefficient and quantitative remainders.
3. Prove or disprove persistence of the added rotating mode; in particular exclude a long transient followed by decay.
4. Only if persistence is rigorously established, pair the explicit SDP disproof with the universal saturation equivalence in Checkpoint 01 and a substantive structural analysis.

No last-step disproof, full closure, publication readiness, originality certification, or journal-percentile assertion is made here.
