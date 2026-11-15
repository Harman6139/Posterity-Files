# Checkpoint 04 — balanced rational SDP: geometry proved, dynamics unresolved

Date: 2026-11-15. This is a research checkpoint, not a completed manuscript or a counterexample certificate.

## Status

The arbitrary-order plain Douglas–Rachford last-step theorem remains neither proved nor disproved in this attempt. Checkpoints 01–03 at remote commit `2d1f975c4a0ecd3ec6b47baeee3be33639ad0118` remain the authoritative previous results. This continuation's newest files have not been pushed to GitHub.

## Exact balanced construction

Use indices 0,...,6, Eii for a diagonal unit, and Fij=Eij+Eji. For positive rational gamma put

    a=-(F01+F34)/2,
    L=span{E00+E33, E11-F02/2, E44-F35/2,
           E66+gamma(F02-F35), F06, E22-E55},
    U=a+L.

Equivalently its free parameters A,c,d,r,u,h give

    X00=X33=A, X11=c, X44=d, X66=r,
    X22=h, X55=-h,
    X02=-c/2+gamma*r, X35=-d/2-gamma*r,
    X01=X34=-1/2, X06=u,

with symmetric counterparts and all other entries zero. All projections use the Frobenius metric. The actual iteration is plain unanchored DRS.

### Proposition: weak infeasibility and escape exponent 1/3

An exact PSD member has h=-(-h)=0 because both X22 and X55 are nonnegative. The zero diagonal entries force rows 2 and 5 to vanish. Thus c=2 gamma r and d=-2 gamma r. Since c,d,r are nonnegative and gamma>0, c=d=r=0. The zero row at index 1 contradicts X01=-1/2. Hence U has no PSD member.

For t>0 take two identical three-by-three PSD blocks

    [[1/(2t), -1/2, -t/2],
     [-1/2,   t,      0 ],
     [-t/2,   0,     t^3]],

and a zero seventh row/column. PSD follows from the Schur complement: the top diagonal equals (1/4)/t+(t^2/4)/t^3. This path satisfies every displayed affine equation except X22+X55=0, whose residual is 2t^3. Its trace is 1/t+2t+2t^3. This proves weak infeasibility and the upper escape estimate O(delta^(-1/3)).

For the converse choose a fixed rational equality description that includes

    X22+X55=0, X34=-1/2,
    X44+2X35+2 gamma X66=0.

A PSD competitor with each of these residuals at most delta, 0<delta<=1/4, satisfies

    0<=X55<=delta, |X34|>=1/4,
    d+2 gamma r<=2|X35|+delta<=2 sqrt(B delta)+delta,

where B=X33, d=X44, r=X66 are nonnegative. Consequently

    1/16<=B d<=2 B^(3/2) sqrt(delta)+B delta.

If B<(1/64)delta^(-1/3), the right side is at most

    2(1/64)^(3/2)+(1/64)delta^(2/3)<=5/256<1/16,

a contradiction. Therefore trace(X)>=B>=(1/64)delta^(-1/3). Norm equivalence gives the same exponent for every fixed norm on any equivalent equality description. The escape exponent is exactly alpha=1/3. By the inherited common-state theorem, its plain DRS exponent is p=1/4.

### Invariant reference subspace

States made of two identical three-by-three blocks and a zero seventh row remain in that form under both projections. The symmetric pair of arrow directions has zero aggregate Gram pairing with E66+gamma(F02-F35), while E22-E55 and F06 pair to zero. Projection onto the direction space therefore gives identical affine arrow blocks and zero seventh row. The PSD projection preserves identical blocks. Nonexpansiveness bounds the distance of a perturbed orbit to the reference orbit by the initial distance. This controls the leading state, not its last differences.

## Numerical records verified from saved arrays

The driver uses double-precision symmetric eigendecomposition and an orthonormalized Frobenius basis of L. The start is

    Z0=a+epsilon F06+(3 epsilon/10) F26, gamma=1.

For epsilon=1/10, the stored data record:

| Iterations N | N^(1/4) times transverse column norm | N^(3/4) times transverse last-step column norm |
|---:|---:|---:|
| 200000 | 0.03134001188148402 | 0.02063248729731429 |
| 2000000 | 0.03247988448852342 | 0.02137588613185579 |
| 6000000 | 0.03300474085790027 | 0.02172003748208494 |

The transverse column is rows 0,...,5 of column 6; a symmetric matrix's Frobenius contribution counts it twice. Samples use the pre-update state and the corresponding step for the Nth update, with scale N; this harmless indexing convention is recorded explicitly.

At N=6000000 the recorded total scaled state norm is 1.50980211996822 and the total scaled step norm is 0.37875820682041716. Other stored starts at N=2000000 have transverse scaled state amplitudes 0.0048492545352295125 (epsilon=1/100) and 0.04587844922873212 (epsilon=1/2).

These are finite floating-point observations, not interval certificates, not a proof of a nonzero limiting amplitude, and not evidence that longer-time damping has been excluded.

## Exact missing analysis

A disproof still requires an exact nonlinear asymptotic argument showing, for an explicit initial state, that the transverse component of N^(3/4)(Z_N-Z_(N-1)) fails to vanish. A moving linearization alone is insufficient. It must control the small-eigenvalue regime, quadratic diagonal feedback, all accumulated remainders, and a nonzero transverse asymptotic amplitude or a rigorous positive limsup.

A positive universal theorem still requires a PSD-geometric reason that actual cone shadows asymptotically saturate the sharp residual-versus-size profile. The earlier exact saturation equivalence does not prove its own hypothesis.

No complete originality assessment, submission-ready manuscript, or upper-quintile journal benchmark is certified. Those gates have not been met.
