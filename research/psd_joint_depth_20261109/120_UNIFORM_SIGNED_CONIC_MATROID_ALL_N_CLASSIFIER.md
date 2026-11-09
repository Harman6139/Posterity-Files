# Milestone 120 — a COMPLETE UNIFORM all-n ANALYTIC spectrum classifier via finite harmonic graphs, weighted matroid bases and SIGNED conic stress towers

**2026-11-09. NEW necessary-and-sufficient characterization, valid for EVERY matrix order n, positive target rank r, minimal facial-reduction degree d, and sharp full-PSD recovery exponent α.** The certificate requires only: finitely many rational harmonic weights; ONE constant real matrix representing the measurement kernel; linear *basis-exchange* rank conditions; finitely many positive-definite/PSD matrix inequalities; and a finite facial-reduction stress tower (or its equivalent first-order no-shorter-chain condition). All requirements are polynomial equalities/inequalities with known rational coefficients, hence admit terminating exact real quantifier elimination. The construction needs NO Puiseux quantification, no unknown path parameter, no asymptotic optimization and no dense-to-tied-game conjecture.

This is a **FULL effective ANALYTIC classification for all n**, significantly more structured than the raw central-curve real-QE formulation in checkpoints 14–16. It is **NOT YET** the stronger compact *purely arithmetic graph-only* formula sought in the project: the finite signed conic-matroid real-feasibility test has not been eliminated by a universal incidence construction. The distinction must be retained when communicating to the project lead.

## 1. Finite combinatorial outer data

Fix integers n>r>=1, ν=n−r, d∈{1,...,ν}. Let N=n(n+1)/2. Enumerate h=0,1,...,ν−1 and every strictly increasing finite harmonic graph with source0, h internal levels and terminal h+1:
\[
0=w_0<w_1<\cdots<w_h<w_{h+1}=1,\quad
2w_i=w_{a_i}+w_{b_i},\quad0\le a_i<i<b_i\le h+1.
\]
Each h admits only (h!)² parent assignments, each solved with rational linear algebra. Let k=h+1. Enumerate positive grade multiplicities m1,...,mk with Σm_i=ν. Put θ=0 on an r-dimensional source block U0, and θ=w_i on the mi-dimensional null grade Ui. Thus every symmetric entry-coordinate a=(u,v) has known rational weight
\[
\eta_a=(\theta_u+\theta_v)/2.
\]
Enumerate candidate α∈{1}∪{w_v/2≤w1:v=1,...,k}; if h=0 also allow 1/2. (For h≥1, w1 itself is a halfweight via the lowest harmonic parent pair.)

**These finitely many outer cases contain EVERY actual dense PSD inverse problem's canonical weights and sharp exponent**, by the independently proved canonical fixed monomial-center theorem (checkpoint89), dense-to-harmonic value normal form (91) and Plücker-matroid exponent formula (93). They therefore supply a bounded finite rational search independent of real QE degrees.

## 2. Exact FINITE signed-conic-matroid kernel certificate

For each outer weight/multiplicity choice, let \(K\subset\mathbb S^n\) be the span of p unknown real symmetric matrices H1,...,Hp, where p∈{0,...,N} is also enumerated. Represent them in a fixed Frobenius-orthonormal symmetric entry basis as the columns of an N×p real matrix A. The columns must be linearly independent. The intended measurement map is simply L=P_(K⊥) and target \(X_*=\operatorname{diag}(I_r,0)\).

When p>=1 impose ALL the following finite conditions.

**(S) Source uniqueness.** The coordinate projection of K onto matrix entries with at least one index OUTSIDE U0 is injective:
\[
K\cap\mathbb S(U_0)=\{0\}.
\]
Equivalently, the corresponding submatrix of A has full column rank p; this is a finite nonzero-minor condition.

**(M) A maximum-weight matroid pivot basis.** Choose an ordered set I=(a1,...,ap) of p distinct coordinate rows, with nonincreasing weights β_j=η_(a_j), and require A[I,:] invertible. Write
\[
C=A(A[I,:])^{-1}.
\]
Require \(C_{a,j}=0\) whenever \(\eta_a>\beta_j\). These are ordinary **polynomial** conditions after clearing det A[I,:]. They exactly certify that the chosen rows form a maximum-total-weight basis of the representable coordinate-row matroid: if a higher-weight row could replace pivot a_j, the corresponding coefficient would be nonzero and violate the condition; conversely local single basis-exchange optimality is equivalent to global matroid maximum-weight optimality.

**(I) FINITE graded initial-cone data.** Define an explicit N×p matrix
\[
B_{a,j}=\begin{cases}
C_{a,j},&\eta_a=\beta_j,\\
0,&\eta_a\ne\beta_j.
\end{cases}
\]
By (M) it is the Grassmannian limit of the scaled kernel \(D_\epsilon^{-1}KD_\epsilon^{-1}\), with \(D_\epsilon=\operatorname{diag}(\epsilon^{\theta_i/2})\), as proved below. Its pivot rows form the identity, so B has column rank p. Let \(\mathcal I_\theta(K)=\operatorname{span}\{\operatorname{mat}(B_{\cdot,j}):j=1,...,p\}\).

Require a real **positive-definite matrix W** orthogonal to ALL p initial generators:
\[
W\succ0,\qquad
\langle W,\operatorname{mat}(B_{\cdot,j})\rangle=0
\quad(j=1,\ldots,p).
\tag{120.1}
\]
This is a finite strict LMI with entries rational functions of A; clearing det A[I,:] makes it polynomial. By Gordan–Stiemke, it is equivalent to
\(\mathcal I_\theta(K)\cap\mathbb S_+^n=\{0\}\).

**(P) ONE grade-positive primal kernel mode per internal grade.** For each i=1,...,h (i.e. each w_i<1), require a linear combination \(T_i=\sum_{j=1}^p c_{ij}H_j\in K\) such that
\[
(T_i)_{uv}=0\quad
\text{whenever }(\theta_u+\theta_v)/2>w_i,
\qquad
P_{U_i}T_iP_{U_i}\succ0.
\tag{120.2}
\]
All coefficients are unknown real variables; positive definiteness of each finite grade compression is a finite principal-minor test.

**(E) EXACT minimal facial-reduction degree d.** Quantify symmetric orthogonal projectors
\(P_0=I,P_1,\ldots,P_d=P_{U_0}\) and stresses \(Z_j\in K^\perp\) such that each current compressed \(S_j=P_{j-1}Z_jP_{j-1}\succeq0\), with \(\operatorname{ker}(S_j)\cap\operatorname{range}(P_{j-1})=\operatorname{range}(P_j)\) and strict rank drop, preserving U0. Encode exact kernel by
\[
P_{j-1}P_j=P_j,\quad S_jP_j=0,\quad
S_j+P_j+(I-P_{j-1})\succ0.
\]
Require **NO** such complete chain of any smaller length \(0,...,d-1\). This is a finite first-order real-algebraic condition (or, equivalently, require each chosen stress to be maximal rank on its current face with a universal PSD-stress test). To refine the result to a prescribed rank-drop PROFILE s1,...,sd, add \(\operatorname{tr}P_{j-1}-\operatorname{tr}P_j=s_j\).

**(A) EXACT exponent:** impose
\[
\boxed{\min(1,\beta_p)=\alpha}.
\tag{120.3}
\]
For p=0, set α=1, and the map is injective, giving d=1 when ν>0.

### Main theorem

For EVERY fixed tuple \((n,r,d,\alpha)\), with positive rank r and rational α, a uniquely recoverable real PSD inverse problem with these invariants **EXISTS if and only if** one of the above FINITELY MANY graph/multiplicity/kernel/pivot choices satisfies the complete (S),(M),(I),(P),(E),(A) certificate.

Every certificate is a first-order formula over the real closed field with finitely many variables and explicit **polynomial** coefficients in Q. Real quantifier elimination TERMINATES and correctly decides the existence claim at ANY n, rank, degree or prescribed full facial rank profile.

## 3. Proof that the weighted pivot B is EXACTLY the graded initial subspace

Represent the scaled kernel \(K_\epsilon=D_\epsilon^{-1}KD_\epsilon^{-1}\) by the row-scaled N×p matrix
\[
A_\epsilon=\operatorname{diag}(\epsilon^{-\eta_a})A.
\]
Its selected pivot rows are
\(A_\epsilon[I,:]=\operatorname{diag}(\epsilon^{-\beta_j})A[I,:]\),
so their inverse is
\((A[I,:])^{-1}\operatorname{diag}(\epsilon^{\beta_j})\).
Therefore the unique coordinate basis normalized to have identity on pivot rows is
\[
A_\epsilon(A_\epsilon[I,:])^{-1}
=\bigl[C_{a,j}\epsilon^{\beta_j-\eta_a}\bigr]_{a,j}.
\]
If \(\eta_a>\beta_j\), (M) forces C_(a,j)=0. Every nonzero remaining exponent \(\beta_j-\eta_a\) is nonnegative. Thus this coordinate basis converges as epsilon→0 to EXACTLY the matrix B in (I); its selected pivot rows remain the identity, so the limiting subspace has dimension p. This proves that (I) is the genuine weighted Grassmannian initial space and not a heuristic tropical support graph.

The matroid maximum-basis condition (M) can be imposed as a finite polynomial replacement-minor test:
\[
\det A[I_j\!\leftarrow a,:]=0
\quad\text{whenever }\eta_a>\beta_j.
\]
This avoids variables for the inverse matrix if desired. No analytic limit or Puiseux coordinate is part of the final membership formula.

## 4. SUFFICIENCY — from one finite certificate to a REAL dense PSD inverse problem

Let (S),(M),(I),(P),(E),(A) hold. Set K=col(A) and L=P_(K⊥). The graded cone theorem of checkpoint119 proves a UNIFORM Loewner upper bound:
\[
Y\succeq0,\quad\|L(Y-X_*)\|\le C_0\epsilon
\quad\Rightarrow\quad
Y\preceq C D_\epsilon^2
\]
from the positive-definite dual W orthogonal to the initial space B. This holds for EVERY ambient PSD competitor, including arbitrarily dense ones.

By (P), the finite generalized polynomial
\[
Y_\epsilon^{(\sigma)}
=X_*+\sum_{i=1}^{h}e^{\sigma w_i^2}\epsilon^{w_i}T_i
     +e^\sigma\epsilon I
\]
has, at each positive null grade Ui, a strictly positive-definite first diagonal coefficient; all nonzero blocks obey the pair-weight order restriction by (P); the terminal grade Uk=1 is strictly positive through the εI term. The elementary diagonal coefficient-rescaling lemma (checkpoints89/119) makes \(Y_\epsilon^{(\sigma)}\succ0\) and
\(Y_\epsilon^{(\sigma)}\succeq cD_\epsilon^2\) for all small epsilon and one sufficiently large fixed sigma. Since each Ti lies in K, its measurement residual is exactly \(e^\sigma\epsilon\|L I\|\).

Hence the canonical shifted maxdet center obeys
\(cD_\epsilon^2\preceq C_\epsilon\preceq CD_\epsilon^2\), by the primal–dual characterization (checkpoint119). The universal Dikin–Hessian curvature theorem and the exact matroid greedy formula (checkpoints10/93/94) then yield the sharp full-PSD exponent
\[
\alpha=\min(1,\beta_p),
\]
which equals the prescribed α by (A).

The same graded dual upper bound implies UNIQUENESS: if \(Y\succeq0\) has exact measurements of X*, the upper chart holds for every epsilon, so letting ε→0 forces Y to be supported entirely on U0. Then Y−X*∈K∩S(U0)={0} by (S), so Y=X*.

Finally (E) gives the exact required MINIMAL facial-reduction degree, or its prescribed rank-drop profile. Thus the constructed *actual real measurement map* realizes the tuple. No dense-to-sparse incidence conjecture enters the proof.

## 5. NECESSITY — extract the certificate from ANY original dense PSD problem

Conversely take an arbitrary dense uniquely recoverable PSD inverse problem with invariants (n,r,d,α). Orthogonal conjugation and fixed positive support normalization put its target in the stated block form, preserving exponent and singularity degree (up to constant norm equivalence). The universal maxdet theorem (checkpoint89) gives a fixed orthogonal valuation flag with rational weights 0<w1<...<wk=1; the independent harmonic downshift theorem (checkpoint91) gives EXACT parent midpoint relations for every internal grade. The corresponding grade multiplicities sum ν. Thus one outer graph case is selected.

Take any Frobenius-orthonormal basis of the ORIGINAL kernel K and its coordinate matrix A; choose a greedy maximum-weight pivot row basis I, giving (M). Stationarity and the two-sided maxdet chart make the normalized dual
\(D_\epsilon C_\epsilon^{-1}D_\epsilon\) converge to a PD matrix W orthogonal to the graded initial subspace B, proving (I) by milestone119. Source uniqueness gives (S).

For every grade w_i<1, the actual Puiseux coefficient of the center at exponent w_i lies in K, satisfies weighted support restrictions and has strictly positive definite Ui diagonal, proving (P) with ONE actual coefficient per internal grade. The actual minimal facial-reduction chain satisfies (E); and the universal matroid curvature theorem gives α=min(1,β_p), proving (A). Hence every realizable tuple yields an admissible FINITE certificate. QED.

## 6. Finiteness, exact computability and what remains

At fixed ν, harmonic graph cases are finite with h≤ν−1, (h!)² parent assignments per h, and finitely many grade multiplicity compositions of ν. Every candidate α is rational and drawn from their halfweights plus 1. The unknown kernel dimension p is at most N; there are finitely many possible pivot row subsets I. For each tuple, (S),(M),(I),(P),(E),(A) comprises **explicit polynomial equality/strict inequality formulas with finitely many quantified real variables**. Exact real quantifier elimination therefore gives a TERMINATING decision and an algebraic sample kernel for every TRUE tuple; it simultaneously permits all prescribed exact exposing rank profiles. The procedure is uniform for every n, with no unseen "for sufficiently large n" gap.

This is a **complete all-n analytic/semialgebraic classification** and a signed-conic-matroid explanation of WHY graph-only models can fail: positive initial cone geometry, not just unsigned parent incidence, must be represented. It is more informative than a brute-force polynomial contact test, because the entire exponent part is handled by finite weighted row matroid rank and a finite graded positive cone.

**NOT CLAIMED:** A compact, purely integer/graph-only necessary-and-sufficient spectrum with no real-conic feasibility subtest, polynomial-time complexity, or a universal dimension-preserving tied-edge construction. The original project's strongest aspirational **closed arithmetic classification** is still open. Previous algorithmic classifiers 14/16 were also complete but less structured. This milestone improves the analytic certificate and finite candidate space; it does NOT remove the remaining real-algebraic satisfiability layer.

## 7. Boundaries

- If r=0, target zero and unique PSD recovery imply a single strictly positive exposing stress and Lipschitz exponent α=1, degree d=1 (unless n=0). If r=n, unique feasibility forces K=0, exponent α=1 and facial degree d=0; treat separately.
- For d=1, positive-rank singular targets have exponents α∈{1,1/2}; the certificate captures both.
- Every eigenvalue/exponent claim relies on the previously proved full Frobenius Dikin–Hessian modulus; specialist external review and novelty/priority checks remain necessary.

## Provenance

The conic Gordan alternative, semialgebraic Puiseux expansions, matroid greedy theorem and Tarski–Seidenberg quantifier elimination are standard mathematics. The finite signed-conic harmonic certificate and its Dikin sufficiency proof are stated here with complete internal proofs. This is a theorem of exact mathematical feasibility, not a claim of a human-readable short fraction formula.
