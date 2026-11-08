# Milestone 47 — COMPLETE closed rational spectrum for every PSD degree-two facial rank profile

**2026-11-08. Universal necessary-and-sufficient arithmetic classification at fixed exposed ranks (s1,s2), all target ranks and all dense measurement maps.** The necessity uses the project's previously established dense sharp weighted-flag/mediated-set extraction (load-bearing); the sufficiency is an explicit full ambient sparse PSD construction whose exact first and second exposing ranks are prescribed.

## Theorem

Fix r>=1, s1>=1, s2>=1 and n=r+s1+s2. Let Σ_(s1,s2) be the set of sharp full-state Hölder exponents of uniquely solvable real PSD inverse problems of target rank r whose **canonical minimal facial reduction has degree exactly two and rank-drop profile (s1,s2)**. Then
\[
\boxed{
\Sigma_{(s_1,s_2)}
=\left\{\frac ab\in\mathbb Q:
\gcd(a,b)=1,\quad \frac14\le\frac ab\le\frac12,\quad
\frac{b}{\gcd(b,4)}\le2^{s_2-1}
\right\}.
}
\]
The profile's first rank drop s1 affects only the total nullity, while the arithmetic denominator bound depends *only on the number of directions removed by the second step*.

## Necessity

The universal degree-two PSD facial-reduction estimate gives sharp exponent α≥1/4; Lipschitz stability implies degree one, so α≤1/2. Let S be a sharp mediated set extracted from the actual dense problem by the weighted-flag theorem. Since the first canonical exposing stress has rank s1, the first-stress alignment lemma forces its range inside the highest-order (weight-one) null valuation block. Hence the number h of internal distinct harmonic levels satisfies h≤(s1+s2)-s1=s2.

The degree-two diagonal bound forces all internal harmonic weights to be ≥1/2. Every nonempty mediated set in [1/2,1) has minimum **exactly 1/2**: its least internal point w has one parent zero (no smaller positive internal point), and 2w≤1. Remove 1/2 and transform any remaining internal weight u by v=2u-1. The transformed set T⊂(0,1) is mediated with endpoint weights 0 and 1, and |T|≤s2-1. The sharp leading relation 2α∈S∪{1} implies t=4α-1∈T∪{0,1}.

If α=a/b in lowest terms, the reduced denominator of t=(4a-b)/b is q=b/gcd(b,4). For a mediated set of size |T|, the integer midpoint matrix has determinant at most 2^{|T|}, and Cramer's rule shows every rational point's denominator divides its determinant. Thus q≤2^{|T|}≤2^{s2-1}. This gives the necessary bound. At α=1/2, t=1 and q=1, so the same conclusion holds.

## Sufficiency with exactly prescribed exposing ranks

Let α be any rational satisfying the conditions, and put t=4α-1∈[0,1]. By ordinary minimum mediated-set theory, there is a mediated set T with at most ceil(log2 q)≤s2-1 points containing t whenever t∈(0,1), and T=∅ at endpoints. Apply the affine map u=(1+v)/2 to T, and include the point 1/2. This produces a mediated set S⊂[1/2,1) containing 2α if α<1/2, with 1+|T|≤s2 internal points. For α=1/2, choose S={1/2}, so 2α=1 is terminal.

If |S|<s2, append a sequence of new harmonic internal weights above the previous maximum: repeatedly add u_new=(u_max+1)/2 with parent pair (u_max,1). This does not change the minimum weight, the distinguished doubled weight 2α, or the exponent. It yields *exactly s2* internal vertices. Every parent edge is distinct, so the standard sparse full-matrix PSD pencil is well defined.

In this network, after the terminal is exposed, all internal vertices can be exposed simultaneously (for every internal midpoint relation either the higher parent is the terminal or, when both parents remain internal, the entire internal set is included in the exposing support). At the first step, no internal vertex can be exposed because any attempted exposure would force the decreasing-parent chain to the unexposed source. Therefore the **exact** sparse exposing rank profile is (1,s2). Add s1-1 fully measured independent null coordinates; their PSD stresses join the first step, giving precisely (s1,s2) without changing the full recovery exponent. To achieve prescribed target rank r, add a fully measured positive-definite (r-1)×(r-1) block and all cross entries.

The upper recovery bound against every ambient PSD competitor follows from the exact harmonic logarithmic inequality and residual projection estimate; the monomial coordinate curve is positive definite after diagonal normalization and trace normalization, providing matching lower bounds. Thus every listed α is attained with the exact prescribed profile, proving sufficiency.

## Examples

- For s2=1, the condition q≤1 gives α∈{1/4,1/3,1/2} within [1/4,1/2]? **Caution:** q=1 means b divides 4, so only α=1/4 or 1/2; 1/3 has q=3 and is excluded. Therefore Σ_(s1,1)={1/4,1/2}.
- For s2=2, q≤2 gives {1/4,3/8,1/2}.
- For s2=3, q≤4 gives {1/4,5/16,1/3,3/8,5/12,7/16,1/2}.
These agree with the project’s established nullity-three and nullity-four degree-two classifications.

## Boundaries

This is a **complete profile-specific arithmetic spectrum for d=2**. The analogous full rational spectrum for d>=3 remains unresolved, although milestone 45 supplies the exact maximum at every profile. The dense weighted-flag extraction is a load-bearing prior project theorem for this classification and warrants independent specialist review. No priority claim is made for ordinary mediated-set constructions, semialgebraic rationality, or facial reduction.