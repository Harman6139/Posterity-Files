# Canonical ordinary-CP all-rule obstruction: checkpoint 000

Date: 2026-11-15. Parent: f79e4d104575603a459718944dc748f4ba261161. Earlier results are unchanged.

## New analytical mechanism

This is a new proof under active checking, not yet a completed publication/novelty claim. It does not transfer a constrained cone to the orthant. It works directly in the ordinary copositive Ryshkov set from canonical T_n.

Let r=n-1, T=T_r the tridiagonal matrix with diagonal 1 and adjacent entries -1/2. The face F of R_n obtained by retaining all top-coordinate interval equalities consists exactly of P(b,c)=[[T,b],[b^T,c]]. It is the epigraph c>=g(b), where

  g(b)=sup_{u>=0 integral,y>=1 integral}(1-u^T T u-2y b^T u)/y^2.

Let z minimize x^T T x+2b^T x over x>=0, and d=b+Tz. Then z,d>=0 and z_i d_i=0. Put Q=2n, kappa=1/(2 Q^(2r)), Y=2 Q^r. Dirichlet approximation of the positive coordinates of z, with denominator at most Q^r, yields

  z^T T z+kappa <= g(b) <= z^T T z+1.

Consequently every active lattice constraint at any boundary point has y<=Y and, writing e=u-yz,

  e^T T e+2y d^T u = 1-y^2(g(b)-z^T T z) <=1.

At a vertex the active (2u/y,1) must span R^(r+1). Thus for every coordinate some active u_i>=1, giving 0<=d_i<=1/2. If two vertices share an active (u,y), then

  b_i+(T u/y)_i in [-1/y,1/2+1/y]

at both vertices. Therefore every bounded edge in F satisfies

  ||b'-b||_infinity <= 5/2.

This holds for ALL n, with no y=1 assumption or low-dimensional covering-radius shortcut. The face recession cone has b-direction>=0 and c-direction>=0. The canonical T_n lies in F and starts with b=-e_r/2.

## Explicit ordinary CP nonmembers

For n>=5 let F_n=I+(3/5)Adj(C_5) on coordinates (1,2,3,4,n), with identity on other coordinates. Let D=diag(1,8/5,8/5,1,...,1), C_n=sum of all interval vv^T, epsilon=1/(100 n^3), and B=D F_n D+epsilon C_n. Then B is positive definite, strictly entrywise positive, and is an ordinary CP nonmember, witnessed by the inverse-diagonal-congruence Horn matrix W_0. Its leading block B_0 is a strictly positive combination of all top interval normals. The base singleton weights are 1/25,8/125,8/125,1/25 and the base adjacent-pair weights are 24/25,192/125,24/25; additional coordinates have unit singleton weights. The anchor adds at least epsilon to every interval coefficient. B has common denominator 500 n^3.

For S_N=diag(N,...,N,1), set B_N=S_N B S_N and A_N=B_N/(4nN^2). This remains an ordinary CP nonmember and PD/strictly positive. With W_N=S_N^-1 W_0 S_N^-1+I/(20nN^2), one has cone margin 1/(20nN^2), norm<=6, and <W_N,A_N><=-1/(5nN^2).

## Dominance controls all extreme rays, not one rule

Let m>=1, d=n(n+1)/2, U=2Y n^2(m+1), E=(d-1)![2U^2]^(d-1), and choose N=20000 n^3 E^2. After at most m moves within F, the bounded-edge lemma gives ||b||_infinity<=3(m+1), z_i<=n^2(m+1), and every active lattice vector has coordinates <=U. Cofactors therefore bound every primitive integral extreme tangent ray by |R_ij|<=E.

The exposure h(R)=<B_0,R_top> is nonnegative on the tangent cone. Equality means R_top=0. If h>0, integrality and the common denominator give h>=1/(500n^3). The objective cost is

  <B_N,R> = N^2 h(R)+2N c_0^T R_cross+a R_nn,

where sum c_0<2 and a<2. Hence all extreme rays with h>0 have strictly positive cost, since their remaining cost has magnitude <=6NE. All improving rays lie in F. No improving ray in F is a recession ray because the input cross-column and bottom diagonal are positive. A selected ray therefore has a bounded adjacent endpoint still in F. At all such vertices, objective pairing stays positive (leading N^2 term dominates O(Nm) and small perturbations), so vertex separation cannot stop the walk. Nonmembership guarantees an improving extreme ray exists. Induction forces at least m pivots for EVERY strictly descending adjacent extreme-ray rule.

## Robustness and identity-correction interface

The same argument should hold on ||A-A_N||_F<=1/(1600n^4N^2), corresponding to an unnormalized perturbation of norm<=epsilon/4. PD, positive entries, norm<=1, strict nonmembership, all outside-face objective signs and positive vertex pairings persist.

For an improving primitive integral ray R in F, R_top=0 and |R_ij|<=E. If R+tau I is copositive, tau>=0, and either a negative bottom entry or a negative cross entry forces tau>=1/(2E). Its objective pairing is then at least -7NE+N^2/(2E)>0. Thus no scalar identity correction of ANY improving ray can separate during the forced prefix. This explains the conservative square E^2 in N.

## Status

The proof above is analytical and has been checked for the main degeneracies, but exact construction tests, polished constants, independent verification, complete manuscript, and current primary-source comparison are still being prepared in this session. No numerical trajectory has been simulated. The forthcoming claim is ordinary CP_n for every n>=5 from T_n, not a cone-restricted variant. Historical novelty and a journal percentile are not yet certified.
