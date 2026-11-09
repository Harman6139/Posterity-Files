# Canonical valuated-matroid gap for sharp PSD recovery

Let the hypotheses and canonical centered matrix X_eps be as in the universal
Dikin–Hessian theorem. Let K=ker L have dimension k>=1, and choose a
Frobenius-orthonormal basis H_1,...,H_k. Let Q_eps: K -> S^n be the
whitening map Q_eps(H)=X_eps^{-1/2} H X_eps^{-1/2}. In fixed orthonormal
bases, represent Q_eps by an N-by-k matrix M_eps, N=n(n+1)/2.

For 0<=j<=k define m_j = min{ord_eps det(M_eps)_{I,J}: |I|=|J|=j}
with m_0=0; only nonzero minors contribute. Then

    alpha = min(1, m_(k-1) - m_k).

The m_j are rational numbers (X_eps semialgebraic, matrix square root
semialgebraic) and are invariant under all constant invertible changes
of bases in S^n and K: the norm of the exterior power transforms by
fixed operator condition numbers, so valuation is unchanged. Thus the
last difference is intrinsic, not a basis artifact.

Proof: G_eps=M_eps^T M_eps is exactly the restricted Dikin Hessian Gram.
By Cauchy–Binet,
 det G_eps = sum_{|I|=k} det(M_{I,[k]})^2,
 e_{k-1}(G_eps) = sum_{|J|=k-1} det(G_{J,J})
 = sum_{|J|=k-1,|I|=k-1} det(M_{I,J})^2.
Every summand is a nonnegative real square on eps>0, hence no leading
valuation cancellation: ord(det G_eps)=2m_k,
ord(e_{k-1}(G_eps))=2m_(k-1).
Because trace(G_eps^-1)=e_{k-1}(G_eps)/det G_eps, the Dikin radius has
order m_(k-1)-m_k. The universal two-sided recovery theorem then yields
the formula. QED.

This is a complete instance-wise combinatorial *contact* invariant on a
single canonical algebraic curve, rather than a closed arithmetic
classification of possible (nullity, singularity degree, alpha).

Warning: a basis-dependent list of individual minor valuations may vary
under basis changes, but the minima of each exterior-minor collection
are invariant. Prior tropical/valuated matroid theory is well developed;
no priority claim is made for these standard Cauchy–Binet identities.