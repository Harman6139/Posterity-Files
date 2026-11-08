# Milestone 44 — UNIVERSAL sharp dimension-dependent separation from square-root stability at every degree >=3

**2026-11-08. PROVED for EVERY arbitrary dense real PSD inverse problem with a uniquely determined PSD target, independent of weighted-flag theory and sparse representations.** This resolves the formerly universal open square-root endpoint: \(\alpha=1/2\) is IMPOSSIBLE at minimal facial-reduction degree \(d\ge3\). It is strengthened by a *sharp* target-nullity gap.

## Main theorem

Let L:S^n→R^m be an arbitrary real linear measurement map, let X*≽0 of positive rank be uniquely determined among PSD matrices, and put ν=n-rank(X*)≥3. Assume the minimal facial-reduction degree d≥3. Let s1≥1 and s2≥1 be the rank drops of the **first two canonical maximal-rank PSD exposing stresses**, and set t=ν-s1-s2≥1. Then
\[
\boxed{
\alpha(\mathcal L,X_*)\le
\frac{2^{t-1}(2^{s_2}-1)}
     {2^t(2^{s_2}-1)+1}
<\frac12.
}
\tag{1}
\]
In particular, *for every* d≥3 with given nullity ν,
\[
\boxed{
\alpha(\mathcal L,X_*)\le
\frac{2^{\nu-2}-1}{2^{\nu-1}-1}
<\frac12.}
\tag{2}
\]
The dimension-only bound (2) is sharp for every ν≥3 **within the whole class of all d≥3**, attained at exact degree d=3 by the explicit rank-one sparse harmonic ladder with one terminal, ν-2 core vertices and one root. All competitors in that construction are controlled; it is not only a feasible-path example.

Consequently:
\[
\boxed{\alpha=1/2\ \Longrightarrow\ d\le2}
\quad\text{for every singular positive-rank uniquely solvable PSD inverse problem.}
\tag{3}
\]
More generally the implication \(\alpha=1\Rightarrow d\le1\) follows from the tangent criterion. This gives a **universal strict endpoint characterization** that was previously unresolved even at ν=4,d=3 in the project.

## Complete direct proof (no sparse/weighted-flag extraction)

The construction in checkpoint 43 requires ONLY:
1. a maximal first exposing stress Z1 PSD, rank s1, supported on an f=s1 dimensional null subspace F;
2. after restricting to W1=F⊥, a maximal second exposing compression Z2 PSD, rank s2, supported on T, disjoint from F;
3. a nonzero residual null subspace D, dim t=ν-s1-s2.

It does **not** require the next facial reduction to expose all D or even to exist at one step. That observation upgrades its proof from d=3 to **all d≥3** without a new unproved step.

For clarity, repeat the actual mechanism. Decompose R^n=U⊕D⊕T⊕F with U=range X*. Let K=ker L and K1=K∩S(U⊕D⊕T).

**Deep modes:** For every nonzero remaining D_rem⊆D, project K1 to S(D_rem⊕T). A strictly positive-definite matrix orthogonal to that projected subspace would lift (by the exact finite-dimensional compression-annihilator identity) to a valid **second-step** exposing stress on U⊕D⊕T with rank s2+dim(D_rem), violating the **maximal second rank** s2. By the strict homogeneous Gordan–Stiemke alternative, the projected subspace therefore intersects PSD nontrivially. Complementarity with the second stress positive on T forces such a PSD compression to be supported inside D_rem. Selecting its support and repeating yields an orthogonal flag D=D1⊕...⊕Dl, l≤t, with actual matrices A_i∈K1, each PD on D_i and zero on the remaining D_(i+1),...,T block. All previously selected D blocks and support-block cross entries may be arbitrary dense.

**Middle modes:** Repeat for every nonzero T_rem⊆T, now projecting the full K to S(T_rem⊕F). The first maximal PSD stress is positive on F. A positive-definite stress in the projected orthogonal complement would be a globally PSD *first-step* exposing stress of rank s1+dim(T_rem)>s1. The Gordan alternative thus produces a nonzero PSD projected kernel matrix supported on T_rem. Iteration yields T=T1⊕...⊕Tk, k≤s2, and actual B_j∈K, positive on T_j, with zero compression to subsequent T blocks and F, but arbitrary earlier-T, D and source couplings.

**Weighted full-PSD curve:** For l,k put
    M=2^l(2^k-1),
    B_*=M/(M+1),
    a_i=B_*(1-2^{-i}), i=1,...,l,
    b_j=1-2^{-j}(1-a_l), j=1,...,k.
Then 0<a1<...<al<b1<...<bk=B_*<1 and
    2a1=bk, 2a_i=a_(i-1)+bk,
    2b1=al+1, 2b_j=b_(j-1)+1.
Assign weights a_i on D_i, b_j on T_j, 1 on F, 0 on U. Every potential dense block of A_i obeys wi+wj≤2a_i because its compression to remaining D/T only occupies D_i; every potential dense block of B_j obeys wi+wj≤2b_j because its compression to remaining T/F occupies only T_j. The inequalities use exactly the midpoint identities above and bk<1. The terminal P_F is PD on F.

Therefore the positive coefficient-rescaling lemma makes
    X(z)=X*+Σ exp(σa_i²) z^(a_i) A_i
           +Σ exp(σb_j²) z^(b_j) B_j
           +exp(σ) z P_F
strictly positive definite for all sufficiently small z>0. The proof is diagonal congruence: the limiting diagonal blocks are PD, while every surviving normalized cross block is multiplied by exp[-σ(wi-wj)²/4] and tends to zero as σ→∞. All A_i,B_j lie in K, and P_F∉K by uniqueness, so the residual is Θ(z); its leading displacement is Θ(z^a1). Hence alpha≤a1.

As l≤t and k≤s2, monotonicity of
    a1 = 2^(l-1)(2^k-1) / [2^l(2^k-1)+1]
yields formula (1).

**Dimension bound:** Since ν=s1+s2+t and s1≥1, s2+t≤ν-1. Write M=2^t(2^{s2}-1)=2^{s2+t}-2^t≤2^{ν-1}-2, with equality when s1=t=1 and s2=ν-2. Because a1=M/[2(M+1)] increases in M, this yields (2). For every ν the sparse harmonic ladder with weights root a=(2^{ν-2}-1)/(2^{ν-1}-1), cores b_j=1-2^{-j}(1-a), terminal 1 has exact degree3, first-rank1, second-rank ν-2, remaining-rank1, sharp exponent a, attaining (2). QED.

## Sharp implications and exclusions

- The full sharp nullity-four degree-three spectrum recorded in checkpoint 41 is now **unconditionally free of the square-root endpoint**; the new theorem removes the last unresolved high-depth square-root possibility at *all* nullities.
- Every high-depth instance, no matter how dense, has exponent bounded away from 1/2 by at least
\[
\frac12-\alpha\ge\frac{1}{2(2^{\nu-1}-1)}.
\]
- For degree d=3, checkpoint 43 gives the exact maximal exponent at every prescribed facial rank profile (f,s,t). For d>3, (1) remains a rigorous strict bound but is not necessarily sharp with that fixed larger degree.
- This **does not yet deliver** the complete arithmetic set of exponents at each prescribed (\nu,d) for ν≥5, nor a depth-preserving sparse conversion. The project goal of a fully universal simple combinatorial spectrum remains open despite this major obstruction theorem.

## Audited subtlety: lifting Gordan alternatives

For deep modes, if Q_R={P_R H P_R:H∈K1} and Z∈Q_R⊥∩PD, the **zero extension of Z inside W1** is orthogonal to K1. The identity
    (K∩S(W1))^⊥_(S(W1)) = P_W1 K^⊥ P_W1
gives an ambient full stress whose ENTIRE W1 compression is precisely that zero extension, hence PSD and of rank dim(R). No uncontrolled cross terms inside W1 are left. For middle modes, Q_R comes from the full K, so zero extension of Z is directly an element of K⊥. Thus both conic alternatives truly contradict canonical maximal exposing ranks. The exposed support U is annihilated in both cases.

No potential matrix entry of the constructed kernel coefficients is dropped without the PSD projected-cone complementarity justification; the support order inequalities hold for ALL arbitrary dense entries permitted by these constraints.

## Prior-art discipline

Facial reduction, maximal-rank exposing stresses, Gordan–Stiemke, and logarithmic/weighted PSD coefficient balancing are established mechanisms. The new rank-profile and universal strict square-root instability bounds are proved here, but bibliographic novelty must be independently checked.