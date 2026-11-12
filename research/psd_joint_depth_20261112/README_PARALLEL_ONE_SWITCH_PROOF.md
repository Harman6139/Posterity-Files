# PSD joint-depth frontier: one-switch completion

**New research continuation, 12 November 2026.**

The main mathematical file is
`128_ONE_SWITCH_FIXED_NULLITY_UNIVERSAL_CLASSIFICATION.md`.
It supplies a complete proof of fixed-nullity interpolation and the resulting
necessary-and-sufficient arithmetic classification of attainable
`(n,r,d,alpha)` tuples for positive target rank. It includes the dense
necessity argument, explicit rational kernels and ambient exposing stresses,
all-competitor sharp recovery estimates, minimum-degree proofs, boundary
cases, and a finite exact minimum-nullity formula.

The new step is a one-switch schedule: an upper-peeling prefix followed by a
lower-peeling suffix. Those schedule lengths cover every integer from `L(w)`
to `U(w)`. A common non-source blocking endpoint for the delayed grades makes
all cross-layer shared-anchor repairs off-face after the switch. This avoids
both earlier independent-edge cancellation failures and the false assertion
that every intermediate coordinate schedule is realizable.

## Scope

The result classifies attainable exponent/depth/nullity/rank tuples. It does
not classify every prescribed facial rank-drop profile and does not claim
that scalar weights determine the depth of a particular arbitrary kernel.
The new proof is not independently refereed; no bibliographic priority claim
is made for its classical ingredients or the branch's previous results.

## Reproducibility

The constructor/auditor requires Python 3.10 or newer and only the standard
library. Do not run it with `python -O`, since its exact certificate checks
use assertions.

Run the targeted regression audit:

```bash
python research/psd_joint_depth_20261112/129_ONE_SWITCH_EXACT_CERTIFICATE_AUDIT.py \
  --output one_switch_audit_results.json
```

The recorded audit checks 225 constructions across 17 targeted systems and
closed-form families. These are exact rational identities and strict
positivity inequalities, not floating-point SDP tests or an exhaustive
search for a theorem. The proof does not depend on the number of tests.

Construct a requested degree/exponent from an input harmonic certificate:

```bash
python research/psd_joint_depth_20261112/129_ONE_SWITCH_EXACT_CERTIFICATE_AUDIT.py \
  --construct research/psd_joint_depth_20261112/EXAMPLE_125_DEGREE_FOUR_INPUT.json \
  --output certificate.json
```

The output gives the rational kernel generators, the exact exposing path,
formal ambient exposing matrices with explicit integer parameters for their
positive diagonals, and an ordinary polynomial matching recovery arc.
The example deliberately combines the checkpoint-125 weights with a final
leading-edge collision, exercising that repair as well.

## Provenance and repository status

Repository: `Harman6139/Posterity-Files`.
Branch: `research/psd-joint-depth-universal-20261107`.
Reviewed source head: `48bcfb75063cb8674f3505384cbcd5e8ddc8af75`.
The Opus handoff and the load-bearing earlier proofs are listed in Section 10
of the theorem file.

**No GitHub commit was made in this session.** The available GitHub connector
actions were read-only, and no authenticated GitHub CLI was available. This
folder is ready to add to the existing research branch. The supplied patch
adds only this new dated folder and does not alter or delete historical
checkpoints. `INDEX_APPEND.md` contains a short entry for the master research
index and project-lead handoff.
