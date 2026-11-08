# Milestone 95 — UNIVERSAL DENSE dual-center threshold: central valuation minimum 1/2 forces facial degree <= 2

**2026-11-08. PROVED FOR EVERY dense uniquely solvable real PSD inverse problem, conditional only on the independently established universal fixed monomial maxdet chart (checkpoint 89) and standard finite PSD coefficient balancing.** No sparse-midpoint or game-representation assumption is used. The proof supplies an explicit second exposing stress formed by finitely many Puiseux coefficients of the original *dual* central path. This is a new clean necessity mechanism for the all-degree joint spectrum.

## Theorem (strong version)

Let \(X_*\succeq0\) be uniquely recovered by \(L:\mathbb S^n\to\mathbb R^m\) and have positive rank. Let
\[
\mathbb R^n=U_0\oplus U_1\oplus\cdots\oplus U_k,\qquad
U_0=\operatorname{range}X_*,
\quad0=w_0<w_1<\cdots<w_k=1
\]
be the **fixed orthogonal monomial valuation decomposition** of the shifted maximum-determinant center (checkpoint 89). If \(k\ge2\) and
\[
\boxed{2w_1>w_{k-1},}
\tag{95.1}
\]
then the minimal PSD facial-reduction degree obeys
\[
\boxed{d\le2.}
\tag{95.2}
\]
For \(k=1\), the first stress already exposes the full target nullspace, so \(d=1\).

In particular, because \(w_{k-1}<1\),
\[
\boxed{w_1\ge\frac12\quad\Longrightarrow\quad d\le2.}
\tag{95.3}
\]
Equivalently **every** dense PSD inverse problem with \(d\ge3\) has a canonical center valuation block with \(w_1<1/2\). This is a structural strengthening of the previously proved strict square-root instability gap: it is a statement about the *entire canonical center quadratic-form filtration*, not solely the scalar exponent.

## Proof

The canonical shifted center \(C_\epsilon\) is positive definite with
\[
C_\epsilon = D_\epsilon M_\epsilon D_\epsilon,
\qquad D_\epsilon=\bigoplus_{i=0}^k\epsilon^{w_i/2}I_{U_i},
\qquad M_\epsilon\longrightarrow M_0\succ0
\]
and \(Z_\epsilon=\epsilon C_\epsilon^{-1}\in K^\perp\cap\mathbb S_+^n\) for \(K=\ker L\). In the fixed orthogonal frame,
\[
Z_\epsilon=\epsilon D_\epsilon^{-1}M_\epsilon^{-1}D_\epsilon^{-1}.
\tag{95.4}
\]
The normalized dual \(M_\epsilon^{-1}\) has a positive-definite finite limit and a convergent Puiseux series; every coefficient of \(Z_\epsilon\) lies in \(K^\perp\), because \(K^\perp\) is a fixed linear subspace.

**First exposing step.** The constant term \(Z_0=\lim_{\epsilon\to0}Z_\epsilon\) is PSD, supported exactly on the terminal grade \(U_k\), and PD there. By comparing \(\langle Z,C_\epsilon\rangle=\epsilon\operatorname{tr}Z\) for arbitrary globally PSD first stresses \(Z\in K^\perp\) with the lower chart \(C_\epsilon\succeq cD_\epsilon^2\), every first stress has range contained in \(U_k\). Hence the maximal first exposed face is
\[
W=U_0\oplus U_1\oplus\cdots\oplus U_{k-1}.
\]

**Construct a full-rank second compressed stress.** Compress \(Z_\epsilon\) to \(W\), writing \(S_\epsilon=P_WZ_\epsilon P_W\). It is PSD for all \(\epsilon>0\). On each internal positive grade \(U_i\), \(1\le i\le k-1\), the first nonzero diagonal block occurs at exponent
\[
v_i=1-w_i
\]
and is exactly \(P_{U_i}M_0^{-1}P_{U_i}\succ0\). Every cross block \(U_i\times U_j\) has valuation at least \((v_i+v_j)/2\), by PSD Cauchy–Schwarz (or directly from (95.4)).

The *largest required internal diagonal order* is
\[
E=1-w_1,
\]
whereas the *smallest possible source-to-internal cross-block order* is at least
\[
1-\frac{w_{k-1}}2.
\]
The strict hypothesis \(2w_1>w_{k-1}\) gives
\[
E<1-\frac{w_{k-1}}2.
\]
Consequently, **every coefficient of the Puiseux expansion of \(S_\epsilon\) through order \(E\) has ZERO \(U_0\) row/column**, while it includes positive-definite first diagonal coefficients on **all** internal grades \(U_1,\ldots,U_{k-1}\). The first source diagonal appears only at exponent one and is also absent from this truncation.

Let \(S_\epsilon=\sum_e\epsilon^eS_e\) be its Puiseux series (all \(S_e=P_WZ_eP_W\), \(Z_e\in K^\perp\)). Form the finite generalized polynomial
\[
T_\sigma(t)=\sum_{0\le e\le E}e^{\sigma e^2}t^eS_e.
\tag{95.5}
\]
It is a compression of a linear combination of the **original dual measurement stresses**, hence is valid for facial reduction on \(W\). All its source rows vanish exactly. On \(V=U_1\oplus\cdots\oplus U_{k-1}\), every coefficient satisfies the PSD order restriction \(2e\ge v_i+v_j\) whenever its \((i,j)\)-block is nonzero; each first diagonal coefficient at \(v_i\) is PD. The finite coefficient-rescaling lemma therefore makes \(T_\sigma(t)|_V\succ0\) for all sufficiently small \(t>0\), after choosing one fixed large \(\sigma\). On \(U_0\) and its cross blocks the matrix vanishes, so \(T_\sigma(t)\succeq0\) on the ENTIRE reduced face \(W\), is PD on \(V\) and annihilates \(X_*\).

Choose one small fixed real \(t>0\). This gives a SINGLE legitimate ambient dual stress with PSD compression exposing **all remaining null directions at once**. Thus after the first stress exposing \(U_k\), one more stress reaches \(U_0\), proving \(d\le2\). QED.

## Consequences and exact scope

1. If \(w_1=1/2\), then automatically \(d\le2\), regardless of the number and multiplicities of later grades. This is the case needed to exclude four high-exponent candidates at target nullity five and degree three (see checkpoint 97).
2. For every \(d\ge3\), \(w_1<1/2\); the leading exponent is \(\alpha\le w_1\), hence \(\alpha<1/2\), recovering the strict high-depth separation via an independent **DUAL** proof.
3. The theorem is stronger than exponent-only rigidity: it states the geometric position of the entire first exposing stress and the existence of a full-rank second stress from a finite dual Puiseux jet.
4. It does NOT prove that every lower weight profile has degree at least three, nor that all nonmaximal exponent/degree pairs are representable by a tied-edge game. It is a NECESSARY dense compatibility condition and a powerful finite-enumeration pruning rule.

## Literature and audit

Facial reduction, Puiseux expansions and Gordan–Stiemke alternatives are classical. This short dual-truncation proof is self-contained given checkpoint 89's maxdet monomial chart; bibliographic priority is not claimed. Strict inequality in (95.1) is essential to ensure no source cross block survives the truncation. The proof makes no arbitrary assumption of coordinate sparsity or diagonal dual stresses.