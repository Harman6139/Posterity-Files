# Milestone 92 — universal dominance of greedy facial reduction by the canonical Dikin valuation flag

**2026-11-08. PROVED for EVERY arbitrary dense uniquely solvable real PSD inverse problem.** This is a structural compatibility theorem independent of sparse graph or game models. It quantifies precisely how many valuation grades the *maximal-rank* facial-reduction process must eliminate at each step. It does not assert that greedy faces necessarily align with individual valuation grades at nonmaximal depth.

## Theorem

Let X*>=0 of positive rank r be uniquely PSD determined by L, K=ker L and nullity nu=n-r. Use the canonical fixed orthogonal Puiseux maxdet chart of checkpoint 89:
\[
\mathbb R^n=U_0\oplus U_1\oplus\cdots\oplus U_k,\quad
U_0=\operatorname{range}X_*,
\quad 0=w_0<w_1<\cdots<w_k=1,\quad m_i=\dim U_i\ge1.
\]
Let \(W_j=U_0\oplus\cdots\oplus U_j\). Let \(F_0=\mathbb R^n\supsetneq F_1\supsetneq\cdots\supsetneq F_d=U_0\) be the **canonical maximum-rank greedy facial-reduction sequence**, with exact exposed rank drops s1,...,sd. Then:

1. The first greedy step is EXACTLY \(F_1=W_{k-1}\), with \(s_1=m_k\).
2. For each \(0\le j\le\min(d,k)\),
\[
\boxed{F_j\subseteq W_{k-j}.}
\tag{92.1}
\]
Consequently \(d\le k\le\nu\).
3. The cumulative rank profile **dominates** the center valuation-grade multiplicities:
\[
\boxed{
\sum_{a=1}^{j}s_a\ \ge\
\sum_{i=k-j+1}^{k}m_i
\qquad (1\le j\le d).
}
\tag{92.2}
\]
4. At maximal degree d=nu, equality holds at every stage and all grades are one-dimensional: \(k=\nu,\ m_i=1,\ F_j=W_{\nu-j}\). This supplies an independent check of the alignment step used in the complete maximal-depth theorem, checkpoint 90.

## Proof

Let Cε be the shifted maxdet center, with \(cD_\epsilon^2\preceq C_\epsilon\preceq CD_\epsilon^2\) and positive semialgebraic normalized limit M0 as proved in checkpoint 89. Stationarity gives \(Z_\epsilon=\epsilon C_\epsilon^{-1}\in K^\perp\cap S_+^n\).

**First greedy face.** On the top grade Uk (weight wk=1), the limit \(Z_0=\lim_{\epsilon\downarrow0}Z_\epsilon\) is PD. On every lower grade it vanishes because its corresponding entries scale as \(\epsilon^{1-(w_i+w_j)/2}\) with positive exponent whenever at least one grade weight is <1. Thus Z0 is a valid first exposing stress with range exactly Uk.

Conversely, let Z∈K⊥∩S_+^n be ANY first exposing stress annihilating X*. For every ε,
\[
\langle Z,C_\epsilon\rangle
=\langle Z,X_*+\epsilon I\rangle
=\epsilon\,\mathrm{tr}Z.
\]
If Z has a positive diagonal compression on any lower grade Ui (wi<1), the lower Loewner estimate for Cε gives
\[
\langle Z,C_\epsilon\rangle\ge
c\epsilon^{w_i}\,\mathrm{tr}(P_{U_i}ZP_{U_i}),
\]
contradicting its order O(ε). Therefore every PSD first stress has zero diagonal on all lower Ui. PSD positivity then forces its entire rows and columns on the lower grades to vanish. Its range lies in Uk, while Z0 is PD there. Thus the maximal first exposed subspace is precisely Uk, and F1=W_(k−1).

**A coefficient stress for EVERY following grade.** The same positive dual path has Puiseux coefficients in K⊥. Fix any j∈{1,...,k}. Its compression to W_j is
\[
P_{W_j}Z_\epsilon P_{W_j}
=\epsilon\,D_{W_j}^{-1}
       [M_\epsilon^{-1}]_{W_j}D_{W_j}^{-1}.
\]
Because Mε→M0≻0, its leading power is ε^(1−w_j); the coefficient at that power is a PD matrix on U_j, zero on W_(j−1). Denote the corresponding full ambient Puiseux coefficient by Q_j∈K⊥. Its **compression to W_j** is therefore PSD and exposes the entire grade U_j, with kernel W_(j−1).

**Greedy induction.** Suppose after a greedy sequence of j−1 steps we know
\(F_{j-1}\subseteq W_{k-j+1}\).
Then the coefficient stress \(Q_{k-j+1}\) has PSD compression on the larger W_(k−j+1), so also on its subspace F_(j−1). Its restriction there is PSD and has kernel exactly
\(F_{j-1}\cap W_{k-j}\), since the grade block U_(k−j+1) is positive definite and Q has zero compression on all lower W_(k−j).
The maximal-rank greedy exposing stress is a relative-interior PSD combination of **all** admissible compressed stresses; its kernel is contained in the kernel of each admissible one (PSD sum property). Hence
\[
F_j\subseteq F_{j-1}\cap W_{k-j}
       \subseteq W_{k-j}.
\]
This proves (92.1) by induction. If no null direction remained, greedy stops earlier; otherwise there is a nonzero exposing stress, since the target minimal face is smaller. Taking j=k gives F_k⊆U0; hence d≤k.

**Rank domination.** Since each greedy face contains U0 and has dimension \(n-\sum_{a\le j}s_a\), while \(W_{k-j}\) has dimension \(r+\sum_{i\le k-j}m_i\), inclusion gives (92.2).

**Maximal depth.** If d=nu, then nu≤k≤nu, hence k=nu and all positive m_i=1. Greedy removes at least one null dimension at each of nu steps, so each s_j=1. Inclusion F_j⊆W_(nu−j) and equal dimensions force equality. QED.

## Interpretation and limits

This gives a **universal finite dominance relation** between canonical Dikin valuations and the *actual* minimum facial-rank profile for arbitrary dense SDP recovery. It cleanly separates:
- primal metric valuation grades (the harmonic weights for the sharp exponent, checkpoint 91);
- dual greedy exposing steps (which may remove grades early, in partial/rotated combinations).

The maximal case d=nu collapses both flags to one common coordinate chain, and the convex-harmonic classification of checkpoint 90 follows. In nonmaximal cases the inclusions in (92.1) can be strict; the central valuation weights and their support matroid alone do not characterize exactly which extra directions can be exposed. The tied-edge 6×6 example of checkpoint75 exhibits this missing dual face-compression coupling.

The theorem therefore supplies **necessary compatibility constraints for the universal exponent/depth profile**, not a complete sufficiency rule at d<nu. A full dense-to-tied-game correspondence would have to represent the rank-dominating extra exposures, including possible non-coordinate rotations and signed cancellations.

The proof uses only the exact universal maxdet envelope and monomial chart (checkpoint89), standard PSD stress complementarity and the finite-dimensional maximal-rank greedy principle (standard facial reduction). No graph universality assumption or arbitrary recovery-curve selection is made.