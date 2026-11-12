# Milestone 131 — Frontier closure: scope, audit, and project-lead handoff

**Date:** 2026-11-12.
**Branch:** `research/psd-joint-depth-universal-20261107`.
**Predecessor:** `48bcfb75063cb8674f3505384cbcd5e8ddc8af75`.

## Result delivered

[128 — One-switch exact-nullity interpolation](128_ONE_SWITCH_EXACT_NULLITY_INTERPOLATION.md) proves, for every strict harmonic vector, every admissible half-weight, and every integer between its canonical lower and upper peeling bounds, an explicit rational PSD realization at the **original nullity**, with the **exact minimum facial degree** and the **sharp full-ambient recovery exponent**.

[129 — Complete all-nullity arithmetic spectrum](129_COMPLETE_ALL_NULLITY_ARITHMETIC_SPECTRUM.md) reconstructs arbitrary-dense necessity and combines it with 128. Its formulas (4) and (8) are the all-nullity necessary-and-sufficient criterion for `(n,r,d,alpha)`. Formula (28), with the explicit finite bound (27), gives the exact smallest possible nullity by bounded integer arithmetic. Boundary cases, including full-rank and zero-rank targets, are included.

This is a complete research proof of the tuple-existence frontier identified by the Opus 5.5 handoff, not a claim of independent referee acceptance or bibliographic priority.

## The mathematical insight

Follow the upper peeling rule for a prefix of its trajectory, then switch once to the lower rule. If the upper states are J_t and f(j) counts the remaining lower transitions, the one-switch lengths are D_t=t+f(J_t), and successive lengths differ by zero or one. Therefore they cover the entire admissible depth interval.

Only tail vertices whose original tight parent has already escaped need new blocking edges. Every such vertex, and every tight owner with which its blocker collides, belongs to the **first lower-tail layer**. Transfer its positive diagonal into that owner rather than introducing a second coefficient on the same main edge. This synchronizes the collision, avoids cancellation, and requires no cloned coordinate.

Shared source releases remain triangular. A leading half-weight can collide with a release only at the final layer; an explicit convex-square-scaled final stress repairs that collision.

## Proof obligations explicitly discharged

The manuscripts prove all of the following, rather than infer them from graph counts:

- Coverage of every integer depth by one-switch schedules.
- Safety, non-source character, and first-tail synchronization of switch blockers.
- Preservation of every grade and the exact sharp exponent, using inequalities for **all ambient PSD competitors**, not only structured curves.
- A matching strictly positive-definite curve and uniqueness of the target.
- Actual ambient measurement stresses, not illegal zero extensions of compressed stresses.
- Maximality at every exposing step, and minimum degree against arbitrary rotated chains.
- Every distinguished half-weight, including the final leading-edge collision.
- Exact nullity and arbitrary positive target rank, with controlled fully measured padding.
- Dense necessity with multidimensional grades, a fixed orthogonal chart, and no sparse-kernel assumption.
- An integer determinant formula and a finite bound for minimum-nullity evaluation.

## Prior routes reviewed and retained

The handoff, chronological index, and load-bearing checkpoint proofs were reviewed. The new proof uses the lower-release mechanism of 114 and positive multi-child ownership of 123. It changes the schedule-selection problem rather than attempting to realize every admissible schedule from 110.

The single-action and independent-two-policy failures remain relevant: the construction permits tied releases and positive multi-child owners. The degree jump in 107 remains valid; no one-edge Lipschitz interpolation is assumed. The signed cancellation examples in 116/121 remain valid; no independent coefficients share a main edge. The dense forbidden schedule in 125 and the exact projected-kernel Gordan test in 127 remain valid; the one-switch schedule avoids that impossible flag.

The graded-cone and conic-matroid route in 119–122 is not refuted or replaced as an instance-wise theory. The new construction eliminates its unknown real feasibility variables only for **existence of the projected invariant tuple**, which is the frontier addressed here.

The small-nullity tables are not used as premises. No claim is made that every one of the 127 predecessor files has received a new line-by-line proof audit.

## Exact implementation audit

Run:

```sh
python 130_EXACT_ONE_SWITCH_CERTIFICATE.py
```

The program uses only Python's standard library and exact `Fraction` arithmetic. It validates a deterministic construction on specified regression policies; it does not search for proof routes or perform exhaustive policy enumeration.

The execution recorded in `130_AUDIT_OUTPUT.txt` reports:

- 13 supplied policies/family specializations, including the no-internal-grade boundary.
- 203 cut/half-weight constructions.
- 3,036 exact stress-step checks.
- 9 final leading-release repairs.
- 22 switch-blocker occurrences, including 4 blocker/tight-owner merges.
- All assertions passed, with no numerical SDP, floating-point fitting, or third-party solver.

The policies include both degree-jump examples of 107, the cancellation example of 116, the forbidden-schedule weights of 125, a simultaneous switch-merge/leading-collision example, and dyadic systems through nullity 32. The code checks exact generator pairings, active-edge support, positive convex-square gaps, survivor obstructions, synchronization, and the no-gap schedule identity. The written general proof, not these finitely many checks, establishes the theorem.

## Scope and limitations

The closed result is the complete **exponent versus minimum degree spectrum at fixed nullity**, and its minimum-nullity arithmetic characterization. It does not classify every exact rank-drop profile, every individual coordinate flag, or every original dense kernel up to isomorphism. Those are strictly stronger questions; the forbidden-flag example demonstrates why they must not be silently substituted for tuple existence.

The finite determinant formula is not claimed to be polynomial-time or an elementary numerator/denominator expression. It removes continuous conic feasibility and is bounded explicitly. Independent specialist verification and a full literature-priority audit remain appropriate before journal submission.

## Repository organization

The new work is in `research/psd_joint_depth_20261112/`. All earlier numbered checkpoints and the Opus handoff are unchanged. The previous long master index and project-lead handoff are preserved as exact blob copies beside the new entrypoints, retaining their relative links. The new entrypoints point to this theorem package and to the complete chronological archive.

No repository visibility change or asynchronous research process is claimed.
