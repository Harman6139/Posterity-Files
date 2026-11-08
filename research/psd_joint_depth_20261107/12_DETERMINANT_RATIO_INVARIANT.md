# Single determinant-ratio invariant for sharp PSD recovery — no eigenvalue optimization

2026-11-07. **Corollary of the fully proved universal Dikin–Hessian theorem** (checkpoint 10). Applies to every uniquely solvable finite-dimensional PSD inverse problem, arbitrary dense maps, all singularity degrees.

Fix the canonical maximum-determinant curve X_e from checkpoint 10. Let K=ker L, k=dim K>=1, and choose Frobenius-orthonormal basis H1,...,Hk. Define the **polynomial** k-by-k matrix
    A_ij(X)=tr(adj(X) Hi adj(X) Hj).
For X>0 this matrix is positive definite. Let e_(k-1)(A) be the sum of its (k-1)-order principal minors, with e_0=1, and define
    R(X)=det(X) * sqrt( e_(k-1)(A(X)) / det(A(X)) ).
Then the universal sharp full Frobenius modulus is
    omega(||L(I)|| epsilon)  ASYMPTOTICALLY_EQUIVALENT_TO  epsilon+R(X_e),
with two-sided comparison constants independent of epsilon. This is a **single scalar determinant-ratio invariant** evaluated on one uniquely defined algebraic central curve; no spectral eigenvalue optimization is needed in the final formula.

**Proof.** Let G_e,ij=tr(X_e^-1 Hi X_e^-1 Hj) be the Hessian Gram matrix in checkpoint 10. Since X^-1=adj(X)/det(X),
    G_e=A(X_e)/det(X_e)^2.
Therefore
    tr G_e^-1=det(X_e)^2 tr A(X_e)^-1
              =det(X_e)^2 e_(k-1)(A(X_e))/det(A(X_e))
              =R(X_e)^2.
For any positive-definite k-by-k matrix G,
    1/lambda_min(G) <= tr(G^-1) <= k/lambda_min(G).
Thus rho_e<=R(X_e)<=sqrt(k)*rho_e, where rho_e is the canonical Dikin kernel radius. The modulus theorem in checkpoint 10 proves the stated equivalence. QED.

If a function f(epsilon) has a nonzero Puiseux leading term, denote its order by ord(f). The sharp exponent is explicitly
    alpha=min{1, ord(det X_e) +
                (1/2) ord(e_(k-1)(A(X_e))) -
                (1/2) ord(det A(X_e)) }.
All quantities are nonnegative or positive on the central branch, and the formula is invariant under orthonormal basis changes in K, because A transforms by orthogonal similarity. This is a finite *polynomial contact invariant* explaining the sharp exponent, not a definition involving arbitrary feasible recovery curves. Algebraic input allows exact calculation by real-algebraic elimination/branch orders, though no low-complexity guarantee is asserted.

For K={0}, the problem is injective and the exponent is 1.

This is **a complete instance-wise universal structural theorem**. It does not settle the separate closed-form combinatorial classification of all possible triples (n,r,d), or a sparse depth-preserving representation. No bibliographic priority for Dikin-radius or determinant-ratio ideas is claimed without a novelty audit.