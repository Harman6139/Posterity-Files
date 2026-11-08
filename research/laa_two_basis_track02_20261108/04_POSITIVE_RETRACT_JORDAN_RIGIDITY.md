# Milestone 04 — positive retracts of real PSD cones have an exact matrix-amplification summand

2026-11-08. This is a rigorous finite-dimensional structural theorem, not a proof of unrestricted quadratic-size two-basis universality. Its operator-algebraic roots lie in Kadison's inequality and the structure of reversible positive maps, so novelty/priority requires additional literature review.

## Theorem (faithful Jordan amplification in every positive linear PSD retract)

Let J:S^m -> S^d and D:S^d -> S^m be real linear maps with
  J(S^m_+) subset S^d_+, D(S^d_+) subset S^m_+, D o J = id.
Replace the output by the support of J(I_m), so J(I_m) is positive definite in S^d. Let R=J(I_m)^(1/2), and define
  Phi(X)=R^(-1) J(X) R^(-1),
  Delta(Y)=D(R Y R).
Then Phi and Delta are positive, Phi(I_m)=I_d, Delta(I_d)=I_m and Delta o Phi=id.

Put A=Delta*(I_m), a PSD d-by-d matrix, and let E be the orthogonal projection onto ran A. Then there exists an integer t>=1 and an orthogonal identification ran E=R^m tensor R^t such that
  E Phi(X) E = X tensor I_t                     (1)
for every X in S^m. Moreover the compression of Delta to ran E is a faithful positive unital left inverse of this tensor amplification, and the discarded component is invisible to Delta:
  Delta(Y)=Delta(EYE)                             (2)
for every Y in S^d.

In particular rank E=mt and mt<=d. Every positive linear encoder/decoder pair contains a canonical real symmetric m-by-m matrix subsystem, even when the decoder is not given by a principal matrix block. After a fixed positive-definite congruence and orthogonal coordinate change, one may select any unit ancilla vector e in R^t and obtain an exact compression
  V^T J(X) V=X
with V=R^(-1) O( id_R^m tensor e) (where O identifies ran E with R^m tensor R^t).

The result does NOT require J or Delta to be completely positive, trace preserving, or self-adjoint maps on matrix spaces. It does not assert that the entire J is a tensor amplification: extra positive companion information may lie in the Delta-invisible complement.

### Lemma 1 (Kadison square inequality in the real symmetric setting)

If T:S^a -> S^b is positive and unital, then T(H^2)>=T(H)^2 for every H in S^a.

Proof. Spectrally write H=sum_i lambda_i P_i. Put M_i=T(P_i)>=0, sum_i M_i=I_b. The linear map V:z -> (M_1^(1/2)z,...,M_k^(1/2)z) is an isometry. Let Z=diag(lambda_1 I_b,...,lambda_k I_b). Then T(H)=V^T ZV and T(H^2)=V^T Z^2 V. Their difference is V^T Z(I-VV^T) Z V>=0. QED.

### Lemma 2 (support of a positive decoder)

If Delta:S^d -> S^m is positive, A=Delta*(I_m)>=0 and E=supp A, then Delta(Y)=Delta(EYE) for every symmetric Y.

Proof. For u in ker A, Delta(uu^T)>=0 has trace u^T A u=0, hence Delta(uu^T)=0. For any v, positivity of Delta((u+tv)(u+tv)^T) for all real t, and its expansion t Delta(uv^T+vu^T)+t^2 Delta(vv^T), force Delta(uv^T+vu^T)=0 by sending t to 0 with either sign. Rank-one symmetric matrices and these cross terms span the discarded complement. QED.

### Lemma 3 (faithful positive inverse forces Jordan homomorphism)

Define Psi(X)=E Phi(X) E on ran E and delta(Y)=Delta(EYE). Then Psi and delta are unital positive, delta o Psi=id, and delta is faithful: for Y>=0 on ran E, delta(Y)=0 implies Y=0.

Proof of faithfulness: A is positive definite on ran E and tr delta(Y)=tr(AY); if Y>=0 nonzero the trace is strictly positive.

By Lemma 1 for Psi, B_X=Psi(X^2)-Psi(X)^2>=0. By Lemma 1 for delta and delta(Psi(X))=X,
  delta(Psi(X)^2)>=X^2,
while delta(Psi(X^2))=X^2, hence
  0<=delta(B_X)=X^2-delta(Psi(X)^2)<=0.
Thus delta(B_X)=0, and faithfulness forces B_X=0. Therefore Psi(X^2)=Psi(X)^2 for every X. Polarization gives
  Psi((XY+YX)/2)=(Psi(X)Psi(Y)+Psi(Y)Psi(X))/2.
QED.

### Lemma 4 (classification of unital real symmetric Jordan embeddings)

If Psi:S^m -> S^n is linear, unital and satisfies Psi(X^2)=Psi(X)^2, then n=mt for an integer t>=1 and, up to orthogonal similarity, Psi(X)=X tensor I_t.

Proof. Let e_i denote the coordinate rank-one projections, and P_i=Psi(e_i). Then P_i are orthogonal projections summing to I_n. From Psi(e_i o e_j)=0 for i!=j we obtain (P_iP_j+P_jP_i)/2=0; multiplying by P_i on both sides gives P_iP_jP_i=0, hence P_iP_j=0.

Let E_ij=e_i e_j^T+e_j e_i^T for i!=j and F_ij=Psi(E_ij). Jordan product with the e_k shows F_ij has support only in P_i direct-sum P_j and consists solely of its off-diagonal blocks. The square identity F_ij^2=P_i+P_j makes its (i,j) block an orthogonal isometry between ran P_i and ran P_j, so all P_i have the same rank t>=1 (nonzero because Psi has a left inverse).

Choose an orthonormal basis in ran P_1, and use the isometry block of F_1j to transport it to ran P_j. In these bases F_1j=E_1j tensor I_t. For i,j distinct >1, the identity E_1i o E_1j=E_ij/2 forces F_ij=E_ij tensor I_t. Diagonal projections are e_i tensor I_t by construction. These elements span S^m, proving the claim. The m=2 case uses only F_12, with the same argument. The m=1 case is immediate. QED.

### Corollary (canonical unavoidable matrix subsystem)

Combine Lemmas 2-4. There is an orthogonal embedding W:R^m tensor R^t -> R^d with
  W^T Phi(X) W=X tensor I_t.
For unit e in R^t, set V=R^(-1) W(id tensor e). Then V^T J(X)V=X. This V is not required to have orthonormal columns; congruence normalizes it. It shows that a general positive decoder cannot evade the canonical source PSD block: the correct remaining freedom is a positive matrix-valued companion and its mixed blocks.

### Hostile audit and limitations

1. The proof does NOT infer Psi(X)^2=Psi(X^2) solely from a nonfaithful decoder. It first compresses to support of Delta*(I), where the decoder is faithful.
2. Both maps become unital only after restricting to the support of J(I) and congruence by its positive square root. This step is essential.
3. Kadison's inequality holds for positive unital maps on real symmetric matrices; the spectral/isometry proof is included rather than assuming 2-positivity.
4. The classification is for the Jordan algebra S^m and is proved directly from matrix units. No classification theorem is imported.
5. The compression factor V generally depends on J,D and need not be an orthogonal embedding before congruence.
6. The theorem does not prove an O(m^4) lower bound for arbitrary positive retracts, and does not rule out O(m^2) two-basis encodings with sophisticated matrix-valued auxiliaries.

References for context: Kadison square inequality and positive projections/Jordan algebra structure; see Seetharama Gowda (Linear Algebra Appl., 2017) and Westerbaan--Westerbaan--van de Wetering (2018) on Euclidean Jordan maps. The finite-dimensional theorem is proved here independently, but priority is not claimed.
