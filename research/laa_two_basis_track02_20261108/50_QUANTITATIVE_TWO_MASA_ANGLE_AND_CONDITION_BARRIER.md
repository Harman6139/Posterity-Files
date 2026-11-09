# Milestone 50 — an EXPLICIT robustness/conditioning barrier for approximating ordinary partial-trace observables by two ONB diagonals

Track 02, 2026-11-09. Builds directly on the complete generic geometric obstruction in Milestone 49. This is an analytic quantitative theorem: any approximate two-MASA representation of a generically rich source measurement space must have a nontrivial approximation error OR a large coefficient splitting norm. The result holds for arbitrary first and second orthonormal bases and every tensor ancilla order r. It is not a lower bound for arbitrary positive decoders or singular-face quotients.

**Threshold update:** The rank-four commutator margin gamma_4(L)>0 holds on an open dense family already when dimL>=m+3, m>=4, by Milestone 53. The p>=2m+1 threshold originally cited here is obsolete.

## 1. Statement

Let m>=3, r>=1, N=mr, and L⊂S^m be a real linear operator space. For T∈so(m) define the bilinear commutator form
  omega_T(H,K)=<T,[H,K]>_F,
and represent it as a real skew-adjoint operator on the Frobenius Hilbert space L. Define
  gamma_4(L)=min_{T∈so(m),||T||_F=1} sigma_4(omega_T|_L),
where sigma_4 denotes its fourth largest singular value, with zeros padded if dimL<4.

Suppose gamma_4(L)>0. Milestone 49 proves this for an open dense real semialgebraic family of source spaces containing I and of dimension p>=2m+1 when m>=4; it also holds deterministically for codimension s<=m-3. The compact minimization makes gamma_4(L) strictly positive for each such fixed L.

Let D1,D2⊂S^N be the real diagonal operator spaces of ANY two real ONBs. Suppose there exist REAL LINEAR maps
  H -> A_H∈D1,  H ->B_H∈D2
with approximation and decomposition bounds
  ||H⊗I_r−A_H−B_H||_op <=epsilon ||H||_F,
  ||A_H||_op+||B_H||_op <=K ||H||_F
for every H∈L, where epsilon>=0,K>=0.

**Theorem.** Necessarily
  8K epsilon+2epsilon²
    >=gamma_4(L)*sqrt[(m-1)/(2(mr-1))].             (1)

In particular, if 0<=epsilon<=1, then
  epsilon >= gamma_4(L)/(8K+2)
                  *sqrt[(m-1)/(2(mr-1))].           (2)

Thus an all-tolerance approximation with epsilon->0 for a fixed m,r,L of positive gamma_4 REQUIRES K->infinity. More generally, at growing ancilla order r the necessary tolerance/conditioning tradeoff has an explicit factor of order 1/sqrt(r). The output is an operator-inclusion conditioning no-go, not by itself an approximation-recovery error lower bound for an arbitrary nonlinear SDP solver.

## 2. Commutator decomposability and explicit error bound

Fix a first ONB ψ_i (i=1,...,N). Let
  X_H=H⊗I_r,
  E_H=X_H−A_H−B_H.
For i≠j define the linear forms
  ell_ij(H)=<ψ_i,X_H ψ_j>,
  f_ij(H)=<ψ_i,A_H ψ_i>−<ψ_j,A_H ψ_j>.

Because all A_H commute and all B_H commute, the commutator of the APPROXIMANTS is
  [A_H+B_H,A_K+B_K]=[A_H,B_K]+[B_H,A_K].
The (i,j) first-basis matrix entry is
  f_ij(H) <ψ_i,B_K ψ_j>
    −f_ij(K)<ψ_i,B_H ψ_j>.
Since A_H has no offdiagonal entry in the first basis and X_H=A_H+B_H+E_H,
  <ψ_i,B_H ψ_j>=ell_ij(H)−<ψ_i,E_H ψ_j>.

Therefore the (i,j) entry of the FULL commutator [X_H,X_K] differs from the decomposable alternating form
  f_ij(H)ell_ij(K)−f_ij(K)ell_ij(H)
by terms bounded (for unit Frobenius H,K) as follows:
(a) replacing B offdiagonal entries by ell costs <=4K epsilon, since |f_ij(H)|<=2||A_H||_op<=2K;
(b) [A_H+B_H,E_K] and [E_H,A_K+B_K] cost together <=4K epsilon by ||[P,Q]||_op<=2||P||_op||Q||_op;
(c) [E_H,E_K] costs <=2epsilon².
Thus the difference has operator norm as an alternating bilinear form on L at most
  8K epsilon+2epsilon².                           (3)
(The bound is UNIFORM over all H,K of unit Frobenius norm, so no extra dimL factor is needed.)

The decomposable form has matrix rank <=2. By the rank-two singular-value approximation bound (Eckart–Young in operator norm),
  sigma_4(omega_(T_ij)|_L)<=8Kepsilon+2epsilon²,   (4)
where T_ij is the skew reduced matrix defined by
  <T,T_ij>_F=<ψ_i,(T⊗I_r)ψ_j>
for every skew T. Sign conventions do not affect the singular values.

By definition of gamma_4 and homogeneity,
  gamma_4(L) ||T_ij||_F <=8Kepsilon+2epsilon²
for EVERY i<j. It remains to show that at least one T_ij has a quantified nonzero norm, independently of which first basis was chosen.

## 3. The reduced-skew matrices form an EXACT tight frame

The map T ->T⊗I_r is an isometric scaled inclusion of real skew matrix spaces, with
  ||T⊗I_r||_F²=r||T||_F².
For ANY complete real ONB ψ_i, the matrix T⊗I_r is skew, so its diagonal entries vanish and
  ||T⊗I_r||_F²
   =2 sum_(i<j) |<ψ_i,(T⊗I_r)ψ_j>|².
Consequently the reduced-skew matrices {T_ij:i<j} defined above satisfy the exact TIGHT FRAME identity
  sum_(i<j) <T,T_ij>_F²=(r/2)||T||_F².        (5)
Polarization says their frame operator on so(m) is exactly (r/2)I.

Taking the trace of that operator identity and writing k=dim so(m)=m(m−1)/2 yields
  sum_(i<j) ||T_ij||_F²=(r/2)k.
There are N(N−1)/2 pairs, so
  max_(i<j)||T_ij||_F²
   >= r k/[N(N−1)]
    = (m−1)/[2(mr−1)].                              (6)

Choose a maximizing pair in (4). Combining (4) and (6) proves (1). If epsilon<=1, then 8Kepsilon+2epsilon²<=(8K+2)epsilon, proving (2). QED.

## 4. Exact scope and numerical interpretation

- gamma_4(L)>0 is a CHECKABLE finite-dimensional semialgebraic condition (minimization over a compact unit sphere); it is not claimed polynomial-time decidable in arbitrary input dimension.
- For generic dense L of dimension p>=2m+1 (m>=4), Milestone 49 supplies strict positivity of gamma_4(L). Its numerical value may be extremely small for ill-conditioned rational inputs; no dimension-only polynomial lower bound is assumed.
- K is the operator norm of the proposed LINEAR decomposition maps into the two MASAs, not the norm of the resulting sum (which could stay bounded by cancellation). The theorem explicitly quantifies how near-parallel MASAs can hide coefficients of diverging size.
- The basis pair is completely arbitrary, and the proof needs neither a reflection nor maximally entangled first basis.
- The ancilla r is completely arbitrary. The 1/sqrt(r) dependence is a necessary robustness scale, not a statement that enlarging r suffices for approximate universality.
- The result tests approximate OPERATOR inclusion L⊗I_r⊂D1+D2, which is necessary for exact PSD marginal soundness at an interior lifted state. To convert it into a bound on a particular approximate SDP algorithm, one must additionally show its soundness/conditioning estimates produce the assumed linear decomposition with parameters epsilon,K.
- No full-ambient PSD recovery modulus, objective decoding, or computational completeness assertion is made here. Those remain separate from the two-MASA bottleneck.
- The tensor-skew tight frame identity is exact for every first ONB and gives a basis-independent certificate of obstruction.
- Published results on two-basis quantum tomography and matrix commutators are contextual; this proof is self-contained and is not externally priority-certified.
