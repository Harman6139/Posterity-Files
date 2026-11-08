# Milestone 37 — a canonical valuated-matroid gap determines sharp PSD recovery

**Proved, 2026-11-08, for every arbitrary dense uniquely solvable PSD inverse problem.** The theorem refines the universal Dikin–Hessian comparison (checkpoint 10) using only Cauchy–Binet sums of squares. It is a *complete instance-wise intrinsic combinatorial contact invariant*, NOT the still-open compact arithmetic enumeration of all (nullity, minimal facial degree, sharp exponent) triples.

Let K=ker L have dimension k>=1 and X_epsilon denote the uniquely defined shifted maximum-determinant center. Let H1,...,Hk be a fixed Frobenius-orthonormal basis of K, and define a linear whitening operator
    Q_epsilon:K -> S^n,
    Q_epsilon(H)=X_epsilon^{-1/2} H X_epsilon^{-1/2}.
Represent it in fixed Frobenius-orthonormal bases by an N-by-k matrix M_epsilon, where N=n(n+1)/2.

For 0<=j<=k put
    m_j = min{ ord_epsilon det M_epsilon[I,J]:
               |I|=|J|=j and the minor is not identically zero },
    m_0=0.
Every nonzero minor has a Puiseux leading term, since X_epsilon and its unique PSD square root are semialgebraic. Then the exact optimal Hölder recovery exponent is
\[
\boxed{ \alpha(L,X_*)=\min\{1,\;m_{k-1}-m_k\}. }
\]
For K={0}, alpha=1.

**Proof.** The restricted barrier-Hessian Gram matrix is precisely G_epsilon=M_epsilon^T M_epsilon. Cauchy–Binet gives
\[
\det G_\epsilon =\sum_{|I|=k}(\det M_\epsilon[I,[k]])^2,
\]
and
\[
e_{k-1}(G_\epsilon)=
\sum_{|J|=k-1}\sum_{|I|=k-1}(\det M_\epsilon[I,J])^2.
\]
All summands are real nonnegative squares, so **there is no leading valuation cancellation**:
   ord(det G_epsilon)=2m_k,
   ord(e_(k-1)(G_epsilon))=2m_(k-1).
As trace(G_epsilon^-1)=e_(k-1)(G_epsilon)/det G_epsilon, the Dikin kernel radius
    rho_epsilon=sqrt(1/lambda_min(G_epsilon))
is within a factor sqrt(k) of sqrt(trace G_epsilon^-1), hence
    ord(rho_epsilon)=m_(k-1)-m_k.
The universal two-sided modulus theorem (checkpoint 10) gives
    omega(||L I||epsilon)~epsilon+rho_epsilon,
and therefore the claimed exponent. QED.

**Intrinsic basis independence.** Although the individual minors depend on bases, the minimum valuation m_j equals ord||wedge^j(Q_epsilon)||_{HS}, since the squared Hilbert–Schmidt exterior-power norm is exactly the sum of all squared j-minors. A fixed orthogonal basis change leaves this norm invariant. More generally, a constant invertible basis change distorts it only by fixed multiplicative condition-number factors, preserving valuation. Thus all m_j and their gap are intrinsic.

**Interpretation.** The scalar Dikin–Hessian eigenvalue exponent is the *final gap in the exterior-minor valuation profile* of the canonical whitened measurement kernel. This resembles a representable valuated-matroid invariant, with no symbolic eigenvalue root selection and no cancellation ambiguities.

**Scope:** The theorem is valid for every PSD target rank, every singularity degree, and every dense map. However, the possible values of the intrinsic gap at *fixed* (n,r,d) are constrained by which measurement kernels and dual stress chains exist; an elementary closed arithmetic spectrum is not derived here. Signed tropicalization and valuated-matroid theory have substantial existing literature (e.g. Akian–Allamigeon–Gaubert–Sergeev, 2025, DOI 10.1007/s10957-025-02732-2); we claim no novelty for those earlier mathematical tools.