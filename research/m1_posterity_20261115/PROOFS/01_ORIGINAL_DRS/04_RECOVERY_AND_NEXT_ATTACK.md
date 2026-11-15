# Checkpoint 04 — recovered state and next analytical attack

Recovered at continuation following repeated interrupted sessions. Base commit: 2d1f975c4a0ecd3ec6b47baeee3be33639ad0118. The user requests incremental durable saves.

## Exact status

The arbitrary-order plain Douglas–Rachford last-iterate theorem is NOT proved or disproved. Checkpoints 01–03 are recovered and preserved. Checkpoint 01 proves a scalar saturation equivalence conditional on the inherited common-state theorem. Checkpoint 02 constructs a rational weakly infeasible order-seven candidate with escape exponent 1/3. Checkpoint 03 gives exact matrix/congruence virial identities and warns that the candidate's apparently persistent transverse oscillation may be a long transient.

No journal-percentile, originality, submission-readiness, or full-resolution claim is warranted.

## Continuation focus

1. Audit the inherited common-state hypotheses and the exact cone identities.
2. Exploit the PSD-specific representation T(Z)=(Z+|2P_U Z-Z|)/2. In particular, any negative lower bound on Z decays geometrically: Z_k >= -2^(-k) max(0,-lambda_min(Z_0)) I. This follows immediately by induction from |R|>=0; it does not imply positive steps or scalar saturation.
3. Investigate whether cone positivity forces nonlinear damping of transverse modes. Do not infer infinite-time behavior from a moving linearization or a finite numerical window.
4. Preserve every proved result, unsuccessful route, and diagnostic separately. A future restart should read checkpoints 01–04 before rerunning old work.

The original complete mathematical target is in research/three_flagship_pro_handoffs_20261114/01_MANUSCRIPT_I_ALL_ORDER_PLAIN_DRS.md on branch research/three-flagship-pro-handoffs-20261114. The inherited baseline is 22ed4becd320695b41f8a11f1223ea090ef89ecf.
