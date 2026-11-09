# Milestone 49 — DIMENSION-INDEPENDENT two-MASA obstruction for generic dense partial-trace SDP quotients

Track 02, 2026-11-09. Complete self-contained real-matrix theorem and incidence proof. It is a genuine strengthening of the maximally-entangled-first-basis obstruction in Milestone 20: **BOTH measured ONBs may now be arbitrary**, with NO condition on their individual reduced states, and the auxiliary tensor dimension is unlimited. This rules out a large class of quadratic many-to-one proposals that relied on ordinary partial trace with a strictly feasible ambient lift. It does NOT exclude arbitrary positive/CP decoders, positive-dimensional singular support reductions, or unrestricted O(m²+p) universality.

**Threshold update (Milestone 53):** The generic source dimension hypothesis p>=2m+1 proved below has now been strengthened to p>=m+3 for m>=4 by the exact symplectic degeneracy-stratum count in 53_GENERIC_M_PLUS_THREE_TWO_MASA_NO_GO_VIA_EXACT_SYMPLECTIC_DEGENERACY.md. All structural two-MASA lemmas in this document remain unchanged.

## 1. Pure two-MASA algebraic criterion

Let L⊂S^m be any real linear subspace. For T∈so(m) define the alternating bilinear form on L
  omega_T(H,K)=tr(T[H,K]),  H,K∈L,
where [H,K]=HK−KH is real skew symmetric. Sign or Frobenius inner-product convention is irrelevant for the rank. Define the rank-two commutator locus
  B_L={T∈so(m):rank(omega_T|_L)<=2}.

**Theorem 1 (basis-free necessary condition).** If for some r>=1 and two real orthonormal bases of R^(mr), with diagonal operator spaces D1,D2, one has
  L⊗I_r ⊂ D1+D2,                                         (1)
then
  span_R B_L = so(m).                                     (2)
In particular, if B_L is contained in a proper real linear subspace of so(m), NO pair of orthonormal bases of ANY tensor order mr can satisfy (1).

**Proof.** Choose the first ONB ψ_1,...,ψ_(mr). Since L⊗I_r lies in D1+D2, choose a LINEAR splitting H⊗I_r=A_H+B_H with A_H∈D1 and B_H∈D2 for H∈L (take a right inverse of the surjection D1⊕D2→L⊗I_r). All A_H commute, and all B_H commute.

For i≠j define real linear functionals
  ell_ij(H)=<ψ_i,(H⊗I_r)ψ_j>,
  f_ij(H)=<ψ_i,A_H ψ_i>−<ψ_j,A_H ψ_j>.
Using [H⊗I,K⊗I]=[A_H,B_K]+[B_H,A_K], and that the off-diagonal entries of B_H equal those of H⊗I, obtains
  <ψ_i,([H,K]⊗I_r)ψ_j>
    =f_ij(H)ell_ij(K)−f_ij(K)ell_ij(H).             (3)
The right side is a DECOMPOSABLE alternating two-form and has rank <=2.

The left side is omega_(T_ij)(H,K) for the skew part T_ij of the partial trace of the real rank-one cross matrix ψ_i ψ_j^T (up to an irrelevant sign). Thus every T_ij belongs to B_L.

The family {T_ij:i<j} SPANS so(m). Indeed, if a skew T is Frobenius-orthogonal to all T_ij, the real skew matrix T⊗I_r has zero off-diagonal entries in the complete ONB ψ_i; its diagonal entries are automatically zero because a real skew matrix has x^T(T⊗I)x=0 for every x. It is therefore zero, forcing T=0. Hence the orthogonal complement of span{T_ij} is zero, proving (2). QED.

A useful simpler corollary: if for EVERY nonzero skew T the form omega_T|L has rank>=4, the two-MASA inclusion (1) is impossible.

## 2. Lower rank of the full symmetric commutator form

**Lemma 2.** For any m>=2 and nonzero real skew T, the alternating form omega_T on S^m has rank at least 2m−2. The same bound holds on the traceless subspace S_0^m={H:trH=0}.

**Proof.** Cyclicity of trace identifies the form with the linear transformation
  ad_T:S^m→S^m,  H↦[T,H].
Here [T,H] is symmetric and traceless. The scalar identity I is killed, so removing I from the domain does not change its rank.

Complexify, and diagonalize the real skew T. Its eigenvalues are pure imaginary iλ_j, where λ_j∈R occur in opposite-sign pairs and zeros. Under S^m_C≅Sym²(C^m), the linear map H↦TH−HT=T H+H T^T is the induced action T⊗I+I⊗T, with eigenvalues i(λ_i+λ_j) on symmetric basis pairs i<=j.

Let λ*>0 be the greatest absolute value among λ_j, with multiplicity h among positive λ* and h among negative −λ*. The other m−2h eigenvalues lie strictly inside (−λ*,λ*). The following symmetric tensor pairs have NONZERO induced eigenvalue:
 (a) all pairs within the +λ* group, h(h+1)/2 of them;
 (b) all pairs within the −λ* group, h(h+1)/2 of them;
 (c) all 2h(m−2h) pairs between either extreme group and a nonextreme eigenvalue.
Therefore
  rank ad_T >= h(h+1)+2h(m−2h)
            =2hm−3h²+h.
Since m>=2h and h is a positive integer, this is >=2m−2: at m=2h its difference from 2m−2 is (h−1)(h−2)>=0; for larger m the difference increases with slope 2h−2>=0. Thus rank omega_T>=2m−2. QED.

**Corollary 3 (deterministic high-measurement obstruction).** If L contains I and has codimension s<=m−3 in S^m, then no ordinary partial-trace amplification L⊗I_r lies in the sum of two real ONB diagonal spaces for ANY r. Indeed restricting an alternating form to a subspace of codimension s drops its rank by at most 2s, so
  rank(omega_T|L)>=2m−2−2s>=4
for every T!=0. Apply Theorem 1.

This includes dense noncommuting measurement spaces at any m>=4; it is not merely a statement about maximally entangled or product first bases.

## 3. Generic dense obstruction at p>=2m+1 independent source measurements

Put D=m(m+1)/2, V=S_0^m of dimension n=D−1, and let p=dim L with I∈L. Thus L=R I⊕L_0, where L_0 is an l=(p−1)-dimensional subspace of V. Write k_so=m(m−1)/2.

**Theorem 4 (generic real incidence theorem).** Let m>=4 and
  2m+1 <=p<=D.                                          (4)
Then there is an OPEN DENSE full-measure semialgebraic subset of the real Grassmannian of p-dimensional operator spaces L⊂S^m containing I, such that
  rank(omega_T|L)>=4   for EVERY T∈so(m)\{0}.          (5)
In particular, generic rational measurement spaces L satisfying (4) admit NO two-MASA inclusion L⊗I_r⊂D1+D2 for ANY r, with either basis chosen arbitrarily.

This includes generic 'balanced dense' measurement spaces with p comparable to D/2, and also source spaces of dimension only 2m+1 (linear in m).

### Proof: incidence dimension count with an exact lower codimension

Fix a nonzero real skew T. By Lemma 2, omega_T on V has rank R=2r>=2m−2, so r>=m−1. Let K=rad omega_T and h=dim K=n−2r.

If the restriction of omega_T to an l-plane L_0⊂V has rank<=2, then L_0 contains an omega_T-ISOTROPIC (l−1)-plane S. To see this, the radical of a rank<=2 alternating form on L_0 has codimension<=2; adjoining one more direction gives an isotropic hyperplane (or choose an arbitrary hyperplane if the form is zero).

Set a=l−1 and stratify such isotropic a-planes S by t=dim projection of S to the 2r-dimensional symplectic quotient V/K. One necessarily has
  0<=t<=min(a,r),  b:=a−t<=h.
The t-dimensional projected plane must be isotropic in a 2r-dimensional symplectic vector space. Its isotropic Grassmannian has dimension
  t(2r−t)−t(t−1)/2.
The radical intersection S∩K is a b-plane in the h-dimensional radical, contributing dimension b(h−b); the graph lift contributes t(h−b). Their sum is a(h−b)=a(h−a+t). Therefore the stratum of isotropic a-planes S has dimension
  I(a,t)=t(2r−t)−t(t−1)/2+a(h−a+t).            (6)

For each S, the family of l-planes L_0 containing S has dimension n−l, since l=a+1. The full Grassmannian Gr(l,V) has dimension l(n−l). Hence the bad set for this fixed T has codimension at least
  C(a,r,t)=a(n−l)−I(a,t)
          =[4ra−4rt−2at−2a+3t²−t]/2.          (7)

As a function of admissible t<=min(a,r), this expression is STRICTLY DECREASING: its derivative is −2r−a+3t−1/2<0. Therefore it is bounded below by its value at t=min(a,r), regardless of the radical-dimension restriction:

 If r>=a,      codim bad >= a(a−3)/2;
 If m−1<=r<a,  codim bad >= r(a−(r+1)/2)−a.

Because a=l−1>=2m−1, the second expression is increasing in r for r<a and is minimized at r=m−1. Uniformly in nonzero T,
  codim bad >= C_min:=(m−2)(2m−1)−m(m−1)/2.  (8)
The first case is even larger. For m>=4,
  C_min−(k_so−1)=(m−1)(m−3)>0.                (9)
(In some small-dimensional strata the isotropic a-plane does not exist at all; then the bad set is empty, and the bound is automatic.)

Now let T vary projectively in P(so(m)), of dimension k_so−1. The incidence subset
  {(L_0,[T]):rank(omega_T|L_0)<=2}
of Gr(l,V)×P(so(m)) has dimension at most
  dim Gr(l,V)−C_min+(k_so−1)
  < dim Gr(l,V)
by (9). Its projection to Gr(l,V) is therefore a semialgebraic subset of strictly smaller dimension, with empty interior and measure zero. It is also CLOSED: the condition rank<=2 is the vanishing of all 4×4 Pfaffians, and the projective parameter space is compact. Thus its complement is nonempty, open, dense and full-measure.

Rational subspaces L_0 are dense in real Grassmannian charts; they can be chosen in this complement. Adding the rational identity gives rational L with the theorem's property. Apply Theorem 1 to finish. QED.

## 4. Consequence for positive PSD marginal quotients (precise scope)

Let A:S^m→R^p be a trace-controlled linear measurement map with range(A*)=L as in Theorem 4, and let r be arbitrary. Let D:S^(mr)→S^m be ORDINARY partial trace over R^r. Suppose a two-ONB PSD fibre
  T={Y>=0:diag_B1(Y)=a, diag_B2(Y)=c}
has an ambient POSITIVE-DEFINITE feasible matrix Y_0>0, and all its decoded feasible matrices obey the source equations:
  D(T)⊂{X:A(X)=b}.

Then this is IMPOSSIBLE for L satisfying (5). Indeed the affine tangent space at Y_0 is precisely the kernel of the two-basis linear measurement map; each such direction H can be perturbed in both signs while remaining PSD. Soundness forces A(D(H))=0 for all tangent H. By finite linear duality,
  D*(range A*) = L⊗I_r ⊂ span{B1 projectors,B2 projectors}
               = D1+D2,
contradicting Theorem 4.

Thus the entire 'ordinary partial-trace decoder, choose two arbitrary global bases with strictly feasible lifted target' strategy is GENERICALLY IMPOSSIBLE regardless of tensor ancilla order, NOT ONLY when the first ONB is maximally entangled (the older obstruction in Milestone 20). It excludes even source SOUNDNESS, before requiring exact PSD surjectivity or sharp recovery moduli.

The theorem does NOT apply when the lifted feasible PSD fibre has no full-rank point on the whole tensor space: one must then restrict to its minimal face, changing the compressed adjoint observables to P_E(H⊗I_r)P_E. A genuinely different positive decoder also escapes the specific operator inclusion condition. This is why Theorem 4 is NOT an architecture-independent impossibility for unrestricted quadratic-size SDP universality.

## 5. Reproducibility and audit points

1. The decomposable-form rank<=2 condition is a PROPERTY OF EVERY TWO-MASA SUM, and does not depend on overlap zero/nonzero or which basis is used.
2. The matrix-element skew reductions T_ij span so(m) for EVERY complete real ONB of R^(mr), because skew operators have zero diagonal in any real ONB.
3. The source scalar identity lies in the radical of omega_T, so passing to traceless subspaces does not lose any commutator rank.
4. The full symmetric rank bound is PROVED by complexifying a real skew matrix and counting eigenvalue sums; it does not assume a generic skew T.
5. The isotropic Grassmannian formula accounts explicitly for radical intersections, instead of silently treating omega_T as nondegenerate.
6. The incidence codimension remains uniform as rank omega_T varies. For m>=4, its lower bound exceeds the real projective dimension of all possible skew T, giving a genuinely OPEN DENSE conclusion.
7. The PSD marginal corollary requires a full-rank ambient feasible point. For a singular lifted face, the full tensor source observables may compress to a different operator system, and the no-go cannot be copied without proof.
8. Arbitrary positive maps, nonlinear decoders, exact-affine retractions with matrix-valued companions and many-to-one quotient fibres of singular support are outside the theorem.
9. All arguments are in REAL symmetric/skew matrices; complex Hermitian cases may have a different diagonal-skew mechanism.
10. Literature: two-MASA sums, matrix commutators and quantum marginal tomography are related, but no exhaustive priority audit has been performed. This proof is self-contained and remains subject to external refereeing.
