# Checkpoint 009: observability, strict dual certificates, and every rational direction

Date: 2026-11-15. This extends the core arithmetic facial theorem. Proofs below are analytic; historical priority of the convex observability identities is not claimed (they are separation/minimax consequences).

## 1. Exact test for an individual perturbation direction

Let P be a finite union of closed rational polyhedral cones, A rational, and D nonzero rational. Apply arithmetic facial reduction to the rational affine line H_D=A+R D. If it returns EMPTY, D cannot be a robust rationalization direction. Otherwise define

 I_D={t in R:A+tD belongs C(P_{*,D})}.

This is a closed interval. Then A+tD admits rational permitted Gram columns for every sufficiently small positive rational t if and only if 0 belongs I_D and I_D contains a positive point. Necessity follows from the closure identity. For sufficiency, every rational t in the interior of I_D is an actual rational factor point: the feasible rational parameter set is dense in I_D and is convex under rational convex combinations; bracket t by two rational feasible parameters and interpolate with rational coefficients. Hence all sufficiently small positive rational t work. For D=0, the criterion is exact rational factorability of A. This decides membership in the full requested robust-direction set, not only its nonemptiness. Nonemptiness for D in a given rational subspace E is equivalent to A lying in the terminal slice for H=A+E.

## 2. An exact observation condition

Let C=C(P) be nonzero and L a rational linear observation map. Define

 beta(P,L)=min{||L(X)||_2:X in C, tr(X)=1}.

The trace-one base is compact. The following are equivalent:
(a) beta>0;
(b) ker(L) intersect C={0};
(c) there is y with L*(y)[x]>0 for every nonzero x in P;
(d) there is a finite kappa with tr(X)<=kappa||L(X)|| for all X in C.

The best kappa is 1/beta. The exact dual formula is

 beta=max_{||y||_2<=1} min_{x in P,||x||_2=1} x^T L*(y)x.

Proof: set B=L({X in C:tr X=1}). This is compact and convex. If its closest point to zero is z!=0, y=z/||z|| satisfies <y,b> >= ||z||=beta for every b in B. The opposite inequality is Cauchy-Schwarz at z. If z=0, the maximum is zero, attained at y=0. The minimum of a linear functional on the Gram base is its minimum on normalized atoms. Homogeneity proves (a)--(d) and sharpness of kappa. Under these conditions L(C) is closed, because bounded observations give bounded trace and hence bounded PSD lifts.

This condition is stronger than closedness of L(C), and is not to be conflated with it.

## 3. Necessary correction to the proposed strict-margin Farkas alternative

Take P=R_+^2, L(X)=X_11 and b=-1. This is strongly infeasible, but any observation-compatible separator is L*(y)=diag(y,0), so it has zero margin on e_2. No separator with strictly positive cone margin exists. Thus the grand handoff's unconditional positive-margin alternative fails even without weak infeasibility.

If beta>0 and ||b||<=1, let delta=dist(b,L(C))>0. Conic projection gives a unit y with L*(y) in C* and <y,b>=-delta. Let y0 be a unit vector with L*(y0)[x]>=beta||x||^2 on P. With t=delta/8, y+t*y0 has target pairing at most -7delta/8 and cone margin at least delta*beta/8. Approximate it by a rational vector with norm error at most min(delta/8,delta*beta/[16 max(1,||L||)]). The result has negative target pairing at most -3delta/4 and positive cone margin at least delta*beta/16. Rational entry heights are O(log m+log(1/delta)+log^+(1/beta)+log^+||L||), apart from encoding supplied rational bounds. The optimization and verification costs are real-algebraic operations counted by the main fixed-dimensional algorithm, not unit-cost oracles.

If beta=0 the image may still be closed, as in the previous example, or nonclosed: L(X)=(X_11,X_12), b=(0,1) on CP_2 is approached by [[epsilon,1],[1,1/epsilon]] but has no exact lift. A true strict separator cannot be promised in this latter case. A real-feasible but arithmetically infeasible slice is a third, different situation: it needs the arithmetic reduction chain, not separation from the original real cone.

## 4. Total tolerance alternative with exact side constraints

First run arithmetic reduction for exact rational constraints H_0. If it returns EMPTY, provide its arithmetic obstruction chain. Otherwise, for a further rational observation M, target b and rational rho>0, decide the real semialgebraic system

 X in C(P_*) intersect H_0, ||M(X)-b||_2<rho.

If feasible, the closure theorem and the open inequality imply existence of a rational Gram factor meeting H_0 exactly and the error bound strictly. To construct it, move a feasible point slightly toward a terminal relative-interior completion while keeping the open inequality, and use rational approximation plus exact measurement repair. If infeasible, the exact conclusion is that every rational Gram completion satisfying H_0 has observation error at least rho. This is a total finite-precision alternative; it is not an exact membership claim. With beta>0 and no conflicting exact side constraints, the usual strict observation-separator option is additionally available for nonmembers.

## 5. Why the condition still does not bound adjacent walks

For the fixed nonsimplicial cone in checkpoint 007 and full observation L=identity, beta=1/sqrt(n): the trace-one PSD norm is at least 1/sqrt(n), and I/n belongs C(K). All A_N are interior, their arithmetic depth is zero, their factors have O_n(log N) height and fixed width, and their binary interior condition is O_n(log N), but the specified shadow walk has N-1 pivots. Thus even adding exact observation coercivity to arithmetic facial depth and coefficient-height bounds does not yield a polynomial bound on local adjacent crossings. This does not assert impossibility for every conceivable invariant or every local rule.
