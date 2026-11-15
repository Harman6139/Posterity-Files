# Checkpoint 17 — the switching fast map and an exact neutral charge

Date: 2026-11-15. This is a proved description of the frozen leading map at a small-eigenvalue crossing. It explains a failure of the separated-chart proof at gamma=1. It is NOT a proof of the long-time behavior of the original gamma=1 DRS orbit: the frozen parameters move along that orbit, and their cumulative coupling remains to be controlled.

## 1. The uniform one-step model across a spectral crossing

Use the weighted coordinates of 16. Fix gamma>0, and set the symmetric leading variables to H0=sqrt(3)/4, b0=1/sqrt(3), (C,G)=Psi(H0,b0), chi=(3/4)eta. Let the scaled asymmetric variables z=(Ca,Ga,Q), j,xi,eta range over a fixed compact set. Define

 r=(3Q+4gamma Ca+8gamma Ga)/(3+8gamma^2),
 cf=2(Ca-Ga+gamma r)/3, gf=-cf/2+gamma r,
 p0=3xi^2, Lambda=2r-Q-3xi^2+sqrt(3)eta^2.

Then the leading asymmetric update of the ACTUAL PSD projection is the continuous piecewise-affine map

 F_gamma(z;j,xi,eta)=
 (cf+3j/2,
  [b0 Ga+(1-b0)gf+(j-xi*eta)/2]/(1+b0),
  Q+3xi^2+max(Lambda,0)-r).

The normalized one-step error is O(tau), uniformly on the compact set, including Lambda=0. Symmetric-target perturbations add errors tending to zero with those perturbations; no fixed-inertia assumption is made in this one-step statement.

The leading diagonal overlaps are

 v66/t^3=3xi^2+max(Lambda,0)+O(tau),
 s66/t^3=sqrt(3)eta^2+max(-Lambda,0)+O(tau).

### Proof of uniformity at zero

The two positive eigenvalues of orders t^-1 and t remain separated from zero, with positive middle Schur coefficient 1/8; the large negative eigenvalue is of order -t^-1. Their spectral subspaces have the same weighted analytic graphs used in 07 and 16, without deciding the sign of the remaining eigenvalue. The remaining eigenvalue is

 lambda_small=t^3 Lambda+O(t^5).

Its normalized eigenvector, with last coordinate positive, has coordinate orders (t^2,t,t^2,1) in (0,1,2,6). These orders follow directly by eliminating the large coordinates and then the positive middle coordinate; their denominators are b0, 1+b0 and 1/8, uniformly bounded away from zero. In particular its leading middle coordinate is -4t*xi.

The positive spectral part of the two already-positive eigenvalues contributes 3xi^2*t^3+O(t^5) in entry 66. The large negative spectral part contributes sqrt(3)eta^2*t^3+O(t^5) there. Adding the remaining spectral term uses the Lipschitz scalar function max(.,0), so the O(t^5) errors remain uniform at Lambda=0. The extra positive eigenvalue contributes only O(t^5) to entry 11, O(t^7) to entry 02, and O(t^6) to entry 12. It therefore changes the leading Q update but not the leading Ca or Ga update. This proves the displayed map and overlap formulas.

This proof uses a separated subspace for the three nonzero-scale eigenvalues and a scalar positive part for the crossing eigenvalue. It does not differentiate the PSD projection at a zero eigenvalue.

## 2. Firm nonexpansiveness of the frozen map

Equip R^3 with the inner product W=diag(2,4,1). Write M_- and M_+ for the linear parts of the Lambda<=0 and Lambda>=0 formulas. Both branches are affine, and they agree at Lambda=0.

Put

 ell=(1,(1-8gamma^2)/2,-2gamma)^T.

Direct multiplication gives the SAME rank-one defect for both branches:

 W-(2M_+-I)^T W(2M_+-I)
 =W-(2M_--I)^T W(2M_--I)
 =32(2sqrt(3)-3) ell ell^T/(3+8gamma^2)^2 >=0.

Hence 2F_gamma-I is nonexpansive on each halfspace. For two points on opposite sides, split their connecting segment at the crossing hyperplane, apply the two Lipschitz inequalities, and add their lengths. Continuity gives global nonexpansiveness. Therefore F_gamma is firmly nonexpansive in the weighted metric.

This is an exact statement about the explicitly displayed finite-dimensional frozen map, not a claim that moving spectral coefficients may be frozen for an infinite DRS trajectory.

## 3. Complete fixed-point classification

Define the scalar

 d=6gamma j+sqrt(3)eta^2.

Solving the first two fixed-point equations and the affine Gram identity gives, with a scalar r,

 Cfa=2sqrt(3)j+2gamma r+sqrt(3)xi*eta,
 Ca=Cfa+3j/2,
 Ga=gamma r-Cfa/2+3j/2,
 Q=r-6gamma j.

The remaining fixed-point equation reduces to

 r=3xi^2+max(r-3xi^2+d,0).

Consequently:

- If d<0, there is exactly one fixed point, obtained by r=3xi^2. Its small spectral coefficient is Lambda=d<0.
- If d=0, the fixed points form the ray given by every r>=3xi^2.
- If d>0, the frozen map has no fixed point.

Equivalently its fixed-point geometry is the complementarity system

 d<=0, r>=3xi^2, (r-3xi^2)d=0,

together with the affine formulas above. This is a nontrivial loss of uniqueness at the spectral crossing, not a harmless replacement of one smooth derivative by another.

## 4. The neutral charge and global frozen dynamics

Let n_gamma=(2gamma,0,1)^T and define

 C_gamma(z)=n_gamma^T W z=4gamma Ca+Q.

The positive branch fixes n_gamma in its linear part. More precisely, for the full frozen map,

 C_gamma(F_gamma z)-C_gamma(z)=d+max(-Lambda,0).       (4.1)

The proof is substitution: for Lambda>=0 the increment is

 4gamma(cf+3j/2-Ca)+(r-Q+sqrt(3)eta^2)=d,

because (3+8gamma^2)r=3Q+4gamma Ca+8gamma Ga. Switching to the other branch subtracts Lambda, giving (4.1).

For d<=0, firm nonexpansiveness and the nonempty fixed set imply convergence of every frozen orbit to a fixed point. Indeed the standard squared-distance expansion gives Fejer decrease and summability of squared increments; every cluster point is fixed, and Fejer monotonicity to such a cluster point forces convergence of the entire finite-dimensional orbit. For d<0 the limit is the unique fixed point; eventually the orbit lies strictly in the negative branch, where the weighted Gram defect of 16 gives geometric convergence.

For d>0, every frozen orbit has the explicit common drift

 F_gamma^k(z)/k -> [d/(8gamma^2+1)] n_gamma.           (4.2)

Here is a proof without appealing to an unidentified minimal-displacement theorem. The fixed space of M_+ is exactly span(n_gamma), as follows from the homogeneous fixed equations. Since M_+ is firmly nonexpansive, it is strictly contractive on the W-orthogonal complement of that line, which it preserves. Write F_+(z)=M_+z+f. Its charge increment is d, so with c=d/(8gamma^2+1), the equation

 (I-M_+)w=f-c*n_gamma

has a solution on that complement. Add a large multiple of n_gamma to w so Lambda(w)>=0. Since Lambda has directional derivative one along n_gamma, the points w+k*c*n_gamma stay in the positive branch and form an exact affine-ray orbit of the FULL frozen map. Nonexpansiveness keeps any other orbit at bounded distance from this ray. Dividing by k proves (4.2).

Thus all three frozen regimes are determined exactly. At the boundary the fast contraction loses a direction; above it, that direction acquires a nonzero drift. This is the missing mode in a naive extension of the separated gamma=2 proof to gamma=1.

## 5. What this establishes for the original route

The smooth periodic target of 16 has j_gamma=-S_gamma/(6gamma), so its gap is

 d_target=-(S_gamma-sqrt(3)eta^2).

At gamma=1 and xi=0, eta!=0,

 S_1=(sqrt(3)/2)eta^2,
 d_target=(sqrt(3)/2)eta^2>0.

The putative smooth target would therefore pass through phases where the actual frozen fast map has NO equilibrium. Its neutral charge then drifts rather than tracking a stationary fast point. It is mathematically invalid to extend the gamma=2 stable-fast-manifold proof through these phases by continuity alone.

A successful analysis of the actual gamma=1 orbit must control the coupled motion of j, the phase, and the neutral charge (4.1), including passages through d=0. The one-step O(tau) error need not have a summable total; the frozen drift theorem does not settle the moving-parameter orbit. No conclusion of persistent oscillation or eventual damping for the original rational start is asserted here.

The exact script switching_fast_map.py checks the fixed-direction, charge and rank-one defect identities. The conclusions in Sections 2–4 are proved algebraically above; the computation is corroboration.
