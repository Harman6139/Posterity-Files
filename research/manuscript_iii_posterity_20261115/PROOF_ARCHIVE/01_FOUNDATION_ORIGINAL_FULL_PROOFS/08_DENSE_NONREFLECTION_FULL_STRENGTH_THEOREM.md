# Milestone 08 — the full-strength quadratic normal form

Date: 2026-11-12. This combines the original quotient theorem with 06–07 in ONE explicit construction. It removes all zero overlaps, makes the basis change genuinely nonreflection even after independent signed permutations, makes every feasible observation positive INCLUDING at zero source, and retains complete positivity, dual attainment, exact facial depth, and the sharp whole-ambient leakage law.

## 1. Unified theorem

Let m,p>=1, let A_i be rational real symmetric m-by-m matrices, and let z be a rational trace-control certificate with H=A*z>0. Set rho=2 tr(H^{-1}) and alpha=m rho^2. The construction does not depend on the source datum b or cost C.

There exist a real orthogonal U, a coisometry V with VV^T=I_m, a completely positive linear map E_lin, a fixed rank-one PSD matrix Y_0, and a rational affine target map

  y_b=Phi b+y_0,
  E(X)=E_lin(X)+Y_0,
  D(Y)=VYV^T,

of order

  N=11m^2+8m+14+2p,                                    (1)

such that:

1. D is globally completely positive and a Frobenius contraction; E is PSD-positive on the source cone, D E=id, and B_U E=Phi A+y_0. The linear part E_lin is completely positive, not merely positive.
2. For EVERY b, including inconsistent data,

     D({Y>=0:B_U(Y)=y_b})={X>=0:A(X)=b}.                 (2)

   There are precisely two complete real orthonormal-basis observation lists. No external equations are added to the returned problem.
3. Every entry of U is nonzero. In fact an explicit rational eta_*>0 below satisfies |U_ij|>=eta_* for all i,j. U is not equivalent to ANY symmetric matrix, and hence not to a reflection, under independent signed permutations of rows and columns.
4. Every observation of every feasible source datum, including b=0, is at least eta_*^2. The zero source fibre is represented by the singleton {Y_0}, with rank(Y_0)=1 and a sharp Lipschitz ambient recovery modulus.
5. For EVERY PSD ambient Y,

     ||A(D(Y))-b||_2<=K_+ ||B_U(Y)-y_b||_2,              (3)

   where K_+ is the explicit polynomial constant in Section 7. It contains no source-rank, source-Slater, facial-depth, or source feasible-eigenvalue gap.
6. Every source cost C pulls back to V^T C V on ALL ambient matrices. This pullback has exactly the eigenvalues of C with additional zeros; operator norm, Frobenius norm, and rank are unchanged. Both primal and dual optimal values are preserved; finite dual attainment is equivalent.
7. For nonzero feasible b, with source maximum feasible rank r and source singularity degree k, the maximum lifted rank is

     r+m^2+m+3,

   the minimum lifted support is explicitly identified in Section 8, and

     k_lift=max(1,k).                                  (4)

   The same pointwise rank maximum holds for the preimage of each nonzero feasible source X, with r replaced by rank X. At b=0 the lifted rank and depth are one.
8. With the ORIGINAL-SOURCE minimum support E_b and leakage modulus

     mu_b(t)=max{tr(P_{E_b^perp}X):X>=0,||A(X)-b||<=t},

   the full lifted distance modulus satisfies

     Omega_b(t) asymp sqrt(t+mu_b(t))  for b!=0,
     Omega_0(t) asymp t.                                (5)

   These are sharp estimates against the entire ambient PSD cone and distance to the entire lifted feasible fibre. They are not claims that source and ambient moduli always coincide. Decoded recovery separately satisfies dist(D(Y),F_b)<=omega_b(K_+ delta).
9. Given the rational trace certificate, construction is polynomial-bit in the ordinary input/certificate length. Every individual entry of U,V,E_lin,Y_0 and of a rational-cost pullback is rational or a rational multiple of one square root of a positive rational. The target map is rational. The explicit reciprocal overlap and observation margins and K_+ are polynomial in m,p,1+sum_i||A_i||_F^2. Forward target/encoder norms additionally contain the declared trace-certificate conditioning.
10. All exact-fibre, complete-positivity, objective and residual assertions amplify to an arbitrary untouched ancillary factor as in 07, with the SAME residual constant. At level n these are explicitly matrix-valued basis observations, not two scalar rank-one bases on the whole Nn-space. The affine anchor becomes Y_0 tensor I_n.

No source solution, source minimum face, source rank or source facial chain is needed to CONSTRUCT the normal form. The constants in the sharp whole-ambient modulus, unlike the global decoded residual constant, use the explicit source/face conditioning parameters described in 06.

## 2. Inner data and rational column factors

Use the strict-trace shielded frame G of 06 on

  d=m^2+2m+2,
  M=8m^2+2m+4+2p

coordinates/columns. Its raw list has M_0=7m^2+2+2p columns. Write epsilon=1/(2L), where

  S_A=sum_i||A_i||_F^2,
  L=4m^2+6m+2p+6+2S_A.

The completion matrix lies between I/2 and I. In its unpivoted rational LDL factorization every pivot lies in [1/2,1]: this follows from the same spectral bounds on each Schur complement. Therefore every column admits

  g_j=sqrt(s_j)u_j,  s_j rational positive, u_j rational,
  epsilon<=s_j<=1.

The shield completion is the pure column sqrt(1-epsilon)e_s. Split it into two identical columns. Denote the resulting column number by Mbar=M+1 and retain the notation G for this Parseval frame. Their common factor is

  s=(1-epsilon)/2 in [1/4,1/2].

Their target values are each half the old completion target. All raw columns remain unchanged, so the exact source operator identity and its coefficient bound remain valid:

  A D_0=epsilon^{-1} R_0 P_raw M_G,
  ||R_0||<=C_R:=sqrt(9S_A/16+p/8).                       (6)

The upper-left/source diagonal targets are theta_i tau, tau=z.b, with the shield entry theta_s=1. Write c_j(b) for the split frame targets. They are rational and

  sum_j c_j(b)=tau sum_i theta_i

for EVERY b, including inconsistent data.

## 3. A signed, anchored coisometry with rational factored columns

Fix rational h=1/10, v_0=1/100 and positive roots

  a^2=(5+3h^2)/7,   beta^2=(1-5h^2)/7.

In R^d put three columns a e_i,beta e_i,beta e_i at weights -1,2,3 for every i, and put h g_j at weight 4 for every split frame column. Let A_0 denote this d-by-n_0 matrix, where n_0=3d+Mbar, and Delta_0 its diagonal weight matrix. Then

  A_0 A_0^T=I_d,        A_0 Delta_0 A_0^T=0.

Define rational

  r_i=h sum_j s_j(u_j)_i,
  t_0=2(Mbar+1),

and column anchor coordinates

  zeta_(i,1)=(2r_i+t_0)/(3a),
  zeta_(i,2)=-(5r_i+4t_0)/(3beta),
  zeta_(i,3)=t_0/beta,
  zeta_j=sqrt(s_j) for the G columns.

Direct substitution gives

  A_0 zeta=0,       A_0 Delta_0 zeta=0.                  (7)

All zeta entries are nonzero. Indeed |r_i|<=h sqrt(Mbar)<=t_0/20. In particular

  min_j |zeta_j|>=sqrt(epsilon),
  Zeta:=sum_j zeta_j^2<=200d(Mbar+1)^2+Mbar.

Both Zeta and qZeta=zeta^T Delta_0 zeta are rational, and |qZeta|<=4 Zeta.

Select a positive rational eta by the finite quantitative grid in Section 4. Put v^2=s v_0^2 and

  x^2=[2+eta^2(qZeta-2Zeta)+2v^2]/3,
  y^2=[1-eta^2(Zeta+qZeta)-5v^2]/3.

Attach eta zeta_j as the last coordinate of every old column and append the three pure-anchor columns x e_c,y e_c,v e_c at weights -1,2,4. The resulting F has d+1 rows and

  N=n_0+3=3d+M+4=11m^2+8m+14+2p

columns. Equations (7) and the two scalar formulas give

  FF^T=I_(d+1),       F Delta F^T=0.                    (8)

Every column has a nonzero anchor coordinate. Every column is sqrt(s_j') times a rational vector: for example zeta_(i,1)/a=(2r_i+t_0)/(3a^2) is rational. The pure weight-4 anchor is deliberately represented with factor sqrt(s), vector v_0 e_c, matching the factor of the selected duplicate shield column.

Put P=F^TF, Q=I-P, R=2P-I. Delta has exactly d+1 negative entries -1; every other entry is at least 2. To prove the strict exposing gap, view its isotropic subspace ran P as a graph (u,Tu) over the negative coordinates. Equation (8) gives T^T Delta_+ T=I and ||T||^2<=1/2. Its Euclidean orthogonal complement consists of (-T^T v,v), on which the Delta quadratic form is at least the Euclidean norm squared. Therefore

  S_0=Delta+R Delta R=2Q Delta Q>=2Q.                   (9)

This is an explicit fixed gap, not an unknown singular-value margin.

## 4. A deterministic polynomial grid with a proved overlap margin

Choose eta_0 to be the largest positive dyadic number satisfying

  (2eta_0)^2 Zeta<=1/1000,
  2eta_0<=v_0/100.

This is found by rational comparisons. Its reciprocal is polynomial in d,Mbar; for example it is bounded by 400/v_0+4 sqrt(1000 Zeta).

Let J_1=n_0(n_0-1)/2+1 and test

  eta_j=eta_0(1+j/(J_1-1)), j=0,...,J_1-1.

For each pair of distinct old columns the inner product is

  a_ij+eta_j^2 zeta_i zeta_j.

The successive eta_j^2 are separated by more than 2eta_0^2/J_1. Since |zeta_i zeta_j|>=epsilon, at most ONE grid point for this pair can have absolute inner product smaller than

  beta_*=epsilon eta_0^2/(2J_1).

There are J_1-1 pairs, so a grid point exists where EVERY such inner product has magnitude at least beta_*. Choose the first. Its exact comparisons are rational after squaring the known column factors.

The old squared column norms stay within 1/1000 of a^2,beta^2 or at most h^2, so none approaches 1/2. The pure-anchor squared norms satisfy x^2,y^2>=1/4 and have a fixed separation from 1/2; v is nonzero. Hence every entry of R is nonzero. A valid rational lower bound is

  eta_R=min(2beta_*, eta_0 epsilon v_0/2, v_0^2/8, 1/10). (10)

The unit anchor vector nu=F^T e_c has every coordinate of magnitude at least

  eta_nu=min(eta_0 epsilon, v_0/2, 1/2).                 (11)

These bounds account separately for old/old, old/pure-anchor, pure/pure, and diagonal entries. Their reciprocals are polynomial in d,Mbar,epsilon^{-1}. Finite exact avoidance is therefore quantitatively conditioned, not a genericity assertion.

## 5. Nonreflection, without losing the degree-two coefficient model

Let a be one duplicate shield-column index, a' its untouched duplicate, and b the pure weight-4 anchor index. The two selected columns have the SAME factor sqrt(s):

  f_a=sqrt(s)(h e_s,eta),    f_b=sqrt(s)(0,v_0).

Let O(t) be the rational plane rotation on these indices with

  c(t)=(1-t^2)/(1+t^2),   l(t)=2t/(1+t^2),
  O_aa=O_bb=c, O_ba=l, O_ab=-l,

and set U(t)=R O(t). Since both weights equal 4, O commutes with Delta, and the exposing certificate (9) is unchanged. Every unrotated column keeps its old second-basis observation. Removing indices a,b leaves a complete spanning analysis: the untouched duplicate restores f_a, and the other two pure anchors restore the scalar anchor projector.

### Why some rotation is genuinely nonreflection

For an orthogonal matrix U, form its row and column fourth-moment multisets, with row value sum_j U_ij^4 and column value sum_i U_ij^4. Independent signed row/column permutations do not change either multiset. A symmetric matrix has identical multisets.

Under rotation of columns a,b, only TWO column fourth moments can vary. But at least THREE row fourth moments are nonconstant functions of t. Use the rows belonging to the two unrotated pure anchors and the row a'. Their derivatives at zero are nonzero multiples of

  R_ia R_ib (R_ia^2-R_ib^2).

For either unrotated pure-anchor row the two entries are proportional to eta and v_0, respectively, and eta<v_0/100. For a' the entries are 2s(h^2+eta^2) and 2s eta v_0, unequal and nonzero. Thus all three derivatives are nonzero.

If the row and column multisets agreed identically on an interval, their monic root polynomials would agree. The N-2 constant column roots, with multiplicity, would force at least N-2 row functions to be constant (use the integral-domain property of real analytic functions in each linear factor). This contradicts the three nonconstant rows. Therefore at least one of the first N power-sum differences is a nonzero rational function of t. After multiplying by (1+t^2)^{4k}, its numerator has degree at most 8k<=8N.

### Simultaneous quantitative selection

Put xi=min(eta_R,eta_nu), J_2=12N+5, and Delta_t=1/[10(J_2-1)]. Test the J_2 points

  t_j=1/10+j Delta_t, j=0,...,J_2-1.

Each of the 2N rotated entries, and the two rotated anchor coordinates, has a quadratic numerator in t whose coefficient maximum is at least xi. For a polynomial of degree at most two, Lagrange interpolation on three grid nodes in [1/10,1/5] bounds its coefficient maximum by 12 Delta_t^{-2} times the largest of its three values. Consequently at most TWO nodes can have numerator magnitude below xi Delta_t^2/100.

The entry/anchor conditions therefore exclude at most 4N+4 nodes. The nonzero power-sum polynomial excludes at most 8N nodes. Since J_2=12N+5, a node satisfying all conditions exists. Test the rational squared magnitudes and the exact rational fourth-moment multisets and choose the first successful node.

At that node,

  eta_*:=xi Delta_t^2/200>0                            (12)

is a lower bound for every |U_ij| and every coordinate magnitude of both the first and second anchor vectors. The denominator 1+t^2 is less than 2. No small-angle assumption is needed.

Because f_a and f_b have the same factor sqrt(s), rotating the two corresponding columns of R never adds unrelated radicals. Every entry of U remains rational or a rational multiple of one square root of a positive rational. Its fourth powers, and all exact comparisons used above, are rational. The algorithm uses polynomially many rational operations with polynomial bit lengths. It does not use an oracle for signs of arbitrary algebraic sums.

## 6. Targets and exact entire fibres

Let J_s be the inner encoder of 06 and define

  E(X)=F^T(J_s(X) direct-sum [1])F,
  V=[V_0,0]F.

For the first basis prescribe:

- for a coordinate triplet column (p e_i,eta zeta_j), value p^2 theta_i tau+eta^2 zeta_j^2;
- for a G column (h g_j,eta sqrt(s_j)), value h^2 c_j(b)+eta^2 s_j;
- for the pure anchors, x^2,y^2,v^2.

For the second basis only indices a,b differ. Their values are

  s[c^2 h^2 tau+(c eta+l v_0)^2],
  s[l^2 h^2 tau+(-l eta+c v_0)^2].                       (13)

All these values are rational affine functions of b. Denote the full target by y_b=Phi b+y_0.

The signed target pairing with the coefficient vector (diag Delta,diag Delta) is zero for EVERY b. The inner-source part cancels by -a^2+5beta^2+4h^2=0 and sum_j c_j=tau sum_i theta_i. The anchor part cancels by (8). Rotation preserves the weighted sum because its two weights are equal.

Every exact PSD ambient solution is therefore supported on P by (9). On that support the first list, or the retained list, determines the anchor scalar, every source-to-new-anchor cross entry, and all frame outputs. The pure anchor gives scalar 1. The difference of the two beta-coordinate observations gives each anchor cross entry; their nonzero coefficient is displayed in Section 7. Subtracting those known entries from the G observations gives M_G(Z)=c(b). Consequently the EXACT full fibre is

  T_b={F^T(Z direct-sum [1])F : Z>=0,M_G(Z)=c(b)}.        (14)

It is generally much larger than E(F_b). Equation (6) gives soundness, and J_s gives completeness. This proves (2) including inconsistent data.

For feasible b and any source X in F_b, the source term in each observation of E(X) is nonnegative. The anchor term is at least eta_*^2 by (12). This proves strict uniform positivity even at X=0. At zero source, the inner coordinate data vanish and PSD forces Z=0, giving T_0={Y_0}, where Y_0=F^T e_c e_c^T F.

## 7. Explicit all-PSD residual constant

For arbitrary augmented symmetric Z write its new-anchor scalar as s_c, cross vector as z_c, and old principal block as Z_old. Let e be its vector of retained frame-output residuals from the prescribed targets. All assertions in this paragraph are linear identities; positivity is unnecessary.

An unrotated pure anchor gives

  |s_c-1|<=4||e||_2.

For coordinate i, with the two beta columns indexed 2,3,

  (z_c)_i=[e_(i,3)-e_(i,2)
            -eta^2(zeta_(i,3)^2-zeta_(i,2)^2)(s_c-1)]
           /[2 beta eta(zeta_(i,3)-zeta_(i,2))].         (15)

Since beta(zeta_3-zeta_2)=(5r_i+7t_0)/3>=2t_0 and eta^2 Zeta<=1/1000,

  ||z_c||_2<=sqrt(d) eta^{-1}||e||_2.

For each old frame column,

  g_j^T Z_old g_j-c_j(b)
   =h^{-2}[e_j-2h eta sqrt(s_j)g_j^T z_c
                  -eta^2 s_j(s_c-1)].                 (16)

Use the untouched duplicate when j=a. The G-error vector then obeys

  ||M_G(Z_old)-c(b)||_2 <= C_G ||e||_2,
  C_G=100(2+sqrt(d)+4sqrt(Mbar)).                        (17)

To verify the constant, duplication increases the selected error norm by at most sqrt(2); Parseval tightness and s_j<=1 bound the cross-output norm by ||z_c||; the scalar term has coefficient-vector norm at most sqrt(Mbar). The eta^{-1} in (15) cancels against eta in (16). Thus decoded source soundness does not depend on a tiny anchor inverse.

For ambient PSD Y put delta=||B_U(Y)-y_b||, Z=FYF^T and

  kappa=||diag Delta||_2/sqrt(2)
        =sqrt((14d+16Mbar+21)/2).

The stress gives tr(QYQ)<=kappa delta. On every retained coordinate, U equals R, so averaging the two measured residuals cancels exterior cross blocks exactly. It gives

  ||e||_2 <= (1/sqrt(2)+kappa)delta.

Combining (6) and (17) proves (3) with

  K_+=epsilon^{-1} C_R C_G(1/sqrt(2)+kappa).             (18)

This estimate is global in delta and b and applies to arbitrary ambient PSD ranks. Equations (15)–(16) also define an explicit rational extraction matrix R_obs supported on retained coordinates, with

  A D_0(Z_old)=R_obs (f_j^T Z f_j)_j,
  R_obs y_first(b)=b,
  ||R_obs||<=epsilon^{-1} C_R C_G.                      (19)

## 8. Minimum faces, ranks, and exact facial depth

For nonzero source data, use canonical coordinates J_s(X)=X direct-sum K(X) with K(X)>0 from 06. The new anchor is also positive. If E_b is the maximum source support, then (14) and positivity of the compression decoder imply

  L_b=F^T( V_0^T E_b direct-sum ker V_0 direct-sum R e_c )

is exactly the minimum lifted support. The encoder of a maximum-rank source point is positive definite on this support. Its dimension is

  r_b+d-m+1=r_b+m^2+m+3.

The same argument applied to an individual source X proves the stated maximum preimage rank.

The retained compressed observable span is exactly

  W_aug={[[B,z],[z^T,s]]:B in range M_G*, z arbitrary,s arbitrary}.

Equations (15)–(16) prove this equality, including the rotated case. A measured facial certificate positive on E_i direct-sum ker V_0 direct-sum R e_c and annihilating E(X_*) must kill every auxiliary and anchor direction. Its original-source block belongs to range A* by pulling back through the LINEAR part of J_s direct-sum 1. Conversely D_0*(A*y) direct-sum 0 is measured and performs any source step. Thus the augmented inner singularity degree is exactly the source degree.

For the outer step use the same proof as 06, with representations supported on retained coordinates. Their diagonal coefficient matrix has zeros at a,b and hence commutes with O. Reflection averaging gives a block-diagonal P/Q observable. Adding enough of S_0 makes its Q block positive definite, merging outer exposure with the first nontrivial source step. Intersecting arbitrary ambient chains with P proves the reverse inequality. Hence (4) holds. At b=0 the measured old-block identity plus outer exposure leaves only the positive anchor in one step, so the depth is one.

## 9. Both duals and finite attainment, despite the affine anchor

Given a source dual feasible lambda, let f=R_obs^T lambda, extended by zero at rotated indices. Then

  F diag(f)F^T=diag(D_0*(A*lambda),0),
  f.y_first(b)=lambda.b.

Because f_a=f_b=0, its diagonal matrix commutes with O. Thus gamma_0=(f/2,f/2) satisfies

  B_U*gamma_0=D*(A*lambda)+Q diag(f)Q.

Exactly as in 06,

  gamma=gamma_0-(||f||_infinity/2)(diag Delta,diag Delta)

is lifted-dual feasible for the pulled-back cost, with objective exactly b.lambda. Its norm is bounded by the explicit formula (6) of 06 with the bound (19).

Conversely, for ANY lifted feasible dual multiplier gamma, its PSD slack S=D*C-B_U*gamma pulls back through the positive linear part E_lin to

  E_lin*S=C-A*(Phi^T gamma)>=0.

The source multiplier lambda=Phi^T gamma is feasible. The affine offset satisfies

  y_0.gamma=-<Y_0,S><=0,

because D(Y_0)=0. Therefore b.lambda>=y_b.gamma. These two transformations prove equality of extended-real dual suprema. If a finite optimum is attained on either side, the appropriate transformation attains the same optimum on the other: in the reverse direction the inequality must be equality at an optimum. No dual Slater or dual-attainment assumption was introduced.

For a concrete pathology that is preserved, take m=2, A(X)=(X11,X22), b=(1,0), and C=[[0,1],[1,0]]. The source fibre is {E11}, with optimum zero, but its dual requires lambda_1<0 and lambda_1 lambda_2>=1; the supremum zero is not attained. The present N=78 two-basis instance has all-positive observations, no zero overlaps, a genuinely nonreflection U, and the SAME failure of dual attainment. Thus the observational nondegeneracies do not falsely regularize dual optimization.

## 10. Sharp ambient modulus and the zero exception

For nonzero feasible b, all arguments of 06 apply to (14). The upper proof uses the minimum support above and

  tr((I-P_{L_b})Y)<=kappa delta+mu_b(K_+ delta).

Use the explicit compression, affine pseudoinverse correction, and relative-interior mixing bound (8)–(10) of 06, with

  lambda_* >= min(lambda_min(X_*|E_b), nu tau,1),
  tr Y_*=(m rho+2+m^2 alpha)tau+1.

This proves Omega_b(delta)<=C sqrt(delta+mu_b(delta)), with the displayed source/face conditioning.

The shield lower bound survives unchanged: the raw and completed old vectors never mix shield and source; the coordinate triplets do not do so either; the two rotated vectors have old component only in the shield and otherwise the new anchor. Therefore every source-to-shield cross perturbation used in 06 is invisible in BOTH basis lists. The same Schur-positive lift proves the matching sqrt(mu_b) lower bound.

For the sqrt(delta) lower bound, the invisible cross-block space from two positive target directions into Q has dimension 2(N-d-1)>N. The first diagonal imposes at most N-1 constraints. The rotated second list adds at most ONE independent constraint, since its two new entries have the same sum as before. Thus a nonzero invisible cross block exists. The Gram-repaired curve in 06 proves the lower bound against the entire fibre. This establishes (5) for nonzero b.

At b=0, frame extraction controls the trace of the PSD old compressed block by O(delta), and the stress controls exterior trace by O(delta). Relative to the unit rank-one target vector nu, write

  Y=a nu nu^T+nu w^T+w nu^T+Z_perp,
  w perpendicular to nu, Z_perp>=0 on nu^perp.

The preceding mass estimates give tr Z_perp<=B delta for an explicit polynomial B; trace measurement gives |a-1|<=(sqrt(N)+B)delta. Each first-basis residual is

  r_j=(a-1)nu_j^2+2nu_j w_j+(Z_perp)_jj.

Since min_j|nu_j|>=eta_*, division gives ||w||=O(delta), with polynomial constant in eta_*^{-1}, B and N. Hence ||Y-Y_0||=O(delta). Scaling Y_0 provides the matching linear lower bound. This proves Omega_0~delta with all observations strictly positive, rather than replacing the zero case by the nonzero square-root law.

The rational all-depth separation family in 06 still has source exponent 2^{-(k-1)} and exact ambient exponent 2^{-k} in this dense, positive-data, nonreflection version. Depth remains exactly k for k>=1. This supplies all-depth sharpness examples for the unified theorem, not only for a reflection with zero overlaps.

## 11. Complete positivity, amplification, and complexity

By 07 the linear map J_s is completely positive. Thus E_lin(X)=F^T(J_s(X) direct-sum 0)F is completely positive, and the fixed offset is the PSD rank-one Y_0. D is one-Kraus. The algebraic identities extend to all matrix levels; the block-PSD stress and Frobenius estimates (10)–(11) of 07 work on retained coordinates here. Therefore the SAME K_+ works for arbitrary untouched ancillary order, with the affine offset tensored by I_n.

All raw data are rational. Rational LDL completion gives column factors sqrt(s_j)u_j. The anchor ratios, eta grids, pure-anchor squared norms, Cayley rotation and targets are rational. Matching the two rotated factors prevents sums of unrelated radicals. Every returned coefficient therefore remains individually of degree at most two with polynomial bit length. The two finite grids have polynomial size and use only rational comparisons. Their explicit margins (10)–(12) are inverse-polynomial in normalized source magnitudes and dimensions, not nonconstructive generic gaps.

The ordinary source conditioning, forward encoder/data-map norms, two-sided weak-feasibility gap transfer and finite-precision estimates follow from 03 with the explicitly returned affine map and the new K_+. Without a supplied trace certificate, the conditioned certificate-finding algorithm of 03 remains available. No unconditioned exact SDP solver is asserted.

## 12. Audit summary

This is one uniform construction for every source, not a classification by low-dimensional cases. Its free auxiliary covariance is retained, so it remains a quotient rather than the forbidden exact-bijection model. The first and second genericity choices are replaced by finite rational grids with quantitative margins. Nonreflection is proved by a signed-permutation invariant, not by merely checking U!=U^T. The rotated columns have matched radical factors, avoiding a hidden exact-bit-complexity regression. Noise recovery uses retained outputs and exact even averaging; it does not assume access to the unrotated missing outputs. Both SDP duals are treated with the affine anchor offset accounted for. Zero data, arbitrary ranks, nonsingleton fibres and arbitrary source singularity degree are covered. Ambient and decoded moduli are explicitly distinguished.

Numerical and exact-symbolic diagnostics are in the strengthening audit scripts; they support the audit but are not premises of the proof. External literature priority and independent referee certification remain separate, uncompleted tasks.
