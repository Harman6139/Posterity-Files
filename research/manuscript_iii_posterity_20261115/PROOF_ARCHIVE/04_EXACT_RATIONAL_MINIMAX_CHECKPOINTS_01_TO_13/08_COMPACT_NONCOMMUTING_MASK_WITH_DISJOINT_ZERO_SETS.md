# Checkpoint 08 — compact spectral masking can change the optimizer

Date: 2026-11-15. This is a sharp boundary example for checkpoint 06. It is not a dimension-growing query lower bound: the full oracle solves the example in one query.

## Theorem

For every d>=2 there are two explicitly rational, isometrically parametrized weakly infeasible PSD pencils with d+1 coordinates and order

    m=18(d+1)+2,

whose natural objectives f_+,f_- have the SAME values and gradients whenever the first d coordinates x satisfy ||x||>=27/10, but have disjoint small-objective regions. They satisfy the common beta=1/2 profile

    (1/2)s^(-1/2)<=rho_f(s)<=s^(-1/2), 0<s<=1/8,
    f_+(0,0)=f_-(0,0)=1/2+1/2400<1.

For objective tolerance epsilon<1/2400, any algorithm confined to those exterior queries has worst-case success at most 1/2, even with arbitrarily many calls and an unrestricted unqueried output. Under the ORIGINAL unrestricted oracle, one query suffices and zero queries cannot guarantee success greater than 1/2. Thus the distinction is genuine optimization-relevant masking, not global minimax hardness.

## 1. Exact moment data and radial cores

Let e be the first standard unit vector and define the two multisets of positive radii

    A=(9/10,3/2,3/2), B=(11/10,11/10,17/10).

They have the same moments of orders zero, one and two:

    |A|=|B|=3,
    sum A=sum B=39/10,
    sum_{r in A}r^2=sum_{r in B}r^2=531/100.

Put S_A(t)=sum_{r in A}(t-r)_+^2 and define S_B similarly. For t>=17/10,

    S_A(t)=S_B(t)=3t^2-(39/5)t+531/100.               (1)

Define, for theta in {-1,+1},

    G_theta(x)=[S_A(||x-theta e||)+S_B(||x+theta e||)]/24,
    f_theta(x,z)=G_theta(x)+phi(z),
    phi(z)=(sqrt(z^2+4)-z)^2/8.                      (2)

Every summand in G is a convex C1 squared distance to a Euclidean ball. If ||x||>=27/10, both center distances are at least 17/10. Equation (1) then makes G_+=G_-; their gradients also coincide, including at the boundary by the exact C1 formulas. Their z dependence is identical for every z.

The compact agreement claim concerns the x-core. After adding the unbounded tail, the disagreement set is a bounded x-region times the whole z-line; it is NOT claimed to be compact in the full coordinate space.

## 2. Disjoint zero sets and an objective separation

G_+(x)=0 exactly when

    ||x-e||<=9/10 and ||x+e||<=11/10.

The sum of the radii is the distance 2 between their centers. The triangle inequality is therefore an equality. The two balls are externally tangent and their intersection is the single point e/10. Similarly

    argmin G_theta={theta e/10}, min G_theta=0.       (3)

Moreover theta x_1<=0 implies ||x-theta e||>=1. The smallest A radius gives

    G_theta(x)>= (1/24)(1-9/10)^2=1/2400.            (4)

Thus epsilon<1/2400 success requires the correct sign of the first output coordinate.

## 3. Rational isometric affine pencil

For each radius r in A place THREE copies of the arrow block

    (1/6) [[r,(x-theta e)^T],[x-theta e,r I_d]]

in a block diagonal matrix. For each r in B do the same with x+theta e. There are 18 arrow blocks. Append W(z)=[[0,1],[1,z]]. This is an affine symmetric pencil with rational coefficients.

The unscaled arrow at radius r>0 and center c has eigenvalues

    r+||x-c||, r-||x-c||, r (multiplicity d-1).

Only the second can be negative. Its natural objective is (||x-c||-r)_+^2/2. Scaling by 1/6 and taking three copies gives the coefficient 3/(2*36)=1/24 required in (2).

For each x-coordinate, the derivative in one scaled arrow consists of two symmetric off-diagonal entries of size 1/6; its squared Frobenius norm is 1/18. Summing 18 blocks gives one. Distinct x-coordinate derivatives are orthogonal, and the z-direction has unit norm and disjoint support. Hence the complete chart is isometric.

For d>=2 the arrow direction matrices do not commute. For example the commutator of E_01+E_10 and E_02+E_20 is E_12-E_21, which is nonzero. Thus checkpoint 06's commuting/ridge-sum exterior theorem does not apply.

The W block forbids a PSD point for every finite (x,z). At x=theta e/10 all arrow blocks are PSD, while W(z) approaches the cone as z tends to infinity. Thus both affine spaces are genuinely weakly infeasible.

## 4. Normalization and all-scale escape

At x=0 every center distance is one. Only the radius 9/10 contributes, giving G_theta(0)=1/2400 and the displayed f(0).

If f_theta(x,z)<=s<=1/8, then phi(z)<=s, and

    z >= (2s)^(-1/2)-sqrt(2s) >= (1/2)s^(-1/2).

For the upper bound take x=theta e/10 and this same displayed z, so f=s. Its norm satisfies

    ||x||^2+z^2 <= 1/100+1/(2s) <=1/s.

This proves the common profile with constants independent of d and theta. The chart coefficients are fixed small rationals; order and ordinary explicit description size are polynomial in d. The norm of X0 is not uniform in d, nor required to be by the stated oracle class.

## 5. Exact information accounting

For a uniform hidden theta chosen before the algorithm's seed, all exterior-query transcripts are identical under the two instances. Any randomized unqueried output then has the same distribution under both. By (4) its success regions are disjoint at epsilon<1/2400, so average success is at most 1/2. A fair sign guess followed by the corresponding point (3) and a known accurate tail attains 1/2; unlimited exterior queries do not improve it.

At the origin,

    grad_x f_theta(0,0)=-(theta/120)e.

A single unrestricted gradient query therefore identifies theta, and (3) with a sufficiently large finite z gives any positive tolerance. Zero queries have the same disjoint-success-set lower bound 1/2. This proves the precise one-query statement.

## 6. What the example rules out

It would be false to extend either of these claims to all rational PSD-distance objectives:

(a) agreement at every sufficiently large x forces global equality;
(b) such exterior agreement forces a common core optimizer.

The pair (2) contradicts both. Conversely, exterior masking alone does not provide the requested T-query lower bound: its single interior gradient solves the pair. Constructing an optimization-relevant, polynomial-size sequence of such revelations without exponential energy loss remains a separate missing step.
