# Milestone 60 — generic dense SDPs exclude EVERY single-Kraus two-basis decoder at an ambient full-rank feasible point, ANY size

Research Track 02, 2026-11-09. Complete real linear-algebra/Grassmannian theorem. This is a major sharpening of Milestone 57 in a complementary direction. Milestone 57 gave quantitative dimension and giant-slack tradeoffs for arbitrary many-to-one rank-one Kraus PSD quotients. Here the ambient order N is UNBOUNDED: for a generic sufficiently rich trace-controlled measurement space, the source observations cannot even be SOUND under a positive-definite lifted two-basis feasible point through ANY single-Kraus CP decoder D(Y)=CYC^T, regardless of C or N. Crucially, we allow EVERY positive-definite source congruence; thus changing decoder coordinates does not escape the result.

This is an impossibility for an INTERIOR-lifted family, not for singular-face many-to-one quotients and not for all high-Kraus CP decoders. The frontier therefore remains a singular-face, non-Jordan multi-Kraus CP quotient or a different positive/nonlinear decoder.

## 1. Uniform generic theorem

Let m>=9, let 2m+1<=p<=D_m=m(m+1)/2, and let L be a p-dimensional real subspace of S^m containing I_m. For G>0 in S^m and nonzero real skew T in so(m), define on L
  omega_(T,G)(H,K)=<T,H G K−K G H>_F.

**Theorem A (congruence-uniform rank-four gap).** There is a nonempty OPEN DENSE, full-measure, semialgebraic family of such L, including rational L, for which
  rank omega_(T,G)|L >=4                                   (1)
for EVERY positive-definite G and EVERY nonzero skew T.

This is much stronger than the earlier generic two-MASA commutator criterion (Milestone 53), which fixes G=I. It makes the criterion invariant under ALL possible invertible positive source congruences G^(1/2) L G^(1/2).

## 2. A uniform rank bound on the traceless source space

Put V=S_0^m={H:tr H=0} of dimension n=D_m−1, and l=p−1. Let L=R I_m ⊕L0 with L0=L∩V, dimL0=l. It suffices to prove (1) restricted to L0.

For fixed G>0 and T!=0, the alternating form omega_(T,G) on S^m is congruent (under H ->G^(1/2)H G^(1/2)) to the ordinary matrix-commutator form omega_T'(H,K)=<T',[H,K]> for a nonzero skew T'=G^(-1/2) T G^(-1/2), so its rank on S^m is at least 2m−2 by Milestone 49's explicit real skew spectral argument.

Also G^(-1) belongs to its radical: for H=G^(-1),
  H G K−K G H=K−K=0.
Because tr G^(-1)>0, this radical vector lies OUTSIDE V. The quotient map V -> S^m/rad omega is consequently SURJECTIVE, so restricting omega_(T,G) to V does NOT decrease its rank. Hence for every fixed (G,T)
  rank omega_(T,G)|V =2r>=2m−2, i.e. r>=m−1.       (2)

This observation prevents an otherwise easy-to-miss loss of two in the rank bound when moving from the full symmetric space to traceless source perturbations.

## 3. Uniform incidence codimension with an extra positive-congruence parameter

For a fixed (G,T), the rank<=2 restriction locus
  B_(G,T)={L0 in Gr(l,V):rank omega_(T,G)|L0<=2}
is a real semialgebraic/algebraic Grassmannian degeneracy locus.

The exact symplectic rank-two degeneracy count from Milestone 53 says: for an alternating form of rank 2r on V and l-dimensional L0, the bad-locus codimension is at least
  c1=(l−2)(l−3)/2  if r>=l−1,
  c2=(r−1)(l−(r+4)/2) if r<=l−2.                 (3)
The formula correctly includes arbitrary radical intersections, not merely nondegenerate ambient alternating forms.

Our hypothesis p>=2m+1 gives l>=2m. If r<=l−2, c2 is increasing as a function of r in [m−1,l−2], so its minimum is attained at r=m−1. Thus
  c2>=(m−2)(l−(m+3)/2)
     >=(3/2)(m−2)(m−1).
If r>=l−1, c1>=(m−1)(2m−3), which is larger. Therefore every (G,T) has
  codim B_(G,T) >=c_min=(3/2)(m−2)(m−1).        (4)

The real positive-definite matrix G varies in an open semialgebraic cone of dimension
  dim S^m=D_m=m(m+1)/2.
The projective skew parameter [T] varies in dimension
  dim P(so(m))=m(m−1)/2−1.
Their TOTAL parameter dimension is
  D_m+dim P(so(m))=m²−1.                        (5)

For m>=9,
  c_min−(m²−1)
     =[3(m−2)(m−1)−2m²+2]/2
     =[(m−1)(m−8)]/2 >0.                        (6)

Form the incidence set of triples (L0,G,[T]) satisfying rank omega_(T,G)|L0<=2. Its dimension is bounded above by dim Gr(l,V)−c_min+(m²−1), strictly less than dim Gr(l,V). Its projection onto the source Grassmannian is semialgebraic and its closure has lower dimension. Thus its complement contains an open dense full-measure semialgebraic subset of Gr(l,V); rational L0 are dense and may be chosen there. For those L, condition (1) holds for all G>0,T!=0. QED.

## 4. Corner-Jordan two-MASA rigidity

**Lemma B (any isometric corner Jordan embedding).** Let V0:R^N→R^m satisfy V0 V0^T=I_m, and let S⊂S^m. If
  {V0^T H V0:H in S} ⊂D1+D2
for two real ONB diagonal MASAs D1,D2 in S^N, then the skew commutator forms omega_T|S have rank<=2 for a family of T∈so(m) that SPANS all of so(m).

Proof. The map Phi(H)=V0^T H V0 preserves products in the corner:
 Phi(H)Phi(K)=V0^T H (V0 V0^T) K V0=Phi(HK),
and likewise preserves commutators. Fix the first ONB ψ_i and split Phi(H)=A_H+B_H linearly into the two commuting diagonal spaces. For each offdiagonal pair i<j, the matrix element of [Phi(H),Phi(K)] equals a decomposable alternating form
  f_ij(H)ell_ij(K)−f_ij(K)ell_ij(H)
with rank at most two, where f_ij comes from differences of first-basis diagonal A_H entries and ell_ij from first-basis offdiagonal Phi(H) entries.

Let T_ij in so(m) represent the skew functional
  <T,T_ij>_F=<ψ_i,V0^T T V0 ψ_j>.
Then the commutator form omega_(T_ij)|S has rank<=2. The family {T_ij} SPANS so(m): if T were orthogonal to all of them, V0^T T V0 would have every offdiagonal zero and (as a REAL skew matrix) every diagonal zero, so V0^T T V0=0. Multiplying by V0 left/right yields T=0. QED.

This extends the ordinary tensor-amplification lemma of Milestone 49 to every genuine single-Kraus corner embedding, with no assumption on N.

## 5. The SDP impossibility statement

**Theorem C (no full-rank lifted two-basis soundness under a single-Kraus decoder).** Choose L from the generic class in Theorem A, and define a rational trace-controlled source measurement map A with range A*=L and datum b=A(I_m). Let C be ANY real m-by-N matrix and let
  D(Y)=CYC^T
be the CP decoder. Suppose a nonempty two-basis PSD fibre
  T={Y>=0:B_U(Y)=y}
contains a POSITIVE-DEFINITE feasible matrix Y0>0 and satisfies
  A(D(Y))=b for EVERY Y∈T.
Then the hypotheses are mutually contradictory; no such U,C,y,N exist, at ANY N.

Proof. Soundness on a full-rank feasible point implies, by +/- small symmetric perturbations in the kernel of the two-basis measurement map,
  D*(L)={C^T H C:H in L} ⊂D1+D2.          (7)
Because b=A(I_m), the source I_m is positive definite and belongs to the decoded feasible set in an exact surjective representation, and therefore C has full row rank. More generally a sound fibre need not be surjective: to apply the theorem assume explicitly D(T) contains one positive-definite source matrix; this guarantees rank C=m. (The conclusion of Theorem C is for such full-source-rank sound designs.)

Let G=CC^T>0 and V0=G^(-1/2)C, so V0 V0^T=I_m. Write
  C^T H C=V0^T (G^(1/2) H G^(1/2)) V0.
Thus (7) puts the CORRECTLY CONGRUENCE-TRANSFORMED source space
  S=G^(1/2)L G^(1/2)
inside the corner Jordan embedding of two MASAs. Lemma B then produces a spanning family of skew T' with rank omega_T'|S<=2. But Theorem A says for ALL G>0,T'!=0 these commutator ranks are at least four, contradiction. QED.

**Scope correction:** the theorem needs rank C=m, equivalently the decoded fibre contains at least one positive-definite source matrix. Without that hypothesis a degenerate decoder C=0 could map a full-rank input fibre to a zero source matrix and be trivially sound for a different datum. The exact SURJECTIVE normal-form problem does contain I_m, so it automatically satisfies the needed hypothesis.

The result excludes even linear source soundness, before asking for completeness, objective preservation, polynomial conditioning, positivity of every observed datum, nonreflection basis design or uniqueness of ambient PSD solutions.

## 6. Sharp interpretation and limitations

- The obstruction is independent of ambient matrix order N. Increasing the ancillary/output dimension cannot cure a full-rank-lift single-Kraus construction.
- Source operators can be generic rational, dense, noncommuting, and have only p=2m+1 independent measurements (linear in source order), for m>=9.
- A lifted fibre supported in a PROPER PSD face has no positive-definite Y0 on the full N-space; its compressed rank-one measurements are no longer the two MASAs and may escape the lemma. This is the main remaining singular-face route.
- A decoder with two or more Kraus operators need not be Jordan on source operators, so the exact commutator preservation in Lemma B fails; it is subject only to the quantitative commutator-defect inequality of Milestone 54.
- A general positive non-CP decoder, nonlinear decoder, or merely sound numerical algorithm on selected outputs is outside the theorem.
- This is a generic exact algebraic NO-GO, not an asymptotic computational hardness theorem or a proof against all near-quadratic many-to-one reductions.
- A new explicit polyhedral/semidefinite output-cone obstruction for entanglement-breaking CP decoders is in Milestone 58, and the generic strict-positivity barrier for very high Kraus rank is in Milestone 59. Together these identify a narrow but nonempty space of SPECIAL, NON-JORDAN, high-Kraus, singular-support designs that remains viable.
