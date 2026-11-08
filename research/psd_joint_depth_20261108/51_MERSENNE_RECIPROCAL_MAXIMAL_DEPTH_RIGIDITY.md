# Milestone 51 — universal Mersenne reciprocal exponents force maximal PSD facial depth

**2026-11-08. Theorem proved conditional on the project's previously established dense sharp weighted-flag → harmonic-midpoint extraction theorem.** The new determinant extremal combinatorics, uniqueness of the sharp mediated graph, and dense primal–dual forcing are proved below. No sparse depth-preservation hypothesis is used.

## Theorem

Let ν≥3 and q=2^(ν−1)−1. If an arbitrary real PSD inverse problem uniquely determines a target of positive rank r and nullity ν, with exact sharp full-matrix recovery exponent
    α=1/q,
then its **minimal facial-reduction degree is exactly d=ν**.

The converse is constructive: for every ν≥3 and r≥1 an explicit sparse midpoint PSD pencil with nullity ν and exact degree ν realizes α=1/q. This supplies an infinite series of **universal exact exponent→depth rigidity statements** in every nullity, beyond previously classified ν≤4.

For ν=3,4,5,6 the rigid exponents are respectively 1/3, 1/7, 1/15, 1/31.

## Proof I: the determinant has exactly one cyclic functional assignment

The dense sharp weighted-flag extraction provides h≤ν−1 internal positive harmonic levels S, with the strictly ordered values w_i∈(0,1), endpoints 0 and 1, satisfying each 2w_i=w_{a(i)}+w_{b(i)} with a(i)<i<b(i), and **2α∈S∪{1}**. Every internal distinct valuation level has positive null multiplicity. The h×h reduced integer midpoint matrix M has row 2e_i−e_{a(i)}−e_{b(i)}, suppressing boundary columns.

Let q=2^(ν−1)−1 be odd. Since 2α=2/q has reduced denominator q, Cramer's rule gives q|det M (if 2α is terminal this is impossible for q≥3). By row expansion of each 2e_i−e_a−e_b as (e_i−e_a)+(e_i−e_b), det M equals the number of parent-choice functions on the h internal nodes whose functional directed graph has **no internal directed cycle**. Every acyclic choice contributes +1 and every cyclic choice contributes 0. Therefore
    q ≤ det M ≤ 2^h ≤ 2^(ν−1)=q+1.
Because q≥3 and det M is a multiple of q, det M=q. Thus h=ν−1 and exactly one of the 2^h parent-choice functions is cyclic.

The directed parent graph must contain a directed cycle C. If it contained a cycle on k<h internal vertices, then the other h−k parent choices could be selected arbitrarily, creating at least 2^(h−k)≥2 cyclic functions, contradiction. Hence **every directed cycle must use all h vertices**. There is exactly one h-cycle: if two distinct cyclic assignments existed we would contradict the count. Let σ be its successor permutation. The other parent of each vertex cannot be another internal vertex u ≠σ(v), because the edge v→u followed by the unique cycle path u→...→v would make a shorter internal cycle. Consequently each vertex has precisely two successors: its cycle successor σ(v) and a boundary successor b(v)∈{0,terminal 1}.

The midpoint equation becomes
    2w_v=w_(σ(v))+b(v).
Since 0<w_(σ(v))<1, b(v)=floor(2w_v), and w_(σ(v))={2w_v}, the fractional part of 2w_v. Thus the h weights constitute one periodic orbit of the doubling map modulo 1.

One vertex has weight 2/q. Since 2^h=q+1, its orbit is exactly
    {1/q,2/q,4/q,...,2^(h−1)/q}.
These are strictly increasing as written. Hence the **unique sharp harmonic graph** has weights
    w_i=2^(i−1)/q, i=1,...,h,
and parent pairs
    (0,i+1) for i<h; and (1,h+1) for i=h,
where the latter means the smallest vertex 1 and terminal h+1. (All vertices except i=h have w_i<1/2 and boundary successor 0; the highest has w_h>1/2 and boundary successor terminal.)

Since h=ν−1, every internal valuation block and the terminal valuation block has exactly one null dimension.

## Proof II: actual dense kernel coefficients force every exposing step to have rank one

Let U=range X*, and write an orthogonal sharp null valuation basis e_1,...,e_h,e_ν with weights w_1,...,w_h,1 respectively. For each i≤h, the **actual** Puiseux kernel coefficient H_i∈K=ker L at exponent w_i has positive diagonal entry (H_i)_(i,i)>0 and obeys the PSD support-order restriction
    (H_i)_(j,k)=0 whenever w_j+w_k>2w_i,
where w_0=0 on U and w_ν=1. Because w_(i+1)=2w_i for i<h and 2w_h<1,
**every null-null block of H_i with either index>i vanishes**: the smallest null weight w_1>0, and w_(i+1)+w_1>2w_i. Its support-to-U entries may reach e_(i+1), but never further; this is harmless in the compressed stress pairing.

Let Z_1∈K^⊥∩PSD be any nonzero first exposing stress, <Z_1,X*>=0. From its PSD positivity and measurement orthogonality,
    tr(Z_1 X(t))=O(t^Q)
on the sharp arc (after normalizing its residual order Q=1). Because the diagonal leading coefficients on each valuation block are PD and weights strictly increase, every vector in range Z_1 must lie in the terminal weight-one block. That block is one-dimensional, so the *first* facial step removes exactly e_ν.

Inductively suppose the first ν−j steps have removed e_ν,...,e_(j+1), leaving the coordinate face
    W_j=U⊕span(e_1,...,e_j).
For each i<j, the matrix H_i is supported inside W_j: it has no null-null entries past i, no U-to-null entries past i+1, and no entries on the previously removed faces. Hence H_i∈K∩S(W_j).

Let S=P_Wj Z P_Wj≽0 be ANY valid exposing stress on that face. It annihilates U. Orthogonality to H_i gives <S,H_i>=0 for i=1,...,j−1. For i=1 this is
    0=(H_1)11 S11,
so S11=0, and PSD kills the entire e1 row/column. Assuming rows 1,...,i−1 vanish, the support restriction on H_i gives
    0=<S,H_i>=(H_i)ii Sii,
hence Sii=0 and its row also vanishes. After i=j−1, S is supported solely on e_j. Every nonzero exposing stress thus removes at most one dimension. Since the target has unique feasible PSD fibre, facial reduction supplies a nonzero exposing stress at every proper remaining face, and the process must require exactly ν steps.

This argument invokes NO dense-to-sparse depth-preserving conversion; the actual kernel Puiseux matrices H_i supply the constraints. The upper bound d≤ν is automatic, so d=ν. QED.

## Sharp construction and exact arithmetic audit

The unique harmonic cycle weights w_i=2^(i−1)/q and parent pairs above generate the standard weak-offdiagonal rank-one PSD pencil with trace, terminal and off-pencil measurements. Its full-state sharp exponent is the smallest internal weight 1/q by PSD quadratic minor upper bounds and a matching monomial PD arc; its greedy peel removes terminal then every internal vertex singly. Fully measured positive rank padding yields any r≥1.

An exhaustive Fraction check of all strict harmonic graphs through h=5 showed that **exactly one** graph realizes α=1/(2^h−1) at h internal levels, agreeing with the algebraic cycle proof; the proof itself applies for every h.

## Important scope and prior attribution

This theorem depends on the earlier full dense weighted-flag/midpoint-extraction statement. Its determinant cycle argument and conic stress pairing are proved directly. It does not establish that every other nonreciprocal sharp exponent at maximal depth is excluded, nor that every dense sharp flag has a depth-preserving sparse representation. The exact high-dimensional joint spectrum remains open.

Combinatorial functional graph determinant expansions, mediated graphs, and PSD facial reduction have prior literatures; bibliographic novelty and review of the load-bearing dense flag theorem remain essential.
