Exact seed and geometry instance supplement

Source: Harman6139/Posterity-Files, immutable commit
8e551996c8462cfe78c20e5edf18d18c0707f2c5,
research/pro_m2_reusable_hardness_20261115/release/.
The five code/data/input files in this directory are byte-identical to that
source. The original research release and its manuscript are preserved separately.

Run from an extracted writable copy, with Python 3.9+ and its standard library:
  python code/verify_certificates.py
  python code/generate_certificates.py
  python code/verify_certificates.py
Do not use python -O: the generator uses assertions.

The generator overwrites certificates/exact_certificates.json; the verifier
overwrites certificates/verification_report.json. On Windows the unchanged
upstream text writer may use CRLF instead of LF. Fresh parsed certificate data
were checked equal to the pinned data; byte hashes can consequently differ.

The suite checks eight seed cases, 65 maximal proper principal blocks, 18
amplification scales, 20 geometric records with 142 listed active identities
and 128 listed rays, seven one-dimensional templates, three arrow
decompositions, four restriction groups and nine rejected corruptions.

Scope: the geometric records test residual/shear identities, listed-normal rank
and listed-ray feasibility. They do not independently establish global lattice
feasibility, completeness of active lists, or extremality of every listed ray.
There is no implemented exhaustive movement-inequality loop. The article's
universal geometry, all-choice induction and perturbation results have analytic
proofs; these finite data are reproducibility evidence, not their replacement.
The original canonical suite one directory above separately tests a complete
small improving-branch prefix. No exponentially long trajectory is simulated.
