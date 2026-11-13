# Latest continuation: exact versus noisy PSD complexity

Date: 2026-11-13. This supplements, and does not replace, 00_CURRENT_RESULTS.md through milestone 22.

Read **23_NOISE_BOUNDARY_AND_AFFINE_COMPATIBILITY.md** for the full proofs.
Proof commit: 379a7bb8e70082b7b7a68e3f75b7ec038962aed6.
Exact rational constructor: noise_boundary/rational_psd_approximation.py, committed at 748538c56a5e7c9b1b0d19d886f7e6bd17357ae2.

## Definitive answer to the fixed-noise strengthening

The exponential exact PSD-rank family of 22 CANNOT have an exponential lower bound at every fixed positive relative error. For every positive matrix M of rank r and entry ratio at most K, and 0<epsilon<=1, there is a rational construction when the data are rational, with

    M <= N <= (1+epsilon) M,
    psdrank(N) <= binom(r+t,t),
    t=ceil(K log(4 sqrt(K)/epsilon)).

The factors may all have rank one. For fixed K and epsilon this is polynomial in r. The qualitative polynomial-square approximation principle is already Barvinok's Theorem 5.1, arXiv:1204.0471; it is NOT a newly solved open theorem. Manuscript 23 gives an explicit one-sided relative estimate and its consequences.

If K is fixed and log(1/epsilon_r)=o(r), approximate PSD rank is exp(o(r)). Exponential approximate-rank lower bounds therefore require exponentially fine relative accuracy. This is a necessary condition, not a matching precision threshold.

## Operational consequence

Every positive rank-r probability table of bounded entry ratio has approximations with the SAME two marginals, local shared quantum dimension at most binom(r+t,t), relative entropy at most epsilon^2/8 and total variation at most epsilon/4. Marginal preservation uses positive diagonal scaling and does not increase the amplitude rank. For the family of 22, exact generation needs Omega(r) local qubits, while every fixed positive accuracy needs only O(log r). Exact scaling coefficients may be irrational; no circuit-preparation efficiency claim is made.

## Geometric consequence

For the smooth-body slack tables from 21–22, free entrywise approximations have polynomial PSD rank. However, approximations at the same fixed absolute tolerance that preserve the row-affine slack relations for the ORIGINAL supporting normals still require PSD order greater than floor(2^(n/4)). This proves a superpolynomial output-size obstruction to arbitrary polynomial-size affine repair. It explains why the free approximate-factor theorem does not contradict exponential Hausdorff approximation hardness.

## Exact status

The fixed-noise extension is ruled out with a complete proof, and the affine-compatibility separation follows from the inherited geometric lower bound. The optimal polynomial approximate-rank exponent, a sharp precision threshold, efficiently explicit exponentially hard families, and efficient general semidefinite extension complexity remain unproved here. No broad classical conjecture or the whole research programme is labelled fully solved.
