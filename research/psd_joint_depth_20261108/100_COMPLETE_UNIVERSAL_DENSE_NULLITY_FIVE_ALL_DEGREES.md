# Milestone 100 — COMPLETE universal ALL-DEGREE joint PSD exponent classification at target nullity FIVE

**2026-11-08. NEW universally necessary-and-sufficient finite arithmetic classification for every arbitrary DENSE real PSD measurement map with positive target rank and nullity exactly ν=5.** This strictly extends milestone 97 (degree three) to degrees one, two, four and five, closing the entire first unclassified matrix-nullity stratum. NO dense-to-tied-game representation assumption is needed. The proof combines the genuine universal maxdet harmonic valuation chart (89/91), BOTH new primal/dual integer peeling bounds (99), Sturm's universal error bound, and exact constructions from independent-edge systems plus only two small tied-edge examples (75 and 96).

## Main theorem

Fix any positive integer target rank r≥1, and consider all real linear maps \(\mathcal L:\mathbb S^{r+5}\to\mathbb R^m\) having a uniquely recoverable PSD target \(X_*\) of rank exactly r. Let d be the MINIMAL PSD facial-reduction degree and α the EXACT sharp full ambient Frobenius Hölder recovery exponent. Then for every d=1,...,5 the exact attainable exponent set is:

\[
\boxed{\Sigma_{5,1}=\{1,\tfrac12\}.}
\]

\[
\boxed{\begin{aligned}
\Sigma_{5,2}=\{&
1/4,9/32,2/7,7/24,3/10,5/16,9/28,1/3,
11/32,7/20,5/14,3/8,11/28,2/5,13/32,
5/12,3/7,7/16,9/20,11/24,13/28,15/32,1/2
\}.
\end{aligned}}
\]
Exactly **23** values.

\[
\boxed{\begin{aligned}
\Sigma_{5,3}=\{&
1/8,3/22,1/7,3/20,5/32,1/6,5/28,2/11,
3/16,5/26,1/5,5/24,3/14,7/32,2/9,5/22,
3/13,7/30,1/4,7/26,3/11,5/18,9/32,2/7,
7/24,3/10,5/16,7/22,9/28,1/3,11/32,
9/26,7/20,5/14,4/11,11/30,3/8,5/13,
7/18,11/28,2/5,9/22,5/12,11/26,3/7,
13/30,7/16,4/9,5/11,6/13,7/15
\}.
\end{aligned}}
\]
Exactly **51** values (also proved in checkpoint 97).

\[
\boxed{\begin{aligned}
\Sigma_{5,4}=\{&
1/16,1/14,1/13,1/12,1/11,3/32,1/10,
3/28,1/9,3/26,1/8,3/22,1/7,3/20,
2/13,5/32,1/6,5/28,2/11,3/16,1/5,
3/14,7/32,2/9,5/22,3/13,1/4,
3/11,5/18,2/7,7/24,3/10,5/16,1/3,3/8
\}.
\end{aligned}}
\]
Exactly **35** values.

\[
\boxed{
\Sigma_{5,5}=
\{1/32,1/30,1/28,1/26,1/24,1/22,1/20,1/18,
1/16,1/15,1/14,1/13,1/12,1/11,1/10,1/9,1/8,1/7,1/6,1/5\}.
}
\]
Exactly **20** values. This d=ν case also follows from the independently established universal convex-harmonic maximal-depth theorem (90/72).

**Every fraction appears with an explicit finite rational PSD measurement construction and exactly the prescribed singularity degree, at matrix order n=r+5.** No asymptotic dimension increase, coefficient perturbation guess or equivalence to a graph for the arbitrary dense instance is assumed.

## A completely finite, universally NECESSARY arithmetic test

Let \(K=\ker\mathcal L\). The universal fixed maxdet monomial chart and downshift theorem (89 and 91) supply a canonical grade decomposition
\[
\mathbb R^{r+5}=U_0\oplus U_1\oplus\cdots\oplus U_k,\quad
U_0=\operatorname{range}X_*,\quad
0=w_0<w_1<\cdots<w_k=1,\quad k\le5.
\]
Every internal grade is a genuine rational harmonic midpoint
\(2w_i=w_{a(i)}+w_{b(i)}\) with a<i<b, and the sharp exponent is a half-weight \(w_v/2\le w_1\). The central dual flag proves \(d\le k\).

**Universal primal forced-depth lower bound \(L(w)\)** (milestones 54/97): start at j=k, first remove only the terminal grade to reach k−1, and at each later j replace j by the number of indices 1≤i<j with \(2w_i<w_{j+1}\). The number of steps to reach zero is L(w). Pairing ACTUAL positive internal-grade kernel Puiseux coefficients with ANY PSD exposing stress shows no dense problem with these grades can have d<L(w), even when positive grades have multiplicities.

**NEW universal dual truncation UPPER bound \(U(w)\)** (milestone 99): again start at j=k, first reach k−1, and at every later j put
\[
p(j)=\min\{1\le p\le j:2w_p>w_j+w_{p-1}\},\quad j\mapsto p(j)-1.
\]
The steps to zero are U(w). Truncating the actual PSD dual central path \(\epsilon C_\epsilon^{-1}\) through exponent \(1-w_{p(j)}\) excludes all lower-grade rows, then rescaling its finitely many dual coefficients yields a single compressed PSD exposing stress positive on grades p(j),...,j. Hence **EVERY dense instance** satisfies
\[
\boxed{L(w)\le d\le U(w)\le k\le5.}
\tag{100.1}
\]
This is NOT a graph-preservation assumption; both inequalities have direct independent original-kernel proofs.

Sturm additionally gives \(\alpha\ge2^{-d}\), and if d=1 the standard full-stress/tangent criterion gives \(\alpha\in\{1,1/2\}\).

Therefore, for any d=2,3,4,5, a NECESSARY condition for α at nullity5 is the existence of h=k−1∈{d−1,...,4} and strictly increasing rational weights
\[
0=w_0<w_1<\cdots<w_h<w_{h+1}=1
\]
with one harmonic parent pair a_i<i<b_i per internal vertex and
\[
\boxed{L(w)\le d\le U(w),\quad
2^{-d}\le\alpha=w_v/2\le w_1.}
\tag{100.2}
\]

At h internal vertices there are exactly \((h!)^2\) parent assignments (1,4,36,576 for h=1,2,3,4), each yielding a rational linear system. The standalone exact enumerator (checkpoint 101) applies (100.2) to **every one** and returns, degree by degree, exactly the listed 23,51,35,20 fractions. This proves the entire DENSE NECESSITY of every finite list above.

**Key advantage over previous candidate tests:** When d=4, the earlier one-sided forced-depth condition left THIRTEEN seemingly unresolved values. The new independent dual UPPER bound U(w) excludes ALL THIRTEEN, because every possible canonical harmonic weight pattern supporting them has U(w)≤3. Thus the 35-element d=4 necessity is proved without dense-to-game conversion or case-by-case PSD deformations.

## Universal SUFFICIENCY at the same dimension and exact d

Choose one or more independent parent *actions* at each scalar internal vertex of a strict Bellman incidence graph. Each is a distinct globally collision-free edge a<i<b; its associated kernel generator is \(H_{i,a,b}=E_{ii}-E_{00}+\lambda F_{ab}\). Checkpoints 57 and 62 prove exactly:
- global PSD recovery exponent is the minimum controlled harmonic value or an independent source-edge half-weight, with bounds for ALL ambient PSD competitors;
- minimal exposing rank profile is computed by one finite monotone all-actions closure rule, with actual PSD exposing stresses;
- tying cloned diagonal coordinates by the vertex blow-up procedure permits any larger prescribed nullity without changing exponent or minimal exposing degree.

An exhaustive **17,302-instance** collision-free action-system enumeration over h=1,...,4 internal vertices, using exact Fraction Bellman policy improvement and exact exposing closure, supplies:
\[
\begin{array}{c|cccc}
d&2&3&4&5\\\hline
\text{different sharp exponents from independent-edge systems}&23&49&35&20.
\end{array}
\]
Each output has an explicit finite parent-action certificate and an ambient PSD realization. The two degree-three values not covered by the independent-edge systems are:
- α=3/22: exact rational tied-edge 6×6 construction with rank profile (1,3,1), checkpoint75;
- α=3/20: exact rational tied-edge 6×6 construction with rank profile (1,3,1), checkpoint96.

Both have their own fully self-contained global PSD upper bounds, matching strictly PD monomial curves and exact minimal-depth stress proofs. Thus every value from the necessary list is attained at exactly the prescribed nullity and degree. Rank-one targets are padded with a fully measured positive-definite block and all cross entries to achieve any prescribed rank r≥1 without changing ν,d or α. This proves the full theorem. QED.

## Current significance and precise limitation

- **All joint exponent/depth spectra at ν≤5 are now completely classified for arbitrary dense PSD maps**, extending the prior ν≤4 work (checkpoint41). The crucial new mathematical mechanism is the universal **two-sided** primal/dual center-grade integer peeling sandwich (checkpoint99), whose upper bound rules out otherwise plausible nonmaximal-depth candidates.
- At ν=5,d=3 a *tied-edge* generator is essential for two of the realizable exponent values, so one-action or independent-action graph sparsification is NOT a universal requirement. Our proof avoids this false claim.
- **Still open:** Do the universal necessary grade-weight inequalities L(w)≤d≤U(w), together with the full harmonic support certificate and Sturm's lower bound, always suffice at larger nullity? In other words, can every integer depth between the intrinsic primal/dual canonical peeling bounds be realized by finite tied-edge or richer signed games at the same nullity? This is a much sharper remaining **universal combinatorial classification conjecture**, now verified completely through ν=5 but not proved at ν≥6.
- The precise canonical rank-drop profile, as opposed to degree alone, remains a stronger general open refinement: the grade-only L/U recurrences bound step count, not every possible grouped/rotated exposing subspace.
- The completed proofs are internal mathematical research manuscripts with exact checks; independent specialist review and literature priority audit are necessary before claiming publication-level novelty.
