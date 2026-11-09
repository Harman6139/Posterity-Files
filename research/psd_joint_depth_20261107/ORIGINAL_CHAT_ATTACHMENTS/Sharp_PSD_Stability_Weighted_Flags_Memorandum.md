# Sharp PSD stability: weighted flags and constrained midpoint networks

**Research memorandum — 7 November 2026**

## Scope and status

This memorandum establishes a finite geometric classifier for an individual dense PSD inverse problem, a complete combinatorial characterization of the exponent spectrum at fixed matrix size and target rank, an exact minimum-dimension formula through constrained midpoint networks, a generic classification conditioned on uniqueness, and an exponent- and depth-preserving reduction for bounded nonsingleton spectrahedra.

It also gives a complete closed-form spectrum when the singularity degree is one or two. The joint classification at an arbitrary prescribed triple `(matrix size, target rank, singularity degree)` is not completed for degree at least three. The fixed-size/rank spectrum and the individual-instance classifier do not have that restriction.

The foundational semialgebraic results, facial reduction, and ordinary mediated-set theory are established tools. The claims below concern the additional reduction from arbitrary dense PSD recovery to bounded weighted flags and constrained midpoint networks. Priority for those claims has not been established by the literature check; the proofs, rather than a priority claim, are the basis for this memorandum.

---

## 1. Setting and elementary reductions

Let `L:S^n -> R^m` be linear, let `X_* >= 0`, and assume

\[
\{X\succeq0:LX=LX_*\}=\{X_*\}.
\]

Write `K=ker L`, `r=rank X_*`, `nu=n-r`, and

\[
\omega(\delta)=\sup\{\|X-X_*\|_F:X\succeq0,\ \|L(X-X_*)\|\le\delta\}.
\]

All exponents concern the full ambient PSD cone and the full matrix Frobenius distance. They are not exponents of a projected coordinate or of a restricted-rank competitor class.

### 1.1 Positive-definite trace control follows from uniqueness

Uniqueness implies `K cap S_+^n={0}`. Otherwise `X_*+tR` would be a distinct solution for a nonzero PSD `R in K`. The compact convex set

\[
C=L\{R\succeq0:\operatorname{tr}R=1\}
\]

does not contain zero. If `z` is its nearest point to zero, then `<z,c> >= ||z||^2` for every `c in C`. Consequently

\[
W=L^*z\succeq\|z\|^2I\succ0.
\]

It follows that residual sublevel sets are bounded. A congruence by `W^{1/2}` makes the identity a measured matrix and preserves the exponent. We use boundedness below without repeatedly invoking this normalization.

### 1.2 Standard semialgebraic input

Compactness and uniqueness imply `omega(delta)->0`. The graph of the maximum defining `omega` is semialgebraic. One-variable semialgebraic growth and selection, followed by Puiseux reparameterization, give

\[
\omega(\delta)\asymp\delta^\alpha
\]

for an attained positive rational exponent `alpha`, and a PSD extremal arc with the corresponding orders. More specifically, when `alpha<1`, there are integers `P<Q` and a convergent power-series arc with

\[
X(t)\succeq0,\quad X(0)=X_*,\quad
\|X(t)-X_*\|\asymp t^P,\quad
\|L(X(t)-X_*)\|=O(t^Q),\quad \alpha=P/Q.
\]

These are standard facts of real algebraic geometry, not new results asserted here. The subsequent arguments replace the unbounded arc information by bounded PSD-specific data.

The perturbations `X_*+tI` show `alpha<=1`. If `r=0`, positive-definite trace control gives `alpha=1`. If `r=n`, uniqueness makes `L` injective, also giving `alpha=1`. Henceforth assume `0<r<n` unless otherwise stated.

### 1.3 Only the kernel and target support affect the exponent

Equivalent norms on the quotient by `K` give equivalent residuals. Thus the exponent depends on `L` only through `K`.

Suppose `X_1,X_2` are positive definite on the same support `U_0` and zero on its orthogonal complement. Choose `lambda>0` so that `X_2-lambda X_1 >=0`. For every `X>=0`,

\[
X_2+\lambda(X-X_1)=\lambda X+(X_2-\lambda X_1)\succeq0.
\]

This transfers competitors and their residuals from target `X_1` to target `X_2`. Reversing the targets proves equivalent moduli up to fixed changes of scale. It also proves that uniqueness is invariant under this change of target. In particular, positive eigenvalues of the target affect constants, not the exponent.

---

## 2. The PSD coefficient-rescaling lemma

This is the main mechanism that removes dependence on determinant cancellations.

### Lemma 2.1

Let

\[
\mathbb R^n=U_0\oplus\cdots\oplus U_k,
\qquad 0=w_0<w_1<\cdots<w_k,
\]

be an orthogonal decomposition. Consider a finite generalized polynomial

\[
Y(t)=A_0+\sum_{e>0}t^eA_e.
\]

Assume:

* `A_0` is positive definite on `U_0` and zero on the other blocks;
* the `U_i,U_j` block of `A_e` is zero whenever `2e<w_i+w_j`;
* on each diagonal block `U_i`, the coefficient at exponent `w_i` is positive definite.

Then, for all sufficiently large fixed `sigma`,

\[
Y_\sigma(t)=A_0+\sum_{e>0}e^{\sigma e^2}t^eA_e
\]

is positive definite for all sufficiently small positive `t`.

### Proof

Let `D_sigma(t)` be scalar on `U_i`, with scalar

\[
e^{\sigma w_i^2/2}t^{w_i/2}.
\]

The normalized matrix `D_sigma(t)^{-1}Y_sigma(t)D_sigma(t)^{-1}` has a finite limit as `t->0`. Its diagonal blocks are the prescribed positive-definite leading blocks. An off-diagonal block can survive only at exponent `e=(w_i+w_j)/2`, in which case its multiplier is

\[
\exp\!\left(\sigma\left[\frac{(w_i+w_j)^2}{4}
-\frac{w_i^2+w_j^2}{2}\right]\right)
=\exp\!\left(-\frac{\sigma(w_i-w_j)^2}{4}\right).
\]

All off-diagonal blocks therefore tend to zero as `sigma->infinity`. The limiting normalized matrix is positive definite for sufficiently large `sigma`, and remains so for sufficiently small `t`. This proves the assertion. `QED`

The lemma preserves every homogeneous linear condition on each coefficient. In particular, multiplying a coefficient in `K` by a positive scalar leaves it in `K`. Arbitrarily large fixed rescaling constants are harmless: the small-`t` limit is taken after `sigma` is fixed.

---

## 3. A finite geometric classifier for a dense instance

Set `U_0=range X_*`. A block pattern is a set of unordered block pairs `(j,l)`, with diagonal pairs allowed. A matrix is supported in a pattern if its other blocks are zero.

Choose `1<=k<=nu` and positive block dimensions summing to `nu`, and seek an orthogonal flag

\[
\mathbb R^n=U_0\oplus U_1\oplus\cdots\oplus U_k.
\]

There are two modes.

**Diagonal-leading mode.** Here `k>=2`. Choose matrices `H_i in K`, `1<=i<k`, each with a positive-definite `U_i,U_i` block, and choose a support pattern `P_i` for each. Introduce weights

\[
0<w_1<\cdots<w_{k-1}<w_k=1,
\qquad p=w_1.
\]

For every `(j,l) in P_i`, impose

\[
2w_i\ge w_j+w_l. \tag{3.1}
\]

**Off-diagonal-leading mode.** Choose the same `H_i` for `1<=i<k`, together with a nonzero `H_p in K` and its pattern `P_p`. Introduce

\[
0<p<w_1<\cdots<w_k=1.
\]

Impose (3.1), and for `(j,l) in P_p` impose

\[
2p\ge w_j+w_l. \tag{3.2}
\]

The case `k=1` has no `H_i`.

A pattern choice is **geometrically feasible** when its flag and matrices exist and its strict weight region is nonempty. For such a choice, let `lambda_P` be the infimum of `p` over its strict weight region. It is obtained by minimizing over the closed rational polytope: mix any closed feasible point with a strictly feasible point to justify this equality.

### Theorem 3.1 — finite weighted-flag classifier

\[
\boxed{\alpha(K,U_0)=
\min\bigl(\{1\}\cup\{\lambda_P:P\text{ geometrically feasible}\}\bigr).}
\tag{3.3}
\]

There are finitely many pattern choices. Every exponent optimization is a rational linear program with at most `nu` variables. The geometric part consists only of an orthogonal flag, kernel membership, block-zero conditions, positive-definite diagonal compressions, and one possible nonzero matrix.

For algebraic data the geometric tests are finite real algebraic feasibility problems. For a fixed flag they reduce to linear algebra and semidefinite feasibility. No polynomial-time complexity assertion is made.

### Proof: every feasible pattern gives a sharpness obstruction

For strict feasible weights form

\[
Y(t)=X_*+\sum_{i<k}t^{w_i}H_i+tP_{U_k}, \tag{3.4}
\]

adding `t^p H_p` in the off-diagonal-leading mode. Lemma 2.1 applies. After coefficient rescaling the matrix is positive definite for small `t`, its displacement has order `t^p`, and its residual has order exactly `t`.

Indeed, every coefficient below order one belongs to `K`, while `L(P_{U_k})` is nonzero because `K` contains no nonzero PSD matrix. Therefore `alpha<=p`, and hence `alpha<=lambda_P`.

### Proof: extracting a bounded flag from a sharp arc

Take the standard sharp arc of Section 1.2 and add `ct^Q I`, with fixed `c>0`. Its displacement order is still `P`; its residual is `O(t^Q)`; and every compression is bounded below by `ct^Q I`.

Compress the arc to `ker X_*`. Its first nonzero coefficient is PSD. Let its range be `U_1`, with order `W_1`. Compress further to the kernel of that coefficient and repeat. This gives a fixed orthogonal decomposition, not a moving eigenbasis, with

\[
P\le W_1<\cdots<W_k\le Q.
\]

The leading coefficient on each `U_i` is positive definite. Positivity and the inequality

\[
|u^TX(t)v|^2\le(u^TX(t)u)(v^TX(t)v)
\]

show that the `U_i,U_j` block has order at least `(W_i+W_j)/2`, with `W_0=0`.

Every coefficient of order below `Q` lies in `K`. Necessarily `W_k=Q`. Otherwise retain just the coefficients at `W_1,...,W_k` and, if different, at `P`. Lemma 2.1 would turn them into a nonconstant exact PSD solution curve, contradicting uniqueness.

Normalize by `Q`: set `w_i=W_i/Q`, `p=P/Q=alpha`. The relevant coefficients give one of the finite patterns above. Its minimum is at most `alpha`. Combining with the first half proves (3.3). `QED`

### Consequences

The upper recovery bound in (3.3) holds for all PSD competitors. If it failed, the actual semialgebraic modulus would have a smaller exponent, and the extraction argument would produce a pattern contradicting (3.3).

A sharp witness uses at most `nu` kernel coefficient matrices and one PSD terminal coefficient. There is no need for an unbounded-order list of Taylor coefficients. The finite flag tests, rather than unrestricted elimination of the original recovery optimization, are the proposed intrinsic classifier.

---

## 4. From dense flags to finite midpoint networks

A finite set `S subset (0,1)` is **mediated** when every `s in S` is the midpoint of two distinct points of `S union {0,1}`. Its parents necessarily lie on opposite sides of `s`.

### Lemma 4.1 — the least-weight principle

For a fixed feasible pattern in Section 3, its closed weight polytope has a componentwise least point.

### Proof

Each nontrivial inequality has the form “one variable is at least a nonnegative average of other variables,” or is an ordering inequality of the same monotone kind. The endpoints are fixed at zero and one. The componentwise minimum of two feasible vectors is feasible: use the vector attaining the smaller left coordinate, and observe that all right coordinates only decrease.

Compactness gives a coordinatewise minimizer for each coordinate; the componentwise minimum of these finitely many vectors is the required least point. `QED`

### Lemma 4.2 — mediated extraction

Suppose a feasible pattern has minimum `p=alpha<1`. At its componentwise least point, let `S` be the distinct diagonal weights strictly between zero and one. Then

\[
|S|\le\nu-1,\qquad S\subseteq[\alpha,1),
\qquad 2\alpha\in S\cup\{1\}, \tag{4.1}
\]

and `S` is mediated. The empty set is permitted only for `alpha=1/2`.

### Proof

The least leading weight cannot be zero, because mixing with a strictly feasible point and applying Lemma 2.1 would give obstructions with arbitrarily small positive exponent, contradicting Section 1.2.

Consider all coordinates at an intermediate common value `a`. If every active inequality with its left coordinate in this group also had all its right coordinates in the group, reducing the whole group slightly would preserve all active inequalities, all inactive inequalities, and the ordering constraints. That contradicts componentwise minimality. Therefore some active averaging inequality crosses levels. Its parents have values below and above `a`, and their average is `a`.

For a diagonal level this is precisely a midpoint representation. In off-diagonal-leading mode, the original strict inequality `p<w_1` forces the support of `H_p` to have only top-block entries and top-to-null entries. It has at least one top-to-null entry, since a nonzero kernel matrix supported on `U_0` would contradict uniqueness. Hence its nontrivial weight constraints are `2p>=w_j`. If the least leading weight stays strictly below the least diagonal weight, minimality makes one such inequality tight. If it merges with the least diagonal level, the preceding group argument applies to the combined group.

Thus either `alpha` is the smallest member of `S`, or `2alpha` is a diagonal weight. In the first case, the midpoint parents of the smallest positive level must be zero and `2alpha`, proving (4.1) as well. At most `k-1<=nu-1` distinct diagonal weights lie strictly below one. `QED`

This is the universal necessity statement: midpoint networks are not merely examples. Every dense PSD recovery exponent has such a network with no more internal vertices than its target nullity minus one.

---

## 5. Exact spectrum and exact minimum dimension

For rational `0<alpha<=1/2`, define the constrained mediated number

\[
h(\alpha)=\min\left\{|S|:
\begin{array}{l}
S\subseteq[\alpha,1)\text{ is finite and mediated},\\
2\alpha\in S\cup\{1\}
\end{array}\right\}. \tag{5.1}
\]

Set `h(1/2)=0`, using the empty set.

### Theorem 5.1 — spectrum and optimal dimension

For every `r>=1` and `nu>=1`, the complete exponent spectrum with matrix size `n=r+nu` and target rank `r` is

\[
\boxed{\Sigma_\nu=\{1\}\cup
\{\alpha\in\mathbb Q\cap(0,1/2]:h(\alpha)\le\nu-1\}.} \tag{5.2}
\]

Equivalently, the exact minimum matrix size for target rank `r` and non-Lipschitz exponent `alpha` is

\[
\boxed{n_{\min}(r,\alpha)=r+1+h(\alpha).} \tag{5.3}
\]

This is an exact finite combinatorial formula, not a claim that `h` has an elementary expression in the numerator and denominator.

### Necessity

Apply Theorem 3.1 to a sharp pattern and Lemma 4.2. This gives `h(alpha)<=nu-1`. It also proves the universal forbidden interval `(1/2,1)`.

### Sufficiency: a sparse full-matrix PSD realization

Let `S={w_1<...<w_h}` meet (5.1), and include boundary weights `w_0=0`, `w_{h+1}=1`. Choose parents `a(i)<i<b(i)` with

\[
2w_i=w_{a(i)}+w_{b(i)}.
\]

Use one matrix row for each of these `h+2` vertices. Its diagonal variables are `x_0,...,x_{h+1}`. Set the off-diagonal entry on the parent edge `{a(i),b(i)}` equal to `lambda x_i`, where `lambda=1/(2(h+2))`. All other off-diagonal entries are zero, except for the following possible extra variable.

If `alpha` is not in `S`, add an off-diagonal variable `lambda z` on the edge joining vertex zero to the vertex of weight `2alpha`. This edge is unused: another variable on it would have weight `alpha`, contrary to the assumption. If `alpha in S`, it is the smallest internal weight and its existing parent edge is already `{0,2alpha}`; no extra variable is needed.

Let `V` be the resulting linear pencil range. Measure

\[
X\longmapsto\bigl(P_{V^\perp}X,\operatorname{tr}X,X_{h+1,h+1}\bigr),
\]

and take `X_*=E_{00}`.

#### Upper bound against arbitrary PSD matrices

Let the residual be at most `delta`, set `Y=P_VX`, and write its pencil coordinates as above. Then `||X-Y||_F<=delta`, `Y+delta I>=0`, the trace is bounded, and `|x_{h+1}|<=delta`. All coordinates are bounded.

Put `U_j=|x_j|+delta`. The parent-edge principal minors give, with a fixed constant `c_lambda`,

\[
U_i^2\le c_\lambda U_{a(i)}U_{b(i)}. \tag{5.4}
\]

Let `Q` be the matrix assigning probability one half to each internal parent. Every vertex reaches a boundary by repeatedly taking its smaller or larger parent, so `rho(Q)<1` and `(I-Q)^{-1}>=0`. Taking logarithms in (5.4) and applying this inverse gives

\[
|x_i|\le C_i\delta^{w_i}.
\]

The optional edge similarly gives `|z|<=C delta^alpha`. The trace equation controls `x_0-1`, and the projection error controls all off-pattern entries. Therefore

\[
\|X-X_*\|_F\le C\delta^\alpha.
\]

No rank or exact-structure assumption was imposed on `X`. Sending `delta` to zero also proves uniqueness.

#### Matching positive-definite curves

Set `x_j=t^{w_j}` and, when present, `z=t^alpha`. After congruence by `diag(t^{-w_j/2})`, the pencil is a matrix with diagonal one and off-diagonal entries either zero or `lambda`. Its off-diagonal absolute row sums are less than one half, so it is positive definite. Normalize its trace.

The terminal residual is comparable to `t`, and a diagonal or off-diagonal coordinate has magnitude comparable to `t^alpha`. This proves sharpness. Adjoin a fixed positive-definite block of size `r-1` and measure that block and every new cross entry to obtain target rank `r`. Fully observed zero rows pad the nullity without changing the exponent. `QED`

The same padding preserves any positive singularity degree. Original exposing stresses lift, and the extra zero rows can be exposed in the first step. Conversely, restrict a reduction of the padded problem to the original coordinate space. For a PSD compressed stress, a vector in that space has zero quadratic form exactly when it belongs to the stress kernel; therefore the intersections of successive faces give valid original exposing steps, with zero steps omitted. Padding cannot reduce the original degree. Adjoining a fully fixed positive-definite block likewise preserves degree, since every exposing stress annihilates its support.

### 5.1 A finite exact algorithm

For a prospective size `h`, number the internal vertices increasingly. Each chooses one lower and one upper parent. There are exactly

\[
\prod_{i=1}^h i(h+1-i)=(h!)^2
\]

parent assignments. Solve the rational harmonic system for each assignment; retain only strictly increasing solutions between zero and one. Test whether `2alpha` is a vertex and whether all internal weights are at least `alpha`.

This enumerates all sets in (5.1). For a fixed nullity it produces the entire spectrum with exact rational arithmetic. The supplied reference implementation performs this enumeration and returns explicit sparse-pencil witnesses.

---

## 6. Denominator bounds and explicit minimum dimensions

### 6.1 Universal parity-sensitive denominator bound

For a mediated set of size `h`, the harmonic system is `Mv=b`, where each row of `M` has the form `2e_i-e_j-e_l`, with boundary columns removed. It is nonsingular because the associated absorbing chain is transient.

Each row is a sum of two reduced directed-incidence rows. Multilinearity expands `det M` into `2^h` determinants, each in `{0,1,-1}`. To see the latter claim directly, a square incidence matrix with a cycle has dependent rows; otherwise eliminate a leaf repeatedly. Thus

\[
0<|\det M|\le2^h.
\]

Every harmonic weight has denominator dividing this integer. If `alpha=a/b` in lowest terms, then `2alpha` is such a weight or the endpoint one. Consequently

\[
\boxed{\frac b{\gcd(b,2)}\le2^{\nu-1}.} \tag{6.1}
\]

This controls denominators by target nullity, independently of target rank.

### 6.2 A logarithmic finite search bound

Ordinary one-dimensional mediated-set theory gives a set of size `ceil(log_2 N)` containing any reduced rational `a/N` in `(0,1)`; this is Wang's minimum-mediated-set theorem [W]. A short verification is included below.

For `alpha=a/b<1/2`, choose such a set `T` containing `a/(b-a)`, and put

\[
S=\{\alpha\}\cup\{\alpha+(1-\alpha)t:t\in T\}.
\]

It contains `2alpha`, all its elements are at least `alpha`, and it is mediated: the transformed relations use endpoints `alpha,1`, while `alpha` is the midpoint of `0,2alpha`. Therefore

\[
\left\lceil\log_2\frac b{\gcd(b,2)}\right\rceil
\le h(\alpha)
\le1+\lceil\log_2(b-a)\rceil. \tag{6.2}
\]

The exact finite search has logarithmically many vertices. The displayed bounds differ by at most one for odd `b`, and by at most two for even `b`.

For completeness, the ordinary mediated-set construction can be verified with three integer multiplicities. Let `k=ceil(log_2 N)`, initialize counts `(a,N-a,2^k-N)` and labels `(N,0,a)`. Choose the two odd counts `s_i<=s_j`, replace label `t_i` by `(t_i+t_j)/2`, and replace counts `s_j,s_l` by `(s_j-s_i)/2,s_l/2`, retaining `s_i`. Total multiplicity and weighted label sum halve at every step. An odd count persists, so the next step exists. After `k` steps the sole remaining label is `a`. Distinct generated interior labels form a mediated set; for each label use its first nontrivial generation, including the generated occurrence of `a`. There are at most `k` labels. The determinant bound gives the matching lower bound. This is the established construction in [W], used here with the additional barrier transformation above.

### 6.3 Every reciprocal exponent has an elementary optimal formula

For `b>=2` and `r>=1`,

\[
\boxed{
n_{\min}(r,1/b)=
\begin{cases}
r+\lceil\log_2 b\rceil,&b\text{ even},\\
r+1+\lceil\log_2 b\rceil,&b\text{ odd}.
\end{cases}}
\tag{6.3}
\]

The lower bounds are (6.1). For an integer `s>=2`, let `a_0=s` and `a_j=ceil(s/2^j)` until `a_k=1`, where `k=ceil(log_2 s)`. The set `{a_j/s:1<=j<=k}` is mediated, because `a_j=(a_{j-1}+epsilon_j)/2` with `epsilon_j` equal to zero or one, and one is the final numerator in the set. Its minimum is `1/s`.

For odd `b`, take `s=b`. For even `b=2s`, take this set for `s`, whose minimum is `2/b`, and use the optional leading edge of weight `1/b`. The case `b=2` uses the empty set. These constructions attain (6.3).

### 6.4 The numerator genuinely matters: exponent `2/7`

The exact minimum nullity for `2/7` is five, hence

\[
n_{\min}(r,2/7)=r+5.
\]

The denominator bound alone only gives nullity at least four. If a three-point mediated set met the barrier condition, its determinant would be seven: it is divisible by seven and at most eight. Its points would therefore be multiples of `1/7`. They must lie in `{2,3,4,5,6}/7` and contain `4/7`.

The six possible triples are

\[
(2,3,4),(2,4,5),(2,4,6),(3,4,5),(3,4,6),(4,5,6).
\]

None is mediated relative to endpoints `0,7`: respectively, the entries `4,4,6,3,4,4` have no two distinct available parents. Four points suffice:

\[
S=\{2,4,5,6\}/7,
\]

with relations `2=(0+4)/2`, `4=(2+6)/2`, `5=(4+6)/2`, and `6=(5+7)/2`.

### 6.5 Complete small-nullity spectra

\[
\Sigma_0=\{1\},\quad
\Sigma_1=\{1,1/2\},\quad
\Sigma_2=\{1,1/2,1/4\},
\]

\[
\Sigma_3=\{1,1/2,3/8,1/3,1/4,1/6,1/8\}.
\]

At nullity four the complete spectrum is

\[
\begin{split}
\Sigma_4=\{&1,1/2,7/16,3/7,5/12,2/5,3/8,5/14,1/3,5/16,3/10,\\
&1/4,3/14,1/5,3/16,1/6,1/7,1/8,1/10,1/12,1/14,1/16\}.
\end{split}
\]

The parity bound leaves only these candidates and `2/7`; the preceding argument excludes `2/7`. The following mediated sets realize all remaining nontrivial values. The leading exponent is half an indicated member, or the minimum of the set.

| Exponent | Internal mediated set |
|---|---|
| 1/16 | {1/8,1/4,1/2} |
| 1/14, 1/7 | {1/7,2/7,4/7} |
| 1/12 | {1/6,1/3,1/2} |
| 1/10, 1/5 | {1/5,2/5,3/5} |
| 1/8 | {1/4,1/2} |
| 1/6, 1/3 | {1/3,2/3} |
| 3/16 | {1/4,3/8,1/2} |
| 3/14, 5/14, 3/7 | {3/7,5/7,6/7} |
| 1/4 | {1/2} |
| 3/10, 2/5 | {2/5,3/5,4/5} |
| 5/16 | {1/2,5/8,3/4} |
| 3/8 | {1/2,3/4} |
| 5/12 | {1/2,2/3,5/6} |
| 7/16 | {1/2,3/4,7/8} |
| 1/2 | empty set |

The exact enumerator additionally gives 78 exponents through nullity five and 306 through nullity six, with a rational parent-network witness for every value in the supplied JSON catalogue.

---

## 7. What can be classified at prescribed facial-reduction depth?

Use the ordinary singularity degree: the minimum number of exposing steps needed to reach the minimal PSD face containing the solution.

### 7.1 A diagonal refinement of the depth bound

If the degree is `d>=1`, then every bounded PSD competitor satisfies

\[
\operatorname{tr}(P_{\ker X_*}X)=O(\delta^{2^{-(d-1)}}). \tag{7.1}
\]

Here is a direct proof. The first exposing stress controls the trace on its positive eigenspace by `O(delta)`. At step `j`, all previously removed blocks have total trace `O(delta^{2^{-(j-2)}})`. PSD Cauchy--Schwarz bounds their cross entries with the still-bounded remaining matrix by `O(delta^{2^{-(j-1)}})`. Pairing the `j`th stress with the residual then bounds the trace on its newly exposed block by the same order. Summing over the chain gives (7.1).

Thus, in Lemma 4.2, the mediated set can be required to satisfy the stronger barrier

\[
S\subseteq[\max\{\alpha,2^{-(d-1)}\},1). \tag{7.2}
\]

To justify the passage to the least LP point, every strict feasible weighting gives an actual PSD arc whose null-space trace has order `w_1`. Equation (7.1) forces `w_1>=2^{-(d-1)}` for all these weightings, and hence for their least limit.

This is a finite combinatorial obstruction stronger than the scalar inequality `alpha>=2^{-d}`. It does not, by itself, characterize all depth constraints for `d>=3`.

### 7.2 Degree one

A full stress on the target null space gives `O(delta)` control of the null diagonal block and `O(sqrt(delta))` control of its cross block. Uniqueness controls the support block. Hence the exponent is either `1` or `1/2`.

Conversely, Lipschitz recovery forces degree one when the target is singular. Indeed, put

\[
T=\left\{\begin{pmatrix}A&B\\B^T&C\end{pmatrix}:C\succeq0\right\}.
\]

Lipschitz recovery is equivalent to `K cap T={0}`. If this holds, the bottom-block projection is injective on `K`, and its image contains no nonzero PSD matrix. Strict separation yields a positive-definite bottom-block matrix orthogonal to that image, hence a full null-space stress in `K^perp`.

For necessity of the tangent criterion, every tangent direction `H` has a PSD realization `X_*+tH+O(t^2)` by the Schur complement. A nonzero `H in K cap T` therefore precludes Lipschitz recovery. Sufficiency follows because every PSD difference lies in `T` and the unit tangent slice is compact.

### Theorem 7.1 — complete degree-two spectrum

For `r>=1` and `nu>=2`, the exact spectrum at singularity degree two is

\[
\boxed{
\Sigma_{\nu,2}=
\left\{\frac ab\in\mathbb Q\cap[1/4,1/2]:
\gcd(a,b)=1,\quad \frac b{\gcd(b,4)}\le2^{\nu-2}\right\}.}
\tag{7.3}
\]

Equivalently, the exact minimum dimension at degree two is

\[
\boxed{n_{\min,d=2}(r,a/b)
=r+2+\left\lceil\log_2\frac b{\gcd(b,4)}\right\rceil}
\tag{7.4}
\]

for `1/4<=a/b<=1/2`; there are no other exponents at degree two.

### Proof: necessity

Lipschitz recovery has degree one, so only non-Lipschitz exponents need consideration. Equation (7.2) says that all internal mediated weights are at least `1/2`. A nonempty mediated set with this property has minimum exactly `1/2`: its minimum is the midpoint of zero and some weight at most one.

Every weight above `1/2` has both parents at least `1/2`; a zero parent would give a midpoint at most `1/2`. Therefore, removing `1/2` and applying the affine map `s -> 2s-1` gives an ordinary mediated set in `(0,1)` containing `4alpha-1` when `1/4<alpha<1/2`.

For `alpha=a/b` reduced, the denominator of `4alpha-1` is `b/gcd(b,4)`. The determinant bound requires at least its ceiling base-two logarithm internal vertices. Restoring the vertex `1/2` and the terminal null direction gives (7.4). The endpoints use the empty transformed set and require nullity two, as they must at degree two. The case `alpha<1/4` is excluded by (7.2).

### Proof: sufficiency and exact degree

Take a minimum ordinary mediated set for `4alpha-1`, transform it by `u -> (1+u)/2`, and add `1/2`. For the endpoints use just `{1/2}`. Apply the sparse realization of Theorem 5.1.

The first exposing stress has zero source row. Orthogonality to each internal-variable coefficient reads

\[
Z_{ii}+2\lambda Z_{a(i),b(i)}=0.
\]

Induction through the increasing internal weights forces each internal stress row to zero: its smaller parent has already been forced to zero. Thus every first stress is supported only on the terminal vertex, so degree one is impossible.

After exposing the terminal, a positive-definite stress on all internal vertices exists. For an internal weight `s`, set `c(s)=(s-1/2)(1-s)` and choose diagonal stress entries `epsilon^{c(s)}`. For each parent edge wholly within the remaining internal vertices, choose its stress entry to satisfy the displayed orthogonality equation. The normalized absolute entry is

\[
(2\lambda)^{-1}\epsilon^{c(s)-(c(a)+c(b))/2}
=(2\lambda)^{-1}\epsilon^{(a-b)^2/4}\longrightarrow0.
\]

Thus the compressed stress is positive definite for sufficiently small `epsilon`. Edges meeting the removed terminal are unrestricted off-face entries and can be chosen to satisfy the remaining equations. The source row of the compressed stress is zero. This completes a two-step reduction. `QED`

### Examples and limitation

The exponent `1/3` has minimum nullity three, and every such minimum-dimensional realization has degree three; degree two needs nullity four. The exponent `2/7` has minimum nullity five and already admits a degree-two realization, using

\[
S=\{1/2,4/7,9/14,11/14\}.
\]

In particular, depth two admits every rational exponent in `[1/4,1/2]` when dimension is unrestricted, with arbitrarily large denominators.

For `d>=3`, (7.2) is necessary, but a proof that a suitable constrained midpoint network can always preserve the prescribed depth has not been obtained. The fixed-`(n,r)` catalogue is complete; its subdivision by every possible degree is not claimed complete.

---

## 8. Generic strata conditioned on uniqueness

Fix a target `X_*` of rank `0<r<n`. Let `m` be the effective measurement rank, and let `U_m` be the set of full-row-rank maps with a singleton PSD fiber at this target. Set

\[
a=\frac{r(r+1)}2,\qquad
\ell=a+r\nu,
\]

and define

\[
T_0=\left\{\begin{pmatrix}A&B\\B^T&0\end{pmatrix}\right\},
\qquad \dim T_0=\ell.
\]

### Theorem 8.1 — conditional generic classification

The uniqueness locus is nonempty exactly when `a+1<=m<=n(n+1)/2`. On a relatively open dense subset of this locus, the problem has a full null-space exposing stress and

\[
\operatorname{rank}(L|_{T_0})=\min\{\ell,m-1\}.
\]

On that subset,

\[
\boxed{
\alpha_{\rm gen}=
\begin{cases}
1/2,&a+1\le m\le\ell,\\
1,&\ell+1\le m\le n(n+1)/2.
\end{cases}}
\tag{8.1}
\]

The same relative-density statement holds while retaining an identity measurement. This is genericity within the uniqueness locus, not a probability assertion for unconditioned random measurements.

### Proof

Uniqueness makes the restriction to matrices supported on `U_0` injective, requiring rank at least `a`. Separation of the affine fiber from the positive-definite cone supplies a nonzero exposing stress. Its multiplier annihilates that support restriction, so `m>=a+1`.

Conversely, measuring all support-block entries and the null-space trace gives uniqueness with `a+1` measurements. Add independent measurements for larger `m`.

For density, choose any nonzero exposing stress as the first measurement row and replace it by that stress plus `epsilon P_{ker X_*}`. The first row now fully exposes the null space. The support restriction has not changed, so uniqueness persists. Perturb the remaining rows to make their restriction to `T_0` have maximal possible rank, while retaining injectivity on the support block. This proves density.

For relative openness, every uniquely solvable map has a nonzero exposing multiplier, so the restriction rank is always at most `min(ell,m-1)`. At maximal rank its adjoint kernel varies continuously within the uniqueness locus. Project a full-stress multiplier onto the nearby adjoint kernel; its bottom compression remains positive definite. Thus both conditions persist.

A full stress forces every tangent kernel direction to have zero bottom block, so `K cap T=K cap T_0`. The latter has dimension `ell-min(ell,m-1)`. The tangent criterion in Section 7 and the square-root upper bound prove (8.1). `QED`

### 8.1 Exact constants on the regular strata

Define

\[
\gamma=\min_{H\in T,\ \|H\|_F=1}\|LH\|.
\]

On the Lipschitz stratum,

\[
\lim_{\delta\downarrow0}\frac{\omega(\delta)}\delta=\frac1\gamma.
\tag{8.2}
\]

The upper bound holds globally for PSD differences. A quadratic PSD realization of a minimizing tangent direction gives the matching limit.

On the square-root stratum, write `X_*=diag(D,0)`, `D>0`, and let `pi` project in measurement space onto `(LT_0)^perp`. Then

\[
\lim_{\delta\downarrow0}\frac{\omega(\delta)}{\sqrt\delta}=c_* ,
\tag{8.3}
\]

where

\[
c_*=\max\left\{
\left\|\begin{pmatrix}A&B\\B^T&0\end{pmatrix}\right\|_F:
\begin{array}{l}
H=\begin{pmatrix}A&B\\B^T&0\end{pmatrix}\in K,\\
C\succeq B^TD^{-1}B,\\
\|\pi L(0\oplus C)\|\le1
\end{array}\right\}.
\tag{8.4}
\]

The maximum is finite: a full stress `L^*y=0 op S`, `S>=mu I`, bounds `tr C` by `||y||/mu`. This bounds `B`, while support injectivity bounds `A`.

For the upper limit, take near-extremal competitors, divide their support and cross perturbations by `sqrt(delta)` and their bottom block by `delta`, and pass to a subsequence. The Schur complement yields the constraint on `C`; projection by `pi` removes the support/cross contribution to the residual. Every limit therefore satisfies (8.4).

For the lower limit, choose a feasible pair `(H,C)` and `W_2 in T_0` cancelling the component of `L(0 op C)` in `LT_0`. For sufficiently large fixed `M`,

\[
X(t)=X_*+tH+t^2(W_2+0\oplus C)+Mt^3P_{\ker X_*}
\]

is PSD by its Schur complement. Its residual is `t^2 pi L(0 op C)+O(t^3)` and its distance is `t||H||+O(t^2)`. Set `t=(1-epsilon)sqrt(delta)` and then let `epsilon` decrease to zero. This proves (8.3).

Both constants are continuous within their respective regular strata. For `c_*`, upper semicontinuity follows from the uniform stress bound and compactness. For the lower direction, perturb a kernel vector within the constant-rank kernel, add a small positive multiple of the identity to `C`, and scale slightly to obtain strict residual slack. This gives feasible nearby pairs approaching every original pair.

### 8.2 An exact singular-perturbation crossover

For a non-Lipschitz problem with `omega_0(delta) asymp delta^alpha`, add weak full observation:

\[
L_\epsilon H=(L_0H,\epsilon H).
\]

Uniformly for `0<epsilon<=1` and small `delta`,

\[
\omega_\epsilon(\delta)\asymp
\min\{\delta^\alpha,\delta/\epsilon\}. \tag{8.5}
\]

The upper bound is immediate. For the lower bound choose an original extremizer at residual

\[
\eta=\min\{\delta/2,(\delta/(2C\epsilon))^{1/\alpha}\},
\]

where `omega_0(eta)<=C eta^alpha`. Its two residual components are at most `delta/2`, and its displacement has the required lower bound. The crossover scale is `delta asymp epsilon^{1/(1-alpha)}`. Its exact asymptotic Lipschitz constant is `1/epsilon`, since the tangent constant becomes `sqrt(gamma_0^2+epsilon^2)=epsilon`.

Finally, the finite flag description makes every fixed-exponent locus semialgebraic. It yields a finite exponent stratification at fixed dimensions, although a complete set of transition laws between all nongeneric strata is not asserted.

---

## 9. Bounded nonsingleton spectrahedra reduce without losing exponent or depth

Let

\[
F=\{X\succeq0:LX=b\}
\]

be nonempty and bounded, and choose `X_0 in relint F` of maximum rank. Set `W=range X_0` and

\[
N=\ker L\cap\mathbb S(W).
\]

Every feasible matrix is supported on `W`, since otherwise its average with `X_0` would have larger rank. Because `X_0` is positive definite on `W`,

\[
\operatorname{aff}F=X_0+N.
\]

Define the augmented map

\[
\widehat L H=(LH,P_NH).
\]

### Theorem 9.1 — gauge reduction

The target `X_0` is uniquely recoverable under `widehat L`. Let

\[
\Omega(\delta)=\sup\{\operatorname{dist}(X,F):X\succeq0,
\ \|LX-b\|\le\delta\}
\]

and let `widehat omega` be its singleton counterpart. There are fixed positive constants `C,lambda` such that, for all sufficiently small `delta`,

\[
\widehat\omega(\delta)\le\Omega(\delta)+\delta,
\qquad
\Omega(\delta)\le\frac C\lambda\widehat\omega(\lambda\delta).
\tag{9.1}
\]

Thus the two problems have exactly the same exponent, matrix size, maximum feasible rank, and singularity degree.

### Proof of modulus equivalence

Boundedness of `F` implies `ker L cap S_+^n={0}`, hence positive-definite trace control as in Section 1. Thus nearby residual sublevels are bounded.

Set `H=X-X_0` and `e=||P_{N^perp}H||=dist(X,aff F)`. Let `mu` be the least positive eigenvalue of `X_0`, and let `M` uniformly bound `||P_NH||` on these sublevels. With `Z=X_0+P_NH`, the compression `Z|_W` is bounded below by `-eI`. Therefore

\[
Z'=(1-\theta)Z+\theta X_0\in F,
\qquad \theta=\frac e{\mu+e},
\]

and

\[
e\le\operatorname{dist}(X,F)\le(1+M/\mu)e.
\tag{9.2}
\]

Choose fixed `lambda>0` small enough that `(1-lambda)mu-lambda M>=0`. Then

\[
Y=X_0+\lambda P_{N^\perp}H
=\lambda X+(1-\lambda)X_0-\lambda P_NH\succeq0.
\]

Its gauge residual is zero, its original residual is scaled by `lambda`, and `||Y-X_0||=lambda e`. This proves the second bound in (9.1). For an augmented competitor, `||P_NH||<=delta`, so `||H||<=e+delta<=dist(X,F)+delta`, proving the first.

An exact augmented competitor belongs to `F` and differs from `X_0` by an element of `N` with zero projection onto `N`; thus it equals `X_0`.

### Proof that singularity degree is unchanged

At any intermediate PSD face whose support contains `W`, an augmented exposing stress has the form

\[
Z=L^*y+T,\qquad T\in N.
\]

Its compression to that face is PSD and pairs to zero with `X_0`, so that compression annihilates `W`. Consequently `<Z,T>=0`. But `LT=0`, so

\[
\langle Z,T\rangle=\|T\|_F^2.
\]

Thus `T=0`. The augmented and original problems admit exactly the same exposing steps at every relevant face, hence the same chains and degree. `QED`

For `rank X_0=0`, boundedness forces `F={0}`, and the assertion reduces to the elementary Lipschitz case. The theorem concerns full-matrix distance to a spectrahedron, not distance in the projected coordinates of a spectrahedral shadow.

---

## 10. Adversarial audit and limits

**Coefficient feasibility.** Entrywise orders alone do not ensure PSD. Lemma 2.1 proves full positive definiteness after coefficient rescaling, while preserving the linear kernel conditions. Distinct weight groups and positive-definite leading diagonal compressions are essential.

**Closure of LP cells.** Coincident or zero weights at the minimizing boundary are not silently used as PSD arcs. They are approached by convex mixing with the original strictly feasible weighting. All constructed arcs use strict weights. The least-point argument uses these arcs to identify the exact infimum.

**Auxiliary coordinates.** The barrier `S subset [alpha,1)` controls the entire lifted matrix. Omitting it would confuse a projected-coordinate exponent with the full recovery exponent and gives incorrect minimum dimensions. Exponent `2/7` is an explicit test of this distinction.

**Ambient competitors.** The sparse realizations use `Y=P_VX` only as an auxiliary approximation. The bound `Y+delta I>=0` and logarithmic inequalities control arbitrary PSD competitors with arbitrary off-pattern perturbations and arbitrary rank.

**Target rank.** The universal necessity proof permits blocks of any dimension. It yields a scalar rank-one realization with no larger nullity; this is not an assumption that competitors or original targets have rank one.

**Genericity.** The open dense statement is relative to the uniqueness locus and uses the effective measurement rank. It does not assert that an arbitrary random measurement system is uniquely solvable below its usual sampling threshold.

**Nonsingleton reduction.** The added gauge measurements do not alter exposing stresses; this is proved explicitly rather than assumed from equality of minimal faces.

**What remains unproved.** The individual dense-map exponent is covered by Theorem 3.1. The fixed-size/rank spectrum and exact minimum size are covered by Theorem 5.1. The degree-one and degree-two subdivisions are complete. For every prescribed degree at least three, a complete compatibility classification between sharp midpoint networks and minimal facial-reduction chains is not supplied. Nor is a polynomial-time algorithm for the dense flag-feasibility tests or an elementary arithmetic formula for every constrained mediated number claimed.

---

## 11. Literature comparison

[S] J. F. Sturm, *Error Bounds for Linear Matrix Inequalities*, SIAM Journal on Optimization 10(4), 1228–1248 (2000), DOI 10.1137/S1052623498338606. This supplies the classical depth-based error bound.

[SWW] S. Sremac, H. J. Woerdeman, H. Wolkowicz, *Error Bounds and Singularity Degree in Semidefinite Programming*, SIAM Journal on Optimization 31(1), 812–836 (2021), DOI 10.1137/19M1289327; arXiv:1908.04357. Its central-path and eigenvalue results concern the relationship between degree and slow convergence, not the constrained-network classification proved here.

[W] J. Wang, *Weighted Geometric Mean, Minimum Mediated Set, and Optimal Simple Second-Order Cone Representation*, SIAM Journal on Optimization (2024), DOI 10.1137/22M1531257; arXiv:2206.05924. Ordinary midpoint representations and their optimal one-dimensional size are prior work. The additional lower barrier and the necessity reduction from arbitrary dense PSD recovery are the distinctions here.

[BM] V. Blanco, M. Martínez-Antón, *On the Structure and Computation of Extremal Mediated Graphs with Applications to Conic Optimization*, Journal of Optimization Theory and Applications 210, article 24 (published 11 July 2026), DOI 10.1007/s10957-026-03048-5. This provides graph-theoretic and mixed-integer methods for mediated structures.

[P26] G. Pataki, *Strict complementarity in semidefinite programming, singularity degree, and the (dis)connection of forward and backward errors*, arXiv:2607.12942 (14 July 2026). This develops normal forms for failure of strict complementarity and results on singularity degree.

[NLL26] M. Nishijima, G. Li, B. F. Lourenço, *Radial-Type Error Bounds for Semidefinite Feasibility Problems without Strict Feasibility: Qualitative Estimates and Asymptotic Tightness*, arXiv:2608.09013 (10 August 2026). This develops explicit radial dependence of error-bound constants and asymptotic tightness results.

Semialgebraic selection and convergent Puiseux parameterization are used as standard real-algebraic-geometric input. No novelty is asserted for those tools, rationality alone, or finite decidability via real algebraic methods.

[BCR] J. Bochnak, M. Coste, M.-F. Roy, *Real Algebraic Geometry*, Springer (1998). Standard source for the semialgebraic growth and selection input.