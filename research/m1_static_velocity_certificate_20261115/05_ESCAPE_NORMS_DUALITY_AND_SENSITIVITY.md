# Checkpoint 05 — escape norms, duality and stable implicit selection

Date: 2026-11-15. This isolates the reusable static object behind Checkpoints 02–04. It is a family of ordinary norms defined by convex semidefinite programs; the DRS theorem gives those norms a dynamical interpretation. The construction does not require the order-seven example.

## 1. A norm associated with two matrix subspaces

Let A be a linear subspace of S^r containing a positive-definite matrix H0, and B a linear subspace of S^s containing a positive-definite matrix G0. For a prescribed rectangular C in R^(r by s), define kappa(C) as the optimum

 min { ||H||_F^2/4+||R||_F^2 :
        H in A, Z in B^perp,
        [[H,C],[C*,S]]>=0, Q>=0, R=S+Q-Z }.         (1.1)

Define n_(A,B)(C)=sqrt(kappa(C)).

### Theorem 1

n_(A,B) is a norm on the rectangular matrix space. Its squared value is computed by an attained, strictly feasible convex quadratic semidefinite program. Its unit ball has a representation as a projection of linear matrix inequalities and a second-order-cone constraint.

Proof. The compact-sublevel proof of Checkpoint 02 applies with fixed C. Feasibility follows by taking H=H0, S sufficiently large, Q=0, Z=0. Its value is zero exactly when C=0: a zero objective forces H=R=0, then pairing R=S+Q-Z with G0 forces S=Q=0 and block positivity forces C=0.

The value kappa is convex in C, since it is the partial minimum of a jointly convex objective over a convex feasible graph. Rescaling all variables and reversing the sign of the cross block give

    kappa(lambda C)=lambda^2 kappa(C) for real lambda.

The unit sublevel set is therefore convex, symmetric and absorbing. It is bounded: the objective controls H,R; G0 controls S as in Checkpoint 02; and ||C||_F^2<=tr(H)tr(S). Its gauge is exactly sqrt(kappa), which proves the triangle inequality and all norm axioms. The displayed finite program gives the conic representation. QED.

Consequently there are positive instance-dependent constants c,C such that

    c||X||_F <= n_(A,B)(X) <= C||X||_F.

This is a geometric norm; no claim is made that it is a newly invented abstract norm representation technique. Its role as the coefficient selected by weakly infeasible DRS is the substantive connection.

## 2. An exact dual norm formula

Use the standard rectangular inner product Re tr(D* C), without doubling it. The dual norm satisfies

 n_(A,B)^*(D)^2/4
  = min { ||P_A Y||_F^2+||G||_F^2/4 :
           G in B,
           [[Y,-D/2],[-D*/2,G]]>=0 }.              (2.1)

Proof. Let phi(D) denote the minimum on the right. It is finite: choose G positive in B and then Y sufficiently large. It is closed and attained. Indeed a bounded objective bounds G; positivity gives Y>=0, and pairing P_A Y with the positive H0 bounds tr(Y). The off-diagonal block and every matrix variable are then bounded. This also proves compactness when D varies over a sublevel.

The explicit dual of (1.1), from Checkpoint 02 with no cross-direction constraint, gives

    kappa(C)=sup_D {<D,C>-phi(D)}.

Strict primal feasibility gives equality rather than just weak duality. Since phi is proper closed convex, conjugation gives phi=kappa*. Alternatively the same conclusion follows from the exact gap formula and the separating-hyperplane form of convex duality.

For any norm n, direct optimization of the scalar radius t>=0 proves

    (n^2)^*(D)=sup_(t>=0){t n*(D)-t^2}=n*(D)^2/4.

This proves (2.1). QED.

## 3. The general implicit-selection principle

For the affine–PSD pair in Checkpoint 02, let its affine cross-space be C0+Cdir. The full finite program is exactly

    min_(C in C0+Cdir) n_(A,B)(C)^2.                (3.1)

If its coefficient matrices H_*,G_* are positive definite, its cross optimizer C_* is unique. By Checkpoint 03, every original plain DRS orbit has

    z_k=(H_*+G_*)sqrt(k)+O(log k),
    sqrt(k)d_k -> (H_*+G_*)/2,
    (P_Uz_k)_EF -> C_*,
    (P_PSD(2P_Uz_k-z_k))_EF -> C_* .               (3.2)

Moreover

    limiting squared DRS speed
     = lim_(r->infinity) rD(r)
     = min_(C in C0+Cdir) n_(A,B)(C)^2.              (3.3)

Thus the diverging algorithm implicitly minimizes a finite conically represented norm of its BOUNDED cross block. The same minimization determines the escape speed and the sharp static size/accuracy constant. This is an input-data selection law, not a criterion based on observing an infinite orbit.

The norm need not be strictly convex for arbitrary A,B; no uniqueness claim is made at a boundary optimizer. In the regular case, G_*>0 and H_*>0 make the weighted cross minimization strictly convex, giving the stated uniqueness.

## 4. Three exact norm identities

These illustrate how the permitted diagonal directions change the implicit regularization, even though the algorithm always uses Frobenius projections.

### (a) Free symmetric positive block and free symmetric dual block

If A=S^r and B=S^s, then

    n_(A,B)(C)=||C||_F.

Here Q=Z=0 at the optimum and S=C*H^dagger C. For H>0, put M=H^(-1/2)CC*H^(-1/2). Then

    ||C||_F^2=tr(HM)<=||H||_F||M||_F
             =||H||_F||C*H^(-1)C||_F
             <=||H||_F^2/4+||C*H^(-1)C||_F^2.

Equality is attained at H=sqrt(2)(CC*)^(1/2), with the Moore–Penrose interpretation at singular C, and S=(C*C)^(1/2)/sqrt(2). These matrices satisfy the block constraint by an SVD factorization. Thus the value is exactly ||C||_F^2. For a square invertible optimizing C, the dynamic certificate is fully regular.

### (b) A common scalar primal diagonal

If A=span(I_r) and B=S^s, then

    n_(A,B)(C)=r^(1/4)||C||_(Schatten 4).

Indeed H=hI gives objective r h^2/4+||C*C||_F^2/h^2. Minimizing over h gives value sqrt(r)||C*C||_F=r^(1/2)||C||_(Schatten 4)^2. The optimal G is 2C*C/h; it is positive definite when C has full column rank.

### (c) Independent diagonal entries and one dual coordinate

If A is the diagonal subspace of S^r and B=R, then

    n_(A,B)(c)=||c||_(4/3),
    n_(A,B)^*(w)=||w||_4.

The complete proof and DRS consequences are in Checkpoint 04. For one hyperplane w^Tc=d, this explains both the cubic formula c_i=d w_i^3/sum w_j^4 and the speed |d|/||w||_4.

These are actual changes in the selected norm caused by affine recession geometry, not changes in the projection metric.

## 5. Analytic sensitivity on the regular stratum

Fix A,B,Cdir and allow the affine offset C0(theta) to vary real-analytically. Assume the optimizer is regular at theta0. Then in a neighborhood of theta0 its coefficient pair H(theta),G(theta) and cross minimizer C(theta) are uniquely defined and real-analytic. The DRS leading state and velocity inherit this sensitivity.

Proof. On positive H,G let

    Phi_theta(H,G)=min_(C in C0(theta)+Cdir)
                           tr(H^(-1)C G C*).

The minimizer is the solution of a positive-definite quadratic linear system on Cdir, so Phi is analytic. For fixed positive G, the matrix fractional form is jointly convex in (H,C), and minimizing over the fixed affine C-space preserves convexity in H. For fixed H it is an infimum of functions linear in G, hence concave in G.

The balancing equations are F_theta(H,G)=0, where

    F_theta=(H/2+grad_A Phi_theta,
             G/2-grad_B Phi_theta).

The symmetric part of its Jacobian is block diagonal with blocks

    I/2+Phi_HH >= I/2,
    I/2-Phi_GG >= I/2.

The off-diagonal mixed derivatives cancel in the symmetric part. Thus this Jacobian is invertible, with inverse operator norm at most 2. The analytic implicit function theorem supplies the local solution, which remains positive. The exact primal–dual certificate in Checkpoint 02 makes it the global optimizer, not merely a local stationary point. In particular

    D_theta(H,G)=-(D_(H,G)F_theta)^(-1)D_theta F_theta,
    ||D_theta(H,G)|| <= 2||D_theta F_theta||.         (5.1)

The cross minimizer is analytic by its quadratic normal equations. QED.

This is robustness under changes preserving the indicated support/subspace geometry. Arbitrary perturbations can destroy weak infeasibility and are NOT covered.

## 6. Practical meaning and limits

The data-only program, dual gap, and implicit norm selection provide the new optimization-facing content requested by the editorial assessment. They supply a usable static certificate, exact coefficients, sensitivity and nontrivial all-order families. They do not classify every singular regime and do not turn a numerical solver's unverified output into an exact certificate. No claim about journal acceptance or comprehensive historical priority follows from these mathematical results.
