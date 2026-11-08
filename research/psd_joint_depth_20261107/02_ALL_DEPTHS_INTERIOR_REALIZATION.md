# Checkpoint 02 — every rational interior exponent at every depth, unrestricted dimension

**Verified theorem (2026-11-07).** For each integer d>=2, target rank r>=1 and rational 2^{-d}<=alpha<1/2, some finite-dimensional real PSD inverse problem uniquely recovers a rank-r target, has *exact* minimal facial-reduction degree d and *exact* sharp full-matrix Hölder exponent alpha. The matrix size is finite but not claimed minimal. The endpoint alpha=1/2 for d>=3 and the fixed-size spectrum remain unresolved.

## Sparse graph construction and proof tools

A midpoint graph has a source O (weight 0), terminals T (weight 1), and internal weighted vertices v in (0,1) with two distinct parents a(v),b(v) satisfying 2w_v=w_a+w_b. Vertices may be grouped into independent components sharing only O. Put diagonal variables x_v in a symmetric matrix, and off-diagonal lambda*x_v at the parent edge of v, with fixed lambda=1/(4*number_of_vertices). If desired alpha is below all interior weights and 2alpha is a vertex, place another free off-diagonal variable lambda*z on edge (O,2alpha), which is not occupied by any internal parent edge. Measure orthogonal projection off the pencil range, trace, and every terminal diagonal; target E_OO.

**Sharp exponent.** For any PSD matrix X with measurement residual <=delta, Y=projection_to_pencil(X) satisfies Y+delta*I>=0. Its principal 2x2 minors give (|x_v|+delta)^2<=C(|x_a|+delta)(|x_b|+delta). The finite harmonic Markov-chain maximum principle implies |x_v|=O(delta^{w_v}); the optional edge gives |z|=O(delta^alpha). Trace controls x_O, projection controls all off-pattern coordinates. Hence the full recovery exponent is at least the smallest relevant weight. Conversely x_v=t^{w_v}, x_T=t and z=t^alpha, normalized by trace, is PSD by strict diagonal dominance after diagonal congruence (each normalized edge equals lambda). Its displacement has the desired order and its residual order is t, yielding equality.

**Exact depth.** At every remaining coordinate face, the exposing-stress equations are Z_vv+2lambda*Z_{a(v),b(v)}=0, Z_OO=0 and (if present) Z_{O,2alpha}=0. The maximal simultaneously removable set C of non-source vertices has the closure rule: whenever internal v in C has both parents remaining, those parents also lie in C. Necessity follows because a PSD compression with nonzero off-diagonal forces both incident diagonal entries positive. Sufficiency: set Z_vv=epsilon^{-w_v^2} on C, zero outside, and Z_{a(v),b(v)}=-Z_vv/(2lambda), using unrestricted off-face entries if a parent was already removed. After diagonal normalization, within-face off-diagonal magnitudes are (2lambda)^{-1}epsilon^{(w_a-w_b)^2/4}->0. Hence this stress is positive definite on C. As in the canonical greedy argument, no alternative chain removes more axes earlier. Therefore the combinatorial greedy peeling count is exactly the *minimal* singularity degree. For separate components glued only at O, peeling is componentwise: the depth is the maximum of component depths and the exponent the minimum of component exponents.

## Base realization at the natural dyadic depth e

For rational 0<alpha<1/2 choose e>=2 so 2^{-e}<=alpha<=2^{-(e-1)}, and set c=2^{-(e-1)}. Create the dyadic spine vertices 1,1/2,1/4,...,c, with parent pairs (0,2^{-(j-1)}) for 2^{-j}. Express 2alpha=c+(1-c)*a/b and adjoin the affine grid c+j(1-c)/b (1<=j<b), omitting duplicate spine weights. New grid vertices have their immediate grid neighbors as parents. Spine vertices at coincidences keep spine parents; all midpoint equations are still exact. All interior weights >=c>=alpha and 2alpha is a vertex. If alpha<c, add the extra edge O--2alpha; if alpha=c, the spine coordinate supplies the leading order. The exponent is exactly alpha.

Peeling removes the terminal first, then successively smaller spine vertices; after the final spine vertex is eligible, all remaining grid vertices are eligible simultaneously. It therefore has degree exactly e.

## Depth-d helper with exponent approaching 1/2

Fix d>=3, m>=1. Set s=d-3, q=2^s/(2^s+1), a=(1-q^m)/(2-q^m), and x_i=1-q^i(1-a) for i=0,...,m. Create root R of weight x_0=a, core X_i of weight x_i (1<=i<=m), terminal T=1 and source O=0. Root parents are (O,X_m), since x_m=2a.

For s=0, X_i has parents (X_{i-1},T), interpreting X_0=R. For s>=1, add Y_{i,j} of weight y_{i,j}=x_i+2^{-(s-j+1)}(1-x_i), j=1,...,s. Let X_i have parents (X_{i-1},Y_{i,1}), Y_{i,j} have parents (X_i,Y_{i,j+1}) when j<s, and Y_{i,s} have parents (X_i,T). All are midpoint identities. All weights are distinct: a collision between core levels and support levels would imply an impossible rational equality between a power of q=2^s/(2^s+1) and a fraction 1-2^{-k}; collisions across two support levels similarly contradict the 2-adic valuations (and the remaining k=s, one-step possibility has unequal odd numerators). Root a is uniquely smallest.

Peeling is T, then Y_{i,s},...,Y_{i,1} layer by layer, then all X_i, finally R: exactly s+3=d steps. Each later layer is blocked by a still-present parent chain through R. Exponent is a=(1-q^m)/(2-q^m), increasing to 1/2 as m grows.

## Gluing proves the theorem

Take the dyadic-spine base for alpha with degree e<=d. If e=d, done. If e<d, choose the depth-d helper with a>alpha (possible since alpha<1/2), and glue the two graphs at O. The exponent is min(alpha,a)=alpha and minimal depth max(e,d)=d. The target is E_OO, rank one. Adjoin a fully observed positive block and cross entries to increase target rank without changing the exponent or facial depth.

Sturm's error bound gives the necessary alpha>=2^{-d} for any PSD recovery map of depth d. This checkpoint proves sufficiency for **all rational alpha strictly below 1/2** and >=2^{-d}. The issue of alpha=1/2 at degree >=3 is specifically *not* settled here.

## Verification
Exact Fraction arithmetic and greedy-peeling tests were run for d=3,...,8 and m=1,...,4; dyadic-spine and source-gluing examples passed their midpoint and exact-depth assertions. These tests support but are not used as substitutes for the proofs above.