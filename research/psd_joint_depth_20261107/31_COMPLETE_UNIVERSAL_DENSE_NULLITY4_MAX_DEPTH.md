# Milestone 31 — full universal DENSE maximal-depth spectrum at nullity four

Date: 2026-11-08. **PROVED conditional only on the already-established dense weighted-flag/midpoint extraction theorem**, not on sparse depth preservation or on any new universal extrapolation. All coefficient-support deformations have been independently checked by exact Fraction arithmetic (companion checkpoint 32). This resolves the two candidates isolated in checkpoint 27, and fully classifies arbitrary dense PSD maps with target nullity 4 and minimal degree 4.

## Theorem

Let L:S^n -> R^m be arbitrary real linear, and let X*>=0 be its unique PSD solution with positive rank r and nullity nu=n-r=4. If minimal singularity degree d=4, then the exact sharp full-matrix recovery exponent belongs to
\[
\boxed{\Sigma^{\mathrm{dense}}_{4,4}=
\{1/4,1/5,1/6,1/7,1/8,1/10,1/12,1/14,1/16\}.}
\]
Conversely all nine listed exponents occur for arbitrary prescribed target rank r and matrix size n=r+4, by the explicit exact-degree sparse chains of checkpoint 17. Thus the formula is an **if-and-only-if universal dense result**.

The only previously open candidates were 3/16 and 3/14. We rule out both by a contradiction using the *same dense kernel* and no sparsification.

## 1. Universal flag data and first facial stress

Write U0=range X*, dim U0=r, and choose an orthonormal decomposition of the nullspace into one-dimensional eigendirections e1,e2,e3,e4. By the dense sharp weighted-flag theorem, if the sharp exponent were 3/16 or 3/14, the reduced denominator of 2alpha forces exactly three distinct internal valuation levels w1<w2<w3<1, plus the terminal level w4=1. The complete exact harmonic-network enumeration (checkpoint 27) gives only these possibilities:

A: alpha=3/16, (w1,w2,w3)=(3/8,1/2,3/4), leading doubled weight w1.
B: alpha=3/16, (w1,w2,w3)=(1/4,3/8,1/2), leading doubled weight w2.
C: alpha=3/14, (w1,w2,w3)=(3/7,5/7,6/7), leading doubled weight w1.

The sharp extraction supplies **actual fixed matrices** G,A1,A2,A3 in K=ker L, where G has a nonzero support-to-e_t block (t=1 in A,C, t=2 in B), and Ai has a strictly positive e_i,e_i diagonal entry. In the old weights w0=0,w1,w2,w3,w4=1:
- every potentially nonzero (a,b) block of G satisfies w_a+w_b<=2alpha;
- every potentially nonzero (a,b) block of Ai satisfies w_a+w_b<=2w_i;
- the terminal PSD coefficient E44 occurs at residual order 1.
All blocks on U0 are assigned weight zero. No further sparse support assumption is made: **every** block allowed by these inequalities may be nonzero.

Since d=nu=4, every first exposing PSD stress has rank at most one. The universal primal–dual sharp-valuation alignment theorem (checkpoint 23) says its range lies in the terminal valuation block span(e4), which is one-dimensional. Thus after scaling the first stress is E44 in K-perp, and
   H44=0 for all H in K.
Put W3=U0+span(e1,e2,e3), K3=K intersect S(W3); later W2=U0+span(e1,e2), K2=K intersect S(W2).

## 2. A universal coefficient-deformation lemma

For any strictly ordered positive prospective null weights v1<v2<v3<v4=1, if every nonzero (a,b) block of each selected kernel coefficient H_e obeys
   v_a+v_b<=2e,
and each null weight v_i is achieved first by a coefficient whose e_i diagonal is positive, then the positive coefficient-rescaling lemma (Section 2 of the pinned weighted-flag memorandum) makes
   X(t)=X*+sum_e c_e t^e H_e+c_4 t E44
positive definite for sufficiently small t>0, with fixed positive constants c_e. Since all H_e lie in K and E44 does not, the residual is Theta(t). If the earliest coefficient G appears at p'<alpha and is nonzero, the displacement is Theta(t^p'), contradicting optimality of alpha.

For the nine cases below the necessary block inequalities are **verified for every original allowed block**, not only sparse parent edges. A complete self-contained exact rational audit is checkpoint 32. In each line take a small rational tau>0 (e.g. tau=1/1000). Notation (a,b,c) refers to the *original* three null weights, (a',b',c') to the changed weights, and the order list to (G,A1,A2,A3). The new extra kernel matrix H is inserted at the stated positive diagonal weight. A4=E44 remains at order 1.

### Case I: a kernel matrix in K3 with nonzero e3 diagonal

If some H in K3 has H33!=0, reverse its sign to make H33>0. For each of A,B,C define:

A: c'=c-tau, a'=c'/2, b'=b; orders (a'/2,a',b,c); H at c'.
B: c'=c-tau, a'=c'/2, b'=3c'/4; orders (b'/2,a',b',c); H at c'.
C: c'=c-tau, a'=c'/2, b'=(a'+1)/2; orders (a'/2,a',b',c); H at c'.

The new matrix H is supported on W3 and has positive e3 diagonal. Since c' is the largest null weight in W3, **all** its possible blocks satisfy the support order inequality at exponent c'. The original four modes satisfy the inequalities with their displayed new orders, even when they have *every* originally permitted dense block: this is a finite exact check of w_a+w_b<=2 old_order => v_a+v_b<=2 new_order for a,b in {0,...,4}. The other diagonal levels remain led by A1 and A2 (or by A2 and A1 in their ordered positions), while the terminal is E44. The leading exponent is p'=a'/2 or b'/2, strictly below old alpha. Thus no such H exists:
\[
\boxed{H_{33}=0\quad\text{for all }H\in K_3.}
\tag{2.1}
\]

The linear-algebra compression identity
  (K intersect S(W3))^\perp_{S(W3)} = P_W3 K^\perp P_W3
now shows that E33 is the compression of a full dual stress in K-perp. It is PSD on W3 and annihilates U0. We may therefore choose the *second* facial step to remove exactly e3. If any two-dimensional exposing step were available instead, d would already be at most three, so d=4 implies this choice leaves two further necessary steps.

### Case II: a kernel matrix in K2 with nonzero e2 diagonal

Suppose some H in K2 has H22!=0. Reverse sign so H22>0 and deform:

A: b'=b-tau, c'=(b'+1)/2, a'=c'/2; orders (a'/2,a',b,c'); H at b'.
B: b'=b-tau, a'=a, c'=c; orders (b'/2,a,b,c); H at b'.
C: b'=b-tau, c'=(b'+1)/2, a'=c'/2; orders (a'/2,a',b,c'); H at b'.

The new H is supported on W2 and b' is the largest weight in W2, so all its entries are permitted at order b'. The old A2 may be retained at its *old* order b; in A,C the old A3 is moved to c', maintaining its active original (e2,e4) order, and A1 moves to a'. All originally allowed dense blocks remain permitted by the displayed orders (verified exactly in checkpoint 32). Positive diagonal leading coefficients occur at a',b',c',1, and G moves to strictly earlier p'<alpha. This is a genuine PSD curve with residual Theta(t), contradicting sharpness. Therefore
\[
\boxed{H_{22}=0\quad\text{for all }H\in K_2.}
\tag{2.2}
\]
Hence E22 is the compression of a valid *third* exposing stress on W2. As d=4 is minimal, no PSD stress positive definite simultaneously on e1,e2 can exist at W2, or total depth would be three.

### Case III: minimal depth forces a nontrivial first-null kernel mode

Write on K2 the two real linear functionals f(H)=H11 and g(H)=H12. If f=c g on K2, then
  Z=E11-(c/2)F12+M E22
for any M>c²/4 is positive definite on span(e1,e2), annihilates U0 and belongs to K2-perp, because H22=0 on K2. The compression identity would make it a valid rank-two exposing stress at W2, giving total degree at most 3, contradiction.

Therefore f is NOT a multiple of g. There exists J in K2 with
\[
J_{11}>0,\qquad J_{12}=0,\qquad J_{22}=0.
\tag{2.3}
\]
(The last equality holds for every element of K2 by (2.2).) This J is supported on U0+e1+e2, and apart from support-block terms can have only source-to-e1, source-to-e2 and e1 diagonal entries. It can therefore be inserted at the earlier weight a' as follows:

A: a'=a-tau, b'=b, c'=c; orders (a'/2,a,b,c); J at a'.
B: a'=a-tau, b'=(a'+c)/2, c'=c; orders (b'/2,a,b',c); J at a'.
C: a'=a-tau, b'=(a'+1)/2, c'=(b'+1)/2; orders (a'/2,a,b',c'); J at a'.

For sufficiently small tau, in all three cases b'/2<=a', ensuring J's possible source-to-e2 entry is permitted; e1-e2 and e2 diagonal entries vanish by (2.3). The old A1 may be retained at its original order a, and in B,C the other modes are moved as indicated. Every originally allowed dense block is compatible with its moved coefficient order. The new leading exponent p'=a'/2 or b'/2 is strictly less than the proposed alpha. Coefficient rescaling again gives a positive definite curve of residual Theta(t). Contradiction.

This rules out all three potential sharp patterns A,B,C. Thus neither 3/16 nor 3/14 can occur when d=4.

## 3. Complete all-degree conclusion at nullity four, maximal degree

The previously established unconditional dense nullity-four spectrum and maximal-depth universal upper bound alpha<=1/4 (checkpoints 22 and 27) imply only nine reciprocal values plus the excluded 3/16,3/14 could occur. Checkpoint 26 constructs **all nine** reciprocals at exactly d=4. Hence the displayed spectrum in the theorem is both necessary and sufficient. QED.

## 4. Adversarial audit

1. **No assumption of a sparse original kernel:** The coefficient compatibility check is over *all* block pairs allowed by the original sharp weighted flag. The actual kernel can be arbitrarily dense, contain arbitrary additional basis directions, and have arbitrary target rank.
2. **First-stress alignment:** Since d=nu=4 its rank is one. Terminal valuation block is one-dimensional; alignment is forced. No simultaneous diagonalization of later stresses and the sharp flag is assumed.
3. **Face-compression lifting:** All compressed E33,E22 exposures lift to full stresses through the elementary annihilator identity; the full stress need not be PSD outside the active face.
4. **Three possibilities for obstruction:** Existence of any K3 matrix with H33!=0 produces Case I; otherwise E33 is exposable. Existence of any K2 matrix with H22!=0 produces Case II; otherwise E22 is exposable. Minimal degree then forces the J of Case III. This is exhaustive and makes no hidden genericity assumption.
5. **Full matrix PSD, not just 2x2 minors:** The coefficient-rescaling lemma produces positive definiteness by a diagonal normalized limit. Every exponent decrease is witnessed by an actual PSD recovery perturbation.
6. **Rational exactness:** The nine sets of support inequalities and positivity/order conditions have been checked with Fraction and the complete source is checkpoint 32. The finite check is fully specified in the theorem; it is not numerical evidence.
7. **Limit:** This proves the complete maximal-depth dense spectrum only at nu=4. A general induction for all nu and all facial depth profiles still requires new work. In particular no universal all-(n,r,d) closed arithmetic formula is claimed in this checkpoint.