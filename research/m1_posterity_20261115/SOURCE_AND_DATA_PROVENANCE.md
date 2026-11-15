# Primary-source and local-data provenance ledger

_Date: 2026-11-15. This file is part of the immutable-minded research archive; it records exactly what is and is not remote._

## 1. Source lineage

All 53 copies in `ORIGINAL_HANDOFFS/`, `FOUNDATIONS/`, `PROOFS/`, and `PARALLEL_RESONANCE_AUDIT/` were created by referencing existing GitHub blob SHAs in a new Git tree. Therefore those exact copied sources have **byte-identical Git object contents** to their original commits.

| Parent or source | Pinned commit | Description and preservation |
|---|---|---|
| Original LAA baseline | `22ed4becd320695b41f8a11f1223ea090ef89ecf` | Milestones 12, 26, 28, 30, 31, 35, 36, 40 and manuscript status included in FOUNDATIONS; original larger history remains in branch ancestry |
| Original Track I DRS branch | `3ede4efb66c42da2b9b25584478a42e7cf35648f` | Checkpoints 00–06, including 01 saturation, 02 doubled-arrow, 03 matrix virial, 04 recovery, 05 duality, 06 good-orbit transfer |
| Initial 2026-11-14 all-order handoff | `778e4ffe29c132dd785b2a38769e5249372d82db` | Exact source blob `6aa28386893e2871b14cb5d6f26727adb5cc26c8` |
| Grand 2026-11-15 handoff | `c8a4f3380a8d7b8420059a57d724db9badcb3942` | Exact source blob `728710cba71ab67f761f97e59d5ba3876d8e8779` |
| Grand spectral proof draft | `637d4417c63751d1bfaef51d4ecd23549081ae15` | Checkpoints 00–05 |
| Parallel resonance proof audit | `6acf318bb326b5116938f8b8a6d5f64edeab9f0c` | Nonidentical alternative proof files 06–09 + exact symbolic scripts, copied without overwrite |
| Static-excess and angular continuation | `287cc9a6e073afc4f6b6c5aa6b43e3fe18c12943` | Checkpoints 10–14 |
| Latest consolidated manuscript | `0be40beea703afbd07807028ee34ed8ee82b9ee6` | Checkpoints 15–18, full 21-page LaTeX draft, scripts, earlier checked proofs |
| First archival commit | `ef82a6b419e89ae2169e2691827fed7b07a3f7b7` | All 53 curated full-source blobs and original handoffs mirrored into one research directory |

Do not silently merge differing files that happen to use the same number (e.g. two distinct `09` audits). All preserved versions are part of the evidentiary history.

## 2. User-provided unpushed local packet (recovered during this chat)

Original conversation file: `DRS_progress_checkpoint_20261115.zip`. Container SHA-256 (computed from exact local bytes):
```
e84e1101bf255a3a3c785789ade761ec8bf9ca8c91556801b96d7191a58964a0  DRS_progress_checkpoint_20261115.zip
```
Its original manifest lists:
```
d7a48bcb675455491837de8df753aa2e4ec647034905ab651116f3c780ce25e9  checkpoints/00_RECOVERY.md
cd585b09d13fcbaa325191ca76f13ae0810ac4b40e0c1d6c96611529111cd899  checkpoints/04_BALANCED_VARIANT_AND_VERIFIED_STATUS.md
bb01ceda6bdf138cbf9b7f8b035277b1c243a61c1a6d8797bc333b28044d8c36  diagnostic.py
362caca36f3e4592f9fb1f15f4e621c8de3ad497fce8c2f8db1c5b51bcec814d  diagnostics/balanced_eps0.01_g1.npz
1ab91aa13a26ce1d99d7be87605db9e603024b4fe3d2a24eee8a7ae8eb30654d  diagnostics/balanced_eps0.1_g1.npz
d057d3d5a5be9cc68f6eb50b0690555b649ddd350a8291e62465fa94e219b67d  diagnostics/balanced_eps0.5_g1.npz
```
These SHA-256 checksums are a way to test that future copies of the **original** files are unchanged. The three `.npz` arrays are binary NumPy records; this GitHub connector workflow does **not** upload them from local container bytes. Their exact arrays therefore remain in the original conversation ZIP, not in the GitHub archived tree. The two local markdown notes and numerical source driver have been transcribed into `LOCAL_20261115/`. Those transcriptions have not been independently checked by byte-hashing GitHub copies against the original local hashes; prefer the original ZIP when byte-for-byte provenance matters.

Original runner invocation (from the archived source):
```
python diagnostic.py --variant balanced --gamma 1 --epsilon 0.1 --steps 200000
python diagnostic.py --variant balanced --gamma 1 --epsilon 0.1 --steps 2000000 --resume
```
Requires Python, NumPy and Numba. Runs use floating-point eigendecomposition and cannot replace a rigorous asymptotic proof. The `--resume` argument preserves earlier sampled arrays by saving an atomic compressed NPZ file. The last saved `gamma=1, epsilon=0.1` sample is at 6,000,000 iterations.

## 3. Reproducible numerical facts, not theorem premises

For the *original gamma=1 local simulation*, the scaled one-column transverse state / last-step amplitudes are:

| k | state `k^(1/4)||column_6||` | step `k^(3/4)||Delta column_6||` |
|---:|---:|---:|
| 200,000 | 0.03134001188148402 | 0.02063248729731429 |
| 2,000,000 | 0.03247988448852342 | 0.02137588613185579 |
| 6,000,000 | 0.03300474085790027 | 0.02172003748208494 |

These amplitudes do not imply a nonzero limit or eventual decay. They are distinct from the **gamma=2 rational-parameter analytical family** in Checkpoints 07–09 and 16. Do not mix the perturbation `epsilon=0.1` with the separate large-`M` rational starting family.

## 4. Exactly where to restart a future adversarial audit

1. Inspect the original two handoffs for the full success standard, including no algorithm substitutions.
2. Recheck the 2026-11-14 scalar saturation reduction and virial identities.
3. Derive the gamma-2 weighted Riccati equations directly from the exact Frobenius affine projection; compare to parallel audit 07/09.
4. Prove the **uniform** Taylor remainder at every point of the chosen compact spectral chamber, and validate the numerical constants of the enormous rational-entry bound without extrapolating finite runs.
5. Verify each triangular fast-variable, slow-filter and amplitude barrier estimate before accepting all-time trapping.
6. Separate positive generic-cone excess theorem from the PSD-specific negative construction and from the original gamma=1 switching calculations.
7. Finish primary-source originality comparisons and full-proof journal sampling, not just DOI lists.

The working manuscript and source record are intentionally left **unmodified**, so a later referee can locate what was claimed, the precise proof offered and any potential correction.
