# Proof and scope audit

Source theorem: `11ffd7fe0e83b7eda47459d1d9b90b7358a4fcfc`.
Production date: 2026-11-15, America/New_York.

Two independently scoped internal audits reconstructed the entire source proof.
Neither found a substantive mathematical error. The author-side production pass
also read every supplied proof line and both complete scripts. A final regression
pass checks the polished source separately. These are analytical internal checks,
not proof-assistant certification or independent human refereeing.

## Theorem crosswalk

| Polished statement | Original source | Checked dependency and boundary |
|---|---|---|
| Theorem 2.1 | Theorem 1.1 | Fixed integer n>=5, integer t>=1; ordinary CP cone; exact canonical start; every improving extreme ray; all three permitted exits |
| Corollary 2.2 | Final paragraph of original main theorem/proof | Reduced rational encodings; fixed-order constants; bottom entry gives matching lower bound on length; distance term controlled |
| Theorem 3.1 | Theorem 2.2 | Arbitrary positive definite fixed H; bounded edge only; common active pair; cross coordinates only, not all matrix entries |
| Lemma 3.2 | Lemma 2.1 | Zero support, changing support, arbitrary active y, Dirichlet nonnegativity, uniform finite neighborhood, degeneracy |
| Section 3.2 | Original Section 3, Lemma 2.3 | Interval basis; exact face; strict copositivity; full local polyhedrality; closed finite adjacent endpoint; exact recession cone |
| Lemma 4.1 | Lemma 4.1 | Five distinct cycle coordinates; eigenvalue margin; interval weights; Horn copositivity; denominator and norm bounds |
| Lemma 4.2 | Lemma 4.2 | Whole real symmetric closed ball; eigenvalue and entry reserves; common strict separator; distance lower bound |
| Lemma 5.1 | Lemma 3.1 | Every vertex reachable in <=t face steps; all full-set active vectors; primitive integral rays; cofactor bounds without simplicity |
| Lemma 5.2 | Lemma 5.1 | Positive leading exposure gap; full tangent rays; dominance including perturbations; no improving recession direction |
| Lemma 5.3 | Lemma 5.2 | Positive current pairing; every real scalar identity correction; negative bottom/cross cases; trace lower bound |
| Section 5.4 | Original main proof | Improving ray exists by dual cone contradiction; simultaneous branching induction; no eventual-termination claim |

## Mathematical clarifications retained in production

- Local finiteness uses continuity of the nonnegative quadratic minimizer and one
  uniform finite bound on both denominator and numerator vectors near the point.
- A nonrecession extreme direction has a finite attained endpoint by closedness;
  common independent equations plus a newly active equation make it a vertex.
- The common active integer pair cancels between edge endpoints in the movement
  estimate. No assumption that its last coordinate is one is used.
- The proof explicitly gives the trace reserve used to exclude scalar corrections
  and the elementary N>=24(t+1), N>=n(t+1) estimates.
- The original phrase “bounded ray” is replaced by a direction with a finite
  adjacent endpoint. The ray itself is unbounded.

## Exact computation and portability

Fresh generator and independent determinant/cofactor verifier runs passed six
families in orders 5,6,8,10; all 36 tested canonical rays; a complete improving
branch prefix of depth three in order five with 18 vertices and 26 edges; 7,869
finite lattice evaluations; 119 shared-active incidences; seven corruption tests.
The omitted-vector exclusions in the short-prefix verifier were inspected.

The largest tested family has t=2^64 and a 4,823-bit N. This is an analytical
prefix guarantee, not a 64-bit input or a simulated trajectory. The scripts check
the parameter inequalities for those six families, not all n,t. The general
inequalities and all-choice induction are proved in the article.

Windows originally wrote CRLF data with hash a46a67a09f1609a1a2397ac2e396f5b9bb5a106952976d66a3a8b4d47a04dee4.
Changing only CRLF to LF reproduced the pinned original hash. The delivered scripts
write explicit UTF-8 bytes and produce that LF hash directly on this computer.

## Exact limitations

The theorem lower-bounds the number of adjacent pivots, not elapsed running time.
It covers the canonical start and strictly decreasing extreme-direction choices
with current-vertex, selected-copositive-ray, and scalar-identity-corrected-ray
exits. It does not cover arbitrary algorithms, unrelated separators, nonlocal
preprocessing, input-dependent starting vertices, nonadjacent jumps, or
non-descending moves. Random choices are covered pathwise. No unique path is
claimed, and no eventual termination claim is proved or refuted.

Binary bounds are for fixed n and explicit rational centers and separators.
Arbitrary rational perturbations may have much longer encodings. The robustness
radius and distance reserves are explicit but small; no optimal exponent or
uniform variable-dimensional lower bound is claimed. General copositivity
verification is not claimed efficient from certificate entry length alone.
