# Milestone 35 — An analytic firmly nonexpansive map with a circular last-step limit set

Date: 2026-11-14.
Parent research snapshot: 68cf4b1f2b4c211c2b95da9494b9d2843b200ba4.

## Status and exact scope

The requested Manuscript I strengthening was the last-step law for PLAIN Douglas–Rachford on EVERY weakly infeasible SDP:

    Z_k = V k^p + o(k^p)  =>  k^(1-p)(Z_(k+1)-Z_k) -> p V.

That all-order SDP statement is NOT proved or disproved here. The counterexample below is a semialgebraic, real-analytic, firmly nonexpansive resolvent on R^3. It rules out obtaining the conclusion from tameness, firm nonexpansiveness, a clean leading state term, or maximal monotonicity alone. It is NOT claimed to be Douglas–Rachford for an affine space and a PSD cone. Resolvent iteration can be viewed as splitting with a zero second operator, but that broader model must not be conflated with the specified conic-feasibility model.

Companion 36 proves the desired law for every weakly infeasible affine problem over ONE Lorentz cone, in arbitrary dimension, including all real order-two SDPs. Higher-order PSD cones and coupled products of Lorentz cones are not settled. The calculations here are self-contained and independent of earlier project results. Historical priority is not certified.

## 1. Explicit map and theorem

Let J=[[0,-1],[1,0]]. For t>0 and y in R^2 put R=||y||^2 and

    A(t,y)=(-(1+3R^2/4)/t^4, (R y+J y)/t^3),
    T=(I+A)^(-1).                                      (1)

**Theorem A.** T is single-valued on all R^3, real analytic, semialgebraic and firmly nonexpansive. It has no fixed point and has infimal displacement zero. From any initial z_0=(t_0,y_0),

    z_k=T^k z_0=5^(1/5) k^(1/5) e_0+o(k^(1/5)).        (2)

If y_0!=0, then

    Clust{k^(4/5)(z_(k+1)-z_k)}
       =5^(-4/5){(1,w): w in R^2, ||w||=1},             (3)

    k^(4/5)||z_(k+1)-z_k|| -> sqrt(2)5^(-4/5).          (4)

If y_0=0, the scaled last steps instead converge to 5^(-4/5)e_0. Thus even the scaled residual-norm coefficient is not fixed by the common leading state vector. All statements concern exact iterates.

## 2. Monotonicity, global existence and regularity

The symmetric part of DA has blocks

    S_tt=(4+3R^2)/t^5,
    B=S_yy=(R I+2yy^T)/t^3,
    b=S_yt=-(3R y+(3/2)J y)/t^4.

For y!=0, B has eigenvalues 3R/t^3 along y and R/t^3 along Jy. These two vectors are orthogonal and have squared norm R. Consequently

    b^T B^(-1)b=(3R^2+9/4)/t^5,
    S_tt-b^T B^(-1)b=7/(4t^5)>0.                       (5)

At y=0 the lower and cross blocks vanish and S_tt=4/t^5. Thus the symmetric Jacobian is PSD everywhere. Integrating along segments in the convex open domain proves monotonicity of A.

For input (u,v), an output (t,y) must obey

    u=t-(1+3R^2/4)/t^4,
    v=[(1+R/t^3)I+t^(-3)J]y.                           (6)

For each t>0 there is a unique R>=0 satisfying

    ||v||^2=R[(1+R/t^3)^2+t^(-6)].                      (7)

The right side increases strictly from zero to infinity. Its solution R(t) is continuous, bounded by ||v||^2, tends to zero at t=0, and tends to ||v||^2 at infinity. Thus t-u-(1+3R(t)^2/4)/t^4 changes from minus to plus infinity and has a root. The second equation then determines y. Strong monotonicity of I+A proves uniqueness.

For x=Tz and x'=Tz', monotonicity gives

    ||Tz-Tz'||^2 <= <Tz-Tz',z-z'>.                      (8)

This proves firm nonexpansiveness directly. Surjectivity of I+A also makes A maximal monotone by the resolvent criterion. The symmetric part of I+DA is at least I, so its Jacobian is nonsingular. The analytic inverse function theorem and uniqueness make T analytic on all R^3. Clearing the positive t denominators in (6) describes its graph by polynomial equalities and t>0, so it is semialgebraic.

A has strictly negative first component and therefore no zero. Outputs (t,0) have inputs (t-t^(-4),0), showing infimal displacement zero as t tends to infinity.

## 3. Exact iteration and the state scale

For k>=1 put z_k=(t_k,y_k), R_k=||y_k||^2; t_k>0. Equations (6) give

    t_(k+1)-t_k=(1+3R_(k+1)^2/4)/t_(k+1)^4,
    y_k=[(1+R_(k+1)/t_(k+1)^3)I+t_(k+1)^(-3)J]y_(k+1).
                                                               (9)

Let

    D_k=(1+R_(k+1)/t_(k+1)^3)^2+t_(k+1)^(-6).

Then R_k=D_k R_(k+1). Hence t_k increases, R_k decreases, and nonzero transverse vectors remain nonzero. A bounded t sequence would have increments bounded below, impossible. Thus t_k diverges, and t_k/t_(k+1) tends to one. The difference of fifth powers is bounded above and below by positive constants on a tail, proving t_k=Theta(k^(1/5)).

If R_k had positive limit, log D_k would be bounded below by a positive constant times t_(k+1)^(-3). Its sum diverges, contradicting R_k=R_1/product D_j. Thus R_k->0. Equation (9) now gives

    t_(k+1)^5-t_k^5 ->5,
    t_k~(5k)^(1/5).                                   (10)

## 4. Exact transverse amplitude

For y_0!=0 put B_k=1/R_k and t=t_(k+1). The exact reciprocal recurrence is

    B_(k+1)-B_k
       =[2/t^3+(R_(k+1)+B_(k+1))/t^6]/D_k.             (11)

First, B_k=O(t_k^2). For t>=2, D_k>=1 implies

    (1-t^(-6)) B_(k+1)
       <=B_k+2t^(-3)+R_(k+1)t^(-6).

The cumulative product of (1-t^(-6))^(-1) is bounded, since sum t_k^(-6)<infinity. Iteration and (10) give

    B_k=O(1+sum_(j<=k)t_j^(-3))=O(k^(2/5))=O(t_k^2).

The B/t^6 term in (11) is now O(t^(-4))=o(t^(-3)); the R/t^6 term is smaller, and D_k->1. Therefore

    B_(k+1)-B_k ~2/t_(k+1)^3.

Equation (9) also gives t_(k+1)^2-t_k^2~2/t_(k+1)^3. Stolz--Cesaro yields

    B_k/t_k^2 ->1,
    t_k||y_k|| ->1.                                   (12)

Thus the transverse state actually tends to zero, while creating a leading scaled step.

## 5. Infinite rotation and all cluster directions

Identify R^2 with C. For an unwrapped argument theta_k of y_k,

    theta_(k+1)-theta_k
       =-arctan[1/(t_(k+1)^3+R_(k+1))]
       ~-t_(k+1)^(-3).

Comparison with the t_k^2 increment gives theta_k/t_k^2->-1/2. Hence theta_k decreases to minus infinity with increments tending to zero. For any angle, choose the first crossing of that angle minus 2pi times a growing integer. The overshoot tends to zero. Thus y_k/||y_k|| has the whole unit circle as its cluster set.

Finally,

    t_(k+1)^4(t_(k+1)-t_k)->1,
    t_(k+1)^4(y_(k+1)-y_k)
       =-t_(k+1)[R_(k+1)I+J]y_(k+1)
       =-J[t_(k+1)y_(k+1)]+o(1).

Since t_(k+1)^4/k^(4/5)->5^(4/5), (3)--(4) follow. The axial case follows directly from (9). Equation (2) follows from (10) and y_k->0. QED.

## 6. A completely nonrotating discounted path

For anchor zero, J_(sA)(0)=(s^(1/5),0,0). The discounted fixed point of T, defined by q+t(q-Tq)=0, is exactly

    q(t)=(t/(1+t)^(4/5),0,0).                           (13)

Indeed Tq=((1+t)^(1/5),0,0) and q=tTq/(1+t). The curve predicts the correct state law but does not capture the rotating leading residual from a shrinking transverse perturbation. The failure is differentiating a state asymptotic, not the cosmic/state theorem.

## 7. A sufficient condition isolating the missing ingredient

For any nonexpansive T and orbit x_(k+1)=Tx_k, assume

    x_k=V k^p+o(k^p), V!=0, 0<p<1,

and that the unit step directions converge. Then necessarily

    k^(1-p)(x_(k+1)-x_k)->pV.                           (14)

To prove it, let r_k=||x_(k+1)-x_k||, a nonincreasing sequence. Its sum S_k diverges. Convergence of directions to u gives x_k/S_k->u, so u=V/||V|| and S_k~||V||k^p. For lambda>1, monotonicity bounds r_k by forward and backward secants of S. After rescaling, these limits are

    ||V||(lambda^p-1)/(lambda-1),
    ||V||(1-lambda^(-p))/(1-lambda^(-1)).

Let lambda decrease to one to obtain k^(1-p)r_k->p||V||. This proves (14).

Thus a cone-specific residual-direction theorem would close the step law once the state term is known. The example proves that firm nonexpansiveness and tameness alone do not supply that theorem.

## 8. What is and is not resolved

The cosmic/state results are not refuted. This is a sharp restriction on a proposed general last-iterate extension. No realization of this map as DRS for an affine space and S_+^m has been established. A is not asserted to be a convex-function subdifferential; its skew part is material. Companion 36 establishes the full single-Lorentz-cone theorem, including all order-two SDPs. Higher-order SDP last-step asymptotics remain unproved in this continuation.

Context: Liu--Ryu--Yin, *A New Use of Douglas--Rachford Splitting and ADMM for Identifying Infeasible, Unbounded, and Pathological Conic Programs*, arXiv:1706.02374. All new assertions here are proved above; no historical-priority or external-certification claim is made.
