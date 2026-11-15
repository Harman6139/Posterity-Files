# Milestone 17 — general semidefinite extension complexity: finite slack tests and complete SOS certificates

Date: 2026-11-13. Builds a general framework around, rather than overstates, the escape lower bounds in 15–16.

IMPORTANT ATTRIBUTION. The equivalence between cone lifts and slack factorizations is classical: Gouveia–Parrilo–Thomas, *Lifts of convex sets and cone factorizations*, Math. Oper. Res. 38 (2013), 248–264, arXiv:1111.3164. Bounded PSD-factor rescaling and lower semicontinuity are also established ingredients; see Fawzi–Gouveia–Parrilo–Robinson–Thomas, *Positive Semidefinite Rank*, arXiv:1407.4095. The results below give a self-contained, size-uniform finite-obstruction formulation, its complete polynomial/SOS certificate version, and precise scope. They are not a claim to have newly discovered the classical general characterization, an efficient solution of PSD rank, or a closed-form evaluation for every convex set. The SOS ingredients are Putinar/Lasserre; rational certificates use Victoria Powers, arXiv:0911.1331.

## 1. Which complexity is being characterized

Work over real symmetric matrices. For a nonempty closed convex set C in R^n, define sxc(C) as the least d for which C is the projection onto x of an affine system in (x,Y), with Y in S_+^d. Arbitrarily many affine EQUALITIES and free auxiliary real variables are allowed; auxiliary free variables can be eliminated to obtain an affine subspace of R^n times S^d. Every additional scalar INEQUALITY must be encoded in the conic block and counts toward its size. Thus this is ordinary single-matrix SDP extension complexity, not the curvature resource sum(d_j-1), and not the largest-block extension degree.

For line-free C this agrees with the usual affine-image-of-an-affine-section definition: a free direction in the kernel of the matrix variables cannot change x, or C would contain an affine line. In particular the convention is exactly the usual one for convex bodies and polytopes. Allow d=0 for affine spaces. Equivalently one can work in the affine span and quotient lineality first. For a nontrivial convex body the minimum is at least one. Set sxc(C)=infinity when no finite lift exists.

Let F(C) be the nonzero affine functions

    f(x)=a_f+b_f.x,       inf_{x in C} f(x)=0.

They are nonnegative on C. Infimum zero is required, but ATTAINMENT is not required. Every nonempty closed convex set is the intersection of the halfspaces f>=0 for f in F(C), with affine-hull equalities handled in its affine span. Indeed a point outside C is strictly separated by the supporting hyperplane at a nearest point of C.

Define bounded normalized slack

    r(x)=1+||x||_1,
    c(f)=|a_f|+||b_f||_infinity >0,
    S_C(x,f)=f(x)/(r(x)c(f)).                         (1)

Then 0<=S_C(x,f)<=1. The normalization works for UNBOUNDED C as well. Positive row/column scalings never change PSD factorization size.

For a finite nonnegative matrix S, rank_psd(S) is the least d admitting

    S_ij=tr(P_i Q_j),       P_i,Q_j in S_+^d.

The zero matrix has rank zero.

## 2. General finite-obstruction theorem

**Theorem A.** For every nonempty closed convex C in the convention above,

    sxc(C)=sup_{I subset C finite, J subset F(C) finite}
                          rank_psd(S_C[I,J]).           (2)

Equivalently, a fixed order d works globally if and only if EVERY finite normalized slack table admits an order-d PSD factorization. If order d fails, SOME FINITE table already proves failure. No smoothness, semialgebraicity, strict feasibility of a supplied lift, boundedness of C, unique lift, positive decoder, or coefficient bound is assumed.

For a convex body with 0 in its interior one can instead use the ordinary bounded slack

    S(x,y)=1-x.y,        x in C, y in C^polar.          (3)

All points and all polar points are permitted, not merely extreme points. Formula (2) holds with (3). The values in (3) are bounded by 1+R/r when r B_2 subset C subset R B_2.

### 2.1 Size-uniform bounded factor normalization

**Lemma.** If a finite matrix M with entries in [0,M0] has PSD rank at most d, it has a factorization satisfying

    tr(P_i)<=1,       tr(Q_j)<=d M0.                   (4)

The bound is independent of the number of rows and columns.

Proof. Start with any factorization A_i,B_j and compress to U=span_i range(A_i), of dimension t<=d. Compression of each B_j leaves every pairing unchanged. The matrix sum_i A_i is positive definite on U. If t=0 the matrix is zero and the result is immediate.

Maximize log det X on

    X positive definite on U,       tr(A_i X)<=1.

The closure with X>=0 is bounded: tr((sum_i A_i)X) is bounded by the number of rows. A sufficiently small positive multiple of identity is strictly feasible. The maximum is attained at X_*>0, since log determinant tends to minus infinity at a singular boundary. The elementary Lagrange/KKT equations give nonnegative lambda_i with

    X_*^{-1}=sum_i lambda_i A_i,
    lambda_i(tr(A_i X_*)-1)=0.

Taking the pairing with X_* yields sum_i lambda_i=t. Set

    P_i=X_*^{1/2} A_i X_*^{1/2},
    Q_j=X_*^{-1/2} B_j X_*^{-1/2}.

Then tr(P_i)<=1 and

    tr(Q_j)=sum_i lambda_i M_ij<=t M0<=d M0.

Pad by zero coordinates if t<d. This proves (4). The same proof works for complex Hermitian factors. QED.

This proof is a normalization argument, not a polynomial-time algorithm for finding a factorization.

### 2.2 A lift gives slack factors, even on a singular face

Take any order-d lift and restrict all feasible PSD matrices to their maximum support. Averaging finitely many feasible matrices gives a point positive definite on this support. The compressed problem therefore has a Slater point; its order is at most d.

For every x in C choose one feasible lifted matrix A(x). For f in F(C), minimize f over the lifted problem. Its value is zero and finite. Slater duality gives an attained PSD dual slack B(f) with

    f(x)=tr(A(x) B(f))                                (5)

at every feasible lift of x. This uses dual attainment after support compression; it does not require the primal infimum to be attained or the original lift to be strictly feasible. With free coordinates, the dual stationarity equations eliminate their coefficients in exactly the same way. Padding and the positive scalings in (1) give finite rank_psd<=d.

For a compact body, (5) for tight inequalities also covers every polar point y. Each y in C^polar is a convex combination of extreme polar points; those points have support value one, since zero is interior. Combining their PSD dual slacks gives the slack 1-x.y. This explains why finite rational samples can be taken in the INTERIORS of C and its polar.

### 2.3 All finite factorizations glue to one global factorization

Assume every finite table in (1) has PSD rank at most d. Give every x its own variable P_x in the compact set {P>=0:trP<=1}, and every f its own variable Q_f in {Q>=0:trQ<=d}. Impose the closed equations

    tr(P_x Q_f)=S_C(x,f).

Every finite family of these equations is feasible: take its finite union of rows and columns and apply the normalization lemma. The finite intersection property in the product of the compact factor sets therefore supplies factors satisfying ALL equations simultaneously.

For countable dense index sets this step can instead be done by a diagonal convergent subsequence. No boundedness assumption on an originally supplied infinite factorization, and no uniform congruence for that factorization, is being presumed.

Undo the positive row and column scalings:

    A(x)=r(x)P_x,       B(f)=c(f)Q_f.

Then (5) holds globally.

### 2.4 A global factorization gives a finite affine SDP lift

Consider the affine equations, in the FINITE-dimensional variables (x,Z),

    tr(B(f) Z)=f(x)       for every f in F(C).          (6)

Their coefficient vectors lie in a space of dimension n+1+d(d+1)/2. A finite basis of their span therefore imposes all equations; at most that many are needed. This is an actual finite affine system, not an output with infinitely many constraints.

For x in C, Z=A(x)>=0 solves (6). Conversely, if Z>=0 solves (6), every f in F(C) is nonnegative at x. Closedness of C implies x in C. Hence (6) is an exact order-d lift. This proves Theorem A.

This sufficiency proof also handles sets containing lines in the free-variable convention. For line-free sets, x is determined affinely by Z, as explained in Section 1.

## 3. The complete PSD block-size profile

Fix a finite tuple dvec=(d_1,...,d_s). A product-PSD lift exists if and only if every finite normalized slack table admits

    S_ij=sum_{h=1}^s tr(P_i^(h) Q_j^(h)),
                P_i^(h),Q_j^(h)>=0 of order d_h.       (7)

For a table bounded by one, each summand is nonnegative and at most one. Apply (4) to the individual summand matrices. Thus one can require tr P_i^(h)<=1 and tr Q_j^(h)<=d_h, uniformly in the table size. The same finite-intersection and reconstruction proof then applies.

This characterizes every finite block-size tuple, not just the single-matrix resource. It correctly distinguishes:

- sxc(C): the smallest single order;
- a prescribed product-block profile;
- extension degree: the smallest largest block over all FINITE block counts.

The last statement still contains an existential quantifier over the number of blocks. A bound for sum(d_h-1) from 15 is a necessary geometric obstruction inside this full profile; it is not itself the full profile.

## 4. Every failed finite test has a finite SOS certificate

Let S be a finite normalized table with a rows and b columns and entries in [0,1]. For a proposed order d>=1 introduce real d-by-d matrices U_i,V_j. Define

    L_S(U,V)=sum_{i,j} [S_ij-||U_i^T V_j||_F^2]^2,     (8)
    g_i=1-||U_i||_F^2,
    h_j=d-||V_j||_F^2.

This is a degree-at-most-eight polynomial on the product of the indicated Euclidean balls. Any P_i,Q_j in (4) can be written U_i U_i^T,V_j V_j^T with these norm bounds. Consequently

    rank_psd(S)<=d  iff  min_{g_i,h_j>=0} L_S=0.        (9)

The minimum is attained. If rank_psd(S)>d, its minimum is STRICTLY positive.

Let w collect all scalar entries of the U_i,V_j and include the redundant ball inequality

    g_ball=a+bd-||w||_2^2>=0.

It is exactly sum_i g_i+sum_j h_j. Thus the quadratic module is explicitly Archimedean.

**Theorem B.** A finite table S has PSD rank greater than d if and only if there are gamma>0 and finitely many sum-of-squares polynomials such that the exact polynomial identity

    L_S-gamma = sigma_0+sum_i sigma_i g_i
                      +sum_j tau_j h_j+sigma_ball g_ball          (10)

holds. If S is rational, gamma and all polynomial coefficients in the sum-of-squares representations can be chosen rational.

Proof. The forward direction follows from strict positivity of L_S-gamma on the compact ball product, choosing gamma below its positive minimum and applying Putinar's theorem. For rational S, choose rational gamma; the explicit integer-radius ball permits the rational version proved by Victoria Powers (arXiv:0911.1331). Conversely, evaluation of (10) at a zero-loss factorization would give -gamma>=0, impossible. QED.

At any fixed degree, finding (10) is a finite SDP using Gram matrices for the SOS polynomials and coefficient-matching affine equations. Increasing degree is complete: when the table fails at order d, some finite degree succeeds with gamma>0. This does not promise a degree bound, polynomial runtime, or numerical certification from an uncertified floating-point solution. A displayed rational SOS identity is independently checkable by exact polynomial arithmetic.

For the product-block version, replace ||U_i^T V_j||^2 by its sum over blocks and use the corresponding ball generators. The conclusion is unchanged.

### A small exact illustration

For S=I_2 and proposed order d=1, write a_i=u_i^2 and b_j=v_j^2. Then

    L_S-1=(a_1 b_1+a_2 b_2-1)^2
                         +(a_1 b_2-a_2 b_1)^2.        (11)

This is already a rational SOS certificate, without multipliers. It proves no scalar PSD factorization of I_2 exists. The general theorem states that an analogous finite certificate exists for every finite order obstruction, although its degree may be much larger. The example is illustrative, not a claim of new PSD-rank theory.

## 5. A complete lower-bound hierarchy for arbitrary convex bodies

Let C be a full-dimensional convex body with 0 in its interior. Choose nested finite sets X_n dense in C and Y_n dense in C^polar, including initial affinely spanning points. Form S_n=(1-x.y) on X_n times Y_n, and divide by any fixed upper bound M for these entries.

Then

    sxc(C)=sup_n rank_psd(S_n).                        (12)

To see that dense samples suffice, approximate any finite set of rows and columns by the sampled ones. Bounded factor normalization makes the finite rank<=d condition closed under taking these limits. Theorem A applies.

For each d and n apply the degree-increasing SOS test (10). If sxc(C)>d, a finite n and finite SOS degree produce a strictly positive certificate. If sxc(C)<=d, none can do so. Thus EVERY fixed-order lower bound is detected at a finite stage. If sxc(C)=infinity, every fixed d is eventually rejected. This is not a single finite certificate that rejects all orders simultaneously.

When an explicit order-r lift is also supplied, the hierarchy eventually supplies the matching finite lower certificate at r-1. Hence the combination of an upper construction and the hierarchy is complete for proving an exact finite minimum. The nonconvex factorization search has not thereby become easy; we have a complete certificate characterization, not an efficient formula.

## 6. Fixed-order decidability for rational semialgebraic input

Suppose C is specified by a first-order real formula phi(x) with rational polynomial coefficients. Fix d and put D=d(d+1)/2 and k=n+D. Every order-d lift can be written using an affine subspace in (x,z) in R^k, described by at most k affine equations. Pad the equation list with zero equations. Thus existence of an order-d lift is exactly the first-order sentence

    exists Gamma in R^(k x k), c in R^k, for all x:
       phi(x) iff exists z in R^D:
           Gamma (x,z)=c and Mat(z)>=0.               (13)

PSD is expressed by the finitely many principal-minor inequalities. Real quantifier elimination therefore decides (13). If it holds, parameters can be chosen real algebraic, since the real algebraic numbers form a real closed field and the sentence has rational coefficients.

This is a finite, generally expensive decision procedure for a SPECIFIED d. It does not give a uniform upper bound on the required order and does not decide absence of every finite lift by simply running d=1,2,... . It makes no polynomial-time claim. Theorem (13) is a direct first-order consequence, not claimed as a new complexity-theoretic discovery.

## 7. Why escape exponents alone cannot be the characterization

A compact set has no finite unattained linear minimum. In particular the direct escape invariant of 15 contains no information for ANY compact polytope. Yet an n-dimensional simplex has sxc=n+1: its slack table is a diagonal identity of size n+1, and PSD zero-pairing forces that many independent support directions. The diagonal PSD lift attains the bound.

Likewise, allowing arbitrary linear inequalities for free makes the curvature resource zero for every polytope. It cannot equal standard SDP extension complexity, which counts these inequalities when they are encoded as scalar PSD blocks. This distinction is essential.

The escape obstruction remains useful for producing lower bounds, especially after changing to conic sections as in 19. The full slack/SOS characterization also detects the combinatorial and algebraic obstructions that escape alone misses.

## References and scope

1. J. Gouveia, P. A. Parrilo, R. R. Thomas, *Lifts of convex sets and cone factorizations*, Math. Oper. Res. 38 (2013), 248–264; https://arxiv.org/abs/1111.3164 . The classical factorization theorem is the foundational antecedent.
2. H. Fawzi, J. Gouveia, P. A. Parrilo, R. Z. Robinson, R. R. Thomas, *Positive Semidefinite Rank*, https://arxiv.org/abs/1407.4095 . In particular, bounded scaling, lower semicontinuity, block-diagonal additivity, and polyhedral sandwich interpretations are established theory.
3. C. Wang, L. Zhi, *Lifts of Non-compact Convex Sets and Cone Factorizations*, https://arxiv.org/abs/1501.00115 . Their recession-compatible generalized lift is stronger than the ordinary lift used in Section 1; no recession-surjectivity conclusion is silently inferred here.
4. J. B. Lasserre, *Global Optimization with Polynomials and the Problem of Moments*, SIAM J. Optim. 11 (2001), 796–817, DOI 10.1137/S1052623400366802.
5. V. Powers, *Rational Certificates of Positivity on Compact Semialgebraic Sets*, https://arxiv.org/abs/0911.1331 . This supplies the rational SOS conclusion in Theorem B.

This manuscript is a general exact characterization and certificate synthesis. It does not claim a novel universal closed-form expression evaluating PSD rank, a solution of the general efficient-lift classification problem, or publication priority for its classical ingredients. The next manuscripts give quantitative geometric consequences and applications of the earlier escape theorem within this general framework.
