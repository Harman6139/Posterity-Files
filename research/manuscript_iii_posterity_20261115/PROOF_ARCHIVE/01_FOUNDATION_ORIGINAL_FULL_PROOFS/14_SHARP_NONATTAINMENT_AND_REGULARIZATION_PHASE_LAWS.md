# Milestone 14 — sharp regularization laws for every SDP with finite optimum

Date: 2026-11-13. This turns the feasibility escape theorem of 12 into a theorem for GENERAL SEMIDEFINITE OPTIMIZATION. It treats exact source feasibility, finite but unattained optima, arbitrary minimum feasible faces, and every minimizer of the regularized problem. The sharp exponent envelope and exact leading asymptotics distinguish attainment from nonattainment. The one-scale normal form in 11 preserves the entire regularization value function exactly after its known trace normalization.

This is linear trace regularization, not a log-determinant barrier. A norm-power extension, including squared-norm regularization, is given in Section 8. No claim about solving the polynomial-time exact SDP feasibility problem is made.

## 1. Setup

Let

    F={X>=0:A(X)=b} be nonempty,
    v=inf_{X in F}<C,X> be finite.

No strict feasibility, dual feasibility, zero duality gap, or primal/dual attainment is assumed. Let E be the minimum support of F, r=dim E the maximum feasible rank. Compress to E by an orthogonal isometry when needed. There exists X0 in F positive definite on E, by averaging finitely many feasible matrices whose ranges span E.

For eta>0 define the minimum size of an EXACTLY FEASIBLE eta-optimal point by

    T(eta)=min{tr X:X in F, <C,X><=v+eta}.              (1)

The minimum is finite and attained by compactness of trace sublevels. Define, for lambda>0,

    V(lambda)=min_{X in F}[<C,X>-v+lambda tr X].        (2)

For every positive lambda this minimum is attained: the unregularized cost is bounded below by v and the trace penalty is coercive on the PSD cone.

## 2. The main theorem

### Attained optimum

If v is attained, let

    tau_star=min{tr X:X in F,<C,X>=v}.

Then every choice X_lambda of a minimizer in (2) satisfies

    tr X_lambda -> tau_star,
    V(lambda)/lambda -> tau_star,
    (<C,X_lambda>-v)/lambda -> 0.                     (3)

The matrices X_lambda are uniformly bounded as lambda decreases to zero, and every accumulation point is a trace-minimal source optimizer. If tau_star=0, the zero matrix is feasible and optimal, X_lambda=0 for all lambda, and V is identically zero.

### Unattained optimum

If v is not attained, necessarily r>=2. Put

    E_r=2^(r-1)-1.

There are p0>0 and a positive rational a such that

    T(eta) ~ p0 eta^(-a),
    1/E_r <= a <= E_r.                               (4)

For EVERY choice of regularized minimizers X_lambda, put

    eta_lambda=<C,X_lambda>-v,
    q_lambda=(a p0 lambda)^(1/(a+1)).

Then

    eta_lambda ~ q_lambda,
    tr X_lambda ~ p0 q_lambda^(-a),
    V(lambda) ~ [(a+1)/a] q_lambda.                   (5)

In particular the regularization value has a rational leading exponent theta with

    V(lambda) ~ c0 lambda^theta,
    2^(-(r-1)) <= theta <= 1-2^(-(r-1)),
    theta=1/(a+1).                                   (6)

BOTH endpoints of (4) and (6) are attained by explicit rational SDPs at every r>=2, with a strictly feasible source fibre in that order. The coefficients of the defining equality systems are bounded independently of r.

Thus for a fixed feasible support rank r there is a forbidden interval of value exponents between 1-2^(-(r-1)) and 1: a finite unattained optimum cannot have such a leading trace-regularization exponent. An attained optimum with positive trace-minimum has exponent exactly one; a zero optimizer gives V identically zero.

The theorem covers every nonempty finite-value SDP, including positive original duality gaps. It concerns primal objective values and exact primal feasibility; it does not silently assume that an ordinary dual optimum equals v.

## 3. Exact feasible repair with no exponent loss

The key step is to compare (1), which requires EXACT source equalities, with a weak-infeasibility profile. This comparison must be made AFTER restricting to the true minimum feasible face. It cannot in general be asserted in the original larger cone without that restriction.

Work on S^r so that X0>0, and retain the notation A,C. Define

    B(X)=(A(X),<C,X>),    d=(b,v).

If v is unattained, d belongs to closure B(S_+^r) but not to B(S_+^r): a sequence of exactly feasible near-optimizers proves the closure statement, and an exact preimage would attain the optimum. Hence this is a weakly infeasible order-r SDP.

Write

    R_d(delta)=min{tr Y:Y>=0,||B(Y)-d||<=delta}.

Immediately

    R_d(delta)<=T(delta).                             (7)

Choose a linear right inverse L of A on range A; put k_A=||L||, gamma=lambda_min(X0)>0, g0=<C,X0>-v>0. Such an inverse exists on the finite-dimensional range, and b-A(Y) always belongs to that range. Set

    M=1+||C||_F k_A+k_A g0/gamma >=1,
    B0=sqrt(r) k_A+k_A tr(X0)/gamma.

For any PSD Y with augmented residual <=delta, let

    Z=Y+L(b-A(Y)),
    s=k_A delta/(gamma+k_A delta),
    Zplus=(1-s)Z+s X0.

The matrix Z satisfies A(Z)=b and Z>=-k_A delta I. The choice of s makes Zplus>=0 and A(Zplus)=b. Its objective and trace obey

    0<=<C,Zplus>-v<=M delta,
    tr Zplus<=tr Y+B0 delta.                          (8)

The objective inequality follows because the equality correction changes cost by at most ||C|| k_A delta and the mixing changes it by at most (k_A delta/gamma)g0. The trace inequality uses |tr L(b-A(Y))|<=sqrt(r) k_A delta and s<=k_A delta/gamma. These bounds do not multiply the possibly huge trace of Y by an adverse factor; the coefficient of Y is at most one.

Taking a trace-minimizing Y yields

    R_d(eta)<=T(eta)
       <=R_d(eta/M)+(B0/M)eta.                        (9)

Therefore T and R_d have EXACTLY the same power exponent. Their leading coefficients need not be equal; no such claim is made.

By the order-r sharp envelope in 12, the exponent belongs to [1/E_r,E_r]. The graph of T is semialgebraic (the real constant v is permitted as a parameter), so T has an attained leading rational power. It diverges at zero: otherwise trace-compactness would produce an optimizer. This proves (4).

When r<=1, the problem is a linear program on a zero- or one-dimensional PSD ray; a nonempty closed feasible set with finite linear infimum attains it. Thus nonattainment indeed requires r>=2.

## 4. Exact scalar variational formula and all-minimizer asymptotics

For every lambda>0,

    V(lambda)=inf_(eta>0) [eta+lambda T(eta)].          (10)

For the lower inequality, an arbitrary X in F has eta=<C,X>-v and tr X>=T(eta), except at attained eta=0, which is handled by taking a limit. For the upper inequality, a minimizer defining T(eta) has cost gap at most eta. This proves (10); in the nonattained case every eta is strictly positive.

If X_lambda minimizes (2), then

    tr X_lambda=T(eta_lambda).

Otherwise a lower-trace feasible point with no larger cost would strictly improve the regularized objective. Thus eta_lambda minimizes the scalar expression in (10).

Suppose T(eta)~p0 eta^(-a). The elementary model minimization

    min_(eta>0) [eta+lambda p0 eta^(-a)]

has unique optimizer q_lambda=(a p0 lambda)^(1/(a+1)), at which the value is [(a+1)/a] q_lambda.

For completeness, the asymptotic replacement is uniform at actual optimizers. Evaluating at q_lambda gives V(lambda)=O(lambda^(1/(a+1))). Hence eta_lambda<=V(lambda) tends to zero and is O(lambda^(1/(a+1))). For small eta, T(eta)>=(p0/2)eta^(-a), so lambda T(eta_lambda)<=V(lambda) gives the reverse bound eta_lambda>=c lambda^(1/(a+1)). The rescaled optimizers eta_lambda/q_lambda therefore lie in a fixed compact subset of (0,infinity). On that set the relative asymptotic for T is uniform. The unique minimizer of the limiting scalar function forces eta_lambda/q_lambda->1, regardless of the choice among matrix minimizers. Substituting into T proves all three equivalences in (5).

No differentiation of a possibly nonsmooth value function, unique matrix optimizer, or continuity of a chosen optimizer selection is assumed.

## 5. Attainment proof and an intrinsic detection criterion

If the original optimum is attained, comparing any X_lambda with a trace-minimal optimizer gives

    0<=<C,X_lambda>-v,
    tr X_lambda<=tau_star,
    0<=V(lambda)<=lambda tau_star.

Thus all minimizers remain trace bounded. Along any lambda_n->0, every cluster point is feasible and optimal because its cost gap is at most lambda_n tau_star. Such a point has trace at least tau_star; consequently all selected traces converge to tau_star. The inequalities

    tr X_lambda<=V(lambda)/lambda<=tau_star

then prove (3), including the vanishing scaled cost gap.

Conversely, if some sequence lambda_n->0 has bounded regularized minimizers, the elementary fact V(lambda)->0 (compare against any fixed eta-optimal source point and then let eta->0) gives a feasible optimal cluster point. Therefore

    the source optimum is attained
      iff regularized minimizers stay bounded near zero
      iff lim_{lambda downarrow 0} V(lambda)/lambda is finite.
                                                               (11)

In the attained case that limit is tau_star; in the unattained case it is +infinity. Equation (11) is an asymptotic structural criterion, not a finite-precision decision algorithm. Semidefinite geometry strengthens it to the explicit sharp exponent gap (6).

## 6. Rational extremizers for both endpoints

Use coordinates 0,...,r-1.

### Fast near-optimal escape

Minimize X_00 subject to

    X_01=1,
    X_ii=X_(0,i+1),  1<=i<=r-2,
    X>=0.                                             (12)

The finite infimum is zero and is unattained, because PSD zero-row propagation would contradict X_01=1. For x=X_00>0, put a_i=X_0i. PSD gives

    a_1=1,
    a_(i+1)>=a_i^2/x,
    X_(r-1,r-1)>=a_(r-1)^2/x.

Thus tr X>=x^(-E_r). For x=eta a rank-one matrix simultaneously attains these inequalities, with

    X_ii=eta^(-(2^i-1)), 1<=i<=r-1.

Its trace is eta+sum_i eta^(-(2^i-1)). Hence

    T(eta) ~ eta^(-E_r),  p0=1,
    theta=1/(E_r+1)=2^(-(r-1)).                       (13)

The fibre is strictly feasible. For example take an arrow matrix with X_00=s>0, X_01=1, choose each next cross a_(i+1) larger than a_i^2/h for h=s/r, set the corresponding diagonal equal to a_(i+1), and choose the final diagonal large enough. Each term of the top Schur sum is then below h, so the matrix is positive definite while preserving all equations. Thus its maximum feasible support has order r.

### Slow near-optimal escape

Minimize Z_(r-1,r-1) over arrow matrices with leaf offdiagonals zero, subject to

    Z_01=-1/2,
    2 Z_(0,j)+Z_(j-1,j-1)=0, 2<=j<=r-1,
    Z>=0.                                             (14)

The infimum is zero and is unattained by backward zero-row propagation. For t>0 take leaf diagonals d_j=t^(2^j-1),

    Z_00=(r-1)/(4t), Z_01=-1/2,
    Z_0j=-d_(j-1)/2 for j>=2.

Each term in the top Schur sum equals 1/(4t), so Z(t)>=0 exactly. Its cost is eta=t^E_r and trace is Theta(1/t). This gives T(eta)=O(eta^(-1/E_r)); (4) supplies the matching lower bound. Hence

    a=1/E_r,
    theta=E_r/(E_r+1)=1-2^(-(r-1)).                   (15)

Adding any fixed positive number to Z_00 makes this matrix positive definite without changing the source equations or the objective. Again the full feasible support has order r.

For r=2 the two endpoints coincide. In (12), T(eta)=eta+1/eta for eta<=1. The regularized problem can be solved exactly:

    V(lambda)=2 sqrt(lambda(1+lambda)),
    X_00=sqrt(lambda/(1+lambda)),
    X_11=sqrt((1+lambda)/lambda).

This confirms the constants p0=1,a=1 and V(lambda)~2 sqrt(lambda) without any numerical approximation.

## 7. A pointwise primal-certificate consequence

In the minimum-face coordinates, use the augmented map B from Section 3 and target d=(b,v). Define

    Q_d(epsilon)=min{||y||:d.y=-1, B*y+epsilon I_r>=0}.

Milestone 12 gives a reciprocal exponent beta=1/a for this normalized approximate Farkas-certificate profile. The same a is the EXACT feasible near-optimal escape exponent by (9). Thus the regularization exponent can also be written

    theta=beta/(beta+1).                              (16)

These certificates concern infeasibility of attaining the optimum in the minimal face. They are not being confused with ordinary optimal dual multipliers of the original optimization problem. Original duality gaps and original dual nonattainment are not assumed away.

## 8. Positive-definite weights and norm-power regularization

The theorem is not tied to the identity trace weight. If the regularizer is <P,X> with P positive definite, the congruence X=P^(-1/2) Z P^(-1/2) changes it into tr Z without altering feasible support rank. All statements hold with the corresponding weighted size profile and leading coefficient.

More generally, let w be any semialgebraic norm on the source matrix space, restricted to PSD matrices. On the finite-dimensional minimum face it is comparable with trace. Therefore

    T_w(eta)=min{w(X):X in F,<C,X><=v+eta}

has the same power exponent a as T, though generally a different leading coefficient p_w. For any fixed real q>0 for which the penalty is being considered, the scalar minimization argument yields, when T_w(eta)~p_w eta^(-a),

    eta_lambda ~ (q a p_w^q lambda)^(1/(q a+1)),
    w(X_lambda) ~ p_w eta_lambda^(-a),
    min_F[<C,X>-v+lambda w(X)^q]
           ~ [(qa+1)/(qa)] eta_lambda.                (17)

For q>=1 this is a convex norm-power regularization; q=2 includes squared-Frobenius regularization. The sharp value-exponent interval is

    1/(1+q E_r) <= theta_q <= E_r/(E_r+q).             (18)

Both endpoints are attained by the same rational families because norm equivalence preserves the source escape exponent. Equation (17) concerns global minimizers; no algorithmic convergence guarantee or strong convexity at the unregularized boundary is inferred.

If the original optimum is attained, the analogous norm-power value is lambda times the minimum w(X)^q among original optimizers, plus o(lambda), with the same compactness proof. A zero norm-minimal optimizer gives the identically zero gap.

## 9. Exact preservation by the rational two-basis one-scale normal form

Milestone 11 supplies a completely positive decoder D and an exact lifted fibre T_b^lift such that

    D(T_b^lift)=F,
    tr Y=c tr D(Y) for every Y in T_b^lift,
    <D*C,Y>=<C,D(Y)>.

Every source point has a lifted preimage. Therefore for EVERY lambda>0,

    min_{Y in T_b^lift}
       [<D*C,Y>-v+(lambda/c)tr Y]
       = V(lambda).                                  (19)

Likewise the minimum normalized lifted trace at exact source cost gap <=eta equals T(eta), not merely an equivalent power profile. Thus all leading constants, regularization values, attainment status and trace/cost asymptotics in (3)–(6) persist EXACTLY after the known normalization. The quadratic increase in matrix order does not weaken these source-dependent exponents.

This gives a concrete operational consequence of the normal form: two rational basis lists with one common free scale contain the full nonattainment and regularization behavior of arbitrary rational SDPs, including the sharp endpoint families.

## 10. Source dependencies and scope

The dimension-only escape envelope is the theorem in 12_RECIPROCAL_ESCAPE_LAW_AND_SHARP_DIMENSIONAL_BOUNDS.md (proof commit 2e2f8f75c99f49e4b6e51fad2a37b41891928901). The exact-feasible repair in Section 3 is proved here rather than presumed from an approximate feasibility estimate. The exact two-basis trace/objective identities are from 11_OPTIMAL_ONE_SCALE_UNRESTRICTED_UNIVERSALITY.md (proof commit cd97bc32a1febc3f37ad3803c7cd582d140cf04d).

Regularization of singular SDPs has substantial prior literature. A directly relevant primary work is T. Tsuchiya, B. F. Lourenco, M. Muramatsu and T. Okuno, A limiting analysis on regularization of singular SDP and its implication to infeasible interior-point algorithms, Mathematical Programming 200 (2023), 531–568, DOI 10.1007/s10107-022-01891-8. Its two-sided perturbations and limiting duality-gap analysis are not being claimed as new or as resolved by the one-sided rate theorem here. Primary article: https://link.springer.com/article/10.1007/s10107-022-01891-8 .

The support-function, compactness, semialgebraic growth, and scalar regular-variation principles used here are classical. The sharp all-support-rank envelope, exact repair, leading all-minimizer formulas, and exact normal-form transfer are supported by the displayed proofs. Priority of the complete synthesis and independent referee certification are not asserted.

The value v and minimum face E are analytic objects in the theorem; no polynomial-time method to find them is claimed. The asymptotic criteria do not yield a finite-precision attainment decision algorithm. No uniform bound on the instance-dependent leading coefficient p0, on the relative-interior eigenvalue gamma, or on the threshold where an asymptotic estimate is valid is assumed.
