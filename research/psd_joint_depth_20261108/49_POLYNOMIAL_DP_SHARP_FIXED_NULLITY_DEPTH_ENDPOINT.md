# Milestone 49 — exact polynomial-size dynamic program for the UNIVERSAL sharp PSD endpoint at fixed (nullity, facial depth)

**2026-11-08. PROVED for all arbitrary dense PSD measurement maps via checkpoint 45.** This replaces enumeration over all positive compositions of nullity with a short rational dynamic program computing the exact *largest attainable* recovery exponent at prescribed target nullity ν and minimal facial-reduction degree d. It also returns an explicit extremal exposing rank profile and hence a matching sparse PSD pencil. The full set of subendpoint rational exponents remains unsolved.

## Main result

For integers ν>=d>=3 let
\[
B_{\nu,d}:=\sup\{\alpha(\mathcal L,X_*):\ \operatorname{nullity}X_*=\nu,\ \operatorname{singdeg}=d,\ \operatorname{rank}X_*\ge1\}.
\]
The supremum is achieved and equals the **maximum** of the exact profile expression β(s_1,...,s_d) in checkpoint 45, over all positive compositions s_1+...+s_d=ν. The expression does not involve s_1; increasing another s_j increases β. Hence every maximizer has s_1=1.

Put m=ν-1 and define recursively, for 2<=j<=d-1 and integer budgets b>=j-1:
\[
F_2(b)=\frac{1}{2^b-1},
\quad
F_j(b)=\min_{\substack{a\ge1\\b-a\ge j-2}}
\frac{1+F_{j-1}(b-a)}{2^a-1}\qquad(j\ge3).
\]
Then
\[
\boxed{
B_{\nu,d}=
\frac{1}{2(1+R_{\nu,d})},
\qquad
R_{\nu,d}=
\min_{\substack{a\ge1\\m-a\ge d-2}}
\frac{F_{d-1}(m-a)}{2^a}.
}
\]
The minimizing indices reconstruct a positive profile (s_1,...,s_d) with s_1=1, s_d=a, and s_2,...,s_{d-1} obtained from the nested argmin choices in F. The exact harmonic layered network in checkpoint 45 realizes B_{\nu,d}, so the result is sharp, constructive, and valid for all dense kernels on the necessity side.

For d=2, B_{\nu,2}=1/2, and for d=ν, B_{\nu,\nu}=1/ν.

## Proof of recursion

With q_j=2^{s_j}-1 and the exact endpoint formula
\[
\beta(s)=\frac{2^{s_d-1}\prod_{j=2}^{d-1}q_j}
{1+\sum_{\ell=2}^d\prod_{j=2}^{\ell}q_j},
\]
divide numerator/denominator by \(2^{s_d}\prod_{j=2}^{d-1}q_j\) to obtain
\[
\beta(s)=\frac1{2(1+2^{-s_d} H_{d-1})},
\quad
H_2=\frac1{q_2},\qquad
H_j=\frac{1+H_{j-1}}{q_j}\quad(3\le j\le d-1).
\]
For each fixed total budget b assigned to s_2,...,s_j, the optimal H_j is obtained by choosing the last size a=s_j and the optimal preceding H_{j-1}, precisely the displayed F_j recurrence. Finally minimize \(2^{-s_d}H_{d-1}\) over the last size a=s_d, with remaining budget m-a.

The expression is independent of s1 and strictly increasing in all sj for j>=2 when d>=3. Thus if s1>1, transferring one unit from s1 to s_d strictly increases β; an optimizer must have s1=1. This proves the recurrence and its global optimality. Each candidate ratio is rational with numerator/denominator of bit length O(poly ν), and there are O(dν) states and O(ν) transitions each, yielding O(dν²) exact rational arithmetic operations. QED.

## Small exact values

| ν | d=3 | d=4 | d=5 | d=6 |
|---|---|---|---|---|
| 3 | 1/3 | — | — | — |
| 4 | 3/7 | 1/4 | — | — |
| 5 | 7/15 | 3/8 | 1/5 | — |
| 6 | 15/31 | 7/16 | 1/3 | 1/6 |
| 7 | 31/63 | 15/32 | 7/17 | 3/10 |
| 8 | 63/127 | 31/64 | 5/11 | 7/18 |

The exact profile/witness enumerator and an independent dynamic-program implementation agree on ALL positive compositions through ν=10 (1,013 profile networks checked with exact Fraction arithmetic). A further test at ν=22,d=20 confirms that optimal profiles may distribute extra directions over multiple layers, so concentrating all surplus in the penultimate layer is NOT a universal rule. The DP handles this correctly.

## Scope and rigor

This is a closed combinatorial (arithmetic recurrence) theorem for **the sharp upper endpoint**, not an all-value set classification. It provides a finite, explicit optimal dimension/depth barrier:
    α > B_(ν,d)  =>  impossible at that (ν,d),
and equality is always attainable for every r>=1. This is stronger than Sturm's depth-only lower bound, which constrains α from the opposite side.

No quantifier elimination, SDP solving, or full mediated-set enumeration is required to compute B_(ν,d). The proof of necessity is the direct dense Gordan–Stiemke coefficient-rescaling theorem; the construction is the layered sparse harmonic pencil.