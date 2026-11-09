# A proved facial-peeling invariant for sparse harmonic PSD recovery systems

**Research progress note — 7 November 2026.** This establishes a new, fully finite **within-family** theorem for the sparse midpoint constructions in `Sharp_PSD_Stability_Weighted_Flags_Memorandum.md`. It does **not** prove that arbitrary dense PSD recovery problems preserve minimal facial-reduction degree under network reduction. Accordingly, it is not the complete joint compatibility classification requested.

## 1. The sparse system

Let the vertices be `0,1,...,h,T`, where `T=h+1`, with weights

\[
0=w_0<w_1<\dots<w_h<w_T=1.
\]

For each `i=1,...,h`, choose distinct parent indices `a(i)<i<b(i)` satisfying

\[
2w_i=w_{a(i)}+w_{b(i)}.
\]

Fix `lambda>0` (smallness is needed for the recovery construction, but not for the facial-peeling theorem). Define a symmetric pencil with diagonal `x_0,...,x_T` and off-diagonal entry `lambda x_i` at the parent edge `{a(i),b(i)}`. Distinct `i` use distinct parent edges, since they have distinct midpoint weights. Optionally, when `alpha` is not one of the interior weights, put `lambda z` on the otherwise-unused edge joining `0` to the vertex of weight `2alpha`. (The optional coordinate is allowed only under the original construction's constraint `2alpha in {w_1,...,w_h,1}` and `alpha<=w_1`.) Measure orthogonal projection off the pencil range, trace, and the terminal diagonal `x_T`. Let `X_*=E_{00}`.

The preceding recovery theorem proves the exact exponent `alpha` for this system.

For the singularity-degree computation, let `K` be its measurement kernel. An exposing stress `Z in K^perp` must satisfy `Z_{00}=0` and, for each internal vertex,

\[
Z_{ii}+2\lambda Z_{a(i),b(i)}=0. \tag{1}
\]

If an optional `z` is present, it also must satisfy `Z_{0,j}=0` for its unique edge. The terminal diagonal is unrestricted. Formula (1) follows by pairing `Z` with the kernel vector changing `x_i` by one and `x_0` by minus one (to preserve trace).

## 2. Exact combinatorial peeling algorithm

Initially `R=empty`. The **remaining face** is the PSD cone on coordinate subspace `W={0,...,T}\R`. Define `C(R)` as the **largest** subset of `W\{0}` with the following closure rule:

> If an internal vertex `i` belongs to `C(R)` **and both its parents remain in `W`**, then both parents must also belong to `C(R)`.

`C(R)` exists, since unions of sets satisfying the rule also satisfy the rule. Compute it by starting with `W\{0}` and repeatedly deleting any internal `i` whose two parents remain in `W` but whose parent set is not contained in the current candidate set.

Now replace `R` by `R union C(R)`, and repeat until only vertex zero remains. Let `p(G)` be the number of iterations.

### Theorem: the sparse system has singularity degree exactly `p(G)`.

**Proof, part A — any exposing stress is confined to `C(R)`.** Let `Z in K^perp` expose the current face. Thus `Z_{W,W}` is PSD and `Z_{00}=0`. Let

\[
S=\{i\in W\setminus\{0\}:Z_{ii}>0\}.
\]

If `i in S` is internal and both parents are in `W`, equation (1) implies `Z_{a(i),b(i)} !=0`. A PSD matrix can have a nonzero off-diagonal entry only if **both** corresponding diagonal entries are positive. Therefore both parents belong to `S`. Thus `S` satisfies the closure rule, so `S subset C(R)`. All diagonal entries of `Z_{W,W}` vanish outside `S`, and PSD then makes all their rows vanish. Hence the stress's range lies inside the coordinate span of `C(R)`. In particular no exposing step can remove coordinate axes outside `C(R)`.

**Proof, part B — there exists one stress exposing all of `C(R)`.** Put `C=C(R)`. For a parameter `epsilon in (0,1)`, prescribe on the remaining face

\[
Z_{ii}=\epsilon^{-w_i^2}\ \ (i\in C),\qquad
Z_{ii}=0\ \ (i\in W\setminus C),
\]

and `Z_{00}=0`. For each `i in C` with **both parents still in** `W`, prescribe

\[
Z_{a(i),b(i)}=-\frac{Z_{ii}}{2\lambda}.
\]

The closure condition ensures `a(i),b(i) in C`. For an internal `i in C` having at least one removed parent, prescribe the same value for its **off-face** entry `Z_{a(i),b(i)}`; these off-face entries are unrestricted by positive semidefiniteness of the compression. Set entries of all remaining internal parent edges to zero, and set any other entries to zero, apart from the optional-edge constraint `Z_{0,j}=0` (its edge is distinct from every parent edge). This satisfies all of (1) and the optional condition. The diagonal of an already removed vertex can be set to zero.

Normalize the `C x C` compression by the square roots of its diagonal entries. Every nonzero off-diagonal entry comes from a midpoint relation, and has absolute normalized value

\[
\frac1{2\lambda}
\epsilon^{-w_i^2+(w_{a(i)}^2+w_{b(i)}^2)/2}
=
\frac1{2\lambda}\epsilon^{(w_{a(i)}-w_{b(i)})^2/4}
\longrightarrow0.
\]

Consequently the compression is positive definite on `C` and zero on its complement, for all sufficiently small positive `epsilon`. It exposes **exactly** the coordinate axes in `C`.

**Proof, part C — greedy peeling minimizes the number of steps.** The construction in B shows that the algorithm is an admissible facial-reduction chain. Conversely, compare it with any other exposing chain, allowing its intermediate faces to be non-coordinate. Inductively assume the greedy coordinate face is contained in the competing chain's face. The competing stress is PSD when compressed to the greedy face. By part A its range on that coordinate face is confined to `C(R)`. All coordinate axes remaining after greedy removal therefore lie in the competing stress's kernel; by PSD, their zero quadratic forms imply membership in the kernel on the whole competing face. Thus the next greedy face remains contained in the next competing face. If a competing chain reaches the minimal face in fewer steps, so would the greedy chain, contradicting its termination count. Therefore the minimum singularity degree equals `p(G)`. **QED.**

The process always terminates: if the terminal remains, it is exposed; otherwise choose the largest remaining internal index `i`. Its larger parent is already removed, so `{i}` is admissible. Consequently `p(G)<=h+1`, and the first layer is always `{T}`.

## 3. Consequences and exact examples

The sharp exponent and the minimal exposing degree are now separately computable from **the same finite data**. The degree depends on the *parent assignment*, not simply the rational weights or the minimum weight.

For `alpha=1/3`:

* A two-internal-vertex network with weights `(1/3,2/3)` and parents `(0,2),(1,3)` peels as `{3}`, `{2}`, `{1}` and has depth **3** (nullity `3`).
* A three-internal-vertex network with weights `(1/2,2/3,5/6)` and parents `(0,4),(1,3),(2,4)` peels as `{4}`, `{1,2,3}` and has depth **2** (nullity `4`). Here `alpha=1/3` is encoded by the optional edge joining the source to weight `2/3`.
* A four-internal-vertex network with weights `(1/3,1/2,2/3,5/6)` and parents `(0,3),(1,3),(2,4),(3,5)` peels as `{5}`, `{4}`, `{3}`, `{1,2}` and has depth **4** (nullity `5`).

Thus one rational exponent can be realized at three different exact degrees using explicitly specified finite PSD systems.

The exact enumerator `psd_depth_peeling.py` computes all **sparse-network realizable** exponent–degree pairs through small nullities. For nullity at most 5 its counts of distinct attainable exponents at each degree are:

| Nullity bound | Degree 1 | Degree 2 | Degree 3 | Degree 4 | Degree 5 |
|---|---:|---:|---:|---:|---:|
| 1 | 1 | 0 | 0 | 0 | 0 |
| 2 | 1 | 2 | 0 | 0 | 0 |
| 3 | 1 | 3 | 4 | 0 | 0 |
| 4 | 1 | 7 | 12 | 9 | 0 |
| 5 | 1 | 23 | 49 | 32 | 20 |

Degree 1 entries in this table refer to exponent `1/2`, not the additional Lipschitz exponent `1`, which is available at degree one with a different, fully stressed system.

## 4. The exact unproved implication

The theorem above proves **sufficiency and exact depth** for sparse harmonic PSD-network constructions.

To conclude the *universal* triple `(n,rank X_*,d)` classification, one must additionally prove that **every** arbitrary dense problem with sharp exponent `alpha` and singularity degree `d` has a constrained mediated network with at most `n-rank X_*-1` internal nodes and peeling degree **exactly** `d` (or provide another necessary-and-sufficient compatibility invariant). The existing weighted-flag reduction preserves the exponent but does not control the depth of its network, and the diagonal bound `w_i >= 2^{-(d-1)}` does not supply that implication.

No such universal implication is claimed in this note. In particular, the sparse-network pair catalogue is a rigorously certified lower inclusion in the universal joint spectrum, **not** a complete classification for arbitrary dense maps.