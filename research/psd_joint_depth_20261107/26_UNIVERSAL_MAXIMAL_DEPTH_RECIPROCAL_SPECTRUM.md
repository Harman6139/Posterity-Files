# Full **universal dense** reciprocal exponent spectrum at maximal PSD facial depth

2026-11-07 — NEW if-and-only-if arithmetic classification, valid for **all arbitrary dense PSD measurement maps** rather than solely midpoint networks. It combines (i) universal maximal-depth instability α<=1/nu (checkpoint 22), (ii) universal sharp-exponent denominator obstruction (checkpoint 23 / earlier dense weighted-flag theorem), and (iii) explicit sparse realizations attaining all permitted reciprocal denominators (checkpoint 17).

## Theorem

Fix positive target rank r≥1 and nullity nu≥2; impose **minimal facial-reduction degree d=nu**. A sharp Hölder exponent alpha of the form 1/q, q a positive integer, is attainable by some finite-dimensional real PSD inverse problem of target rank r, matrix order n=r+nu and minimal degree exactly nu if and only if
\[
\boxed{
q\ge\nu\quad\text{and}\quad
\frac{q}{\gcd(q,2)}\le2^{\nu-1}.
}
\tag{1}
\]
Equivalently, the EXACT universal maximal-depth **reciprocal** spectrum is
\[
\boxed{
\bigl\{1/q:\nu\le q\le2^{\nu-1},\ q\in\mathbb Z\bigr\}
\ \cup\
\bigl\{1/q:2^{\nu-1}<q\le2^\nu,\ q\ {\rm even}\bigr\}.
}
\tag{2}
\]
Every allowed exponent is realized by an explicit rank-one PSD sparse midpoint pencil, followed by a fully observed positive-definite block when r>1. Hence the necessary conditions are also sufficient **across all dense kernels**.

This characterizes *all* maximal-degree reciprocal exponents, but does not exclude nonreciprocal fractions at the same (nu,d).

## Complete proof

**Necessity.** The new universal dense maximal-depth theorem (checkpoint 22) proves α<=1/nu, so α=1/q requires q>=nu. Independently, the dense weighted-flag/midpoint denominator theorem (checkpoint 23, with first stress rank s1=1 because d=nu removes exactly one direction at each step) states
   denominator(2alpha)<=2^(nu-1).
For alpha=1/q this reduced denominator is q/gcd(q,2), yielding (1). The dyadic Sturm lower bound is consistent with and subsumed by q<=2^nu here.

**Sufficiency.** If nu<=q<=2^(nu-1), invoke the explicit maximal-depth sparse construction of checkpoint 17 with parameter Q=q and choose its diagonal-leading sharp exponent 1/Q=1/q.

If q>2^(nu-1), condition (1) forces q even and q<=2^nu. Put Q=q/2. Then Q<=2^(nu-1) and Q>=nu, because:
- for nu=2, q>=4 implies Q>=2;
- for nu=3, q>=6 implies Q>=3;
- for nu>=4, q>2^(nu-1) and q even give Q>=2^(nu-2)+1>=nu.
Thus Q lies in the valid interval [nu,2^(nu-1)] of checkpoint 17. Use its *offdiagonal-leading* sharp exponent 1/(2Q)=1/q. That construction has target rank 1, nullity nu and **exact minimal degree nu**, with a matching feasible sharp arc and a universal recovery upper bound against every ambient PSD competitor. Appending a fully observed positive block raises target rank to any r without changing nu, d or alpha. QED.

## Concrete spectra (reciprocal portion)

- nu=2, d=2: {1/2,1/4}; COMPLETE spectrum in this nullity.
- nu=3, d=3: {1/3,1/4,1/6,1/8}; COMPLETE spectrum by dense checkpoint 20.
- nu=4, d=4: {1/4,1/5,1/6,1/7,1/8,1/10,1/12,1/14,1/16}. The *only* other values not excluded by the previously established unconditional nu=4 sharp-exponent catalogue and alpha<=1/4 are **3/16 and 3/14**. Whether either occurs at dense maximal degree 4 remains unresolved.
- nu=5, d=5: all 1/q for 5<=q<=16, and all even q with 16<q<=32.
- general nu: formula (2).

## Consequence: sharp optimal dimension for reciprocal alpha under the maximal-degree constraint

For a prescribed q, the possible maximal depth/nullity nu (for some r>=1) satisfy exactly (1). Thus the **least matrix order at rank r under the constraint d=nu** realizing alpha=1/q is
    n=r+min{nu>=2:nu<=q and q/gcd(q,2)<=2^(nu-1)}.
The set is nonempty for every q>=2: choose nu=ceil(log2(q/gcd(q,2)))+1, adjusting to nu>=2, and check nu<=q. This is the exact universal optimum for reciprocal exponents within maximal-depth realizations; it is not a formula for the minimum dimension when d<nu is prescribed.

## Audit, literature and remaining frontier

The new mathematical point is the **match of all universal necessary conditions with explicit maximal-depth constructions** for the reciprocal subclass; no unproved dense/sparse equivalence is needed. The determinant bound relies on the previously proved dense weighted-flag result, and Sturm's bound and facial reduction are established literature. A closed full dense spectrum at nu>=4 remains open **only for nonreciprocal candidates**: already at nu=4 the unresolved maximal-depth fractions are 3/16 and 3/14. No assertion is made that these are impossible without proof.