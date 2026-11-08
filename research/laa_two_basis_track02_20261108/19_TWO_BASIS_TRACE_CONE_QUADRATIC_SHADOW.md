# Milestone 19 — genuine order-2m² TWO-BASIS PSD quotient onto the entire trace-one density cone

Date 2026-11-08. This completes the most elementary many-to-one large-slack escape at exact two-basis level, with positive data, no zero basis overlaps, arbitrary ambient PSD competitors, and a positive Lipschitz decoder. It is NOT a universal result for arbitrary intermediate measurement subspaces L.

## Theorem

Fix m>=2 and tau>0. Let r=2m and n=mr=2m². There exist two real orthonormal bases B_1,B_2 of R^n such that (a) every basis vector in BOTH bases has reduced density I_m/m under partial trace over R^r; (b) every overlap between a vector of B_1 and one of B_2 is nonzero; (c) the bases are different and the change of basis matrix is a nontrivial real orthogonal matrix, with generic choices not an involution.

Let the common fixed positive diagonal datum in each basis be tau/n, and put
 T_tau={Y>=0 in S^n:diag_B1(Y)=diag_B2(Y)=(tau/n) 1_n}.
Define D(Y)=Tr_aux Y and E(X)=X tensor I_r/r.

Then
  D(T_tau)={X>=0 in S^m:tr X=tau},
  D(E(X))=X,
  E({X>=0:trX=tau}) subset T_tau,
with completely positive trace-preserving decoder D, positive linear section E, and exact objective identity
  <C,D(Y)>=<C tensor I_r,Y>.
All source and ambient competitor ranks are unrestricted.

For arbitrary Y>=0, let delta be the full two-basis data residual from the uniform target. Then
  |tr(D(Y))-tau|=|trY-tau|<=sqrt(n) delta/sqrt(2)
and, whenever trY>0,
  dist_F(D(Y),{X>=0:trX=tau})<=|trY-tau|<=sqrt(n/2)delta.
For Y=0 the same inequality holds. Thus the positive decoded source residual and feasible-set distance are uniformly LIPSCHITZ, with explicit constant sqrt(n/2).

Moreover, for a generic Q in SO(r) selected as below, every overlap is nonzero, so the two-basis data map has rank 2n-1. The ambient fibre T_tau contains the positive-definite matrix E((tau/m)I_m)=(tau/n)I_n. Its affine dimension is
  dim T_tau = n(n+1)/2-(2n-1).
The source trace-tau body has affine dimension m(m+1)/2-1. The decoder-invisible auxiliary tangent dimension is exactly
  a=n(n+1)/2-2n-m(m+1)/2+2=Theta(m^4).
Thus the enormous auxiliary fibre predicted by Milestone 09 is realized in an honest pair of positive-visibility orthonormal-basis measurements, not merely in a hybrid SDP.

## Proof

1. (Maximally entangled real basis.) Use the realification of the complex Weyl matrices from Milestone 14. The n real basis vectors psi_j are vectorizations of real m-by-2m matrices A_j of full row rank with A_j A_j^T=I_m/m. Therefore every reduced rank-one projector equals I_m/m.

2. (Second basis.) Let Q in SO(r), and define psi_j'=vec(A_j Q). Right orthogonal multiplication preserves the real Hilbert-Schmidt inner product between A_j matrices, so {psi_j'} is a real ONB. It also preserves every row Gram matrix A_j Q Q^T A_j^T=I_m/m.

3. (All overlaps nonzero.) For i,j,
  <psi_i,psi_j'>=tr(A_i^T A_j Q)
is a real linear polynomial in the entries of Q. The coefficient matrix A_i^T A_j has rank m because both A_i and A_j have full row rank, and so is nonzero. The real linear span of SO(r) is all M_r(R) for r>=3 (for example coordinate rotations and even sign changes separate all matrix units; r>=4 here). Hence this polynomial is NOT identically zero on SO(r). Its zero set is a proper closed real algebraic subset. Finitely many such subsets cannot cover the connected smooth manifold SO(r), so their common complement is open dense. Choose Q there, additionally excluding the proper algebraic set of Q for which the transition U=B_1^T(I_m tensor Q)B_1 is an involution or equals a signed permutation. Thus the bases are genuinely distinct and no transition entry vanishes.

4. (Embedded fixed data.) Let X>=0 with trX=tau. For either psi_j=vec(A_j) or psi_j'=vec(A_j Q),
  <psi_j,E(X)psi_j> = (1/r)tr[X A_j A_j^T]=tau/(rm)=tau/n.
Thus E(X) belongs T_tau. It has partial trace X.

5. (Soundness.) For any Y in T_tau, the first diagonal constraints imply trY=tau. Partial trace is positive and trace preserving, so X=D(Y)>=0 and trX=tau. Combining with step 4 proves exact surjectivity.

6. (Lipschitz decoder.) The two measured diagonal residual lists each sum to trY-tau. By Cauchy--Schwarz,
  2(trY-tau)^2 <=n(||r_1||_2^2+||r_2||_2^2)=n delta^2,
proving the trace residual bound. For X=D(Y)>=0 with s=trX>0, the matrix X'=(tau/s)X is PSD with trace tau, and
  ||X-X'||_F=|s-tau| ||X||_F/s<=|s-tau|.
For s=0, X=0 and choosing any trace-tau PSD X' gives distance <=tau=|s-tau|. This proves the distance bound.

7. (Auxiliary tangent count.) If all transition entries U_ij are nonzero, a matrix diagonal in both bases is scalar: otherwise its eigenspace partition in the first basis forces each column of U to be supported in one proper block, giving zeros. Therefore intersection of the two MASAs is RI and the linear measurement rank is 2n-1. Since the uniform positive-definite matrix (tau/n)I belongs T_tau, the exact affine fibre dimension is D_n-(2n-1). Its image under D is the trace-tau density body, whose affine dimension is D_m-1; subtracting gives the claimed auxiliary dimension.

## Audit / limitation

- All overlaps are nonzero by a finite algebraic avoidance argument, not by unproved generic randomness alone.
- Both bases measure exactly the SAME uniform list on every encoded source X; the bases themselves are distinct, but this theorem does not give different observation data on encoded sources. Distinct-data universality for nontrivial A is open.
- The change of basis is generically non-involutory, but this theorem does not prove it is not signed-permutation equivalent to a symmetric matrix for all m. Do not conflate these notions.
- The result covers ONLY trace-only source constraint. Arbitrary measurement spaces L still require source one-body observables to lie in the measured two-MASA span or an alternative genuinely nonlinear encoding. That is not solved here.
- The decoder is CP with Kraus rank r=2m, and its source residual is Lipschitz, regardless of extra ambient directions.
