# Milestone 41 — complete joint exponent × facial-degree classification for ALL dense PSD problems at target nullity four

**2026-11-08. NEW result.** The *sharp upper endpoint* at degree three is proved directly from facial reduction and Gordan–Stiemke alternatives, without sparse reduction or the weighted-flag theorem. The exact finite lists require the independently established nullity-four dense weighted-flag/midpoint extraction and certified sparse constructive catalogues. This distinction is explicit.

Let rank X*=r>=1, nullity ν=n-r=4, and d be the minimal PSD facial-reduction degree. Then:
\[
\boxed{\begin{array}{c|l}
d &\text{exact sharp exponent set } \Sigma_{4,d}\\
1&\{1,\,1/2\}\\
2&\{1/4,\,5/16,\,1/3,\,3/8,\,5/12,\,7/16,\,1/2\}\\
3&\{1/8,\,1/6,\,3/16,\,1/5,\,3/14,\,1/4,\,3/10,\,1/3,\,5/14,\,3/8,\,2/5,\,3/7\}\\
4&\{1/4,\,1/5,\,1/6,\,1/7,\,1/8,\,1/10,\,1/12,\,1/14,\,1/16\}.
\end{array}}
\]

## Direct universal exclusion of square root at ν4,d3

There are exactly three possible positive rank-drop profiles of length three summing to nullity four:
(2,1,1), (1,1,2), and (1,2,1). The newly proved *independent dense* theorems are:
- checkpoint 38: (2,1,1) implies α≤1/3; construct tA+t²B+t³P_F, with Gordan–Stiemke providing the clean B.
- checkpoint 39: (1,1,2) implies α≤2/5; construct t²A+t³H+t⁴B+t⁵P_F using two cone alternatives.
- checkpoint 40: (1,2,1) implies α≤3/7; construct t³A+t⁵B+t⁶C+t⁷P_F or t³A+t⁵B+t⁷P_F, according to rank of a PSD projected kernel direction.

Each polynomial is made *fully positive definite* by the explicit block coefficient-rescaling lemma; all coefficients below the last residual order lie in K. Thus for EVERY dense nullity-four depth-three problem,
\[
\boxed{\alpha\le3/7<1/2,}
\]
and the value 3/7 is attained by an exact sparse construction with rank profile (1,2,1). This is a sharp universal dense endpoint theorem and completely resolves the prior question whether square-root stability can coexist with degree three **at nullity four**.

## Exhaustiveness of the arithmetic sets

For d=1, standard first-order tangent and full-stress arguments give only {1,1/2}. For d=2, the already established dense degree-two theorem gives exactly the displayed seven values. For d=4, checkpoint 31 rules out the only potential nonreciprocal candidates 3/16,3/14, and checkpoint 26 constructs all nine remaining reciprocals.

For d=3, the unconditional fixed-nullity-four weighted-flag/midpoint classification supplies a 22-element rational candidate set. Sturm's lower bound d=3 excludes exponents <1/8; checkpoint 35 proves α=1/7 forces d=4; checkpoint 33 proves 5/16,5/12,7/16 require d=2; Lipschitz α=1 forces d=1; and the new independent endpoint theorem excludes α=1/2. Every remaining candidate is one of the twelve listed above and is realized by an exactly verified sparse midpoint-network construction with d=3. Thus equality holds.

Positive-rank padding and fully measured null padding preserve sharp exponents and minimal facial-reduction degree as established in the base memorandum, so the result applies to every prescribed positive target rank r.

## Scope and next frontier

This is now the **full universal dense fixed-nullity joint classification through ν=4**. It does NOT prove a closed arithmetic or combinatorial formula for every ν≥5 and all d. The unresolved general square-root endpoint d≥3 at larger nullity remains open; it is not inferred from the ν4 theorem.

**Proof audit priority:** The dense upper-endpoint proof in checkpoints 38–40 is independent of the weighted-flag extraction. The complete arithmetic lists additionally depend on that earlier broad theorem and should be independently referee-checked before a publication claim.