# Milestone 88 — identical LEADING NORMALIZED CANONICAL CENTER and barrier Hessian, but distinct PSD facial degrees

Date: 2026-11-08. **PROVED for explicit rational 6×6 data.** This strengthens checkpoint 87: not merely the central/Hessian *eigenvalue valuations*, but the **entire leading positive-definite normalized maxdet center matrix and its full scaled Hessian matrix** coincide in two problems with distinct minimal facial-reduction degrees. The first difference in the normalized affine pencils is exactly at Puiseux order ε^(1/22), carried by one tied edge.

## 1. Explicit paired affine sections

Use the two 6×6 kernels from checkpoint 87, both with X*=E00, lambda=1/100, and K spanned by H1,H2,H3,H4,G, where

    H1=E11-E00+lambda F02,
    H3=E33-E00+lambda F15,
    H4=E44-E00+lambda F35,
    G=lambda F01,

and H2 differs:
    H2_base=E22-E00+lambda F14,
    H2_tied=E22-E00+lambda(F14+F05).

The exact common Bellman weights are (w0,w1,w2,w3,w4,w5)=(0,3/11,6/11,7/11,9/11,1), and both sharp full-matrix exponents are α=3/22. Their exact greedy facial profiles are respectively (1,2,1,1), d=4, and (1,3,1), d=3, as proved in checkpoints 75/87.

Let ε=t^22, t>0, and define the common diagonal scaling
\[
D_t=\operatorname{diag}(1,t^3,t^6,t^7,t^9,t^{11}).
\]
For either K, the canonical shifted maximum-determinant center has the form
\[
C_t=E_{00}+t^{22}I
      +t^6\theta_1H_1+t^{12}\theta_2H_2
      +t^{14}\theta_3H_3+t^{18}\theta_4H_4
      +t^3\theta_G G,
\]
where the vector θ=θ(t) of five scaled coefficients is chosen to maximize logdet C_t.

Because det C_t=(det D_t)^2 det(D_t^{-1}C_tD_t^{-1}), this is equivalent to maximizing logdet of the normalized affine matrix
\[
M_t^{\rm base}(\theta)=M_0(\theta)+R_t(\theta),
\]
where the COMMON t=0 limit is explicitly
\[
M_0(\theta)=
\begin{pmatrix}
1&\lambda\theta_G&\lambda\theta_1&0&0&0\\
\lambda\theta_G&\theta_1&0&0&\lambda\theta_2&\lambda\theta_3\\
\lambda\theta_1&0&\theta_2&0&0&0\\
0&0&0&\theta_3&0&\lambda\theta_4\\
0&\lambda\theta_2&0&0&\theta_4&0\\
0&\lambda\theta_3&0&\lambda\theta_4&0&1
\end{pmatrix},
\tag{1}
\]
and R_t(θ) consists entirely of common entries with strictly positive t powers: its diagonal entries are
    R00=t^22−t^6 θ1−t^12 θ2−t^14 θ3−t^18 θ4,
    R11=t^16, R22=t^10, R33=t^8, R44=t^4, R55=0,
with no other nonzero entries. The TIED problem differs by EXACTLY ONE additional entry:
\[
\boxed{M_t^{\rm tied}(\theta)-M_t^{\rm base}(\theta)
        =\lambda\theta_2\,t\,F_{05}.}
\tag{2}
\]
Thus both normalized affine pencils have exactly the same constant coefficient M0(θ); the new relation appears only at t=ε^(1/22).

## 2. Both normalized analytic-center coefficient vectors converge to the SAME θ*

The Dikin–Bellman Loewner theorem (checkpoint 86) gives for BOTH kernels fixed c,C>0 independent of t:
\[
cI\preceq D_t^{-1}C_tD_t^{-1}\preceq CI.
\tag{3}
\]
In particular their five scaled coefficient vectors θ(t) stay bounded: θ_i is the normalized i-th diagonal entry up to a vanishing known diagonal term and θ_G is the (0,1) entry divided by lambda.

Let the limiting feasible cone section be
\[
\mathcal M=\{\theta\in\mathbb R^5:M_0(\theta)\succeq0\}.
\]
It contains a positive definite point, e.g. θ1=...=θ4=1, θG=0, since lambda=1/100 and the normalized matrix is strictly diagonally dominant. Its determinant-maximization problem has a unique positive-definite maximizer θ*:

- **Compactness:** from the principal 2x2 inequalities of M0≽0, using the explicit edges, one gets
  θ1²≤lambda^-2 θ2,
  θ2²≤lambda^-2 θ1 θ4,
  θ3²≤lambda^-2 θ1,
  θ4²≤lambda^-2 θ3.
  These imply uniform upper bounds on θ1,...,θ4; θG²≤lambda^-2 θ1 from the (0,1) minor. (All θ_i are nonnegative by PSD diagonals.) Thus M is compact.
- **Existence:** det M0 is continuous on the compact set and positive at θ=(1,1,1,1,0), so its maximizer lies in M0≻0.
- **Uniqueness:** the affine map θ↦M0(θ) is injective because the four internal diagonal entries and the independent (0,1) edge recover all θ. Logdet is strictly concave on positive-definite matrices, hence strictly concave in θ on the feasible interior. Therefore θ* is unique.

For any fixed θ with M0(θ)≻0, both M_t^base(θ) and M_t^tied(θ) remain PD for sufficiently small t, and their determinants converge to det M0(θ). Because θ_base(t),θ_tied(t) are maximizers and bounded, any subsequential limit θbar satisfies M0(θbar)≽0 and det M0(θbar) at least det M0(θ) for every interior θ. Density of the interior in M gives θbar=θ*. Thus BOTH scaled center coefficient vectors converge to θ*, proving
\[
\boxed{
\lim_{t\downarrow0}D_t^{-1}C_t^{\rm base}D_t^{-1}
=
\lim_{t\downarrow0}D_t^{-1}C_t^{\rm tied}D_t^{-1}
=M_0(\theta_*)\succ0.}
\tag{4}
\]

## 3. The complete leading scaled restricted Hessian matrices also coincide

Let θ coordinates correspond to the five constant kernel generator directions. Define the rescaled tangent matrices
\[
A_i^{(\cdot)}(t)
 = \partial_{\theta_i} M_t^{(\cdot)}(\theta)
\]
and the 5x5 normalized logdet Hessian
\[
\widehat G^{(\cdot)}_{ij}(t)
=\mathrm{tr}\left(
 (M_t^{(\cdot)}(\theta_{(\cdot)}(t)))^{-1}
 A_i^{(\cdot)}(t)
 (M_t^{(\cdot)}(\theta_{(\cdot)}(t)))^{-1}
 A_j^{(\cdot)}(t)\right).
\]
The two affine pencils have the same limiting coefficient directions A_i(0)=∂_θi M0(θ), since the tied F05 term is λtθ2. Their normalized central matrices have the same PD limit (4). Continuity of inversion and trace therefore gives
\[
\boxed{
\lim_{t\downarrow0}\widehat G^{\rm base}(t)
=
\lim_{t\downarrow0}\widehat G^{\rm tied}(t)
=
\bigl[\mathrm{tr}(M_0(\theta_*)^{-1}
A_i(0)M_0(\theta_*)^{-1}A_j(0))\bigr]_{ij}.
}
\tag{5}
\]
The common limit is PD because the five matrices A_i(0) are linearly independent.

In fact both θ(t) solve analytic stationarity equations ∇_θ logdet M_t=0, with strictly PD Hessian at t=0. The analytic implicit-function theorem gives θ_base(t), θ_tied(t) real-analytic near t=0, and (2) shows the first possible discrepancy occurs at order O(t). Thus the normalized full centers and Hessians have identical constant Puiseux jets, despite distinct facial degrees.

## 4. Interpretation: what a universal dense-to-game bridge MUST preserve

The Dikin radius and all its *spectral* asymptotics read the leading normalized analytic-center metric. This is enough for the sharp recovery exponent. But the linked facial degree depends on **subleading coefficient-incidence relations** that can disappear in the normalized t→0 leading matrix. Here F05 appears only as lambda θ2 t F05 but becomes an essential off-face dual cancellation after first exposing e5.

Therefore:

- A classification using only the leading tropical center, full Dikin spectrum, and leading reduced Hessian can NEVER reconstruct the facial degree for arbitrary PSD recovery; explicit rational counterexamples have identical such data and different degree.
- A potential universal tied-game reduction must preserve **the complete dual face-compression incidence tower**, or an equivalent signed/valuated matroid with *subleading* Plücker/circuit data, not merely its dominant exponents.
- The smallest richer incidence gadget needed in this example is a single generator with **two tied edges**: the dominant (1,4) edge and the subleading yet dual-decisive (0,5) edge. Independent-edge two-policy models were shown insufficient at the same nullity/depth/exponent in checkpoint 75.

This is a rigorous Dikin–Hessian explanation of the failure of the earlier two-policy model, not a proof that the tied-edge MIN–MAX model is universal for all dense kernels.

## Proof audit/novelty

Only the universal analytic-center Loewner sandwich (checkpoint 86), elementary principal-minor inequalities, strict concavity of logdet and finite-dimensional continuity/analytic implicit-function theory are used. All matrix entries and the size 6 are explicit and rational before the scalar center maximization. No numerical optimization or unproved genericity assumption appears. The analytic-center technique itself is classical; novelty of this precise two-system observation has not been externally checked.
