# Universal Dikin–Hessian classifier of the sharp PSD recovery exponent

**Research checkpoint, 2026-11-07. Fully proved for every finite-dimensional uniquely recoverable PSD target and every singularity degree.** Applies to arbitrary dense measurement maps, target ranks, and all full-matrix PSD competitors. No claim of bibliographic priority: analytic centers, logdet barriers and Dikin ellipsoids are known tools. The exact modulus comparison below is independently proved. A longer full proof/audit was also saved as PSD_Universal_Dikin_Hessian_Classifier_2026-11-07.md in this conversation.

## Definition

Let L:S^n -> R^m be real linear, X*>=0 its unique feasible PSD target for b=LX*, K=ker L, and q=||L(I)||>0. For each epsilon>0, define the **single canonical maximum-determinant curve**
    X_e = argmax {log det X : X>0, X-X*-epsilon I in K}.
It is uniquely defined by the polynomial-algebraic central equations
    X-X*-epsilon I in K; adj(X) in K^perp; X>0.
On K equip symmetric H with the logdet Hessian squared norm
    g_e(H,H) = tr(X_e^{-1} H X_e^{-1} H).
For nonzero K, let lambda_e=min{g_e(H,H):H in K,||H||_F=1}>0 and rho_e=lambda_e^{-1/2}. For K=0 set rho_e=0.

## UNIVERSAL STRUCTURAL THEOREM

There exist fixed constants 0<c<=C<infty such that for **every epsilon>0**
    c(epsilon+rho_e) <= omega_L,X*(q epsilon) <= C(epsilon+rho_e).
The *entire sharp Frobenius recovery modulus* is therefore equivalent to the residual scale plus **one smallest Hessian eigenvalue along one intrinsic algebraic curve**, with no optimization over arbitrary PSD recovery arcs. If rho_e~epsilon^s, then the exact sharp Hölder exponent is
    alpha = min(1,s).
For algebraic input data, the central curve, its restricted Hessian eigenvalues and the exponent s are exact semialgebraic/Puiseux quantities; a terminating real-algebraic algorithm computes them. For K=0, alpha=1.

## Complete proof

**Existence/centrality and key lower eigenvalue bound.** Since X* is uniquely feasible, K intersects PSD only at 0. Separating zero from the compact image under L of the trace-one PSD matrices yields W>0 in K^perp, which bounds the shifted PSD affine slice. The slice contains X*+epsilon I>0. Strict concavity gives a unique interior maximum X_e; stationarity along K gives X_e^{-1} in K^perp. Since X_e-X*-epsilon I in K,
    n=tr(X_e^{-1} X_e)=tr(X_e^{-1} X*)+epsilon tr(X_e^{-1}).
Both terms on the right are nonnegative. Thus with Z=epsilon X_e^{-1} one has tr Z<=n, ||Z||_F<=n, <Z,X*><=n epsilon, and
    X_e >= (epsilon/n) I.                                         (A)

**Global Loewner envelope.** Fix a right inverse R of L* on K^perp and kappa=||R||. Then y=R(Z) satisfies L*y=Z and ||y||<=kappa n. Every PSD Y with ||L(Y-X*)||<=delta obeys
    epsilon tr(X_e^{-1}Y)
       =<Z,X*>+<y,L(Y-X*)>
       <= n epsilon+kappa n delta.
A PSD matrix has largest eigenvalue no larger than its trace. Congruence by X_e^{-1/2} therefore gives
    0<=Y<= n(1+kappa delta/epsilon) X_e.                          (B)
In particular X*<=n X_e and all PSD competitors at residual q epsilon satisfy Y<=C0 X_e with C0=n(1+kappa q). Note X_e itself has exactly residual epsilon L(I), of norm q epsilon.

**Dikin radius and lower bound.** Put T_e(H)=X_e^{-1/2} H X_e^{-1/2}. Then
    rho_e=max{||H||_F:H in K, ||T_e(H)||_F<=1}.
Every admissible H has ||T_e(H)||_op<=1, so Y_+=X_e+H and Y_-=X_e-H are both PSD. As H lies in K, both have residual q epsilon. Their difference is 2H, hence at least one has distance to X* at least ||H||_F. Therefore omega(q epsilon)>=rho_e. The PSD matrix X*+epsilon I also lies at residual q epsilon and has distance sqrt(n)epsilon. Thus
    omega(q epsilon)>=max(rho_e,sqrt(n)epsilon)>=(rho_e+epsilon)/2. (C)

**All-competitor upper bound.** Choose any bounded right inverse J of L on its image, norm j. Given PSD Y at residual <=q epsilon, define
    E=J(L(Y-X_e)), H=Y-X_e-E in K.
Then ||E||_F<=2jq epsilon. Using (A) gives ||T_e(E)||_F<=2njq, while (B) gives ||T_e(Y)||_F<=sqrt(n)C0. Since T_e(X_e)=I,
    ||T_e(H)||_F<=sqrt(n)(C0+1)+2njq=:A.
By definition of rho_e, ||H||_F<=A rho_e.

The center displacement is also controlled by the Dikin radius: put
    H0=X_e-X*-epsilon I in K.
From X*<=n X_e, ||T_e(X*)||_F<=n sqrt(n); from the trace identity epsilon ||X_e^{-1}||_F<=n. Therefore
    ||T_e(H0)||_F<=sqrt(n)+n sqrt(n)+n=:B,
and ||H0||_F<=B rho_e. Finally
    Y-X*=H+H0+E+epsilon I,
so
    ||Y-X*||_F <= (A+B)rho_e+(2jq+sqrt(n))epsilon.
Take the supremum to prove the upper bound in the theorem. QED.

## Finite intrinsic invariant and joint-depth application

Choose any Frobenius orthonormal basis H1,...,Hk of K. Compute the finite symmetric Gram matrix
    G_e[i,j]=tr(X_e^{-1} Hi X_e^{-1} Hj).
Then lambda_e=lambda_min(G_e), invariant under basis changes. The full exponent is the valuation of the **single smallest eigenvalue** along the **unique polynomial central curve**. This is the requested canonical finite geometric classifier for each arbitrary dense pair (L,X*), including all d>=1. No arbitrary competitor path search, sparse representation or weighted-flag hypothesis remains.

The same kernel has a canonical minimum-depth facial-reduction chain computed using relative-interior/max-rank exposing stresses (standard prior literature, checkpoint 01). These two intrinsic finite objects yield the **exact joint pair (alpha,d)** for every individual arbitrary dense instance in all degrees. They also yield a real-algebraic decision procedure for existence at any fixed (n,r,d) by quantification over kernel projectors. This does **not** give a closed arithmetic formula for every universal spectrum Sigma_(n,r,d), nor prove any sparse-network degree-preserving equivalence.

## Sharp examples and boundary of claim

For X*=E11 in S^2, L(X)=(X11,X22), one has X_e=diag(1+epsilon,epsilon), K=span(F12). The restricted Hessian smallest eigenvalue is Theta(1/epsilon); rho_e~sqrt(epsilon), so alpha=1/2, correctly detecting cross-block instability *invisible in the diagonal entries of X_e*. A rank-one 1/3 feedback sparse pencil is similarly classified by the Hessian valuation 1/3.

This theorem is a complete **instance-wise universal structural theorem**, not a proof of the stronger explicit fixed-(n,r,d) arithmetic catalogue. The open high-depth alpha=1/2 endpoint and dense-to-sparse exact-degree conversion do not affect this classifier. Beware of the ambiguity of “complete classification”: computing the exact exponent of every pair is solved here; listing all allowed triples by a simple formula is a different question.

### Novelty discipline
Maximum-determinant analytic centers, barrier Hessians and Dikin ellipsoid containment are established semidefinite-optimization concepts; novelty is **not independently verified**. The theorem and proof are reported with exact scope rather than claimed as original to the literature.