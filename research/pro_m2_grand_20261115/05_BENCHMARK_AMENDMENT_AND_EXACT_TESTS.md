# Prospective benchmark correction and exact-test checkpoint

2026-11-15. This amendment is made before assigning any comparative score to the new manuscript. All cohort articles remain UNSCORED.

## Mechanical correction to the sampling rule

The previously committed rule requested six research articles from each of LAA volumes 718 and 719. Volume 718 contains only five research articles (pages 1–103), followed by an index. A sixth research article does not exist. Preserve the consecutive-selection intent by taking the first TWELVE research articles when reading volume 718 and then volume 719 in printed-page order: all five from volume 718 and the first seven from volume 719. No selection is based on mathematical strength or full-text accessibility.

The additional sixth and seventh articles of volume 719 are:

6. Chang Liu and Jianping Li, Extensions on spectral extrema of theta_(1,2,5)-free graphs with given size, pages 136–157, DOI 10.1016/j.laa.2025.04.010.
7. Yury Grabovsky, Graeme W. Milton and Aaron Welters, Complete characterization of symmetric Kubo–Ando operator means satisfying Molnar's weak associativity, pages 158–182, DOI 10.1016/j.laa.2025.04.015.

The five-plus-seven cohort, two consecutive volumes, inaccessible-paper denominator rule, complete-central-proof reading requirement, and conservative ten-of-twelve operational comparison threshold are now fixed. The amendment is not a claim that such a small consecutive cohort statistically establishes a journal-wide percentile.

## Exact certificate implementation

Local standard-library programs build_certificates.py and verify_certificates.py have both run successfully. The verifier imports no generator code and uses a different exact linear-system method. Six groups passed:

- A rational affine CP fiber with a real completion but no rational completion; the displayed algebraic PSD exposer and invertible rational coefficient matrix certify one arithmetic reduction.
- A totally real factorization whose conjugate leaves the polyhedral column cone, together with a rational constrained factor of the same matrix.
- Seven exact bounded-moment corrections, dual identities, finite-grid positivity checks and strict rational sharpness witnesses.
- A complete 31-support exact copositivity check for the fixed Horn matrix.
- Three perfect-lattice sharpness instances, including a q=2^32 case, checked for integral minima, matrix identities and full rank of active normals.
- Twelve compressed nonsimplicial shadow normal certificates across three dimensions, with exact reconstruction, positive coefficients and rank d-1 of retained normals. For n=7 and N=2^128, the universal proof certifies at least 34415567301696923 pivots. This is not a simulated trajectory.

The separately coded verifier rejected six deliberately corrupted certificates, one per group. Its successful checks are not independent human review or proof-assistant verification, and the general theorems do not rest on finite tests.

The six data-file SHA256 hashes are:

arithmetic_obstruction.json: 59c8a1de7a5513ed5c801dc2f8b1ea819f983b365d4196ab054984f19727b63a
cube_moment_corrections.json: 9db2c4f538043609685bf210f234bbde2a40b06dba238555b412b89fc0c7983e
horn_support_certificate.json: b9924993a210dc65974afe3617a328520bff10de9ed0e4d512f6c61d61b2a47c
lattice_sharpness.json: d660620b61c0d82b11f04f00a443c04feacb29ad762a470887ab1b271a85ac1f
nonsimplicial_shadow_paths.json: c57a7a70f5117ad1fba99843b749b2d844171aa6f654462761682c4732ac4f8b
totally_real_descent.json: dfe4716c73ddbeb800b23045de5cc7b47202887ba477f6055ae3729b88fff038

Source and data files are currently present under /mnt/data/grand_matrix_cones in the active runtime. This checkpoint does not assert that those complete source files have already been uploaded. Full release packaging and the main submission manuscript remain in preparation during this session.
