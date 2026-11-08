# Milestone 68 — nonreciprocal sharp exponents at MAXIMAL facial depth, in every nullity >=6

**2026-11-08. PROVED, with an independent arbitrary-competitor stability argument and explicit six-stage dual stress chain.** This is a new phenomenon absent from the earlier single-action maximal-depth reciprocal family: at target nullity ν=6 and *maximal* singularity degree d=6, the sharp exponent may be the nonreciprocal rational **3/46**. Suspending the terminal yields such a pair in every nullity ν>=6. The earlier theorem classifying the *reciprocal subclass* remains true, but the conjectural *reciprocal-only* maximal-depth necessity fails already in the controlled two-action family.

## The first explicit rational example (7x7 matrices)

Index rows 0,...,6, let E_ii=e_i e_i^T and F_ij=e_i e_j^T+e_j e_i^T. Fix λ=1/100, target X*=E_00 and kernel K spanned by the eight matrices

    H1 = E11-E00 + λ F02
    H2 = E22-E00 + λ F13
    H3 = E33-E00 + λ F05
    J3 = E33-E00 + λ F24
    H4 = E44-E00 + λ F16
    J4 = E44-E00 + λ F35
    H5 = E55-E00 + λ F46
    G  = λ F01.

Let L be orthogonal projection onto K^perp, identified with Euclidean measurement coordinates. All generators have trace zero and terminal diagonal (6,6) zero, so trace and the terminal are measured.

**The Bellman vector is**
\[
(w_0,w_1,w_2,w_3,w_4,w_5,w_6)
=(0,3/23,6/23,9/23,13/23,18/23,1).
\]
The five optimal harmonic equations are
  2w1=w0+w2;
  2w2=w1+w3;
  2w3=w0+w5;
  2w4=w1+w6;
  2w5=w4+w6.
The extra J3 and J4 constraints are **strictly slack**:
\[
(w_2+w_4)/2=19/46> w_3=18/46,\qquad
(w_3+w_5)/2=27/46> w_4=26/46.
\]
Every parent edge is globally distinct. The independent edge G=(0,1) has exponent w1/2=3/46, which is smaller than all internal diagonal weights. Thus the sharp *full-state* exponent is
\[
\boxed{\alpha=3/46}.
\]

### Upper bound for every ambient PSD competitor

For any X≽0 with ||L(X-X*)||_F<=δ, put Y=X*+P_K(X-X*), so E=X-Y has ||E||_F<=δ and Y+δI≽0. Trace Y=1, Y66=0 and trace X=1+O(δ), hence the diagonal coordinates of Y are uniformly bounded.

Write U_i=|Y_ii|+δ (i=0,...,6). Each action coefficient has a UNIQUE parent edge. The 2x2 PSD inequalities of Y+δI give
\[
\begin{split}
U_1&\le C\sqrt{U_0U_2}+\delta,\\
U_2&\le C\sqrt{U_1U_3}+\delta,\\
U_3&\le C(\sqrt{U_0U_5}+\sqrt{U_2U_4})+\delta,\\
U_4&\le C(\sqrt{U_1U_6}+\sqrt{U_3U_5})+\delta,\\
U_5&\le C\sqrt{U_4U_6}+\delta.
\end{split}
\]
Here U0=O(1), U6=δ. Because every parent-action average is >=w_i and some attains equality, a finite weighted maximum principle gives U_i=O(δ^{w_i}).

For full self-containment: Let h_i be the maximal expected number of fair-parent transitions before absorption in {0,6}, allowing adaptive action choice at each state. Always choosing the higher-index parent reaches 6 within <=5 steps, an event with probability >=2^-5, so every h_i is finite and satisfies h_i>=1+(h_a+h_b)/2 for all actions. Choose M0,M6>=4 and M_i=M0 exp(A h_i), with A sufficiently large depending on C and the finite action counts, so that
    δ+C sum_actions sqrt(M_a M_b)δ^{(w_a+w_b)/2}
          <=(M_i/2)δ^{w_i}.
For the boundary variables U0<=M0 and U6=δ<=M6δ. If max_i[U_i/(M_iδ^{w_i})]=R>1, the maximizing internal i has
    R M_i δ^{w_i} <= (1+R)/2 * M_i δ^{w_i},
a contradiction. Thus U_i<=M_iδ^{w_i} for all i. Every individual action coefficient obeys the corresponding parent-edge bound; the leading G variable satisfies |G_coefficient|=O(sqrt(U0U1))=O(δ^{3/46}), and Y00-1 is controlled by trace. Together with ||E||<=δ this proves
\[
\omega(\delta)=O(\delta^{3/46})
\]
for **every** full ambient PSD competitor, and uniqueness follows by sending δ down to zero.

### Exact matching strictly PD curve

For s>0 define
\[
X(s)=E_{00}+s^6H_1+s^{12}H_2+s^{18}H_3+s^{26}H_4
     +s^{36}H_5+s^3G+s^{46}E_{66}.
\]
The two slack generators J3,J4 have coefficient zero. Its source diagonal is
    1-s^6-s^12-s^18-s^26-s^36>1/2
for sufficiently small s; all other diagonal entries are the indicated positive powers. After congruence by inverse square roots of these diagonal entries, the matrix has diagonal one and each nonzero offdiagonal of absolute value at most 2λ=1/50. Each row has at most six such entries, so strict diagonal dominance makes the **entire matrix positive definite** for small s. Since E66∈K^\perp, the residual equals s^46 while displacement is Θ(s^3). This proves
\[
\boxed{\omega(\delta)=\Theta(\delta^{3/46})}.
\]

## EXACT minimal facial depth 6 and explicit dual stresses

Write Z_j as follows:
\[
\begin{array}{ll}
Z_1=E_{66},&
Z_2=E_{55}-50F_{46},\\
Z_3=E_{44}-50(F_{16}+F_{35}),&
Z_4=E_{33}-50(F_{05}+F_{24}),\\
Z_5=E_{22}-50F_{13},&
Z_6=E_{11}-50F_{02}.
\end{array}
\]
For every j=1,...,6 and every one of the eight kernel generators, the Frobenius pairing is **exactly zero**. After removing the last j−1 null coordinates, the compression of Z_j to the current face is the rank-one PSD matrix E_(7−j),(7−j). These give six valid exposing steps.

No step can expose more than one direction: initially, every PSD exposing stress annihilates the source row 0. The equations from H1 and H3 force rows 1 and 3 to vanish; H2 then forces row 2 to vanish, J4 then forces row 4 to vanish, and H5 then forces row 5 to vanish. Only row 6 can be exposed. After removing row 6, H1,H3,H2,J4 force rows 1,3,2,4 to vanish, leaving only row 5. After removing row 5, H1,H2,J3 force rows 1,2,3 to vanish, leaving only row 4. After removing row 4, H1 and H2 force rows 1,2 to vanish, leaving row 3. After removing row 3, H1 forces row 1 to vanish, leaving row 2. Finally row 1 is removed. These arguments apply to **arbitrary PSD compressed exposing stresses** and do not assume diagonal stresses. Thus the canonical maximal exposing ranks are
\[
\boxed{(1,1,1,1,1,1),\quad d=\nu=6.}
\]

## Infinite suspension to every nullity ν>=6

Replace the current terminal T by a new *internal* vertex, introduce a new terminal T+1, and add exactly one kernel generator
\[
H_T=E_{TT}-E_{00}+\lambda F_{0,T+1}.
\]
Leave all old generators and the leading edge unchanged. All old Bellman weights are divided by two, while w_T becomes 1/2 and w_{T+1}=1. The old action edges remain distinct, the new edge is fresh, and all strict inequalities and two original slack margins persist under scaling. The new terminal is exposed at stage one, then the old terminal, followed by the old six-step schedule; exact peeling degree and nullity both increase by one. The monomial PD curve and the global-competitor maximum principle from above apply inductively.

After ν−6 suspensions, the rank-one target has nullity ν, maximal minimal degree d=ν, and exact exponent
\[
\boxed{\alpha_\nu=\frac{3}{46\,2^{\nu-6}}
                =\frac3{23\cdot2^{\nu-5}},\qquad \nu\ge6.}
\]
The numerator three never cancels; all exponents are nonreciprocal.

## What this does—and does NOT—prove

It **refutes** the proposed possibility that maximal-depth sharp PSD exponents must all be reciprocals, already within explicit strict two-action incidence systems. It does NOT contradict the previously proved *reciprocal-subclass* classification or the universal upper endpoint 1/ν. The universal all-exponents arithmetic spectrum at fixed (ν,d) and the dense-to-two-policy necessity conjecture remain open.

A second strictly convex-harmonic example at ν=6 has sharp exponent 2/15 and degree 6 (optional leading edge omitted), further showing the phenomenon is not confined to a single numerator pattern.

This is self-contained apart from elementary finite stochastic hitting-time arithmetic, principal PSD inequalities and standard facial-reduction definitions. All matrix coefficients are rational, and exact symbolic stress orthogonality plus the Bellman and peeling data are checked in companion checkpoint 69.