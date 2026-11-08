# Milestone 28 — elementary, independently proved universal rank-one Parseval compiler at the sharp full-rank Stiefel ancilla r=m+1

Date 2026-11-08. This eliminates dependence on the earlier codimension-adaptive extreme-point/pair-support compiler for GENERAL sharp polynomial-size two-basis universality. It gives a simpler universal fallback at O(m⁴) order, with a sharp minimal ancilla statement inside the full-rank Stiefel orbit architecture. For fixed small codimension the earlier codimension-adaptive compiler is more efficient.

## 1. Theorem — every real operator system containing identity has a finite real Parseval rank-one dilation in order m(m+1)

Let L<=S^m be any real linear subspace with I_m in L. Put
  r=m+1,  d=mr=m(m+1),
  s=codim L, q=d(d+1)/2-s,
  W_L={Z in S^d:T(Z) in L},
where T:S^(m r)->S^m is the UNNORMALIZED real partial trace over the r-dimensional ancilla.

Then there is an explicitly selectable FINITE rank-one Parseval frame G=(g_j) in R^{d x M} with
  GG^T=I_d,
  0<||g_j||,
  span{g_j g_j^T}=W_L,
  M<=2q.
This works for ALL operator systems L containing I, whether sparse, dense, noncommuting or generic. No admissible ONB inside W_L is required; Milestone 26 constructs one after a Naimark stabilization.

Combining this theorem with Milestone 26 gives, for EVERY trace-controlled real PSD linear inverse problem A:S^m->R^p, a sharp two-basis embedding of order
  N<=12q-d+4 <= 6m²(m+1)²+5m(m+1)+4,
with all target observations positive, all basis overlaps nonzero, positive decoding, exact full feasible fibres, arbitrary ambient PSD ranks, exact source-objective identity and the SHARP modulus law
  omega_U(t)~omega_A(t)+sqrt(t)  for nonzero source target,
  omega_U(t)~t for the zero target.
Thus the universality/sharpness corollary is now proved by an elementary full-rank-Stiefel route independent of the prior low-rank extreme-ray construction. This theorem does NOT establish the unrestricted O(m²+p) dimension target, which is ruled out in the global exact positive-retract model for generic dense inputs by Milestones 07/08.

## 2. Rectangular Stiefel orbit spanning lemma (self-contained)

Let r>=m+1. For each real m-by-r matrix Q with QQ^T=I_m, let q_Q=vec(Q) with row-major vectorization. Then
  span{q_Q q_Q^T:QQ^T=I_m}
   ={Z in S^(mr):T(Z) in R I_m}.                     (1)

**Proof.** Suppose W in S^(mr) satisfies q_Q^T W q_Q=0 for every row-orthonormal Q. View W as m-by-m blocks W_ij of size r. Independently changing the signs of the ith and jth rows of Q and taking the four-term alternating difference isolates
  u^T W_ij v=0 for all unit u perpendicular to v.
A real linear map satisfying u^T A v=0 for every u perpendicular to v is scalar identity (Av belongs span v for every v; using v=e_i and v=e_i+e_j shows all eigenvalues agree). Thus W_ij=c_ij I_r for all i!=j.

For each i and each 2-plane E in R^r, choose the other m-1 orthonormal row vectors in E^perp; this is possible because r-2>=m-1. Vary the ith unit row vector inside E while keeping the other rows fixed. The previously shown off-diagonal blocks contribute zero because rows are orthogonal, so the ith diagonal quadratic form is constant on every two-dimensional unit circle. This forces W_ii=c_ii I_r. Consequently W=H tensor I_r for some symmetric H. Evaluating on QQ^T=I gives
  0=q_Q^T W q_Q=tr(HQQ^T)=tr H.
Hence the orbit-annihilator is exactly {H tensor I_r:tr H=0}. This is the orthogonal complement of the right-hand side of (1), proving the lemma. QED.

## 3. Add arbitrary measurement directions without losing Parseval tightness

Choose a linear basis
  L=span{I,H_1,...,H_h},
where each H_i is traceless, h=dim L-1. Scale H_i so ||H_i||_op<=1/2. Then
  B_i^+=I+H_i, B_i^-=I-H_i
are positive definite. Also set B_0=I. The family {B_0,B_i^+,B_i^-} lies in L, and its linear span is all of L.

For each such B choose
  V_B=[B^(1/2) , 0_(m x(r-m))] in R^{m x r}.
It has V_B V_B^T=B. For every O in O(r), the rank-one projector
  P_(B,O)=vec(V_B O)vec(V_B O)^T
has partial trace B, so P_(B,O) belongs W_L.

By the Stiefel lemma, the orbit for B_0=I spans W_scalar={Z:T(Z) in R I}. Since the quotient W_L/W_scalar is isomorphic to L/R I under partial trace, and the additional B_i^+ orbits have linearly independent quotient classes H_i, the union of ALL these orbits spans EXACTLY W_L.

## 4. Finite explicit real orthogonal twirling

Let Lh=2^ceil(log2 r) <=2r. Take the first r columns of a real Sylvester Hadamard matrix of order Lh, giving Lh diagonal sign matrices S_a whose signs have pairwise orthogonal column patterns. Let P be the cyclic permutation of r coordinates and define
  T={S_a P^k: a=1,...,Lh, k=0,...,r-1}.
Every member is a REAL rational orthogonal matrix, |T|=Lh r<=2r². For EVERY real m-by-r V,
  (1/|T|) sum_{T0 in T} vec(V T0)vec(V T0)^T
    =(VV^T tensor I_r)/r.                           (2)
Indeed the sign average removes all distinct ancilla coordinate products, and the cyclic average equalizes the remaining diagonal entries.

Fix any finitely many base right rotations R_1,...,R_n in O(r) for a given B. The full twirl blocks {vec(V_B R_j T0):T0 in T} still average to (B tensor I_r)/r for each j, independent of R_j. Rational Cayley rotations with a fixed reflection are dense in O(r), so one can select FINITELY many such base rotations for each B until their rank-one projector span is W_L, by an exact rank test. Finiteness follows from the full-orbit spanning result; no positivity argument is hidden here.

Let n_B be the number of selected base rotations of type B. For h>=1 choose positive weights
  c_0=r/2,
  c_(i,+)=c_(i,-)=r/(4h).
For h=0 choose c_0=r. Then
  sum_B c_B B=r I_m.
Scale each vector vec(V_B R_j T0) by
  sqrt(c_B/(n_B |T|)).
Summing its outer product over all B,j,T0 and applying (2) gives EXACTLY
  (1/r) sum_B c_B(B tensor I_r)=I_(mr).
Thus the finite family is Parseval and its projector span is precisely W_L.

## 5. Reduce to M<=2q without losing the span

Let q=dim W_L. Select q independent projectors from the positive Parseval family and reserve half of their positive coefficients. The residual PSD identity representation is a nonnegative linear combination of the original projectors. If more than q residual projectors have positive coefficients, their q-dimensional linear dependence has coefficients of both signs because the trace of a projector is positive. Move along the dependence until one coefficient vanishes while preserving nonnegativity and the represented matrix. Repeat until at most q positive residual coefficients remain. Add back the reserved q projectors. The resulting Parseval family has at most 2q nonzero columns, and the reserved independent projectors guarantee full span W_L.

This conic support reduction is finite exact linear algebra; it does not require any admissible ONB in the original order d.

## 6. Sharpness of r=m+1 in the scalar full-rank purification architecture

Let L=R I_m. If r<m and v=vec(V) is a nonzero allowed rank-one vector with VV^T in L, then VV^T=cI_m for c>0, which has rank m, contradicting rank(VV^T)<=r. Thus no nonzero allowed projectors exist.

If r=m, every nonzero allowed V satisfies VV^T=cI_m, so V=sqrt(c) O for a square orthogonal O. For any nonzero traceless symmetric ancilla matrix D in S^m, the operator I_m tensor D satisfies
  vec(V)^T(I_m tensor D)vec(V)
    =tr(D V^T V)=c tr D=0.
Hence this nonzero operator annihilates ALL admissible rank-one projectors, but it does not belong W_L^perp={H tensor I_m:tr H=0}. Thus the allowable projectors cannot span W_L. Therefore r=m+1 is the EXACT minimum ancilla dimension for a rank-one spanning compiler of the scalar operator system through ordinary partial trace, not merely sufficient.

This lower bound does NOT apply to different non-tensor positive encodings or to general source operator systems of higher dimension.

## 7. Quantitative source-fibre equivalence and final transfer

The positive tensor encoder J(X)=X tensor I_r and positive decoder rho(Z)=T(Z)/r satisfy rho J=id, ||J(X)||_F=sqrt(r)||X||_F. Since
  ker M_G=W_L^perp=J(ker A),
the rank-one compressed exact fibre is J(F_b). The two linear maps on symmetric matrices
  Z->M_G(Z)-M_G(J(X_*)),
  Z->(Z-J(rho Z), A(rho Z)-b)
have exactly the same kernel, hence possess equivalent Euclidean quotient norms with explicit finite singular-value constants. Positive rho therefore gives full-ambient O(delta) decoded source residual and O(delta) off-model retraction distance. It follows
  omega_compiler(t)~omega_A(t).
Apply Milestone 26 to G. Its balanced source-only/exterior-only Naimark enrichment creates an admissible ONB at order M, and its signed outer dilation yields
  omega_final(t)~omega_compiler(t)+sqrt(t)
for nonzero feasible data, zero-source Lipschitz, positive measurements, nonzero overlaps, exact objectives and full ambient PSD fibres. Combining gives the claimed sharp universal law with dimension <=12q-d+4.

## 8. Effective construction and scope

A finite exact construction exists by enumerating rational Cayley rotations and testing the rank until W_L is spanned. Expected-polynomial arithmetic-operation selection can be obtained by sampling skew-matrix Cayley parameters from a polynomial-size rational grid: whenever the span is deficient, some orbit projector has a nonzero polynomial rank-increment minor; after clearing the determinant of (I+T) its degree is O(r), so a Schwartz--Zippel bound gives constant success probability from a sufficiently large grid. Selecting complete twirl blocks retains Parseval tightness after every iteration. Conic reduction ends with M<=2q.

Uniform Turing bit-polynomial time for arbitrary rational inputs is NOT claimed without positive spectral/separation and trace-normalization promises. No arithmetic complexity claim is used to prove the exact fibre or modulus results.

The proof is real throughout. It uses no full-rank complex Hilbert space, no conjectural unitary error basis, no strict feasibility of the source fibre, and no unsupported simultaneous hollowization claim. All-rank ambient competitors are covered by the positive decoder and exposing certificate in Milestone 26.

Novelty caveat: Stiefel orbit identities, Naimark dilation, conic Caratheodory, and symmetric/orthogonal invariant arguments have established precedents. The combined scalar-orbit + paired full-rank perturbations, positive tight-frame sparsification, and its use in the sharp two-basis transfer theorem are candidate new contributions pending full external prior-art review.
