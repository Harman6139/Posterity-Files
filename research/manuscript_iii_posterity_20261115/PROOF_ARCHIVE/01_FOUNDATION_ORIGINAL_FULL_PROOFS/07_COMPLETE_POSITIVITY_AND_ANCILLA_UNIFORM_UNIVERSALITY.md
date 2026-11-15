# Milestone 07 — complete positivity and ancillary-level-uniform universality

Date: 2026-11-12. Uses the strict-trace, shielded quadratic normal form in 06. This strengthens global scalar PSD positivity to complete positivity and proves that exact lifting and the residual constant survive every matrix amplification without an ancillary-dimension loss.

The term complete positivity is used in its standard matrix-algebra sense: a map has real Kraus matrices B_a with Phi(X)=sum_a B_a X B_a^T, and therefore Phi tensor id_n is positive for every n. The proof below supplies the positive block matrices whose Gram factorizations give these Kraus matrices. It does not infer complete positivity merely from positivity on real symmetric inputs.

## 1. The theorem

Let the rational trace certificate be H=A*z>0, put rho=2 tr(H^{-1}), alpha=m rho^2, and use the shielded construction of 06 of order

  N=9m^2+4m+6+2p.

There is a specified real completely positive extension of its encoder E from S^m to ALL real m-by-m matrices, and the decoder D(Y)=VYV^T is completely positive, such that

  D E=id on M_m(R),       B_U E=Phi A on M_m(R).           (1)

The encoder admits a real Kraus representation using at most

  m^3+m^2+2m+1                                           (2)

Kraus matrices. For rational input and a rational trace certificate these matrices can be given by polynomial-bit rational LDL factorizations and square roots of positive rationals. No high-degree joint algebraic number field is required.

For EVERY integer n>=1, keep an arbitrary n-dimensional ancillary factor. Define

  E_n=E tensor id_n, D_n=D tensor id_n,
  A_i^{(n)}(X)=sum_{a,b=1}^m (A_i)_{ab} X_{ab},

where X is an m-by-m block matrix with n-by-n blocks. Define B_U^{(n)} by the two lists of diagonal n-by-n blocks in the first-factor bases I and U. Then, for arbitrary symmetric matrix-valued data b_1,...,b_p in S^n,

  D_n({Y>=0:B_U^{(n)}(Y)=(Phi tensor id_n)b})
    ={X>=0:A^{(n)}(X)=b}.                               (3)

Equip a matrix-valued list with norm (sum_i ||b_i||_F^2)^{1/2}. The SAME scalar constant K_r from 06 gives

  ||A^{(n)}(D_n(Y))-b|| <= K_r
       ||B_U^{(n)}(Y)-(Phi tensor id_n)b||                (4)

for all n and all PSD Y, with no factor depending on n. The forward residual constant likewise stays ||Phi||. Every amplified linear cost pulls back exactly through D_n*, with unchanged Frobenius norm.

This is a stronger matrix-valued measurement theorem. At n=1 the output consists of two actual complete rank-one orthonormal-basis diagonal lists. At n>1 each observed block has size n: these are two basis measurements on the FIRST factor with the ancillary system retained. They are NOT being mislabeled as just two scalar rank-one bases on the entire Nn-dimensional space.

## 2. A completely positive strict complement

Write G=H^{-1}, s=tr G, and Omega=sum_i e_i tensor e_i. The map

  K_1(X)=rho tr(HX) I_m-X

has the real Choi/Gram block matrix

  W_1=rho I_m tensor H-Omega Omega^T.

Indeed its block (a,b) is rho delta_ab H-E_ab, giving the output coefficients of the displayed map. Since

  Omega^T(rho I tensor H)^{-1}Omega=s/rho=1/2,

one has W_1>=0, in fact W_1>0. More explicitly, conjugating by (rho I tensor H)^{-1/2} gives I-vv^T with ||v||^2=1/2. A Gram factorization W_1=sum_l w_l w_l^T, with w_l=vec(B_l), gives K_1(X)=sum_l B_l X B_l^T. Thus K_1 is completely positive and needs at most m^2 Kraus matrices.

This is stronger than the elementary scalar inequality rho tr(HX)I-X>=0. The chosen trace bound is essential to the Choi argument; an arbitrary merely sufficient scalar bound rho>=||H^{-1}|| need not meet this complete-positivity threshold.

## 3. The entry-copy arrow is also completely positive

For ordered indices i,j put

  S_ij=(E_ij+E_ji)/2,
  T_ij=S_ij-(rho/2)delta_ij H.

For symmetric X, tr(T_ij X)=X_ij-(rho/2)tr(HX)delta_ij, exactly the entries copied into the anchor in 02 and 06. Define an extension of the arrow map on all matrices by

  K_2(X) = [ tr(HX), (tr(T_ij X))_(ij)^T ;
             (tr(T_ij X))_(ij), alpha tr(HX) I_(m^2) ].  (5)

Its Choi/Gram matrix is the real symmetric block matrix

  W_2 = [ H, T_11, T_12, ... ;
          T_11, alpha H, 0, ... ;
          T_12, 0, alpha H, ... ; ... ].                 (6)

We prove it is positive definite, rather than presume the scalar Schur-complement argument survives amplification.

Let B_ij=H^{-1/2} T_ij H^{-1/2}. Direct calculation gives

  sum_(i,j) S_ij G S_ij=(G+(tr G)I)/2.

Consequently

  sum_(i,j) B_ij^2
    =(G^2+sG)/2-rho G+(m rho^2/4)I
    <=(m rho^2/4)I=(alpha/4)I.                          (7)

For the inequality, G<=s I and rho>=s imply

  G^2/2+(s/2-rho)G <= G^2/2-sG/2 <=0.

Conjugate (6) by the block diagonal matrix with H^{-1/2} in every position. Its normalized offdiagonal column has blocks B_ij and operator norm at most sqrt(alpha)/2 by (7). Hence its lower Schur complement is at least (3alpha/4)I. Thus W_2>0.

A real Gram factorization of W_2 now gives Kraus matrices for (5). Its order is m(m^2+1), so that many Kraus matrices suffice. The use of the symmetric S_ij specifies the extension on nonsymmetric and complex inputs; no unspecified extension ambiguity remains.

## 4. The full encoder is completely positive

In the canonical source/auxiliary coordinates from 06,

  J_s(X)=X direct-sum K_1(X) direct-sum K_2(X)
               direct-sum [tr(HX)].                     (8)

The first map is the identity and has one Kraus operator. Sections 2–3 prove complete positivity of the next two. The last scalar functional is completely positive with at most m real Kraus rows, by a Gram factorization of H.

Direct sums and orthogonal output congruences preserve a Kraus representation. Reversing the real Hadamard change on the l/r coordinates and applying the final isometry Z->F^T ZF therefore give a completely positive E that agrees with the real-symmetric encoder of 06. The count is

  1+m^2+m(m^2+1)+m=m^3+m^2+2m+1.

The original decoder is already one-Kraus. In (8) it simply extracts the source block, so DE=id holds on ALL matrices, not just symmetric ones.

Every coefficient matrix in the Choi proofs is rational for rational input. W_1,W_2,H are positive definite, so rational LDL factorization uses positive rational pivots. Reshaping the columns sqrt(pivot) times a rational vector produces Kraus matrices with individually quadratic algebraic coefficients and polynomial bit lengths. Matrix orders are polynomial in m, so explicitly returning this Kraus representation still has polynomial, although larger, output length. The original sparse formula for E is much more economical and does not require listing all Kraus matrices.

The data identity in (1) also holds on the entire matrix algebra. It was proved on the symmetric part in 02. Every real Kraus map preserves transposition; therefore it maps skew input matrices to skew matrices. Quadratic measurements in real vectors and source traces against symmetric A_i both annihilate the skew part. The identity follows on all matrices by decomposition into symmetric and skew parts. Complex linear extension gives the same algebraic identity.

## 5. Exact amplified fibres

Complete positivity makes E_n and D_n positive for every n. Tensoring the two linear identities in (1) gives

  D_n E_n=id,
  B_U^{(n)} E_n=(Phi tensor id_n) A^{(n)}.                (9)

Thus every source PSD solution has a PSD lifted solution at every level. For the converse it remains to prove (4); at zero residual it gives the exact source equations, while D_n is PSD-positive.

This proof covers arbitrary ranks and arbitrary, possibly inconsistent, matrix-valued data. It does not assume that the matrix-valued trace datum sum_i z_i b_i is invertible. No rank-dependent normalization of that datum is used.

## 6. The residual constant is independent of the ancillary order

Let Q=I-F^TF and let w be the two-list stress coefficient vector of 06, so

  B_U*w=S_0>=2Q,       w^T(Phi tensor id_n)b=0.

For a PSD block matrix Y define the PSD ancillary matrix

  T_Q(Y)=sum_j [ (Q tensor I_n)Y(Q tensor I_n) ]_{jj}.

This is the partial trace over the first factor of its Q-supported PSD block. Likewise contraction by S_0 gives a PSD ancillary matrix T_S(Y). Positivity of contraction with S_0-2Q gives

  0<=2 T_Q(Y)<=T_S(Y).

The target pairs to zero with w, so for the full matrix-list residual r,

  T_S(Y)=sum_j w_j r_j.

The Frobenius norm is monotone on PSD matrices: if 0<=A<=B, then tr(B^2-A^2)=tr((B-A)(B+A))>=0. Therefore

  ||T_Q(Y)||_F <= (||w||_2/2)||r||
               =kappa ||r||.                           (10)

Let Z_j be the individual diagonal ancillary blocks of (Q tensor I)Y(Q tensor I). They are PSD. Hence

  sum_j ||Z_j||_F^2 <= ||sum_j Z_j||_F^2
                     =||T_Q(Y)||_F^2,                  (11)

because every cross trace tr(Z_i Z_j) is nonnegative. This avoids the spurious factor sqrt(n) that would arise from bounding everything through the scalar total trace.

Reflection averaging works as an EXACT block identity:

  [Y+(U tensor I)Y(U^T tensor I)]/2
   =(P tensor I)Y(P tensor I)+(Q tensor I)Y(Q tensor I).

Equations (10)–(11) therefore give the same frame-residual estimate as at level one. The subsequent source extraction uses R_0 tensor id on a Hilbert direct sum of matrix spaces; its norm is exactly ||R_0||, independent of n. The entire calculation of 02/06 goes through unchanged and proves (4) with the SAME K_r.

The forward constant is ||Phi tensor id||=||Phi|| for these Hilbert norms. Thus the two-sided weak-feasibility gap inequalities also hold at every n with the same constants.

## 7. Objectives and computational scope

For an arbitrary symmetric (or complex Hermitian after complex extension) source cost C of order mn, set

  C_tilde=(V^T tensor I_n) C (V tensor I_n).

Then <C_tilde,Y>=<C,D_n(Y)> for every symmetric Y. Since VV^T=I_m, C_tilde has the eigenvalues of C together with zeros; in particular its Frobenius and operator norms and rank are unchanged. Exact fibre surjectivity gives identical feasible objective-value sets.

The construction of U,E,D,Phi does not depend on n. Their amplified descriptions are tensor expressions with I_n. Expanding all input/output matrices has its usual polynomial cost in their dimensions, but there is no hidden change in construction coefficients, no additional inverse trace effect, and no ancillary factor in the residual constants.

The scalar facial-depth and whole-ambient modulus theorem of 06 is not automatically asserted at every matrix-valued level: a singular matrix-valued trace datum may have its own ancillary support. What is proved at every level is complete positivity, exact entire-fibre surjectivity, objective identity, and the explicit residual/weak-feasibility bounds (3)–(4).

## 8. Applicability to a subsequent anchored nonreflection compiler

A compiler of the form

  E_new(X)=F_new^T (J_s(X) direct-sum [1])F_new

has a completely positive LINEAR part and a fixed PSD anchor offset. At matrix level its natural definition is

  (E_linear tensor id_n)(X)+E_offset tensor I_n.

Both terms are PSD. Its affine data map is amplified with the same constant offset times I_n. Any signed exposing certificate and retained-coordinate averaging argument that prove scalar source residual soundness also satisfy (10)–(11), so the same ancilla-uniform result follows. Equal-weight rotations of two columns do not change this conclusion when the source extraction uses only retained, unrotated coordinates.

## 9. Attribution and audit

The characterization of complete positivity by a positive Choi matrix/real Kraus representation is classical: M.-D. Choi, Completely positive linear maps on complex matrices, Linear Algebra and its Applications 10(3) (1975), 285–290, DOI 10.1016/0024-3795(75)90075-0. The elementary Gram-factorization implication was included above to make the construction self-contained.

The new load-bearing calculation is the exact sum-of-squares identity (7) for the entry-copy arrow and its combination with the source-block identity section. The amplified norm proof uses matrix-valued PSD order, not a scalar trace estimate with an unacknowledged dimension loss. All matrix-valued observations are explicitly identified as such. No trace-preserving quantum-channel claim is made: the encoder and decoder are completely positive but are not generally trace preserving on their entire ambient cones. No external novelty priority or independent referee certification is claimed.
