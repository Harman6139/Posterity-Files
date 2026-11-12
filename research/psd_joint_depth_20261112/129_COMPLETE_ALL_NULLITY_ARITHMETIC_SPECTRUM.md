# Milestone 129 — Complete arithmetic classification at every nullity

**Date:** 2026-11-12. **Status:** complete research proof, not independently refereed; no bibliographic priority claim.

**Branch:** `research/psd-joint-depth-universal-20261107` in `Harman6139/Posterity-Files`.
**Predecessor snapshot:** `48bcfb75063cb8674f3505384cbcd5e8ddc8af75`.

The new ingredient is [milestone 128](128_ONE_SWITCH_EXACT_NULLITY_INTERPOLATION.md): every depth between the two canonical peeling bounds is attained at the original nullity. This manuscript gives the resulting exact spectrum, reconstructs the dense necessity proof, and provides a finite arithmetic formula for the smallest possible nullity. It does not rely on the computer-assisted catalogues through nullity seven.

## 1. The classification theorem

Let \(\mathcal L:\mathbb S^n\to\mathbb R^m\) be real linear, and suppose \(X_*\succeq0\) is the unique PSD matrix with measurements \(\mathcal L(X_*)\). Assume \(r=\operatorname{rank}X_*\ge1\), and put \(\nu=n-r\). Let \(d\) be the **minimum** number of facial-reduction steps needed to reach the face supported on \(\operatorname{range}X_*\). Define the full ambient recovery exponent by
\[
\omega(\delta):=\sup\{\|X-X_*\|_F:X\succeq0,\ \|\mathcal L(X-X_*)\|\le\delta\}
=\Theta(\delta^\alpha).
\tag{1}
\]
All norms on the finite-dimensional measurement space give the same exponent.

For a strict harmonic vector
\[
0=w_0<w_1<\cdots<w_{k-1}<w_k=1,
\quad 2w_i=w_{a_i}+w_{b_i},\quad 0\le a_i<i<b_i\le k,
\tag{2}
\]
define, for \(1\le j<k\),
\[
\ell_w(j)=\#\{1\le i<j:2w_i<w_{j+1}\},\qquad
u_w(j)=\min\{1\le i\le j:2w_i>w_j+w_{i-1}\}-1.
\tag{3}
\]
Let \(L(w)\) and \(U(w)\) count the transitions in the two chains beginning \(k\to k-1\), then iterating \(\ell_w\) and \(u_w\), respectively, until zero. For \(k=1\), both equal one.

**Theorem 129 (all-nullity joint spectrum).** For every fixed positive target rank \(r\):

1. If \(\nu=0\), the only pair is \((d,\alpha)=(0,1)\).
2. If \(\nu\ge1\), the Lipschitz exponent \(\alpha=1\) occurs exactly at \(d=1\).
3. If \(\nu\ge1\) and \(\alpha\ne1\), the tuple \((r+\nu,r,d,\alpha)\) is attainable **if and only if** there exist \(1\le k\le\nu\), ordered parents as in (2), and \(1\le v\le k\) such that
\[
\boxed{\quad \alpha=w_v/2\le w_1,\qquad L(w)\le d\le U(w).\quad}
\tag{4}
\]
Every attainable tuple has a rational realizing measurement map and a rank-\(r\) rational target. The criterion has no unknown real kernel, conic-feasibility test, quantifier elimination, asymptotic path search, or unbounded-dimensional auxiliary object.

The familiar necessary inequality \(\alpha\ge2^{-d}\) is automatic in (4), as proved below. All attainable exponents are rational. Criterion (4) classifies existence of tuples, not every possible rank-drop profile or every individual dense kernel.

## 2. A finite integer-only form

For each \(k\), put \(h=k-1\). Choose parents \(0\le a_i<i<b_i\le k\), and form the integer matrix and vector
\[
A_{ij}=2\mathbf1_{i=j}-\mathbf1_{a_i=j}-\mathbf1_{b_i=j},
\qquad c_i=\mathbf1_{b_i=k}\qquad(1\le i,j\le h).
\tag{5}
\]
Let
\[
Q=\det A,\qquad B_i=\det A[i\leftarrow c],\qquad B_0=0,\quad B_k=Q,
\tag{6}
\]
where \(A[i\leftarrow c]\) means replacement of column \(i\) by \(c\). Keep only choices with
\[
0<B_1<\cdots<B_{k-1}<Q.
\tag{7}
\]
The matrix is always nonsingular with \(Q>0\). To see this, write \(A=2(I-P)\), where \(P\) is the substochastic internal transition matrix of choosing either parent with probability one-half. Choosing the lower parent repeatedly reaches source zero in at most \(h\) steps with probability at least \(2^{-h}\). Thus \(\rho(P)<1\); continuity of \(\det(I-tP)\) for \(0\le t\le1\) shows its determinant is positive. Cramer's rule gives \(w_i=B_i/Q\). For \(h=0\), use the empty determinant \(Q=1\) and \(B_1=1\).

Compute \(L(B)\), \(U(B)\) by replacing every \(w_i\) in (3) by \(B_i\). There are exactly \(((k-1)!)^2\) parent choices. If \(\Sigma_{\nu,d}\) denotes the attainable exponent set at fixed nullity and degree, then for \(\nu\ge1\),
\[
\boxed{
\Sigma_{\nu,d}
=\{1:\ d=1\}
\ \cup\!
\bigcup_{k=1}^{\nu}
\left\{
\frac{B_v}{2Q}:
\begin{array}{l}
\text{(5)--(7) hold},\quad 1\le v\le k,\\
B_v\le2B_1,\quad L(B)\le d\le U(B)
\end{array}
\right\}.
}
\tag{8}
\]
This is the closed finite combinatorial/arithmetic spectrum. The number of parent choices may be large; no efficiency claim is part of the theorem. Unlike an instance-wise analytic classifier, formula (8) contains only explicitly bounded discrete choices, determinants of integer matrices, and integer comparisons.

## 3. Dense necessity: canonical fixed monomial coordinates

We give the argument for arbitrary dense real kernels. The analytic mechanisms correspond to milestones 09/10/89/91/122, but the load-bearing implications are included here.

Write \(K=\ker\mathcal L\). Uniqueness implies \(K\cap\mathbb S_+^n=\{0\}\). The finite-dimensional semidefinite separation alternative supplies \(W\succ0\) in \(K^\perp\). Consequently shifted PSD slices are bounded. For \(\epsilon>0\), let
\[
C_\epsilon=\arg\max\{\log\det X:X\succ0,\ X-X_*-\epsilon I\in K\}.
\tag{9}
\]
The slice contains \(X_*+\epsilon I\), and strict concavity and boundary divergence give a unique center. Stationarity gives \(C_\epsilon^{-1}\in K^\perp\), and
\[
n=\langle C_\epsilon^{-1},X_*\rangle+\epsilon\operatorname{tr}C_\epsilon^{-1},
\qquad C_\epsilon\succeq(\epsilon/n)I.
\tag{10}
\]
Boundedness and uniqueness imply \(C_\epsilon\to X_*\).

The equations defining the center become polynomial after using the adjugate in place of the inverse. Hence its graph is semialgebraic. The standard one-variable semialgebraic Puiseux theorem gives convergent expansions with rational exponents near \(\epsilon=0^+\).

Starting with \(U_0=\operatorname{range}X_*\), recursively take the range of the first nonzero positive coefficient of the compression to the remaining orthogonal complement. This produces a fixed orthogonal decomposition
\[
\mathbb R^n=U_0\oplus U_1\oplus\cdots\oplus U_k,
\quad 0=w_0<w_1<\cdots<w_k\le1,
\tag{11}
\]
with each \(U_i\ne0\). The leading diagonal coefficient on \(U_i\) at exponent \(w_i\) is positive definite. Since there are \(\nu\) null directions, \(k\le\nu\). PSD Cauchy--Schwarz gives the coefficient restriction
\[
P_{U_a}A_eP_{U_b}=0\quad\text{whenever }w_a+w_b>2e,
\tag{12}
\]
where \(C_\epsilon=X_*+\sum_{e>0}\epsilon^e A_e\). Coefficient comparison in the affine equation gives
\[
A_e\in K\quad(0<e<1),\qquad A_1-I\in K.
\tag{13}
\]

### 3.1 Finite coefficient rescaling

Suppose a finite generalized polynomial has positive definite first diagonal coefficients at distinct block orders \(w_i\), and obeys (12). Multiply its coefficient at exponent \(e\) by \(\exp(\sigma e^2)\). Normalize block \(i\) by \(\exp(-\sigma w_i^2/2)\epsilon^{-w_i/2}\). A surviving cross block can occur only at \(e=(w_a+w_b)/2\), and its multiplier is
\[
\exp[-\sigma(w_a-w_b)^2/4].
\tag{14}
\]
For large fixed \(\sigma\), all surviving cross blocks are small relative to the positive diagonal blocks. Higher-order terms vanish with \(\epsilon\). Thus the rescaled polynomial is positive definite for sufficiently small \(\epsilon\), with a uniform diagonal-power lower bound.

If \(w_k<1\), apply this to the center's truncation through \(w_k\). All nonconstant coefficients lie in \(K\), so it would be a positive definite exact feasible curve, contradicting uniqueness of singular \(X_*\). Therefore
\[
w_k=1.
\tag{15}
\]
Apply the same rescaling to the truncation through exponent one. It gives a positive definite family \(Y_\epsilon\) with residual \(O(\epsilon)\) and
\[
Y_\epsilon\succeq cD_\epsilon^2,
\qquad D_\epsilon=\bigoplus_i\epsilon^{w_i/2}I_{U_i}.
\tag{16}
\]

### 3.2 The universal maxdet envelope

Put \(Z_\epsilon=\epsilon C_\epsilon^{-1}\in K^\perp\). Equation (10) gives \(\operatorname{tr}Z_\epsilon\le n\) and \(\langle Z_\epsilon,X_*\rangle\le n\epsilon\). A fixed bounded right inverse for \(\mathcal L^*\) on \(K^\perp\) yields, for every PSD \(Y\) of residual at most \(\delta\),
\[
\operatorname{tr}(C_\epsilon^{-1}Y)\le n+C\delta/\epsilon,
\quad Y\preceq(n+C\delta/\epsilon)C_\epsilon.
\tag{17}
\]
Applying this to (16) proves the lower bound in
\[
\boxed{cD_\epsilon^2\preceq C_\epsilon\preceq CD_\epsilon^2.}
\tag{18}
\]
The upper bound follows by bounding the trace of the PSD normalized center using its diagonal blocks. Thus the chart uses a **fixed** orthogonal basis; no assumption about fixed eigenvectors was made.

## 4. Exact exponent and harmonic necessity

For nonzero \(K\), define its Dikin radius
\[
\rho_\epsilon=
\max\{\|H\|_F:H\in K,\ \|C_\epsilon^{-1/2}HC_\epsilon^{-1/2}\|_F\le1\}.
\]
Let \(q_0=\|\mathcal L(I)\|>0\). Then
\[
\omega(q_0\epsilon)=\Theta(\epsilon+\rho_\epsilon).
\tag{19}
\]
For the lower bound, both \(C_\epsilon\pm H/2\) are positive definite for a maximizing normalized direction \(H\), have residual \(q_0\epsilon\), and at least one is at distance at least \(\|H\|_F/2\) from \(X_*\). The competitor \(X_*+\epsilon I\) also gives an \(\Omega(\epsilon)\) bound.

For the upper bound, given any PSD competitor of residual \(O(\epsilon)\), write \(X-X_*=H+E\), where \(H\in K\) and \(\|E\|_F=O(\epsilon)\), using a fixed right inverse. The whitened \(H\) has trace zero by stationarity. It is bounded below by a constant multiple of \(-I\): use (10), \(X\succeq0\), and \(\operatorname{tr}(C_\epsilon^{-1}X_*)\le n\). Trace zero then bounds it above as well. Its Frobenius norm is uniformly bounded, so \(\|H\|_F=O(\rho_\epsilon)\). This proves (19) for all ambient competitors.

Using (18), the squared Dikin norm is comparable to
\[
\sum_{a,b}|H_{ab}|^2\epsilon^{-(w_a+w_b)}.
\]
In this expression each coordinate index is assigned the weight of its grade. Define
\[
\tau=\min_{0\ne H\in K}\max_{H_{ab}\ne0}\frac{w_a+w_b}{2}.
\tag{20}
\]
There are finitely many possible support thresholds. Projection from \(K\) to entries of weight at least \(\tau\) is injective, while some nonzero \(H\) has no entries of weight larger than \(\tau\). These two finite-dimensional facts give
\[
\rho_\epsilon=\Theta(\epsilon^\tau),\qquad \alpha=\min(1,\tau).
\tag{21}
\]
If \(K=0\), the exponent is one.

### 4.1 Every internal grade is a harmonic midpoint

For \(i<k\), the actual coefficient \(H_i=A_{w_i}\in K\) has positive definite \(U_i\)-compression and satisfies (12). The matrices
\[
W_\epsilon=D_\epsilon C_\epsilon^{-1}D_\epsilon
\]
are uniformly bounded and uniformly positive definite by (18). Along a subsequence they converge to \(W\succ0\). The scaled fixed kernel direction
\[
\epsilon^{w_i}D_\epsilon^{-1}H_iD_\epsilon^{-1}
\]
converges to its weight-\(w_i\) homogeneous part, and its pairing with \(W_\epsilon\) is zero by stationarity.

If \(H_i\) had no nonzero block between grades \(a<i<b\) with \(w_a+w_b=2w_i\), that homogeneous part would be exactly its nonzero positive definite \(U_i\) diagonal block, extended by zero. Its pairing with \(W\succ0\) would be strictly positive, a contradiction. Thus genuine midpoint parents exist for every internal grade, even with multidimensional grades.

### 4.2 The sharp exponent is an admissible half-weight

For \(k\ge2\), \(H_1\) in (20) has threshold \(w_1\), so \(\alpha\le w_1\). If equality holds, the midpoint relation at the lowest grade has lower parent zero and gives \(w_v=2w_1\). If \(\alpha<w_1\), a minimizing kernel direction in (20) has no null--null entry. It cannot be supported entirely in \(U_0\), since uniqueness implies \(K\cap\mathbb S(U_0)=0\). Its largest support-to-null weight is therefore \(w_v/2=\alpha\). This proves (3) of milestone 128's input requirements.

For \(k=1\), the only entry weights are \(0,1/2,1\), and weight zero alone is excluded by source uniqueness. Hence \(\alpha\in\{1/2,1\}\).

## 5. Dense necessity of both facial-depth bounds

A valid ambient stress is \(Z\in K^\perp\) with \(\langle Z,X_*\rangle=0\) and PSD compression to the current face. Its compression annihilates \(U_0\). Put \(V_j=U_0\oplus\cdots\oplus U_j\).

### 5.1 Lower bound for arbitrary, possibly rotated chains

At the first step, successively pair a PSD stress with \(H_i=A_{w_i}\), \(i=1,\ldots,k-1\). Once lower rows vanish, (12) leaves only the positive definite \(U_i\) diagonal pairing. This forces the \(U_i\) row to vanish. Therefore every first surviving face contains \(V_{k-1}\).

More generally, suppose the current face contains \(V_j\). If \(i\le\ell_w(j)\), then \(2w_i<w_{j+1}\), so (12) implies that \(H_i\) is supported entirely in \(V_j\). Its pairing is therefore determined by the current PSD compression even if the remaining face is not coordinate aligned. Successive row-zero arguments force every such \(U_i\) to survive. The next face contains \(V_{\ell_w(j)}\).

Following the lower recurrence proves
\[
d\ge L(w)
\tag{22}
\]
for every facial-reduction chain, including chains with rotated subspaces.

### 5.2 Upper bound by genuine ambient dual coefficients

The dual center \(Z_\epsilon=\epsilon C_\epsilon^{-1}\in K^\perp\) is PSD and has a Puiseux expansion. Its diagonal grade \(U_i\) has positive definite leading coefficient at order \(1-w_i\), and its \((a,b)\) block has order at least
\[
1-(w_a+w_b)/2.
\tag{23}
\]
All coefficient matrices belong to \(K^\perp\). Those at exponents below one also pair to zero with \(X_*\), because \(\langle Z_\epsilon,X_*\rangle=O(\epsilon)\).

The order-zero coefficient exposes precisely \(U_k\). At a subsequent prefix \(V_j\), let \(p=u_w(j)+1\) and truncate the dual series through exponent \(1-w_p\). Since
\[
2w_p>w_j+w_{p-1},
\]
every block touching a grade below \(p\), within \(V_j\), has order strictly greater than the truncation threshold. The compression is supported on \(U_p\oplus\cdots\oplus U_j\), and includes its positive definite leading diagonal coefficients.

Apply the finite coefficient-rescaling argument of Section 3.1, now to the dual orders \(1-w_i\). For a sufficiently small positive parameter the resulting finite sum is a legitimate **ambient** member of \(K^\perp\), still orthogonal to \(X_*\), with compression positive definite exactly on this suffix. No zero-extension of a compressed stress is being assumed. Iterate the upper recurrence to obtain
\[
d\le U(w).
\tag{24}
\]
Equations (2), (21)--(24), and \(k\le\nu\) prove the full dense necessity in Theorem 129.

## 6. Sufficiency, padding, and boundary cases

For any certificate in (4), milestone 128 constructs a rank-one instance at nullity exactly \(k\) with the specified exponent and minimum degree. Fully measure all extra coordinates and all cross entries when adding a positive support block of size \(r-1\), or adding \(\nu-k\) null coordinates. The added null coordinates are exposed with the first maximal stress. On the old coordinates, the maximal stress cones and subsequent greedy chain are unchanged. Thus padding preserves \(d\) and \(\alpha\). The same conclusion for the global modulus follows by restriction to the old principal block and the \(O(\delta)\) control on all added entries.

If \(\nu=0\), \(X_*\) is positive definite, so every nonzero kernel direction would give another feasible PSD matrix for small displacement. Thus \(K=0\), \(\alpha=1\), and \(d=0\). For \(\nu\ge1\), injective measurements realize \((d,\alpha)=(1,1)\). Conversely \(\alpha=1\) forces \(k=1\) by Section 4.2, hence \(d\le U(w)=1\). This proves all parts of Theorem 129.

For completeness, when the target has rank zero and \(n\ge1\), uniqueness gives a positive definite stress in \(K^\perp\). Pairing it with any PSD competitor bounds its norm by a constant times the measurement residual. Thus the only possibility is \((d,\alpha)=(1,1)\); it is attained by injective measurements.

### 6.1 The dyadic inequality is redundant

In the lower chain, the smallest weight in the first removed layer is one. At each subsequent layer, its smallest weight is at least half the smallest weight removed in the preceding layer. This is exactly the definition of \(\ell_w\), including the top vertex of a prefix, for which harmonicity gives \(2w_j\ge w_{j+1}\). Therefore
\[
w_1\ge2^{1-L(w)}.
\]
Every admissible half-weight satisfies
\[
\alpha=w_v/2\ge w_1/2\ge2^{-L(w)}\ge2^{-d}.
\tag{25}
\]
Thus no separate error-bound filter is needed in the arithmetic formula.

### 6.2 Dimension-free attainable degrees and exponents

Allowing arbitrary finite nullity, the exact spectra are
\[
\begin{array}{ll}
d=1:&\{1,1/2\},\\
d=2:&\mathbb Q\cap[1/4,1/2],\\
d\ge3:&\mathbb Q\cap[2^{-d},1/2).
\end{array}
\tag{26}
\]
Necessity follows from the theorem and (25). In particular, \(\alpha=1/2\) with \(k\ge2\) forces \(w_1=1/2\); since \(w_{k-1}<1\), the upper rule removes all internal grades after the terminal, so \(d\le2\). Sufficiency and an explicit finite dimension bound follow in the next section. Formula (26) was already a projection result in the predecessor work; the new result is the exact fixed-nullity formula (8).

## 7. Exact minimum nullity as a bounded arithmetic formula

For fixed \(d\) and \(\alpha\), write \(\mathcal A_k(d,\alpha)\) for the entirely integer predicate in the braces in (8), with equality \(\alpha=B_v/(2Q)\). For rational \(0<\alpha=p/q<1/2\) in lowest terms and an admissible degree in (26), define
\[
N(d,q)=
\begin{cases}
q+1,&d=2,\\
d+1+q\bigl((d+2)2^{d-3}-1\bigr),&d\ge3.
\end{cases}
\tag{27}
\]
Then the exact minimum nullity and matrix order are
\[
\boxed{
\nu_{\min}(d,\alpha)=
\min\{1\le k\le N(d,q):\mathcal A_k(d,\alpha)\},
\qquad n_{\min}(r,d,\alpha)=r+\nu_{\min}(d,\alpha).
}
\tag{28}
\]
The finite set is nonempty. Each \(\mathcal A_k\) has only \(((k-1)!)^2\) parent choices and at most \(k\) distinguished vertices. Thus (28) is a bounded arithmetic minimum, not an open-ended search over real problems. It is not asserted to simplify to an elementary expression involving only the numerator and denominator.

Exceptional minima are
\[
\nu_{\min}(0,1)=0,\quad
\nu_{\min}(1,1)=\nu_{\min}(1,1/2)=1,\quad
\nu_{\min}(2,1/2)=2.
\tag{29}
\]
For all other pairs excluded by (26), no finite realization exists.

### 7.1 Proof of the explicit finite bound

We spell out the unrestricted-dimension construction underlying the bound; it is the mechanism of predecessor milestone 02, not the new interpolation theorem.

Choose \(e\ge2\) so that \(2^{-e}\le\alpha<2^{-(e-1)}\), and put \(c=2^{-(e-1)}\). Then \(e\le d\). Form a dyadic spine with positive weights \(c,2c,\ldots,1\), each nonterminal spine vertex having parents zero and the next doubled weight. Write
\[
\frac{2\alpha-c}{1-c}=a/b
\]
in lowest terms, taking \(b=1\) for zero. Add the affine grid \(c+j(1-c)/b\), \(1\le j<b\), with adjacent grid parents; at coincidences retain the spine vertex and its spine parents. The denominator satisfies \(b\le q(2^{e-1}-1)\). Add the unused source-to-\(2\alpha\) leading edge. The minimum exponent is \(\alpha\), and the exact depth is \(e\): the spine cannot peel sooner, while all remaining grid vertices can join the final spine layer. Its nullity is at most
\[
e+b-1\le d+q(2^{d-1}-1)-1.
\tag{30}
\]
The global PSD estimate and the matching positive curve follow from the single-main-edge special case of the maximum principle and diagonal normalization in milestone 128. Exact peeling follows from the same source-row and positive stress arguments.

For \(d\ge3\), put \(s=d-3\), \(\rho=2^s/(2^s+1)\), and \(m=2^s q\). Define
\[
a_*=(1-\rho^m)/(2-\rho^m),\qquad
x_i=1-\rho^i(1-a_*),\quad 0\le i\le m.
\]
Then \(x_0=a_*\), \(x_m=2a_*\). Introduce a root of weight \(a_*\), cores \(X_i\) of weights \(x_i\), and a terminal of weight one. The root parents are zero and \(X_m\). For \(s=0\), the parents of \(X_i\) are \(X_{i-1}\) and the terminal. For \(s\ge1\), add vertices
\[
y_{i,j}=x_i+2^{-(s-j+1)}(1-x_i),\quad 1\le j\le s.
\]
The parents of \(X_i\) are \(X_{i-1},Y_{i,1}\); the parents of \(Y_{i,j}\) are \(X_i,Y_{i,j+1}\), with the terminal replacing \(Y_{i,s+1}\). All are exact midpoint identities. Distinct named coordinates may be retained even if scalar weights happen to agree; all physical parent edges are distinct.

The exact layers are the terminal, the \(s\) successive \(Y\)-levels in reverse order, all cores, and the root. Thus its minimum degree is \(d\), and its exponent is \(a_*\). At each earlier step, the active lower-parent chain blocks every later layer; positive diagonal-normalized stresses expose exactly the stated layer. Its nullity is \(m(d-2)+2\).

Bernoulli's inequality gives
\[
\rho^m\le\frac1{q+1}<\frac{q-2p}{q-p},
\]
so \(a_*>\alpha\). Glue this helper and the base system at their source, keeping all other coordinates distinct and choosing the common offdiagonal coefficient small. Their exponent is the minimum \(\alpha\), and their depth is the maximum \(d\), since the source row vanishes and the exposing equations separate by component. Their combined nullity is at most the second line of (27). For \(d=2\), the base construction alone has nullity at most \(q+1\).

Applying the dense necessity theorem to these finite explicit instances gives a strict harmonic certificate with at most \(N(d,q)\) grades. This proves that (28) is a genuinely bounded exact formula.

## 8. Relation to the two handoff routes

The one-switch construction resolves Route A by selecting a compatible schedule rather than attempting to realize every prefix schedule. Main-edge collisions are absorbed into positive multi-child owners, and every such owner is synchronized with its actual exposing layer. Source releases share edges only in a triangular way; the final half-weight collision has an explicit repaired stress.

For Route B, no claim is made that every signed conic-matroid tower can be reduced to rank data. That stronger instance-wise reduction is unnecessary for the tuple spectrum: the explicit construction supplies a rational realization for every necessary arithmetic certificate. Consequently the existential real-kernel and conic-feasibility variables in milestone 120 can be eliminated **for the projected tuple-existence question**. The face-level Gordan criterion of milestone 127 and its forbidden schedules remain valid.

## 9. Provenance and verification scope

The canonical center, Loewner envelope, Dikin radius, harmonic necessity, and dense peeling bounds were developed in the predecessor milestones. Their relevant proofs have been reconstructed above. The genuinely new uniform constructive ingredient is milestone 128's one-switch schedule and synchronized blocker ownership. The old small-nullity enumerations and their claimed counts are not premises of either proof.

Classical background includes J. F. Sturm, *Error Bounds for Linear Matrix Inequalities*, SIAM J. Optim. 10(4), 1228--1248 (2000), DOI 10.1137/S1052623498338606; and S. Sremac, H. J. Woerdeman, H. Wolkowicz, *Error Bounds and Singularity Degree in Semidefinite Programming*, SIAM J. Optim. 31(1), 812--836 (2021), DOI 10.1137/19M1289327. The present proof does not claim novelty for facial reduction, analytic centers, semialgebraic Puiseux expansions, or Dikin ellipsoids. An independent specialist proof audit and a full priority review remain appropriate before submission.
