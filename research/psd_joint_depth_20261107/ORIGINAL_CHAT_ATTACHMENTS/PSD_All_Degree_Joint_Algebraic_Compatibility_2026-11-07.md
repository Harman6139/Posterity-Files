# All-degree joint exponent–facial-depth compatibility: a canonical finite algebraic test

Research note — 7 November 2026. This is an **exact decision theorem** for every fixed matrix size, target rank, singularity degree and proposed rational exponent. It does not need midpoint-network realizations or the earlier weighted-flag classifier. The PSD-specific reduction is the independently proved universal Dikin–Hessian theorem. Standard real-algebraic quantifier elimination performs the last (possibly expensive) decision step; novelty is not attributed to quantifier elimination itself.

## Theorem

Fix integers \(n\ge2\), \(1\le r<n\), \(1\le d\le n-r\), and rational \(0<\alpha\le1\). There is a finite, explicitly constructible first-order formula over real closed fields whose truth is **equivalent** to existence of some linear measurement map \(\mathcal L:\mathbb S^n\to\mathbb R^m\) (for some finite \(m\)), a uniquely recoverable PSD target \(X_*\) of rank \(r\), whose *minimal* facial-reduction degree is exactly \(d\) and whose optimal full Frobenius stability exponent equals \(\alpha\). Every coefficient of the formula is rational. The formula contains no quantified arbitrary recovery curves.

When true, real-algebraic sample coefficients yield a finite-dimensional realizing map. When false, its infeasibility is a finite exact impossibility proof. All possible triples have therefore a complete *algorithmic* joint compatibility classification; a short closed arithmetic list for every \((n,r,d)\) is a separate, not established, refinement.

## Construction of the finite formula

1. **Fix the target by support congruence.** Set \(X_*=\operatorname{diag}(I_r,0_{n-r})\), and put \(N=n(n+1)/2\). Parameterize an arbitrary kernel \(K\subseteq\mathbb S^n\) by a real \(N\times N\) orthogonal projector \(\Pi\) satisfying \(\Pi^\top=\Pi=\Pi^2\). The measurement map can be taken to be the orthogonal projector \(I-\Pi\) onto \(K^\perp\). Fix its rank \(k=\operatorname{tr}\Pi\) in a finite disjunction over \(k=0,\ldots,N\).

2. **Enforce uniqueness (polynomial first-order).** Require that the only \(Y\succeq0\) with \(Y-X_*\in\operatorname{range}\Pi\) is \(X_*\). This is a first-order formula using principal-minor inequalities, quantified over a finite \(N\)-tuple \(Y\). Consequently \(K\cap\mathbb S^n_+=\{0\}\), so the canonical center exists for every \(\varepsilon>0\).

3. **Enforce exact facial-reduction degree.** A length-\(j\) facial-reduction chain is encoded by a finite sequence of orthogonal face projectors \(P_0=I,P_1,\ldots,P_j=P_U\) and exposing stresses \(Z_i\in K^\perp\), each with \(S_i=P_{i-1}Z_iP_{i-1}\succeq0\) and \(P_i\) the projector onto \(\ker(S_i)\cap\operatorname{range}(P_{i-1})\). The latter is encoded by
\[
P_iP_{i-1}=P_i,\quad P_i^2=P_i=P_i^\top,\quad S_i P_i=0,\quad S_i+P_i+(I-P_{i-1})\succ0,
\]
with strict rank drops \(\operatorname{tr}P_i<\operatorname{tr}P_{i-1}\), target inclusion \(P_iP_U=P_U\), and \(\Pi Z_i=0\). All are polynomial matrix equalities/positivity. Exact degree \(d\) means **there exists** a length-\(d\) valid chain and **no** valid chain of any shorter length (finite disjunction \(j<d\)). Uniqueness ensures such chains are available, and the definition exactly expresses minimal facial-reduction degree.

4. **An orthonormal kernel basis.** Choose symmetric matrices \(H_1,\ldots,H_k\) with \(\Pi H_i=H_i\) and \(\langle H_i,H_j\rangle=\delta_{ij}\). Dimension \(k=\mathrm{tr}\Pi\) ensures they span \(K\). For any \(X\succ0\) define the polynomial matrix
\[
A_{ij}(X)=\operatorname{tr}(\operatorname{adj}(X)H_i\operatorname{adj}(X)H_j),
\]
its positive denominator \(D(X)=\det A(X)\), and numerator \(N(X)=(\det X)^2 e_{k-1}(A(X))\) for \(k\ge1\). The universal Dikin–Hessian theorem and its determinant-ratio corollary establish
\[
\omega(\varepsilon\|\mathcal LI\|)\asymp\varepsilon+\sqrt{N(X_\varepsilon)/D(X_\varepsilon)},
\]
where \(X_\varepsilon\) is the unique positive-definite solution of the polynomial stationarity conditions
\[
\Pi(X-X_*-\varepsilon I)=X-X_*-\varepsilon I,
\quad\Pi(\operatorname{adj}X)=0,
\quad X\succ0.
\]
Here \(\Pi\) acts on \(\mathbb S^n\) in Frobenius coordinates.

5. **Exact exponent as an explicit polynomial first-order predicate.** Let \(\alpha=a/b\in(0,1)\) be reduced. Require existence of real constants \(c,C,\eta>0\) such that for every \(t\) satisfying \(0<t<\eta\), there exists a matrix \(X\succ0\) satisfying the central equations at \(\varepsilon=t^b\) and
\[
\boxed{c\,t^{2a}D(X)\le N(X)\le C\,t^{2a}D(X).}
\]
This is equivalent to \(\sqrt{N(X_\varepsilon)/D(X_\varepsilon)}\asymp\varepsilon^\alpha\). Since \(\alpha<1\), the residual term \(\varepsilon\) is negligible, and the universal modulus formula makes this **necessary and sufficient for the exact optimal recovery exponent to equal \(\alpha\)**. For \(\alpha=1\), require only \(N(X_\varepsilon)\le C\varepsilon^2D(X_\varepsilon)\) for all sufficiently small \(\varepsilon\) (or \(k=0\)). The universal modulus is always at least a constant times \(\varepsilon\), so this is necessary and sufficient for exponent one.

All quantifiers range over finitely many real matrix entries and real scalars; all constraints are polynomial equalities and inequalities, with integer exponents \(a,b\). First-order real-closed-field quantifier elimination therefore terminates and decides existence.

## Why this is a structural classification rather than merely unrestricted quantifier elimination

The finite algebraic formula does **not** re-quantify the original family of PSD competitors at every residual, nor a continuum of candidate sharp recovery curves. Its rate predicate uses only (i) the **unique** max-determinant solution of a fixed-degree polynomial central system; (ii) one polynomial determinant quotient of its logdet-Hessian Gram matrix on \(K\); and (iii) finite facial stress chains. The difficult PSD stability analysis is condensed into the proved two-sided uniform Dikin-modulus theorem. Quantifier elimination is only a final verification mechanism, and its use in real algebraic geometry is not claimed novel.

## Limitations

This proves a necessary-and-sufficient **terminating algorithm** for membership of any proposed rational \(\alpha\) in every prescribed joint spectrum \(\Sigma_{n,r,d}\). Producing a particularly simple, explicit, arithmetic list of those spectra without solving large real-algebraic problems remains open. The criterion alone neither proves nor refutes sparse midpoint depth-preservation, and does not settle the isolated conjecture of exponent exactly \(1/2\) at depth at least three without running the test for each fixed finite dimension.