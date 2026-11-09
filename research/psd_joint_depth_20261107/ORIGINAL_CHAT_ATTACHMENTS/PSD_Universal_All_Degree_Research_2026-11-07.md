# Universal PSD stability: an all-degree decision theorem and unrestricted-dimension joint realizations

**Research memorandum, 7 November 2026.** This memorandum distinguishes an *all-degree finite decision theorem* from the stronger, still unproved *closed combinatorial spectrum at each fixed nullity*. No dense-to-sparse depth-preserving universality is assumed.

## 1. Main new theorem: any interior rational exponent at any permitted exact depth

Let `L: S^n -> R^m` be linear and `X_*` PSD and uniquely determined by its measurement. Write `sd(L,X_*)` for the smallest number of semidefinite facial-reduction steps to reach `range X_*`, and `alpha(L,X_*)` for the optimal full Frobenius recovery exponent.

**Theorem A.** For every `d>=2`, `r>=1` and rational `alpha` satisfying

\[
2^{-d}\le\alpha<1/2,
\]

there is a finite-dimensional **rank-`r` target** and a measurement map with **exact singularity degree `d`** and **exact optimal Hölder exponent `alpha`**. The construction is explicit, with rational coefficients and rational weight exponents, and the upper estimate covers all ambient PSD matrices. The matrix dimension is not claimed minimal.

The only standard necessary ingredients are `alpha>=2^{-d}` (Sturm) and the universal PSD tangent-cone alternative `alpha=1` or `alpha<=1/2`. Therefore, for unrestricted matrix size, Theorem A leaves only the endpoint `alpha=1/2` at depths `d>=3` undecided. At depth 1, only `{1,1/2}` occurs; at depth 2, the entire interval `Q cap [1/4,1/2]` occurs.

### Sparse harmonic PSD construction

Take a finite network with source `O` of weight 0, at least one terminal of weight 1, and intermediate vertices `v` with weight `w_v in (0,1)`. Each intermediate vertex has two distinct parents satisfying `2w_v=w_a+w_b`. Each distinct intermediate vertex has a distinct parent edge. Multiple subnetworks may share `O` while all other vertices remain disjoint.

Use a symmetric pencil whose diagonal entries are the free variables `x_v`, and whose off-diagonal entry at parent edge `(a,b)` of vertex `v` is `lambda*x_v`, `lambda=1/(4N)`, `N` the total number of vertices. All other off diagonal entries are zero. If a desired leading exponent `alpha` lies strictly below every intermediate weight but `2alpha` is a vertex weight, introduce a free off-diagonal entry `lambda*z` on the unused source-to-`2alpha` edge.

Let `V` be the range of this pencil. Measure `(P_{V^perp}X, tr(X), terminal diagonal coordinates)` and use target `E_OO`. For any `X PSD` with measurement residual at most `delta`, its projection `Y=P_V X` satisfies `Y+delta I PSD`, all coordinates are bounded, and each terminal coordinate is `O(delta)`. Principal `2x2` minors imply

\[
(|x_v|+\delta)^2 \le C (|x_a|+\delta)(|x_b|+\delta).
\]

Taking logarithms and inverting the finite transient harmonic Markov matrix gives `|x_v|<=C_v delta^{w_v}`. The optional edge gives `|z|<=C delta^alpha`; the trace controls the source diagonal. This proves the full ambient upper recovery bound. Conversely `x_v=t^{w_v}`, terminal `x_T=t`, `z=t^alpha` and trace normalization gives a PSD sharpness curve: after diagonal congruence the matrix has all diagonal entries 1 and off-diagonal magnitude at most `lambda`, hence is strictly diagonally dominant. Residual is comparable to `t` and the displacement has the prescribed order.

### Exact facial peeling

At a coordinate face with remaining vertex set `W` containing `O`, a stress orthogonal to the kernel must satisfy

\[
Z_{vv}+2\lambda Z_{a(v)b(v)}=0,
\qquad Z_{OO}=0,
\]

for every intermediate vertex, and must vanish on any optional source edge. An exposable vertex set `C subset W\setminus{O}` obeys: if `v in C` and **both** of its parents are still in `W`, then **both** parents must belong to `C`. The largest such `C` is computed by iterative deletion from `W\setminus{O}`. A PSD exposing stress cannot remove vertices outside `C`, since any nonzero off diagonal entry in a PSD compression requires both diagonal entries positive. Conversely choose `Z_vv=epsilon^{-w_v^2}` for `v in C` and zero otherwise, and use the kernel orthogonality equations to fix the parent-edge entries. Off-face entries are free. After normalization by the square roots of the positive diagonals, an within-face parent-edge entry has magnitude

\[
(2\lambda)^{-1}\epsilon^{(w_a-w_b)^2/4}\to0.
\]

For sufficiently small `epsilon`, the face compression is positive definite exactly on `C`, so the entire `C` is exposed in one step. Greedy maximal exposure is shortest by induction comparing it with arbitrary competing chains. The **exact minimal facial-reduction depth** equals this graph peeling count.

For graphs glued at the source, the sharp exponent is the minimum of the component exponents, and the minimal peeling depth is the maximum of the component depths. The latter follows because candidate peeling sets factor into the components.

### Dyadic spine of its natural depth

Given rational `alpha<1/2`, choose the smallest integer `e>=2` with `2^{-e}<=alpha` and `alpha<=2^{-(e-1)}` and set `c=2^{-(e-1)}`. Include dyadic intermediate weights `1/2,1/4,...,c` with the parent equations `2*2^{-j}=0+2^{-(j-1)}`. Write `2alpha=c+(1-c)a/b` reduced, and include all grid values `c+j(1-c)/b`, `j=1,...,b-1`, with immediate grid neighbors as parents. If a grid value coincides with a dyadic spine value, retain the spine parent equation. This is a valid finite mediated network with minimum intermediate weight `c>=alpha` and with `2alpha` a vertex. If `alpha<c`, add the optional leading source edge; otherwise the minimum spine variable is the leading perturbation.

Its peeling degree is **exactly `e`**, because the terminal and then the dyadic spine vertices become available successively. At the last spine step all remaining grid vertices become simultaneously available, as none has source `O` as a parent. Its exponent is exactly `alpha`.

### A depth-d helper approaching one-half

Fix `d>=3`, `s=d-3`, `m>=1` and define

\[
q=\frac{2^s}{2^s+1},\qquad
\beta_{d,m}=\frac{1-q^m}{2-q^m},\qquad
x_i=1-q^i(1-\beta_{d,m})\quad (0\le i\le m).
\]

Make a root vertex `R` of weight `x_0=beta`, core vertices `X_i` of weights `x_i`, and terminal `T` of weight 1. The root's parents are `(O,X_m)`; indeed `x_m=2 beta`. For `s=0`, the core vertex `X_i` has parents `(X_{i-1},T)` with `X_0=R`.

For `s>=1`, add support vertices `Y_{i,j}` (`1<=i<=m`, `1<=j<=s`) with

\[
y_{i,j}=x_i+2^{-(s-j+1)}(1-x_i).
\]

Give `X_i` parents `(X_{i-1},Y_{i,1})`, give `Y_{i,j}` parents `(X_i,Y_{i,j+1})` if `j<s`, and give `Y_{i,s}` parents `(X_i,T)`. All are exact midpoint identities, all weights are distinct, and the minimum weight is `beta`. Peeling removes terminal `T`, then each support layer `Y_{i,s},...,Y_{i,1}`, then all core vertices, then root `R`: exactly `s+3=d` steps. Hence this network has depth `d` and exponent `beta_{d,m}`, and

\[
\beta_{d,m}\nearrow1/2\qquad(m\to\infty).
\]

The pairwise distinctness follows from 2-adic valuations of powers of `q` versus the quantities `1-2^{-k}` (any potential one-step valuation coincidence still has different odd numerators).

### The gluing conclusion

For given `d>=e`, if `d=e` use the spine alone. Otherwise choose `m` with `beta_{d,m}>alpha` and glue the spine with the helper at their source. The resulting exact exponent is `min(alpha,beta)=alpha`, and the exact minimal depth is `max(e,d)=d`. Add a completely observed positive definite block and all cross entries to raise the target rank to any prescribed `r`.

One explicit dimension estimate is:

\[
\nu\le\begin{cases}
e+b-1,&d=e,\\
e+b+1+(d-2)m,&d>e,
\end{cases}
\]

where `b` is the denominator of `(2alpha-c)/(1-c)` in lowest terms, and `m` is any positive integer with

\[
\left(\frac{2^{d-3}}{2^{d-3}+1}\right)^m < \frac{1-2\alpha}{1-\alpha}.
\]

This proves Theorem A, including explicit full-matrix upper bounds and sharp curves, and exact minimal facial depth.

## 2. Canonical greedy facial reduction for arbitrary dense maps

Write `K=ker L`, `U=range X*`. For every face supported on `W superset U`, let

\[
\mathcal C_W=\{P_W ZP_W:Z\in K^\perp,\ \langle Z,X_*\rangle=0,\ P_WZP_W\succeq0\}.
\]

Let `G(W)=W intersect (intersection of ker S for S in C_W)`. A sum of finitely many PSD matrices in `C_W` has kernel exactly that intersection, so `G(W)` is reachable by one exposing step. If `G(W)=W` and `W` properly contains `U`, the semidefinite theorem of the alternative contradicts uniqueness, since `X_*` lies in a proper face of `S_+(W)`.

The iteration `W_0=R^n`, `W_{j+1}=G(W_j)` is canonical and terminates at `U`. It is **shortest**: if another chain has faces `V_j`, then by induction `W_j subset V_j`; a valid exposing stress on `V_j` compresses to a valid stress on `W_j`, so `W_{j+1} subset V_{j+1}`. Thus its number of steps is precisely the singularity degree.

This is an intrinsic dense-map depth calculation. The maximum stress support at each step is the semidefinite analogue of the greedy sparse peeling set.

## 3. Complete all-degree *algorithmic* joint classification, without sparse universality

This is a separate exact decision theorem. It does not require a sparse graph to preserve the degree of an arbitrary dense instance.

Fix matrix size `n`, target rank `r>=1`, `nu=n-r>=1`, prescribed degree `d` between 1 and `nu`, and write `N=n(n+1)/2`. Represent an unknown kernel `K` by a symmetric idempotent `N x N` orthogonal projector `Pi` on the space of symmetric matrices. Then `H in K` means `Pi H=H`, while `Z in K^perp` means `Pi Z=0` (in fixed orthonormal matrix coordinates). Set `X*=diag(I_r,0_nu)`.

**Finite candidate exponent set.** Enumerate all partitions of the null space into at most `nu` nonzero ordered diagonal-weight blocks, all possible permitted supports of their kernel coefficient matrices, and an optional off-diagonal-leading coefficient. The PSD block-order constraints are rational linear inequalities

\[
2w_i\ge w_j+w_k
\]

for each permitted block of each coefficient. Require strictly ordered weights, one terminal weight equal to 1, and either leading `p=w_1` or `0<p<w_1`. Discard weight systems with no strict feasible point; solve the closed rational LP minimizing `p`. The finite set of their positive rational optimal values, together with `1`, is `A_nu`.

For each discrete weighted pattern `P`, let `Geo_P(Pi)` mean: there exist orthogonal weighted flag projectors and at most `nu` symmetric coefficient matrices `H_i` in `range Pi`, with zero forbidden blocks and positive definite indicated diagonal compressions, and (in off-diagonal-leading mode) a nonzero leading kernel matrix with its forbidden blocks zero. This is a finite existential polynomial predicate; the weight LP optimum `lambda_P` is already precomputed.

The earlier weighted-flag arc reduction and PSD coefficient-rescaling argument proves, for unique recovery,

\[
\alpha(\Pi)=\min\left(\{1\}\cup\{\lambda_P:Geo_P(\Pi)\}\right).
\]

Thus exact exponent `a<1` is equivalent to *at least one* predicate with `lambda_P=a` being true and *every* predicate with `lambda_P<a` being false. Exact exponent 1 is equivalent to all predicates with `lambda_P<1` being false.

**Algebraic canonical-depth predicate.** Introduce orthogonal projectors `P_0,...,P_d` onto face-support spaces, with `P_0=I`, `P_d=P_U`, `P_j P_{j-1}=P_j` and strictly decreasing ranks. At step `j`, introduce symmetric `Z_j` with `Pi Z_j=0`, `<Z_j,X*>=0`, and `S_j=P_{j-1}Z_jP_{j-1} PSD`. Require

\[
S_jP_j=0,\qquad
S_j+P_j+(I-P_{j-1})\succ0.
\]

This ensures `P_j` is *exactly* the kernel projector of the compressed stress in the current face. Require moreover that **every** symmetric `Z` with `Pi Z=0`, `<Z,X*>=0` and `P_{j-1}ZP_{j-1} PSD` satisfies

\[
\operatorname{tr}(P_j P_{j-1}ZP_{j-1})=0.
\]

This makes the chosen stress maximal-support and the chain canonical, so its length is the minimal degree. All are first-order real polynomial equalities and inequalities, with PSD expressible by principal minors.

Finally require the Gram determinant of `(I-Pi)|_{S(U)}` to be positive (the linear measurement is injective on the final support face). Combined with the exposing chain, this **proves uniqueness**. Conversely uniqueness guarantees a chain and support injectivity.

For a candidate `a in A_nu`, let `Psi(n,r,d,a)` be the explicit first-order real-closed-field sentence saying that there exists such a kernel projector `Pi` simultaneously satisfying this canonical depth certificate, support injectivity, and the finite exact-exponent pattern formula. Then

\[
\boxed{\quad
\Sigma_{n,r,d}=\{a\in A_{n-r}: \Psi(n,r,d,a)\text{ is true}\}.\quad}
\]

This is a **complete universally terminating exact decision algorithm for every triple**: enumerate finite patterns, solve rational LPs, build polynomial formulas, and use a real-closed-field decision algorithm to decide each `Psi`. A true instance yields algebraic sample data for a measurement map; a false one proves nonrealizability. It is independent of the unproved dense-to-sparse depth-preservation implication.

**Scope restriction:** this is an *algorithmic structural classification*, not an elementary arithmetic formula or a practical polynomial-time algorithm. Unrestricted real quantifier elimination is standard, not claimed novel. The PSD-specific contribution is reducing the search to at most `nu` weighted kernel coefficients and `nu` canonical maximal-exposure stages, with finitely many rational LP values—no arbitrary competitor curves or unbounded valuations remain in the decision sentences.

## 4. Proof audit and unresolved explicit formula

1. **Ambient PSD:** all sparse upper bounds start from an arbitrary PSD matrix `X`, not a restricted curve or pencil. The projection error `X-P_V X` is controlled.
2. **Full minors:** the constructive sharp curves use diagonal dominance after congruence, not merely positive `2x2` minors.
3. **Exact minimal degree:** greedy peeling is compared against every alternative chain, including rotated intermediate faces.
4. **No silent dense-to-sparse depth equivalence:** the universal all-degree decision theorem works directly with a single kernel `K` and its genuine dual stresses.
5. **Known ingredients:** semialgebraic selection, the ordinary Lojasiewicz/semialgebraic rational exponent, facial reduction, and real quantifier elimination are standard and are not presented as inventions.
6. **Remaining finer classification:** an explicit combinatorial list at each fixed triple `(n,r,d)` is not obtained, nor is a theorem asserting all dense instances admit a dimension- and depth-preserving midpoint network. The endpoint `alpha=1/2,d>=3` is unresolved *as a uniform dimension-independent statement*, although the finite decision theorem covers each fixed dimension.

**GitHub preservation:** see branch `research/psd-joint-depth-universal-20261107` in repository `Harman6139/Posterity-Files`, checkpoints 01 (dense greedy depth), 02 (all rational interior realizations), and 03 (all-degree finite decision theorem).