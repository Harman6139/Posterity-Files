# Dense quadratic two-basis PSD universality — Track 02

Research branch: laa-track02-quadratic-dense-20261108 (2026-11-07/08).

## Verified mathematical contributions

1. An explicit single-copy two-basis representation of every normalized PSD measurement space of codimension one, in order N <= m^2+4m+2, with rank amplification exactly one. The construction uses a deterministic sparse-grid parameterization of the isotropic quadric, positive Parseval frame sparsification, and a quantitative exposing certificate.
2. The same dimension bound for block-graph operator systems: independent local trace-zero quadratic constraints on orthogonal blocks together with arbitrary cross-block measurements on a prescribed graph. This includes genuinely noncommuting annihilators and dense conjugates.
3. A different quadratic construction for every measurement space with commuting annihilator, N <= 4m^2+8m+5, rank amplification at most m+1, using finite-field Sidon sign frames and a Hadamard/Naimark enlargement. The auxiliary block is (tr X) I, not a fixed identity, so the zero target stays rank one and Lipschitz.
4. A two-coordinate equal-weight rotation producing non-reflection, genuinely different two-basis measurements while preserving the same exposing certificate.
5. A codimension-two counterexample showing that no unassisted rank-one compression is universal beyond codimension one: rank-one allowable projectors fail even to span the positive trace matrix.

All results concern real symmetric PSD matrices, arbitrary-rank ambient competitors, and feasible-set moduli including non-singleton fibres. The unrestricted arbitrary-noncommuting quadratic-size conjecture remains unresolved; the previous deterministic O(m^4) width-adaptive universality remains the general fallback.

See QUADRATIC_DENSE_THEOREMS.md for proofs and quantified constants, and AUDIT_README.md for reproducible numerical checks. The proofs are self-audited, not externally peer reviewed.

## Provenance

Research Track 02 is defined at prompts/laa_two_basis_significance_20261107/02_UNIVERSAL_STABILITY_TRANSFER.md in the parent branch. Earlier tensor and width-adaptive developments exist in the same research conversation; their claims are not silently upgraded to these new theorems. This branch leaves the original research brief untouched.
