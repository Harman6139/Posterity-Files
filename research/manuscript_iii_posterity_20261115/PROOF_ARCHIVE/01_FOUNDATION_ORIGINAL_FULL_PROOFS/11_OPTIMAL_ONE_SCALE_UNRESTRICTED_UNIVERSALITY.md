# Milestone 11 — unrestricted rational SDP universality: two bases and one free scale

Date: 2026-11-13. Uses the entirely rational construction in 10. There are NO trace-control, boundedness, strict-feasibility, feasibility-gap, or supplied-certificate hypotheses on the original input.

## 1. The necessary change of model

A fixed complete basis diagonal fixes the trace of a PSD matrix. Its PSD fibre is compact. Therefore no continuous decoder of a finite fixed-data two-basis fibre can have an unbounded feasible set as its image. Also the complete two-basis PSD measurement cone is closed, so a fixed-data two-basis system cannot be weakly infeasible.

Thus a literal extension to arbitrary SDPs with TWO FIXED DIAGONAL LISTS is impossible at ANY order. This corrects the earlier research suggestion that trace control could simply be deleted without changing that model.

The minimal repair is to let the two observation lists vary jointly on ONE prescribed affine line. The theorem below proves that this one scalar is sufficient, while Section 8 proves that zero free scalars are insufficient and that one basis is insufficient for datum-uniform positive decoding. Optimality here concerns these two discrete resources, NOT a claim that the matrix-order constant or the quadratic order is optimal under all positive decoders.

## 2. Main theorem

Let A:S^m->R^p be ANY rational linear map, m>=1,p>=0, and let C be any rational symmetric cost. There is a deterministic polynomial-bit construction, from A alone, of:

    N=9m^2+4m+5+2p,
    U in O(N) with every entry rational,
    W in Q^(2N x p), v in Q^(2N) with v_j>0,
    rational linear completely positive maps E,D,
    positive rational scalars c and f,

such that the following hold. The source datum b and cost C are not needed to construct U,E,D,W,v.

(a) D(Y)=VYV^T, VV^T=I_m; the coefficients of D are rational. E is completely positive and

    D E=id,
    B_U E(X)=W A(X)+v tr X,
    tr E(X)=c tr X,
    W^T W=f^2 I_p,
    1<=c<=10m^5.                                      (1)

(b) Define the one-scale two-basis fibre

    T_b={Y>=0: exists t in R, B_U(Y)=Wb+t v}.            (2)

Then for every b, including infeasible data,

    D(T_b)={X>=0:A(X)=b}=:F_b.                          (3)

For every exact Y in T_b the scalar is unique, nonnegative, and satisfies

    t=trY/c=trD(Y).                                    (4)

No extra measurement is used: these are exactly two complete real ONB lists, whose allowed data have one common free scale. Equivalently the free scalar is eliminated by the known trace of Y.

(c) Put

    h=(1_(2N))/(2c), Q_data=I_(2N)-v h^T,
    W_hat=W/f,
    M(Y)=[B_U(Y)-v trY/c]/f.                            (5)

Then Q_data^2=Q_data, h^T v=1, h^T W=0, W_hat^T W_hat=I_p, and T_b={Y>=0:M(Y)=W_hat b}. In particular M is an explicit RATIONAL linear measurement map, obtained by centering the two complete diagonal lists.

There is an explicit polynomial constant K, given below, such that for EVERY Y>=0 and every b,

    sqrt(||A(D(Y))-b||^2+|trD(Y)-trY/c|^2)
       <=K ||M(Y)-W_hat b||.                            (6)

The forward residual is EXACTLY isometric:

    ||M(E(X))-W_hat b||=||A(X)-b||                     (7)

for every symmetric X.

(d) Every source objective has the rational pullback D*C, with identical spectrum up to extra zeros, identical Frobenius/operator norms, and exact ambient objective identity. All primal objective-value sets, extended-real infima, and finite primal attainment are preserved. The two standard Lagrange duals have exactly the same attainable objective-value sets, extended-real suprema, and finite-attainment status. Explicit multiplier transformations are in Section 6.

(e) Feasible, weakly infeasible, and strongly infeasible data are preserved exactly, as are nonclosedness at specified source data, unbounded feasible sets, recession cones under D, and growth of the minimum trace needed for approximate feasibility. These statements require no source conditioning promise.

(f) E and D admit full-matrix CP extensions, and the exact-fibre and residual statements amplify to arbitrary ancillary order with the SAME constant K. At ancillary order n the observations are two lists of n-by-n blocks and the free scale is one n-by-n matrix, not one scalar on the whole Nn-dimensional space. No incorrect scalar-measurement claim is made at n>1.

The output has rational, not merely algebraic, coefficients of polynomial bit length. This is a polynomial-time normal-form reduction, NOT a polynomial-time algorithm deciding feasibility.

## 3. Construction and exact proof

Append the trace to the source measurements:

    Aplus(X)=(A(X),trX), q=p+1.

This augmented operator has the KNOWN certificate H=I_m, with z selecting its last row. Apply 10 with

    rho=2m, alpha=4m^3.

This costs no optimization, certificate search, positive-cone margin, eigenvalue separation promise, or branching on feasibility. Write its data map as

    Phi_plus(b,t)=Wb+t v.

Its order is N=9m^2+4m+3+2q, giving the claimed formula. Its exact fibre theorem holds for every pair (b,t). Taking the union over t proves (3).

The trace identity from 10 is

    tr E(X)=c trX,
    c=2m^2+(s_a^2+alpha tr(S_qblock^2))/s_l^2.           (8)

Here I<=S<=5I/4, and 1<=s_l<=5/4. Consequently

    c<=2m^2+(25/16)(1+4m^5)<10m^5.

Also c>=1 because D is trace nonincreasing on PSD matrices and DE=id. Each half of Phi_plus(b,t) sums to ct. The W columns sum to zero in each half. Therefore exact data force t=trY/c. Exact augmented-source soundness also forces trD(Y)=t, proving (4).

Let eta=4 sigma^2/s_l^2 and beta=3/5 as in 10. An original b_i enters just its two +/- raw equation outcomes, with coefficients +/-2 beta^2 eta, repeated in the two bases. The supports for different i are disjoint. Thus

    f=4 beta^2 eta,
    W^T W=f^2 I_p.                                    (9)

The last augmented datum t enters other places too, but is a separate column v. The scale vector v is strictly positive even when (0,1) is not feasible source data. For an original equation its unscaled entries at (0,1) are

    1+alpha||A_i||^2 +/- rho tr(A_i),

both at least 3/4 by |trA_i|<=sqrt(m)||A_i|| and alpha=m rho^2. For the added trace equation they are

    1+alpha m +/- (2-rho m),

which are positive for every m>=1. All other targets in this column are manifestly positive coordinate/copy/completion values. This establishes v_j>0 without a source feasibility hypothesis.

Since h^T B_U(Y)=trY/c, (5) follows. Tensoring and composing the data identities gives

    M E=W_hat A.

Equation (7) follows from W_hat^T W_hat=I. For any PSD Y choose t=trY/c in the global estimate (14) of 10 for Aplus. The raw two-basis residual is f times the residual in (5), so the entire augmented source residual is bounded by

    K=4 C_R(1/sqrt(2)+kappa),                            (10)
    C_R=sqrt(9(S_A+m)/16+(p+1)/8),
    d=(m+1)^2, M=8m^2+2m+4+2p,
    kappa=sqrt(2[d(3/5)^4+M(4/5)^4])/(2(7/25)).

One may replace K by max(1,K). This is polynomial in m,p and source coefficient magnitudes. Notably the inverse small raw measurement scale cancels out of (10). This proves (6) globally.

For the physical distance to the target LINE, rather than the trace-centered norm, define

    delta_line(Y)=inf_t ||B_U(Y)-Wb-tv||.

Equation (14) of 10 gives ||A(D(Y))-b||<=K_raw delta_line(Y). Moreover the centered physical residual is between delta_line and (1+sqrt(N))delta_line: apply Q_data to a minimizing residual and use ||v||<=sqrt(2)c, ||h||=sqrt(2N)/(2c). Thus either convention gives polynomially comparable residuals. They are not silently declared equal.

## 4. Exact preservation of all feasibility regimes

Set

    r_src(b)=inf_(X>=0)||A(X)-b||,
    r_lift(b)=inf_(Y>=0)||M(Y)-W_hat b||.

Equations (6)–(7) imply

    r_src(b)/K<=r_lift(b)<=r_src(b).                    (11)

For finite residual budgets, the stronger set inclusions hold:

    {X>=0:||A(X)-b||<=delta}
       subset D({Y>=0:||M(Y)-W_hat b||<=delta})
       subset {X>=0:||A(X)-b||<=K delta}.               (12)

Exact feasibility is equivalent by (3). Thus an infeasible datum has zero residual infimum on one side exactly when it does on the other. This is weak infeasibility. A positive residual infimum on one side is equivalent to a positive residual infimum on the other. This is strong infeasibility. No closure of arbitrary PSD linear images is presumed.

For every exact lift, (4) gives

    trY=c trD(Y).                                      (13)

Hence D:T_b->F_b is a proper surjection: preimages of compact source subsets are closed and trace-bounded PSD sets, thus compact. In particular F_b is bounded if and only if T_b is bounded. If F_b is nonempty, their recession cones satisfy

    rec(F_b)={X>=0:A(X)=0},
    rec(T_b)={Y>=0:M(Y)=0},
    D(rec T_b)=rec F_b.                                (14)

The homogeneous exact fibre has no nonzero PSD direction annihilated by D, since (13) would force its trace to vanish. There can still be large bounded decoder-invisible affine fibres; (14) does not reintroduce bijectivity.

## 5. Minimum trace and weak-infeasibility escape rates

Define, with inf empty = +infinity,

    R_b(delta)=inf{trX:X>=0,||A(X)-b||<=delta},
    Rtilde_b(delta)=inf{trY/c:Y>=0,||M(Y)-W_hat b||<=delta}.

The forward section and the trace component of (6) give

    R_b(K delta)-K delta<=Rtilde_b(delta)<=R_b(delta).   (15)

For weakly infeasible data, R_b(delta) tends to infinity as delta decreases to zero. Otherwise a trace-bounded sequence of approximate PSD solutions has a convergent subsequence yielding an exact source solution. Thus (15) preserves the escape to infinity, and any two-sided power growth R_b(delta) asymp delta^(-a) transfers with the SAME exponent a. This is a statement about source and lifted approximation resources, not an unconditional feasibility algorithm.

An explicit family with exponentially large exponents is given in Section 10.

## 6. The standard dual, not just primal objective values

The source primal is inf <C,X> over F_b and its usual dual is

    sup{b.lambda:C-A*lambda>=0}.                        (16)

The centered lifted dual is

    sup{(W_hat b).gamma:D*C-M*gamma>=0}.                (17)

For ANY feasible gamma in (17), positivity of E* and DE=id give

    E*(D*C-M*gamma)=C-A*(W_hat^T gamma)>=0.

Thus lambda=W_hat^T gamma is source-dual feasible, with EXACTLY the same objective and ||lambda||<=||gamma||.

Conversely let lambda be source-dual feasible. In the augmented construction use (lambda,0), giving ell supported on the raw frame entries as in Section 7 of 10. Write w=(diag Delta,diag Delta), g=7/25, and

    gamma0=(ell/2,ell/2)-[||ell||_infinity/(2g)]w.

Then

    D*C-B_U*gamma0
      =D*(C-A*lambda)-Qout diag(ell)Qout
          +[||ell||_infinity/(2g)]S0>=0.

The target identities for EVERY (b,t) imply W^T gamma0=lambda and v^T gamma0=0. Therefore gamma=f gamma0 is feasible in (17), since

    M*gamma=B_U*gamma0,
    W_hat^T gamma=lambda.

Furthermore

    ||gamma||<=4 C_R(1/sqrt(2)+kappa)||lambda||=K||lambda||. (18)

This proves equality of the entire dual objective-value sets and both finite-attainment statuses, including when strict feasibility fails. Primal value sets coincide by (3) and the exact objective pullback. Hence infeasible duals, unbounded objectives, unattained optima, and primal-dual gaps are preserved rather than regularized away.

## 7. Facial structure for nonempty source fibres

Let E_b be the maximum source support and let r_b=dim E_b. If F_b contains a nonzero point, choose a maximum-rank point X_*. Such a point exists by taking a finite average of feasible matrices whose ranges span all feasible ranges; compactness is not needed.

For rho=2m, the complement rho trX I-X is positive definite whenever X>=0 is nonzero. The arrow is strictly positive as in 10. The compensating rational congruence is invertible and acts identically on the source block. Thus, in canonical coordinates,

    Jhat(X)=X direct-sum Khat(X), Khat(X)>0 for X!=0.

Positivity of the decoder shows that every lifted feasible matrix annihilates the source directions orthogonal to E_b. The encoder of X_* is positive definite on the remaining inner support. Therefore the minimum lifted support is exactly

    F^T(V0^T E_b direct-sum ker V0),

and its dimension is

    r_b+d-m=r_b+m^2+m+1.                               (19)

The same formula with r_b=rank X is the maximum preimage rank of each nonzero feasible X; the explicit encoder attains it.

For completeness, the facial-depth argument also survives freeing trace. On the inner space let M_in be the restriction of the centered observations to matrices F^T ZF. Then M_in Jhat=W_hat A, so Jhat*(range M_in*) is contained in range A*. The explicit extraction coefficients for (lambda,0) give the converse inclusion through D0*: D0*(range A*) is measured by M_in.

An inner facial certificate positive on a support E_i direct-sum ker V0 and annihilating Jhat(X_*) must kill the entire auxiliary block, since Khat(X_*)>0 there. Its source block is in range A*, by pulling back through Jhat; it performs exactly a valid source step. Conversely each source certificate lifts by D0*. Hence the inner singularity degree equals the source degree k.

The outer signed stress is still a centered measured zero stress because w.v=0 and w.Wb=0. A symmetric first/second-list average of any inner certificate is block diagonal across P and Qout. Adding a sufficiently large multiple of S0 makes its exterior block strictly positive, so outer exposure can be merged with the first nontrivial source step. Conversely intersecting any ambient facial chain with ran P gives an inner chain no longer than it: positivity equates the restricted zero-quadratic-form sets with the restricted kernels. Thus

    k_lift=max(1,k).                                   (20)

If F_b={0}, necessarily b=0 and T_b={0} by (13). Both homogeneous systems have a one-step positive definite measured stress: separate zero from the compact image of the trace-one PSD base. Hence both depths are one in this exceptional case.

No claim of a global ambient distance modulus for unbounded fibres is inferred from (20). The global guarantees here are the residual and trace-profile statements (6),(15).

## 8. Exact necessity of the two discrete resources

### Zero free scales are insufficient, at any dimension

For a complete fixed first diagonal a, the PSD set {Y>=0:diag Y=a} is closed and trace-bounded. It is therefore compact (or empty). Every continuous image of it is compact. The unbounded scalar source {x>=0}, already an SDP, cannot be such an image. This excludes any number of fixed complete basis lists, arbitrary finite dimensions, and arbitrary continuous decoders for unrestricted entire-fibre universality.

Moreover C_U=B_U(S_+^N) is closed: convergence of its data bounds trY through the first diagonal; a PSD subsequence converges. Thus any infeasible fixed-data two-basis system has strictly positive distance to C_U and is strongly, not weakly, infeasible. A two-sided residual-preserving reduction of arbitrary weakly infeasible SDPs into this fixed-data model is impossible.

### One basis is insufficient for a uniform positive decoder

Fix m>=2 and the full-tomography source operator A=id on S^m. Suppose a finite single-basis model with a fixed globally positive LINEAR decoder D represented every source datum X>=0, so each corresponding feasible fibre had decoded image {X}. Allow arbitrary target functions and any number of free scalar data parameters; the only physical constraints on the PSD matrix must depend on that one basis diagonal.

Choose a lift Y_X. Dephasing Y_X in that basis preserves PSD, every basis observation and the same free parameters. Thus it is still feasible and must also decode to X. Therefore

    X=sum_j (Y_X)_(jj) D(e_j e_j^T)

for every PSD X. This would make the entire PSD cone a finitely generated cone of PSD matrices. Impossible: each rank-one ray uu^T in such a sum requires a nonzero generator supported on span u, and there are infinitely many different projective directions u but only finitely many generators.

This lower bound allows arbitrary positive, not necessarily CP, decoders and arbitrarily large auxiliary PSD dimension. It requires the decoder to be fixed across source data for the fixed operator A, as in our uniform theorem. It does not exclude datum-specific decoders that simply hardcode a source solution or decoders outside the stated positive-linear model.

Consequently TWO bases and ONE common free scale are necessary and sufficient in this precisely defined uniform representation model.

## 9. Universal nonclosedness inside a one-dimensional quotient of a closed two-basis cone

Let C_U=B_U(S_+^N), a closed convex cone. Equations (2)–(3) give

    A(S_+^m)={b:Wb in C_U+span(v)}.                    (21)

The global residual bounds also give the closure identity

    closure A(S_+^m)={b:Wb in closure(C_U+span(v))}.     (22)

For the nontrivial direction of (22), approximate Wb by B_U(Y_j)+s_j v and use the augmented residual bound at (b,-s_j) to obtain A(D(Y_j))->b. This avoids assuming that closure commutes with restriction to the subspace range W.

Furthermore

    v in C_U <=> exists 0!=X>=0 with A(X)=0.             (23)

When (23) holds, the tangent cone of C_U at v is

    T_(C_U)(v)=closure(C_U+span(v)).                    (24)

Indeed for a cone containing v, cone(C_U-v)=C_U+span(v), and the tangent cone is its closure. Thus b is weakly infeasible exactly when

    Wb in T_(C_U)(v) but Wb not in C_U+span(v).          (25)

The scale direction v has all coordinates STRICTLY POSITIVE. Hence arbitrary weak-infeasibility geometry is realized at positive two-basis observation data, through one missing scale direction, not through zero observed coordinates.

For an arbitrary A one can force (23), without changing its cone image, by replacing A on S^m by Xtilde -> A(Xtilde_top) on S^(m+1). The extra coordinate is an unmeasured PSD recession direction. This gives an all-input realization of every PSD linear image as the indicated section of a radial cone at a positive-data point of a closed two-basis cone, at order 9(m+1)^2+4(m+1)+5+2p. This geometric corollary is distinct from a polynomial-time algorithm for closedness or tangent membership.

## 10. A sharp all-order weak-infeasibility family

For every m>=2, index source coordinates 0,...,m-1 and impose

    X_00=0, X_01=1,
    X_ii-X_(0,i+1)=0, 1<=i<=m-2.                      (26)

There are p=m rational equations of bounded coefficient size. Exact PSD feasibility is impossible because X_00=0 forces row 0 to vanish.

For epsilon>0 put a_i=epsilon^{-(2^{i-1}-1)} for 1<=i<=m-1, and define the rank-one PSD matrix from the vector

    u_0=sqrt(epsilon), u_i=a_i/sqrt(epsilon).

Its entries are rational functions of epsilon despite the displayed Gram factor. It has X_00=epsilon, X_01=1 and X_ii=X_(0,i+1) exactly. Its residual norm is epsilon, and

    trX=epsilon+sum_(i=1)^(m-1) epsilon^{-(2^i-1)}.

Thus the source is weakly infeasible and its minimum-trace profile satisfies the upper bound O_m(epsilon^{-(2^{m-1}-1)}).

For the matching lower bound, any PSD approximate solution of residual <=delta<=1/4 has x=X_00<=delta and a_1=X_01>=1/2. Its x must be positive. The principal 2x2 minors and the chain equations give

    a_(i+1)>=a_i^2/delta-delta.

Inductively a_i>=1/2, so the right side is at least a_i^2/(2delta). Therefore

    a_i>=2^{-(2^i-1)} delta^{-(2^{i-1}-1)},
    X_(m-1,m-1)>=2^{-(2^m-2)}delta^{-(2^{m-1}-1)}.

Hence the exact exponent is

    R_b(delta) asymp_m delta^{-(2^{m-1}-1)}.            (27)

By (15), the rational two-basis one-scale normal form, of order

    N=9m^2+6m+5,

has the SAME minimum-scale escape exponent. At the inverse-polynomial centered residual delta=1/(16K), every approximate lifted point satisfies

    trY/c >= 2^{2^m-2}-1/16.                            (28)

Thus the restricted observation model contains weakly infeasible instances requiring doubly exponential trace already at inverse-polynomial residual precision. This is an explicit consequence of the reduction, not a new claim that large-solution phenomena were previously unknown.

## 11. A dimension-uniform operational CP consequence

The rational encoder has tr E(X)=c trX for all matrices and is CP. Therefore Qenc=E/c is a trace-preserving quantum channel (using its real Kraus extension, also a complex CP channel). The decoder D is CP and trace nonincreasing, since V^*V is a projection. On encoded states,

    D(Qenc(rho))=rho/c.                                (29)

It is a heralded exact recovery branch with state-independent success probability 1/c>=1/(10m^5), including inputs entangled with an untouched ancilla. Failure can be sent to a flag by the complementary positive effect I-V^*V. This is NOT deterministic recovery or a claim that merely listing the two classical probability histograms reconstructs an unknown quantum state. It is an operational realization of the positive section with explicit polynomial success probability.

## 12. Complexity, interpretation, and antecedents

Every operation in 10 is rational matrix arithmetic of polynomial dimension. Here the trace certificate is H=I supplied by augmentation, so the construction is unconditionally polynomial-bit in the original rational source input. The resulting centered model is itself a rational SDP; conversely its affine-line formulation is immediately an ordinary SDP with one free scalar. Thus exact rational SDP feasibility is polynomial-time reducible to this restricted two-rational-basis one-scale class, and conversely. This is completeness for exact SDP feasibility under polynomial reductions, not NP-hardness, membership in P, or a resolution of the exact SDP complexity problem.

The elementary trace-augmentation step alone does not supply the main arithmetic improvement: the rational Cayley-frame compensation in 10 is what avoids algebraic coefficients while retaining exact positivity and all-PSD residual control. The minimal-scale lower bound and the dephasing lower bound explain the precise representation frontier. The weak-infeasibility and dual results prevent the reduction from hiding difficult cases through a compactification that changes their status.

Related existing research, used for context rather than as premises of these proofs: G. Pataki, Characterizing Bad Semidefinite Programs: Normal Forms and Short Proofs, SIAM Review 61 (2019), DOI 10.1137/17M1140844, arXiv:1709.02423; M. Liu and G. Pataki, Exact Duals and Short Certificates of Infeasibility and Weak Infeasibility in Conic Linear Programming, arXiv:1507.00290; G. Pataki and A. Touzov, How Do Exponential Size Solutions Arise in Semidefinite Programming?, SIAM Journal on Optimization (2024), DOI 10.1137/21M1434945, arXiv:2103.00041. Homogenization, bad projections, and repeated-squaring large-solution phenomena are not claimed as new here. No generalist-journal reception, independent referee certification, or comprehensive priority claim follows merely from this proof.
