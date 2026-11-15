# Checkpoint 004 — priority audit and scope correction

Date: 2026-11-14. This checkpoint supplements, and does not delete, earlier mathematical checkpoints.

## Important identified antecedent

Valentin Dannenberg and Achill Schürmann, *Perfect copositive matrices*, Communications in Mathematics 31 (2023), no. 2, 137–156, DOI 10.46298/cm.11141, arXiv:2303.17310v4, already contains the vertex family used in checkpoint 002.

In Section 5, their order-three P_k is exactly twice our P_k after permuting the duplicated coordinates together. Lemma 5.1 gives the coordinate-duplication lifting, Corollary 5.3 proves the minimal vectors, the count 2k+5 in order three, and adjacency of successive matrices, and the following discussion iterates the lift to all orders. Thus the shear vertices, lifting mechanism, order-three active-set growth, and adjacency are NOT new discoveries of this project. The all-order binomial count and its output-size interpretation are immediate quantitative consequences, not an independent structural breakthrough.

What checkpoint 002 adds relative to the specific results inspected there is the explicit rational objective family, unique minimum-ratio shadow choices via a strictly positive normal-cone decomposition, exact exponential-in-bit-precision pivot count, and robustness under the prescribed objective-dependent grid correction. Historical novelty of those algorithmic statements has not yet been certified beyond these comparisons.

## Other primary comparisons retrieved

- Dutour Sikirić–Schürmann–Vallentin, *A simplex algorithm for rational cp-factorization*, Mathematical Programming 187 (2021), 25–45, DOI 10.1007/s10107-020-01467-4, arXiv:1807.01382. Procedure 3 / Conjecture 3.2 asks finite termination with a suitable pivot rule, NOT a polynomial pivot bound. Its binary Farey-chain analysis and exact copositivity discussion are important antecedents.
- Oertel–Schürmann, *Generalized Perfect Matrices*, arXiv:2602.05841v2 (2026). Section 6 discusses rational cone certificates/interior representations and graph traversal. No polynomial shadow-pivot theorem was found in the sections inspected. Do not describe this limited comparison as a complete independent verification of every theorem in that paper.
- Oertel–Schürmann, *On Computing the Copositive Minimum and its Representatives*, arXiv:2509.23696 (2025 preprint). The arithmetic minimum and enumeration bottleneck are directly relevant; do not relabel its 2025 submission as a new 2026 result.
- Hendrix–Casado–G.-Tóth, *On monotonicity and search strategies in face-based copositivity detection algorithms*, DOI 10.1007/s10100-021-00737-6; open predecessor https://optimization-online.org/wp-content/uploads/2020/04/7724.pdf. Face-stationarity enumeration is established prior work. The exact support oracle and ellipsoid method in checkpoint 003 are classical ingredients, not a claimed new discovery of fixed-dimensional polynomial tractability.

## Limitations that must remain explicit

1. The lower-bound inputs are entrywise nonnegative but not PSD. A PSD pretest rejects them immediately. The proof disproves the specified adjacent-pivot theorem but does not prove a similar lower bound after PSD preprocessing, or on doubly nonnegative nonmembers.
2. The all-order construction uses a fixed P_1 depending only on n; the canonical tridiagonal initialization is covered directly in order two. Do not assert that the higher-order canonical-start path has been proved.
3. The repaired algorithm bypasses Ryshkov adjacency. It is an explicit exact-rational implementation with polynomial binary-precision complexity and exponential dimension dependence. It is not evidence that every adjacent-pivot algorithm can be accelerated.
4. The original milestone 34 was not located by connected Project/Library filename searches. The restated proof in milestone 37 was retrieved. No inaccessible source is cited as if read.
5. Reported September/November 2026 counterexamples to unrestricted rational boundary CP factorization are independent of these results. Their full certificate verification has not been completed here.
6. No preregistered full-proof 10-paper-per-venue benchmark is complete. No upper-quintile, 80% acceptance, or eight-month decision guarantee is justified.

## Publication status

The exact quantitative conjecture is disproved by the explicit family. A general rational replacement theorem has been supplied. The stronger requirement of a historically novel, comparably consequential replacement plus defensible upper-quintile venue comparison is NOT established. The manuscript must present the actual result and these boundaries, rather than calling the entire flagship assignment completed.
