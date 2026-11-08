# Universal canonical maximum-determinant Loewner envelope for PSD inverse problems

**2026-11-07. Fully proved.** Covers every nonempty bounded PSD measurement fibre, including nonsingleton feasible sets, arbitrary dense maps, and all ambient PSD competitors. Does not assert full Frobenius exponent determined by this center alone; no bibliographic novelty/priority claim for analytic-center machinery.

## Theorem
Let L:S^n -> R^m be linear and F={X>=0:LX=b} nonempty and bounded. Choose X0 in F and K=ker L. For epsilon>0 uniquely maximize log(det X) over X>0 with X-X0-epsilon I in K, writing its maximizer X_epsilon. Let q=||L I||>0. Choose a bounded linear right inverse R:K^perp -> R^m for L*, and kappa=||R||.

Then X_epsilon is the unique solution of
    X-X0-epsilon I in K, X>0, X^{-1} in K^perp.
For EVERY delta>=0 and EVERY PSD Y with ||L Y-b||<=delta:
    0 <= Y <= n(1+kappa delta/epsilon) X_epsilon                  (Loewner order).

In particular X_epsilon belongs to R_{q epsilon}, the PSD residual sublevel, and
    X_epsilon in R_{q epsilon} subset {Y:0<=Y<=n(1+kappa q)X_epsilon}.
For all PSD observables C>=0, simultaneously,
    <C,X_epsilon> <= sup_{Y in R_{q epsilon}} <C,Y>
                     <= n(1+kappa q) <C,X_epsilon>.
The constant is independent of epsilon and C.

## Self-contained proof
Boundedness of F implies K intersect PSD={0} (otherwise X0+tH belongs to F for any t>=0). Strict separation of zero from L({H>=0:tr H=1}) produces W>0 in K^perp. Thus {X>=0:X-X0-epsilon I in K} is compact: its pairing with W is fixed, and W>0 controls trace. The affine slice contains the strictly PD point X0+epsilon I. Strict concavity and boundary blowup of log(det X) give a unique positive-definite maximizer. Differentiating along every K direction proves X_epsilon^{-1} in K^perp, which also suffices for optimality.

Let Z=epsilon X_epsilon^{-1}. Then Z in K^perp, Z>=0. The stationarity identity
    n = <X_epsilon^{-1},X_epsilon>
      = <X_epsilon^{-1},X0> + epsilon tr(X_epsilon^{-1})
gives tr Z<=n, ||Z||_F<=n, <Z,X0><=n epsilon. Let y=R(Z): L*y=Z, ||y||<=kappa n. For any competitor Y>=0 with residual<=delta,
    epsilon tr(X_epsilon^{-1}Y)
      = <Z,Y>
      = <Z,X0> + <y,L(Y-X0)>
      <= n epsilon + kappa n delta.
As X_epsilon^{-1/2} Y X_epsilon^{-1/2}>=0, its operator norm is bounded by its trace, <=n(1+kappa delta/epsilon). Undo the congruence to obtain the stated Loewner inequality. Since L(X_epsilon-X0)=epsilon L(I), its residual is exactly q epsilon. Pairing the Loewner bound with any C>=0 yields the observable sandwich. QED.

## Polynomial intrinsic equations and exact positive observable exponents

Because det X>0, the stationarity condition is equivalent to adj(X) in K^perp; thus the center curve is the unique PD branch of the **finite polynomial system**
    X-X0-epsilon I in K, adj(X) in K^perp, X>0.
For algebraic measurement data the center is semialgebraic. Each positive-observable quantity <C,X_epsilon> vanishing at epsilon=0 has a rational Puiseux exponent; the observable sandwich proves the *same exponent* is globally sharp over all PSD competitors. This is intrinsic and does not optimize over arbitrary recovery curves. It settles the universal positive-observable sharpness problem, not all signed directions.

## Full Frobenius modulus: sharp factor-two interval

Assume now F={X*}, 0<r=rank(X*)<n, U=range X*, V=ker X*. Let
    b_epsilon=tr(P_V X_epsilon) ~ epsilon^beta
and let alpha be the full Frobenius recovery exponent. Then
    beta/2 <= alpha <= beta,   0<beta<=1.
The stationarity trace identity gives epsilon tr(X_epsilon^{-1})<=n, so X_epsilon>=(epsilon/n)I and beta<=1; singleton compactness gives beta>0. The center is an actual residual competitor and ||X_epsilon-X*||>= b_epsilon/sqrt(n-r), implying alpha<=beta. Conversely, the Loewner envelope bounds the null block trace of EVERY Y at residual q epsilon by O(b_epsilon). PSD Cauchy–Schwarz bounds cross blocks by O(sqrt(b_epsilon)); uniqueness makes L injective on S(U), so support-block deviations are O(epsilon+sqrt(b_epsilon)). Thus omega(q epsilon)=O(epsilon^(beta/2)), proving alpha>=beta/2.

The interval is sharp. For n=2, X*=E11 and L(X)=(X11,X22), the center is diag(1+epsilon,epsilon), beta=1, while cross-block competitors have alpha=1/2. In a rank-one sparse feedback PSD realization with alpha=1/3, a null diagonal has worst-case growth epsilon^(1/3), and the observable sandwich forces beta=1/3, attaining alpha=beta.

## Status of high-depth endpoint

Whether a dense PSD problem can have exact alpha=1/2 with minimal singularity degree d>=3 is NOT solved. One potentially sufficient route is to prove beta<1/2 at d>=3 for the canonical center, which would imply alpha<1/2 by the interval above. Do not infer this inequality merely from known slow central-path rate bounds without checking their exact hypotheses and direction.

Analytic centers, logdet stationarity, self-concordant barriers, Puiseux theory and related central-path bounds are established prior tools. This theorem's residual-ball Loewner transfer has a complete elementary proof above; its literature priority is not certified.