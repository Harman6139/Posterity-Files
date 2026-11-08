# Universal PSD stability / joint exponent-depth research (2026-11-07)

**Current deliverables**
- [01_CANONICAL_GREEDY_DEPTH.md](01_CANONICAL_GREEDY_DEPTH.md): self-contained proof of the **previously known** maximal-rank/relative-interior stress method for minimal facial reduction; included to define a canonical depth test, not claimed novel.
- [02_ALL_DEPTHS_INTERIOR_REALIZATION.md](02_ALL_DEPTHS_INTERIOR_REALIZATION.md): explicit sparse PSD midpoint graphs realizing every rational \(2^{-d}\le\alpha<1/2\) with **exact** minimal singularity degree \(d\ge2\) in finite (not necessarily optimal) dimension; rank \(r\ge1\).
- [03_FINITE_JOINT_ALL_DEGREES_DECISION.md](03_FINITE_JOINT_ALL_DEGREES_DECISION.md): necessary-and-sufficient **finite real-algebraic** decision procedure for occurrence of every sharp exponent at fixed \((n,r,d)\), via finite weighted flags combined with the canonical depth predicate on the **same dense kernel**. Not a closed arithmetic formula and no efficient complexity claim.
- [04_EXACT_LADDER_CHECK.py](04_EXACT_LADDER_CHECK.py): exact-rational reproducibility test; no floating-point evidence used as proof.

## Results vs unresolved

**Proved in this packet** (conditional only on the previously proved weighted-flag structural theorem recorded in the parent project): a universal terminating decision algorithm for all fixed triples, and a new unrestricted-dimension all-depth constructive realization theorem below one-half.

**Not proved**: the stronger equivalence mapping each dense instance into a sparse midpoint network preserving exponent, nullity *and* exact minimal facial depth; a closed arithmetic/combinatorial formula for every fixed triple; optimal nullity for a general prescribed \((\alpha,d)\); and whether exponent exactly \(1/2\) is possible at \(d\ge3\). Do not infer absence from unsuccessful sparse search.

**Prior-art attribution**: maximal-rank greedy facial reduction is standard (see Sremac–Woerdeman–Wolkowicz, *Error Bounds and Singularity Degree in Semidefinite Programming*, SIAM J. Optim. 31 (2021), doi:10.1137/19M1289327; see also literature on relative-interior exposing vectors). Semialgebraic quantifier elimination, Puiseux selection and Sturm's depth error bound are also established, not novel.

**Safeguard**: these are research proofs requiring independent specialist review before declaring a journal-level new theorem or priority. The decision theorem avoids the unproved dense-to-sparse depth preservation, but uses exact-algebraic feasibility and therefore may be expensive.
## 2026-11-07: universal extremal structural breakthrough
- [05_UNIVERSAL_DYADIC_RIGIDITY.md](05_UNIVERSAL_DYADIC_RIGIDITY.md): universal feedback-cycle necessity for non-dyadic sharp exponents; extremal `alpha=2^(-nullity)` forces unique dyadic kernel-weight spine and maximal singularity degree; every odd-numerator dyadic `a/2^nu` has a **simultaneously dimension-minimal and facial-degree-minimal** explicit PSD realization, for arbitrary target rank.
- [06_DYADIC_BISECTION_CHECK.py](06_DYADIC_BISECTION_CHECK.py): exact Fraction construction and peeling audit (511 cases, nullity 2..10).
- These are structural results for **all dense kernels on the necessity side**, but they DO NOT prove the general sparse-network/dense-depth equivalence for every rational exponent. The endpoint alpha=1/2 at depth >=3 remains unresolved. No novelty claim is made for determinant combinatorics or generic facial reduction in isolation.
