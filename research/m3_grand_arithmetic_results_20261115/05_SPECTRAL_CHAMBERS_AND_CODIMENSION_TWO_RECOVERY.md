# Checkpoint 05 — spectral chambers, codimension-two recovery, and the boundary of germ identification

Date: 2026-11-15. This sharpens checkpoint 02. The original rational exact OPTIMIZATION frontier remains unresolved; the global-identification bounds below must not be substituted for it.

## 1. The rank-drop set is an explicit algebraic object

For a rational affine symmetric pencil X_a(x) of order m, let r_a be its maximum rank on R^d. Define

   Sigma_a={x:rank X_a(x)<r_a}.

When r_a=0, set Sigma_a empty. Otherwise Sigma_a is the common zero set of all r_a-by-r_a minors. Equivalently it is the zero set of the rational polynomial

   D_a(x)=sum_M det(M(x))^2,

where M runs over those minors. This polynomial is nonzero and has degree at most 2m. Therefore Sigma_a is closed, semialgebraic, and has empty interior. It is not the locus of repeated nonzero eigenvalues: such repetitions do not obstruct analyticity of the negative spectral projector.

On R^d\Sigma_a the natural objective f_a=dist_F(X_a,S_+)^2/2 is real analytic, by the spectral-projector proof in checkpoint 02. The matrix rank and inertia are constant on each connected component there. The set and its dimension are effectively computable from rational coefficients by real algebraic algorithms.

## 2. Pairwise continuation theorem

THEOREM A. Let a,b be two rational pencils of the same declared order and coordinate dimension. Let q be the algebraic germ probe constructed in checkpoint 02. If f_a(q)=f_b(q), then the functions agree on the ENTIRE connected component of

   R^d \ (Sigma_a union Sigma_b)

containing q. The analogous statement holds for their gradients. If this complement is connected, value equality at q implies global equality of objectives. Gradient equality implies global equality up to a constant, and a common finite infimum forces the constant to vanish.

Proof. The probe avoids both rank-drop sets and turns equality at one point into equality of analytic germs. Both functions are analytic on the specified common regular locus. The real-analytic identity theorem propagates equality throughout its connected component. If the complement is connected, it is also dense, and continuity extends equality to the omitted algebraic set. For gradients, the same argument extends gradient equality everywhere; integrating along line segments gives a constant difference. QED.

In particular, if distinct rational natural objectives share a germ, the union of their rank-drop sets must disconnect the coordinate space. This is an explicit spectral-geometric obstruction, not a definition in terms of an optimal decision tree.

## 3. No codimension-one rank loss: one query suffices

Let C_(m,d) be the class of rational pencils satisfying

   dim Sigma_a <= d-2,

with the convention that this requires Sigma_a empty for d=1. No global C2 or analytic regularity at Sigma_a is assumed.

THEOREM B. A single height-independent bounded algebraic VALUE query identifies the objective of every member of C_(m,d) up to global functional equality. A single GRADIENT query does the same on a subclass with common finite infimum zero. The decoding and subsequent epsilon-optimization are effective with unrestricted exact algebraic computation, as in checkpoint 02.

Proof of the needed connectivity fact. Let S be a closed semialgebraic set of dimension at most d-2, and x,y not in S. Points p for which the segment [x,p] meets S lie in

   {x+t(z-x): z in S, t>=1},

a semialgebraic set of dimension at most dim S+1<=d-1. The analogous bad set for y has the same bound. Their union cannot cover R^d. Choose p outside it. The polygonal path x--p--y avoids S. Thus R^d\S is path connected.

For two members of C_(m,d), the union of their rank-drop sets still has dimension at most d-2, so Theorem A applies. For decoding, enumerate rational pencils whose rank-drop set has dimension at most d-2, testing this property by an effective semialgebraic dimension algorithm. Match the algebraic reply. The true pencil occurs at a finite stage and any match has the correct global objective. If infimum zero is promised, rational-point enumeration then finds a point below any positive tolerance. This is not a polynomial-time or polynomial-degree algorithm.

Consequently codimension-one rank barriers are NECESSARY for any failure of this uniform one-query germ-decoding principle. They are NOT sufficient for optimization hardness, or even for nonanalyticity of the objective. The identification-hard/optimization-trivial example of checkpoint 01 demonstrates the first distinction.

## 4. A weakly infeasible, rational, isometric example that is not C2

This shows that Theorem B goes beyond global analyticity. Let

   A(u,v)=[[7u/10,v/2],[v/2,-u/10]],
   X(u,v,z)=diag(A(u,v),A(u,v),W(z)),
   W(z)=[[0,1],[1,z]].

All data are rational. The u direction has squared norm 2[(7/10)^2+(1/10)^2]=1. The v direction has four entries 1/2 and hence squared norm one. The z direction has one unit entry in W. Their supports are disjoint, so the chart is Frobenius isometric.

The determinant of A is -7u^2/100-v^2/4. Therefore A has one positive and one negative eigenvalue except at (u,v)=(0,0), where it is zero. W is nonsingular everywhere. The full rank-drop set is exactly the z axis, of codimension TWO in R^3. The maximum rank is six, falling to two on that axis.

The natural objective is exactly

   f(u,v,z)=[(1/2)sqrt(16u^2/25+v^2)-3u/10]^2+phi(z).

At v=0, its core is u^2/100 for u>=0 and 49u^2/100 for u<=0. Thus it is NOT twice differentiable along the u line at the origin. It is nevertheless C1 and 1-smooth, as every isometric natural PSD-distance objective is.

The W block precludes feasibility, and (u,v)=(0,0), z->+infinity gives zero distance. All core terms are nonnegative and vanish at u=v=0, so f(0)=1/2 and the exact escape profile is the same beta=1/2 formula in checkpoint 01. It belongs to C_(6,3), and one algebraic value identifies its objective among the entire declared codimension-two class, despite the missing global C2 regularity.

## 5. A chamber-count upper bound for full identification

Let Z be a KNOWN closed rational algebraic set with empty interior. Suppose a hidden rational pencil of fixed order/dimension is promised to have Sigma_a contained in Z. Let K be the number of connected components (spectral chambers) of R^d\Z. This number is finite and computable; it is geometric, not defined as query complexity.

THEOREM C. K exact natural VALUE queries suffice to identify the entire hidden objective, uniformly over arbitrary rational coefficient heights. With common infimum zero, K GRADIENT queries suffice as well. The probes can be chosen in advance. Subsequent optimization to any positive tolerance requires no additional oracle calls, with unlimited computation.

Proof. Choose a rational open ball inside each component: the components are nonempty open semialgebraic sets, so rational balls exist and can be found effectively. In each ball choose the algebraic germ probe of checkpoint 02, with the SAME fixed format-dependent degree. For any two candidates matching all replies, their analytic functions agree on a neighborhood of the probe in each chamber, hence throughout that chamber. The chamber union is dense, so continuity gives global equality. For gradient replies, first extend gradient equality globally, then use the common infimum to fix the additive constant. Enumerating the promised rational pencils gives an effective decoder; Sigma_a subset Z is a real algebraic sentence. QED.

For a known finite prior of N pencils one may take Z=union_a Sigma_a, the zero set of the product of the nonzero D_a. Its polynomial degree is at most 2mN. This gives an effective finite identification bound, but N can be exponential in the rational description length. We do NOT claim that this bound is small enough to refute the original minimax target.

The K-dependence is worst-case sharp up to an absolute constant. In checkpoint 01, the union of all rank-drop sets consists of the 4n distinct threshold lines x=a_j, a_j+1, a_j+3, a_j+4, and possibly the one padding line x=B. Thus K is 4n+1 or 4n+2, while success probability 2/3 in global identification requires n queries. All instances have the same uniform weak-infeasibility escape profile and polynomial rational encodings. This proves a Theta(K) worst-case IDENTIFICATION law for classes with a declared chamber envelope.

It does NOT prove an Omega(K) OPTIMIZATION law: that very family has a common known epsilon-approximate point, obtained with zero queries.

## 6. Optimization consequence and exact limit of the result

For the normalized escape-profile class with a declared K-chamber envelope, two valid exact-oracle procedures give

   N_opt(epsilon) <= min{K, C_beta epsilon^(-beta-1/2)}.

The first identifies the objective and performs unrestricted offline optimization; the second is the existing accelerated comparator method. A uniform lower bound matching this minimum is NOT proved. For K=1, the one-query bound is sharp on classes containing W(z) and W(-z), but those two functions alone do not address the full dimension-growing frontier.

The important invariant established here is spectral continuation across the complement of the maximal-rank-drop locus, combined with a coefficient-height-independent algebraic germ fingerprint. It locates the possible exact rational ambiguity at separating rank barriers. The still-missing theorem must determine whether those barriers can conceal the LOCATION OF NEAR-FEASIBLE POINTS for T arbitrary adaptive queries, or instead prove a universal way to bypass that optimization-relevant ambiguity.

Classical inputs are effective semialgebraic geometry, dimension under polynomial maps, and analytic continuation. No invention of these ingredients or completed grand theorem is claimed.