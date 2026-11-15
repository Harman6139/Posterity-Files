# Checkpoint 03 — globally analytic weak infeasibility with arbitrarily large escape exponents

Date: 2026-11-15. This construction makes the one-query theorem of checkpoint 02 nontrivial well beyond a single order-two example. It does not settle the rank-changing rational optimization class.

## Theorem

For every integer n>=1 there is an explicit rational, Frobenius-isometric affine PSD pencil Y_n(y) such that:

* its matrix is nonsingular with constant inertia at EVERY finite y;
* its affine space is genuinely weakly infeasible;
* its natural objective is globally real analytic, convex, and 1-smooth;
* f_n(0)<=1 and rho_(f_n)(s)=Theta_n(s^(-beta_n)) on a fixed sufficiently small interval, with beta_n=(2^n-1)/2;
* for n>=2 its order is 10n-2 and its coordinate dimension is n; its nonzero rational coefficients have O(log(n+1)) bits. For n=1 use the ordinary order-two example.

Thus the rational constant-rank class contains arbitrarily severe (indeed exponentially increasing in this family order) escape powers, yet the EXACT hidden-objective information complexity in checkpoint 02 is ONE query, not epsilon^(-beta_n-1/2). This is a contrast with iteration counts for a specified gradient/projection method, not a contradiction of the generic dimension-uniform minimax upper bound.

## 1. Two everywhere-nonsingular elementary blocks

Let

   W(t)=[[0,1],[1,t]].

Its eigenvalues have opposite signs for every real t. Its negative eigenvalue has magnitude

   r(t)=(sqrt(t^2+4)-t)/2,
   r(t)(t+r(t))=1.

For real s,t define the REAL symmetric 4-by-4 affine block

   B(s,t) = [[0,0,s,-1],
             [0,0,1, s],
             [s,1,t, 0],
             [-1,s,0,t]].

Writing K(s)=[[s,-1],[1,s]], it is [[0,K],[K^T,tI_2]], and K K^T=(s^2+1)I_2. Therefore its characteristic polynomial is

   det(lambda I-B)=[lambda^2-t lambda-(s^2+1)]^2.

Its eigenvalues are (t+sqrt(t^2+4(s^2+1)))/2 and (t-sqrt(t^2+4(s^2+1)))/2, EACH with multiplicity two. They are respectively strictly positive and strictly negative for every finite s,t. In particular det B=(s^2+1)^2>0 and inertia B=(2,2).

The negative eigenvalue magnitude r_B obeys

   r_B(t+r_B)=s^2+1.

This block is the real representation of a two-by-two complex Hermitian block with off-diagonal s+i, but the pencil used in the theorem is entirely real and rational. The fixed imaginary component becomes the displayed real constants +/-1. Its role is to prevent the rank loss at s=0 that occurs for a purely real scalar off-diagonal.

## 2. Coupled chain and rational isometric normalization

For n>=2 use variables t_1,...,t_n. Form a block-diagonal matrix from

   W(t_1), B(t_1,t_2),...,B(t_(n-1),t_n).

Append four more copies of W(t_1), three copies of W(t_i) for each 2<=i<n, and two copies of W(t_n).

Before coordinate rescaling, the squared Frobenius norm of the t_1 direction is 1+4+4=9: one original W diagonal, four entries in B(t_1,t_2), and four padding W diagonals. For 2<=i<n it is 2+4+3=9. For t_n it is 2+2=4. Distinct variable directions have disjoint entry supports, even in adjacent blocks. Hence set

   y_i=3t_i for i<n, y_n=2t_n.

The resulting direction matrices are rational and Frobenius orthonormal. Denote this unscaled pencil by X_n(y)=X_0+H y.

There are 3n+1 W blocks and n-1 B blocks. Thus the order is

   m=2(3n+1)+4(n-1)=10n-2,

and the number of negative eigenvalues is

   k=3n+1+2(n-1)=5n-1=m/2.

Every block is nonsingular for every finite y, so the full pencil is nonsingular with constant inertia (k,k). At y=0 every negative eigenvalue equals -1, giving f_X(0)=k/2.

To normalize the initial objective WITHOUT losing isometry, take the rational number kappa=1/(10n) and define

   Y_n(y)=kappa X_n(y/kappa)=kappa X_0+H y.

The direction matrices remain unchanged and orthonormal; all offsets stay rational. The natural objectives satisfy

   f_Y(y)=kappa^2 f_X(y/kappa),
   rho_Y(s)=kappa rho_X(s/kappa^2).

In particular f_Y(0)=kappa^2 k/2<1. The affine reparametrization and positive scalar multiplication preserve nonsingularity, inertia, and the escape exponent. Coefficient bit lengths are O(log(n+1)).

For n=1 simply use W(y_1), already isometric with initial value 1/2.

## 3. Lower bound allowing arbitrary matrix perturbations

It suffices to prove the exponent for X_n. Suppose dist_F(X_n(y),S_+)<=delta with 0<delta<=1/2. Every negative eigenvalue of each diagonal block has magnitude at most delta. Consequently

   t_1 >= delta^-1-delta,
   t_i >= (t_(i-1)^2+1)/delta-delta, 2<=i<=n.

These are NECESSARY conditions for the true Frobenius distance, not merely inequalities along a chosen comparison curve. They follow directly from the exact negative eigenvalue identities in Section 1 and monotonicity of a/r-r in positive r.

Put E_i=2^i-1. We claim

   t_i >= 2^(-E_i) delta^(-E_i).

For i=1, delta^-1-delta >= (1/2)delta^-1. If the claim holds for i-1, then

   t_i >= 2^(-2E_(i-1)) delta^(-E_i)-delta.

The subtracted delta is at most one quarter of the leading term for delta<=1/2, because E_i+1=2E_(i-1)+2. In particular at least half remains, yielding the displayed constant 2^(-E_i). This proves the induction. Therefore

   ||y|| >= 2 t_n >= 2^(1-E_n) delta^(-E_n).

The added W blocks can only strengthen the residual condition.

## 4. An explicit small-residual curve

For 0<e<=1 choose

   t_1=e^-1,
   t_i=(t_(i-1)^2+1)/e, 2<=i<=n.

Every W(t_i) has negative eigenvalue magnitude at most 1/t_i<=e. Every B(t_(i-1),t_i) has negative eigenvalue magnitude at most (t_(i-1)^2+1)/t_i=e. Since there are k negative eigenvalues counting multiplicity,

   dist_F(X_n(y(e)),S_+) <= sqrt(k) e.

The recursion gives t_i<=C_i e^(-E_i), with C_1=1 and C_i=C_(i-1)^2+1; all constants depend only on n. Hence ||y(e)||<=C_n' e^(-E_n).

Set e=delta/sqrt(k). This gives the matching upper minimum-radius bound O_n(delta^(-E_n)). It also proves that the distance between the affine space and the cone is zero. Exact feasibility is impossible because every W block has a strictly negative eigenvalue at every finite argument. Thus infeasibility is weak.

Converting residual delta to objective s=delta^2/2 gives

   rho_X(s)=Theta_n(s^(-E_n/2)).

The normalization identity in Section 2 preserves this exponent and gives fixed n-dependent constants and onset for Y_n. No horizon-dependent onset is introduced.

## 5. Exact arithmetic versus dynamics

Checkpoint 02 applies because Y_n has constant rank at every point. For a hidden rational member of the declared constant-rank class of this order/dimension, its globally analytic objective is recovered from one algebraic query; a near-feasible rational point can then be found by unlimited exact computation. The probe does not need to know its escape exponent.

For comparison, the fixed-step gradient and specified accelerated schemes in original milestone 26 have, on each such instance,

   f_GD(k)=Theta_n(k^(-1/(2beta_n+1))),
   f_acc(k)=Theta_n(k^(-2/(2beta_n+1))).

Since 2beta_n+1=2^n, their objective iteration counts scale respectively as epsilon^(-2^n) and epsilon^(-2^(n-1)). These inherited algorithm-specific conclusions follow from the proved profile and the cited comparator/radius theorem; they are not new iteration algorithms and not lower bounds on all exact-information methods.

To see that one information query can be necessary, compare Y_n(y) and Y_n(-y) as hidden rational charts. At sufficiently small objective level, the first W block forces respectively y_1>0 and y_1<0. Their success sets are disjoint, so a zero-query randomized rule cannot succeed with probability above 1/2 on both. The one-query upper from checkpoint 02 is therefore sharp on a class containing this pair.

The example shows that catastrophic conic escape and very slow projection trajectories do not, by themselves, imply a large oracle-information requirement. Arithmetic and global spectral continuation can remove it. It does NOT imply that rank-changing rational problems are equally easy.

## Attribution and limitations

Realification of a complex Hermitian matrix, eigenvalue calculations for a 2-by-2 block, and repeated-squaring growth are standard. The construction's asserted features are their combination into a rational isometric EVERYWHERE-NONSINGULAR weak-infeasibility ladder, with the true PSD-distance lower bound and the one-query consequence. Historical priority is not certified. No optimal order for these exponents is claimed.

The full exact-rational, rank-changing, fixed-prior optimization lower-bound frontier remains unresolved.