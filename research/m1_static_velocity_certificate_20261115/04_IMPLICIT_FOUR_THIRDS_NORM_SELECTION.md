# Checkpoint 04 — a hidden l^(4/3) selection law in semidefinite DRS

Date: 2026-11-15. This supplies a concrete arbitrary-order consequence of the finite static certificate. It is not the earlier isolated order-two or scalar common-diagonal example. The minimization below is a standard strictly convex vector problem, determined by the original affine data.

## 1. An affine family in every matrix order

Let C be a nonempty closed affine subset of R^r with 0 not in C. Consider

    U_C={ [[diag(t_1,...,t_r),c],[c^T,0]]:
                            t in R^r, c in C }

in S^(r+1), with the ORIGINAL Frobenius metric. The ordinary affine-first DRS map is

    T(Z)=Z+(2P_U Z-Z)_+-P_U Z.

The family is weakly infeasible: a PSD matrix with last diagonal zero has last row zero, which would require c=0. For any c in C, the PSD matrix with upper block tI and last diagonal ||c||^2/t approaches U_C as t tends to infinity. The static supports are E=R^r, F=R, with A the diagonal matrices, B=R and cross-space C.

Let

    c_* = argmin_(c in C) ||c||_(4/3),
    S_* = sum_i |(c_*)_i|^(4/3).

The minimizer exists, is unique and is nonzero, by coercivity and strict convexity of the norm (or of its square).

## 2. Exact theorem

Assume every coordinate of c_* is nonzero. Put

    h_i=sqrt(2) S_*^(1/4) |(c_*)_i|^(2/3),
    g=sqrt(2) S_*^(3/4),
    V=diag(h_1,...,h_r,g).

Then from EVERY symmetric starting point,

    Z_k=V sqrt(k)+O(log k),
    Z_(k+1)-Z_k=V/(2sqrt(k))+O(log(k)/k),
    sqrt(k)||Z_(k+1)-Z_k||_F -> ||c_*||_(4/3).       (2.1)

In addition the cross blocks of BOTH the affine and PSD shadows converge to c_*:

    (P_U Z_k)_(E,F) -> c_*,
    ((2P_U Z_k-Z_k)_+)_(E,F) -> c_*.                (2.2)

Their errors are O(log(k)/sqrt(k)). Thus although the full matrix diverges, its bounded coupling block converges to the minimum-l^(4/3)-norm point of the prescribed affine cross-space. In general this differs from the minimum-Euclidean-norm point used by the individual affine projection. The selection is induced by the interaction with the PSD projection, not inserted as a regularizer in the algorithm.

The finite program's interior condition is satisfied IF AND ONLY IF every coordinate of c_* is nonzero. Hence this vector optimization problem exactly tests fully regular leading spectra for the entire displayed affine family. Zero coordinates do not prove oscillation; those cases lie outside the interior conclusion.

## 3. Reduction of the matrix program to a vector norm

In Checkpoint 02's program, B is the full scalar space. Minimization over Q,Z therefore leaves Q=Z=0 and R=S=s>=0. With H=diag(h_i), block positivity is equivalent to

    h_i>=0,
    c_i=0 whenever h_i=0,
    s>=sum_(i:h_i>0)c_i^2/h_i.

For a fixed c, let q=sum c_i^2/h_i. Holder's inequality gives

 sum |c_i|^(4/3)
   =sum (c_i^2/h_i)^(2/3)(h_i^2)^(1/3)
   <=q^(2/3)(sum h_i^2)^(1/3).

Thus, including the zero-coordinate cases by continuity,

    ||c||_(4/3)^2 <= q ||h||_2
      <= ||h||_2^2/4+q^2
      <= ||h||_2^2/4+s^2.                           (3.1)

Equality is attained at

    h_i=sqrt(2) S(c)^(1/4)|c_i|^(2/3),
    s=S(c)^(3/4)/sqrt(2), S(c)=sum|c_i|^(4/3).

Indeed q=s and ||h||_2=2s. Therefore the optimum of the matrix program is EXACTLY

    kappa_* = min_(c in C)||c||_(4/3)^2
             =||c_*||_(4/3)^2.                     (3.2)

Its unique H and G=2s are the displayed h_i,g. If c_* has full support they are positive, so Checkpoint 03 gives (2.1).

For (2.2), the normal tracking in that proof gives w_k=w0(n_k)+O(k^-1/2), while n_k approaches V/||V|| at rate O(log(k)/sqrt(k)). The center space is support-block diagonal, so it contributes no cross block to the affine shadow. The cross block of a+P w0 is the unique minimizer of the weighted quadratic cross problem; at V that minimizer is precisely c_*. The PSD shadow differs from the affine shadow by d_k=O(k^-1/2). This proves (2.2) and its error bound. QED.

## 4. Closed form for one linear measurement

Take C={c:w^T c=d}, where every w_i is nonzero and d!=0. Let W4=sum_i w_i^4. Holder duality, or the strict-convex first-order condition, gives

    (c_*)_i=d w_i^3/W4,
    ||c_*||_(4/3)=|d|/||w||_4=|d| W4^(-1/4).

Every coordinate is nonzero. Hence (2.1)–(2.2) apply with

    h_i=sqrt(2)|d| w_i^2/W4^(3/4),
    g=sqrt(2)|d|/W4^(1/4).

This is an arbitrary-order formula for genuinely coupled affine equations, not a sum of independent two-by-two algorithms.

For example w=(1,2,3), d=1 gives

    c_*=(1,8,27)/98,
    P_C(0)=(1,2,3)/14,
    sqrt(k)||d_k|| -> 98^(-1/4).

The two selected vectors are visibly different. The algorithm uses Euclidean projections at every step, yet its limiting cross block solves an l^(4/3) optimization problem.

## 5. A modest exact rational certificate, with no enormous starting point

Let r=8,

    w=(2,2,3,4,4,5,5,5), d=5,
    H=diag(w_i^2/50), G=1, c=w_i^3/500.

Since sum w_i^4=2500, all entries of U's data, H,G,c are rational. Put W=w/10, S=R=1/2, Q=Z=0. Then exactly

    H>0, G>0, w^T c=5, HW=c,
    diag(WGW^T)=H/2, c^T W=G/2.

The positive primal block has zero Schur complement. A positive dual certificate is

    Y=[-W;1][-W^T,1].

Its cross block is -w/10, perpendicular to the direction space w^perp. Both primal and dual objectives are 1/2, so the exact gap is zero. The predicted limiting state is V=diag(w_i^2/50,1), and the exact last-step speed coefficient is 1/sqrt(2), from every start. There is no large-integer initialization assumption.

The diagnostic script verifies all these certificate identities with Python Fraction arithmetic. Its floating-point runs are separate corroboration, not the proof.

## 6. Diagnostics actually run

For w=(1,2,3), d=1 and 100000 ordinary DRS iterations, the predicted scaled step norm is 0.31782897044671854. The observed values were 0.3178343778743902 from zero and 0.31786653896315864 from a seeded random symmetric start.

For the rational order-nine certificate, the predicted value is 0.7071067811865477. The observed values at 100000 steps were 0.7071235553386991 from zero and 0.7072377791762594 from a seeded random start. All four runs showed decreasing scaled-vector and cross-selection errors at the recorded checkpoints.

These finite floating-point values are not asymptotic certificates. The exact certificate and proofs in Sections 1–5 are the mathematical basis.

## 7. What has and has not been generalized

This proves a concrete, calculable implicit-selection law and exact last-step constants across arbitrary matrix orders and arbitrary affine cross-spaces whose l^(4/3) minimizer has full support. It is strictly more predictive than assuming a positive-definite limiting orbit. It does not classify every boundary-support case and does not repair the universal raw velocity conjecture, which remains separated from the new regularity certificate.
