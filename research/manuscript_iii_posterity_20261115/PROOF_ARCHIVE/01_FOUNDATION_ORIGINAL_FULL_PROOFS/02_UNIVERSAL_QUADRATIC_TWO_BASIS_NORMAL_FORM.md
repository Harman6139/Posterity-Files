# Fresh analytic milestone 02 — a universal quadratic-size two-basis SDP quotient

Date: 2026-11-12. Historical handoff: ff6117295c329dc88d5bc280ee18adfe64cda8b0.

## The structural insight

Do not force the auxiliary covariance to equal its chosen forward-lift value. Copy the entries of a bounded source block into correlations with one anchor, using four signed rank-one observations per entry. Arbitrary source equations then become anchor correlations with coefficient vectors. An isotropic auxiliary covariance supplies a positive lift of EVERY source point, while remaining largely unconstrained in the reverse direction. The resulting feasible fibres have very large decoder-invisible freedom. This is a many-to-one quotient, not an exact-bijection construction.

The copy observations have diagonal frame operator. The only nondiagonal remainder is entirely inside the auxiliary covariance block, where arbitrary additional rank-one observations have known forward values. This permits Parseval completion without revealing extra source information. The completed frame contains a coordinate ONB, so a single signed reflection converts it to two actual complete bases at linear overhead.

## 1. Main theorem

Let m>=1, p>=1 and A:S^m->R^p be given by real symmetric matrices A_1,...,A_p. Suppose a trace-control certificate z in R^p is supplied with

  H=A*z=sum_i z_i A_i > 0.

Choose any rho>0 with H>=(1/rho)I; for rational H one may take rho=tr(H^(-1)). Set alpha=m rho^2. For b in R^p put tau=z.b. No feasibility assumption on b is needed for the exact equivalence below.

There are explicit linear maps

  E:S^m -> S^N,     D:S^N -> S^m,     Phi:R^p -> R^(2N)

and an explicit real orthogonal reflection U in O(N), depending on A,H,rho but not on b or the objective, with

  N=9m^2+4m+3+2p <= 16m^2+2p,

such that:

**(a) Positive section and contraction decoder.** E and D are globally PSD-positive, D E=id, and D(Y)=V Y V^T for an explicitly known m-by-N matrix V with VV^T=I_m. In particular ||D||_(F->F)=1. A positive section is allowed, but the full lifted fibre is NOT required to equal the section image.

**(b) Two complete bases and exact data fidelity.** With

  B_U(Y)=(diag Y,diag(U^T Y U)),

one has the linear identity B_U E=Phi A on ALL symmetric source matrices. Set y_b=Phi b.

**(c) Exact entire-fibre surjection.** For every b, including inconsistent data,

  D({Y>=0:B_U(Y)=y_b}) = {X>=0:A(X)=b}.                    (1)

All ranks, singularity degrees, nonsingleton fibres and auxiliary PSD competitors are included. Empty source and lifted fibres occur together.

**(d) Explicit global residual bound.** Let

  S_A=sum_i ||A_i||_F^2,
  L=4m^2+6m+2p+6+2S_A,
  T=33m^2+10m+9+8p,
  K=3 sqrt(2) L (1+sqrt(T)) sqrt(9S_A/16+p/8).

For EVERY Y>=0 and every b,

  ||A(D(Y))-b||_2 <= K ||B_U(Y)-y_b||_2.                  (2)

The constant is independent of target rank, lifted rank, Slater feasibility, and any facial-reduction gap. The trace certificate affects the target size and forward encoder, not this reverse residual constant.

**(e) Exact objectives.** For every C in S^m, put C_tilde=V^T C V. Then for every symmetric Y,

  <C_tilde,Y>=<C,D(Y)>,    ||C_tilde||_F=||C||_F.

Thus feasible source and lifted optimization problems have identical attainable objective sets and identical optima.

**(f) Positive nonzero data.** If b is feasible and its source fibre is not {0}, every coordinate of y_b is strictly positive. If b=0, both exact fibres are {0} and y_b=0. The two bases are distinct; U is not a signed permutation. No claim that every overlap of the two bases is nonzero is needed or made for this minimal version.

**(g) Exact construction and representation.** For rational A,z,H,rho,b, the target y_b is rational. The coefficients of E,D,U have polynomial-size expressions using rational arithmetic and square roots of positive rational numbers. Given the rational trace certificate, the construction takes polynomially many rational bit operations and radical gates, with polynomial coefficient bit length. A precision/conditioning supplement is given in milestone 03; no unconditional polynomial-time exact SDP-solving claim is made.

The proof below gives every matrix and data entry explicitly.

## 2. A positive bounded-entry lift

Put k=m^2 and d=2m+1+k=(m+1)^2. Label the coordinates of R^d by

  l_1,...,l_m; r_1,...,r_m; a; q_11,...,q_mm.

The q coordinates are ordered by the same row-major vectorization convention as the entries of an m-by-m matrix. Let e_s denote the coordinate vectors.

Define V_0:R^d->R^m by

  V_0=(1/sqrt(2)) [I_m, I_m, 0, 0],

and D_0(Z)=V_0 Z V_0^T. Then V_0 V_0^T=I_m and D_0 is a positive contraction.

For an arbitrary symmetric X write t=tr(HX), B=X-(rho t/2)I_m, x=vec(B), and define J(X) by the orthogonal block sum

  J(X) = [ (rho t/2)I_m, B ; B, (rho t/2)I_m ]
         direct-sum
         [ t, x^T ; x, alpha t I_k ].                       (3)

This is linear in X and D_0 J(X)=X identically.

**Positivity for all X>=0.** If X>=0, then t>=0 and

  0<=X<=tr(X)I<=rho t I.

The first block of (3) is orthogonally congruent to X direct-sum (rho t I-X), hence PSD. Also ||B||_F^2<=m rho^2 t^2/4=alpha t^2/4. If t>0, the second block has Schur complement

  alpha t I_k-xx^T/t >= (3/4)alpha t I_k >0.

If t=0, trace control gives X=0 and J(X)=0. Thus J is globally positive, without any fixed-rank restriction.

Its diagonal is t times the positive vector

  theta=((rho/2)1_(2m), 1, alpha 1_k).                    (4)

Its auxiliary q-q block is alpha t I_k, its a-q correlations equal the entries of its l-r block, and both l-l and r-r blocks are (rho t/2)I_m. These facts determine the measurements below. The chosen forward auxiliary covariance is NOT subsequently imposed entry by entry.

## 3. The raw rank-one measurement list

Use the following M_0=7m^2+1+2p vectors v_j in R^d. Each has a prescribed squared-quadratic value c_j^0(b).

### Group A: all coordinates

For every coordinate s, take v=e_s, with target theta_s tau. There are d such vectors.

### Group B: the two fixed diagonal blocks

For each h in {l,r}, i<j, and sign s in {+1,-1}, take

  v=e_(h_i)+s e_(h_j),        target=rho tau.

There are 2m(m-1) vectors. Together with Group A they fix the l-l and r-r blocks to (rho tau/2)I_m.

### Group C: four-character entry copies

For every ordered pair (i,j) and signs s,u in {+1,-1}, take

  v_(ij,s,u)=e_a+s e_(q_ij)+u e_(l_i)-s u e_(r_j),
  target=(1+alpha+rho)tau.                                  (5)

There are 4m^2 such vectors. For ANY symmetric Z, not merely a forward lift, sign summation gives

  (1/8) sum_(s,u) s v_(ij,s,u)^T Z v_(ij,s,u)
       = Z_(a,q_ij)-Z_(l_i,r_j).                           (6)

Indeed the four coefficient functions 1,s,u,-su are mutually orthogonal on the four sign pairs. The diagonal terms and every unwanted cross term cancel in (6). Thus these measurements equate the anchor-copy and source-block entries, with no assumptions on other cross blocks.

### Group D: all original equations as anchor correlations

For each i=1,...,p let

  a_i=sum_(j,h) (A_i)_(j,h) e_(q_jh),
  beta_i=b_i-(rho tau/2)tr(A_i).

Take the two vectors

  v_(i,+)=e_a+a_i,       v_(i,-)=e_a-a_i,

with targets

  c_(i,+)^0=tau(1+alpha||A_i||_F^2)+2 beta_i,
  c_(i,-)^0=tau(1+alpha||A_i||_F^2)-2 beta_i.                (7)

Their difference reads the desired linear combination of the copied entries:

  (v_(i,+)^T Z v_(i,+)-v_(i,-)^T Z v_(i,-))/4=a_i^T Z e_a.  (8)

There are 2p vectors.

All targets are linear functions of b. Every J(X) has these targets with b=A(X), by (3). Conversely, every PSD Z with these raw targets decodes through D_0 to a PSD X with A(X)=b: Groups A–B fix the two diagonal blocks, (6) identifies every copied entry, and (8) enforces each original equation. This is already an exact rank-one PSD quotient, before tight-frame completion.

## 4. A quantitative matrix identity, not just exact-fibre reasoning

Let M_0(Z)=(v_j^T Z v_j)_j. There is an explicit p-by-M_0 matrix R_0 such that, for ALL symmetric Z and all b,

  A(D_0(Z))-b = R_0(M_0(Z)-c^0(b)).                        (9)

For row i its nonzero coefficients are:

* Group A, coordinates l_j and r_j: (A_i)_(j,j)/2 each.
* Group B, each block h, pair j<h, sign s: s(A_i)_(j,h)/4.
* Group C, ordered pair (j,h), signs s,u: -s(A_i)_(j,h)/8.
* Group D for the same equation i: +1/4 on its plus vector and -1/4 on its minus vector.

To check (9), write B_Z=Z_(l,r). Then

  <A_i,D_0(Z)>-b_i
   = (1/2)<A_i,Z_(l,l)+Z_(r,r)-rho tau I>
     + sum_(j,h)(A_i)_(j,h)(Z_(l_j,r_h)-Z_(a,q_jh))
     + a_i^T Z e_a-beta_i.

The displayed coefficients recover these three terms by polarization, (6), and (8), respectively. All constants cancel correctly, so R_0 c^0(b)=b.

The squared Euclidean norm of row i is

  (1/2)sum_j(A_i)_(j,j)^2
   +(1/4)sum_(j<h)(A_i)_(j,h)^2
   +(1/16)||A_i||_F^2+1/8
  <= (9/16)||A_i||_F^2+1/8.

Consequently

  ||R_0||_(2->2) <= sqrt(9S_A/16+p/8).                    (10)

No inverse of a poorly conditioned source measurement matrix is used.

## 5. Parseval completion without additional source restrictions

Let Q_0=sum_j v_j v_j^T be the raw frame operator. Sign cancellation gives EXACTLY

  Q_0=(6m-1)I_(2m)
       direct-sum [1+4m^2+2p]
       direct-sum [5I_k+2 sum_i a_i a_i^T],                 (11)

where a_i in the final block is identified with vec(A_i). In particular all nondiagonal entries lie in the auxiliary covariance block.

Set epsilon=1/(2L), with L as in the theorem. Then 0<Q_0<L I_d and

  R_c=I_d-epsilon Q_0 >= (1/2)I_d.                        (12)

Choose d columns h_s satisfying sum_s h_s h_s^T=R_c, respecting its block structure: scalar coordinate columns on the l,r,a blocks, and any Cholesky columns on the q block. Define the frame

  G=[sqrt(epsilon)v_1,...,sqrt(epsilon)v_(M_0),h_1,...,h_d]. (13)

It has M=M_0+d=8m^2+2m+2+2p columns and GG^T=I_d. Its projector span contains EVERY coordinate projector, since Group A was retained with positive weight.

For each raw column use target epsilon c_j^0(b). The completion columns have known targets on J(X):

* a completion column h supported on l or r has target (rho tau/2)||h||^2;
* the a-coordinate completion column has target tau||h||^2;
* any completion column supported on q has target alpha tau||h||^2.

Call the full M-vector c(b). Adding these measurements cannot remove any forward lift J(X), because its q-q covariance is alpha tr(HX)I. Conversely, the retained raw observations still give (9). Thus, with M_G(Z)=(g_j^T Z g_j)_j,

  D_0({Z>=0:M_G(Z)=c(b)})={X>=0:A(X)=b},                  (14)

and for all symmetric Z,

  A(D_0(Z))-b
    = epsilon^(-1) R_0 P_raw(M_G(Z)-c(b)),                (15)

where P_raw selects the first M_0 coordinates.

Also, for every b (whether feasible or not),

  sum_j c_j(b)=sum_s theta_s tau=(m rho+1+m^2 alpha)tau.    (16)

To verify this without assuming feasibility, sum the raw targets. Their two source-equation values in (7) cancel beta_i, so the sum is the trace pairing of Q_0 with diag(theta tau). The completion targets give the pairing with I-epsilon Q_0. Equation (16) follows.

For rational data, take a rational LDL^T decomposition of the positive definite q-block of R_c. If R_q=L_q diag(d_j)L_q^T, use h_j=sqrt(d_j)(L_q)_:j. Each d_j is a positive rational and every squared column norm d_j||(L_q)_:j||^2 is rational. Hence all targets c(b) are rational even though some frame coefficients are algebraic.

## 6. A two-basis compiler with only d+M coordinates

Set

  a=sqrt(2/3),     b_0=1/sqrt(3),
  F=[a I_d, b_0 G] in R^(d x N),       N=d+M,
  P=F^T F,       Q=I_N-P,       U=2P-I_N.

Then FF^T=I_d, P is an orthogonal projection, and U is a real symmetric orthogonal matrix. Its first d diagonal entries equal 1/3, so it is not a signed permutation. The standard basis and the columns of U are two distinct complete real orthonormal bases.

Let

  Delta=diag(-I_d,2I_M).

One has F Delta F^T=0. Moreover, for w=(x,z) in ker F,

  x=-Gz/sqrt(2),
  w^T Delta w-||w||^2=||z||^2-||Gz||^2>=0.

Thus Q Delta Q>=Q, and the measured stress

  S=Delta+U Delta U^T=2Q Delta Q>=2Q                     (17)

has kernel exactly ran P.

For a source datum b define

  y_0(b)=((2/3)theta tau, (1/3)c(b)),
  y_b=(y_0(b),y_0(b)).                                    (18)

Equation (16) gives

  <diag Delta,y_0(b)>=0.                                  (19)

The map b->y_b is the promised explicit linear map Phi.

### Exact full-fibre proof

If Y>=0 and B_U(Y)=y_b, equations (17)–(19) give <S,Y>=0. Hence Y=PYP. Put Z=FYF^T>=0; then Y=F^T ZF. Its first-basis diagonal equations give diag Z=theta tau and M_G(Z)=c(b). Conversely, every Z>=0 with M_G(Z)=c(b) has diag Z=theta tau because the raw coordinate measurements remain in G, and F^T ZF satisfies both lists in (18), since U F^T=F^T.

Therefore the FULL lifted fibre is

  {Y>=0:B_U(Y)=y_b}
   ={F^T ZF: Z>=0, M_G(Z)=c(b)}.                          (20)

Define

  D(Y)=D_0(FYF^T),          E(X)=F^T J(X)F,
  V=V_0 F.

Then VV^T=I_m, D is positive, E is positive, DE=id, and (14) and (20) prove (1). The identity B_U E=Phi A follows from the explicit target formulas for all symmetric X, not only PSD inputs. This proves the exact normal form with N=9m^2+4m+3+2p.

## 7. Global arbitrary-PSD residual control

Let Y>=0 be arbitrary, let delta=||B_U(Y)-y_b||_2, and put Z=FYF^T. The coefficient vector of S in the two lists is

  w=(diag Delta,diag Delta),       ||w||_2=sqrt(2(d+4M)).

By (19), w.y_b=0 for every b. Positivity and (17) yield the GLOBAL estimate

  tr(QYQ)<= (1/2)<S,Y>
           <=sqrt((d+4M)/2) delta.                        (21)

No small-noise assumption or target support information enters this bound.

Write r_1=diag Y-y_0(b), r_2=diag(U^T YU)-y_0(b). Reflection averaging cancels both P-Q cross blocks exactly:

  diag(F^T ZF)-y_0(b)
    =(r_1+r_2)/2-diag(QYQ).

Because QYQ>=0, its diagonal Euclidean norm is at most its trace. Thus

  ||diag(F^T ZF)-y_0(b)||_2
   <=(1+sqrt(d+4M))delta/sqrt(2).

Restrict to the last M coordinates, which equal (M_G(Z)-c(b))/3. Therefore

  ||M_G(Z)-c(b)||_2
   <=[3(1+sqrt(d+4M))/sqrt(2)] delta.                      (22)

Combining (15), epsilon^(-1)=2L, (10), and d+4M=33m^2+10m+9+8p proves (2) with the stated K.

This proof is valid for EVERY ambient PSD matrix of every rank. It does not project onto the exact fibre, assume a positive-definite lifted point, or invoke a local Schur-complement approximation.

## 8. Explicit certificates matching milestone 01

There is also a direct dual audit of the residual bound. For equation i let ell_i in R^N have zero first d coordinates and last M coordinates equal to 3 epsilon^(-1) times row i of R_0 P_raw. Then

  D*(A_i)=P diag(ell_i)P,
  ell_i.y_0(b)=b_i,
  B_U*((ell_i/2,ell_i/2))
       =D*(A_i)+Q diag(ell_i)Q.

Put beta_i=||ell_i||_infinity/2. Since S>=2Q, the two coefficient vectors

  lambda_(i,+)=(ell_i/2,ell_i/2)+beta_i w,
  lambda_(i,-)=-(ell_i/2,ell_i/2)+beta_i w

satisfy

  B_U*lambda_(i,+)-D*(A_i)>=0,    lambda_(i,+).y_b=b_i,
  B_U*lambda_(i,-)+D*(A_i)>=0,    lambda_(i,-).y_b=-b_i.

These are attained two-sided certificates on the FULL PSD cone, with explicit polynomial norms. They verify that the correction terms are supported on the first exposed exterior R=ran Q, exactly as required by the first-exposure invariant. This is not merely compressed operator inclusion.

## 9. Objective, positivity, and degenerate-data audit

For C_tilde=V^T C V, cyclicity of trace gives exact objective equality on all symmetric Y. Since VV^T=I, the Frobenius norm of C_tilde equals that of C.

For feasible nonzero b, every feasible X has tau=tr(HX)>0. The coordinate and block-copy targets are positive. For the source-equation vectors, write B=X-rho tau I/2. The bound ||B||<=sqrt(alpha)tau/2 gives

  tau(1+alpha||A_i||^2) +/-2<A_i,B>
  >=tau[1+alpha||A_i||^2-sqrt(alpha)||A_i||]
  >=(3/4)tau>0.

Completion columns are nonzero by (12), so their targets are positive. Consequently all entries of y_b are strictly positive even for singular, rank-one, or otherwise degenerate nonzero source solutions.

If b=0, trace control forces X=0; all target entries are zero and the first complete diagonal list forces Y=0. This case is included by the same formulas and the same residual inequality. If b is inconsistent with trace control or with the source equations, (1) proves that the lifted exact fibre is empty, without any presolve.

The lifted feasible set is compact whenever nonempty, because its first diagonal list fixes trace to (m rho+1+m^2 alpha)tau. Its positive image is therefore closed. No unsupported assertion that an arbitrary PSD cone image is closed is used.

## 10. Why the previous no-go theorems do not apply

The construction does have positive linear E,D with DE=id, but its full feasible fibre is (20), NOT E(F_b). Almost all auxiliary covariance and cross-block degrees of freedom remain free. For strictly feasible source data and a choice rho>||H^(-1)||, J(X_0) is positive definite on the entire inner d-dimensional space. That space has order d=Theta(m^2), only O(m^2+p) measured directions, and therefore Theta(m^4) invisible affine directions when p=O(m^2). This is precisely the large-slack alternative allowed by historical Milestone 09, not a contradiction of it.

The final N-dimensional fibre is singular, supported on ran F^T. Thus full-ambient two-MASA obstructions for principal or partial-trace decoders cannot be applied after pretending that compressed frames are MASAs. The decoder has a singular trace effect V^T V, so faithful-decoder assumptions also fail. Unlike the spectraplex-only template excluded by historical Milestones 62–64, this construction uses essential nontrivial copy and source-equation measurement constraints.

The proof is unified in m,p,rank and b. It does not classify input cases, select a proof route numerically, or assume a nonlinear witness-selection oracle. J is a single explicit positive linear forward map; completeness is proved directly for every source PSD point.

## 11. Verification and remaining reporting obligations

The mathematical identities in this manuscript prove the stated normal form. An exact rational symbolic check of the raw source-operator identity at m=2 with three independent test matrices, and numerical diagnostics at m=1,2,3,4 with zero, rank-one and full-rank source points, were run locally in audit_quadratic_quotient.py. They are diagnostics, not premises of the proof.

The precision/complexity and recovery-modulus supplement, full historical-obstruction audit, and reproducible scripts are separate companion files. No priority claim or external-referee certification is made. The optional stronger demands of nonzero basis overlaps, nonreflection U, a prescribed rank amplification, or equality of the entire ambient recovery modulus with the source modulus are NOT part of the theorem just proved.
