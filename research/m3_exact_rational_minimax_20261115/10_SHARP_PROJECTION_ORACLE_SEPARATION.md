# Checkpoint 10 — an exact, quantitative separation of conic oracle interfaces

Date: 2026-11-15. Continues checkpoint 09 and the rational family of checkpoints 01–02. This theorem measures the information lost by returning only a natural objective and its coordinate gradient instead of the PSD projection matrix. It does NOT close the dimension-growing power-law optimization frontier.

## 1. Same instances, two oracle interfaces

Use exactly the ordered rational pencils X_w(x,z) of checkpoint 01, indexed by w in {-1,+1}^n, with

    h=1/8, a=1/4, lambda=1/64, eta=1/4096,
    f_w(x,z)=H_w(x)+phi(z),
    epsilon_n=(5/384) eta^n.

Their matrix order is 24(n+1)+2 and they have two rational orthonormal affine coordinates. They are genuinely weakly infeasible and satisfy the SAME uniform beta=1/2 escape constants for all n and w. Fix, once and for all, nonnegative rational four-square representations of the six lower-reservoir weights. The upper factors and base factors are then fixed as in checkpoint 01. Rows remain in their specified depth/side/atom/factor order; the oracle does not hide an additional ambient conjugation.

Call the original oracle O_vg(q)=(f_w(q),grad f_w(q)). Call the matrix oracle O_P(q)=P_+(X_w(q)). Define the single target response

    C_w = O_P(2,0).                                   (1)

All statements below refer to exactly these SAME hidden rational pencils. No real coordinate chart, radius charge, positive error in O_vg, or epigraph representation is introduced.

## Theorem A — one projection versus an exact binomial number of value-gradient calls

One matrix-projection query, at the bounded rational point (2,0), identifies the entire hidden word w and hence permits optimization to every positive tolerance without another call.

In contrast, the best worst-case probability of producing the EXACT matrix C_w after T calls to O_vg is

    S(n,T)=2^(-n) sum_{j=0}^{min(T,n)} binom(n,j).       (2)

The same expression is the optimal average probability under the fixed uniform prior on w, independent of the algorithm's seed. Thus exact simulation with certainty requires n original calls; success probability at least 2/3 requires the corresponding binomial quantile, n/2+O(sqrt(n)). No constant number of original calls can simulate one projection reply uniformly in matrix order.

The lower bound includes arbitrary real query locations, unlimited exact computation, adaptivity, independent randomization, and arbitrary unqueried matrix outputs. It is an oracle-SIMULATION/identification separation. Its associated optimization lower bound remains the logarithmic-in-accuracy theorem of checkpoint 02, not the unresolved power law.

### 2. Explicit decoding of one full projection

All atom thresholds lie in [-1,1]. At x=2 every lower scalar entry b(2-t) is nonnegative, every upper entry b(t-2) is nonpositive, and all factors b are nonnegative. The projection therefore keeps the lower entries and sets the upper entries to zero. The known 2-by-2 W(0) projection is common to all words.

Suppose the first j signs are known, with 0<=j<n. Their prefix center is c and their spatial scale is h^j. The three lower-reservoir thresholds at the next node are

    t_i=c+h^j L_i, L=(-1,-3/4,-1/2),                  (3)

which are known before the next sign is learned. The four coefficient factors for that reservoir atom are h^j b_i^{w_{j+1}}, where

    ||b_i^-||^2=r_i^-(-a), ||b_i^+||^2=r_i^-(a).

Hence the corresponding four-entry vector in C_w is

    h^j (2-t_i) b_i^{w_{j+1}}.                       (4)

The squared norm of (4), divided by h^(2j)(2-t_i)^2, is the reservoir weight. For example the first atom has weights 2665/16384 and 2121/16384, which are different. This identifies the next sign. Update c to c+a h^j w_{j+1}, increment j, and repeat. All needed entries already belong to the single response C_w. The decoder uses only finitely many rational operations and exact comparisons. It does not need to reconstruct an eigenbasis of a hidden noncommuting block.

After all signs are recovered, choose x=c_w and z with phi(z)<epsilon. This is an approximate feasible point for every prescribed epsilon>0.

Notice that the original value and coordinate gradient AT THE SAME POINT (2,0) are independent of w, because every H_w has the same exterior quadratic there. The matrix entries retain atom-level information that summing negative eigenvalue squares and taking tangential contractions destroys.

### 3. Lower and upper simulation probabilities

The decoder above proves that w -> C_w is injective. Therefore any algorithm outputting the correct C_w also identifies w, by finite comparison with the known catalogue. Checkpoint 02 simulates every original value-gradient query by one stronger first-mismatch word query and proves the exact maximal word-identification probability (2). This applies even when the original algorithm returns an arbitrary real matrix not selected from the catalogue: equality with C_w still identifies w, while an output outside the catalogue is simply unsuccessful.

Conversely, the Q(sqrt(2)) natural-gradient probes of checkpoint 02 attain (2) for every fixed word. Having guessed a word, compute C for that candidate from its supplied template with no extra calls. This attains the same simulation success probability. The upper and lower bounds match, including the random-seed quantifiers. QED.

For a concrete horizon, let n=4(T+1). Then the best T-call simulation success is at most (T+1)/(T+2)^2<=1/4 by the elementary binomial variance estimate. Meanwhile the matrix oracle returns C_w in one call. The matrix order and binary description remain polynomial in T.

## Theorem B — the sharp measurement precision at this one projection query

Let

    delta_n = min_{w != v} ||C_w-C_v||_F.

There are fixed positive constants c,C, depending only on the chosen finite four-square representations and NOT on n, such that

    c h^(n-1) <= delta_n <= C h^(n-1).                (5)

Consequently the exact robust recovery threshold for an adversarial Frobenius error in the single response (1) is delta_n/2, in the following strict/closed sense:

* an error budget b<delta_n/2 permits deterministic recovery of every word by nearest-catalogue decoding;
* an error budget b>=delta_n/2 does not permit worst-case exact-word success greater than 1/2, because two closest candidates admit the same midpoint response.

The ambiguous midpoint is PSD, so this necessity remains valid even when the measurement must itself be PSD-valued. This is not an assertion about an unbiased projection sampler or any specified hardware rounding rule.

The order of the required absolute matrix accuracy is

    delta_n = Theta(8^(-n)) = Theta(epsilon_n^(1/4)).  (6)

It corresponds to 3n+O(1) binary accuracy bits, or (1/4)log_2(1/epsilon_n)+O(1). These statements concern exact identification of the depth-n label from this particular projection response, not a universal precision threshold for solving arbitrary SDPs.

### 4. Proof of the lower separation

For each i=1,2,3, put D_i=b_i^+-b_i^- and

    kappa0=(sum_i ||D_i||^2)^(1/2)>0.                (7)

Strict positivity follows already from the unequal first-atom squared norms; it does not require a specially engineered four-square representation.

Let two words first differ at position j, 1<=j<=n. They have the same prefix center and same thresholds t_i in their depth-(j-1) lower reservoir. Equation (4) gives a difference h^(j-1)(2-t_i)D_i in that row group. All t_i<=1, so 2-t_i>=1. The squared Frobenius norm of the entire projection difference is at least that of these disjoint diagonal rows. Therefore

    ||C_w-C_v||_F >= kappa0 h^(j-1)
                  >= kappa0 h^(n-1).                 (8)

Later rows cannot cancel these differences: they occupy distinct positions of a diagonal matrix.

### 5. Proof of the upper separation

Choose two words with the same first n-1 signs and opposite last signs. Every earlier reservoir row agrees. The three last lower-reservoir groups differ by at most

    3 kappa0 h^(n-1)

in Euclidean norm, since 2-t_i<=3. All upper rows are zero after projection. The base lower rows have the same factors h^n b_i^0 and their centers differ by 2a h^(n-1). Their total base weight before scaling is 1/2, so their squared difference is

    (1/2) h^(2n) (2a h^(n-1))^2
      = 2a^2 h^(4n-2).

The W projection agrees. Thus

    delta_n^2 <= 9 kappa0^2 h^(2n-2)+2a^2 h^(4n-2)
              <= (9 kappa0^2+2a^2) h^(2n-2).          (9)

Equations (8)–(9) prove (5). Nearest-neighbor balls of radius strictly less than half the minimum separation are disjoint. At half the separation, the midpoint of a closest pair lies in both closed error balls and is PSD. A randomized decoder receiving this common point cannot have success greater than 1/2 on both candidates. This proves the precision assertion. Finally eta=h^4 and epsilon_n=(5/384)h^(4n), giving (6). QED.

## 6. Significance and remaining scope

Checkpoint 09 proves universal two-query identification for a known finite family using full PSD projections. Theorem A explains quantitatively why that theorem cannot be invoked as a constant-call reduction in the original scalar/coordinate-gradient model: even one specified bounded projection query can require linearly many such calls in PSD order.

Theorem B also shows where finite matrix precision removes this particular exact-arithmetic shortcut. It is a response-separation calculation for genuinely rational conic instances, not the transfer of a generic Gaussian gradient-noise lower bound. The error specification and information returned are different from all previous gradient-bias models and have been kept distinct.

This does not establish the original dimension-growing Omega(epsilon^(-1)) query lower bound at beta=1/2. The family still has an exponential-in-T deterministic objective upper bound, as proved in checkpoint 04. No stronger minimax conclusion is inferred from the oracle-separation statement.

The first-mismatch counting in (2), rational four-square representations, and finite-code packing/nearest-neighbor arguments are established methods. The asserted contribution is their exact quantitative realization and comparison on the SAME normalized weakly infeasible rational pencils. A comprehensive independent priority assessment is not complete.
