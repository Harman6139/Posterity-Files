# Milestone 12 — reciprocal escape laws and sharp dimensional bounds for weak infeasibility

Date: 2026-11-13. This is a theorem about GENERAL conic feasibility, with sharp semidefinite consequences. It is independent of the two-basis construction. Milestone 11 then transfers the semidefinite conclusions into the rational two-basis one-scale class.

The central insight is not another representation gadget: minimum primal size and minimum approximate Farkas-certificate size are exact dual profiles. Their asymptotic exponents are reciprocal. For order-m PSD systems this gives a sharp universal envelope with both endpoints explicitly attained.

## 1. General conic definitions

Let K be a closed pointed full-dimensional convex cone in a finite-dimensional Euclidean space E, and let e belong to int K*. Let A:E->R^p be linear. Suppose b is WEAKLY INFEASIBLE:

    b in closure(A(K)) but b not in A(K).

In particular b!=0 and b belongs to range A. Use Euclidean norm in R^p. Define the primal size profile, the residual under a size cap, and the approximate normalized Farkas-certificate profile by

    R_b(delta)=min{<e,x>:x in K, ||Ax-b||<=delta},
    d_b(R)=min{||Ax-b||:x in K, <e,x><=R},
    Q_b(epsilon)=min{||y||:b.y=-1, A*y+epsilon e in K*}. (1)

For every positive delta and epsilon the displayed minima are finite and attained; R_b(delta) and Q_b(epsilon) tend to infinity as their arguments tend to zero. The size-capped minimum is positive for every finite R and tends to zero as R tends to infinity.

## Theorem A — exact profile duality

For every R>0,

    d_b(R)=sup_(0<epsilon<1/R)
                 (1-R epsilon)/Q_b(epsilon).            (2)

In particular,

    1/[2 Q_b(1/(2R))] <= d_b(R) <= 1/Q_b(1/R).          (3)

No Slater condition, cone-image closedness, dual optimum attainment, or differentiability is assumed. The dual object in (1) is a normalized approximate Farkas certificate, not the ordinary cost dual of an arbitrary chosen objective.

## Corollary B — reciprocal exponents, including leading constants

If K is semialgebraic, there are positive rational exponents a,beta and positive constants p0,q0 such that

    R_b(delta) ~ p0 delta^(-a),
    Q_b(epsilon) ~ q0 epsilon^(-beta).

They satisfy

    a beta=1,
    d_b(R) ~ [beta^beta/((beta+1)^(beta+1) q0)] R^(-beta),
    p0^beta q0 = beta^beta/(beta+1)^(beta+1).            (4)

Here ~ means ratio tending to one, not merely two-sided comparability. The rational exponents follow from the standard one-variable semialgebraic growth theorem; the reciprocity and the coefficient identity follow from the exact formula (2).

## 2. Proof that all profiles are legitimate

Since e is in int K*, there is c_e>0 such that <e,x>>=c_e||x|| for x in K. Thus the sets K intersect {<e,x><=R} are compact. Weak infeasibility gives arbitrarily accurate primal points, proving finiteness of R_b(delta); a minimizing sequence is size bounded, proving attainment. If R_b(delta) stayed bounded as delta->0, compactness would give an exact feasible point, a contradiction. Positivity and the limiting behavior of d_b(R) follow similarly.

We next justify the existence of approximate normalized certificates without invoking an invalid Farkas alternative. Consider the affine subspace

    L_b={A*y:b.y=-1}.

It is nonempty. It is disjoint from K*: an element A*y in K* with b.y=-1 would strictly separate b from closure A(K).

The distance between L_b and K* is zero. Otherwise strong separation would give x in K=(K*)* annihilating the direction space A*(b^perp), and with <x,Z><0 for Z in L_b. Annihilating that direction space means Ax=t b for some scalar t. Taking y0 with b.y0=-1 gives <x,A*y0>=-t<0, hence t>0. Then x/t is source feasible, contradiction.

Choose mu>0 with e+mu B contained in K*. For any epsilon>0, the zero-distance property gives Z=A*y in L_b and S in K* with ||Z-S||<mu epsilon. Then

    Z+epsilon e = S+epsilon[e+(Z-S)/epsilon] in K*.

Thus the constraint set defining Q_b(epsilon) is nonempty. It is closed, and norm minimization is coercive, so its minimum is attained. A bounded sequence of such y as epsilon->0 would converge to an exact separating certificate, which was just excluded. Hence Q_b(epsilon)->infinity.

## 3. Proof of the exact profile identity

For any approximate normalized certificate y at accuracy epsilon and any x in K with <e,x><=R,

    <y,Ax-b>=<A*y,x>+1 >= 1-epsilon R.

Cauchy–Schwarz implies ||Ax-b||>=(1-epsilon R)/||y||. Minimize over x and then choose the norm-minimizing y to obtain

    d_b(R)>=(1-epsilon R)/Q_b(epsilon)

for every 0<epsilon<1/R. This proves one inequality in (2).

For the reverse inequality let

    C_R=A({x in K:<e,x><=R}),

a compact convex set containing zero. Euclidean distance to C_R has the elementary support representation

    d_b(R)=max_(||u||<=1) [b.u-h_(C_R)(u)].              (5)

To see this without a minimax assumption, every expression is at most the distance by Cauchy–Schwarz; equality is achieved by the unit vector from a nearest point of C_R toward b, using the first-order projection inequality.

Write h(u)=h_(C_1)(u)>=0; cone scaling gives h_(C_R)(u)=R h(u). Let u attain the positive maximum in (5). Then b.u>R h(u). Moreover h(u)>0: if h(u)=0, then -A*u is in K*, and y=-u/(b.u) would be an exact normalized infeasibility certificate.

Put

    epsilon=h(u)/(b.u), y=-u/(b.u).

Then 0<epsilon<1/R, b.y=-1, and A*y+epsilon e is in K*: every x in K satisfies <A*u,x><=h(u)<e,x>. Also ||y||<=1/(b.u), so Q_b(epsilon)<=1/(b.u). Therefore

    (1-R epsilon)/Q_b(epsilon)
        >=(b.u)(1-R epsilon)=d_b(R).

Combined with the preceding inequality, this proves (2). Substituting epsilon=1/(2R) gives the lower bound (3); monotonicity of Q gives its upper bound.

## 4. Semialgebraic exponents and leading constants

When K is semialgebraic, the graphs of the value functions in (1) are semialgebraic by real quantifier elimination; attainment makes the minimization formulations unambiguous. The standard growth theorem for a nonzero one-variable semialgebraic function gives positive leading coefficients and rational exponents. Since R_b,Q_b diverge, their exponents have the stated negative signs.

Suppose Q_b(epsilon)~q0 epsilon^(-beta). The relative error in this asymptotic formula is uniform for all 0<epsilon<=1/R once R is sufficiently large. In (2), write s=R epsilon. Then

    d_b(R) ~ R^(-beta) q0^{-1} max_(0<=s<=1)(1-s)s^beta.

The maximum occurs at s=beta/(beta+1) and equals beta^beta/(beta+1)^(beta+1). Finally,

    d_b(R)<=delta  <=>  R_b(delta)<=R,

using the attained minima. Inverting the asymptotic power gives (4).

Thus reciprocity is a consequence of exact convex duality, not an inference from matching examples or a guessed pattern of exponents.

## 5. Semidefinite specialization and the sharp envelope

Now let K=S_+^m, e=I_m, m>=2, and A:S^m->R^p arbitrary. Put

    E_m=2^(m-1)-1.

## Theorem C — optimal dimension-only escape exponents

For EVERY weakly infeasible order-m SDP there are instance-dependent positive constants c,C,delta0 such that

    c delta^(-1/E_m) <= R_b(delta) <= C delta^(-E_m)
       for 0<delta<delta0.                              (6)

Both exponents are optimal at each m: rational bounded-coefficient systems attain

    R_b(delta) asymp delta^(-E_m)

and rational bounded-coefficient systems attain

    R_b(delta) asymp delta^(-1/E_m).

Equivalently every attained escape exponent a lies in the sharp interval [1/E_m,E_m]. This is a sharp ENVELOPE, not an assertion that every real number or every rational number in the interval occurs at fixed m.

The upper bound has the stronger form E=2^k-1 when a complete hyper-feasible partition has k blocks. If r0 is the maximum rank of a PSD matrix in ker A, one may take k<=m-r0, so the upper exponent improves to 2^(m-r0)-1. These parameters concern recession geometry, not the singularity degree of a nonempty primal feasible fibre.

## 6. Self-contained upper bound by block recession directions

Let L=ker A and choose any Z_base with A(Z_base)=b; b belongs to range A because it is a limit of source data. A sequence X_n>=0 with A(X_n)->b can be corrected into the affine space Z_base+L:

    Z_n=X_n+T(b-A(X_n)),

where T is a fixed linear right inverse on range A. Hence dist(Z_n,S_+^m)->0.

Construct a complete block partition as follows. If the current compression of L contains a nonzero PSD matrix, choose one, lift it to H_i in L, and orthogonally diagonalize its compressed support. Remove its positive support and repeat on the remaining coordinates. Earlier removed zero blocks remain zero after these later orthogonal rotations. In one fixed final orthogonal coordinate system, the resulting H_1,...,H_k satisfy

    compression of H_i to block i and all later coordinates
        = G_i direct-sum 0,       G_i>0.                (7)

The blocks have positive sizes. Stop when the residual compressed subspace L_terminal contains no nonzero PSD matrix.

The projected affine space has a PSD point. Indeed its projected Z_n have distance to PSD tending to zero. If they had an unbounded subsequence, normalization and a further subsequence would give a nonzero PSD member of L_terminal, contradiction. Therefore they have a bounded subsequence and a PSD affine limit. Lift that limit to Z0 in Z_base+L. Its terminal principal block is PSD.

The terminal block has positive dimension. If it had dimension zero, descending from the last positive G_k and adding sufficiently large multiples of H_k,...,H_1 would make Z0+sum_i lambda_i H_i positive definite, by successive Schur complements. That would be an exact feasible point, contradiction. Thus k<=m-1. Also k>=1, since without any removable direction the initial affine approximate sequence would already be bounded and feasible.

We now quantify the descending Schur construction. Put

    e_(k+1)=0, e_i=2 e_(i+1)+1=2^(k-i+1)-1,
    gamma_i=lambda_min(G_i)>0,
    beta_i=1+i/(k+1), 1<=i<=k+1.

Choose positive constants recursively from i=k down to 1:

    M_i=1+||Z0||_op+sum_(j>i) C_j ||H_j||_op,
    C_i=[M_i+(k+1)M_i^2]/gamma_i.                      (8)

For 0<epsilon<=1 define

    X(epsilon)=Z0+2 epsilon I+sum_(i=1)^k
                         C_i epsilon^(-e_i) H_i.      (9)

The terminal block is at least 2 epsilon I=beta_(k+1)epsilon I. Assume the block starting at i+1 is at least beta_(i+1)epsilon I. Subtract beta_i epsilon I when extending to block i. The lower block then has smallest eigenvalue at least epsilon/(k+1). The offdiagonal block and the unshifted upper block have norms at most M_i epsilon^(-e_(i+1)). The added diagonal is C_i epsilon^(-e_i)G_i. By (8), it dominates the possible negative upper part and the Schur term

    (k+1)M_i^2 epsilon^(-(2e_(i+1)+1)).

Thus the extended block is at least beta_i epsilon I. Induction proves X(epsilon)>=epsilon I. All H_i are in ker A, so

    A(X(epsilon))-b=2 epsilon A(I),
    tr X(epsilon)<=B epsilon^(-(2^k-1))                (10)

for an explicit constant B from (8) and the witness norms. A(I)!=0 in a weakly infeasible system: otherwise a sufficiently large multiple of I would turn any exact affine solution into a PSD solution. Taking epsilon=delta/(2||A(I)||) proves the upper bound in (6).

To obtain the r0 refinement, choose H_1 of maximum PSD rank r0. Since a nonempty terminal coordinate remains and each later block removes at least one coordinate, k<=m-r0.

This construction is a finite Laurent-polynomial path with displayed exponents. It does NOT assert a polynomial-time algorithm for finding the recession partition or the terminal PSD point, nor uniformly bounded bit length for the resulting large approximate solutions. Its constants are instance-dependent. The hyper-feasible decomposition is a classical ingredient; the quantitative recurrence is stated and proved here.

## 7. Universal lower bound by applying the upper bound to the normalized dual

The affine matrix space

    L_b={A*y:b.y=-1}

is weakly infeasible for the PSD cone, by Section 2. It is an affine subspace of S^m, so it can itself be specified by linear equality measurements on an order-m PSD matrix.

Apply Section 6 to that system, using an orthonormal description of distance to L_b. For each sufficiently small epsilon there are S_epsilon>=0 and Z_epsilon in L_b such that

    ||S_epsilon-Z_epsilon||_F<=epsilon,
    tr S_epsilon<=C epsilon^(-E_m).

Because b annihilates ker A*, the value b.y is determined by A*y. Choose the minimum-norm preimage y_epsilon of Z_epsilon under A*. Then b.y_epsilon=-1 and

    A*y_epsilon>=-epsilon I,
    ||y_epsilon||<=||(A*)^dagger||
                          (tr S_epsilon+epsilon).

Consequently Q_b(epsilon)<=C' epsilon^(-E_m). The lower bound in (3) now gives d_b(R)>=c'R^(-E_m), and inversion yields

    R_b(delta)>=c delta^(-1/E_m).

This proves the lower half of (6). It uses the same matrix order m, not an augmented order m+1, which is essential for the sharp exponent.

For clarity, the normalized dual's PSD trace profile and Q_b have the same power exponent. Conversely to the preceding construction, any y feasible for Q_b(epsilon) gives

    S=A*y+epsilon I>=0,
    dist(S,L_b)<=sqrt(m)epsilon,
    trS<=sqrt(m)||A*||||y||+m epsilon.

Together the two comparisons identify the exponent of Q_b with the normalized-dual escape exponent. Therefore the primal and normalized-dual PSD trace escape exponents multiply to ONE.

## 8. Rational extremizers at the fast endpoint

Use coordinates 0,...,m-1 and the bounded-coefficient equations

    X_00=0, X_01=1,
    X_ii-X_(0,i+1)=0 for 1<=i<=m-2.                  (11)

These are infeasible by PSD zero-row propagation. For epsilon>0 set

    a_i=epsilon^{-(2^{i-1}-1)},
    u_0=sqrt(epsilon), u_i=a_i/sqrt(epsilon),
    X(epsilon)=u u^T.

All entries of X(epsilon) are rational functions of epsilon. Its only residual is X_00=epsilon, and

    trX=epsilon+sum_(i=1)^(m-1) epsilon^{-(2^i-1)}.

For any PSD residual-delta competitor, delta<=1/4, we have X_00<=delta, a_1=X_01>=1/2, and

    a_(i+1)>=a_i^2/delta-delta>=a_i^2/(2delta).

Here a_i>=1/2 follows inductively, making the second inequality valid. Hence

    trX>=2^{-(2^m-2)}delta^(-E_m).

The matching explicit curve proves R_b(delta) asymp delta^(-E_m).

## 9. Rational extremizers at the slow endpoint

Use symmetric arrow matrices Z with zero offdiagonals in the leaf block (indices 1,...,m-1). Impose

    Z_(m-1,m-1)=0,
    Z_01=-1/2,
    2Z_(0,j)+Z_(j-1,j-1)=0 for 2<=j<=m-1,
    Z_ij=0 for 1<=i<j<=m-1.                          (12)

All coefficients are bounded rationals. The exact system is infeasible: the last zero diagonal kills its row, the preceding leaf diagonal then vanishes, and the chain eventually contradicts Z_01=-1/2.

For t>0 define leaf diagonals d_j=t^(2^j-1), leaf offdiagonals zero, and

    Z_00=(m-1)/(4t),
    Z_01=-1/2,
    Z_(0,j)=-d_(j-1)/2 for j>=2.

The leaf block is positive definite. Each term of the top Schur sum equals 1/(4t):

    (1/4)/d_1=1/(4t),
    d_(j-1)^2/(4d_j)=1/(4t).

Their sum equals Z_00, so Z(t)>=0 exactly. The only violated equation is the final diagonal, with residual delta=t^E_m, while tr Z(t) asymp 1/t. Thus

    R_b(delta)=O(delta^(-1/E_m)).

The universal lower bound makes this sharp. These slow and fast endpoint examples are normalized Farkas-dual geometries of each other; the opposing exponents are not an accidental numerical pattern.

## 10. Consequences for the two-basis programme

By 11, the centered two-basis minimum-scale profile satisfies

    R_b(K delta)-K delta<=Rtilde_b(delta)<=R_b(delta).

It therefore preserves each attained escape exponent. The fast family (11), with p=m, becomes a rational two-basis one-scale system of order N=9m^2+6m+5 with exponent E_m. At residual 1/(16K), every lifted approximate point has

    trY/c>=2^{2^m-2}-1/16.

Thus all difficult scale growth occurs in the single allowed observation direction, even though the bases and data have polynomial-bit rational descriptions. The general conic reciprocity theorem explains the paired approximate-certificate growth, and the exact dual transformations of 11 preserve the usual optimization dual as well. Those are distinct, compatible assertions.

This supplies a mathematical consequence beyond the existence of a compiler: a sharp all-dimension quantitative theory of weak-infeasibility escape, with an exact conic primal-dual functional identity and explicit rational extremizers.

## 11. Prior ingredients and scope

The proofs above are self-contained except for the standard one-variable semialgebraic growth theorem used only to turn functional comparisons into rational power asymptotics. That growth theorem is classical (for example the growth-dichotomy lemma recalled in arXiv:1411.0859 and arXiv:1901.01698).

The qualitative hyper-feasible partition and the fact that at most m-1 directions are needed are established antecedents: B. F. Lourenco, M. Muramatsu and T. Tsuchiya, A Structural Geometrical Analysis of Weakly Infeasible SDPs, Journal of the Operations Research Society of Japan 59 (2016), 241–257, DOI 10.15807/jorsj.59.241. Repeated-squaring and large-solution phenomena also have classical antecedents; see G. Pataki and A. Touzov, SIAM Journal on Optimization (2024), DOI 10.1137/21M1434945.

No claim is made here that those qualitative ingredients are new, that every exponent inside the envelope occurs at fixed matrix order, that instance-dependent constants are polynomially bounded in input length, or that exact SDP feasibility is solved in polynomial time. The proof establishes the stated exact profile identity, quantitative bounds and matching families; comprehensive literature priority and journal significance are separate questions.
