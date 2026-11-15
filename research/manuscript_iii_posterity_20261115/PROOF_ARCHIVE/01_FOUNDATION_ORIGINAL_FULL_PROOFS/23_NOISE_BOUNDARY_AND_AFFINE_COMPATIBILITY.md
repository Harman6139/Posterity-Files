# Milestone 23 — exact versus approximate PSD rank, and the affine-compatibility obstruction

Date: 2026-11-13.
Parent research snapshot: efb31c8543c326dc42a5597ffdef1e78aa988e92.

## Status and attribution

This manuscript settles a precise remaining question from 22: can its exponential exact PSD-rank separation persist at a fixed positive entrywise relative error? NO. An explicit polynomial construction rules this out for EVERY fixed positive entry window. This is not a resolution of general SDP extension complexity, a sharp evaluation of all approximate PSD ranks, or an efficiently explicit exponential exact-rank family.

The basic polynomial-square approximation method is CLASSICAL. Alexander Barvinok, *Approximations of convex bodies by polytopes and by projections of spectrahedra*, arXiv:1204.0471v2, Theorem 5.1 and Lemmas 4.3–4.4, already proves that bounded nonnegative matrices have entrywise approximations with PSD rank polynomial in ordinary rank at every fixed absolute accuracy. It would be incorrect to claim that qualitative conclusion as new. Here we give an explicit rational, one-sided relative-error version with a logarithmic accuracy-degree bound on a positive window, derive its precision and marginal-preservation consequences, and combine it with 21–22 to isolate the exact affine-consistency obstruction in geometric reconstruction.

Primary sources read: https://arxiv.org/html/1204.0471 (Section 5); https://arxiv.org/html/1407.4095 (square-root rank, lower semicontinuity, correlation generation). The geometric hard-body and exact-rank inputs are the preceding project manuscripts 21–22, not newly reproved here. All upper bounds and the explicit Hadamard lower bound below are independent of those inputs.

## 1. Definitions

For a finite strictly positive real matrix M, define

    psdrank_rel,eps(M) = min{psdrank_R(N):
                              |N_ij-M_ij| <= eps M_ij for every i,j}.

For 0<eps<1 all admissible N are positive. Real PSD rank uses real symmetric PSD factors. A real factorization is also a complex factorization, so every upper bound below holds in either field. Positive global scaling changes neither rank nor this relative-error rank.

The symbol M need not denote a symmetric or PSD matrix. Only its factor matrices in a PSD factorization must be PSD. Bounded entry range is not a spectral condition-number hypothesis.

## 2. Explicit polynomial approximation theorem

**Theorem A.** Suppose rank(M)=r>=1 and 1<=M_ij<=K, where K>=1. For 0<eps<=1, set

    t = ceil(K log(4 sqrt(K)/eps)),
    D = binom(r+t,t).

There is a nonnegative matrix N with

    M_ij <= N_ij <= (1+eps) M_ij,
    psdrank_R(N) <= D.                                  (1)

All factors can be chosen rank one. If M and K are rational, the factors and N can be rational. For fixed K and eps the construction is polynomial in the length of the explicit input table. More generally it is constructive in the returned feature dimension D; no polynomial dependence on r,t independent of D is claimed. Rank one of M also permits the trivial exact order-one nonnegative factorization.

For K=1, M is the all-one matrix and the exact order-one conclusion applies. The displayed bound remains valid but is unnecessary.

### 2.1 A one-sided square-root polynomial

For j>=1 put

    a_j = binom(2j,j)/(4^j(2j-1)) > 0,
    p_t(z) = 1 - sum_{j=1}^t a_j z^j.

The binomial series gives

    sqrt(1-z) = 1-sum_{j>=1} a_j z^j,  0<=z<1.

Also sum_{j>=1} a_j=1: let z increase to one and apply monotone convergence to the nonnegative series. Consequently, for 0<=z<=q:=1-1/K,

    0 <= p_t(z)-sqrt(1-z)
      = sum_{j>t} a_j z^j <= q^(t+1).                   (2)

There is no approximation-theory oracle in this formula. The coefficients are explicit rationals. Since q<=exp(-1/K), the chosen t satisfies

    sqrt(K) q^(t+1) <= eps/4.

For x in [1,K], set z=1-x/K. Dividing (2) by sqrt(x/K)>=1/sqrt(K) gives

    1 <= p_t(1-x/K)/sqrt(x/K) <= 1+eps/4.

Therefore the rational polynomial

    F_t(x) = K p_t(1-x/K)^2

obeys

    x <= F_t(x) <= (1+eps/4)^2 x <= (1+eps)x.           (3)

Define N entrywise by N_ij=F_t(M_ij).

An exact rational implementation can choose t by testing

    16 K (1-1/K)^(2(t+1)) <= eps^2

instead of evaluating logarithms or square roots. The logarithmic formula is a sufficient upper bound on that search.

### 2.2 Feature dimension and PSD factors

Write M_ij=<u_i,v_j> with u_i,v_j in R^r. Expand the degree-t polynomial p_t(1-x/K) as sum_{l=0}^t c_l x^l. For a multi-index alpha in N^r with |alpha|<=t define

    f_i(alpha)=u_i^alpha,
    g_j(alpha)=c_|alpha| (|alpha|!/alpha!) v_j^alpha.

There are D=binom(r+t,t) such indices. The multinomial theorem gives

    <f_i,g_j> = p_t(1-M_ij/K).

Hence the rank-one PSD factors

    A_i=K f_i f_i^T,     B_j=g_j g_j^T

satisfy tr(A_i B_j)=N_ij. Negative feature coordinates cause no positivity problem: their outer products are PSD. This proves (1).

For rational input, rational Gaussian elimination supplies a rational rank factorization of M. All coefficients and monomials above are rational. Their bit lengths are polynomial in the input and t; writing the full factors is of course at least linear in their output size. For fixed K,eps, t is constant and D is polynomial in r. No potentially ill-conditioned real rank decision is required for an exact rational input table. QED.

### 2.3 Explicit approximation hierarchy

For every t>=0 the same construction gives a decreasing entrywise sequence N^(t) tending to M, with rank-one PSD factors of order at most binom(r+t,t), and relative error at most

    e_t = 2 sqrt(K) q^(t+1) + K q^(2t+2).              (4)

Thus the theorem is an explicit hierarchy, not merely an existence proof. Rationality of the entries does not require a rational square root of K, because K is placed in one PSD factor.

## 3. The exact exponential separation is not fixed-noise robust

For each fixed K and fixed eps>0, Theorem A implies

    psdrank_rel,eps(M) <= r^O_K,eps(1).                 (5)

Applied to the family of 22, whose exact PSD ranks exceed 2^((r-1)/4), this gives a separation on the SAME matrices:

    exact PSD rank = 2^Omega(r),
    fixed-relative-error PSD rank = r^O(1).            (6)

The exact lower bound in (6) is inherited from 21–22; the upper bound is unconditional and already has its qualitative antecedent in Barvinok's theorem. Thus a proposal to prove exponential PSD rank for all fixed-relative-error perturbations of that family is false. No further choice of those bounded-window matrices can repair that proposal.

### 3.1 An exponentially fine precision requirement

Let eps_r be a sequence and keep K fixed. If log(1/eps_r)=o(r), then t=o(r) in Theorem A. The standard product bound for binomial coefficients gives

    log binom(r+t,t)
       <= t log(e(r+t)/t) = o(r).

Therefore

    psdrank_rel,eps_r(M_r) <= exp(o(r))                 (7)

uniformly over EVERY rank-r positive matrix in the fixed window.

In particular an exponential lower bound at accuracy eps_r requires log(1/eps_r)=Omega_K(r).

A nonasymptotic version is useful. For c>0 let theta_c>0 satisfy

    (1+theta_c)log_2(1+theta_c)-theta_c log_2 theta_c=c/2.

If psdrank_rel,eps(M)>=2^(c r), then necessarily

    eps < 4 sqrt(K) exp(-(theta_c r-1)/K).              (8)

Indeed, if t<=theta_c r, the entropy bound yields binom(r+t,t)<=2^(c r/2), a contradiction. Since t<=K log(4sqrt(K)/eps)+1, rearrangement gives (8).

This is a NECESSARY accuracy condition, not a matching lower bound at that precision. It does not identify the exact accuracy threshold of the existential hard family.

### 3.2 Why fixed-matrix lower semicontinuity is not contradicted

For any fixed finite M and d<psdrank(M), there is a positive perturbation radius excluding order d, by bounded factor normalization and closedness of the fixed-order factorization set. The radii need not be uniform as r grows. Equations (7)–(8) constrain how small those radii must be when d is exponential in r. No fixed-rank closedness statement is violated.

## 4. Small noise does not make every matrix constant-size

For every power of two r, let H be the r-by-r Sylvester Hadamard matrix, with first row and column all one, and put

    M=2J+H.

Then M has entries in {1,3} and ordinary rank r. To see invertibility, H^{-1}=H^T/r and 1^T H^{-1}1=1, so the determinant lemma gives det(H+2J)=3det H, which is nonzero.

Suppose |N_ij-M_ij|<=eps M_ij. Then ||N-M||_F<=3eps r. Put T=N-2J and s=rank T. If P is the orthogonal projector onto ker T, then

    ||(H-T)P||_F^2=||HP||_F^2=r(r-s).

It follows that s>=r(1-9eps^2), and rank N>=s-1. Real order-d PSD factors imply rank N<=d(d+1)/2, whence

    d(d+1)/2 >= r(1-9eps^2)-1.                        (9)

For eps=1/12 this is d(d+1)/2>=15r/16-1, an explicit Omega(sqrt r) lower bound. Complex factors give d^2 in place of d(d+1)/2.

This illustrates a genuine remaining polynomial complexity; it is not a claim that the polynomial exponent in (5) is optimal. Determining that optimal exponent for all K,eps is not solved here.

## 5. Exact marginals and approximate quantum correlation generation

Let p be any finite strictly positive probability table of ordinary rank r and entry ratio at most K. Positive scaling places it in the window of Theorem A. Let B be the resulting unnormalized approximate table and normalize it to q0. There are e_ij in [0,eps] such that

    q0_ij = p_ij (1+e_ij)/(1+e_bar),
    e_bar=sum_ij p_ij e_ij.

The nonnegative amplitude matrix sqrt(q0), taken entrywise, has ordinary rank at most D because p_t is positive on the interval. Thus q0 is generated by measuring a pure bipartite state of Schmidt rank at most D.

One can additionally preserve BOTH original marginals exactly without increasing D.

### 5.1 Positive scaling with exact marginals

Minimize D_KL(q||q0) over all joint tables q with the same row and column marginals as p. The feasible set is a nonempty compact transportation polytope and contains the strictly positive table p. The strictly convex objective has a minimizer q. That minimizer is positive: mixing any minimizer with p gives a negative infinite directional derivative if a cell is zero, while the other derivative terms remain finite.

Lagrange stationarity in the affine marginal space yields

    q_ij=a_i q0_ij b_j,        a_i,b_j>0.              (10)

Positive diagonal scaling preserves PSD rank and ordinary rank of the entrywise nonnegative square root. In particular sqrt(q)=diag(sqrt a) sqrt(q0) diag(sqrt b) still has rank at most D.

### 5.2 Quantitative error and no cost for marginal preservation

The scaling relation implies the exact entropy identity

    D_KL(p||q0)=D_KL(p||q)+D_KL(q||q0),               (11)

because log(q_ij/q0_ij) is a sum of a row and a column term and p,q have identical marginals.

On the other hand,

    D_KL(p||q0)=log(1+e_bar)-sum_ij p_ij log(1+e_ij).

The second derivative magnitude of log(1+x) on [0,eps] is at most one. Taylor expansion about e_bar, followed by expectation, bounds this Jensen gap by Var_p(e)/2<=eps^2/8. Therefore

    D_KL(p||q)<=eps^2/8,
    TV(p,q)<=eps/4.                                   (12)

For completeness the last inequality uses Pinsker in natural logarithms: log-sum reduces relative entropy to the two-event partition where p>q, and the binary relative entropy has second derivative at least four, giving D_KL>=2 TV^2.

The pure normalized state sum_ij sqrt(q_ij)|i>|j> has Schmidt rank rank(sqrt q)<=D. Its Schmidt decomposition and local isometries therefore give a no-communication generation of q from local Hilbert spaces of dimension at most D, with local measurements allowed to have the original output alphabets. This uses no additional uncounted shared randomness.

For fixed K and fixed TV tolerance, at most O(log r) qubits per party suffice. For the exact-hard family in 22, exact generation requires Omega(r) local qubits. Thus exact versus approximate generation differs exponentially in local Hilbert dimension, even with EXACT preservation of both marginals.

These are dimension/existence statements. Exact marginal-scaling parameters or state vectors may be irrational; no exact rational state-preparation or uniform circuit-runtime claim is made. This operational upper bound is not a lower bound for approximate generation.

## 6. Why geometric approximation can nevertheless remain exponentially hard

Free entrywise approximation of a slack matrix is not the same as approximating a convex body. The missing condition is that every row still be an affine slack vector for the SAME set of supporting normals.

Use the body C_n from 21 and the rational samples of 22. Put

    epsilon_star=2^(-19), eta=2^(-24)=epsilon_star/32,
    x_i'=(1-eta)x_i, y_j'=(1-eta)y_j,
    S_ij=1-y_j'.x_i'.

The original x_i form an eta-net of C_n, the y_j an eta-net of C_n^polar, and B_2 subset C_n subset 2B_2. The shrunk y_j' form a 2eta-net of the polar, with zero interior to their convex hull. We have rank S=n+1 and eta<=S_ij<=3.

Define the fixed affine slack space

    V_Y={ (1-y_j'.z)_j : z in R^n }.

For this data, define the affine-compatible eta-approximate PSD rank as the least PSD rank of a nonnegative table T such that

    ||T-S||_max<=eta,
    every row of T belongs V_Y.                        (13)

**Theorem B (affine-compatibility separation).** The free eta-approximate PSD rank of S is polynomial in n, but its affine-compatible eta-approximate PSD rank is greater than floor(2^(n/4)). The constants and entrywise tolerance are fixed, independent of n.

### 6.1 Free approximations are polynomial

Normalize S by eta. Its entries lie in [1,K_star] with K_star=3/eta. Apply Theorem A with relative tolerance 1/K_star. Multiplying back by eta gives absolute error at most eta. Its factor order is at most

    binom(n+1+t0,t0),
    t0=ceil(K_star log(4K_star^(3/2))),

where t0 is a fixed absolute integer. This is polynomial in n; no small practical degree is claimed.

### 6.2 Exact row-affine compatibility forces geometric approximation

Suppose T meets (13) and T_ij=1-y_j'.z_i. For w=z_i-x_i', the error bound gives |y_j'.w|<=eta for all j. For w nonzero, the polar contains w/(2||w||), and some y_j' is within 2eta of this vector. Hence

    eta >= (1/2-2eta)||w||,
    ||z_i-x_i'|| <= 3eta.                             (14)

Every point of C_n lies within 3eta of some x_i' and hence within 6eta of some z_i. Also conv{z_i} is full dimensional and contains zero in its interior. Indeed for each unit u its support function is at least

    (1-eta)(h_Cn(u)-eta)-3eta >= 1-5eta>0.

Suppose T has an order-d PSD factorization T_ij=tr(A_i B_j). Put

    Q={z:y_j'.z<=1 for every j}.

Choose positive weights lambda_j summing to one with sum_j lambda_j y_j'=0. Compress the dual factors to the span of their ranges. Then sum_j lambda_j B_j is positive definite on that span, and

    K={z:exists Z>=0, tr(B_j Z)=1-y_j'.z for every j}

is a compact full-dimensional convex body with an order-at-most-d lift. It contains every z_i and is contained in Q. Compactness follows by summing the equations: the positive definite weighted trace of Z equals one; Q is bounded since the normals surround zero.

The outer-net estimate of 22, reproduced here, gives dist(z,C_n)<16eta for z in Q. First a net point near z/(2||z||) gives ||z||<=2/(1-4eta). For any y in the polar choose y_j' within 2eta, obtaining y.z<=1+2eta||z||. Therefore z/(1+2eta||z||) belongs C_n, and

    dist(z,C_n)<=2eta||z||^2/(1+2eta||z||)<16eta.

Combining the inner and outer estimates gives

    d_H(K,C_n)<=16eta=epsilon_star/2.

The body lower bound in 21 forces d>floor(2^(n/4)). This proves Theorem B.

### 6.3 No universal polynomial-size affine repair

Consequently there is no theorem that converts arbitrary free eta-approximate slack factors of order d into affine-compatible eta-approximate factors of order polynomial in n,d, valid for all these bounded rational slack tables. On the displayed family the input order is polynomial in n, while every valid repaired output has exponential order. The claim concerns OUTPUT SIZE, not merely the difficulty of finding a repair.

This does not contradict finite slack characterization, which requires exact pairings, or geometric robustness of the bodies. It explains why the bounded-entry approximation theorem cannot by itself yield a small geometric lift: tiny entrywise errors can violate essential affine dependencies among many supporting inequalities.

Preserving just probability marginals in Section 5 is possible by diagonal scaling. Preserving all geometric slack relations in Section 6 is a genuinely stronger requirement and can have exponential cost.

## 7. Exact scope of completion

Resolved here:

- Exponential exact PSD rank in a fixed positive entry window CANNOT persist at any fixed positive relative error; an explicit rational feature construction proves this for all matrices.
- Subexponential inverse accuracy cannot force exponential approximate PSD rank; equation (8) quantifies the necessary precision.
- Approximate correlations can preserve both marginals with the same polynomial dimension and controlled relative entropy.
- Combining the preceding result with the inherited smooth-body lower bound yields a rigorous exponential separation between free approximate factors and affine-compatible approximate factors.

Not resolved here:

- The optimal polynomial dependence of approximate PSD rank on r,K,eps.
- The exact precision threshold for the existential family of 22.
- An efficiently generated, polynomial-description family attaining the previous exponential exact lower bound or smooth-body lower bound.
- Efficient general SDP extension complexity, a named broad complexity conjecture, or a generalist journal's significance/acceptance question.

The qualitative low-rank approximation conclusion was already proved by Barvinok. The proof and quantitative consequences above are not a claim to have newly settled that classical theorem. The larger programme should not be labelled fully solved on the strength of this continuation.
