# Milestone 127 — EXACT positive-circuit elimination criterion for any proposed PSD facial step; the two research routes meet

**2026-11-09. Proved by finite-dimensional linear algebra and the semidefinite Gordan–Stiemke alternative.** This is the precise local test needed by both routes: kernel circuits that eliminate off-face coordinates can create positive projected obstructions, while a strictly positive-dual certificate is sufficient to expose the intended coordinate/subspace block. This is an **iff for a given current face and proposed exposed subspace**, not a uniform arithmetic classification of all exponent/depth pairs.

## The face-projection theorem

Let \(K\subseteq\mathbb S^n\) be any real linear subspace, \(F\subseteq\mathbb R^n\) a current PSD face's support subspace, and \(C\subseteq F\) an intended exposed subspace with \(C\perp\operatorname{range}X_*\). Write
\[
K_F:=K\cap\mathbb S(F),\qquad
Q_{F,C}:=\{P_CHP_C:H\in K_F\}\subseteq\mathbb S(C).
\]

**Theorem.** The following are equivalent:

1. There exists a legitimate ambient measurement stress \(Z\in K^\perp\) whose compression \(S=P_FZP_F\) is PSD, has support **exactly \(C\)**, and is positive definite on \(C\).
2. \(Q_{F,C}\cap\mathbb S_+(C)=\{0\}\).
3. There is a matrix \(T_C\succ0\) on \(C\) satisfying \(\langle T_C,P_CHP_C\rangle=0\) for all \(H\in K_F\).

If these conditions hold, one can choose the compressed stress \(S\) to be exactly the zero extension of \(T_C\) to \(F\), with no uncontrolled cross-blocks in the current face. Thus the condition is sufficient for an actual PSD facial reduction, not only an abstract linear separating vector.

**Proof.** If (1) holds, \(S\) is the zero extension of some \(S_C\succ0\) because it is PSD with support exactly \(C\). Since the full ambient \(Z\) is perpendicular to K, every \(H\in K_F\) satisfies
\[
0=\langle Z,H\rangle=\langle S,H\rangle
  =\langle S_C,P_CHP_C\rangle.
\]
Thus \(S_C\succ0\) lies in \(Q_{F,C}^\perp\), giving (3), and a strictly positive definite matrix cannot be orthogonal to any nonzero PSD matrix, giving (2).

The equivalence (2) \(\Leftrightarrow\) (3) is the strict homogeneous semidefinite Gordan–Stiemke alternative: because the trace-one PSD cone section is compact, strict separation from the linear space \(Q_{F,C}\) produces a positive-definite normal in \(Q_{F,C}^\perp\). Conversely such a normal has positive pairing with every nonzero PSD element.

Finally assume (3). Extend \(T_C\) by zero inside \(F\), obtaining \(T\in\mathbb S(F)\) with \(T\succeq0\) and support \(C\). It annihilates \(K_F\). The elementary exact compression-annihilator identity
\[
 (K\cap\mathbb S(F))^\perp_{\mathbb S(F)}
 =
 P_F K^\perp P_F
\]
supplies an ambient \(Z\in K^\perp\) whose entire \(F\)-compression equals \(T\). Thus Z is a valid exposing stress with the required PSD rank and support, giving (1). QED.

## Positive-circuit obstruction and its exact graded example

If a concrete finite linear combination \(J=\sum_jc_jH_j\) of genuine original invisible kernel matrices **cancels all off-face entries** (so \(J\in K_F\)), while \(P_CJP_C\succeq0\) is nonzero, then condition (2) fails. Such a \(J\) is an **explicit positive projected circuit** and certifies that C cannot be exposed at that step. No eigenvalue estimation or candidate dual stress construction is needed.

In the six-nullity grade-aligned forbidden schedule of checkpoint125, let
\[
w=(0,1/4,3/7,1/2,17/28,5/7,1),
\quad F=\operatorname{span}(e_0,\ldots,e_5),
\quad C=\operatorname{span}(e_4,e_5).
\]
The ORIGINAL dense canonical center's Puiseux kernel coefficients \(H_3=A_{w_3}\) and \(H_4=A_{w_4}\) have \((H_3)_{06}\ne0\) by the unique harmonic midpoint at \(w_3=1/2\). Their only potential nonzero off-face blocks involving terminal direction e6 are both multiples of \(F_{06}\), by the exact Cauchy–Schwarz weight support restrictions:
\[
w_1+w_6>2w_3,\qquad
w_1+w_6>2w_4.
\]
Consequently the *actual kernel circuit*
\[
\boxed{
J=H_4-\frac{(H_4)_{06}}{(H_3)_{06}}H_3
\in K_F
}
\]
has **no off-face entries at all**. On the desired exposed subspace,
\[
\boxed{
P_CJP_C=(H_4)_{44}E_{44}\succeq0,\qquad
(H_4)_{44}>0.
}
\]
Theorem (2) immediately forbids any PSD exposing stress supported on C at F. This recasts checkpoint125's dual bottleneck contradiction as an explicit PSD projected **primal circuit**.

This construction is independent of all other dense kernel coefficients: H3 and H4 are the actual maxdet Puiseux modes of the original dense instance.

## A purely rank-theoretic special case

When \(C\) is one-dimensional, \(Q_{F,C}\) is either \(\{0\}\) or the full one-dimensional space \(\mathbb S(C)\), and
\[
\boxed{
C\text{ is singly exposable from }F
\iff
H_{CC}=0\text{ for EVERY }H\in K_F.
}
\]
This is an ordinary exact linear rank/nullspace test. The genuine additional difficulty of general nonmaximal-degree classification begins with **multidimensional exposing blocks**, where \(Q_{F,C}\cap\mathbb S_+(C)=\{0\}\) is a conic rather than plain rank condition.

For an arbitrary proposed coordinate-subspace facial schedule \(F_0\supsetneq\cdots\supsetneq F_d\) with exposed subspaces \(C_j=F_{j-1}\cap F_j^\perp\), the sequence is valid iff the face-projection test succeeds at EVERY stage. Exact *minimality* requires excluding all shorter stress chains. This yields the finite signed-conic tower of checkpoint120 directly, without any idealized graph representation.

## Interpretation for the frontier

- **Route 1:** clone elimination cannot be a universally valid local move that blindly identifies duplicate parent edges: the resulting positive kernel circuit can prohibit an intended exposing block or change the canonical exponent. The example shows a genuinely impossible coordinate flag, not necessarily an impossible exponent/depth PAIR.
- **Route 2:** the smallest complete local invariant is the PSD incidence of each projected restricted kernel \(Q_{F,C}\), beyond its scalar valuation weights and ordinary coordinate matroid ranks. This conic-matroid tower determines facial stress feasibility exactly.
- The desired *short, all-nullity, entirely arithmetic formula* for which exponent/depth pairs occur (without constructing general real kernels or solving conic feasibility) remains OPEN. This theorem does not pretend to eliminate the remaining positivity condition; it makes that condition exact and local.

The strict PSD alternative and compression-annihilator identity are established tools; this milestone's contribution is an explicit positive-circuit use of them in the new harmonic Dikin-frontier problem. Bibliographic priority is not asserted.