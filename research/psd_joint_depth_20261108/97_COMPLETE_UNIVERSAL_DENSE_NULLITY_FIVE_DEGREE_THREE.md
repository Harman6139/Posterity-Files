# Milestone 97 — COMPLETE arbitrary-DENSE sharp PSD exponent spectrum at nullity FIVE and facial degree THREE

**2026-11-08. NEW exact necessary-and-sufficient universal theorem for arbitrary real PSD measurement kernels, any positive target rank r, and \((\nu,d)=(5,3)\).** Necessity is proved without sparse/game universality: it combines the genuine dense maxdet-harmonic normal form (checkpoint 91), a blockwise forced-peeling consequence of actual kernel Puiseux coefficients (generalized below from checkpoint 54), the universal two-step dual-center threshold (checkpoint 95), and Sturm's universal \(2^{-d}\) lower exponent. Sufficiency uses explicit fully PSD construction families, plus a NEW tied-edge rational 6×6 example (checkpoint 96). The entire finite logical comparison is checked with exact Fraction arithmetic in checkpoint 98.

## Theorem

Let \(\mathcal L:\mathbb S^{r+5}\to\mathbb R^m\) be arbitrary real linear and let \(X_*\succeq0\) be its UNIQUE PSD solution with target rank \(r\ge1\), target nullity \(\nu=5\), and *minimal* singularity degree **exactly \(d=3\)**. Then the exact sharp full-matrix Hölder recovery exponent belongs to precisely the following **51-element rational set**, and conversely **EVERY** listed fraction is attained at that exact (r,nu,d):
\[
\boxed{\begin{aligned}
\Sigma_{5,3}=\{&
 1/8,\ 3/22,\ 1/7,\ 3/20,\ 5/32,\ 1/6,\ 5/28,\ 2/11,\
 3/16,\ 5/26,\ 1/5,\ 5/24,\ 3/14,\ 7/32,\ 2/9,\ 5/22,\
 3/13,\ 7/30,\ 1/4,\ 7/26,\ 3/11,\ 5/18,\ 9/32,\ 2/7,\
 7/24,\ 3/10,\ 5/16,\ 7/22,\ 9/28,\ 1/3,\ 11/32,\
 9/26,\ 7/20,\ 5/14,\ 4/11,\ 11/30,\ 3/8,\ 5/13,\
 7/18,\ 11/28,\ 2/5,\ 9/22,\ 5/12,\ 11/26,\ 3/7,\
 13/30,\ 7/16,\ 4/9,\ 5/11,\ 6/13,\ 7/15\}.
\end{aligned}}
\tag{97.1}
\]
The universal sharp largest exponent is \(7/15\), agreeing with the direct dense all-profile endpoint theorem (checkpoint 45). The universal smallest exponent is \(1/8=2^{-3}\), agreeing with Sturm.

### How the 51 values break down

- **49 values:** realized by exact collision-free independently controlled multi-action midpoint incidence pencils, with appropriate vertex blow-ups when fewer than five null coordinates are used. Their exact full-ambient recovery and minimal facial depths are established in checkpoints 57 and 62.
- **Two genuinely tied-edge additions:** \(3/22\), from the explicit 6×6 counterexample in checkpoint 75, and \(3/20\), from the new explicit 6×6 proof in checkpoint 96. In the independent-edge family neither is attainable at nullity five and facial degree three.

Thus the richer tied-edge model is not just a convenience: its extra coupling fills the last TWO gaps in a COMPLETE universal dense classification at the first previously open nonmaximal nullity.

## 1. Dense necessity: genuine maxdet harmonic grades

Let \(K=\ker\mathcal L\), and take the universal *fixed* orthogonal monomial chart of the canonical maxdet center from checkpoint 89:
\[
\mathbb R^{r+5}=U_0\oplus U_1\oplus\cdots\oplus U_k,\qquad
0=w_0<w_1<\cdots<w_k=1,
\quad\sum_{i=1}^k\dim U_i=5 .
\]
The center has positive-definite first diagonal Puiseux coefficient \(H_i\in K\) at exponent \(w_i<1\) on every internal grade \(U_i\), and the all-block order restriction
\[
(H_i)_{ab}=0\quad\text{whenever }w_a+w_b>2w_i.
\tag{97.2}
\]
By the independent universal downshift/Loewner proof of checkpoint 91, each internal grade w_i is a genuine harmonic midpoint of two distinct grades \(w_a,w_b\), a<i<b. The exact sharp recovery exponent is a half-weight \(w_v/2\le w_1\). Thus every dense candidate arises from a STRICT rational harmonic graph with \(h=k-1\le4\) internal vertices, and no unproved dense-to-graph depth equivalence is invoked.

The canonical dual central path provides a valid exposing chain along the k grades (checkpoint 92), so \(d\le k\). Because d=3, only \(k=3,4,5\) (h=2,3,4) need consideration.

Sturm's degree-three estimate gives \(\alpha\ge1/8\). The universal dense dual-truncation theorem (checkpoint 95) proves that **if \(w_1\ge1/2\), then \(d\le2\)**, so any degree-three candidate must have
\[
\boxed{w_1<1/2.}
\tag{97.3}
\]

## 2. Additional dense NECESSARY bound: a blockwise forced-peeling recurrence

The earlier forced-peeling theorem (checkpoint 54) was first written for simple one-dimensional null valuation grades. Here is its direct complete extension to arbitrary positive-dimensional grades \(U_i\), needed because \(k\) may be three or four although nullity is five.

For each internal i let
\[
\rho_i=\max\{j\le k:w_j\le2w_i\}.
\]
Equation (97.2) implies **the ENTIRE actual kernel coefficient \(H_i\) is supported on**
\[
W_{\rho_i}=U_0\oplus U_1\oplus\cdots\oplus U_{\rho_i}.
\]
Define a descending integer recurrence on grade indices by
\[
j_0=k,\quad j_1=k-1,
\quad
j_{\ell+1}=
\#\{\,i\in\{1,\ldots,j_\ell-1\}:2w_i<w_{j_\ell+1}\,\}
\quad(\ell\ge1),
\tag{97.4}
\]
and stop when j=0. Let \(f(w)\) be the number of recurrence transitions. Then:
\[
\boxed{\operatorname{singdeg}(\mathcal L,X_*)\ge f(w).}
\tag{97.5}
\]

**Proof.** The maximal first exposing stress has support precisely \(U_k\) (checkpoint 92), hence the first greedy face is exactly \(W_{k-1}\). Suppose at some later stage the current PSD face \(F\) contains \(W_j\). Put \(q=\#\{i<j:2w_i<w_{j+1}\}\). For i≤q, \(\rho_i\le j\), so the actual matrix \(H_i\) belongs to \(K\cap\mathbb S(W_j)\subseteq K\cap\mathbb S(F)\). If S is any PSD compressed exposing stress on F annihilating the target support U0, then
\[
\langle S,H_i\rangle=0\quad(i=1,\ldots,q).
\]
Inductively kill its rows on U1,...,Uq. At i=1, all null-null blocks of H1 involving a higher positive grade must pair with a LOWER positive grade (impossible), because their two weights would otherwise sum to more than 2w1. Thus the pairing reduces to
\(\langle S_{U_1U_1},(H_1)_{U_1U_1}\rangle=0\). The second factor is PD, the first PSD; hence S vanishes on the entire U1 rows/columns. Suppose rows of U1,...,U_(i-1) vanish. Any null-null block of H_i involving a grade U_b with b>i can only join a grade U_a with a<i by (97.2), so its stress pairing is already zero. Lower-grade blocks and source blocks also pair to zero. Hence
\[
0=\langle S,H_i\rangle
 =\langle S_{U_iU_i},(H_i)_{U_iU_i}\rangle,
\]
forcing S to vanish on the entire Ui rows/columns. Consequently S annihilates W_q and the next exposed face still contains W_q. Iterating this constraint from the first greedy face gives (97.4), and no exposing chain can finish in fewer than f(w) steps. QED.

This is a pure **NECESSARY dense-kernel** restriction; it does not assume the scalar harmonic graph's own peeling is equal to the original problem's degree.

## 3. Exhaustive FINITE necessary candidate enumeration

At k≤5 there are at most h=4 internal distinct weights. For each h=2,3,4, enumerate every ordered parent pair
\[
0\le a_i<i<b_i\le h+1,\qquad 1\le i\le h,
\]
for a total of \((h!)^2\) rational harmonic systems at h: 4,36,576 possible choices respectively. Solve each exact rational system. Retain strictly increasing solutions with endpoints 0,1, \(w_1<1/2\), forced-depth recurrence \(f(w)\le3\), and candidate \(\alpha=w_v/2\le w_1\) satisfying \(\alpha\ge1/8\).

The companion standalone exact Fraction program (checkpoint 98) performs these precise rational operations and produces EXACTLY **51** fractions, precisely those in (97.1). Because checkpoints 89, 91, 92 and 95 plus the blockwise recurrence (97.5) show that **EVERY arbitrary dense** candidate must appear in this finite enumeration, this proves the universal NECESSITY of the 51-element list. It is not a sparse-peeling guess.

## 4. Constructive sufficiency for EVERY candidate

For h=1,2,3,4, enumerate every nonempty action subset at each internal node among its finitely many lower/higher parent pairs, requiring no action edge be used by two different vertices. There are precisely **17,302** collision-free action systems over all h≤4 (17,169 at h=4). For each, solve the exact rational Bellman minimum by deterministic proper stochastic policy iteration, retain strict weights and canonical greedy peeling **degree exactly three**, then collect every valid half-weight \(w_v/2\le w_1\).

This independently verified rational enumeration produces exactly **49** values, and for each it outputs an explicit multiaction parent network with exact facial degree three and target nullity at most five. If the network has fewer than five null vertices, the vertex-blow-up theorem (checkpoints 52 and 62) raises nullity to exactly five without changing exponent or number of exposing steps. Its proof constructs full PSD stresses for all clones and proves both the global arbitrary-competitor recovery bound and a matching strictly PD arc. Positive target padding gives arbitrary target rank r.

**Only two candidates from the necessary 51 do not occur among those 49:**
\[
\frac3{22}\quad\text{and}\quad\frac3{20}.
\]
They are realized by explicit tied-edge 6×6 rational systems:
- \(\alpha=3/22\), exposed-rank profile (1,3,1): checkpoint 75;
- \(\alpha=3/20\), exposed-rank profile (1,3,1): checkpoint 96.

Both have direct all-PSD upper recovery estimates, strict PD monomial sharpness curves, and full dual stress minimal-degree proofs, entirely independent of any game universality assumption.

Therefore **EVERY** member of (97.1) is attained at precisely (r,nu,d)=(r,5,3), proving SUFFICIENCY. Together with Section 3, this proves the theorem. QED.

## Significance and scope

1. This is the FIRST completed **nonmaximal-depth arbitrary-DENSE** spectrum at nullity five. It substantially extends the all-degree nullity-four classification in checkpoint 41, without any dense-to-tied-game representation conjecture.
2. The numerical 51-element set is **certified by exact finite rational enumeration** and explicit full-PSD constructions, not fitted data. The proof's universal necessity does not invoke the speculative tied-game universality inclusion.
3. It identifies a second critical tied-edge fraction \(3/20\) beyond the formerly known \(3/22\) counterexample.
4. **Not yet solved:** universal joint exponents for all higher nullities and all nonmaximal degrees, including the full dense-to-tied-game necessity implication. The dual truncation and forced-peeling recurrence are NECESSARY but not always jointly sufficient at arbitrary nullity; the present finite case is special because its candidates exactly match known explicit constructions.
5. The project-wide theorem proofs and code still require independent specialist review before journal-level claims of priority or completeness.

## Reproducibility

The complete standalone standard-library Fraction audit enumerates harmonic parents, forced valuation peeling and collision-free multiaction sets, then validates both tied-edge witnesses. The file is checkpoint 98 in this same folder. It runs without numerical SDP solvers, stochastic sampling or third-party packages.