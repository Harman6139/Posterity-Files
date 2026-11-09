# Exact stability of bounded non-singleton PSD feasible sets via a gauge and the canonical Dikin invariant

Research note — 7 November 2026. Self-contained reduction of bounded, non-singleton PSD feasibility error bounds to uniquely recoverable singleton problems. Combined with the universal Dikin–Hessian classifier, this gives an exact intrinsic sharp exponent for the set-distance modulus and preserves minimal facial-reduction degree.

## Theorem

Let \(\mathcal L:\mathbb S^n\to\mathbb R^m\) be linear, and let
\[
F=\{X\succeq0:\mathcal LX=b\}
\]
be nonempty and bounded (not necessarily a singleton). Choose \(X_0\in\operatorname{relint}F\) of maximum rank, let \(W=\operatorname{range}X_0\), and define the free feasible-direction subspace
\[
N=\ker\mathcal L\cap\mathbb S(W).
\]
Here \(\mathbb S(W)\) denotes symmetric matrices supported on \(W\). Let \(P_N\) be Frobenius orthogonal projection to \(N\). Set
\[
\widehat{\mathcal L}(H)=(\mathcal LH,P_NH).
\]
Then \(X_0\) is **uniquely recoverable** by \(\widehat{\mathcal L}\). The minimal facial-reduction singularity degree of the original set \(F\) is **equal** to that of the augmented singleton problem. The set-distance modulus
\[
\Omega(\delta)=\sup_{Y\succeq0,\;\|\mathcal LY-b\|\le\delta}
\operatorname{dist}(Y,F)
\]
and the unique-target modulus \(\widehat\omega\) for \((\widehat{\mathcal L},X_0)\) satisfy, for fixed \(\lambda\in(0,1)\), \(C>0\) and all sufficiently small \(\delta>0\),
\[
\boxed{\widehat\omega(\delta)\le\Omega(\delta)+\delta,
\qquad
\Omega(\delta)\le C\widehat\omega(\lambda\delta).}
\]
Thus \(\Omega\) and \(\widehat\omega\) have the **same sharp exponent**. Applying the universal Dikin–Hessian theorem to the canonical center \(\widehat X_\varepsilon\) and the restricted Hessian on \(\ker\widehat{\mathcal L}\) computes this exponent exactly from one algebraic curve, with full upper bounds and matching PSD competitors.

## Proof

**Affine span.** The support \(W\) of a relative-interior feasible matrix contains the range of every feasible \(X\in F\): if \(Z\in F\), then for sufficiently small \(t>0\), the relative-interior extrapolation \(X_0+t(X_0-Z)\in F\) is PSD, and evaluating on any vector in \(\ker X_0\) shows \(\ker X_0\subseteq\ker Z\). Thus every point of \(F\) is supported on \(W\). Conversely, since \(X_0|_W\succ0\), every \(H\in N\) has \(X_0\pm tH\in F\) for sufficiently small \(t\). Hence \(\operatorname{aff}F=X_0+N\). If \(\widehat{\mathcal L}Y=\widehat{\mathcal L}X_0\) with \(Y\succeq0\), then \(Y\in F\), so \(Y-X_0\in N\); also \(P_N(Y-X_0)=0\), so \(Y=X_0\). This proves singleton uniqueness.

**Modulus comparisons.** Put \(H=Y-X_0\) and \(e(Y)=\|P_{N^\perp}H\|_F\). Since \(\operatorname{aff}F=X_0+N\), \(e(Y)=\operatorname{dist}(Y,\operatorname{aff}F)\le\operatorname{dist}(Y,F)\). On all bounded residual sublevels \(\|P_NH\|\le M\) for some fixed \(M\), by boundedness of \(F\) and strict trace control (boundedness of all residual sublevels). Let \(\mu>0\) be the least eigenvalue of \(X_0|_W\).

The affine projection \(Z=X_0+P_NH\) is supported on \(W\) and satisfies \(Z\succeq-e(Y)P_W\) because \(Y=Z+P_{N^\perp}H\succeq0\). Set \(\theta=e(Y)/(\mu+e(Y))\), and \(Z'=(1-\theta)Z+\theta X_0=X_0+(1-\theta)P_NH\). Then \(Z'\succeq0\) and \(\mathcal LZ'=b\), so \(Z'\in F\), and
\[
\operatorname{dist}(Y,F)\le\|Y-Z'\|\le e(Y)+\theta M\le(1+M/\mu)e(Y).
\tag{1}
\]
For an augmented competitor with both \(\|\mathcal LH\|\le\delta\) and \(\|P_NH\|\le\delta\), its distance to \(X_0\) is at most \(e(Y)+\delta\le\operatorname{dist}(Y,F)+\delta\). Taking suprema gives \(\widehat\omega(\delta)\le\Omega(\delta)+\delta\).

Choose fixed \(\lambda\in(0,1)\) with \((1-\lambda)\mu\ge\lambda M\). For any original competitor \(Y\) define
\[
\widehat Y=X_0+\lambda P_{N^\perp}(Y-X_0)
=\lambda Y+(1-\lambda)X_0-\lambda P_N(Y-X_0).
\]
The last two terms together are PSD on \(W\), hence \(\widehat Y\succeq0\). Its original residual is \(\lambda\|\mathcal LH\|\le\lambda\delta\), and its gauge residual vanishes: \(P_N(\widehat Y-X_0)=0\). Also \(\|\widehat Y-X_0\|=\lambda e(Y)\). Thus \(\widehat\omega(\lambda\delta)\ge\lambda e(Y)\) for every original competitor. Combine with (1) and take suprema to get \(\Omega(\delta)\le(1+M/\mu)\lambda^{-1}\widehat\omega(\lambda\delta)\).

**Equality of minimal facial-reduction degrees.** At an intermediate face whose support \(V\) contains \(W\), an augmented exposing stress is \(Z=\mathcal L^*y+T\) with \(T\in N\), and its face compression \(P_V ZP_V\succeq0\) annihilates the relative-interior feasible matrix \(X_0\). Since \(X_0|_W\succ0\), positive semidefiniteness forces \(P_W ZP_W=0\). Because \(T\in N\) is supported on \(W\),
\[
0=\langle Z,T\rangle
=\langle\mathcal L^*y,T\rangle+\langle T,T\rangle
=\|T\|_F^2.
\]
Hence \(T=0\). Every augmented exposing step is already a valid original exposing step; conversely original stresses remain augmented stresses. Therefore both problems admit exactly the same facial-reduction chains and have the same minimal depth. QED.

## Limits

The boundedness assumption is essential for a finite global worst-case set-distance modulus (otherwise residual sublevels may be unbounded). The natural parameter for stability of a non-singleton set is distance to the entire set, not distance to one arbitrarily selected feasible point. A direct Dikin radius on the ungauged kernel would detect unrestricted motion inside the feasible set and would have exponent zero; removing the free subspace \(N\) is necessary.