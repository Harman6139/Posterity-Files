# Milestone 93 — universal dense PSD exponent = LAST GREEDY WEIGHT of a linear matroid basis

**2026-11-08. PROVED for every finite-dimensional uniquely solvable dense PSD inverse problem, conditional only on the independently proved global Dikin–Hessian modulus and fixed monomial maxdet chart (checkpoints 10 and 89).** No sparse midpoint or Shapley-game universality is used. The result gives a genuinely finite standard matroid rank algorithm computing the exact sharp exponent of a given dense pair. It does **not** classify the minimal facial-reduction degree from weights alone.

## The theorem

Let L:S^n→R^m uniquely recover a positive-rank PSD target X*, with measurement kernel K=ker L of dimension k>=1. Choose the canonical fixed orthogonal monomial center chart from checkpoint89:
    c D_e^2 <= C_e <= C D_e^2,
    D_e=diag(e^(theta_i/2)), theta_i nonnegative rational.
Choose a fixed Frobenius-orthonormal matrix-entry basis E_a of S^n, a=1,...,N=n(n+1)/2; choose any fixed basis H1,...,Hk of K. Let A be the N×k matrix A_(a,j)=<E_a,H_j>. Assign to each coordinate E_a its weight eta_a=(theta_i+theta_j)/2 where E_a is the (i,j) symmetric entry (diagonal included).

Sort ALL N coordinate rows of A in NONINCREASING eta_a. Starting with the empty row span, retain a row if and only if it raises ordinary real linear rank. Stop on reaching rank k. Then the sharp Hölder exponent is exactly
\[
\boxed{\alpha(\mathcal L,X_*)=\min\{1,\ \eta_{\rm last\ accepted\ row}\}.}
\tag{93.1}
\]
If K=0, alpha=1. This is invariant under fixed kernel basis changes and fixed orthogonal changes within a same-weight center grade.

## Complete proof

The center Loewner comparison and positive Kronecker order make the restricted logdet Hessian quadratic form uniformly equivalent to
\[
\sum_{a=1}^N e^{-2\eta_a}|\langle E_a,H\rangle|^2.
\]
Writing H=Σ_j x_jH_j gives the weighted constant Gram matrix
\[
G_e=A^\top\operatorname{diag}(e^{-2\eta_a})A.
\]
A constant nonorthogonal choice of K basis changes Euclidean/Frobenius normalization by bounded factors only. The universal Dikin recovery theorem gives
\[
\omega(\|L I\|e)\asymp e+\lambda_{\min}(G_e)^{-1/2}.
\]

For j=0,...,k let M_j be the maximum sum of weights of any independent set of j coordinate rows of A, with M0=0. For j>=1 the j-th elementary symmetric function of G_e is the sum of its j×j principal minors. Cauchy–Binet gives
\[
e_j(G_e)=\sum_{|I|=|J|=j}[\det A[I,J]]^2
                       e^{-2\sum_{a\in I}\eta_a}.
\]
Each summand is a NONNEGATIVE square, so its dominant ε-power cannot cancel. Consequently
\[
e_j(G_e)=\Theta(e^{-2M_j}).
\]
Since tr(G_e^-1)=e_(k-1)(G_e)/e_k(G_e) and
  1/lambda_min <=tr(G^-1)<=k/lambda_min,
we obtain
\[
\lambda_{\min}(G_e)^{-1/2}
  =\Theta(e^{M_k-M_{k-1}}).
\]

The selected coordinate rows form an ordinary representable linear matroid. The standard matroid exchange/greedy theorem says that scanning rows in decreasing weight and retaining rank-increasing rows produces, simultaneously for every j, a maximum-total-weight independent set of cardinality j. If selected row weights are beta1>=...>=betak, then M_j=Σ_(a<=j)beta_a. Thus M_k−M_(k−1)=betak, the LAST selected row's weight. This proves (93.1). QED.

## Geometric meaning and the game bridge

The game Bellman weights are exactly the center's monomial Loewner exponents in all strict tied-edge systems (checkpoint86). In this chart, the game exponent is the final greedy coordinate-matroid weight. For a GENERIC DENSE problem the same matroid rule holds, but its nonlinear grade weights are obtained from the canonical maxdet curve, not automatically from an incidence game. The center's actual Puiseux coefficients nevertheless yield an exponent-preserving harmonic graph (checkpoint91).

This also pinpoints the unsolved extra information needed to classify facial depth: the subleading signed linear relations and the PSD-conic dual face-compression lattice. The explicit six-by-six tied/base pair in checkpoints87–88 has the same leading center and all Hessian eigenvalue orders, hence the SAME matroid greedy-weight list, but minimal singularity degrees 3 and 4. Thus **matroid valuations determine the exponent but not the dual exposing profile**.

The formula is a finite ordinary-rank test once the center weights have been computed. No spectral eigenvalue asymptotics, optimized PSD recovery arcs, graph sparsity, or genericity assumption enters the last step.

## Reproducibility and prior-art discipline

An exact SymPy/Fraction audit of the quarter-power S^3 example and the 6×6 tied/base pair is available in this conversation workspace at /mnt/data/psd_dense_game_bridge/93_plucker_conic_exact_audit.py. The symbolic script tests weighted kernel-minor ranks, center normalization and dual peeling. The general theorem does not depend on this finite audit.

Matroid greedy algorithms, Cauchy–Binet, Puiseux valuation and maxdet barrier theory are established prior tools. This recovery-modulus consequence is proved here, but bibliographic priority/novelty is not independently established.

**OPEN:** the full arithmetic set of exponent/exact-facial-profile triples at nonmaximal degree for arbitrary dense kernels, and a dimension-preserving representation by tied-edge games or a definitively richer exact combinatorial model.