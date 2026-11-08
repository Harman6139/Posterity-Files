# Milestone 92 — universal FINITE signed Plücker jets capture dense PSD stability AND facial depth; leading tropical data do not

**2026-11-08. PROVED for all arbitrary dense finite-dimensional PSD inverse problems with a uniquely recoverable target.** This is an explicit **finite algebraic/combinatorial normal form** retaining enough weighted matroid data to compute BOTH the sharp exponent and the complete canonical facial-reduction rank profile. It does **not** claim to be a purely discrete two-edge stochastic-game representation or a compact arithmetic catalogue of all (n,r,d,alpha) triples. The minimal extra subleading datum for the six-by-six counterexample is calculated exactly.

## 1. Universal finite weighted Plücker jet

Let L:S^n→R^m uniquely recover X*≽0, and K=ker L have dimension k. By the universal canonical monomial center theorem (checkpoint89), choose a constant orthogonal support-aligned Q and rational weights \theta∈[0,1]^n such that the scaled maxdet center is positive definite in the limit. Define coordinate weights
\[
\eta_{ij}=(\theta_i+\theta_j)/2,\quad i\le j.
\]
Let A∈R^{N×k} be any full-column-rank coordinate matrix for Q^T K Q, N=n(n+1)/2. For each k-element coordinate subset I, let p_I=det A_I (zero if not a matroid basis), and let
\[
m_I=\sum_{(i,j)\in I}\eta_{ij},\quad
M=\max_{p_I\ne0} m_I,\quad
\Delta_I=M-m_I\in[0,k].
\]
Here every individual 0≤η_ij≤1, so every basis weight 0≤m_I≤k and every nonnegative gap satisfies Δ_I≤k.

Define the **FULL SIGNED WEIGHTED PLÜCKER JET**
\[
\boxed{
\mathcal J_{K,Q,\theta}(z)=
\sum_{I:p_I\ne0}p_I z^{\Delta_I}e_I
}
\tag{1}
\]
with Puiseux variable z>0 (choose a common denominator of rational exponents). This has FINITELY MANY monomials and EVERY exponent lies in [0,k]. Its terms at Δ=0 are exactly the initial-Grassmannian Plücker data of checkpoint90. Its strictly positive-order terms encode **subleading coupling constraints** omitted by the initial tropical matroid.

### Theorem A — sufficiency and exact reconstruction

For every z>0 the vector (1) is a nonzero decomposable k-vector, proportional to the Plücker vector of the rescaled kernel
\[
K_z=D_z^{-1}Q^\top KQD_z^{-1}
\quad
(D_z=\operatorname{diag}(z^{\theta_i/2})).
\]
It therefore determines K_z as an exact linear subspace. Applying the known diagonal inverse congruence and Q reconstructs the original K. Consequently the data
\[
\boxed{(X_*,Q,\theta,\ \mathcal J_{K,Q,\theta})}
\tag{2}
\]
are an **exact finite universal normal form for the full measurement-kernel geometry** and hence determine:
- the exact sharp exponent \alpha by the weighted-matroid rank threshold of checkpoints86/89/90;
- the entire canonical maximal-exposing facial-reduction chain, obtained by the finite standard PSD stress-cone/face-compression iteration on the recovered K;
- every minimal exposed rank and the exact singularity degree d.

**Proof:** In the Frobenius-coordinate basis, the linear congruence H↦D_z^{-1}HD_z^{-1} multiplies row e=(i,j) of A by z^{−η_e}. Therefore its k×k minor at I equals
\[
p_I z^{-m_I}=z^{-M}\,p_I z^{M-m_I}.
\]
The common nonzero scalar z^{-M} has no effect on a Plücker point, and the remaining coefficients are precisely (1). All Grassmannian Plücker vectors are decomposable, and a nonzero decomposable k-vector specifies a UNIQUE k-plane. Inverting the known congruence recovers K. The residual norm depends only on K up to finite constants, and the minimal facial chain is determined by K and X*. The sharp exponent follows from the already-proved center-weight/weighted-kernel-rank formula. Thus (2) is complete. QED.

**This is not a tautological repeated storage of full Puiseux central matrices:** the full jet consists ONLY of the finite constant Plücker minors of K with explicit rational monomial weights; it has **no unknown central-path coefficients**, no semidefinite optimization in its construction, and no infinite expansion. The nontrivial central weight vector can itself be found using the strictly feasible initial Plücker/PSD tests of checkpoints90–91.

## 2. The leading initial matroid alone provably loses facial depth

Consider the paired six-by-six rational PSD problems of checkpoints87–88. They have the same target, same kernel dimension k=5, same strict canonical weight vector
\[
\theta=(0,3/11,6/11,7/11,9/11,1),
\]
and same leading initial Plücker subspace K0 (so the zeroth-order jet Δ=0 is identical). They also have the same full leading normalized maxdet center and Hessian, and the same sharp recovery exponent 3/22, but different exact minimal facial degrees 4 and 3.

Their four ordinary internal generators and optional G are:
\[
\begin{aligned}
H_1&=E_{11}-E_{00}+\lambda F_{02},\\
H_2^{\rm base}&=E_{22}-E_{00}+\lambda F_{14},\\
H_2^{\rm tied}&=E_{22}-E_{00}+\lambda(F_{14}+F_{05}),\\
H_3&=E_{33}-E_{00}+\lambda F_{15},\\
H_4&=E_{44}-E_{00}+\lambda F_{35},\\
G&=\lambda F_{01},\qquad \lambda=1/100.
\end{aligned}
\]

For the five-column kernel basis (H1,H2,H3,H4,G), the maximal Plücker weight is
\[
M=w_1+w_2+w_3+w_4+w_1/2=53/22,
\]
witnessed by choosing coordinate rows
\[
I_0=\{E_{11},E_{22},E_{33},E_{44},F_{01}\}.
\]
In raw symmetric-entry coordinates, the minor coefficient is
\[
p_{I_0}=\pm\lambda\ne0
\]
in BOTH problems.

Now replace the pivot row E22 by the tied offdiagonal coordinate F05:
\[
I_1=\{E_{11},F_{05},E_{33},E_{44},F_{01}\}.
\]
Its weight is
\[
m_{I_1}=M-\left(w_2-\tfrac{w_0+w_5}{2}\right)
       =M-\frac1{22}.
\]
In the independent-edge base problem, F05 is absent from every generator, so
\[
p_{I_1}^{\rm base}=0.
\]
In the tied problem, H2 has an extra F05 coefficient λ, giving
\[
p_{I_1}^{\rm tied}=\pm\lambda^2\ne0.
\]
Hence the two full signed Plücker jets agree **exactly at all leading Δ=0 coordinates**, but differ at the **first strictly positive Puiseux order**
\[
\boxed{\Delta=1/22.}
\tag{3}
\]
Since all coordinate weights are multiples of 1/22, no positive-order Plücker gap smaller than 1/22 exists. Thus the first subleading jet is the **earliest possible place** to distinguish these two systems in this weighted Plücker representation.

This one extra rational minor is precisely the tied-edge coefficient that changes canonical exposing layers from
\[
\{5\},\{3,4\},\{2\},\{1\}
\quad(d=4)
\]
to
\[
\{5\},\{2,3,4\},\{1\}
\quad(d=3),
\]
while leaving the complete leading Dikin metric and \alpha unchanged.

**Minimal richer model for THIS counterexample:** zeroth-order tropical Plücker data are insufficient; recording the **first nonzero subleading signed Plücker coefficient at order 1/22** suffices to distinguish the decisive tied constraint. In the sparse incidence hierarchy this is the single two-edge generator H2^tied, and the full tied-edge min–max/AND–OR game computes both invariants exactly. This is a *minimality statement for this explicit pair*, not a proof of globally minimal complexity for every dense kernel.

## 3. Significance for the dense-to-tied-game conjecture

The full jet (1) is a **genuinely universal dense-kernel algebraic-combinatorial model**: all coefficient dependencies, arbitrary signs, overlaps, cancellations, and facial compressions are retained. It has finite size \(\binom{N}{k}\) and finite rational order bound Δ≤k; in particular it cannot miss a determinant of arbitrarily high *relative* Puiseux order within the weighted entry range.

However the complete jet stores NUMERICAL Plücker coefficients, not only discrete parent-edge incidences. It does not prove that its associated (alpha,facial-rank-profile) can always be reproduced by a bounded two-mode/two-edge Shapley game at the same nullity. That last strong *purely combinatorial incidence realization* remains OPEN.

Checkpoint90 gives a finite strict primal–dual conic criterion for the leading Δ=0 tier; checkpoint91 proves the central weights are isolated rational vertices of the associated Plücker fan and gives a uniform denominator bound. Together with (1), these yield a complete, rigorous **finite signed-matroid plus conic-depth tower** normal form for arbitrary dense PSD recovery.

## Reproducibility

An exact Fraction/SymPy checker can compute p_(I0),p_(I1), M and the 1/22 gap and compare the known exposing layers. No approximate eigenvalue fitting or genericity arguments are needed.

## Scope discipline

This solves the **instance-wise** universal representation problem by a finite signed valued Plücker jet, not the stronger user's original desire for a **compact purely combinatorial iff spectrum at every prescribed (n,r,d)**. The full jet can be exponentially large and contains real algebraic coefficients. Existing Grassmannian/Plücker theory is classical; no originality claim is made for those concepts, only for the explicit stability-depth bridge and its precise proof.
