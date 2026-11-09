# Milestone 53 — generic two-MASA obstruction already with m+3 observables: exact symplectic degeneracy incidence

Track 02, 2026-11-09. Complete improvement of Milestones 49 and 52. The earlier sufficient generic measurement-count thresholds were 2m+1, then m+4. A precise rank-two symplectic degeneracy-locus dimension calculation, together with a separate analysis of the MINIMAL commutator-rank skew stratum, yields the stronger threshold **m+3**. This result is an operator-inclusion and interior PSD marginal-soundness no-go, NOT a universal impossibility for arbitrary positive decoders or singular lifted faces.

## Theorem 1 — generic m+3 dimensional threshold

Let m>=4 and let p be an integer with
  m+3 <=p<=m(m+1)/2.
There is an open dense full-measure real semialgebraic subset of the Grassmannian of p-dimensional subspaces L⊂S^m containing I_m such that
  rank omega_T|L>=4   for every 0!=T∈so(m),         (1)
where omega_T(H,K)=<T,[H,K]>_F.

Consequently, for EVERY integer ancilla r>=1 and every two real ONB diagonal MASAs D1,D2 on R^(mr),
  L⊗I_r is NOT a subspace of D1+D2.                    (2)
A nonempty exactly sound two-basis PSD recovery fibre with ordinary partial-trace decoder and source measurement space L therefore CANNOT have a positive-definite feasible lift on the full tensor space, regardless of r.

For m=3 the same statement holds at p=m+3=6=D_m by the deterministic full-measurement theorem in Milestone 49. Every such generic family contains rational trace-normalized measurement spaces.

## 2. Exact geometry of rank-at-most-two restrictions in a symplectic space

Let U be a real symplectic vector space of dimension 2r (nondegenerate alternating form), and let 2<=t<=2r. Consider the subset B_t⊂Gr(t,U) of t-dimensional subspaces on which the restricted alternating form has rank at most TWO.

**Lemma 2.** If t>r+1, B_t is EMPTY. For 2<=t<=r+1, the locus of restricted rank EXACTLY TWO is nonempty and has dimension
  dim Gr(t,2r)−(t−2)(t−3)/2,
so the rank-at-most-two locus has codimension
  c_symp(t)=(t−2)(t−3)/2.                        (3)
For t=0,1 the rank is automatically zero and the codimension is zero.

**Proof.** If the restricted form has rank two, its radical W has dimension t−2. It is an isotropic subspace of U and, because it is the radical, the t-plane A satisfies
  W ⊂ A ⊂ W^perp.
Since dim W^perp=2r−(t−2), the inclusion of a t-plane requires
  t<=2r−t+2, i.e. t<=r+1.
Conversely for t<=r+1, choose any isotropic W of dimension t−2 and any NONDEGENERATE two-plane A/W inside the symplectic quotient W^perp/W of dimension 2(r−t+2). Then A has restricted rank exactly two and radical W.

The isotropic Grassmannian of w=t−2 dimensional subspaces of U has dimension
  w(2r−w)−w(w−1)/2,
because the ordinary Grassmannian Gr(w,2r) has dimension w(2r−w), and isotropy imposes w(w−1)/2 independent conditions. Given W, the nondegenerate two-planes in W^perp/W form an OPEN nonempty subset of Gr(2,2(r−t+2)), of dimension 4(r−t+1). Their sum is
  (t−2)(2r−t+2)−(t−2)(t−3)/2+4(r−t+1)
 = t(2r−t)−(t−2)(t−3)/2.
The rank-zero locus (isotropic t-planes) has strictly smaller dimension for t>=2: the rank-two dimension exceeds the isotropic t-Grassmann dimension by 2t−3>0. Thus (3) holds for rank<=2 as well. QED.

For t<=3, (3) gives zero; indeed every alternating form on a 0-, 1-, 2- or 3-dimensional space has rank<=2.

## 3. Exact codimension estimate for a fixed skew T

Let V=S_0^m have dimension n=D_m−1. For a fixed nonzero real skew T, the full commutator form omega_T on V has rank 2r>=2m−2, by the eigenvalue-sum proof in Milestone 49. Write K for its radical, dimK=n−2r. Let l=p−1=dim(L∩V), and let L0 be an l-plane in V.

Stratify L0 by the dimension t of its image under the quotient V→V/K. Its intersection with K has dimension l−t. To construct L0 with a specified t-dimensional projected subspace A⊂U=V/K:
  - choose A, a t-plane in 2r-dimensional U;
  - choose B=L0∩K, an (l−t)-plane in the (n−2r)-dimensional K;
  - choose a graph lift A→K/B, contributing t(dimK−l+t) parameters.
The last two contributions sum to l(dimK−l+t). Thus the codimension inside Gr(l,V) of the locus where omega_T|L0 has rank<=2 AND dim projection=t is at least
  C(l,r,t)=l(2r−t)−dim B_t
          =(l−t)(2r−t)+c_symp(t),                (4)
where c_symp(t) is given in Lemma 2. Feasible strata satisfy
  0<=t<=min(l,r+1) and l−t<=dim K.

For t>=4, the expression (4) is strictly DECREASING in t across the feasible interval, because its continuous derivative is
  −(2r+l)+2t+(2t−5)/2
   =3t−2r−l−5/2<0
for t<=min(l,r+1). For t<=3 the term c_symp(t)=0 and the expression is also decreasing. Hence the least possible codimension occurs at the MAXIMUM allowed t, and it is bounded below by the value at t_max=min(l,r+1), even if the radical-size condition makes that t infeasible.

This gives the SHARP UNIFORM fixed-T lower bounds
  if r>=l−1:
      codim bad >=(l−2)(l−3)/2,                 (5)
  if r<=l−2:
      codim bad >=(r−1)(l−(r+4)/2).            (6)

These are stronger than the isotropic-hyperplane estimates used in Milestones 49 and 52.

## 4. Improve the generic count using the minimal-rank skew stratum

Put k=dim so(m)=m(m−1)/2. Assume the NEW threshold
  p>=m+3, so l=p−1>=m+2.
For the minimal l=m+2, the fixed-T estimates are:

(a) If r>=l−1=m+1, (5) gives
  codim >=m(m−1)/2=k.

(b) If r=m, (6) gives
  codim >=(m−1)(m/2)=k.

(c) If r=m−1 (the MINIMAL possible r), (6) gives
  codim >=(m−2)(m+1)/2=k−1.              (7)

Both bounds are increasing in l, so they remain valid or improve for p>m+3. Thus all skew T with r>=m contribute incidence sets of dimension at most
  dim Gr(l,V)−k+(k−1)<dim Gr(l,V),
even after allowing arbitrary projective skew T (dimension k−1).

For r=m−1, the fixed-T codimension bound k−1 would be just insufficient if the projective set of such T had its full ambient dimension k−1. But it DOES NOT. The minimal-rank stratum
  Z_min={[T] in P(so(m)): rank omega_T=2m−2}
is a PROPER real algebraic/semialgebraic subset of P(so(m)), because there exist skew T with higher commutator rank. For m>=4, choose real skew T with two distinct positive rotation frequencies λ1≠λ2 and zero on the remaining m−4 dimensions. Its induced action on Sym² has at least
  4(m−4)+8=4m−8>2m−2
nonzero eigenvalues (four sign-combinations between the two rotation blocks, four extreme self-pairs, and four(m−4) cross pairs with the zero eigenspace). Thus Z_min is the proper determinantal locus rank(ad_T)<=2m−2 and has projective dimension at most k−2.

Combining its dimension <=k−2 with the fixed-T codimension >=k−1 in (7), the corresponding incidence again has dimension strictly below dim Gr(l,V).

Therefore the FULL incidence set
  {(L0,[T]):T!=0 and rank omega_T|L0<=2}
has semialgebraic dimension less than dim Gr(l,V). Its projection onto the real Grassmannian is CLOSED (projective skew parameter compact) and has empty interior and measure zero. Its complement is open dense and full measure. Rational points are dense in real Grassmannian charts, so rational examples exist.

This proves (1). The rank-two commutator necessity of Milestone 49 yields (2), completing the theorem. QED.

## 5. Scope, comparison and sharpness caution

- This is a COMPLETE improvement of the generic threshold p>=m+4 from Milestone 52, not a new conjecture.
- The key new ingredient is an EXACT codimension formula for rank<=2 alternating-form restrictions in a symplectic quotient, and careful control of the projective family where rank omega_T is minimal. Omitting that exceptional stratum would leave an unjustified borderline dimension count.
- This does NOT assert generic impossibility at p=m+2. There the rank<=2 incidence has larger expected dimension and may genuinely span the entire skew parameter space; the weaker basis-free criterion in Milestone 49 may or may not rule it out.
- The result is dimension independent in the tensor ancilla r and assumes neither basis is maximally entangled, nor a reflection, nor zero/nonzero overlaps.
- It tests the operator inclusion L⊗I_r⊂D1+D2. An exact sound PSD two-basis marginal quotient with a positive-definite lifted point must satisfy this inclusion, but a singular-face quotient can evade it by compressing one-body observables.
- The ordinary partial-trace decoder is essential. An arbitrary positive CP decoder with a more general adjoint can evade the commutator obstruction; no universal quadratic-size SDP impossibility is claimed.
- For the quantitative version, gamma_4(L)>0 follows by compactness for every L in the open dense class. Hence the robust coefficient/conditioning and interiority error floors of Milestones 50–51 apply already at p>=m+3, with input-dependent gamma_4.
- All proofs are real; independent external novelty and peer-review audits remain outstanding.
