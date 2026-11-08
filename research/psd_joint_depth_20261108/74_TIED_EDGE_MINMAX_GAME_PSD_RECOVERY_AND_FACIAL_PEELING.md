# Milestone 74 — PSD inverse problems with tied offdiagonal edges: exact MIN–MAX stochastic-game exponents and AND–OR facial peeling

**2026-11-08. PROVED for a broad explicit PSD linear inverse-problem family.** This strictly generalizes the independent-edge multiaction systems of checkpoints 57–62. It is a new construction-level structural theory, not the universal dense-to-game necessity theorem. Connections to *existing* nonarchimedean tropical SDP and Shapley-game theory are noted below.

## Finite matrix-gadget definition

Vertices are 0 (source), 1,...,h (internals), and T=h+1 (terminal). Each internal i has finitely many *modes* a∈A_i, A_i nonempty. Each mode has a nonempty finite set of distinct parent edges
    E_(i,a) ⊂ {(u,v): 0<=u<i<v<=T}.
ALL individual edges across all modes/children are globally disjoint. Allow an optional independent edge (0,t) outside that union.

Fix a sufficiently small positive rational λ, write F_uv=e_u e_v^T+e_v e_u^T, and define kernel generators
    H_(i,a)=E_ii-E_00 + λ Σ_((u,v)∈E_(i,a)) F_uv.
If used, add G=λF_(0,t). Put K=span{all generators}, X*=E00 and L=P_(K^perp) in the Frobenius inner product.

The generator coefficients for different modes are independently recoverable from any one of their globally unique offdiagonal edges. All generators have trace zero and terminal diagonal zero; hence identity and terminal diagonal belong to the measurement span.

## Theorem A — exact stochastic-game sharp exponent for EVERY ambient PSD competitor

Define the finite monotone Shapley map
\[
 w_0=0,\quad w_T=1,\quad
 \boxed{w_i=\min_{a\in A_i}\ \max_{(u,v)\in E_{i,a}}\frac{w_u+w_v}{2}.}
\tag{1}
\]
The operator has a unique value vector w, and all entries are rational. Assume the solution is STRICT:
    0<w1<...<wh<1.
Then X* is uniquely recoverable and the sharp full-matrix exponent is
\[
\boxed{\alpha=\min\{w_1,\ w_t/2\text{ if an independent leading edge is used}\}.}
\tag{2}
\]
In particular \(\omega(\delta)=\Theta(\delta^\alpha)\) as δ→0.

### Unique rational game value

Interpret each internal state i as follows: first the minimizing player selects a mode a, then the maximizing player selects one edge (u,v) from that mode, then fair chance chooses u or v. The boundaries 0,T absorb with rewards 0,1. Every edge has a HIGHER parent v>i. Regardless of either player's policies, choosing the higher parent at each chance transition hits T within h steps, probability at least 2^-h. Thus the h-step Bellman operator is a strict contraction (factor ≤1−2^-h) on the finite internal value vector. It has a unique fixed point. Choosing minimizer and maximizer pure stationary actions at that fixed point gives an ordinary rational harmonic linear system whose transient chain is proper, so all values are rational.

### Global upper bound

Let X≽0 have residual ||P_(K^perp)(X-X*)||_F≤δ. Put Y=X*+P_K(X-X*), E=X−Y. Then ||E||_F≤δ, Y+δI≽0, tr(Y)=1, Y_TT=0, and all diagonal entries are bounded from trace. Write coefficients y_(i,a) for the modes, so
    Y_ii=x_i=Σ_(a∈A_i)y_(i,a),
    Y_uv=λ y_(i,a) for every edge (u,v)∈E_(i,a).
Since every edge is globally unique, the 2x2 PSD principal minor inequality gives
    |y_(i,a)|≤C min_((u,v)∈E_(i,a)) sqrt(U_u U_v),
where U_j=|Y_jj|+δ (boundary U0=O(1), U_T=δ). Therefore
\[
U_i\le \delta+
 C\sum_{a\in A_i}\min_{(u,v)\in E_{i,a}}\sqrt{U_uU_v}.
\tag{3}
\]

Construct a uniform supersolution M_i δ^(w_i). Let h_i be the *maximum* expected absorption time when BOTH players try to delay termination, allowing any modes and edges; the same uniform h-step absorption event bounds it by h2^h, and
    h_i≥1+max_(a∈A_i) max_((u,v)∈E_(i,a))(h_u+h_v)/2,
with h0=hT=0. Set M0=MT≥4 large enough for the boundary U0, and M_i=M0 exp(A h_i). Choose A sufficiently large depending on C and the finite mode counts. For every mode a choose one edge maximizing (w_u+w_v)/2; this exponent is at least w_i by (1), while its expected-time average is at most h_i−1. Thus
    δ+CΣ_a min_edges sqrt(M_uM_v)δ^((w_u+w_v)/2)
        ≤(1/2)M_iδ^(w_i).
If R=max_j U_j/(M_jδ^(w_j))>1 then the maximizer is an internal i, and (3) gives
    R M_iδ^(w_i) ≤ (1+R)/2 M_iδ^(w_i),
contradiction. Hence U_i=O(δ^(w_i)), each generator coefficient y_(i,a)=O(δ^(w_i)), and the leading independent variable is O(δ^(w_t/2)). Trace and ||E||=O(δ) give ||X-X*||_F=O(δ^α).

### Matching positive-definite curve

Choose a minimizing mode a_i attaining (1) at each internal i, and set its coefficient to t^(w_i), setting other mode coefficients to zero; give terminal diagonal t and the independent leading edge coefficient t^(w_t/2) if used. Every edge of a chosen mode has parent-average ≤w_i, by its max definition; therefore diagonal normalization makes its offdiagonal coefficient no larger than λ (up to the harmless source diagonal factor 1+o(1)). For λ<1/[8(h+2)], the normalized full matrix is strictly diagonally dominant and positive definite for small t>0. Every generator before order one lies in K, whereas E_TT∈K⊥. Thus its measurement residual equals t and displacement is Θ(t^α). This proves exact sharpness and uniqueness.

## Theorem B — exact AND–OR exposing closure and minimal facial ranks

Let R be the current set of remaining vertices, containing the source 0. A subset C⊆R\{0} is **exposable in one PSD facial step** if and only if for every internal i∈C and every mode a∈A_i whose ENTIRE edge set E_(i,a) has both endpoints still in R,
\[
\boxed{\exists\,(u,v)\in E_{i,a}\text{ such that }u,v\in C.}
\tag{4}
\]
(If a mode has even one edge touching an already removed coordinate, it imposes no within-face restriction because a free off-face stress entry can fulfill its orthogonality equation.)

The union of any two sets satisfying (4) also satisfies (4), so there is a unique maximal one C_max(R). Remove it, and iterate. This is exactly the canonical maximum-rank PSD facial reduction; the number of iterations is the **minimal singularity degree**, and their cardinalities are the exact facial rank-drop profile.

**Necessity.** For any exposing stress Z∈K⊥, the R-compression S≽0 annihilates the target source. Every mode yields
    Z_ii+2λ Σ_edges Z_uv=0.
If i has positive stress diagonal, and all mode edges remain inside the current face, the sum of the edge entries is negative, so at least one term Z_uv is nonzero. PSD positivity forces BOTH of its endpoints to have positive diagonal, hence to belong to the support C of S. This gives (4). A PSD matrix's range lies in the coordinate span of its positive-diagonal support.

**Sufficiency.** For a closed set C choose artificial rapidly increasing *dual scaling exponents* R_i=10^i (independent of the Bellman weights), set Z_ii=η^(−R_i)>0 on i∈C and zero on other remaining vertices, and Z_00=0. For each mode with i∈C:
- if some edge has an endpoint already removed, choose ONE such off-face entry to solve the orthogonality equation and set its within-face edge entries to zero;
- otherwise (4) gives an edge (u,v) with u,v∈C; set Z_uv=−Z_ii/(2λ) on that edge, other mode edges zero.
For modes at i∉C set all associated offdiagonals zero (and diagonal i=0). Global edge-disjointness makes these independent assignments consistent. The independent source-to-vertex leading edge imposes only Z_(0,t)=0, which holds on the current face because source's PSD row is zero (and can be imposed on the full matrix as well).

All selected within-face negative offdiagonal entries join u<i<v, so
    (R_u+R_v)/2−R_i >= (10R_i−2R_i)/2=4R_i>0,
and after normalization by the stress diagonal their absolute values tend to zero as η→0. The compressed stress is strictly diagonally dominant and PD on the coordinates of C, zero on the others. All ambient K⊥ orthogonality equations hold by the assigned off-face entries. This realizes exactly C with one stress. By the standard maximum-rank greedy facial-reduction theorem, iterating C_max gives minimal degree and exact rank profile.

This is a genuine *AND across modes, OR within tied-edge modes* exposure rule, dual to the primal MIN across modes, MAX across edges stochastic-game equation.

## A simple independent example

Take h=2, target E00 in S^4 and one mode at vertex1 containing BOTH edges (0,2) and (0,3):
    H1=E11−E00+λ(F02+F03),
while vertex2 has one edge (1,3):
    H2=E22−E00+λF13.
The game value solves w1=max(w2/2,1/2)=1/2 and w2=(w1+1)/2=3/4. The sharp exponent is 1/2, and the exposing layers are {3},{1,2} (degree 2). If the second edge F03 is removed from H1, the one-edge harmonic values instead become (1/3,2/3) and the exposing layers are {3},{2},{1} (degree 3). The tied-edge mode changes both invariants via an actual MAX operation, not merely by adding a separately controllable action.

## Research significance and limitations

- This model includes independent one-edge multi-action modes as the special case |E_(i,a)|=1; thus it strictly extends checkpoints 57–62.
- The game form is connected to **established tropical/nonarchimedean SDP theory**: Allamigeon–Gaubert–Skomra, *Solving generic nonarchimedean semidefinite programs using stochastic game algorithms*, J. Symbolic Computation 85 (2018), DOI 10.1016/j.jsc.2017.07.002; and *Tropical spectrahedra* (2019), arXiv:1610.06746. This connection is not a novelty claim for min–max Shapley games.
- The present proof gives a *complete exact recovery-and-depth characterization for this explicit rational PSD construction family*. It does NOT prove that arbitrary dense PSD kernels admit an equivalent tied-edge game at fixed nullity/rank profile. General signed/determinantal cancellations are potential additional mechanisms.
- No assumption that a finite signed support hypergraph alone classifies arbitrary dense matrices is made; checkpoints 63 and 65 show why unbounded-order determinant data can matter in general.