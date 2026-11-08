# Milestone 80 — the two-mode/two-edge budget is sharp for exact subfamily preservation

**2026-11-08. Explicit proof with rational harmonic/Shapley values and exact facial peeling.** This is a *subfamily-compression sharpness result* supplementing checkpoint 79. It does NOT claim that every globally equivalent construction requires these same original generators or that arbitrary dense kernels reduce to tied-edge incidence.

## A tied mode whose TWO distinct edges are indispensable

Use vertices 0,1,2,3,4, with source 0, terminal 4, kernel target X*=E00. Let a rational mode at vertex 2 tie parent edges (0,4) and (1,3), with other vertices having single modes:
- vertex 1 mode: {(0,3)};
- vertex 2 mode: {(0,4),(1,3)};
- vertex 3 mode: {(2,4)}.

Use the standard sparse rational PSD pencil of checkpoint 74 (one diagonal Eii-E00 and lambda times the sum of each mode's offdiagonal F_parent entries, small lambda), with L the orthogonal projection onto the pencil kernel complement.

Its unique strict min–max value and exposing layers are
\[
w=(0,2/5,3/5,4/5,1),\quad
\{4\},\{2,3\},\{1\}.
\]
If the tied mode at vertex 2 is reduced to only edge (0,4), then its value changes to
\[
w'=(0,3/8,1/2,3/4,1),
\]
although the exposing layers stay \{4\},\{2,3\},\{1\}.
If instead it is reduced to only edge (1,3), the original value vector is preserved but the exposing layers change to
\[
\{4\},\{3\},\{1,2\}.
\]
Thus **neither edge can be removed without changing the game vector or the canonical facial rank profile**. This proves that one edge per mode is NOT enough to preserve BOTH complete invariants in every tied-edge incidence problem.

## Two independent modes whose coexistence is indispensable

Use vertices 0,...,5, terminal 5, with parent modes:
- vertex 1 {(0,3)};
- vertex 2 {(1,4)};
- vertex 3 has TWO separately controlled modes {(0,5)} and {(2,4)};
- vertex 4 {(1,5)}.
This is the earlier exact six-by-six PSD system of checkpoint 58; its strict value vector and exposing layers are
\[
w=(0,1/4,7/16,1/2,5/8,1),\qquad
\{5\},\{4\},\{2,3\},\{1\}.
\]
Keeping only vertex 3's mode {(0,5)} preserves w but changes peeling to
\[
\{5\},\{3,4\},\{1,2\},
\]
shortening the degree from four to three.
Keeping only {(2,4)} preserves the four-step peeling but changes the game values to
\[
w'=(0,3/11,5/11,6/11,7/11,1).
\]
Therefore **two modes per vertex are sometimes needed to preserve simultaneously the complete value vector and exact exposing schedule** when compressing an existing incidence system by deleting modes.

## Combined conclusion

Checkpoint 79 proves the sufficient bound "at most two modes, at most two edges per mode" for the entire tied-edge family. The two explicit examples above show that neither of these two budget numbers can be independently reduced to one in a general subfamily-preservation theorem.

All exponents and exposing times follow from the exact Shapley/peeling theorems (checkpoint 74); the arithmetic is a four-by-four or three-by-three rational solve, and the exposing layers can be verified by hand using the AND–OR closure. The companion checker (checkpoint 81) independently redoes both calculations.

**Scope caution:** The examples show indispensability of the particular tied/independent generators as subsets of the given kernel, NOT impossibility of representing an exponent–profile pair through a completely different graph. The full dense PSD-to-tied-game universality claim is still open.