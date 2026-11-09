# Milestone 52 — strengthen the generic two-MASA no-go threshold from 2m+1 to m+4 source observables

Track 02, 2026-11-09. This is a complete improvement of the new commutator-incidence theorem of Milestone 49 and immediately strengthens the quantitative Milestone 50 and soundness Milestone 51. The improvement is genuinely substantial for high-dimensional sources: only m+4 independent source observables are needed, despite allowing arbitrarily large tensor ancillas and arbitrary choices of BOTH measured orthonormal bases.

**Superseded threshold:** Milestone 53 proves the stronger generic threshold p>=m+3 using an exact rank-two symplectic degeneracy-locus count. This milestone remains a valid, independently auditable earlier incidence argument.

## Theorem 1 — generic real two-MASA obstruction at p>=m+4

Let m>=4 and p be an integer satisfying
  m+4 <=p<=m(m+1)/2.
There is a nonempty, OPEN DENSE, full-measure semialgebraic subset U of the real Grassmannian of p-dimensional subspaces L⊂S^m that contain I_m, such that for EVERY L∈U and every nonzero real skew T,
  rank[(H,K) -> <T,[H,K]>_F on L] >=4.             (1)

In particular, for EVERY auxiliary dimension r>=1, there are NO two real orthonormal bases of R^(mr) with diagonal MASAs D1,D2 satisfying
  L⊗I_r ⊂D1+D2.                                        (2)
This extends the impossibility statement of Milestone 49, which previously used the sufficient threshold p>=2m+1.

The generic class contains RATIONAL source measurement spaces L. The resulting trace-controlled rational SDP input can have only O(m) independent dense, noncommuting measurements, not necessarily Theta(m²) measurements.

## Complete dimension-count proof

We reuse the entirely elementary ingredients proved in Milestone 49, and include the decisive arithmetic.

Put D=m(m+1)/2, n=D−1, l=p−1, and a=l−1=p−2. Thus a>=m+2. Write L=R I⊕L0 with L0 in the l-dimensional Grassmannian of the traceless n-dimensional space V=S_0^m.

For nonzero real skew T, the alternating form omega_T on V has rank 2r>=2m−2, i.e. r>=m−1; this follows by diagonalizing T over C and counting nonzero eigenvalue sums on Sym²(C^m), with the scalar identity lying in the radical.

If rank omega_T|L0<=2, then L0 contains an isotropic a-plane S (the radical of a rank<=2 alternating restriction has codimension<=2, and one extra direction gives an isotropic hyperplane). As proved by direct parametrization in Milestone 49, the variety of such l-planes for fixed T has codimension at least
  C(a,r,t)=[4ra−4rt−2at−2a+3t²−t]/2,
for t the image dimension of S in the symplectic quotient by rad omega_T. This expression is strictly decreasing for 0<=t<=min(a,r), so its minimum is bounded below as follows:

Case r>=a:
  codim>=a(a−3)/2.                                   (3)

Case m−1<=r<a:
  codim>=r(a−(r+1)/2)−a
         >=(m−2)a−m(m−1)/2.                          (4)
The last inequality uses that this expression is increasing in r for r<a.

Let k=m(m−1)/2=dim so(m). At the NEW minimal value a=m+2, the case-(3) bound gives
  a(a−3)/2−(k−1)
    =[(m+2)(m−1)−m(m−1)+2]/2
    =m>0.                                               (5)
The case-(4) bound gives
  (m−2)(m+2)−m(m−1)/2−(k−1)
    =(m²−4)−m(m−1)+1
    =m−3>0.                                             (6)

Both lower bounds increase with a, so UNIFORMLY for every a>=m+2 and every nonzero T,
  codim_(Gr(l,V)) {L0:rank omega_T|L0<=2}
    > dim P(so(m))=k−1.                                 (7)
If an isotropic a-plane does not exist for some (r,a), the corresponding bad set is empty and the inequality is automatic.

Now form the semialgebraic incidence set of pairs (L0,[T]) with T!=0 and rank omega_T|L0<=2. By (7), its dimension is STRICTLY smaller than dim Gr(l,V), even after allowing [T] to vary in the real projective skew space of dimension k−1. Its projection to Gr(l,V) is semialgebraic, dimension deficient, and CLOSED (the skew projective parameter is compact and the rank<=2 condition is polynomial). Thus its complement is open dense, full measure and nonempty. Rational Grassmannian charts are dense, so the complement contains rational L0.

For any L in this complement, rank omega_T|L>=4 for all T!=0, proving (1). The purely algebraic rank-two commutator criterion in Milestone 49 says that if L⊗I_r could lie in the sum of two ONB diagonal spaces, EVERY reduced skew matrix T_ij from the first basis would have rank<=2 commutator form, while the T_ij span so(m). Since (1) excludes all nonzero such T, this is impossible, proving (2). QED.

## Corollary 2 — the ordinary partial-trace route needs singular lifted support

Let A:S^m→R^p be trace controlled with range A*=L in the generic class above. Let Y0>0 in S^(mr) be a purported two-basis PSD feasible matrix whose ordinary partial trace is a source-feasible point. If every exact two-basis solution decodes via ordinary partial trace to a source matrix satisfying A(X)=b, tangent-space duality forces
  L⊗I_r⊂D1+D2,
contradicting (2). Thus a sound two-basis partial-trace representation of such an SDP MUST have no positive-definite feasible matrix on the full tensor space; it is necessarily facially degenerate. In a nonempty finite-dimensional PSD fibre the Gordan–Stiemke alternative then supplies a nonzero measured PSD exposing stress annihilating the entire lifted exact fibre. The latter stress is a NECESSARY structural feature, not a proof that a sound singular representation exists.

## Corollary 3 — quantitative error and conditioning margin

For every L in this generic class,
  gamma_4(L)=min_(||T||F=1) sigma_4(omega_T|L)>0
by compactness and (1). Therefore the explicit approximation barrier of Milestone 50 holds:
  8K epsilon+2epsilon²
    >= gamma_4(L) sqrt[(m−1)/(2(mr−1))]
for every linear two-MASA approximate decomposition with operator error epsilon and coefficient bound K. The positive-interiority source soundness error floor of Milestone 51 also applies, now for the reduced threshold p>=m+4.

This is a CONDITION-DEPENDENT lower bound, not a universal polynomial lower bound for gamma_4 on rational input spaces.

## Sharpness of the METHOD, not of the actual phenomenon

At a=m+1 (equivalently p=m+3), the crude fixed-T bad-locus codimension lower bound in Case (3) is exactly k−1, and Case (4) is one smaller. Consequently this particular incidence estimate alone does NOT prove that the bad incidence projection has positive codimension at p=m+3. It may still be possible to rule out two-MASA inclusion for generic p=m+3 through the weaker necessary condition span{T:rank omega_T|L<=2}=so(m), through the real geometry of the Pfaffian locus, or through a different invariant. No such stronger claim is made here.

## Independent adversarial audit

- The improved threshold is m+4, not 2m+1; all inequalities (3)-(7) were rederived with a=p−2 rather than reusing the older a>=2m−1 substitution.
- The rank loss for restriction of alternating forms is avoided by the full isotropic-Grassmannian incidence calculation, including arbitrary radicals.
- The variable T ranges over REAL skew matrices with a compact projective normalization; no assumption of complex generic skew diagonalizability is hidden.
- The key fixed-T rank bound 2m−2 holds for every nonzero real skew T, not merely a generic T.
- The genericity conclusion is real open dense semialgebraic, and rational examples exist. No explicit universal rational basis for U or polynomial conditioning bound is asserted.
- The application to ordinary partial trace requires a FULL-RANK ambient feasible point; a singular lifted minimal support can evade the operator inclusion, so the theorem does NOT settle unrestricted many-to-one quadratic universality.
- The lower source measurement dimension is LINEAR in m, making the obstruction relevant even to many modest-size dense noncommuting SDP systems.
