# Milestone 10 — an entirely rational quadratic two-basis SDP compiler

Date: 2026-11-13. This strengthens 02–04: the orthogonal bases themselves, every coefficient of the encoder/decoder, all targets, and rational objective pullbacks are RATIONAL. There is no algebraic output field, square-root gate, eigenvector computation, or algebraic sign test. The matrix order is unchanged. Milestone 11 uses this result to remove all trace-control hypotheses by allowing exactly one free observation scale.

The construction below is a positive many-to-one quotient, not an assertion that the full lifted fibre equals an encoder image. The rational bases in this milestone are a reflection pair; the additional dense/nonreflection properties of 08 are not asserted for this smaller rational construction.

## 1. The theorem

Let A:S^m -> R^q have rational symmetric coefficient matrices A_1,...,A_q, where m,q>=1. Suppose a rational z is supplied with H=A*z>0. Set

    rho=2 tr(H^{-1}), alpha=m rho^2,
    d=(m+1)^2, M0=7m^2+1+2q,
    M=d+M0, N=d+M=9m^2+4m+3+2q.

There are polynomial-bit explicitly constructible rational matrices U, Phi, and rational linear maps E:S^m->S^N and D:S^N->S^m such that:

- U is orthogonal; the observations are B_U(Y)=(diag Y,diag(U^T Y U)).
- E and D admit completely positive extensions to the full real matrix algebras.
- D E=id and B_U E=Phi A.
- D has a coisometric compression representation D(Y)=VYV^T, VV^T=I_m. V itself may contain the single common factor 1/sqrt(2); every coefficient of the LINEAR MAP D is rational.
- For EVERY datum b, including inconsistent data,

    D({Y>=0:B_U(Y)=Phi b})={X>=0:A(X)=b}.

- For every rational cost C, D*C is rational and has the spectrum of C plus zeros. Objective equality holds on every symmetric Y.
- Every feasible nonzero target has strictly positive observations. Zero source data give the zero lifted fibre.
- The global residual bound in Section 7 holds for every PSD Y, without a rank, Slater, or small-noise hypothesis.

All rational bit-complexity claims include the supplied rational trace certificate in the input length. No exact SDP solver is used in the construction.

## 2. The positive source lift and four-character measurements

Use inner coordinates l_1,...,l_m; r_1,...,r_m; a; q_11,...,q_mm. Put

    V0=[I_m,I_m,0,0]/sqrt(2), D0(Z)=V0 Z V0^T.

For symmetric X, t=tr(HX), B=X-rho t I_m/2, and x=vec(B), define

    J(X) = [[rho t I/2,B],[B,rho t I/2]]
           direct-sum [[t,x^T],[x,alpha t I_(m^2)]].

Then D0 J=id. If X>=0, 0<=X<=rho t I. The first block is orthogonally equivalent to X direct-sum (rho t I-X). Also ||B||_F^2<=alpha t^2/4. For t>0 the arrow Schur complement is at least 3 alpha t I/4; at t=0 the source is zero. Hence J is globally positive. Its coordinate diagonal is theta t, where

    theta=((rho/2)1_(2m),1,alpha 1_(m^2)).

For tau=z.b use the following rational raw vectors and linear target functions c0(b).

(A) Every coordinate vector e_s, with target theta_s tau.

(B) e_(h_i)+s e_(h_j) for h=l,r, i<j, s=+/-1, with target rho tau.

(C) For each ordered i,j and s,u=+/-1,

    v_(ij,s,u)=e_a+s e_(q_ij)+u e_(l_i)-su e_(r_j),

with target (1+alpha+rho)tau.

(D) Put a_i=vec(A_i) in the auxiliary q-block and beta_i=b_i-(rho tau/2)tr(A_i). Use e_a+a_i and e_a-a_i with respective targets

    tau(1+alpha||A_i||_F^2)+2 beta_i,
    tau(1+alpha||A_i||_F^2)-2 beta_i.

The list has exactly M0 columns. Every J(X) has these targets for b=A(X). For any symmetric Z, sign summation gives

    (1/8) sum_(s,u) s v_(ij,s,u)^T Z v_(ij,s,u)
       =Z_(a,q_ij)-Z_(l_i,r_j).

The two vectors in (D) have quadratic difference 4 a_i^T Z e_a. These identities include all otherwise unwanted cross blocks; they do not assume Z=J(X).

Let Vraw be the d-by-M0 matrix of raw vectors, and Mraw its quadratic observation map. There is a rational matrix R0 such that

    A D0 = R0 Mraw,      R0 c0(b)=b                 (1)

on the full symmetric matrix space. Its i-th row has coefficients:

- A_i(j,j)/2 on coordinates l_j and r_j;
- s A_i(j,h)/4 on each block vector in (B) for j<h;
- -s A_i(j,h)/8 on each ordered entry-copy vector in (C);
- +1/4 and -1/4 on its own equation pair in (D).

Indeed these recover, respectively,

    (1/2)<A_i,Z_ll+Z_rr-rho tau I>,
    sum_jh A_i(j,h)(Z_(l_j,r_h)-Z_(a,q_jh)),
    a_i^T Z e_a-beta_i.

Their sum is <A_i,D0(Z)>-b_i. In particular, with S_A=sum_i ||A_i||_F^2,

    ||R0||_(2->2) <= C_R := sqrt(9 S_A/16+q/8).     (2)

## 3. The block structure that permits rationalization

Direct sign cancellation gives

    Q0=Vraw Vraw^T
      =(6m-1)I_(2m) direct-sum [1+4m^2+2q]
       direct-sum [5 I_(m^2)+2 sum_i a_i a_i^T].     (3)

Every nondiagonal term is confined to the auxiliary covariance block.

Set

    L=4m^2+6m+2q+6+2 S_A,
    sigma=1/(2L), Braw=sigma Vraw,
    Q=Braw Braw^T, S=I_d+Q,
    s_l=1+sigma^2(6m-1).

Then 0<Q<=(1/4)I, so I<=S<=(5/4)I. The l- and r-blocks of S are both s_l I. All these matrices and scalars are rational.

Replace the previous square-root Parseval completion by the rational Cayley frame

    G=[ (I-Q)S^{-1}, 2 S^{-1}Braw ].               (4)

Because Q commutes with S,

    GG^T = S^{-1}[(I-Q)^2+4Q]S^{-1}=I_d.           (5)

This identity requires only rational inversion, not a matrix square root.

A general Cayley frame would change the individual source measurements. The block structure (3) is what repairs this issue. Define

    Jhat(X)=S J(X) S/s_l^2.                         (6)

This remains globally positive. Since V0 S=s_l V0,

    D0 Jhat=id.                                    (7)

Its diagonal is theta_hat t for a known rational positive vector theta_hat. Explicitly theta_hat equals rho/2 in the l,r blocks, s_a^2/s_l^2 at the anchor, and alpha diag(S_q^2)/s_l^2 in the q-block, where s_a and S_q are the corresponding blocks of S.

## 4. All new measurements still have source-data-determined values

For a raw column g_j=2 sigma S^{-1}v_j, define

    eta=4 sigma^2/s_l^2.

Then

    g_j^T Jhat(X) g_j=eta v_j^T J(X)v_j,

so its target is eta c0_j(b).

For the j-th completion column g_j=(I-Q)S^{-1}e_j, its target is

    t theta_j ||(I-Q)e_j||^2/s_l^2.                (8)

The reason is that (I-Q)e_j lies entirely in one of the l, r, anchor or q coordinate blocks, and J has a scalar covariance on each such block. There is no assumption about arbitrary reverse lifts having those covariances.

Let c_G(b) be the M-vector consisting of (8) and the raw targets. All its entries are rational linear functions of b. Its sum is

    1^T c_G(b)=c_H tau,
    c_H=m rho+(s_a^2+alpha tr(S_q^2))/s_l^2.        (9)

This identity holds for every b, not only feasible b. The +/- equation pairs cancel their b_i terms in the sum; algebraically the completion and raw contributions add using (I-Q)^2+4Q=S^2. Also tr Jhat(X)=c_H tr(HX).

The inverse identity survives on every symmetric Z. If P_raw selects the last M0 frame entries, then

    A D0(Z)=eta^{-1} R0 P_raw M_G(Z).              (10)

Indeed P_raw M_G(Z)=4 sigma^2 Mraw(S^{-1}ZS^{-1}), and D0(S^{-1}ZS^{-1})=D0(Z)/s_l^2. Equation (1) gives (10).

## 5. Rational two-basis exposure without additional dimension

Choose a=4/5, beta=3/5 and g=a^2-beta^2=7/25. Put

    F=[a I_d,beta G], P=F^T F, Qout=I_N-P,
    U=2P-I_N,
    Delta=diag(-beta^2 I_d,a^2 I_M).

All matrices are rational; FF^T=I_d and U^TU=I_N. Also F Delta F^T=0.

For w=(x,z) in ker F, x=-(beta/a)Gz. Direct calculation gives

    w^T Delta w-g||w||^2=beta^2(||z||^2-||Gz||^2)>=0.

Consequently the measured signed stress is

    S0=Delta+U Delta U^T=2Qout Delta Qout>=2g Qout.  (11)

Define

    y_first(b)=(a^2 theta_hat tau, beta^2 c_G(b)),
    Phi b=(y_first(b),y_first(b)).                  (12)

The coefficient vector w_stress=(diag Delta,diag Delta) obeys w_stress.Phi b=0 for every b by (9).

## 6. Exact quotient and objectives

For an exact PSD competitor Y, the measured stress has zero pairing; (11) forces Y=PYP. With Z=FYF^T>=0, this means Y=F^T ZF. Its data imply

    diag Z=theta_hat tau,   M_G(Z)=c_G(b).

Equation (10) gives A(D0(Z))=b. Conversely, Jhat(X) satisfies all these equations whenever A(X)=b. Thus with

    E(X)=F^T Jhat(X)F,
    D(Y)=D0(FYF^T),       V=V0 F,

we have DE=id, B_U E=Phi A, and exact entire-fibre surjectivity for every datum. In particular the exact fibre is the full set

    {F^T ZF:Z>=0, diag Z=theta_hat tau, M_G(Z)=c_G(b)}.

It is not silently identified with E(F_b). Nor is it necessary to assert that G alone spans every coordinate projector: the first d columns of F retain those observations explicitly.

Let R=[I_m,I_m,0,0]F. This is rational, RR^T=2I_m, and

    D(Y)=(1/2)R Y R^T,     D*C=(1/2)R^T C R.       (13)

Thus all coefficients of D and rational objective pullbacks are rational. The coisometry V=R/sqrt(2) proves ||D||_(F->F)=1 and that D*C has the spectrum of C with extra zeros.

## 7. Global residual and dual extraction

Let delta=||B_U(Y)-Phi b|| for an arbitrary PSD Y. Set

    kappa=||w_stress||/(2g)
         =sqrt(2[d beta^4+M a^4])/(2g).

The stress gives tr(Qout Y Qout)<=kappa delta. Reflection averaging cancels the P-Qout cross blocks, so

    ||diag(F^T(FYF^T)F)-y_first(b)||
       <=(1/sqrt(2)+kappa)delta.

Select the raw frame coordinates and use (10). This proves

    ||A(D(Y))-b|| <= K_raw delta,
    K_raw=[C_R/(beta^2 eta)](1/sqrt(2)+kappa).       (14)

This is global in Y,b,delta. Since eta^{-1}=s_l^2 L^2<=(25/16)L^2, it is explicitly polynomial in dimensions and source measurement magnitudes, independently of target rank or facial gaps.

For any lambda in R^q, form ell in R^N, zero except at the raw frame coordinates, where it is

    (beta^2 eta)^{-1} R0^T lambda.

Then

    P diag(ell)P=D*(A*lambda),
    ell.y_first(b)=lambda.b,
    B_U*((ell/2,ell/2))=D*(A*lambda)+Qout diag(ell)Qout.

These identities give explicit signed PSD certificates and the dual transformations used in 11. No closed-cone-image or Slater premise is needed.

## 8. Complete positivity with rational coefficient maps

The choice rho=2tr(H^{-1}) supplies a CP extension of J. Here are the finite-dimensional Gram identities, included to specify the extension.

The complementary map X -> rho tr(HX)I-X has positive Gram matrix rho I tensor H-Omega Omega^T, where Omega=sum_i e_i tensor e_i: the squared norm of Omega after inverse-square-root normalization is tr(H^{-1})/rho=1/2.

For the arrow, put G_H=H^{-1}, s=tr G_H,

    S_ij=(E_ij+E_ji)/2,
    T_ij=S_ij-(rho/2)delta_ij H,
    B_ij=H^{-1/2}T_ij H^{-1/2}.

The elementary identity sum_ij S_ij G_H S_ij=(G_H+sI)/2 gives

    sum_ij B_ij^2=(G_H^2+sG_H)/2-rho G_H+(m rho^2/4)I
                 <=(alpha/4)I.

Thus the block Gram matrix with top block H, bottom diagonal blocks alpha H, and offdiagonal blocks T_ij in the first row/column is positive definite. Its Gram factorization yields a real Kraus representation of the arrow map, extended using the functionals tr(T_ij X) on all input matrices.

The base block of J is a fixed orthogonal congruence of the identity map direct-sum the complementary map. Together these show J is CP. Rational congruence by S/s_l and isometric embedding by F preserve CP, so E is CP. D is a one-Kraus compression.

The CP property does not require rational Kraus matrices. What is returned rationally is the linear map itself; its Choi matrix is rational. No claim that every rational PSD matrix has a rational Cholesky factor is made.

## 9. Positivity and bit complexity

For feasible nonzero b, tau>0. The old raw targets are positive: the equation pair is bounded below by

    tau[1+alpha||A_i||^2-sqrt(alpha)||A_i||]>=3tau/4.

The completion targets are positive because I-Q>=3I/4, theta>0. The coordinate targets theta_hat tau are positive. At b=0 the full source and lifted fibres are zero, by trace control and the complete diagonal list.

All construction operations are rational additions, products and one inverse of S=I+sigma^2Q0. Its eigenvalues lie in [1,5/4]. Rational Gaussian elimination and determinant/minor bounds give polynomial bit length and polynomial bit time in the input/certificate length. The entries of F,U,Phi, the matrix coefficients of E,D, and rational-cost pullbacks are all rational. There is no hidden large algebraic field. U is exactly orthogonal over Q, not approximately orthogonal after rounding.

This exact rationalization is the new step. The source-entry copying identity is inherited from 02, while the rational Cayley frame and the compensating block congruence make every output coefficient rational at the same order N. It avoids, rather than contradicts, historical rational obstructions restricted to canonical single-copy encodings.
