# First precise remaining dense maximal-depth compatibility tests: (nu,d)=(4,4)

2026-11-07. This checkpoint isolates **exactly two** unresolved fractions at the first nullity beyond the fully classified dense case nu=3. It is a logically exhaustive reduction using previously established results, **not a proof of their impossibility**.

## Theorem (finite two-fraction reduction)

Fix any target rank r>=1 and nullity nu=4, minimal facial-reduction degree d=4. The universal sharp recovery exponent spectrum has the form
\[
\Sigma^{dense}_{4,4}=
\left\{\frac14,\frac15,\frac16,\frac17,\frac18,
\frac1{10},\frac1{12},\frac1{14},\frac1{16}\right\}
\cup T,
\qquad T\subseteq\left\{\frac3{16},\frac3{14}\right\}.
\]
Every displayed reciprocal exponent is attained at matrix order n=r+4, exact degree4, by the **universal dense reciprocal if-and-only-if theorem** (checkpoint 26). No further sharp exponent is possible, conditional only on the previously proved *unconditional* fixed-nullity-four exponent catalogue (finite weighted-flag/midpoint classification) and the new universal dense maximal-depth bound alpha<=1/4 (checkpoint 22).

**Proof:** The complete unconditional nullity-four non-Lipschitz exponent catalogue, extracted by all h<=3 mediated weight networks, is
    {1/16,1/14,1/12,1/10,1/8,1/7,1/6,3/16,1/5,
     3/14,1/4,3/10,5/16,1/3,5/14,3/8,2/5,
     5/12,3/7,7/16,1/2}.
The universal dense d=nu=4 bound alpha<=1/4 excludes every entry larger than 1/4. The surviving entries are the nine reciprocals explicitly realized in checkpoint 26 and the two nonreciprocals 3/16 and 3/14. QED.

## All possible sharp mediated networks for the two unresolved candidates

Exact rational enumeration of the *sharp* weight conditions shows:

**alpha=3/16** (2alpha=3/8):
1. weights (3/8,1/2,3/4), parent pairs (0,3),(0,4),(2,4); sparse peeling degree=3.
2. weights (1/4,3/8,1/2), parent pairs (0,3),(1,3),(0,4); sparse peeling degree=3.

**alpha=3/14** (2alpha=3/7):
1. weights (3/7,5/7,6/7), parent pairs (0,3),(1,4),(2,4); sparse peeling degree=3.

Here vertices are (0,1,2,3,4), with 0 source, 4 terminal and ascending internal weights. These are exhaustive harmonic-support **candidate normal forms** for sharp exponent at nullity4; the preceding unconditional weighted-flag theorem says every dense sharp exponent produces at least one such scalar network. Each candidate's *sparse* realization has minimal degree3. However this **does not prove** dense realizations of the same exponent cannot have degree4: the missing implication is precisely depth preservation under harmonic extraction.

## Why these two cases are decisive

- If neither fraction occurs at degree4, the entire universal dense maximal-depth spectrum at nu4 is exactly the reciprocal set, agreeing with sparse peeling.
- If either fraction occurs for some arbitrary dense kernel with degree4, sparse midpoint-network depth alone is NOT a universal joint compatibility invariant.
- Both fractions satisfy the current universal necessary constraints (degree bound, terminal stress rank, denominator bound and dyadic stress-filtration rank profile in some admissible configuration). Those tools do not by themselves resolve them.

## Next mathematical experiments

A feasible route to a rigorous answer would combine:
(a) the canonical maximal-rank dual stress flags (checkpoint 25);
(b) the finite sharp weight lists above;
(c) existence of mandatory primal kernel modes from maximal-degree dual separation (checkpoint 22);
(d) a proof that simultaneous occurrence of (a)–(c) either creates a strictly worse feasible PSD arc (hence the proposed sharp alpha is false) or yields a shorter exposing chain (hence d<4).

Such an argument would be a genuinely nontrivial dense-to-midpoint compatibility theorem in the first unresolved case. The current packet **does not** assert that it has been obtained.

## Reproducibility
The exact Fraction enumerators in the earlier research packet produced the exhaustive lists and parent networks. Independent direct symbolic checks of each midpoint equation hold. No numeric tolerance is used in this reduction.