# Milestone 27 — fully sharp two-basis transfer for EVERY trace-controlled real PSD linear inverse problem

Date 2026-11-08. This is the rigorous synthesis of the earlier codimension-adaptive rank-one Parseval compiler and the NEW sharp no-admissible-ONB theorem in Milestone 26. It closes the arbitrary-source SHARP MODULUS transfer problem with polynomial output order, not the separately disproved strong-retract universal quadratic-order conjecture.

## Theorem (general quantitative polynomial-size two-basis universality)

Let A:S^m->R^p be a real linear map satisfying
  ker A intersect S^m_+={0},
and let b be a nonempty feasible datum, with F_b={X>=0:A(X)=b}.
Equivalently, some H=A* y is positive definite. Apply a fixed congruence so I_m belongs to the measurement space L=range A*. Put
  s=codim L,  t=max{k>=1:k(k+1)/2<=s+1},
  r=2t+1, d=mr, D_d=d(d+1)/2, q=D_d-s.
Then there is a finite algebraic construction of two REAL orthonormal bases in dimension
  N<=12q-d+4=6d²+5d-12s+4<=150m²(s+1)<=O(m^4),
an affine positive encoder E:S^m_+->S^N_+, a positive linear decoder D:S^N->S^m, and a data encoder Phi with the following properties for EVERY feasible b:

(1) {Y>=0:A_U(Y)=Phi(b)}=E(F_b) among ALL ambient PSD ranks, for the FULL exact fibre, including nonsingleton fibres.
(2) D(E(X))=X, the original and final Frobenius distances are comparable by explicit fixed-instance positive constants. After trace-normalizing the original variable, the final encoded rank is
  rank E(X)=r rank(X)+1.
(3) Every final observation is strictly positive (including at X=0) and every basis-change overlap U_ij is nonzero. The bases can be chosen genuinely different and nonreflection via a small equal-weight output rotation.
(4) Every original cost C has an explicit ambient adjoint cost C_tilde so
  <C_tilde,Y>=<C,D(Y)> for EVERY symmetric ambient Y.
(5) Write omega_A and omega_U for PSD distance-to-feasible-set worst-case moduli. There exist explicit finite positive constants c,C depending on the given frame, trace normalization and nonzero singular gaps, such that
  c[omega_A(c delta)+sqrt(delta)] <= omega_U(delta)
      <= C[omega_A(C delta)+sqrt(delta)]
for all sufficiently small delta>0 if b!=0; the analogous zero-fibre law is omega_U(delta)~delta.
Thus
  omega_U(delta) ~ omega_A(delta)+sqrt(delta) (b!=0).
The optimal local error exponent is ATTAINED and obeys
  alpha_U=min(alpha_A,1/2) for b!=0,
  alpha_U=1 for b=0.
In particular if alpha_A<1, then alpha_A<=1/2 and alpha_U=alpha_A, preserving every non-Lipschitz exponent and recovery modulus up to constants.

This theorem is compatible with the generic N=Omega(m^(8/3)) obstruction of Milestones 07/08 for GLOBAL positive exact face-retract encodings. It does NOT claim N=O(m²+p) for arbitrary dense s=Theta(m²), which those no-go results rule out in the same strong model.

## Proof step I — codimension-adaptive rank-one Parseval compiler

Consider the tensor order d=mr and unnormalized real partial trace T:S^d->S^m. Define the operator system
  W_L={Z in S^d:T(Z) in L},
  W_L^perp={H tensor I_r:H in L^perp}.
It has dimension q=D_d-s and contains I_d.

We reproduce the key existence argument (the detailed algebraic construction is in CODIMENSION_TWO_UNIVERSAL_THEOREM.md, Part 3, inherited from the earlier dense_quadratic research).

The compact trace-one spectrahedron C={B>=0:B in L,tr B=1} contains I/m in its relative interior. An extreme point B with rank k has no nonzero traceless symmetric perturbation supported on ran B and lying in L. The supported symmetric space has dimension k(k+1)/2; the codimension of L is s, hence k(k+1)/2<=s+1. Therefore every extreme point has rank at most t. Every B>=0 in L is a positive sum of rank<=t positive matrices in L by compact convex generation, with finite algebraic rank-reduction.

Choose finitely many such low-rank PSD matrices C_j spanning L and a positive rank<=t decomposition I=sum_i A_i with the supports E_i=ran A_i spanning R^m. Give small positive weights to all pairs A_i+A_j, of rank <=2t<r, and adjust singleton weights to retain the identity. Together with small positive weights of the C_j, this gives a finite positive decomposition I=sum_v c_v B_v, where each B_v belongs L_+, has rank <r, the B_v span L, and all pair supports E_i+E_j are included.

For each B_v select an m-by-r real factor V_v with V_v V_v^T=B_v. All right-orthogonal rank-one projectors vec(V_v O)vec(V_v O)^T have partial trace B_v and hence belong W_L. The rectangular Stiefel lemma states that for a rank-k B_v with k<r, a symmetric operator annihilating all such orbit projectors has compression to E_v tensor R^r of the form H_E tensor I_r, with <H_E,B_v>=0. Its proof independently changes signs of orthonormal Stiefel rows to force off-diagonal ancilla blocks scalar and rotates one row through arbitrary two-planes while placing other rows outside that plane (possible because r>=k+1) to force diagonal ancilla blocks scalar.

Applying this lemma to all pair supports E_i+E_j forces any common annihilator Z to equal H tensor I_r globally. Applying it to the spanning B_v then forces H in L^perp. Hence the full span of these allowed orbit projectors is EXACTLY W_L.

A finite rational orthogonal sign/permutation twirl satisfies
  average_O vec(V O)vec(V O)^T=(B_v tensor I_r)/r.
Weighting all orbits by c_v r makes their total frame operator I_d. Select finitely many algebraic right rotations to attain the complete orbit span (an exact finite rank test stops the search). Preserve exact twirls at every selection. Finally reserve half of q independent projectors and apply conic Caratheodory sparsification to the remaining positive identity representation. This yields a positive Parseval rank-one frame G in R^d with
  GG^T=I_d,
  M<=2q,
  span{g_jg_j^T}=W_L.
Any zero frame column is dropped.

## Proof step II — original-to-compiler modulus equivalence with positive decoding

Let J(X)=X tensor I_r and rho(Z)=T(Z)/r. Then J is positive, rho is positive, rho J=id and
  ||J(X)-J(X')||_F=sqrt(r)||X-X'||_F.

Write M_G(Z)=(g_j^T Zg_j)_j. Its exact fibre at J(F_b) is J(F_b), because
  ker M_G=W_L^perp=J(ker A)
and positivity of J(X) is equivalent to positivity of X.

The linear maps
  Z -> M_G(Z),  Z -> (Z-J(rho Z), A(rho Z))
have exactly the same kernel J(ker A). On the finite-dimensional quotient they induce equivalent Euclidean norms. Thus there is a computable C_0>0 such that for every Z>=0, putting X=rho Z>=0,
  ||Z-J(X)||_F+||A(X)-b|| <=C_0 ||M_G(Z)-M_G(J(X_*))||.
It follows
  omega_G(t) <=sqrt(r)omega_A(C_0t)+C_0t.
Conversely restriction Z=J(X) gives
  omega_G(t)>=sqrt(r)omega_A(t/C_1)
for the explicit operator bound C_1=||M_G J||/sigma_min^+(A) (or any finite valid source residual comparison constant). A trace-controlled PSD fibre has omega_A(t)>=c t for small t (test X_*+epsilon I), so the linear term is dominated and
  omega_G(t)~omega_A(t).

## Proof step III — the stabilized Naimark frame and final two bases

Apply Milestone 26 to the above G. In enlarged intermediate order n=M, form P=G^T G, Q=I-P, and take an ONB h_a of Q. The balanced Parseval frame
  [e_1,...,e_M, Pe_1,...,Pe_M, h_1,...,h_(M-d)]/sqrt(2)
has L=3M-d columns. Every column's rank-one projector pulls back under G to an original source g_jg_j^T or zero. The source-only Pe_j projectors and pure-exterior h_a projectors are both present and are exactly what prevents the extra alpha/2 loss of the naive two-zero dilation.

The signed anchored two-basis lift of this augmented frame, using the standard e_j ONB, has order
  N<=6M-d+4<=12q-d+4,
strictly positive observations, all nonzero basis overlaps, exact full-cone fibre and a positive decoder. Milestone 26 proves the ALL-AMBIENT sharp upper bound
  omega_U(t)<=omega_G(C_2 t)+C_3 sqrt(t),
and both lower bounds
  omega_U(t)>=omega_G(t/C_4),
  omega_U(t)>=c_5 sqrt(t) when b!=0,
by an explicit rank-preserving PSD cross-block Gram-factorization curve. At zero b the anchor-only rank-one target is Lipschitz.

Combining with Step II gives
  omega_U(t)~omega_A(t)+sqrt(t),
the asserted rank amplification r rank X+1, exact cost identity, and nonzero/positive data. Finally normalization by a single fixed positive target trace does not change any local exponent.

The numeric dimension constant follows from
  r=2t+1<=3sqrt(2(s+1)), d=mr,
and
  6d²+5d+4<=108m²(s+1)+22m²(s+1)+4m²(s+1)<150m²(s+1)
for every m>=1 and s>=0. This is conservative, not dimension-optimal.

## Proof step IV — exponent attainment and non-Lipschitz preservation

The PSD feasible fibres and residual-bounded sublevels are semialgebraic and compact because trace is measured. The worst-case modulus is a one-variable positive semialgebraic function tending to zero; it has an attained leading rational Puiseux power alpha in (0,1]. A general PSD tangent-cone argument (earlier Track 02 proof) shows that every non-Lipschitz source modulus obeys omega_A(t)>=c sqrt(t), so the added sqrt term never alters a non-Lipschitz modulus. For a nonzero Lipschitz source omega_A(t)~t, the rank-2-or-higher final target's invisible cross curve forces sharp exponent 1/2.

## Computational interpretation and honest limits

The construction uses finite algebraic operations, rational orthogonal twirls, finite rank tests, conic support reduction, and a finite rational grid to avoid zero overlaps. Polynomial arithmetic-operation complexity holds for suitably specified algebraic oracles and conditioning promises. Quantitative constants can be evaluated using the least positive singular values of the compiler/augmented analysis maps and the explicit exposing certificate gap. No unqualified polynomial Turing bit complexity is claimed for arbitrarily ill-conditioned rational inputs. The source trace-normalizing congruence must include its own positive spectral gap as an input condition parameter.

The result fully resolves the precise SHARPNESS problem for universal rank-one-compilable trace-controlled PSD inverse problems, at polynomial (not necessarily quadratic) dimension. The separate unrestricted near-quadratic dimension problem remains unresolved for arbitrary weak many-to-one reductions, and is ruled out for generic dense systems within the globally positive exact-retract model by Milestones 07/08.

## Adversarial audit

1. A Parseval compiler alone need NOT have an admissible ONB; Milestone 26 creates one at order M using the source frame itself and independently measured pure-source/pure-exterior projectors.
2. Two-zero exposure can introduce source residuals of order sqrt(delta). Milestone 26 repairs this at the linear DATA level before any PSD compression estimates.
3. The signed final certificate excludes ALL off-face exact PSD competitors, and the source-only frame outputs constrain every arbitrary-rank noisy competitor at O(delta), not just embedded source curves.
4. The generic superquadratic lower bound and the polynomial-size upper bound are consistent. We do not infer N=O(m²+p) from fixed-codimension quadratic claims.
5. The no-zero-overlap and positive-data properties hold with a nontrivial anchor, not with zero first/second diagonal observations.
6. The zero source is treated separately and remains Lipschitz; indiscriminately applying the nonzero sqrt law at zero would be false.
7. Novelty relative to Naimark dilation and conic error-bound literature remains a qualified claim pending independent external referee review.
