# Milestone 16 — a universal quantitative law for mixed SDP, SOCP and linear programming

Date: 2026-11-13. This combines the exact general-cone profile duality in 12, the exact-feasible repair in 14, and the nonlinear resource bound in 15. It makes the dimension parameter intrinsic to the nonlinear cone factors rather than the number of coordinates, auxiliary variables, or linear constraints.

## 1. Cone resource

Let

    K=product_j S_+^(d_j) times product_l L_(n_l) times R_+^u,

where the PSD factors may be real symmetric or complex Hermitian, and L_n is a Lorentz cone of dimension n>=3. Scalar cones represent any number of additional linear inequalities. Use the ordinary self-dual Euclidean inner products, and choose e in int K. Define

    tau(X)=<e,X>,
    B=sum_j(d_j-1)+number of Lorentz factors,
    E_B=2^B-1.

The gauge tau is positive and coercive on K. Lorentz factors of dimensions one or two are polyhedral and are absorbed into the scalar cone part. Zero-dimensional factors are omitted. The number B is independent of the Lorentz dimensions and of the number u of polyhedral factors.

## 2. Sharp reciprocal escape envelope

Let A(X)=b be weakly infeasible for K. Then B>=1 and, for instance-dependent c,C,delta0>0,

    c delta^(-1/E_B) <= R_b(delta) <= C delta^(-E_B),
    R_b(delta)=min{tau(X):X in K,||A(X)-b||<=delta},    (1)

for 0<delta<delta0. The minimum exists, and R_b diverges at zero.

Its attained rational escape exponent a satisfies

    1/E_B<=a<=E_B.                                    (2)

The normalized approximate Farkas-certificate profile

    Q_b(epsilon)=min{||y||:b.y=-1,A*y+epsilon e in K}  (3)

has reciprocal exponent 1/a. The exact functional identity from 12 remains

    d_b(R)=sup_(0<epsilon<1/R)
                    (1-R epsilon)/Q_b(epsilon),       (4)

where d_b(R) is the smallest residual with tau(X)<=R. If

    R_b(delta)~p0 delta^(-a),
    Q_b(epsilon)~q0 epsilon^(-beta),

then

    a beta=1,
    p0^beta q0=beta^beta/(beta+1)^(beta+1).             (5)

### Proof of the lower envelope beyond 15

The upper envelope is Theorem B of 15: only a partial PSD-support reduction or a boundary Lorentz-to-ray reduction changes the Laurent exponent by e -> 2e+1. At most B such steps are possible; scalar/polyhedral reductions leave the exponent unchanged.

The affine space L_b={A*y:b.y=-1} is weakly infeasible for the SAME self-dual product cone. This is the general conic argument proved in 12, not an ordinary attained Farkas certificate: L_b is disjoint from K but has zero distance to K. It can be described by a real linear equality system on that product space.

Apply the product-cone upper bound to L_b. For every small epsilon there exist Z_epsilon in K and T_epsilon in L_b with

    ||Z_epsilon-T_epsilon||<=mu epsilon,
    tau(Z_epsilon)<=C epsilon^(-E_B),

where mu>0 is chosen so e+mu times the Euclidean unit ball is contained in K. Consequently T_epsilon+epsilon e belongs K. Since b lies in range A, every preimage of T_epsilon under A* has b.y=-1; choose its minimum-norm preimage. Coercivity of tau and the pseudoinverse bound give

    Q_b(epsilon)<=C' epsilon^(-E_B).

Formula (4), evaluated at epsilon=1/(2R), yields d_b(R)>=c' R^(-E_B). Inverting the attained primal size/residual profiles proves the lower half of (1).

All cones and constraints are semialgebraic, so standard one-variable semialgebraic growth gives rational powers. Formula (4) gives reciprocity and the coefficient relation exactly as in 12. QED.

The exponent envelope is sharp as a function of B, even within products of B three-dimensional Lorentz cones, as demonstrated in Section 5. This is not a claim that every intermediate exponent occurs for a fixed product cone.

## 3. Universal nonattainment and regularization rates

Let F=K intersect {A(X)=b} be nonempty and let l be an affine objective with finite infimum v. Define

    T(eta)=min{tau(X):X in F,l(X)<=v+eta},
    V(lambda)=min_{X in F}[l(X)-v+lambda tau(X)].       (6)

Every positive-lambda minimum exists. If the source optimum is attained, let tau_star be the minimum gauge among exact optimizers. Then EVERY choice of minimizers X_lambda has

    tau(X_lambda)->tau_star,
    V(lambda)/lambda->tau_star,
    [l(X_lambda)-v]/lambda->0.                        (7)

If the optimum is not attained, replace K by the minimum face containing F. That face is a product of smaller PSD cones, full Lorentz cones, scalar rays and zero factors. Let

    B_F=sum_j max(r_j-1,0)+number of full Lorentz
                                          factors in this face,

where r_j is the maximum feasible rank in PSD factor j. Then B_F<=B and B_F>=1. There are p0>0 and a positive rational a with

    T(eta)~p0 eta^(-a),
    1/(2^B_F-1)<=a<=2^B_F-1.                         (8)

For EVERY choice of regularized minimizer,

    q_lambda=(a p0 lambda)^(1/(a+1)),
    l(X_lambda)-v ~ q_lambda,
    tau(X_lambda) ~ p0 q_lambda^(-a),
    V(lambda) ~ [(a+1)/a] q_lambda.                   (9)

In particular the exact value exponent theta satisfies

    2^(-B_F)<=theta<=1-2^(-B_F),
    theta=1/(a+1).                                   (10)

These bounds are independent of the number of linear constraints or auxiliary scalar variables, and independent of all Lorentz dimensions. The finite-dimensional constants and leading coefficients remain instance dependent.

### Proof

Attainment and compactness follow because tau is coercive on K and l-v>=0 on F. The attained case is the comparison with a gauge-minimal optimizer given in 14.

For nonattainment, choose a feasible point X0 in the relative interior of the minimum face. In its span use coordinates identifying that face with a self-dual product cone. Its gauge, inherited from e, is an interior dual functional and is comparable with the standard product gauge. The augmented equality system (A,l) targeting (b,v) is weakly infeasible in that product. By (1) its approximate-optimal trace/gauge profile has exponent between the two bounds in (8).

Exact source feasibility does not change this exponent. Indeed use a fixed right inverse to correct A(Y) to b, producing a cone violation O(delta), then mix with X0 at weight O(delta). This restores positivity and exact source feasibility, changes objective by O(delta), and increases gauge by only O(delta). Section 3 of 14 gives the explicit formula; the identical cone-order proof applies with X0>=_K gamma e. Thus the exact feasible T(eta) has the same exponent as the augmented weak system.

Finally

    V(lambda)=inf_(eta>0)[eta+lambda T(eta)].           (11)

The limiting scalar function eta+lambda p0 eta^(-a) has the unique optimizer q_lambda. The upper test at q_lambda and lower bound T(eta)>=(p0/2)eta^(-a) confine every actual optimizer to a fixed compact interval after scaling by q_lambda. Uniform asymptotics on that interval force the limits in (9). No uniqueness of the matrix/conic minimizer, differentiability of T, or dual Slater condition is required. QED.

## 4. One Lorentz cone: an exact universal square-root law

Suppose there is at most ONE nonpolyhedral Lorentz factor, no nonpolyhedral PSD factor, and any number of linear inequalities. If a finite source optimum is not attained, then B_F=1. Thus

    T(eta)~p0/eta,
    V(lambda)~2 sqrt(p0 lambda),
    l(X_lambda)-v~sqrt(p0 lambda),
    tau(X_lambda)~sqrt(p0/lambda).                    (12)

This holds irrespective of the dimension of the Lorentz cone, the number of equations, and the number of added scalar slack variables. There are no other optimal escape or linear-gauge regularization powers in the nonattained one-cone case.

For a semialgebraic norm w and a penalty lambda w(X)^q, q>0, trace/gauge equivalence gives the same exponent a in the near-optimal norm profile. If its leading coefficient is p_w, then

    l(X_lambda)-v~(q a p_w^q lambda)^(1/(qa+1)),
    min_F[l-v+lambda w^q]
         ~[(qa+1)/(qa)](q a p_w^q lambda)^(1/(qa+1)).  (13)

For one Lorentz cone a=1, so squared-norm regularization (q=2) has value and cost-gap exponent exactly 1/3. This is a global-minimizer asymptotic theorem, not a convergence-rate assertion about a particular numerical algorithm.

## 5. Sharp endpoints in products of SOC cones

Fix B>=1 and set a0=1. On variables x,a1,...,aB impose

    [[x,a_(i-1)],[a_(i-1),a_i]]>=0,
                                        i=1,...,B.   (14)

These are B three-dimensional rotated Lorentz constraints. They have strictly feasible points, and their projection on (x,aB) is

    x>0, aB>=x^(-(2^B-1)).                            (15)

To minimize x, near-optimality x<=eta forces aB>=eta^(-(2^B-1)). Equality choices a_i=x^(-(2^i-1)) give a matching lift with total product gauge of that order. Hence a=2^B-1 and theta=2^(-B).

To minimize aB instead, near-optimality aB<=eta forces x>=eta^(-1/(2^B-1)). Equality choices with x large make all a_i decrease, and the product gauge is of order x. Hence a=1/(2^B-1) and theta=1-2^(-B).

Both finite infima are zero and unattained. Appending the target optimal value as an equality produces weakly infeasible systems with the same profile exponent: the exact-feasible repair from Section 3 ensures that approximate original equalities cannot lower that exponent. Thus both endpoints of (1), (8) and (10) are sharp even for bounded-coefficient rational SOCPs.

These examples also explain the representation lower bound of 15. Any purported formulation with fewer than B Lorentz factors would violate its own maximal allowable escape exponent for the target set (15), regardless of the Lorentz dimensions or added linear constraints.

## 6. Interpretation and limitations

The common structure is

    nonlinear face reductions
       -> maximal escape exponent
       -> regularization phase law
       -> intrinsic lower bound on conic lifts.

This is a statement about arbitrary mixed SDP/SOCP/LP models, not a feature of a particular compiler. The number of polyhedral inequalities is absent because their elimination never creates a Schur-type squaring step. The number and rank of nonlinear factors impose an unavoidable quantitative limit.

The qualitative rank/face-reduction ideas, conic duality, regularization and semialgebraic growth have extensive prior literature. The complete proofs of the resource count, exact repair, rate formulas and matching examples are given in 12–16. The references and primary source links for related work are recorded in those manuscripts. No claim that an identified classical open conjecture is solved, that historical novelty has been exhaustively established, or that all possible intermediate exponents have been classified is made.

The leading coefficients, inverse cone margins and thresholds are not uniformly bounded in input bit length. Detecting a zero regularization limit or an asymptotic power is not presented as a finite-precision decision algorithm. The exact SDP complexity question remains outside these claims.
