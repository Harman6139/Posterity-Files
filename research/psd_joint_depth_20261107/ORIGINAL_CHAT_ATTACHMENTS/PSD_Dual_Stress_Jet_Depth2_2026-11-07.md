# Quadratic dual stress jets detect facial-reduction depth at most two

**Date:** 2026-11-07. This is a complete standalone finite-dimensional SDP statement and proof. It does **not** prove that arbitrary square-root stability has degree at most two.

## Statement

Let \(K\subset\mathbb S^n\) be a linear subspace with a uniquely feasible target \(X_*\succeq0\) of rank \(1\le r<n\), let \(U=\operatorname{range}X_*\), \(V=U^\perp\), and \(C=P_V\). Positive definite trace control \(W\in K^\perp\cap\mathbb S^n_{++}\) is automatic from uniqueness. Let \(d\) be the minimum number of SDP facial-reduction steps.

**Theorem.** The following two conditions are equivalent.

(1) \(d\le2\).

(2) There exist \(Z_0,Z_1\in K^\perp\), \(\lambda>0\), and \(\varepsilon>0\), with
\[
S(t)=Z_0+t(Z_1-C)+\lambda t^2W\succeq0\quad(0<t<\varepsilon),
\]
and
\[
\langle S(t),X_*\rangle=O(t^2)\quad(t\downarrow0).
\]
In fact the latter contact condition is equivalent to \(\langle Z_0,X_*\rangle=\langle Z_1,X_*\rangle=0\).

The existence of these matrices is an algebraic certificate: a symmetric quadratic polynomial matrix is PSD for sufficiently small positive \(t\) if and only if each principal minor is either identically zero or has positive first nonzero coefficient. Thus (2) is a finite semialgebraic condition on the same measurement kernel; it involves no recovery curves.

## Proof: (2) implies (1)

Let \(t\downarrow0\). Positivity gives \(Z_0\succeq0\). Since \(C X_*=0\) and the target contact is \(O(t^2)\), comparing coefficients gives \(\langle Z_0,X_*\rangle=\langle Z_1,X_*\rangle=0\).

If \(Z_0=0\), dividing the polynomial by \(t\) and letting \(t\downarrow0\) gives \(Z_1-C\succeq0\). Thus \(Z_1\succeq C\succeq0\), and it annihilates \(U\), so a single stress fully exposes \(V\) and \(d=1\).

Otherwise \(Z_0\) is a valid first exposing stress. Its kernel \(W_1=\ker Z_0\) contains \(U\). Compress \(S(t)\) to \(W_1\), divide by \(t\), and pass to zero:
\[
P_{W_1}(Z_1-C)P_{W_1}\succeq0.
\]
Since \(C=P_V\), and \(W_1=U\oplus(W_1\cap V)\), this means the compression of \(Z_1\) to \(W_1\) is PSD and at least the identity on its remaining null subspace \(W_1\cap V\). Because \(Z_1\in K^\perp\) and \(\langle Z_1,X_*\rangle=0\), it is a valid second exposing stress and its compression exposes the entire remaining null subspace. Hence \(d\le2\).

## Proof: (1) implies (2)

If \(d=1\), choose a stress \(Z_0\in K^\perp\), \(Z_0\succeq0\), \(Z_0X_*=0\), positive definite on \(V\). Set \(Z_1=0\). For sufficiently small \(t\), \(Z_0-tC\) remains PSD and strictly positive on \(V\), with zero restriction to \(U\). Adding \(\lambda t^2W\succ0\) keeps it PSD, and the target pairing is exactly \(\lambda t^2\langle W,X_*\rangle\).

If \(d=2\), select a first stress \(Z_0\in K^\perp\cap\mathbb S_+^n\) with kernel \(W_1\) containing \(U\), and a second stress \(\widetilde Z_1\in K^\perp\) annihilating \(X_*\), whose compression to \(W_1\) is PSD and positive definite on \(W_1\cap V\). Multiply \(\widetilde Z_1\) by a sufficiently large positive constant \(c\) and set \(Z_1=c\widetilde Z_1\), so
\[
L=P_{W_1}(Z_1-C)P_{W_1}\succeq0,
\]
with positive definite restriction to \(W_1\cap V\). The \(U\) rows of \(L\) vanish, since \(Z_1|_{W_1}\) is PSD and pairs to zero with the positive definite \(X_*|_U\), and \(C|_U=0\).

Decompose \(\mathbb R^n=R_0\oplus W_1\), where \(R_0=(\ker Z_0)^\perp\). Relative to this decomposition, the top-left block of \(S(t)\) is \(Z_0|_{R_0}+O(t)\succ0\), the off-diagonal is \(tB+O(t^2)\), and the lower block is \(tL+\lambda t^2W|_{W_1}\). Its Schur complement is
\[
tL+t^2\left(\lambda W|_{W_1}-B^*(Z_0|_{R_0})^{-1}B\right)+O(t^3).
\]
Choose \(\lambda\) so the expression in parentheses is positive definite. Since \(L\succeq0\), the Schur complement and hence \(S(t)\) are PSD for all sufficiently small positive \(t\). As the first two stresses annihilate \(X_*\), the contact is again \(\lambda t^2\langle W,X_*\rangle\). This proves (2).

## Why this sharpens the endpoint obstruction

For a singular uniquely recoverable target, a **square-root full-state recovery bound** gives support-function bounds \(h_C(\delta)=O(\sqrt\delta)\) for every fixed \(C\). Conic duality supplies some semialgebraic multiplier paths with such rates, but those paths may have fractional Puiseux exponents. If it were always possible, for \(C=P_V\), to replace such a multiplier path by the quadratic integer-power stress polynomial of (2), this theorem would imply
\[
\alpha=1/2\quad\Longrightarrow\quad d\le2.
\]
That **desingularization step is not proved** and is precisely where a proposed full all-degree classification remains open. It is important not to truncate fractional Puiseux terms blindly: the truncation can destroy PSD positivity or the requisite order of contact at \(X_*\).

The theorem itself gives a finite exact dual criterion for low singularity degree, and separates this certified geometric property from the unproved implication from a sharp recovery exponent.