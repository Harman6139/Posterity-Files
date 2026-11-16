# Checkpoint 08 — an all-order class with singular leading spectra, solved for every start

Date: 2026-11-15. This removes the positive-definite-leading-state restriction for a substantial affine family. It does not solve all singular affine–PSD systems. The one-good-orbit transfer lemma used below is an inherited result (original DRS Checkpoint 06); it is reproved here to keep the application self-contained.

## 1. Statement

Let C be any nonempty closed affine subset of the rectangular matrix space R^(r by s), with 0 not in C. Let

    C_*=P_C(0), beta=||C_*||_F>0,
    U={[[A,C],[C*,0]]: A in S^r, C in C}.

Write the actual cross variable as C in the affine set, and use C_* for its unique minimum-Frobenius-norm element. Define

    H=sqrt(2)(C_*C_*^*)^(1/2),
    G=sqrt(2)(C_*^*C_*)^(1/2),
    V=diag(H,G).

All projections use the original Frobenius metric. For EVERY symmetric starting point, plain affine-first Douglas–Rachford satisfies

    Z_k=V sqrt(k)+O(1),
    sqrt(k)(Z_(k+1)-Z_k) -> V/2,
    sqrt(k)||Z_(k+1)-Z_k||_F -> beta.                (1.1)

No full-rank assumption on C_* is needed. In particular V may have arbitrarily many zero eigenvalues. Both the affine and PSD shadow cross blocks converge to C_*.

The system is weakly infeasible with trace-escape exponent alpha=1. If

    D(R)=min{||QX-a||: X>=0, ||PX||<=R},

where P is the direction-space projector and a=P_U(0), then

    lim_(R->infinity) R D(R)=beta^2.                 (1.2)

Thus one ordinary affine least-squares problem computes the exact state matrix, last-step vector, speed, selected cross block and sharp static coefficient for this entire class. Coupled affine equations inside C are arbitrary.

## 2. An exact reference orbit

The affine anchor is a=[[0,C_*],[C_*^*,0]], because C_* is orthogonal to C's direction space. The affine projection of a block-diagonal state has cross block C_* and unchanged upper block.

Take a singular value decomposition of C_* with nonzero singular values sigma_i. Start DRS at zero. Its state remains block diagonal. In each matched pair of left and right singular directions it equals a_k(sigma_i) I_2, with every unmatched direction identically zero, where

    a_0(sigma)=0,
    a_(k+1)(sigma)=[a_k(sigma)+sqrt(a_k(sigma)^2+4sigma^2)]/2.

Indeed the reflected two-by-two block is [[a_k,2sigma],[2sigma,-a_k]], whose absolute value is sqrt(a_k^2+4sigma^2) I_2. The exact PSD DRS identity Tz=(z+|2P_Uz-z|)/2 proves the recurrence and block invariance. No decomposition of the arbitrary-start algorithm into independent blocks is assumed.

Put Delta a_k=a_(k+1)-a_k. Directly,

    a_(k+1) Delta a_k=sigma^2,
    a_(k+1)^2-a_k^2=2sigma^2-(Delta a_k)^2.

The squared increments of a_k are at least sigma^2, so a_k^2>=k sigma^2. Thus (Delta a_k)^2<=sigma^2/(k+1), and summation gives

    a_k^2=2sigma^2 k+O(log k),
    a_k=sqrt(2)sigma sqrt(k)+O(log(k)/sqrt(k)),
    sqrt(k) Delta a_k -> sigma/sqrt(2).

The zero-start reference orbit therefore has the state and velocity in (1.1), with an O(log(k)/sqrt(k)) state error.

## 3. Good-orbit transfer at and above the half-power threshold

### Lemma

Let T be firmly nonexpansive in a finite-dimensional Euclidean space. Suppose one actual orbit y_k has

    y_k=V k^p+o(k^p),
    k^(1-p)(y_(k+1)-y_k)->pV,
    V!=0, 1/2<=p<1.

Then every actual orbit x_k has the same leading state and last-step limits.

Proof. Put e_k=x_k-y_k, a_k=x_(k+1)-x_k, b_k=y_(k+1)-y_k. Firm nonexpansiveness yields

    ||e_(k+1)||^2+||a_k-b_k||^2<=||e_k||^2.

Thus e_k is bounded and epsilon_n=sum_(j>=n)||a_j-b_j||^2 tends to zero. For any fixed lambda>1, m=floor(lambda n), set I=sum_(j=n)^(m-1)j^(2p-2). The reference energy E_y=sum||b_j||^2 is asymptotic to p^2||V||^2 I. Cauchy–Schwarz gives

    |sum||a_j||^2-E_y|<=2sqrt(E_y epsilon_n)+epsilon_n.

Because p>=1/2, I is bounded below by a positive constant on a tail (or tends to infinity). Dividing by I makes the error tend to zero. The nonincreasing sequence ||a_k||^2 is squeezed by forward and backward proportional-window averages; sending lambda to one proves

    k^(2-2p)||a_k||^2 -> p^2||V||^2.                (3.1)

For completeness, the vector direction does not follow from this norm alone. Monotonicity of I-T gives

    <a_k-a_j,x_k-x_j><=0.

Since x_k=V k^p+o(k^p) and (3.1) bounds the steps, for j/k in [1+h,1+2h] it follows uniformly that

    <a_k,V>>=<a_j,V>+o(k^(p-1)).

Averaging over these indices telescopes the a_j. A separated backward window gives the reverse inequality. Sending h to zero proves k^(1-p)<a_k,V>->p||V||^2. Combine with (3.1) and expand ||k^(1-p)a_k-pV||^2 to obtain the vector limit. QED.

Apply the lemma at p=1/2 to the explicit reference orbit in Section 2. Nonexpansiveness also bounds every orbit's state distance to that reference, giving the O(1) state error in (1.1). This proves (1.1) without assuming an interior leading spectrum.

## 4. Selection of the bounded cross block

Let v_k be the PSD shadow and u_k=P_UZ_k the affine shadow. Write v_k=[[X_k,B_k],[B_k^*,Y_k]]. The state and step limits give

    X_k/sqrt(k)->H,
    sqrt(k)Y_k->G/2,

since the affine shadow has lower block zero. For any PSD block matrix, the contraction factorization B=X^(1/2) K Y^(1/2), ||K||_op<=1, gives

    ||B||_F^2<=||X||_F||Y||_F.                     (4.1)

Hence limsup ||B_k||_F^2<=||H||||G||/2=beta^2. Meanwhile u_k has cross block in C and v_k-u_k=d_k->0, so the projection of B_k onto Cdir^perp tends to C_*. Orthogonal decomposition now forces its component in Cdir to tend to zero. Therefore B_k->C_*. The affine-shadow cross block has the same limit. This proves the selection assertion.

## 5. Weak infeasibility and the exact static coefficient

An exact PSD point with lower block zero has zero cross block, impossible since 0 is not in C. For t>0 define

    X_t=[[t(C_*C_*^*)^(1/2),C_*],
         [C_*^*,t^(-1)(C_*^*C_*)^(1/2)]].

An SVD shows X_t is PSD, including rank-deficient cases. Its upper block and cross block match a point of U, and its lower block tends to zero. This proves weak infeasibility. Its direction-space radius is t beta, and its equation-distance is beta/t. Consequently D(R)<=beta^2/R.

For the lower bound take any PSD [[X,B],[B*,Y]] with primal radius at most R and equation-distance delta. Since the upper block is an unconstrained affine direction, ||X||_F<=R. Also ||Y||_F<=delta and

    ||P_(Cdir^perp)B-C_*||_F<=delta/sqrt(2).

Thus ||B||_F>=beta-delta/sqrt(2). Applying (4.1) yields

    R delta >= (beta-delta/sqrt(2))^2

whenever delta<sqrt(2)beta. Since D(R)->0, this and the matching upper bound prove (1.2). Frobenius/trace equivalence on PSD matrices and fixed norm equivalence for equality residuals give alpha=1.

## 6. Why this strengthens rather than contradicts the earlier certificate

Checkpoint 03 characterizes FULLY REGULAR leading spectra. Its test deliberately does not classify boundary optima. Here the finite program reduces to a Frobenius-norm minimization and an exact good orbit can be constructed even when the optimum is singular. Firm nonexpansiveness transfers its velocity to every start at p=1/2.

This supplies an all-order singular-spectrum positive theorem with arbitrary affine cross constraints. It neither extends the transfer lemma below p=1/2 nor settles the slow gamma=1 or gamma=2 p=1/4 dynamics. The singular-spectrum frontier is therefore narrowed by a concrete data-specified class, not declared fully classified.
