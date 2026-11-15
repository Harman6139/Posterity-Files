# Milestone 04 — individually quadratic algebraic output, without a large-field representation assumption

Date: 2026-11-12. Supplements the universal quotient theorem 02 (9030a69bab7f5358065f836a826e9f5a9bbe2c86) and the quantitative supplement 03 (b91ba45c2dd85bd5712e032456623488474065f3).

## 1. The representation refinement

Assume the source matrices A_i, the trace certificate z, the datum b, and the source cost C are rational. Use rational rho=tr((A*z)^(-1)) and the rational LDL^T completion specified in 02–03.

**Theorem.** Every individual entry of the orthogonal basis matrix U, compression matrix V, lifted cost V^T C V, and every individual coefficient of the encoder E and decoder D is rational or of the form r sqrt(s), with r rational and s positive rational. Their numerator and denominator bit lengths, the number of entries, and the total representation length are polynomial in m,p and the ordinary rational input bit length, including the trace certificate. Every target/data-map entry is rational. In particular every individual output coefficient has algebraic degree at most TWO.

This is stronger than merely giving a polynomial-size general radical expression graph. A single joint number field containing all entries may have large degree, but neither its construction nor its expansion is required.

## 2. Proof by column factors

All raw observation vectors v_j in 02 are rational. In the rational LDL^T factorization of the completion matrix, every completion column has the form sqrt(d_j) u_j with d_j positive rational and u_j rational. The scalar base/anchor completion columns have the same form.

Consequently EVERY column f_j of the final coisometry

  F=[sqrt(2/3) I_d, G/sqrt(3)]

can be written

  f_j=sqrt(s_j) u_j,

where s_j is positive rational and u_j is a rational d-vector. For the first d columns take s_j=2/3 and u_j a coordinate vector; for raw columns take s_j=epsilon/3; for completion columns use the rational LDL pivot divided by three.

For i different from j,

  U_ij=2 f_i^T f_j=2(u_i^T u_j) sqrt(s_i s_j).

The diagonal entry is U_ii=2s_i||u_i||^2-1, rational. This proves the assertion for U.

Recall V=V_0 F with V_0=[I_m,I_m,0,0]/sqrt(2). Thus

  V_ij=sqrt(s_j/2) [(u_j)_(l_i)+(u_j)_(r_i)],

again a rational coefficient times one square root. The product V_ai V_bj is a rational coefficient times sqrt(s_i s_j); summation over a,b preserves this single square-root factor. This proves the claim for the decoder coefficients and for every lifted cost entry when C is rational.

The inner encoder J has entirely rational coefficients: it uses rho, alpha, H and rational linear coordinate operations, with no square roots. Therefore every coefficient of

  E(X)_ij=f_i^T J(X) f_j
         =sqrt(s_i s_j) u_i^T J(X)u_j

has the same claimed form. For rational X, every individual encoded matrix entry also has degree at most two.

The raw targets are rational; each completion target is a rational scalar times ||h_j||^2=d_j||u_j||^2; final weighting uses the rational factors 2/3 and 1/3. Hence Phi and y_b=Phi b are rational.

Polynomial bit length follows from the rational inversion and rational LDL minor bounds in 03. Multiplication, addition, and reduction of polynomially many rational numbers of the established polynomial bit lengths preserve polynomial bit length. A representation r sqrt(s) need not factor s into a squarefree integer: recording the positive rational radicand already specifies an exact real algebraic number, with the positive-root convention. Zero coefficients are recorded as zero. QED.

## 3. Exact certification without solving an algebraic sign problem

The construction requires only rational sign tests and exact rational matrix operations, followed by recording positive square roots. Its certificates consist of:

1. A rational positive-definite factorization of H=A*z and the rational bound rho H>=I (or the analytic justification rho=tr H^(-1)).
2. The rational raw-frame identity for Q_0 and the rational source-adjoint identity R_0 M_raw=A D_0. The square-root factor in D_0 cancels in D_0*, so its matrix coefficients are rational.
3. A rational LDL^T factorization of R_c=I-epsilon Q_0 with positive rational pivots, certifying the Parseval completion. The uniform bound I/2<=R_c<=I is established by the explicit norm estimate, not by uncertain floating-point eigenvalues.
4. The formulas P=F^TF, U=2P-I, Delta=diag(-I_d,2I_M) and S=Delta+U Delta U=2Q Delta Q>=2Q. Their correctness follows from FF^T=I and F Delta F^T=0, already certified by the rational frame identities and the factored positive roots.
5. The explicit two-sided dual multipliers in 02, which establish global residual soundness on the entire PSD cone.

An implementation may keep the common column factors sqrt(s_j) rather than expand unrelated radicals. All load-bearing equalities reduce to the stated rational identities by cancelling the known factors. No exponential-degree joint-field computation or general real-algebraic feasibility oracle is used.

## 4. Limits of the computational claim

Given a rational trace certificate, this proves an ordinary polynomial-bit exact construction of the matrices in a standard per-entry quadratic-algebraic encoding. Numerical evaluation to s additional binary digits is polynomial in the exact representation length and s, with the perturbation and data/decoder bounds in 03.

Without a supplied certificate, 03 gives an explicit rational algorithm polynomial in the source input length and the declared numerical inverse cone margin kappa. This refinement does not replace that conditioning dependence by an unproved unconditional polynomial-time exact SDP algorithm.

The exact U is orthogonal. Independently rounding its entries need not preserve orthogonality; the exact algebraic representation defines the bases, while the perturbation bounds in 03 quantify the effect of numerical evaluation.

No claim of literature priority or independent referee certification accompanies this representation theorem.
