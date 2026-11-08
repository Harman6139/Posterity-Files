# Milestone 45 — UNIVERSAL sharp recovery-exponent endpoint for EVERY PSD facial rank profile at EVERY depth

**2026-11-08. PROVED for arbitrary dense real PSD measurement maps without weighted-flag universality, sparse reductions, or quantifier elimination.** This supplies a compact **closed combinatorial formula** for the *largest possible* sharp recovery exponent at any prescribed facial-reduction rank-drop profile, together with a matching rank-one sparse construction at exactly that profile. It does not yet enumerate **all smaller attainable rational exponents** for every fixed dimension and degree.

## Theorem — complete sharp upper-endpoint classification by profile

Let L:S^n→R^m be any real linear map with a uniquely recoverable positive-rank PSD target X*. Let d≥2 be its minimal singularity degree, computed by maximal-rank greedy facial reduction, and let
\[
(s_1,\ldots,s_d),\quad s_j\ge1,\quad\sum_j s_j=\nu=n-\operatorname{rank}X_*,
\]
be the consecutive exact exposed ranks. Put
\[
q_j=2^{s_j}-1\quad(2\le j\le d),\quad
P_1=1,\quad P_\ell=\prod_{j=2}^{\ell}q_j,\quad
D=\sum_{\ell=1}^{d}P_\ell.
\]
Then the exact optimal full-matrix recovery Hölder exponent obeys
\[
\boxed{\alpha(\mathcal L,X_*)\le
\beta(s_1,\ldots,s_d):=
\frac{2^{s_d-1}P_{d-1}}{D}.}
\tag{1}
\]
For d=2 this equals 1/2. For d≥3 it is strictly less than 1/2, since
\[
\beta=\frac{1}{2\left(1+2^{-s_d}
   \sum_{\ell=1}^{d-2}\frac{1}{\prod_{j=\ell+1}^{d-1}q_j}\right)}.
\tag{2}
\]
**Exact sharpness for EVERY integer rank profile:** there exists a finite-dimensional uniquely solvable rank-one PSD inverse problem with precisely this greedy facial rank profile and full ambient sharp exponent exactly β. Fully measured positive-definite padding gives any positive target rank r, without changing the nullity, profile, or exponent.

Thus (1) is a **necessary-and-sufficient closed arithmetic characterization of the maximum attainable sharp exponent given the complete facial rank-drop profile** for all dimensions and all depths, including maximal degree d=ν (where β=1/ν).

## Part I. Universal forced kernel flags at every step

Fix canonical maximal-rank exposed spaces
\[
\mathbb R^n=U\oplus R_d\oplus R_{d-1}\oplus\cdots\oplus R_1,
\qquad U=\operatorname{range}X_*,
\]
where dim R_j=s_j and the j-th exposing stress has PSD compression on
\[
W_{j-1}=U\oplus R_j\oplus\cdots\oplus R_d
\]
that is strictly positive on R_j and zero on the other blocks. Put K=ker L and K_{j-2}=K∩S(W_{j-2}) for j≥2.

**Conic flag lemma (each j=2,...,d).** There exist an integer 1≤k_j≤s_j, an orthogonal decomposition
\[
R_j=V_{j,1}\oplus\cdots\oplus V_{j,k_j},
\]
and actual matrices H_{j,h}∈K_{j-2}, such that:
- their compression to V_{j,h} is positive definite;
- their compression to the remaining block
\[
(V_{j,h}\oplus\cdots\oplus V_{j,k_j})\oplus R_{j-1}
\]
is zero outside the V_{j,h}×V_{j,h} block;
- their entries involving shallower R_i with i≤j-2 vanish, since they are supported on W_{j-2};
- all remaining entries may be arbitrary dense.

**Proof of the conic flag lemma.** Start with V_rem=R_j. Set R=V_rem⊕R_{j-1} and Q_R={P_R H P_R:H∈K_{j-2}}⊂S(R). The (j-1)-th compressed exposing stress is PSD and positive definite on R_{j-1}; its compression to R is in Q_R^\perp. If Q_R∩PSD={0}, the strict semidefinite Gordan–Stiemke alternative gives a positive-definite Z∈Q_R^\perp. Zero extend Z to W_{j-2}: the extension is orthogonal to every K_{j-2} matrix (by the definition of Q_R), and thus lies in (K_{j-2})^\perp inside S(W_{j-2}). The compression-annihilator identity
\[
(K\cap S(W_{j-2}))^\perp_{S(W_{j-2})}
=P_{W_{j-2}}K^\perp P_{W_{j-2}}
\]
lifts this zero extension to an ambient stress in K^\perp whose entire W_{j-2}-compression is PSD and has rank dim R_{j-1}+dim V_rem>s_{j-1}. This contradicts the **canonical maximal exposing rank s_{j-1}**. Hence Q_R∩PSD contains nonzero C, and PSD complementarity with the (j-1)-th stress PD on R_{j-1} forces C supported on V_rem. Choose H_{j,h}∈K_{j-2} lifting C; let V_{j,h}=range C⊂V_rem, and replace V_rem by its orthogonal complement of V_{j,h}. Iterate. The dimension drops at each step, so k_j≤s_j and the claimed exact compression support properties follow. QED.

**Note:** This argument only uses ranks of the first d-1 maximal stresses; the last stress is not otherwise required. No Gordan lift is asserted to be globally PSD in stages j≥3: its compression on the *current face* is PSD, which is precisely the facial-reduction condition.

## Part II. A finite layered midpoint system valid against ALL dense coefficients

For the integers k_j produced above, set q'_j=2^{k_j}-1 (j≥2), P'_1=1, P'_\ell=∏_{j=2}^\ell q'_j, and
\[
D'=\sum_{\ell=1}^{d}P'_\ell,\qquad
M_1=1,\qquad M_{d+1}=0,\qquad
M_j=\sum_{\ell=j+1}^{d+1}\frac{P'_{\ell-1}}{D'}
\quad(2\le j\le d).
\]
Equivalently define the gap Δ_2=1/D' and recursively
\[
\Delta_{j+1}=q'_j\Delta_j\quad(2\le j\le d),\qquad
M_j=\sum_{\ell=j+1}^{d+1}\Delta_\ell .
\]
Then
    1=M1>M2>...>Md>Md+1=0,
and
\[
M_j=M_{j-1}-2^{-k_j}(M_{j-1}-M_{j+1})
\quad(2\le j\le d).
\]
**Within each exposed layer j≥2**, assign weights
\[
w_{j,h}=M_{j-1}-2^{-h}(M_{j-1}-M_{j+1}),
\quad h=1,\ldots,k_j.
\]
Then 0<w_{d,1}<...<w_{d,k_d}=M_d<w_{d-1,1}<...<M_{d-1}<...<w_{2,k_2}=M_2<1. Set w=0 on U and w=1 on R_1. The weights satisfy
\[
2w_{j,1}=M_{j+1}+M_{j-1},\qquad
2w_{j,h}=w_{j,h-1}+M_{j-1}\quad(h>1),
\]
and \(w_{j,k_j}=M_j\). This is a *layered finite harmonic midpoint graph*, completely determined by the numbers k_j.

Form the generalized polynomial
\[
Y(z)=X_*+\sum_{j=2}^{d}\sum_{h=1}^{k_j}
           z^{w_{j,h}}H_{j,h}+zP_{R_1}.
\]

**Universal all-block order check.** For H_{j,h}, by the conic flag lemma it is supported on W_{j-2}, hence has zero blocks involving shallower layers R_i, i≤j-2. Its compression to the remaining part of R_j and R_{j-1} is supported on V_{j,h}. Thus a potentially nonzero block not joining V_{j,h} to itself must have at least one endpoint in:
- U (weight 0);
- a deeper layer R_{j+1}...R_d (weight ≤M_{j+1});
- an earlier V_{j,u}, u<h (weight ≤w_{j,h-1}).

The other endpoint has weight at most M_{j-1}. Therefore its pair-weight is at most
    max(M_{j+1}+M_{j-1}, w_{j,h-1}+M_{j-1})
    ≤ 2w_{j,h}
by the midpoint identities. The V_{j,h} diagonal has exact weight 2w_{j,h}. Every coefficient obeys the PSD order criterion, even if the original kernel is fully dense. P_{R1} at exponent one is positive definite on the terminal exposed block. The first diagonal coefficient at each V_{j,h} is strictly positive there by the conic flag; no earlier coefficient can have an entry on that diagonal because of the support and ordering properties.

Apply the **fully proved PSD coefficient-rescaling lemma**: after multiplying the coefficient at exponent e by fixed exp(σe²) with sufficiently large σ, the generalized polynomial is strictly positive definite for small z>0. Its proof normalizes each valuation block by exp(σw²/2)z^{w/2}, obtaining a positive block-diagonal limit as σ→∞ and vanishing normalized offdiagonal entries exp[-σ(w-w')²/4]. All coefficients before order one lie in K, while the final P_{R1}≽0 does not lie in K (by uniqueness). Hence the residual is Θ(z), and the displacement is Θ(z^{w_{d,1}}). We have proved
\[
\alpha\le w_{d,1}.
\]
The deepest first weight is
\[
w_{d,1}=\frac12M_{d-1}
=\frac{2^{k_d-1}P'_{d-1}}{D'}.
\]

## Part III. Monotonicity in the number of conic kernel layers

For d=2 the expression equals 1/2 for every k2. For d≥3 it rewrites as
\[
w_{d,1}=\frac{1}{
2\left(1+2^{-k_d}
\sum_{\ell=1}^{d-2}
\frac{1}{\prod_{j=\ell+1}^{d-1}(2^{k_j}-1)}\right)
}.
\]
Every k_j≥1 appears through a positive factor that *decreases* the parenthesized positive correction when k_j increases; consequently the exponent is nondecreasing in all k_j. Because k_j≤s_j, we obtain the claimed profile bound (1). QED.

## Part IV. Exact sharpness at every rank profile

For given s1,...,sd, use the weights above with k_j=s_j and create one sparse harmonic midpoint graph with a single terminal R1 vertex of weight one, and s_j internal vertices in layer j≥2, with parent pairs:
- first vertex V_{j,1} has parents (the **last** vertex of deeper layer j+1, the last vertex of shallower layer j-1), using source O=0 for j=d and the terminal for j=2;
- later V_{j,h}, h>1, has parents (previous V_{j,h-1}, the last vertex of shallower layer j-1).

Each pair has distinct endpoints and is used by exactly one internal generator. The displayed weight identities verify that this is a valid mediated network. The sparse PSD pencil with small coefficient λ, one diagonal variable per vertex, offdiagonal λ times the internal variable on its parent edge, trace and terminal measurements, and target E_OO has **exact full ambient recovery exponent** min internal weight=w_{d,1}. The upper bound for arbitrary PSD competitors follows from the harmonic inequalities and the transient Markov maximum principle; normalized monomial choices give a matching positive-definite curve.

Its greedy facial peeling stages remove, in order:
    terminal R1;
    all s2 layer-2 vertices;
    all s3 layer-3 vertices;
    ...;
    all sd layer-d vertices.
At stage j, layer-j vertices are eligible because their higher parent in the preceding layer has already been removed, whereas any vertex in a later layer still has both parents present and including it forces a descending-parent chain to the source, which cannot be exposed. Thus the profile is exactly (1,s2,...,sd), and the minimal degree d is confirmed by the previously proved maximal-rank stress-peeling theorem. Add s1-1 separately fully measured null coordinates: they join the first exposing step, changing the rank profile to (s1,s2,...,sd) while leaving exponent and minimal degree unchanged. Add fully measured positive coordinates to obtain arbitrary positive target rank. Therefore the universal upper bound is attained for every profile.

## Consequences and scope

- This formula **unifies** all previously derived sharp endpoints: degree 2 yields 1/2; degree 3 yields the two-layer formula of checkpoint 43; maximal depth with every s_j=1 gives exactly 1/d; all higher degrees and nontrivial rank profiles are covered.
- In particular for every d≥3, α<1/2, because the positive correction in (2) is nonzero.
- It gives an explicit rational **maximum** sharp exponent at any prescribed profile and matrix size, not merely a computable semialgebraic upper bound.
- **Open stronger problem:** this does NOT yet characterize every rational exponent below β attainable at each profile, or prove dense-to-sparse exact-degree equivalence for all α. The original user’s requested **full joint combinatorial spectrum** is therefore not completely proved. The new theorem solves its sharp upper-endpoint half in a strong universal sense.

## Audited hypotheses and novelty

The exposing chain is the maximal-rank greedy chain (its minimality is standard facial-reduction theory). The Gordan–Stiemke alternative is applied only to finite-dimensional *linear subspaces* of symmetric matrices. Stress lifting is handled by the exact compression–annihilator identity; no unjustified zero-extension to the full measurement kernel is assumed at later steps. Full PSD positivity of the witnessing curve is established by diagonal congruence, not inferred from 2×2 minors. The construction controls arbitrary ambient PSD competitors by the harmonic upper bound. These are complete load-bearing proofs.

Bibliographic priority of the new sharp rank-profile formula is not independently established; the existing mathematics of facial reduction, mediated sets and PSD rescaling is not claimed novel in isolation.