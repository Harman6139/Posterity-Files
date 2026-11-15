# Checkpoint 08 — a rational conic randomized frontier with charged query excursions

This checkpoint proves a different, explicitly charged information model. It does NOT assert that the handoff's free-radius exact-oracle conjecture is false, or that it has been resolved. The distinction is essential.

## 1. Model and theorem

Fix a positive rational beta. Fix common constants c_beta,C_beta,s_beta supplied below, and let C_beta be the class, over all dimensions, of rational affine PSD pencils with Frobenius-orthonormal coordinate directions, genuine weak infeasibility, f(0)<=1, and

    c_beta s^-beta <= rho_f(s) <= C_beta s^-beta, 0<s<=s_beta,
    f(q)=dist_F(X0+Hq,S_+)^2/2.

Only exact natural values and coordinate gradients are supplied. The matrix coefficients are hidden. Queries and outputs may be arbitrary finite real vectors. Computation is unrestricted and algorithms are measurable. At requested objective accuracy epsilon, charge a query at q the amount

    w_epsilon(q)=1+epsilon^(2beta)||q||^2.

The total cost is the sum of these charges. Output locations are not charged. This is an excursion/actuation-energy information model relative to the natural escape radius epsilon^-beta. It is NOT ordinary query counting, a bit-complexity model, or a claim that arithmetic cost is quadratic in magnitude. It explicitly prevents arbitrarily large measurement excursions from being free while retaining ordinary unit-cost behavior inside a constant multiple of the comparator radius.

THEOREM. For sufficiently small epsilon, the randomized dimension-uniform minimax cost for a fixed success probability 2/3 is

    Theta_beta(epsilon^(-beta-1/2)).

The upper bound uses projected accelerated natural gradients. The lower bound uses a fixed finite distribution over rational weakly infeasible PSD pencils, sampled before the algorithm's seed. Matrix order, dimension and rational description length are polynomial in the horizon. No generic SDP epigraph compiler is used.

An equivalent horizon statement, with explicit construction and proof, follows. The relation between the horizon-normalized charge and w_epsilon is justified in Section 7.

## 2. Weighted hinge chain and rational natural pencil

Set

    theta=2/(2beta+1), nu=2-theta in (0,2),
    t=(1-theta)/2 in (-1/2,1/2),
    sigma_i=2^floor(t log_2 i), q_i=sigma_i/sigma_(i+1).

Thus (1/2)i^t<sigma_i<=i^t and q_i is in {1/2,1,2}. For fixed rational beta, these dyadic numbers can be determined by exact integer comparisons. Fix a=1/16 and c0=a^2/2=1/512.

For a horizon T>=1 choose N=4(T+1), gamma=1/(32N^2), and

    R_N=max(1,ceil(sqrt(sum_(i=1)^N sigma_i^2))),
    M=2 ceil(sqrt(T)) R_N,
    d=T+ceil(2^24 N^5 T R_N^2).

Draw an ordered injection p=(p_1,...,p_N) uniformly from {1,...,d}, before algorithm randomness. Write v_i=x_(p_i) and define

    h_p(x)=c0[(v_1-1)^2+
                 sum_(i=1)^(N-1)(|v_i-q_i v_(i+1)|-gamma)_+^2].

Let B_p have first row e_(p_1)^T and subsequent rows e_(p_i)^T-q_i e_(p_(i+1))^T. Put A_p=a^2 B_p^T B_p and P_p=I/2-A_p. The elementary bound ||B_p x||^2<=10||x||^2 gives

    0<=A_p<=10/256 I,       I/4 <= P_p <= I/2.

Choose a rational Gram factor S_p^T S_p=P_p. Its existence and polynomial encoding are explained below. Let g_beta(y) be the fixed rational isometric conic tail constructed in checkpoint 05, with g_beta(0)=1/2 and rho_g(s) comparable to s^-beta.

The natural pencil consists of:

* the 2x2 block [[0,a(v_1-1)],[a(v_1-1),0]];
* for each i<N, two scalar blocks a[gamma-(v_i-q_i v_(i+1))] and a[gamma+(v_i-q_i v_(i+1))];
* the padding arrow [[M,(S_p x)^T],[S_p x,M I]];
* the fixed tail pencil for g_beta.

Spectral clipping gives the EXACT objective

    f_p(x,y)=h_p(x)+(sqrt(x^T P_p x)-M)_+^2/2+g_beta(y).       (1)

The direction Gram matrix in the first two groups is 2A_p. The padding contributes 2P_p=I-2A_p, and the tail directions have disjoint support and unit Gram matrix. Hence the full affine coordinates are orthonormal. In particular f_p is convex C1 and 1-smooth.

At v_i=sigma_i all hinge and anchor terms vanish. The vector has norm <=R_N, so its padding vanishes. Letting the tail approach the cone proves zero distance, while the tail forbids exact PSD feasibility. Every sample is genuinely weakly infeasible. Also f_p(0)=c0+1/2<1.

## 3. Uniform escape geometry at ALL small scales

The tail gives rho_f(s)>=rho_g(s), hence the uniform lower profile. For the upper bound compare h_p with the quadratic chain

    Q_p(x)=c0[(v_1-1)^2+sum_(i<N)(v_i-q_i v_(i+1))^2].

Always h_p<=Q_p. On a prefix of length k<N the minimum of Q_p is c0/D_k, where

    D_k=1+sum_(i=1)^k sigma_i^-2.

This is weighted Cauchy--Schwarz applied to the drops of v_i/sigma_i between the boundary values 1 and 0. The minimizing prefix satisfies |v_i|<=sigma_i. Elementary power sums give

    (1/4)k^theta<=D_k<=(1+4/theta)(k+1)^theta,
    sum_(i=1)^k sigma_i^2<=(k+1)^nu/nu.                 (2)

For any small s, take k of order s^(-1/theta); if k>=N use the exact zero sigma instead. The resulting x has h_p(x)<=s/2 and norm <=K_beta s^(-beta). Its norm is also at most R_N, so the padding is identically zero. Combine it with a fixed tail comparator at s/2. This proves common constants and a common onset

    c_beta s^-beta<=rho_f_p(s)<=C_beta s^-beta

independent of T,d,p. The proof works on the whole interval 0<s<=s_beta, not only at the horizon scale.

## 4. Fixed-distribution locality under a charged budget

Consider any randomized adaptive algorithm whose pathwise cost is at most T under the horizon charge

    w_N(x,y)=1+(||x||^2+||y||^2)/R_N^2.                 (3)

It makes at most T queries and sum_j ||x_j||^2<=T R_N^2. Every individual query satisfies

    sqrt(x_j^T P_p x_j)<=||x_j||/sqrt(2)
                       <=sqrt(T/2)R_N<M,

so the padding is zero, including its gradient, for EVERY possible sample p. This observation is why M grows with the permitted excursion budget. Choosing M merely of order R_N would NOT prove an energy-charged lower bound: a single larger query could expose the hidden Gram matrix at constant charged cost.

Use a reference process which, at reply j, grants the next index p_j for free and answers with the chain truncated after the edge from p_(j-1) to p_j (at j=1 only the anchor). Its query before reply j depends only on the random seed and p_1,...,p_(j-1). If all coordinates at still-unrevealed indices obey |x_(p_i)|<=gamma/4 for i>=j, then every omitted link is exactly inactive, since q_i<=2 implies |v_i-q_i v_(i+1)|<=3gamma/4. Thus the reference value and full gradient coincide EXACTLY with (1). No tiny nonzero signal is discarded.

For a deterministic x, at most 16||x||^2/gamma^2 coordinates exceed gamma/4 in magnitude. Conditionally on the reference prefix, the remaining indices are a uniform ordered sample without replacement. Therefore the probability that some unrevealed coordinate is large at reference query j is at most

    16N ||x_j||^2/[gamma^2(d-T)].                       (4)

This is an unconditional reference-process coupling argument; it does NOT incorrectly condition a Haar/discrete distribution on prior good events. On the intersection of the reference good events, induction identifies the actual and reference transcripts.

## 5. Arbitrary unqueried outputs

Let the reference output be (x_hat,y_hat). The padding bound P_p>=I/4 implies that f_p(x_hat,y_hat)<=1 entails

    ||x_hat||<=2(M+sqrt(2))<=3M+2.

For convenience use B_out=4M, valid since M>=2. If ||x_hat||>B_out, the objective already exceeds 1 and therefore exceeds the lower target. Otherwise, apply the same conditional counting argument to the unqueried output and the remaining indices. Since M<=4sqrt(T)R_N,

    B_out^2=16M^2<=256 T R_N^2.

Combining all queries and this bounded output, the union bound is at most

    16N [T R_N^2+256T R_N^2]/[gamma^2(d-T)]
      <= (16*257*1024)/2^24
      =257/1024 <1/3.                                 (5)

If an output exceeds B_out, replace it by zero solely for defining the output good event; actual failure is then already guaranteed. This makes the event bound valid without assuming an output-radius restriction. Algorithms are taken to enforce their cost budget on all transcripts; truncation at the budget supplies this convention without loss.

On the good event, |v_(T+1)|<=gamma/4. Put

    e_0=|1-v_1|,
    e_i=(|v_i-q_i v_(i+1)|-gamma)_+, 1<=i<=T.

Telescoping the normalized coordinates v_i/sigma_i and using weighted Cauchy--Schwarz gives

    1-|v_(T+1)|/sigma_(T+1)
       <=gamma sum_(i=1)^T sigma_i^-1
          +sqrt(D_T)*sqrt(e_0^2+sum_(i=1)^T e_i^2).

Since sigma_i^-1<=2sqrt(N), our gamma makes the two terms subtracted from 1 have sum less than 1/2. Hence

    h_p(x_hat)>=c0/(4D_T)
       >= c0/[4(1+4/theta)] (T+1)^(-theta).             (6)

All other objective terms are nonnegative. With

    epsilon_T=c0/[8(1+4/theta)] (T+1)^(-theta),

(5)--(6) prove

    Pr_{p,algorithm}{f_p(output)>epsilon_T} >=767/1024>2/3.   (7)

The distribution is fixed before the seed; the proof permits arbitrary measurable adaptive computations, arbitrary finite queries subject only to the charged budget, and arbitrary unqueried outputs.

## 6. Size, rationality and encoding

Here R_N=Theta_beta(N^(nu/2)), so d=O_beta(T^(6+nu)), with 0<nu<2. The scalar-hinge groups have order 2N. A rational Gram factor of P_p can be taken with at most 4d rows, so total PSD order is at most 4d+2N+1+m_beta. Both dimensions are polynomial in T.

Rationality does not rely on approximating Haar frames: the hidden information is an exactly uniform ordered subset of coordinate axes. After permuting these axes, P_p is a rational tridiagonal N-by-N block and a diagonal complement. Rational LDL elimination of the tridiagonal block has numerator and denominator bit lengths O(N+log N), because its entries have fixed bounded dyadic denominators and its positive principal minors are determinants of this bounded tridiagonal matrix. Expanding each positive rational pivot into four rational squares gives a rational Gram factor with polynomial bit length. The diagonal complement 1/2 is represented by two entries 1/2, since 1/4+1/4=1/2. The offsets M,gamma and dyadic weights have O_beta(log T) bits. Thus the entire sparse rational description has polynomial length; no efficiency claim for a particular four-square search algorithm is required to prove the encoding bound.

## 7. Matching upper bound and conversion of charges

For the normalized class, take a comparator u with f(u)<=epsilon/2 and ||u||<=C_beta(epsilon/2)^-beta. Work on the known Euclidean ball of that radius. Projected accelerated gradient, with one natural conic gradient per iteration, gives

    f(x_K)<=f(u)+2||u||^2/(K+1)^2.

Thus K=O_beta(epsilon^(-beta-1/2)) suffices. Every query is a convex combination of points in that ball, and therefore has w_epsilon cost O_beta(1). Total charged cost has the asserted upper order.

For (7), R_N=Theta_beta((T+1)^(nu/2)) and epsilon_T^-beta=Theta_beta((T+1)^(beta theta)). Since nu/2=beta theta, the two charges w_N and w_epsilon_T are comparable by constants depending only on beta. Therefore a sufficiently small constant times T of w_epsilon_T-cost implies at most T of w_N-cost and is excluded by (7). Choosing the integer horizon to make epsilon_T comparable to a requested epsilon proves the lower order epsilon^(-beta-1/2). This is a cost theorem, not an uncharged query theorem.

## 8. Noise and systematic bias in this charged model

The rational Gaussian/testing carriers of checkpoints 01--06 belong to the same profile class after enlarging its fixed constants if necessary. Their indistinguishability bounds survive arbitrary query magnitudes. Their samples can be taken at the origin, where the charge is one. The exact-oracle lower term (7) remains a lower bound for a weaker gradient-only stochastic oracle, because zero noise is admissible under an upper variance budget. Combining the two hard families gives the minimax lower order

    epsilon^(-beta-1/2)+sigma^2 epsilon^(-2beta-2).

The projected accelerated stochastic upper bound from source milestone 39, reproduced in the eventual standalone paper, stays in the comparator ball, and so its sample and charged costs differ by a beta-dependent constant. Under absolute gradient bias nu_bias<=c_beta epsilon^(beta+1), it achieves the same sum. The carrier proves impossibility for nu_bias>=C_beta epsilon^(beta+1).

Thus the full sequential/variance/bias power frontier is matching in THIS radius-charged, measured-coordinate-gradient model. Exact population values are not included in the stochastic lower experiment. The variance lower bound has the 2/3 failure form via the three-sign construction in checkpoint 06; expected-error and fixed-confidence statements must use the corresponding upper guarantee (Markov amplification at a constant smaller target suffices at fixed confidence).

## 9. What this does not settle

Free-radius query complexity is a different model. The padding is inactive precisely because the declared cost bounds the largest allowed excursion. Large uncharged queries can activate it and disclose the hidden chain Gram matrix. Nothing here proves a universal negative statement about ALL rational conic objectives under free-radius exact access. The original handoff's rational exact-value/gradient frontier therefore remains open in this work.

The theorem is a direct natural-PSD-distance construction with an exact transcript proof, not a transfer from SDP epigraph universality. Its model, rationality, uniform profile and random-seed quantifiers are all explicit. Further work is required before any journal-percentile claim.
