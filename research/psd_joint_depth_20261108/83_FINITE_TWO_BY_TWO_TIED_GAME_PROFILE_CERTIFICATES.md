# Milestone 83 — complete bounded rational certificates for the tied-edge PSD construction-family spectrum at every facial rank profile

**2026-11-08. PROVED.** This gives a necessary-and-sufficient finite integer/rational description of the exact Hölder exponent and minimal facial rank profile **within the strict tied-edge Shapley-game incidence family** (checkpoints 74, 77, 79), including all its vertex-blown-up forms. Every retained certificate is explicitly realized with matching upper and lower recovery bounds against all ambient PSD competitors. The reverse implication for EVERY arbitrary dense PSD kernel remains unresolved.

## Certificate at rank profile s=(s1,...,sd), nullity nu=sum s_j

For each integer h with 0<=h<=nu-1, consider vertices 0,1,...,h,T=h+1. At each internal vertex i choose **one or two modes** A_i, each containing **one or two** distinct parent edges (a,b) with 0<=a<i<b<=T. Require every individual parent edge to occur in at most one mode across all vertices. An independent optional leading source-to-v edge (0,v) may be included if not among those edges.

Choose for every internal i:
1. one minimizing mode μ_i;
2. one maximizing edge e_i=(a_i,b_i) inside μ_i.

Solve the rational harmonic system
\[
w_0=0,\qquad w_T=1,\qquad 2w_i=w_{a_i}+w_{b_i}.
\]
Retain only solutions satisfying \(0<w_1<\cdots<w_h<1\) and the following exact rational inequalities:

- for every edge \(e=(a,b)\) of the minimizing mode μ_i,
  \[
  (w_a+w_b)/2\le w_i;
  \]
  equality occurs for its selected e_i;
- for every other mode a at i, **at least one** edge e=(u,v) in that mode satisfies
  \[
  (w_u+w_v)/2\ge w_i.
  \]

These are equivalent to the Shapley optimality equation
\(w_i=\min_{\mathrm{mode}}\max_{\mathrm{edge}}(w_a+w_b)/2\); no real optimization remains.

For the exposing schedule, assign t_0=∞,t_T=1, initialize internal t_i=1, and iterate the integer map
\[
t_i\longleftarrow
\max_{a\in A_i}\min_{(u,v)\in a}
\tau(t_u,t_v),\qquad
\tau(p,q)=\begin{cases}p,&p=q,\\\min(p,q)+1,&p\ne q.\end{cases}
\]
The monotone iteration stabilizes and yields the exact canonical exposing times (checkpoint77). Write \(C_j=\{v\ne0:t_v=j\}\), with \(d_G=\max_vt_v\). Retain only \(d_G=d\) and \(|C_j|\le s_j\) for all j.

For the recovery exponent, take:
- \(\alpha=w_1\) without a leading edge when h>=1; OR
- \(\alpha=\min(w_1,w_v/2)\) with an allowed independent edge (0,v).

Equivalently, the candidate \(\alpha\) can be any half-weight \(w_v/2\le w_1\) for an available independent edge; \(w_1\) is itself a half-weight from its primal minimizing mode because its lower parent must be source0. At h=0 there are no internal modes: with **no optional leading edge**, the kernel is {0} and the exponent is **1** (injective recovery); adding the independent leading source-to-terminal edge G gives the usual **square-root exponent 1/2**. Both have degree one, and terminal clones realize arbitrary first-step rank.

Call the resulting finite rational set for the prescribed profile s **T_s**.

## THEOREM: exact incidence-family spectrum and universal sufficiency

For every target rank r>=1 and every positive rank-drop profile s,
\[
\boxed{
T_s=\{\text{sharp full PSD recovery exponents in the strict tied-edge
incidence and vertex-blow-up family with profile }s\}.
}
\]
Every alpha∈T_s is realized by a real finite-dimensional PSD inverse problem on S^(r+nu), with a uniquely determined rank-r target, sharp full-matrix exponent alpha, and **exact canonical minimal facial rank-drop profile s**. In particular T_s is a universally valid CONSTRUCTIVE lower subset of the all-dense spectrum:
\[
\boxed{T_s\subseteq\Sigma_s^{\rm arbitrary\ dense}}.
\]
No dense necessity or full equality is asserted.

### Necessity within the class

Checkpoint79 proves that any finite strict tied-edge incidence system has a subfamily with at most two modes and two edges per mode, retaining the exact Shapley weights and **every** exposing time. Choosing a minimizing mode and maximizing edge supplies the displayed harmonic equations. The remaining inequalities express precisely the finite Shapley fixed point. The dual tropical integer recurrence of checkpoint77 computes its exposing times. Vertex blow-up replaces every original vertex v by a positive number κ_v of clones; the exact profile is the sum of multiplicities in each exposure layer, so the underlying layer cardinality is ≤s_j. The exact exponent is the minimum internal weight or an independent source-edge half-weight by checkpoint74. Thus every incidence-family instance contributes to the certificate set.

### Sufficiency including CLONE MULTIPLICITIES and ambient competitors

Given a certificate, choose positive integers κ_v for every non-source vertex so that
\[
\sum_{v\in C_j}\kappa_v=s_j.
\]
This is possible because every layer is nonempty and \(|C_j|\le s_j\).

Construct an n=1+sum_vκ_v coordinate pencil with target E00. For each internal i and each mode a, include the independent kernel generator
\[
H_{i,a}
 =
\sum_{q=1}^{\kappa_i}E_{(i,q),(i,q)}
 -\kappa_i E_{00}
 +\lambda\sum_{(u,v)\in E_{i,a}}
 F_{(u,1),(v,1)},
\]
where \((v,1)\) is the distinguished representative of a parent vertex and \(F_{ab}=E_{ab}+E_{ba}\); the source has one representative. Add the optional independent leading generator \(\lambda F_{0,(v,1)}\), if used, and choose fixed sufficiently small rational \(\lambda>0\). Let L be the Frobenius orthogonal projection onto K-perp. Because every generator has trace zero and no terminal diagonal coefficient, the trace and terminal diagonal are exactly measured.

**Full ambient upper bound:** Let X≥0 have residual δ, and let Y=E00+P_K(X-E00), E=X−Y. Then ||E||≤δ and Y+δI≥0, while trace control bounds all diagonal coordinates and the terminal diagonal of Y equals zero. Every unique mode-edge entry is λ times its generator coefficient, and each clone diagonal equals the sum of its modes' coefficients. The exact same principal 2×2 inequalities, Shapley-weighted supersolution and maximum principle as checkpoint74 yield diagonal coordinates O(δ^{w_i}), every mode coefficient O(δ^{w_i}) and the optional leading coordinate O(δ^{w_v/2}). All other ambient entries are O(δ), and the source diagonal follows from trace. Thus ||X−X*||≤Cδ^alpha, proving uniqueness.

**Matching full PSD curve:** At every internal i activate only its minimizing mode μ_i at coefficient z^{w_i}, set all other modes zero, terminal diagonal z, optional leading coordinate z^{w_v/2}, and assign all clones the same z^{w_i} diagonal. The Shapley equalities/inequalities ensure that every selected tied edge has parent-average ≤w_i, so after diagonal congruence all nonzero offdiagonals have size at most a constant times λ. For small λ the normalized full n×n matrix is strictly diagonally dominant, hence PD for small z>0. Its residual is Θ(z), while its displacement is Θ(z^alpha). This establishes sharpness.

**Exact facial profile under clone blow-up:** An exposing stress compression S has one dual orthogonality equation per generator,
\[
\sum_{q=1}^{\kappa_i}S_{(i,q),(i,q)}
  +2\lambda\sum_{(u,v)\in E_{i,a}}
  S_{(u,1),(v,1)}=0.
\]
The same AND-over-modes/OR-over-edges closure rule therefore constrains the set of vertex groups with positive exposed diagonals. Conversely, for every greedily exposable group C_j, assign every clone of each v∈C_j a positive diagonal stress \(\eta^{-10^v}\), zero on all others, and for each active mode choose one edge entirely within the exposed group and set its stress entry to minus the clone-diagonal sum divided by 2λ. Inactive modes can use off-face entries. Global edge disjointness makes the equations independent; diagonal normalization suppresses every within-face offdiagonal because its higher parent index exceeds the child. The resulting PSD stress exposes ALL clones of exactly the vertices in C_j. Maximal-rank greedy facial reduction gives precisely s_j at each step. Finally add a fully measured positive support block of dimension r−1 and all new cross entries.

This proves the theorem.

## Finiteness, significance and correct universal frontier

At fixed nu there are at most h≤nu−1 internal vertices. Each internal vertex has at most two modes, each with one or two parent edges selected from the finite list of i(h+1−i) possible pairs. Thus the above certificate search is finite. Each candidate uses one rational linear solve, sign tests of exact rational numbers, and a bounded monotone integer iteration. There is **no SDP solver, real quantifier elimination or search over recovery curves** in the certificate program.

This is a compact purely combinatorial classification for the largest explicitly proven incidence family, strengthening the two-policy rule already REFUTED as universal in checkpoint75. The remaining ambitious full PSD problem is the dense necessity inclusion
\[
\boxed{\Sigma_s^{\rm arbitrary\ dense}\subseteq T_s?}
\]
This is NOT proved. The existing dimension-five tied-edge example shows T_s strictly contains the old two-policy independent-edge list, but does not establish T_s equals the full dense list. The signed/determinantal obstructions in checkpoints63 and65 show why that last implication cannot simply be inferred from support signs. The universal analytic-center/Hessian exact classifier and finite algebraic spectrum enumeration remain fallback general results.

Prior combinatorial stochastic-game algorithms and SDP facial reduction are established techniques; no unchecked publication-priority claim is made.
## Audit correction: h=0 boundary
If h=0, the data consist of one terminal vertex (possibly blown up). With no optional kernel edge, L is injective and alpha=1. If the independent edge (source,terminal) is added, K has one offdiagonal direction, every exact PSD competitor has terminal diagonal zero so uniqueness holds, and the sharp rate is alpha=1/2 from the principal 2x2 minor. The exposing rank profile has one stage, removing all terminal clones. In particular **do not classify the no-edge h=0 pencil as square-root stable**.
