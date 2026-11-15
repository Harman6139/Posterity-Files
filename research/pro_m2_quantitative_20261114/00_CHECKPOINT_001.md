# Research Track II — checkpoint 001

Date: 2026-11-14. This independent results branch starts at source commit 22ed4becd320695b41f8a11f1223ea090ef89ecf. It does not modify prior milestones.

## Retrieved and read

- Complete flagship handoff 02_MANUSCRIPT_II_COPOSITIVE_QUANTITATIVE_PIVOTS.md.
- Milestone 37, including sharp cubical correction proof, rational regularization, target-aware ray test, neighbor-existence argument and restated shadow termination proof.
- 00_MANUSCRIPT2_SHARP_GRID_STATUS.md.
- Original milestone 34 has NOT been retrieved; the handoff explicitly says it may not exist on GitHub.
- Located primary 2021 article A simplex algorithm for rational cp-factorization (DOI 10.1007/s10107-020-01467-4) and Oertel–Schürmann, Generalized Perfect Matrices (arXiv:2602.05841). Full reading/priority audit pending.

## Exact target and status

UNRESOLVED: polynomial in H=L+ceil(log2(1/delta))+2 bound for the specified minimum-ratio adjacent-vertex rule in every fixed n; or rigorous superpolynomial obstruction plus consequential corrected universal algorithm.

NO BREAKTHROUGH IS CLAIMED. No percentile or submission-readiness claim is justified yet.

## Candidate obstruction to investigate (NOT YET A PROVED RESULT)

Order-two shear chain:

P_k = [[1,-(2k+1)/2],[-(2k+1)/2,k^2+k+1]], k>=0.

Candidate active vectors e1,(k,1),(k+1,1); candidate edge difference R_k=[[0,-1],[-1,2k+2]].

Candidate nonmember A_N=[[N^2-2,N],[N,1]], rescaled rationally to Frobenius norm <=1. Pairing along chain is (N-k)(N-k-1)-1, and <A_N,R_k>=2(k+1-N). If the shadow rule necessarily follows this chain until k=N-1, it gives exponential-in-input-bit-length pivot growth. Need prove all Ryshkov constraints, complete active set, extremality, unique minimum-ratio choices, absence of early vertex/ray certificates, and an explicit polynomial-in-N distance lower bound after normalization.

This is an analytical infinite-family route, not numerical evidence. An order-two obstruction refutes a universal fixed-order assertion, but the handoff requires a general corrected algorithm and significance audit beyond that obstruction.

## Next mathematical checks

1. Compute the full tangent cone and compare all candidate ratios exactly.
2. Check whether the milestone-37 corrected-ray test can terminate before the long chain.
3. Develop a dimension-general non-enumerative replacement (support-stationarity oracle / rational cutting-plane route), while distinguishing known fixed-dimensional real-algebraic complexity from new geometry.
4. Read complete primary conjecture, 2026 generalized perfect-matrix and copositive minimum papers, and reported rational-boundary-factorization counterexamples.

Progress is saved as immutable numbered checkpoints rather than overwriting source proofs.
