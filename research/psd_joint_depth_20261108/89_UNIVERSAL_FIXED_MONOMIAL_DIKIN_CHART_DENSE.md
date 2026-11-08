# Milestone 89 — every dense PSD maxdet center has a FIXED monomial Loewner chart

**2026-11-08. NEW, self-contained theorem for arbitrary real finite-dimensional PSD measurement kernels with a uniquely recoverable PSD target, positive target rank and singular nullity.** This REMOVES the chart assumption in checkpoint 86: the intrinsic Dikin weighted-support formula now applies to EVERY dense inverse problem. It does **not** assert that a chart's scalar weights, by themselves, determine the minimal facial-reduction degree; checkpoints 87–88 show they do not. Nor does it prove dense-to-tied-game realizability at unchanged dimension/profile.

## Theorem

Let L:S^n→R^m be real linear, let X*≽0 be its unique PSD inverse image under L, K=ker L, and q=||L I||>0. For ε>0 let
\[
C_\epsilon=\arg\max\{\log\det X:\ X\succ0,\ X-X_*-\epsilon I\in K\}.
\]
There exist a **fixed** orthogonal decomposition
\[
\mathbb R^n=U_0\oplus U_1\oplus\cdots\oplus U_k,
\quad U_0=\operatorname{range}X_*,
\]
and positive rational exponents
\[
0=w_0<w_1<\cdots<w_k=1
\]
such that, writing \(D_\epsilon=\bigoplus_i\epsilon^{w_i/2}I_{U_i}\),
\[
\boxed{ cD_\epsilon^2\preceq C_\epsilon
                      \preceq CD_\epsilon^2 }
\tag{1}
\]
for all sufficiently small ε, with constants c,C>0. The decomposition is obtained entirely from the Puiseux leading positive compressions of the one *canonical* center; it is independent of ε, even if its eigenvectors rotate with ε.

For any fixed Frobenius-orthonormal coordinates adapted to these U_i put
\[
\eta_{ab}=\tfrac12(w_{i(a)}+w_{i(b)}),\qquad
\tau(K,w):=\min_{H\in K\setminus\{0\}}\ 
              \max_{\{a,b:H_{ab}\ne0\}}\eta_{ab}.
\tag{2}
\]
Then the exact full ambient PSD recovery modulus satisfies
\[
\boxed{
\omega_{\mathcal L,X_*}(q\epsilon)
   =\Theta(\epsilon+\epsilon^{\tau(K,w)}),\qquad
\alpha(\mathcal L,X_*)=\min\{1,\tau(K,w)\}.
}
\tag{3}
\]
When K={0} set τ=+∞ and α=1. Formula (2) is a **finite ordinary linear-rank test**: τ is the least weight threshold u for which the coordinate-projection map from K onto entries of weight greater than u has nonzero kernel. All weights are rational; no numerical spectral fitting, genericity, arbitrary recovery-path search or sparse graph hypothesis is used.

### 1. Maxdet center exists, converges to X*, and has finite Puiseux data

Uniqueness gives \(K\cap S_+^n=\{0\}\). Strict PSD separation supplies \(W\succ0\) in \(K^\perp\), so every affine slice \(X_*+\epsilon I+K\) of PSD matrices is bounded. It contains \(X_*+\epsilon I\succ0\); logdet is strictly concave and tends to \(-\infty\) at its boundary, so Cε exists uniquely. The stationarity equations are polynomial after clearing denominators:
\[
C_\epsilon-X_*-\epsilon I\in K,\quad
\operatorname{adj}(C_\epsilon)\in K^\perp,\quad C_\epsilon\succ0.
\]
The graph ε↦Cε is semialgebraic (even with arbitrary fixed real coefficients), hence each matrix entry has a convergent real Puiseux expansion near ε=0+. All cluster points satisfy the exact measurements of X*, so boundedness and uniqueness imply Cε→X*.

The elementary stationarity identity
\[
n=\langle C_\epsilon^{-1},X_*\rangle
  +\epsilon\,\operatorname{tr}C_\epsilon^{-1}
\]
implies \(C_\epsilon\succeq(\epsilon/n)I\).

### 2. Canonical FIXED orthogonal valuation flag

Start with U0=range X*. Compress Cε to U0^\perp. Its first nonzero Puiseux coefficient is a nonzero PSD matrix A_{w1}, because the compression is PSD for every ε and tends to zero. Let U1 be the range of that coefficient, a fixed positive-dimensional subspace; its restriction to U1 is PD. Compress to the kernel of A_{w1} inside U0^\perp and repeat, defining U2,...,Uk. Every stage strictly lowers dimension, so k<=n-r. Since Cε≽εI/n, all positive diagonal orders are <=1; since Cε→X*, they are >0. Successive nonzero leading orders strictly increase, giving 0<w1<...<wk<=1. In each Ui the first diagonal coefficient at ε^{wi} is positive definite and all lower powers vanish.

**Why the final weight is exactly one.** Suppose \(w_k<1\). Truncate the Puiseux series at \(w_k\) and rescale its coefficients as in the finite PSD coefficient-rescaling lemma in the next section. Every positive diagonal block has its strictly PD leading coefficient by weight \(\le w_k\); all offdiagonal entries meet the order restrictions. The resulting polynomial is PD for small ε, but ALL of its nonconstant coefficients have orders \(e\le w_k<1\) and hence lie in \(K\) by the shifted affine equation. It would be a **nonconstant exact feasible PSD curve** \(X_*+K\), contradicting uniqueness. Therefore \(w_k=1\). This step is indispensable for the monomial chart and is not inferred merely from \(C_\epsilon\succeq\epsilon I/n\), which gives only \(w_k\le1\).

For any fixed vectors u∈Ui, v∈Uj, PSD Cauchy–Schwarz gives
\[
|u^\top C_\epsilon v|
\le\sqrt{u^\top C_\epsilon u}\,
     \sqrt{v^\top C_\epsilon v}
=O(\epsilon^{(w_i+w_j)/2}).
\]
Hence if
\[
C_\epsilon=X_*+\sum_{e>0}A_e\epsilon^e
\]
is its Puiseux series, then each coefficient A_e has zero (Ui,Uj)-block whenever \(2e<w_i+w_j\). The same applies to blocks touching U0 of weight zero.

### 3. The rescaled coefficient lemma creates a PD lower chart

**Lemma (finite PSD coefficient rescaling).** Let V=⊕Vi, weights a_i all distinct, and let a finite generalized polynomial
\(P(t)=\sum_e t^e B_e\) have a strictly positive definite first diagonal coefficient at exponent a_i on Vi, with all blocks forbidden when \(2e<a_i+a_j\). Then for sufficiently large fixed σ,
\[
P_\sigma(t)=\sum_e e^{\sigma e^2}t^e B_e
\]
is PD for small t>0.

**Proof:** Congruence by \(\bigoplus_i e^{-\sigma a_i^2/2}t^{-a_i/2}I_{V_i}\) yields a matrix whose diagonal blocks converge to the fixed PD leading coefficients B_{a_i}|Vi. A normalized cross block (i,j), i≠j, can survive in the limit only for \(e=(a_i+a_j)/2\); its constant multiplier equals
\[
\exp\{\sigma[(a_i+a_j)^2/4-(a_i^2+a_j^2)/2]\}
=\exp\{-\sigma(a_i-a_j)^2/4\}\to0.
\]
All higher-order terms vanish as t→0. For σ large the limiting block matrix is PD, hence Pσ(t) is PD for sufficiently small t. QED.

Apply the lemma to the FINITE truncation of the actual center's Puiseux expansion through exponent one:
\[
Y_\epsilon^{(\sigma)}=
X_*+\sum_{0<e\le1}e^{\sigma e^2}A_e\epsilon^e.
\tag{4}
\]
All w_i<=1, so every diagonal leading coefficient is included. The lemma makes Yε^σ PD and proves
\[
Y_\epsilon^{(\sigma)}\succeq c_0D_\epsilon^2
\tag{5}
\]
for all sufficiently small ε (the source block's exponent zero is unchanged).

Because \(C_\epsilon-X_*-\epsilon I\in K\), coefficient comparison shows
\[
A_e\in K\quad(e<1),\qquad A_1-I\in K.
\]
Therefore the newly constructed PD curve has measurement residual
\[
\|L(Y_\epsilon^{(\sigma)}-X_*)\|
=e^\sigma\epsilon\|L I\|
=e^\sigma q\epsilon.
\tag{6}
\]
This exact identity is what makes the rescaling legitimate for the original inverse problem: no coefficient of order less than ε leaves the invisible kernel.

### 4. A universal analytic-center Loewner envelope transfers the PD lower chart

The previously proved maxdet Loewner envelope (checkpoint 09, with a self-contained proof) states that for ANY PSD Y with measurement residual δ,
\[
0\preceq Y\preceq n(1+\kappa\delta/\epsilon)C_\epsilon,
\tag{7}
\]
where κ is a fixed norm of a right inverse for L* on K^\perp. The proof sets \(Z=\epsilon C_\epsilon^{-1}\in K^\perp_+\), uses \(\mathrm{tr}Z\le n\) and \(<Z,X_*>\le n\epsilon\), and estimates \(<Z,Y>\) by the measurement residual; order-congruence by Cε^{-1/2} completes it.

Apply (7) to Yε^σ with δ=e^σqε. Combining with (5) gives
\[
C_\epsilon\succeq
\frac{c_0}{n(1+\kappa e^\sigma q)}D_\epsilon^2.
\tag{8}
\]

For the upper bound, the diagonal blocks of Cε on each Ui are \(O(\epsilon^{w_i})\); hence the PSD matrix \(D_\epsilon^{-1}C_\epsilon D_\epsilon^{-1}\) has uniformly bounded trace, and therefore is bounded above by its trace times I. Thus
\[
C_\epsilon\preceq C D_\epsilon^2,
\]
completing (1).

### 5. Dikin Hessian becomes EXACTLY a weighted kernel matroid rank test

The universal Dikin–Hessian recovery modulus theorem (checkpoint 10) gives
\[
\omega(q\epsilon)\asymp\epsilon+\rho_\epsilon,\qquad
\rho_\epsilon^{-2}
=\min_{\substack{H\in K\\\|H\|_F=1}}
 \mathrm{tr}(C_\epsilon^{-1}HC_\epsilon^{-1}H).
\]
Loewner sandwich (1), including the corresponding Kronecker product order, makes the Dikin quadratic form equivalent to
\[
N_\epsilon(H)^2
=\|D_\epsilon^{-1}HD_\epsilon^{-1}\|_F^2
=\sum_{a,b}|H_{ab}|^2
   \epsilon^{-(w_{i(a)}+w_{i(b)})}.
\]
Let τ be (2). A nonzero H0∈K achieving the finite minimum has no entry whose weight exceeds τ, so \(N_\epsilon(H_0)\le C\epsilon^{-\tau}\|H_0\|\). Conversely, the map projecting K onto entries of weight at least τ is injective (otherwise a nonzero H would have maximum support weight <τ); finite-dimensional injectivity gives
\[
\|P_{\eta\ge\tau}H\|_F\ge c\|H\|_F.
\]
Consequently \(N_\epsilon(H)\ge c\epsilon^{-\tau}\|H\|\) for all H∈K. Thus
\[
\rho_\epsilon=\Theta(\epsilon^\tau)
\]
and (3) follows.

## Interpretation and limitations

**What is universal now:** The fixed orthogonal monomial Loewner chart and *exact kernel support-rank exponent formula* work for EVERY dense PSD inverse map, even with moving eigenvectors. The formerly conditional chart assumption in checkpoint 86 has been removed, without sparse normal forms or stochastic games.

**What is NOT universal yet:** The weights and support matroid determine the sharp EXPONENT, but not the minimal facial-reduction degree: explicit six-by-six pairs in checkpoints 87–88 have identical leading normalized centers/Hessians and exponents but distinct degrees, because a subleading tied edge changes off-face dual stress cancellation. To classify all exponent/degree pairs at fixed nullity, one must additionally encode the **dual face-compression tower**, not merely the scalar valuations of the monomial metric. This theorem does NOT prove that every such tower can be represented by a tied-edge game at unchanged nullity.

**Potential next step:** Combine this chart's actual linear-matroid graded kernel data with canonical first-stress limits, and ask whether its signed circuit compression supports admit bounded tied-edge game certificates. This is the unresolved dense-to-game universality theorem; a counterexample may require a still richer determinant-aware gadget. The instance-wise universal Dikin–Hessian classifier and the real-algebraic all-degree decision procedure remain valid regardless.

## Novelty discipline

Puiseux expansions of semialgebraic curves, maxdet analytic centers and Dikin ellipsoids are classical techniques. The precise global monomial Loewner chart and matroid rank reduction are proved above, but their bibliographic priority is not independently established.
