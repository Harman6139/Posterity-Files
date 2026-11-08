# Milestone 52 — vertex blow-up preserves sharp exponent and exact facial peeling profile

Date: 2026-11-08. **PROVED within the sparse midpoint-incidence family, with full ambient PSD competitor bounds.** No dense-to-sparse theorem is assumed. This is a constructive sufficiency principle for all prescribed exposed-rank profiles.

## Definition of a vertex blow-up

Start from a finite strict harmonic midpoint network with source O (weight 0), terminal T (weight 1) and h internal vertices v. Every internal v has distinct parents a(v),b(v) with 2w_v=w_a+w_b; parent edges for different internal vertices are distinct. An optional leading source-to-vertex edge has independent variable z and weight p with 2p=w_target. The network has greedy exposing layers C_1,...,C_d, with source never exposed.

Choose any positive integer multiplicity kappa_v for each non-source vertex v. Replace v by kappa_v coordinates v^{(1)},...,v^{(kappa_v)}, all having *the same diagonal variable x_v*; the original parent-edge generator for v is placed on the two distinguished parent representatives a(v)^{(1)},b(v)^{(1)} (and source O when necessary). An optional leading edge joins O to its target's representative. Keep all other offdiagonal entries zero.

Let V be this linear pencil's range and measure P_(V^perp)X, tr(X), and the terminal variable x_T. Set X_*=E_OO. Every fiber and PSD competitor is a full matrix on 1+sum_v kappa_v coordinates; no restriction to block diagonal competitors is made.

## Theorem A (sharp exponent unchanged)

The blown-up problem has unique PSD solution X_*, and its optimal *full-matrix* recovery exponent is the original harmonic leading exponent
    alpha = min{ min_internal w_v, p if optional }.

**Proof.** For arbitrary PSD X with residual <=delta, let Y=P_V X. Then ||X-Y||_F<=delta and Y+delta I is PSD. The measured trace bounds all diagonal entries and hence every pencil coordinate x_v; the terminal coordinate has |x_T|<=C delta. The principal 2x2 submatrix on distinguished parent representatives gives
    (|x_v|+delta)^2 <= C (|x_a|+delta)(|x_b|+delta)
for each internal vertex. Taking logarithms and applying the inverse positive transient Markov matrix gives
    |x_v|<=C_v delta^{w_v}.
The optional leading edge gives |z|<=C delta^p. All clone diagonal entries equal x_v, and the projection error controls every other matrix entry. Trace then controls x_O-1, proving omega(delta)<=C delta^alpha; sending delta→0 proves uniqueness.

For a matching curve, choose x_O=1, x_v=t^{w_v}, terminal x_T=t and optional z=t^p, followed by trace normalization. Scale coordinate v^{(a)} by t^{-w_v/2} and source by 1. After diagonal congruence the matrix has all diagonal entries one, while its offdiagonal entries are exactly lambda (up to a common bounded factor from source normalization), only on the distinguished parent edges and optional edge. Take fixed lambda<1/[4(1+sum_v kappa_v)]; strict diagonal dominance gives positive definiteness for all sufficiently small t. The measurement residual is Theta(t) and the displacement is Theta(t^alpha). Thus equality of exponents holds.

## Theorem B (exact greedy facial-degree and rank-drop preservation)

The blown-up problem has the *same* number d of minimal exposing steps as the original network and its exact canonical exposed-rank profile is
\[
    \boxed{(\sum_{v\in C_1}\kappa_v,\ldots,\sum_{v\in C_d}\kappa_v)}.
\]

**Proof.** The source is always in the current PSD face because X_*=E_OO. Any exposing stress on the current coordinate face is PSD and annihilates source, so its entire source row/column is zero. The kernel generator for an internal vertex v is the sum of all clone diagonal matrices D_v=\sum_a E_(v,a),(v,a), minus a trace adjustment on source, plus lambda F_{a(v)^{(1)},b(v)^{(1)}}. Pairing with a stress S gives
    sum_a S_(v,a),(v,a) + 2lambda S_(a(v)^{(1)},b(v)^{(1)}=0.
For a terminal no kernel generator exists, as its variable is measured. If any clone of an internal v has strictly positive diagonal in S, the sum is positive. If both parent representatives remain in the current face, the indicated offdiagonal is nonzero; PSD forces the *two parent representatives* also to have positive diagonal. Therefore every removable collection of clones projects to a set C of vertices satisfying the original greedy closure rule: whenever v∈C and both its parents remain, both parent vertices belong to C. This proves that a clone of a vertex unavailable to the original greedy process cannot be removed earlier, even by a dense non-diagonal exposing stress.

Conversely, for every original greedily removable vertex set C, construct one exposing stress positive definite on **all clones** of each v∈C and zero on other remaining clones. Assign every clone diagonal \(\eta^{-w_v^2}\), for a small \(\eta>0\). For every generator with both parent representatives still in the current face, set the corresponding offdiagonal stress entry to \(-\kappa_v \eta^{-w_v^2}/(2\lambda)\) if v∈C, and zero otherwise. When some parent is already removed, satisfy that generator equation by a freely chosen off-face entry. Parent-edge distinctness makes these choices consistent; source-to-target leading edge imposes only a source-row equality, automatically satisfied inside the face and solvable using removed coordinates when necessary.

For an active within-face offdiagonal with both parents in C, after congruence by the positive diagonal stress, its magnitude is
\[
 \frac{\kappa_v}{2\lambda}
  \eta^{(w_{a(v)}^2+w_{b(v)}^2)/2-w_v^2}
 =\frac{\kappa_v}{2\lambda}\eta^{(w_{a(v)}-w_{b(v)})^2/4}\to0.
\]
Thus for sufficiently small eta the compressed stress is positive definite on precisely all clones in C and zero elsewhere, by strict diagonal dominance. This constructs the full greedy step and shows its rank is exactly the sum of clone multiplicities. Induction on the remaining face proves the displayed canonical rank-drop profile. By the standard maximal-rank greedy facial-reduction principle, it is the *minimal* singularity degree. QED.

**Important precision:** The proof does not say arbitrary exposing stresses are diagonal; it uses only positivity to force parent representative diagonals, and constructs one stress realizing the maximal closed support. Thus dense offdiagonal stress entries cannot yield earlier removal of any clone.

## Corollary: Sturm's lower endpoint is attained at EVERY facial rank profile

Fix any positive integer composition \((s_1,\ldots,s_d)\), \(d\ge2\). Take the dyadic chain with one terminal T of weight one and one internal vertex of each weight
\[
   2^{-1},2^{-2},\ldots,2^{-(d-1)},
\]
where the vertex of weight \(2^{-j}\) has parents (source, vertex of weight \(2^{-(j-1)}\)). Add an independent leading edge (source, vertex of weight \(2^{-(d-1)}\)), of weight \(p=2^{-d}\). Its minimal greedy peeling profile is (1,...,1).

Blow up the vertex exposed at step j into exactly s_j clones. By Theorems A and B, the resulting PSD problem has **exact** singularity degree d, exact canonical rank profile \((s_1,\ldots,s_d)\), target nullity \(\nu=\sum_j s_j\), rank-one target (or arbitrary target rank by positive padding), and optimal exponent
\[
\boxed{\alpha=2^{-d}}.
\]
Sturm's classical error bound proves \(\alpha\ge2^{-d}\) for all PSD instances at degree d. Therefore **the universal smallest attainable exponent at EVERY prescribed rank profile is exactly \(2^{-d}\)**. This complements the sharp largest attainable exponent \(\beta(s_1,\ldots,s_d)\) from checkpoint 45 and completely classifies BOTH endpoints for ALL rank profiles and ALL degrees.

The dyadic lower endpoint is not claimed to be the only attainable exponent in between.

## Scope and audit

This is a constructive sufficiency theorem, not a full dense-to-sparse representation. The competitor estimate is global in the ambient PSD cone. The exposing-stress construction handles all clones at once and uses the exact scaled parent-edge identity, preserving the rank profile; it is not an informal assertion that adding fixed zero rows changes only the first facial rank.

The strict graph vertex ordering and distinct parent edges ensure independent stress equations. All arithmetic is rational in the graph data, except harmless positive scaling constants used to prove positivity of a stress; rational sufficiently small eta works. Target eigenvalues and measurement-space norms only affect recovery constants.

Bibliographic novelty of clone-type spectrahedral constructions and mediated graphs has not been audited.