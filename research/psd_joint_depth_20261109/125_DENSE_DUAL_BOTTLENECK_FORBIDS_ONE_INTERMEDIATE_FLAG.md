# Milestone 125 — a strict harmonic-grade flag can forbid an intermediate exposing schedule even for arbitrary DENSE kernels

**Date 2026-11-09. RIGOROUS NECESSARY obstruction under explicitly stated canonical valuation-flag alignment.** This is not a counterexample to degree-only interval filling. It is a new dense-kernel face-compression circuit obstruction that shows why a universal interpolation theorem must sometimes change the exposing schedule, not just merge or split layers arbitrarily.

## The example

Fix a uniquely PSD recoverable rank-one target \(X_*=E_{00}\) with nullity six. Suppose its **canonical fixed orthogonal Dikin/maximum-determinant valuation flag** has one-dimensional grades with exact weights
\[
(w_0,w_1,\ldots,w_6)
=\left(0,\frac14,\frac37,\frac12,\frac{17}{28},\frac57,1\right).
\tag{125.1}
\]
These form the unique harmonic parent policy
\[
P=((0,3),(1,4),(0,6),(3,5),(2,6)).
\tag{125.2}
\]
Its universal primal/dual grade-peeling bounds are
\[
L(w)=3,\quad U(w)=5,
\]
with prefix schedules \(6\to5\to2\to0\) and \(6\to5\to4\to3\to1\to0\), respectively. Therefore a degree-four realization is allowed by the scalar bounds.

### THEOREM A — one SPECIFIC intermediate grade-aligned schedule is impossible in ANY dense kernel

There is **no arbitrary dense PSD inverse problem with valuation grades (125.1)** whose *successive coordinate-aligned exposing layers* are
\[
\boxed{
\{6\},\quad\{4,5\},\quad\{2,3\},\quad\{1\}.
}
\tag{125.3}
\]

This is a genuine universal dense stress obstruction: it does NOT assume an incidence pencil, a sparse support, unique parent edges, or two-generator mode constraints. The conclusion is about a grade-aligned schedule, not all potentially rotated facial-reduction chains with the same rank-drop numbers.

**Proof.** From the universal Dikin center theorem and positive graded-harmonic necessity (checkpoints 89,91,122), the ACTUAL coefficient \(H_i\) of the canonical positive center at Puiseux order \(w_i\) belongs to the original invisible kernel K, has \((H_i)_{ii}>0\), and satisfies
\[
(H_i)_{ab}=0\quad\text{whenever }w_a+w_b>2w_i.
\tag{125.4}
\]
Moreover, \(H_i\) must have a nonzero offdiagonal block of exact midpoint weight \(w_i\) joining a lower and a higher valuation grade.

For \(i=3\), where \(w_3=1/2\), direct rational comparison against ALL pairs \(a<3<b\) shows that the **only exact midpoint parent pair is (0,6)**. Thus
\[
(H_3)_{06}\ne0.
\tag{125.5}
\]
In fact among ALL blocks touching the removed terminal direction e6, (0,6) is the ONLY block of pair weight at most w3, because \(w_1+w_6>2w_3\). Furthermore every block of H3 on the proposed second exposing subspace \(C=\operatorname{span}(e_4,e_5)\) vanishes: both diagonal weights w4,w5 exceed w3, and their offdiagonal average also exceeds w3.

Now suppose (125.3) were a valid exposing chain, and consider ANY ambient measurement stress Z∈K⊥ whose compression \(S=P_W ZP_W\succeq0\) to the first reduced face \(W=\operatorname{span}(e_0,\ldots,e_5)\) exposes e4 and e5 while **preserving** e1,e2,e3. Since S annihilates the target support e0 and has the declared kernel, PSD forces all W-rows of S except rows 4,5 to vanish. Pairing Z with H3, all possible terms therefore vanish EXCEPT its unique off-face (0,6) entry. Hence
\[
0=\langle Z,H_3\rangle=2(H_3)_{06}Z_{06},
\qquad\text{so }Z_{06}=0.
\tag{125.6}
\]

Consider next H4, with \(w_4=17/28\). It has \((H_4)_{44}>0\). Every other block on the exposed 4,5 subspace vanishes: (5,5) is forbidden because \(w_5>w_4\), and (4,5) is forbidden because \(w_4+w_5>2w_4\). Its ONLY possibly nonzero off-face block involving e6 is again (0,6): \((w_1+w_6)/2=5/8>17/28\), and all other non-source weights are larger than w1. All other on-face entries pair to zero with S, by the row-zero property.

Consequently
\[
0=\langle Z,H_4\rangle
=(H_4)_{44}S_{44}+2(H_4)_{06}Z_{06}
=(H_4)_{44}S_{44}>0,
\]
a contradiction. QED.

The proof remains valid if arbitrary additional dense kernel vectors exist: orthogonality to the two *actual positive Puiseux coefficients* H3,H4 is unavoidable. It is a finite, explicit **two-coefficient / one-off-face-entry bottleneck**.

### THEOREM B — the SAME weights and degree FOUR are nevertheless realizable

Take the rational rank-one PSD incidence system in \(S^7\), with λ=1/100, target E00, and one generator for each of the following six globally distinct edges/modes:
\[
\begin{aligned}
H_1&=E_{11}-E_{00}+\lambda F_{03},\\
H_2&=E_{22}-E_{00}+\lambda(F_{05}+F_{14})\qquad\text{(two tied edges)},\\
H_3&=E_{33}-E_{00}+\lambda F_{06},\\
J_3&=E_{33}-E_{00}+\lambda F_{24}\qquad\ \text{(separate safe mode)},\\
H_4&=E_{44}-E_{00}+\lambda F_{35},\\
H_5&=E_{55}-E_{00}+\lambda F_{26}.
\end{aligned}
\]
Measure the orthogonal complement of their span.

The exact min–max Shapley values remain (125.1), because H2 has edge midpoint values \(5/14<3/7\) and \(3/7\), while J3 has midpoint \(29/56>1/2\), so H3 remains the minimizing mode. The exact AND-over-modes/OR-over-tied-edges maximal facial closure from checkpoint 74 produces the DIFFERENT layers
\[
\boxed{
\{6\},\quad\{5\},\quad\{2,3,4\},\quad\{1\}.
}
\tag{125.7}
\]
Consequently its **minimal** degree is four and its exact sharp full-ambient PSD exponent is \(w_1=1/4\), including upper bounds for all PSD competitors and a matching strictly PD monomial curve by checkpoint 74.

This explicit construction shows that **the forbidden schedule is not an obstruction to realizing the exponent–degree PAIR** \((1/4,4)\) at nullity six with those weights. The missing all-n classification only asks for *some* suitable schedule and perhaps *some other harmonic weights*, not the impossible schedule (125.3).

## General bottleneck lemma

Let \(F\) be a current PSD face with target support U0 and a proposed compressed exposing subspace C⊂F∩U0⊥. Suppose actual invisible kernel matrices A,B∈K satisfy:

1. \(P_C A P_C=0\) and \(P_CB P_C\succ0\) on at least one intended exposed coordinate;
2. for every ambient stress Z∈K⊥ whose PSD compression to F has range in C and annihilates U0, the only potentially nonzero off-face pairings with A,B are multiples of ONE common scalar linear functional \(\ell(Z)\);
3. the coefficient of \(\ell(Z)\) in \(\langle Z,A\rangle\) is nonzero.

Then orthogonality to A forces \(\ell(Z)=0\), and orthogonality to B contradicts the strictly positive compressed pairing. Thus C cannot be exposed while preserving the stated lower face.

The concrete example above realizes this lemma with \(A=H_3\), \(B=H_4\), and \(\ell(Z)=Z_{06}\). This is a precise **signed face-compression circuit obstruction** absent from the scalar interval L(w)≤d≤U(w).

## Reproducibility and honest interpretation

The companion checkpoint126 checks the harmonic weights, both integer recurrences, the uniqueness of the (0,6) midpoint at grade 3, the allowed off-face supports of H3/H4, the globally distinct six construction edges, the exact game values and both possible exposing schedules. It uses only Fraction arithmetic and combinatorial closure.

**Proved:** A universal compact *rank-PROFILE* or *exact schedule* formula requires extra signed face-compression information beyond scalar weights.

**NOT proved:** That any candidate exponent–degree pair inside the universal interval fails, or that every intermediate depth fails at fixed nullity. Here a DIFFERENT dimension-preserving schedule succeeds for the SAME weights and degree. This distinction is crucial for the project's primary exponent–degree classification.

The statement depends on the canonical center theorem's genuine Puiseux coefficients, whose specialist external audit is still required.