# Milestone 36 — complete nullity-four depth-three spectrum except the universal square-root endpoint

**Proved 2026-11-08 for arbitrary dense uniquely recoverable real PSD problems, conditional on the prior complete dense fixed-nullity exponent catalogue and its sharp-flag theorem.**

Fix target rank r>=1, nullity nu=4, and **minimal** facial-reduction degree d=3. Then the exact spectrum satisfies
\[
\boxed{
S_{4,3}\subseteq\Sigma_{4,3}^{dense}\subseteq S_{4,3}\cup\{1/2\},
}
\]
where the *entire* non-square-root spectrum is
\[
\boxed{S_{4,3}=
\{1/8,1/6,3/16,1/5,3/14,1/4,3/10,1/3,
  5/14,3/8,2/5,3/7\}.}
\]
Every one of the twelve members occurs at **exact degree three** and target nullity four in the explicit sparse constructions (verified by exact-rational sparse peeling and full competitor bounds).

**Necessity:** the universal (nu=4) catalogue is the 22-element set in checkpoint 27; the depth d=3 Sturm lower bound excludes all exponents <1/8; Lipschitz exponent1 forces d=1; the newly proved dense theorem in checkpoint 35 excludes 1/7 because it forces d=4; the newly proved dense Gordan–Stiemke theorem in checkpoint 33 excludes 5/16, 5/12, 7/16 because each forces d=2. All other values in the universal candidate list lie in S_{4,3} except 1/2. No density or sparsity assumption is imposed on a hypothetical counterexample at the endpoint.

**Scope:** If the conjectural universal implication alpha=1/2=>d<=2 is established, this checkpoint immediately becomes a complete closed necessary-and-sufficient dense nullity-four degree-three classification. This endpoint implication remains a genuine missing theorem; we do not infer it from sparse enumeration, from Sturm's lower error bound, or from results on selected central paths.

## Fully settled additional ν4 strata
- d=1: {1,1/2};
- d=2: {1/4,5/16,1/3,3/8,5/12,7/16,1/2};
- d=4: {1/4,1/5,1/6,1/7,1/8,1/10,1/12,1/14,1/16}.
Only d=3 differs from an explicit arithmetic list by one potential endpoint 1/2.