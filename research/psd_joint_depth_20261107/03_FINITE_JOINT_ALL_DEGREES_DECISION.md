# Checkpoint 03 — a universal finite joint exponent/depth decision theorem

Date: 2026-11-07. This checkpoint gives a **complete algorithmic (real-algebraic) classification** for every triple (n,target rank r,minimal singularity degree d), without assuming the previously unproved depth-preserving dense-to-sparse network reduction. It is not a closed arithmetic formula, and it uses real quantifier elimination only **after** a bounded PSD-specific reduction. Quantifier elimination by itself is established mathematics and is not claimed novel.

## 1. Setup and finite candidate set

Fix n>=r>=1, nu=n-r>=1 and N=n(n+1)/2. Fix the target X*=diag(I_r,0_nu), with support projector P_U. Every linear measurement kernel K can be represented by an orthogonal projector Pi on the N-dimensional Euclidean space of symmetric matrices: Pi=Pi^T=Pi^2, K=range(Pi). Kernel membership and stress membership are the linear polynomial relations Pi H=H and Pi Z=0.

**Weighted patterns.** Enumerate all ordered partitions n_1+...+n_k=nu (1<=k<=nu), all choices of allowed block support pairs for k-1 coefficient matrices H_i with strictly positive i-th diagonal compression, and, in an optional mode, one nonzero extra coefficient H_p. Consider their rational linear constraints 2 w_i>=w_a+w_b on each allowed block, with 0<w_1<...<w_k=1, and either p=w_1 or 0<p<w_1. Reject support choices with no strictly feasible weights. Solve the closed rational LP minimizing p; its optimum lambda_P is rational and independent of K. The finite set A_nu={1} union {positive lambda_P} is an explicit computable candidate set for every uniquely recoverable PSD problem of nullity nu.

For each pattern P define the purely algebraic existential predicate G_P(Pi): there exist an orthogonal decomposition U_0=range(X*), U_1,...,U_k of the prescribed sizes, matrices H_i in range(Pi) with their forbidden blocks zero, with (H_i)|_{U_i} positive definite, and, if applicable, H_p in range(Pi) nonzero with the prescribed zero blocks. Orthogonality can be parameterized by a matrix Q in O(nu); all requirements are polynomial equalities, strict inequalities and PSD/principal minor conditions.

**Exact exponent at fixed kernel.** For a unique target, the prior finite weighted-flag theorem gives
alpha(Pi)=min({1} union {lambda_P:G_P(Pi)}).
Its proof: (i) scale positive coefficients according to exp(sigma*w_i^2) to construct full PSD witness curves while retaining their kernel membership; (ii) extract a bounded orthogonal weighted flag by recursive compression of a semialgebraic sharp arc and adding t^Q I, with at most nu nonzero diagonal levels. Every coefficient below order Q lies in K and every nonzero block obeys 2e>=w_a+w_b. A final level at Q exists by uniqueness. This avoids quantifying over arbitrary recovery curves in the final classifier.

Hence exact alpha=beta is the finite semialgebraic formula:
for beta<1, [OR over lambda_P=beta of G_P(Pi)] AND [AND over lambda_P<beta of NOT G_P(Pi)];
for beta=1, just [AND over lambda_P<1 of NOT G_P(Pi)].

## 2. Canonical greedy facial reduction is semialgebraic

For any orthogonal projector P_W with range W containing U, let C(W,Pi) consist of S=P_W Z P_W with Pi Z=0, S>=0, and <Z,X*>=0. Let G(W,Pi)= intersection of kernels of all S in C(W,Pi), intersect W.

A single S in C(W,Pi) has kernel G(W,Pi) if and only if:
(i) S>=0 and its kernel inside W equals a projector P_Wnext;
(ii) for every Z with Pi Z=0 and P_WZP_W>=0 and <Z,X*>=0, we have trace(P_Wnext P_WZP_W)=0.
Condition (ii) says all valid PSD stresses annihilate Wnext. Conversely the sum of finitely many PSD stresses has the common kernel of the entire cone, so such an S exists.

Use projector variables P_0,...,P_d, with P_0=I and P_d=P_U, and at each step a symmetric Z_j in ker Pi. Impose:
- P_j^T=P_j=P_j^2, P_jP_{j-1}=P_j, trace(P_{j-1}-P_j)>=1;
- S_j=P_{j-1}Z_jP_{j-1}>=0, <Z_j,X*>=0, S_jP_j=0, and S_j+P_j+(I-P_{j-1}) is positive definite (so ker(S_j) inside W_{j-1} is exactly W_j);
- for all symmetric Z with Pi Z=0, P_{j-1}ZP_{j-1}>=0 and <Z,X*>=0, impose trace(P_j P_{j-1}ZP_{j-1})=0.

All are first-order polynomial relations (positive semidefiniteness by principal minors, positive definiteness by Sylvester or principal minors), with one bounded universal stress variable for each step. The resulting chain is exactly the canonical maximal-stress greedy chain and has the minimal facial-reduction degree d. Its correctness follows by comparing greedily exposed faces with any other chain: at each step the greedy face is contained in the competitor face, so the greedy chain is shortest.

**Uniqueness.** Let E_1,...,E_a be a fixed orthonormal basis of S(U), a=r(r+1)/2, and form the Gram matrix G_ij=<E_i,(I-Pi)E_j>. Requiring det(G)>0 makes K intersect S(U) only in {0}. Since the greedy stresses force every exactly feasible PSD matrix into S(U), this condition and the chain prove uniqueness. Conversely uniqueness guarantees such a reduction chain, and the Gram condition.

## 3. Exact joint classification algorithm

For every candidate beta in the explicit finite rational set A_nu and d in {1,...,nu}, construct the first-order real-closed-field sentence Psi(n,r,d,beta):

"There exist an orthogonal kernel projector Pi, d canonical greedy projector/stress stages terminating at U, with support Gram det(G)>0, and Pi satisfies the finite exact-exponent pattern formula alpha(Pi)=beta."

Then the exact *universal* joint spectrum at this triple is
Sigma_{n,r,d} = { beta in A_nu : Psi(n,r,d,beta) is true }.

This is a necessary-and-sufficient, universally terminating finite algorithm: (1) enumerate discrete patterns; (2) solve rational LPs; (3) construct the semialgebraic sentence; (4) decide it by a real-closed-field algorithm (e.g. cylindrical algebraic decomposition). When true, algebraic sample coefficients for Pi, stresses and flags yield an explicit measurement map and a certified exponent and minimal depth. When false, real-algebraic infeasibility gives an exact nonrealizability certificate.

This uses bounded PSD-specific information (at most nu weighted coefficient matrices, rational LPs and at most nu maximal exposing stages). It is not the unrestricted original quantified competitor optimization. No practical complexity guarantee is claimed.

## 4. Interpretation and honest limit

This **resolves the all-degree compatibility problem in the algorithmic decision sense**, independently of a depth-preserving sparse network theorem. It does **not** give an elementary closed-form arithmetic list for each (n,r,d), nor prove that the sparse-network peeling catalogue always equals the universal spectrum. The explicit unrestricted-dimension realizations in checkpoint 02 are a separate sharper theorem.

For alpha=1, Lipschitz recovery implies K intersects the PSD tangent cone only at 0. The bottom-block projection of K then avoids PSD and is injective, so separation supplies a full positive definite exposing stress on ker X*. Thus alpha=1 forces d=1 for a singular positive-rank target. Sturm gives alpha>=2^{-d}, while the PSD quadratic tangent realization gives alpha<=1/2 in every non-Lipschitz instance.