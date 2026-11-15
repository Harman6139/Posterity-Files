# Checkpoint 00 — grand spectral transport recovery

Date: 2026-11-15. Parent: 3ede4efb66c42da2b9b25584478a42e7cf35648f. Branch: research/pro-m1-grand-spectral-transport-20261115.

## Exact status

The arbitrary-order plain affine–PSD DRS last-step conjecture is NOT proved or disproved. No persistent transverse mode has been proved for the balanced order-seven candidate. The publication-quality and historical-priority gates are not passed.

## Recovered local source

The actual conversation attachment DRS_progress_checkpoint_20261115.zip is present and has been extracted. It contains checkpoints/00_RECOVERY.md, checkpoints/04_BALANCED_VARIANT_AND_VERIFIED_STATUS.md, diagnostic.py, three saved NumPy datasets, and SHA256_MANIFEST.json. The exact matrix construction and code have been read. The saved epsilon=1/10 state at 6,000,000 steps has been loaded, not regenerated. Floating-point observations are not asymptotic proofs.

## Exact balanced candidate, indices 0,...,6

Let Fij=Eij+Eji, a=-(F01+F34)/2, gamma>0 rational, and

L=span{E00+E33, E11-F02/2, E44-F35/2, E66+gamma(F02-F35), F06, E22-E55}.

Set U=a+L and Tz=z+P_PSD(2P_Uz-z)-P_Uz using the original Frobenius metric. The recorded start is z0=a+epsilon F06+(3epsilon/10)F26, gamma=1, epsilon=1/10. Thus the exact perturbations are 1/10 and 3/100.

This balanced candidate is different from the first doubled-arrow candidate in remote checkpoint 02. In particular the two top diagonal directions are tied and the antisymmetric final-diagonal direction is included. The local packet proves weak infeasibility and escape exponent alpha=1/3, hence state exponent p=1/4 conditional on inherited milestones 30–31. Those proofs are being independently audited.

## Decisive missing statement

The reference orbit has zero seventh row/column. A disproof requires an exact positive limsup for k^(3/4) times the seventh-column last difference for a specified rational start, with cumulative nonlinear spectral errors controlled. A proof of decay for this particular candidate would still not prove the universal theorem.

## Source and proof audit boundaries

The complete new handoff has been read, including its stricter publication requirements. Earlier source material is present in the conversation and is being checked against the pinned repository. The latest remote checkpoints 04–06 have been retrieved and read. Checkpoint 06 proves only good-orbit transfer when p>=1/2; it does not construct a good orbit. Checkpoint 05 is a pointwise projective duality, not a conjugacy of plain iterates. The prior saturation criterion does not prove saturation. In checkpoint 01 section 6.2 the cross-cone pairing should be >=0, not =0; its following argument uses the inequality.

New proved identities, failed routes and unresolved assumptions will be kept in separate numbered checkpoints. Nothing in this recovery file asserts a new theorem or a completed novelty audit.
