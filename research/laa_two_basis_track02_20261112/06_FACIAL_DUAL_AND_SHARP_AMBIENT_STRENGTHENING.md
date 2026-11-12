# Milestone 06 — facially and dually faithful quadratic universality, with an exact ambient modulus

Date: 2026-11-12. Builds on the explicit, independently algebraic construction in 02–04, pinned at 005b1267599a2c18abe37879b4959061bf47729a. The results below do not follow merely from decoded residual soundness. They identify the minimal lifted face, preserve the number of facial-reduction steps, transfer both SDP duals, and determine the optimal whole-ambient recovery modulus.

## 1. One construction and the stronger theorem

Use the notation of 02. Make precisely two modifications:

1. Choose the STRICT rational trace bound rho=2 tr(H^{-1}), where H=A*z>0. Thus rho H >= 2 I.
2. Add one shield coordinate s to the inner matrix and set its forward variance to t=<H,X>. Add its coordinate measurement with target tau=z.b and its scalar Parseval-completion column. No other raw measurement involves s.

Write

  J_s(X)=J(X) direct-sum [<H,X>],
  d=(m+1)^2+1,
  M_0=7m^2+2+2p,
  M=M_0+d=8m^2+2m+4+2p,
  N=d+M=9m^2+4m+6+2p.

The decoder V_0 is unchanged on the old coordinates and zero on s. Use the same completion and reflection formulas:

  F=[sqrt(2/3) I_d, G/sqrt(3)],
  P=F^T F, Q=I-P, U=2P-I,
  V=V_0 F, D(Y)=VYV^T, E(X)=F^T J_s(X)F.

The constant L of 02 is unchanged: the added raw frame-operator block is just [1]. The reverse residual constant becomes

  C_R=sqrt(9 S_A/16+p/8),
  K_r=3 sqrt(2) L (1+sqrt(33m^2+10m+18+8p)) C_R.

All primal, all-data, positivity, objective, polynomial-bit and individually quadratic-algebraic assertions of 02–04 remain valid, with these counts. In particular D E=id, B_U E=Phi A, and D(T_b)=F_b, where T_b denotes the ENTIRE two-basis fibre.

### Stronger conclusions for every nonempty F_b

For b!=0 let E_b be the range of a maximum-rank source feasible point, let r_b=dim E_b, and let k_b be the ordinary singularity degree, defined as the shortest measured facial-reduction chain to E_b. Then:

(a) The minimum lifted support is exactly

  L_b=F^T( V_0^T E_b direct-sum ker V_0 ).                 (1)

Its dimension is r_b+d-m. For every source feasible X!=0, the maximum rank of a lifted preimage of X is exactly rank(X)+d-m, attained by E(X).

(b) The inner frame fibre has singularity degree exactly k_b. The actual two-basis fibre has singularity degree

  k_lift=max(1,k_b).                                      (2)

At b=0 both fibres are {0} and the lifted singularity degree is one.

(c) Source and lifted STANDARD SDP duals have exactly the same extended-real supremum. Dual feasibility is equivalent; finite dual attainment is equivalent. No primal Slater, dual Slater, or zero-duality-gap assumption is needed. Consequently every existing primal-dual gap is preserved, not repaired or concealed.

(d) Define the ORIGINAL-SOURCE leakage modulus

  mu_b(t)=max{ tr(P_{E_b^perp} X): X>=0, ||A(X)-b||_2<=t }.

Define the entire lifted worst-case modulus

  Omega_b(t)=max{ dist_F(Y,T_b):Y>=0, ||B_U(Y)-Phi b||_2<=t }.

For every fixed nonzero feasible b,

  Omega_b(t) asymp sqrt(t+mu_b(t)) as t decreases to zero. (3)

Here asymp means two-sided positive fixed-instance constants. Explicit scaled inequalities and constants are proved below. This is an ambient statement over ALL PSD competitors and distance to the ENTIRE lifted fibre, not merely decoded distance or distance to the encoder image. At b=0, Omega_0(t) asymp t.

The function mu_b depends only on the original source problem and its minimum face. It is a maximization of a linear face-normal functional over the original bounded residual sublevel set, not a relabeling of the lifted distance modulus.

(e) For every integer k>=1 there is an explicit rational source of order k+1 with singularity degree k, source distance modulus Theta(t^{2^{-(k-1)}}), and leakage modulus Theta(t^{2^{-(k-1)}}), whose compiled ambient modulus is exactly Theta(t^{2^{-k}}). Thus equality of singularity degrees does NOT imply equality of optimal recovery exponents. The ambient law (3), rather than the generally false replacement Omega~omega_source+sqrt(t), handles every source fibre uniformly.

## 2. Uniformly positive auxiliary complement

Use the orthogonal decomposition R^d=ran(V_0^T) direct-sum ker(V_0). The Hadamard change of coordinates on the old l/r block gives

  J_s(X)=X direct-sum K(X).

The auxiliary K(X) consists of rho t I-X, the old arrow block [[t,x^T],[x,alpha t I]], and the shield [t]. For X>=0,

  tr X <= rho t/2,
  rho t I-X >= rho t I/2.

As in 02, ||x||^2 <= alpha t^2/4. After congruence by diag(1,sqrt(alpha) I), the arrow divided by t has diagonal blocks I and offdiagonal norm at most 1/2. Therefore

  K(X) >= nu t I,   nu=(1/2)min(rho,1,alpha)>0,          (4)

for every X!=0. The identity J_s=X direct-sum K(X) holds for all symmetric X; K is linear and positive.

This is the key regularity property: ALL auxiliary directions are strictly positive at EVERY nonzero PSD source point, not only at a selected full-rank point.

For any PSD Z with D_0(Z)=X, positivity implies that Z annihilates V_0^T ker X. Indeed v^T Xv=0 implies (V_0^T v)^T Z(V_0^T v)=0, hence ZV_0^T v=0. Thus every preimage of X is supported on V_0^T ran X direct-sum ker V_0. The forward J_s(X) is positive definite on precisely that space by (4), and attains its dimension as rank. This proves the pointwise preimage-rank assertion.

A maximum-rank source feasible point X_* has support E_b containing every feasible source support: otherwise averaging it with another feasible point increases rank. Exact surjectivity and the preceding paragraph prove the inner minimum support E_b direct-sum ker V_0; reflection exposure then proves (1).

## 3. Exact inner singularity degree

Let M denote the completed frame map on S^d and c its target. Two identities from 02 are essential:

  A D_0=R M,      M J_s=Phi_0 A,                        (5)

where R=epsilon^{-1}R_0 P_raw is explicit. Thus D_0*(range A*) is contained in range M*, and J_s*(range M*) is contained in range A*.

Lift a source facial chain to the inner space using D_0*(A*y)=diag(A*y,0). Its PSD compression to E_i direct-sum ker V_0 performs the same source support reduction and leaves the auxiliary factor untouched. Its pairing with J_s(X_*) is zero. This gives k_inner<=k_b.

Conversely consider ANY inner facial chain. Inductively its current support has the form E_i direct-sum ker V_0. A measured certificate S in range M* with PSD compression there and zero pairing with J_s(X_*) must annihilate the whole auxiliary space, because K(X_*) is positive definite. Consequently the entire auxiliary diagonal block of S is zero, and its cross block vanishes after restriction to E_i. Write H for its original-source diagonal block. Since J_s has no source/auxiliary cross terms,

  J_s*(S)=H.

By (5), H lies in range A*. Its compression to E_i is PSD, has zero pairing with X_*, and performs exactly the induced support reduction. Thus every inner chain projects to a source chain of no greater length. This proves k_inner=k_b. Notice that no assertion about an arbitrary positive section would suffice: strict positivity of K(X_*) is used to eliminate every auxiliary block of each certificate.

## 4. Exact outer singularity degree

Put Delta=diag(-I_d,2I_M). The measured zero stress

  S_0=Delta+U Delta U^T=2Q Delta Q>=2Q

exposes ran(F^T).

For a source/inner FIRST globally PSD measured certificate H, choose a diagonal coefficient vector lambda with F diag(lambda)F^T=H. The half-sum of its two basis observables is

  P diag(lambda)P+Q diag(lambda)Q.

Adding a sufficiently large positive multiple of S_0 makes the Q block positive definite while retaining H on P. Thus the first ambient facial step removes Q and performs the first inner facial step SIMULTANEOUSLY. Subsequent inner steps are used on the remaining support inside P. If k_b>=1 this gives k_lift<=k_b; if k_b=0, S_0 alone gives k_lift<=1.

For the reverse inequality, intersect each ambient chain support with ran P. For a certificate positive on its current ambient support, zero quadratic form is equivalent to membership in its compressed kernel. Therefore intersecting its next kernel with P gives exactly the next kernel of the certificate restricted to the current intersection. The compressed observables are in range M*, since coordinate projectors are already in that span. After deleting unchanged steps this is a valid inner facial chain. Hence k_lift>=k_b. Since the exact ambient fibre is confined to a proper face, k_lift>=1 for a nonempty nonzero fibre. This proves (2).

At b=0 trace control forces X=0, every prescribed diagonal is zero, and the first basis forces Y=0. The measured identity exposes zero in one step.

## 5. Both SDP duals, including attainment

Use the minimization convention. The source dual is

  sup b.lambda subject to C-A*lambda>=0.

The lifted dual is

  sup (Phi b).gamma subject to D*C-B_U*gamma>=0.

### Every lifted certificate pulls back with EXACT value

The encoder E is linear and positive in the present milestone. If T=D*C-B_U*gamma>=0, then E*T>=0 and

  E*T=C-A*(Phi^T gamma).

Thus lambda=Phi^T gamma is source-dual feasible, with b.lambda=(Phi b).gamma.

### Every source certificate lifts with EXACT value

For a source-dual feasible lambda, let a=3R^T lambda, indexed by the G columns, and set f=(0_d,a). Then

  F diag(f)F^T=D_0*(A*lambda),
  f.y_0=lambda.b.

Set gamma_0=(f/2,f/2), w=(diag Delta,diag Delta), and eta=||f||_infinity/2. Reflection averaging gives

  B_U*gamma_0=D*(A*lambda)+Q diag(f)Q.

Choose gamma=gamma_0-eta w. Its slack is

  D*(C-A*lambda)-Q diag(f)Q+eta S_0>=0.

The first term is PSD on P; the remaining Q block is PSD because S_0>=2Q. Since w.Phi b=0, the objective is lambda.b. Moreover

  ||f||_2<=3 epsilon^{-1}||R_0|| ||lambda||_2,
  ||gamma||_2<=||f||_2/sqrt(2)+(||f||_infinity/2)||w||_2. (6)

This is an explicit polynomial multiplier bound. No closed-image or dual-attainment theorem is invoked.

The two certificate transformations prove equality of dual feasible-value sets, hence extended-real suprema, and equivalence of finite attainment. Combined with exact primal surjectivity, they preserve every primal-dual gap. Source dual infeasibility is also equivalent to lifted dual infeasibility.

## 6. Source leakage properties

For nonzero feasible b, tau=z.b>0. A source residual bound implies

  tr X <= (rho/2)(tau+||z||t).

Thus the sets defining mu_b(t) are compact. They contain F_b and mu_b(0)=0. Compactness shows mu_b(t)->0 as t->0. The function is nonnegative, nondecreasing, and concave: mix maximizing feasible competitors at two radii, use convexity of the norm bound, and use linearity of tr(P_{E_b^perp}X).

Consequently for c>0,

  min(1,c) mu_b(t) <= mu_b(ct) <= max(1,c) mu_b(t).       (7)

If E_b=R^m, mu_b is identically zero. Otherwise mu_b(t)>=a_b t for some a_b>0: test X_*+s P_{E_b^perp}. Trace control ensures A(P_{E_b^perp})!=0.

## 7. Whole-ambient upper bound with explicit conditioning

Fix X_* of maximum source rank and Y_*=E(X_*). Let Pi be the projector onto L_b. Define

  lambda_* = lambda_min(Y_*|L_b)>0,
  sigma_* = smallest positive singular value of
             B_U restricted to S(L_b),
  M_b=tr Y_*+sqrt(N).

The bound (4) gives

  lambda_* >= min(lambda_min(X_*|E_b), nu tau).

These are explicit fixed-instance conditioning parameters. The construction does not require finding X_* or L_b. No uniform lower bound for these source-dependent margins is asserted.

For arbitrary Y>=0 with residual delta<=1, trace measurement gives trY<=M_b. The exposing stress gives tr(QYQ)<=kappa delta, where kappa=sqrt((d+4M)/2). Also X=D(Y) is PSD with source residual <=K_r delta. The support identity (1) therefore yields

  tr((I-Pi)Y)<=r(delta):=kappa delta+mu_b(K_r delta).

PSD block Cauchy–Schwarz gives

  e_0(delta):=||Y-Pi Y Pi||_F
       <=r(delta)+sqrt(2 M_b r(delta)).                   (8)

Let L_Pi=B_U|S(L_b). Since the exact target lies in its image, the symmetric correction

  T=L_Pi^dagger(Phi b-B_U(Pi Y Pi))

is well defined, supported on L_b, and has norm at most

  a(delta)=sigma_*^{-1}(delta+sqrt(2)e_0(delta)).          (9)

The affine-corrected matrix Z=Pi Y Pi+T has the exact target and eigenvalues at least -a(delta) on L_b. Therefore

  Z_+=(1-theta)Z+theta Y_*,
  theta=a(delta)/(lambda_*+a(delta)),

is PSD and exactly feasible. It follows that

 dist_F(Y,T_b)
 <=e_0(delta)+a(delta)
     +(a(delta)/lambda_*)[M_b+a(delta)+||Y_*||_F].         (10)

This estimate holds whenever delta<=1 and remains valid without assuming a(delta)<=1. For sufficiently small delta, (7)–(10) give

  Omega_b(delta)<=C_b sqrt(delta+mu_b(delta)).            (11)

The dependence in (8)–(10) is polynomial in the displayed inverse singular/relative-interior margins and source/constructed norms. In particular there is no claim of a dimension-only condition number for degenerate source systems.

## 8. Matching ambient lower bound from the shield

Every inner frame vector either avoids the shield or is supported entirely on it. Thus for EVERY source vector h,

  M( (V_0^T h)e_s^T+e_s(V_0^T h)^T )=0.                 (12)

Take a source competitor X>=0 with residual at most t, and put t_X=<H,X>. For t<=tau/(2||z||), t_X>=tau/2. Choose a unit vector v maximizing ||P_{E_b^perp}X^{1/2}v|| and put

  h=sqrt(t_X/2) X^{1/2}v.

In canonical source/auxiliary coordinates, add h as the source-to-shield cross block of J_s(X). The resulting Z_X is PSD: the source/shield Schur complement is

  X-hh^T/t_X>=X/2.

All other auxiliary blocks remain PSD. Equation (12) says its measured data are exactly those of J_s(X). Its decoded source is still X. The two-basis lift F^T Z_X F thus has residual at most K_f t, where K_f=||Phi||_{2->2} (or any explicit larger bound from 03).

Every exact lifted solution annihilates the forbidden source directions E_b^perp. Hence its distance from this competitor is at least

  sqrt(2)||P_{E_b^perp}h||
   >=sqrt(tau/(2m)) sqrt(tr(P_{E_b^perp}X)).

Taking a source leakage maximizer proves

  Omega_b(K_f t)>=sqrt(tau/(2m)) sqrt(mu_b(t)).           (13)

There is independently an ambient square-root obstruction. Y_* has rank at least two. The space of cross blocks from two positive support directions of Y_* into Q has dimension 2(N-d)>N-1. Therefore a nonzero cross block K exists with diag(K+K^T)=0. Reflection changes the sign of this cross block, so both diagonal variations vanish. The exact PSD curve

  Y(u)=Y_*+u(K+K^T)+u^2 K^T Y_*^dagger K

is a Gram-factorized matrix of the same rank as Y_*. Its data residual is Theta(u^2), since trace is measured and the repair is nonzero. Its distance from T_b, which is supported inside P, is at least sqrt(2)|u| ||K||_F. Consequently

  Omega_b(delta)>=c_b sqrt(delta).                      (14)

Combining (7), (11), (13), and (14) proves the full functional law (3). At b=0, the first complete diagonal gives ||Y||_F<=trY<=sqrt(N) delta; scaling any nonzero PSD matrix gives the matching linear lower bound.

## 9. Explicit all-depth separation family

For every k>=1 put m=k+1 and impose the rational equations

  tr X=1,
  X_{m,m}=0,
  X_{i,i}-X_{1,i+1}=0  (i=2,...,k),
  X_{1,2}=0.                                           (15)

The trace certificate is supplied by the first equation. The exact PSD fibre is the singleton X_*=e_1e_1^T: the zero last diagonal kills its entire row, then the preceding diagonal equation kills the preceding row, recursively.

The singularity degree is exactly k. A zero-pairing measured stress has zero coefficient of the trace equation, hence zero (1,1) entry. PSD forces its entire first row to vanish, eliminating all still-active cross-equation coefficients and the coefficient of X12. Initially only a nonnegative multiple of E_{m,m} can reduce support. After that coordinate is removed, only the next diagonal E_{m-1,m-1} can newly reduce support, and so on. Thus no step can skip a coordinate, and k steps suffice and are necessary.

For delta-small PSD competitors, bounded trace and the diagonal chain imply

  X_{m,m}=O(delta),
  X_{i,i}=O(delta^{2^{-(m-i)}}), i=2,...,m.

The trace equation controls X11-1 by their sum. X12=O(delta); for j>=3, PSD gives |X1j|<=sqrt(X11 Xjj)=O(delta^{2^{-(k-1)}}). All remaining entries have that bound as well. Therefore both source distance and leakage are O(delta^beta), beta=2^{-(k-1)}.

For sharpness take, before trace normalization,

  W(t)=v(t)v(t)^T+t^2 e_2e_2^T,
  v(t)=(1,0,t^2,t^4,...,t^{2^{k-1}}).

For k=1 the displayed vector is simply (1,0). Set X(t)=W(t)/trW(t). All equations in (15) except the last-diagonal equation hold exactly. Its residual is

  delta(t)=t^{2^k}/trW(t).

Its leakage and source distance are both Theta(t^2). Hence

  omega_source(delta) asymp mu_b(delta) asymp delta^{2^{-(k-1)}},
  Omega_lift(delta) asymp delta^{2^{-k}}.                 (16)

This family proves both that the ambient lower mechanism is real and that singularity degree alone need not equal the sharp source exponent. For k=2 it is the explicit 3-by-3 source trX=1, X33=0, X22-X13=0, X12=0: source exponent 1/2, lifted exponent 1/4, and facial depth two on both sides.

## 10. Audit and scope

The new statements use the minimum face of the entire source fibre, not the support of an arbitrary lower-rank feasible member. The strict auxiliary bound is global, including rank-one source matrices. Source and lifted costs are unchanged on every symmetric ambient matrix. Dual certificates are constructed in both directions, not inferred from primal equality. The shield lower curve is PSD by a displayed Schur complement and its cross entries are actually unmeasured. The upper bound corrects to the entire lifted fibre, with explicit relative-interior and affine-analysis margins. The all-depth family is an analytic proof, not finite numerical extrapolation.

No all-nonzero overlap or nonreflection assertion is made for the minimal reflection version of this milestone; those are addressed by a separate constructive compiler. No external priority or independent referee certification is claimed.

Context, not premises: classical facial-reduction error bounds include J. F. Sturm, Error Bounds for Linear Matrix Inequalities, SIAM J. Optim. 10 (2000), DOI 10.1137/S1052623498338606; and B. F. Lourenco, Amenable cones: error bounds without constraint qualifications, arXiv:1712.06221. The exact positive-quotient, duality-transfer, and shield-matching statements above are proved here rather than attributed to those works.
