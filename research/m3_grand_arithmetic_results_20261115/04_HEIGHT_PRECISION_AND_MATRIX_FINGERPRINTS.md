# Checkpoint 04 — coefficient height, one-query matrix fingerprints, and measurement precision

Date: 2026-11-15. This is a proved matrix-IDENTIFICATION theorem. It is not a lower bound for approximate linear-system solution or for the unresolved rational conic OPTIMIZATION problem. Positional encoding and response counting are classical ingredients; priority for the precise synthesis is not certified.

## 1. Information model

An unknown matrix A is queried at any finite v in R^d. The response is

   Y=A v+e,   ||e||_2 <= zeta(1+||v||_2).

The error may depend on A and v. Computation and query magnitude are uncharged. Only this matrix-vector measurement is supplied: an additional exact quadratic value or a complete matrix description is not allowed. Identification means recovering A exactly, not merely returning an approximate solution of one linear system.

A one-query randomized rule chooses v from its independent seed, then decodes Y. All lower distributions below are fixed before that seed. The adversarial oracles used in the proofs are deterministic functions of A and v and satisfy the error bound for every query.

## 2. Integer matrices: upper and lower precision bounds

Let I_(d,H) be all d-by-d integer matrices with entries in {0,...,H}, H>=1.

THEOREM A (sufficiency). There is a rational query of norm less than 2 and coordinate encoding length O(d log(H+1)) such that EVERY A in I_(d,H) is recovered from one measurement whenever

   zeta <= (2H+2)^(-(d-1))/24.                         (1)

THEOREM B (necessity under a fixed prior). Under the uniform distribution on I_(d,H), there is an admissible deterministic measurement oracle for which EVERY randomized one-query identification rule has success probability at most

   min{1, (3+Hd/zeta)^d / (H+1)^(d^2)}                (2)

for zeta>0. Consequently success probability at least 2/3 requires, whenever the displayed denominator is positive,

   zeta <= Hd / [(2/3)^(1/d)(H+1)^d-3].               (3)

The logarithms of these explicit bounds agree to order d log(H+1), in the nontrivial large-d or large-H regime. The explicit formulas, rather than an asymptotic assertion at d=1, are the primary statements.

### Proof of Theorem A

Put B=2H+2 and v=(1,B^-1,...,B^(-(d-1))). Its norm is at most (1-B^-2)^-1/2<2. Let c,c' be distinct candidate rows. At their first differing coordinate j, numbered from zero, the integer difference has magnitude at least one. The remaining tail has magnitude at most

   H sum_(k>j) B^-k <= [H/(B-1)] B^-j < B^-j/2.

Therefore

   |(c-c')v| >= B^(-(d-1))/2.

Each observed coordinate has error at most zeta(1+||v||)<3zeta. Under (1), twice this error is strictly below the separation just proved. Exhaustive comparison with the finite row list therefore determines every row uniquely. This is a finite exact-decoding algorithm, not a claim of efficient arithmetic on the entire candidate list.

### Proof of Theorem B

Let r=||v|| and h=2zeta/sqrt(d). For each A, define the fixed oracle

   Y_A(v)=(1+r) h round( A v / [(1+r)h] ),

where rounding is coordinatewise to the nearest integer with a fixed tie rule. Each coordinate error is at most (1+r)h/2; hence the vector error is at most zeta(1+r), as required.

Every normalized exact coordinate lies in [-H sqrt(d),H sqrt(d)], by Cauchy--Schwarz. Thus each rounded coordinate has at most 3+Hd/zeta possible values, and at a FIXED query v the full reply has at most (3+Hd/zeta)^d possible values. The scale (1+r)h is known to the algorithm and does not increase this count.

For each fixed algorithm seed, a decoder can be correct on at most one matrix for each distinct reply. The uniform prior has (H+1)^(d^2) matrices. This proves (2) for every seed and then for independent randomization by averaging. Rearranging the condition that (2) be at least 2/3 gives (3).

This proof is uniform over arbitrarily large or algebraically complicated v. Increasing ||v|| cannot evade the input-relative error normalization.

## 3. The same phenomenon for well-conditioned symmetric positive definite matrices

Let S_(d,H) consist of

   A=I+B/(2dH),

where B is symmetric and its d(d+1)/2 independent upper-triangular entries are chosen freely from {0,...,H}. Since ||B||_op<=||B||_F<=dH, every A has eigenvalues in [1/2,3/2] and condition number at most 3. The matrices have rational entries with O(log(dH+1)) bits per coefficient.

THEOREM C. One rational bounded-norm query recovers every member in the measurement model whenever

   zeta <= (2H+2)^(-(d-1))/(48dH).                    (4)

Conversely, under the fixed uniform prior on S_(d,H), an admissible deterministic oracle bounds every randomized one-query success probability by

   min{1, (3+1/(2zeta))^d / (H+1)^(d(d+1)/2)}.        (5)

In particular, whenever the denominator is positive, success at least 2/3 requires

   zeta <= 1 / {2[(2/3)^(1/d)(H+1)^((d+1)/2)-3]}.     (6)

Thus measurement precision of order d log(H+1) bits is necessary and sufficient up to fixed multiplicative constants in the growing regimes, even though all matrices are uniformly well-conditioned. Exact identification is a different task from solving one well-conditioned system approximately.

Proof of sufficiency: subtract the known v and multiply the reply by 2dH. The resulting observation of Bv has input-relative error level 2dH zeta. Apply Theorem A; symmetry only reduces the candidate list.

Proof of necessity: subtract v in defining the rounding oracle and round the normalized unknown part (A-I)v/(1+r). Each coordinate is bounded by 1/(2sqrt(d)), since the corresponding row of B has norm at most H sqrt(d). Rounding on the same mesh h=2zeta/sqrt(d) leaves at most 3+1/(2zeta) possibilities per coordinate. Add the known v back to the answer. The vector error remains admissible. There are (H+1)^(d(d+1)/2) equally likely symmetric matrices; the same per-seed counting argument proves (5), and rearrangement gives (6).

## 4. Rational entries and unbounded-height exact arithmetic

A comparable sufficiency statement holds when each row entry is a rational p/q with |p|<=H and 1<=q<=H. Distinct entries differ by at least H^-2; row-coordinate differences are at most 2H. Use B=8H^3+2 in the same positional query. At the first differing digit, the tail is at most [2H/(B-1)] times its weight, below half the leading difference. Therefore the row separation is at least

   (1/(2H^2)) B^(-(d-1)).

The same decoding proof works, for example, under

   zeta <= B^(-(d-1))/(24H^2).

This establishes an O(d log(H+1)) sufficient precision budget. The integer subclass supplies a matching order obstruction for one-query exact identification, up to constants. No sharper leading constant for all rational denominators is asserted.

At zeta=0, a HEIGHT-INDEPENDENT algebraic query also works for arbitrary rational rows: alpha=2^(1/(d+1)) and v=(alpha,...,alpha^d), or any nonzero rational scaling thereof. Rational linear independence of 1,alpha,...,alpha^d gives injectivity, and rational enumeration with exact equality tests decodes the rows. The supplied model permits this; it does not make the decoding polynomial-time.

## 5. A finite-family continuity fact and the noncommuting limits

For any FIXED finite known family of distinct rational matrices, choose a bounded algebraic query separating every pair. Its minimum pairwise response distance Delta is strictly positive. Any error bound satisfying

   2zeta(1+||v||)<Delta

still allows unique nearest-response decoding from one query. Thus there is no discontinuity at zero error for a fixed finite separable family.

The old conic checkpoint 11 is different: its hard rational prior changes as zeta decreases, and its coefficient height is allowed to grow with log(1/zeta). The existence of that moving family cannot be read as a theorem uniform over one fixed finite list of bounded-height inputs. Equations (1)--(6) quantify this height/precision distinction for a recognizable matrix-recovery problem, but do not themselves establish a conic optimization phase diagram.

## 6. Limits of the consequence

These results concern exact matrix IDENTIFICATION from one vector measurement with adversarial input-relative norm error. They neither lower-bound approximate Ax=b solution, nor establish the original rational conic sequential term, nor describe the rounding law of a particular numerical eigensolver. The strongly conditioned example shows why numerical conditioning and exact information encoding are separate quantities.

The main rational exact-conic OPTIMIZATION frontier, including rank-changing inactive branches and matching arbitrary-query randomized bounds, remains unresolved.