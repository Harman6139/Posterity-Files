## 2026-11-12 — One-switch fixed-nullity interpolation and full attainable-tuple spectrum

[Milestone 128](../psd_joint_depth_20261112/128_ONE_SWITCH_FIXED_NULLITY_UNIVERSAL_CLASSIFICATION.md)
supplies a complete proof that every strict harmonic weight vector, every
admissible leading half-weight, and every integer `L(w)<=d<=U(w)` has a rational
rank-one PSD realization at exactly the original nullity. The construction
uses an upper-peeling prefix followed by a lower-peeling suffix; these lengths
have increments zero or one and cover the entire interval. Common non-source
blockers and multi-child edge ownership prevent the collision failures of the
previous interpolation routes.

Combined with dense harmonic extraction and the primal/dual bounds, the note
gives the full finite arithmetic iff for attainable `(n,r,d,alpha)` tuples,
including an exact finite minimum-nullity formula. The complete proofs include
all-ambient-PSD recovery, a matching polynomial positive-definite arc, exact
ambient dual stresses, and **minimality** of the constructed facial degree.

[Audit/constructor 129](../psd_joint_depth_20261112/129_ONE_SWITCH_EXACT_CERTIFICATE_AUDIT.py)
and [recorded exact results 130](../psd_joint_depth_20261112/130_ONE_SWITCH_EXACT_AUDIT_RESULTS.json)
check the formulas on targeted obstruction examples and closed-form families.
This is a new research proof, not an independently refereed result. The
stronger classification of every prescribed rank-drop profile is not claimed.
