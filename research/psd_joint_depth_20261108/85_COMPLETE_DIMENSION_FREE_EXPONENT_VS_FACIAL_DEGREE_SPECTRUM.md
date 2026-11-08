# Milestone 85 — COMPLETE UNIVERSAL spectrum of sharp PSD recovery exponents at each prescribed singularity degree, with MATRIX DIMENSION UNRESTRICTED

**2026-11-08. PROVED for ALL arbitrary real finite-dimensional PSD linear inverse problems with a uniquely determined positive-rank PSD target.** This is a fully explicit necessary-and-sufficient arithmetic classification of the exponent versus exact *minimal facial-reduction degree*, with no restriction on matrix dimension. It combines the dimension-free sharp lower error bound, the directly proved high-depth strict square-root gap, and a constructive degree-preserving gluing principle. This **does not** complete the more ambitious fixed-(n,r,d) or fixed-rank-profile spectrum.

## Main theorem (complete dimension-unrestricted exponent/degree spectrum)

Fix any positive target rank r>=1 and any integer exact minimal facial-reduction degree d>=1. Allow the matrix order n>=r+1 and number of measurements to vary freely, with finite n. Then the set \(\Sigma^{\rm unbounded\ dimension}_{r,d}\) of all optimal full-matrix PSD recovery Hölder exponents is EXACTLY
\[
\boxed{
\begin{array}{c|l}
d&\Sigma_{r,d}^{\rm unbounded\ dimension}\\ \hline
1&\{1,\ 1/2\}\\[1mm]
2&\mathbb Q\cap[1/4,\,1/2]\\[1mm]
d\ge3&\mathbb Q\cap[2^{-d},\,1/2)
\end{array}}
\tag{1}
\]
Every value in (1) is attained by an explicit finite-dimensional *rational* linear PSD measurement map with target rank exactly r and minimal singularity degree **exactly d**, with a matching feasible positive-definite arc and a proven recovery upper bound against ALL ambient PSD competitors.

Thus **the singularity degree alone completely determines the universe of possible sharp exponents when dimension is unrestricted**. The only universal gap at high depth is the forbidden endpoint 1/2.

## Necessity

Unique PSD recovery yields positive-definite trace control, compact residual sublevels and a positive rational sharp exponent by standard semialgebraic curve selection and growth theory. The first-order PSD tangent criterion gives \(\alpha=1\) or \(0<\alpha\le1/2\); if \(\alpha=1\), the minimal facial degree is one (full-null exposing stress).

At exact degree \(d\), Sturm's classical SDP error bound gives
\[
\alpha\ge2^{-d}
\]
for bounded competitors. If d=1, the upper bound \(\omega(\delta)=O(\sqrt\delta)\) follows directly from the globally PSD full-null exposing stress, giving only \(\alpha=1/2\) or \(\alpha=1\). If d=2, the two inequalities imply \(\alpha\in[1/4,1/2]\).

For EVERY d>=3, the independently proved dense-kernel high-depth theorem (checkpoint 44; strengthened in checkpoint 45) constructs a positive-definite arc in the ORIGINAL kernel with exponent strictly below 1/2, hence
\[
\alpha<1/2.
\]
Its proof uses only the first two maximal exposing stresses, a finite homogeneous Gordan–Stiemke alternative and fully rigorous PSD coefficient balancing. No weighted-flag extraction or sparse normal form is assumed. These facts prove necessity of (1).

## Sufficiency I — a finite rational *base* network for any alpha>=2^{-d}

Fix any rational \(0<\alpha<1/2\). Choose the *natural depth*
\[
e=\left\lceil\log_2(1/\alpha)\right\rceil\ge2,
\quad 2^{-e}\le\alpha<2^{-(e-1)}.
\]
Let \(c=2^{-(e-1)}\). Since \(c\le2\alpha<2c\le1\), write uniquely
\[
\frac{2\alpha-c}{1-c}=\frac{a}{b}
\]
in lowest terms with \(0\le a<b\). (If e=2 then c=1/2 and the same formula is valid.) Build one source vertex O of weight 0, one terminal T of weight 1, and the DYADIC SPINE internal vertices of weights \(1/2,1/4,\ldots,c\). Each spine vertex of weight \(2^{-j}\) has parent pair \((O,2^{-(j-1)})\), with the terminal as parent at j=1. Add the AFFINE GRID vertices of weights
\[
c+\frac{k(1-c)}b,\qquad k=1,\ldots,b-1,
\]
except for any vertices already coinciding with the spine; assign to each new grid vertex its two nearest neighbors in the affine grid from c to 1. Every internal vertex has EXACT midpoint relation \(2w_i=w_{a(i)}+w_{b(i)}\), and the parent edges are distinct. The point \(2\alpha\) is one of the grid points or c.

All positive internal weights are at least c>=alpha. If \(\alpha<c\), add an independent leading source-to-vertex edge \((O,2\alpha)\); it has half-weight alpha, is not occupied by a parent edge, and yields the desired leading full-matrix exponent. If \(\alpha=c\), the diagonal variable on the spine vertex of weight c itself supplies the leading order, and no optional edge is required.

Use the standard rational weak-offdiagonal PSD incidence pencil, measure trace, terminal diagonal, and orthogonal projection away from its linear pencil range, with X*=E_OO. The principal 2x2 inequalities for ALL ambient PSD competitors give \(\omega(\delta)=O(\delta^\alpha)\) via the rational harmonic maximum principle; normalized monomial coordinates yield a matching strictly PD curve of residual order one and displacement order alpha. Thus the sharp exponent is alpha and X* is unique.

**Exact facial degree of the base:** its maximal-rank greedy exposing stages remove terminal at stage one, then successively lower dyadic spine vertices at stages 2,3,...,e, with every affine-grid vertex removable by the time the smallest spine vertex is removed. The spine's source-parent dependency prevents any earlier exposure of the next spine vertex. The exact minimal degree is \(e\). A direct proof follows from the all-actions exposing closure and the sparse stress existence theorem; no claim about dense-to-graph necessity is needed.

For \(\alpha\ge2^{-d}\), the natural depth e satisfies e<=d.

## Sufficiency II — arbitrarily high prescribed depth with exponent arbitrarily close to 1/2

Fix d>=3. For any positive integer M, use the proven explicit layered harmonic PSD pencil of checkpoint 45 with canonical exposing rank profile
\[
(s_1,\ldots,s_d)=(1,\underbrace{1,\ldots,1}_{d-3\text{ entries}},M,1).
\]
Its exact singularity degree is d and its sharp exponent, by the explicit rational profile formula, is
\[
\boxed{
b_{d,M}=\frac{2^M-1}{\,2(2^M-1)+(d-2)\,}.
}
\tag{2}
\]
This is rational, strictly below 1/2, and increases to 1/2 as M→∞. The network and its full-PSD recovery bounds are constructed in checkpoint 45; in particular this is NOT merely a limiting assertion with infinite matrix dimension — every M gives a finite rational pencil.

For any prescribed rational \(\alpha<1/2\), choose a **finite** integer M large enough that \(b_{d,M}>\alpha\). Such an M exists because b_(d,M)↑1/2.

## Sufficiency III — SOURCE GLUING preserves the min exponent and the max degree

Take the base harmonic graph of Part I (exact exponent alpha, degree e<=d), and, if e<d, a distinct depth-d helper graph from Part II with exponent b_(d,M)>alpha. Identify ONLY their source vertices O; keep all non-source vertices, terminals and parent-edge variables disjoint and measure EACH terminal diagonal.

The combined kernel is the span of the individual graph generators, each with a source E_OO term but disjoint non-source diagonal and parent-edge supports. The trace measurement remains valid because every generator is trace zero. Every ambient PSD competitor is controlled separately by the two independent systems' principal 2x2 inequalities and measured terminals, while off-pattern and intercomponent entries are O(delta) by projection. Therefore its exact global exponent is the minimum of the component exponents:
\[
\alpha_{\rm glued}=\min(\alpha,b_{d,M})=\alpha.
\]
A matching positive-definite arc activates only the base component's monomial variables, while terminal diagonals in the helper component may be chosen of order one (relative to the residual parameter) with matching harmonic coordinates to make the full normalized matrix strictly diagonally dominant. Equivalently, use the base monomial arc and the helper monomial arc with the same residual parameter, and choose sufficiently small common rational lambda. The base component contributes displacement Theta(delta^alpha), and both terminals contribute residual O(delta). Thus the global rate is exactly alpha.

The sparse canonical greedy exposing closure works componentwise for two graphs that share only the source: each action edge belongs to exactly one component; a closed exposable vertex set is the union of its componentwise closed subsets. Therefore the combined minimal facial degree is exactly
\[
d_{\rm glued}=\max(e,d)=d,
\]
with the second component ensuring depth d. This is independent of the amplitude of either monomial curve.

If e=d, use the base graph alone. This proves sufficiency for ALL rational \(2^{-d}\le\alpha<1/2\) at every d>=3. For d=2, the base graph already realizes every rational in [1/4,1/2), and the alpha=1/2 endpoint is realized by the two-step network with one internal weight 1/2 and independent source-to-terminal leading edge. For d=1, take a fully measured singular PSD target (alpha=1, degree one) or retain an invisible source-to-null offdiagonal coefficient while measuring the null diagonal (alpha=1/2, degree one).

All constructions have target rank one. Adjoining a fully observed positive-definite block and measuring every added cross entry raises the rank to arbitrary prescribed r without changing target nullity, exponent or facial degree. This completes the classification (1). QED.

## Finite dimension bound (explicit, not optimal)

The base construction uses at most \(e+b-1\) null dimensions (e-1 spine vertices, at most b-1 grid vertices, one terminal). The depth-d helper uses M+d−1 null dimensions. If e<d, the glued construction therefore uses
\[
\nu\le e+b+M+d-2
\]
null dimensions (take the sum of both bounds). The helper M can be chosen as any integer satisfying
\[
2^M-1>\frac{\alpha(d-2)}{1-2\alpha}.
\]
This gives a fully explicit computable dimension bound for every prescribed (alpha,d), although it is not claimed optimal.

## What remains open

This is a **complete unrestricted-dimension exponent-versus-degree spectrum**, genuinely universal on the necessity side because it uses Sturm and the direct dense-kernel strict endpoint theorem. The more ambitious fixed-(n,r,d) spectrum, exact optimal dimension as a function of arbitrary alpha/d, and full equivalence with any compact tied-edge/Shapley-game normal form remain open. Do NOT conflate the proven projection (alpha,d) with the unsolved full four-way relation (n,r,d,alpha).

The use of Sturm error bounds, semialgebraic rationality, and sparse harmonic SDP gadgets has significant prior literature. The combined exact dimension-unrestricted degree spectrum is proved here, but bibliographic priority/novelty should be audited separately.