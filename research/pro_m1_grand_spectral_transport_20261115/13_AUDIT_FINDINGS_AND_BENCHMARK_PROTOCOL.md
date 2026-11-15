# Checkpoint 13 — independent audit findings and predeclared benchmark protocol

Date: 2026-11-15. This continuation has independently derived all four weighted Riccati equations from the unscaled reflected matrix, checked the seven-variable implicit Jacobian, and verified the first nonzero rotation, radial, small-eigenvalue, and asymmetric-filter coefficients exactly with SymPy. Separate 90-decimal tests of the actual Frobenius affine projection and PSD projection cover 16 phases at each of t=1/100, 1/1000, 1/10000. They corroborate the predicted extra t^2 remainder and the exact cut identity; they are not the infinite-time proof.

## Correction to Checkpoint 09

The expanded seven polynomial equations have term counts [14,22,22,19,19,19,19], totaling 134, not the reported 154. Their total degrees are [8,6,6,6,5,6,6] and maximum coefficient magnitude is 4/3. Thus the loose envelope of at most 500 terms, degree at most 8, and coefficient magnitude at most 1000 used by the analytic bound is unaffected. The original symbolic script did not contain this term-count check; the independent script supplied in this continuation does.

The exact chart determinant is, up to sign,

  b^2 (1+b)^2 (4Cb-16Gb+12H^2-3b)/6
   =2b^3(1+b)^2[2c-C+H^2/b-1/4], c=2(C-G)/3.

At the reference point the final factor is 1/8. The derived filter is

  Delta j/tau = -9sqrt(3)j/8 -9xi^2 -(3sqrt(3)/4)xi eta +O(tau).

The trapping proof is analytic: a fixed compact spectral chamber, strictly contracting fast variables, stable slow filters, then inward amplitude and charge bounds. The uniform hierarchy and explicit-witness envelope are retained as substantive proof obligations, not replaced by these computations. No claim about the original gamma=1 switching orbit is inferred.

## Published-paper comparison: protocol fixed before sampling

Venues: Advances in Nonlinear Analysis (ANA), and Bulletin of the London Mathematical Society (BLMS).

Primary sample: the first five items labeled original research (excluding surveys, corrections, editorials, and issue information) in each of two publisher tables of contents: ANA volume 13 issue 1 (2024) and volume 14 issue 1 (2025); BLMS volume 56 issue 1 (2024) and volume 57 issue 1 (2025). The publisher display order at retrieval will be recorded. The sample is ten research papers per venue and is not chosen for similarity to this project.

If a publisher table is unavailable, retain the missing-access entry rather than silently replacing it with an attractive paper. Closest-topic papers may be added separately, clearly outside the ten-paper sample. Full statements and proofs will be inspected where accessible; inaccessible proofs will be marked, not scored as if read.

Each paper is compared on five 0–5 dimensions: theorem novelty N, proof depth D, scope/generalizability G, likely mathematical reuse R, and exposition C. The predeclared substance composite is .25N+.25D+.20G+.15R+.15C. Audience fit F is scored separately and is not used to inflate substance. Scores are qualitative assessments, not measurements; uncertainty intervals and cross-subfield comparison limits must be reported. A superiority count is defensible only when correctness and priority gates pass and the evidence supports the comparison. No automatic 8/10 count will be inferred from the ambition of the theorem.

The proposed manuscript may be described as a credible upper-quintile contribution only if at least 8/10 comparisons at a venue support that assessment without failed correctness/priority gates. This is not an acceptance probability. Submission-to-acceptance timing, if reported, will use actual dates with sample sizes and will explicitly include revision time; otherwise it remains unverified.
