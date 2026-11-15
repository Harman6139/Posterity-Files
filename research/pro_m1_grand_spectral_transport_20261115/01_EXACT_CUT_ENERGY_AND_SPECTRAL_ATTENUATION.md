# Checkpoint 01 — exact cut energy and spectral attenuation

2026-11-15. The identities and conditional product criterion below are proved. They do NOT resolve the nonlinear balanced candidate or the all-order last-step theorem. No historical originality claim is made.

## 1. Compatible matrix cut

Work with real symmetric or complex Hermitian matrices, with the real Frobenius inner product. Split the coordinate space into H1 direct sum H2 and let J=diag(I,-I). Suppose U=a+L, a perpendicular to L, satisfies J U J=U. Then a is block diagonal and L splits orthogonally into block-diagonal and off-diagonal parts. If W=Z12, the off-diagonal block of P_U Z is Pi W, with Pi an orthogonal projector on the rectangular matrix space (real-linear is sufficient).

For a plain DRS step write u=P_U Z, d=T Z-Z, v=P_PSD(2u-Z), s=P_PSD(Z-2u). Exactly,

    v=u+d, s=Z-u+d, v,s PSD, vs=sv=0.

Putting Delta W=d12 gives v12=Pi W+Delta W and s12=(I-Pi)W+Delta W.

### Theorem 1: exact transverse energy

    ||W_next||_F^2+||Delta W||_F^2+2 tr(v22 s22)=||W||_F^2.       (1)

The overlap tr(v22 s22) is real, nonnegative, and equals tr(v11 s11).

Proof. The (2,2) block of vs=0 gives v12* s12+v22 s22=0. Orthogonality of Pi W and (I-Pi)W therefore gives

    Re <W,Delta W>+||Delta W||^2=-tr(v22 s22).

Expand ||W+Delta W||^2. Nonnegativity follows because the diagonal blocks are PSD. The (1,1) block of vs gives the second equality. No spectral simplicity, differentiability, definability or asymptotic assumption is needed. QED.

Consequently ||W_k|| is nonincreasing and

    sum_(k>=n) [||Delta W_k||^2+2 tr(v22,k s22,k)]
        =||W_n||^2-lim_k ||W_k||^2.                            (2)

The zero-cut subspace is invariant. This identifies the exact nonnegative defect in firm nonexpansiveness for the orbit and its sign-reflected twin, rather than dropping that defect.

## 2. Exact bordered spectral formula

Let R=[A b; b* c] be real symmetric or complex Hermitian. Let lambda_i be eigenvalues of A, let (mu_j,q_j) be an orthonormal eigendecomposition of R, and put omega_j=|(q_j)_last|^2. Thus omega_j>=0 and sum omega_j=1.

For f(t)=|t| use the divided difference f[1](x,y)=(|x|-|y|)/(x-y). At equal nonzero arguments use sign(y); at (0,0) any value in [-1,1] is allowed. Define

    g(lambda)=sum_j omega_j f[1](mu_j,lambda), C=g(A).

Then C is Hermitian, -I<=C<=I, and exactly

    (|R|)12=C b.                                              (3)

Proof. In an A-eigenbasis, (mu_j-lambda_i)(q_j)_i=b_i(q_j)_last. If b_i!=0 and mu_j=lambda_i, the last coordinate is zero. Subtract |lambda_i| times the orthogonality identity sum_j (q_j)_i conjugate((q_j)_last)=0 in the spectral formula for |R|. This gives (3) componentwise. If b_i=0 the corresponding eigenvector is uncoupled, and the relevant off-diagonal entry is zero. Repeated eigenspaces cause no ambiguity. Every divided difference belongs to [-1,1]. QED.

With v=R_+ and s=(-R)_+, one also has

    <b,(I-C^2)b>=4 v_last,last s_last,last.                    (4)

Indeed the bottom diagonal of |R|^2=R^2 gives ||Cb||^2+(v_last,last+s_last,last)^2=||b||^2+c^2, and c=v_last,last-s_last,last.

For a compatible rank-one cut of DRS, H=2Pi-I is an orthogonal reflection, the reflected coupling is b=HW, and

    W_next=(I+C H)W/2.                                        (5)

This is an EXACT current-orbit spectral transport formula, not a moving linearization. Formula (4) measures the attenuation absent when C is replaced by the sign of a reference principal block.

For D=(I+C)/2, the spectral coefficients satisfy

    1-D_i=sum_(mu_j<0) omega_j |mu_j|/(lambda_i+|mu_j|), lambda_i>0,
    D_i=sum_(mu_j>0) omega_j mu_j/(|lambda_i|+mu_j), lambda_i<0.

Hence 1-D_i<=s_last,last/lambda_i for positive lambda_i, and D_i<=v_last,last/|lambda_i| for negative lambda_i. These estimates must not be used at a zero lambda_i.

## 3. Accumulated-loss criterion: precise conditional scope

Suppose r_k=||W_k||>0 on a tail. Set

    rho_k=(||Delta W_k||^2+2 tr(v22,k s22,k))/r_k^2,
    L_k=sum_(j=N)^(k-1) -log(1-rho_j).

Then 0<=rho_k<1 and exactly r_k^2=r_N^2 exp(-L_k). If a rho_j equals one, the cut becomes zero and remains zero instead.

If an actual orbit additionally satisfies ||Delta W_k||/||W_k||~omega/sqrt(k), omega>0, then for any p in (0,1),

    k^(1-p)||Delta W_k||
       =omega r_N exp(-[L_k-(1-2p)log k]/2)(1+o(1)).            (6)

Thus the accumulated loss relative to (1-2p)log k determines vanishing, finite positive survival, or divergence of the scaled transverse speed. This classifies norms under the stated frequency hypothesis, not general vector limits.

If also sum rho_k^2<infinity and sum |(||Delta W_k||/r_k)^2-omega^2/k|<infinity, Taylor expansion of -log(1-x) gives

    L_k=omega^2 log k
        +2 sum_(j=N)^(k-1) tr(v22,j s22,j)/r_j^2+C+o(1).       (7)

This separates angular contraction from cumulative nonlinear complementarity loss. The extra hypotheses have NOT been verified for the balanced candidate.

## 4. Exact application and open boundary

The balanced order-seven affine space is invariant under diag(1,1,1,1,1,1,-1). Its cut W is column 6, rows 0,...,5, and Pi retains only row 0. Therefore (1) applies for every starting point, with overlap v66 s66. This application is unconditional.

The available linear calculation suggests omega^2=sqrt(3)/4 and p=1/4. These constants are not yet proved for the nonlinear orbit. If established with (7)'s hypotheses, persistent scaled transverse speed would require the critical overlap budget

    sum_(j<k) v66,j s66,j/||W_j||^2
        =(1/4-sqrt(3)/8)log k+O(1).

This is a conditional diagnostic, not an established asymptotic. The exact identity explains why discarding quadratic diagonal feedback is invalid; it does not determine its cumulative size.

## 5. Corroborating checks

A separate NumPy script checks (1), (3), (4), and complementarity at 500 seeded random symmetric inputs, repeated/zero-eigenvalue cases, and the saved six-million-step state. The largest normalized discrepancy in this run was 3.31e-15. These are double-precision checks of algebraic identities, not interval certificates or asymptotic proofs. The proof is the algebra above.
