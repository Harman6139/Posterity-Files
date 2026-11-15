# Checkpoint 04 — a rigorous limit of the new moment-matched route

Date: 2026-11-15. This file prevents the exact logarithmic theorem from being mistaken for the original dimension-uniform power-law frontier.

## 1. Deterministic error decreases exponentially, uniformly in the depth

Write eta=1/4096 and v0=(77/192)eta, as in checkpoints 01--02. For EVERY depth n and every T<n, there is a deterministic T-query algorithm with

    H_w(x_output) <= v0 eta^T

for every hidden word w. If T>=n the core can be made exactly zero. For the full natural conic objective, the infimum of the corresponding worst-case objective is therefore at most v0 eta^T (or zero after full recovery).

Proof. Use any fixed complete sign guesses consistent with the already learned prefix, with the exact Q(sqrt(2)) probes from checkpoint 02. Each query either learns the whole remaining word or reveals at least one additional sign. After T queries, the known prefix has length k>=T unless k=n. Output its center. If k<n, the core value at that center is exactly v0 eta^k for EVERY remaining suffix; this is the identity used in the expected-risk proof. If k=n, output the true zero center. Append a finite known-tail coordinate with phi below any prescribed positive delta. QED.

In fact this is the exact deterministic minimax objective INFIMUM:

    R_det(n,T)=v0 eta^T for 0<=T<n,
    R_det(n,T)=0 for T>=n.

For the lower bound use the stronger prefix oracle from checkpoint 02. Against a deterministic strategy, every informative query can be answered by making its very next unknown guessed sign wrong; this fixes one further true bit and leaves all later bits free. Queries inconsistent with the already fixed prefix reveal nothing. After at most T calls the fixed prefix has length k<=T. The remaining uniform suffix has average core minimum v0 eta^k, so every fixed output has core loss at least that large for some completion. Because eta<1, this is at least v0 eta^T. A consistent single word can be fixed at the end of this DETERMINISTIC adversarial proof; it is not being used as a fixed-prior randomized lower proof. The randomized theorem was already proved separately by the uniform prior.

## 2. Arbitrarily increasing n cannot repair the target exponent

For any choice n=n(T), even a superpolynomial one, T queries on THIS family achieve objective at most 2v0 eta^T by taking tail loss at most v0 eta^T (or less when the word is fully recovered). Consequently, for every fixed c>0 and theta>0, sufficiently large T satisfy

    2v0 eta^T < c(T+1)^(-theta).

Thus this family cannot yield the original polynomial-threshold lower bound by simply choosing a larger depth. This is an algorithmic obstruction for the family, not a universal obstruction for rational PSD-distance objectives.

## 3. Independent copies do not amplify sequential query hardness

Consider a known separable sum sum_i A_i H_(w_i)(x_i), with A_i>0 and nonempty hidden words. One vector query gives EVERY coordinate gradient. The prefix probes for all copies can therefore be performed simultaneously. After T queries each copy has either been fully identified or has core value at most A_i v0 eta^T. Total core error is at most

    v0 eta^T sum_i A_i.

When the copies start at zero and the total initial objective is at most one, sum_i A_i is bounded by 1/v0. Thus these separable direct sums retain exponential decay in T. Merely increasing the number of independent scalar hard cores does not produce the desired sequential power-law lower bound in a full-gradient oracle model.

This statement is for the displayed separable objective. Any extension with additional padding must separately verify that the chosen prefix comparators have zero or controlled padding loss. No transfer through arbitrary coupled padding is asserted. In particular, the argument does not rule out a genuinely coupled higher-dimensional family. This qualification replaces an overbroad padding sentence in the initial version of this checkpoint; the exact minimax and deterministic family results are unchanged.

## 4. Spatial rescaling alone does not change this conclusion

For an unshifted rescaling A H_w(x/R) plus a nonnegative tail, normalization f(0)<=1 forces A<=1/v0, because H_w(0)=v0 for every nonempty word. Scaling R affects coordinate radius but does not remove the eta^T energy decay of the prefix algorithm. Multiplying the core by an exponentially large A to offset that decay would violate the initial-value bound in this construction.

More generally, in an equal-scale binary interval recursion, two disjoint children each contained in their parent must have spatial contraction h<=1/2. With nonnegative measure reservoirs and a common total mass, the child mass fraction obeys lambda<=1. The recursive squared-loss energy multiplier is lambda h^2<=1/4. Consequently that particular positive-moment, nested-interval architecture inherently loses an exponential factor with each revealed level. This does not cover anisotropic higher-dimensional cells, different spectral couplings, or all rational conic constructions.

## 5. Consequence for the next proof obligation

The original sharp lower bound cannot be obtained by renaming this logarithmic theorem, increasing its depth, taking the displayed separable direct sums, or rescaling it within the stated normalization. A successful continuation must supply a qualitatively different optimization-relevant hiding mechanism whose energy barrier remains polynomial in the number of sequential revelations, or a universal upper theorem showing that such a mechanism is impossible in the entire rational conic class. Neither universal alternative has been established.
