# Milestone 18 — robust finite witnesses and the Hausdorff boundary of SDP extension complexity

Date: 2026-11-13. Uses the finite slack characterization and bounded factor normalization in 17. The foundation is classical cone-factorization theory; the statements below provide self-contained quantitative geometric consequences and a complete finite-sampling formulation. No claim of historical priority for lower semicontinuity or the underlying sandwich theorem is made.

Throughout, sxc counts the order of ONE PSD matrix, with every scalar inequality counted if it is part of that matrix. The results do NOT apply to the curvature resource when arbitrarily many scalar inequalities are free: polytopal approximation alone would defeat such a claim.

## 1. Exact finite samples and intermediate convex bodies

Let C subset R^n be a full-dimensional convex body with

    r B_2 subset C subset R B_2,       0<r<=R.

Choose finite sets X={x_1,...,x_a} subset C and Y={y_1,...,y_b} subset C^polar such that zero is in the interior of both their convex hulls. Set

    P=conv X,
    Q={z:y_j.z<=1 for all j},
    S_ij=1-y_j.x_i.                                    (1)

The sets P,Q are full-dimensional bounded polytopes and P subset C subset Q.

**Theorem A (exact sandwich size).**

    rank_psd(S)
       =min{sxc(K):K is a convex body, P subset K subset Q}.       (2)

This is the finite pair-slack factorization principle, proved here including compactness of the constructed intermediate body. It is an established antecedent of the argument; see Fawzi et al., arXiv:1407.4095, Section 3.1.

### Proof

If P subset K subset Q and K has an order-d PSD lift, its slack factors on x_i in K and y_j in K^polar give rank_psd(S)<=d.

Conversely take an order-d factorization S_ij=tr(A_i B_j). Choose positive weights lambda_j with

    sum_j lambda_j=1,       sum_j lambda_j y_j=0.

Such strictly positive weights exist because zero is interior to conv Y; one can assign a small positive weight to each point and compensate within an interior simplex. Let U be the span of all ranges of B_j. Compress A_i,B_j to U, retaining every pairing. Then

    T=sum_j lambda_j B_j

is positive definite on U. Define

    K={x: exists Z>=0 on U,
                     tr(B_j Z)=1-y_j.x for all j}.      (3)

The row factors A_i prove P subset K; positivity proves K subset Q. Summing the equations in (3) with lambda_j gives tr(TZ)=1, so all feasible Z have bounded trace. The set of pairs (x,Z) is closed and bounded because x belongs Q; hence its projection K is compact. It has interior since it contains P. Its PSD order is at most d. This proves (2). QED.

## 2. Quantitative approximation from nets

Assume X is an epsilon_x-net of C and Y is an epsilon_y-net of C^polar in Euclidean norm, with

    epsilon_y<=1/(2R).

Then every K in the sandwich P subset K subset Q satisfies

    d_H(K,C)<=max(epsilon_x, 2 R^2 epsilon_y).          (4)

Proof. Since X is an epsilon_x-net, every point of C is within epsilon_x of P and hence of K.

For z in Q and z!=0, put u=z/||z||. The point u/R belongs C^polar, so some y_j differs from it by at most epsilon_y. Thus

    1>=y_j.z>=||z||(1/R-epsilon_y),
    ||z||<=R/(1-R epsilon_y).

For every y in C^polar choose a nearby y_j. Then

    y.z<=1+epsilon_y||z||,

so z/(1+epsilon_y||z||) belongs C. Therefore

    dist(z,C)<=epsilon_y||z||^2/(1+epsilon_y||z||)
              <=R^2 epsilon_y/(1-R epsilon_y)
              <=2R^2 epsilon_y.

The same bound holds on K subset Q, proving (4). QED.

Consequently nested dense samples yield a sequence of EXACTLY REPRESENTABLE intermediate bodies K_n with

    P_n subset K_n subset Q_n,
    sxc(K_n)=rank_psd(S_n),
    K_n -> C in Hausdorff distance.                    (5)

The sampled PSD ranks are nondecreasing and

    sup_n rank_psd(S_n)=sxc(C)                         (6)

by 17. If sxc(C) is finite, the integer sequence eventually equals it. This does not mean that observing a finite plateau certifies that no future increase is possible; an upper lift or a separate exact decision is still needed.

## 3. A coefficient-independent positive separation margin

Fix d<sxc(C). By 17 there are finite X subset C and Y subset C^polar for which S in (1) has PSD rank greater than d. Extra spanning points may be appended without decreasing rank. Put

    M=2+R/r,
    L=(r+R)/r^2,
    Delta_d(S)=min max_(i,j)|S_ij-tr(P_i Q_j)|,          (7)

where the minimum is over PSD factors of order d satisfying

    tr P_i<=1,       tr Q_j<=d M.

The factor domain is compact. The normalization theorem in 17 and rank_psd(S)>d imply

    Delta_d(S)>0.

**Theorem B (explicit Hausdorff obstruction).** Every convex body K with sxc(K)<=d satisfies

    d_H(K,C)>=min(r/2, Delta_d(S)/L).                  (8)

This lower bound allows arbitrary coefficients, arbitrary nonunique auxiliary fibres, and singular lifted faces in K's representation. No coefficient bound on the competing SDP is imposed.

### Proof

Suppose epsilon=d_H(K,C)<r/2. Convex-body support functions differ by at most epsilon, so K contains (r-epsilon)B_2 and has zero in its interior. For each x_i select x_i' in K with ||x_i'-x_i||<=epsilon. Put

    y_j'=y_j/(1+epsilon/r).

For any z in K, choose c in C at distance at most epsilon. Then

    y_j.z<=1+epsilon||y_j||<=1+epsilon/r,

so y_j' belongs K^polar. The finite slack table

    T_ij=1-y_j'.x_i'

has PSD rank at most d, since it is sampled from K. Its entries are nonnegative and bounded above by

    1+(R+epsilon)/r < M.

The normalization lemma supplies factors admissible in (7). Moreover

    ||y_j'||<=1/r,
    ||y_j'-y_j||<=epsilon/r^2,

and hence

    |T_ij-S_ij|
       <=||x_i'-x_i|| ||y_j'||
                          +||x_i|| ||y_j'-y_j||
       <=epsilon/r+R epsilon/r^2=L epsilon.

Thus Delta_d(S)<=L epsilon. This proves (8). QED.

A finite algebraic slack obstruction therefore gives a quantitative geometric gap. Large, cancelling, or diverging coefficients in a competing lift cannot bypass it, because the factor normalization is automatic and size dependent, not supplied as a conditioning assumption.

## 4. Turning an SOS identity into a numerical geometric lower bound

Use Gram variables P_i=U_i U_i^T, Q_j=V_j V_j^T, with

    ||U_i||_F^2<=1,       ||V_j||_F^2<=d M.

Suppose a finite exact SOS certificate proves

    sum_(i,j)(S_ij-||U_i^T V_j||_F^2)^2>=gamma>0

on these balls. The product-ball positivity certificate is precisely the form proved complete in 17, with an added redundant integer-radius ball if M is rational.

Since a table with maximum entry error e has squared loss at most ab e^2, (8) becomes

    d_H(K,C)>=min(r/2, sqrt(gamma/(ab))/L)             (9)

for every K with sxc(K)<=d.

For rational samples and rational declared radii, gamma and the certificate may be rational, using Powers' rational Positivstellensatz. There is no asserted polynomial bound on the sample size, polynomial degree, reciprocal gap, or certificate bit length. This is a complete finite-certificate statement, not a practical complexity guarantee.

## 5. No smaller fixed-order limit representation

**Corollary C.** The function C -> sxc(C) is lower semicontinuous under Hausdorff convergence of full-dimensional convex bodies to a full-dimensional convex body:

    C_j -> C  implies  sxc(C)<=liminf_j sxc(C_j).       (10)

Indeed, for each d<sxc(C), Theorem B excludes every sufficiently close order-d body. Equivalently, the class of bodies with lift order at most d is closed at every full-dimensional body.

Define a fixed-order limiting complexity by asking for the smallest d such that C is a Hausdorff limit of bodies of SDP order at most d. Then

    limiting complexity(C)=sxc(C).                    (11)

The trivial constant sequence proves one direction; (10) proves the other. In particular, if C has NO finite SDP lift, then every fixed d has a positive Hausdorff approximation floor. Any arbitrarily accurate family must have unbounded order.

This is NOT a statement that approximating C is as costly as representing it exactly at every specified tolerance. The positive floor depends on C and d and may be extremely small.

A bounded nonclosed order-d spectrahedral shadow whose closure is a full-dimensional body also has a closure of order at most d. To prove this, approximate any finite list of closure points by points of the shadow; its supporting functionals have the same infima on the shadow and its closure. Slater duality on a compressed lift gives the finite slack factorizations before taking the limit. The bounded factor lemma gives a limiting factorization for each finite table, and 17 reconstructs a closed lift. This conclusion is an existence theorem; it does not say that the original unclosed projection was already closed.

## 6. Rational finite lower certificates for arbitrary convex bodies

If C and C^polar have nonempty interiors, rational points are dense in both. Thus the dense samples in Section 2 can be chosen rational, even when boundary coordinates are not rational. Each sampled slack table is rational.

If sxc(C)>d, some finite rational sample table already has rank_psd>d, and 17 supplies a finite rational SOS obstruction. This assertion has two separate certificate requirements:

1. the sampled points and inequalities really belong to C and C^polar;
2. the displayed rational SOS identity rules out an order-d factorization of their slack.

The second is an exact algebraic certificate. The first needs a valid description or oracle for C. We do not claim that arbitrary uncomputable convex bodies admit an algorithm for checking sample membership. For rational semialgebraic descriptions, real quantifier elimination supplies an exact, potentially expensive membership procedure, consistent with 17 Section 6.

## 7. Relation to the escape programme and limitations

The earlier curvature resource is not Hausdorff robust when arbitrary linear inequalities are free: polytopes have resource zero and approximate every convex body. Standard single-matrix order DOES charge for those scalar inequalities and obeys (8)–(11).

Theorems (2), (6), and the SOS certificates give a general necessary-and-sufficient approach to SDP extension complexity. The escape exponents of 15–16 are one tool for establishing rank lower bounds within it, not a replacement for the entire slack structure. Compact bodies have no directly unattained linear objectives; 19 transfers the escape obstruction to them through same-order homogenization.

Prior results on PSD-factor lower semicontinuity and sandwich factorizations are expressly acknowledged. This document does not claim a new solution of efficient general PSD-rank computation, a universal closed-form minimum-order formula, or a finite procedure proving absence of all orders merely by testing finitely many proposed orders.

Primary references: Gouveia–Parrilo–Thomas, arXiv:1111.3164; Fawzi–Gouveia–Parrilo–Robinson–Thomas, arXiv:1407.4095; Powers, arXiv:0911.1331. The exact normalization and finite-certificate derivations used here are included in 17.
