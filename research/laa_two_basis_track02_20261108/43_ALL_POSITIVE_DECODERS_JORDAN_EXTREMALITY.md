# Milestone 43 — unconditional 2m+1 dimension barrier for ALL POSITIVE trace-preserving fixed-diagonal PSD quotients

Date 2026-11-08. This upgrades Milestone 42 from completely positive decoders to EVERY globally positive trace-preserving REAL linear decoder, including non-CP maps. The proof uses elementary order-theoretic orthogonality of pure-output support spaces and a Jordan-homomorphism rigidity theorem, not Stinespring. It allows arbitrary nonlinear auxiliary lift selection, arbitrary nonunique feasible points, and any number of measured orthonormal bases.

## Theorem A — universal dimension bound, no complete positivity assumption

Let m>=2 and tau>0. Let D:S^n -> S^m be linear, POSITIVE on PSD matrices, and TRACE PRESERVING. Suppose for some real ONB f_1,...,f_n the nonempty PSD set
  T subset {Y>=0:f_j^T Y f_j=a_j for all j}
satisfies
  D(T)={X>=0:trX=tau}.
Then
  n>=2m;
and if m>=3, necessarily
  n>=2m+1.                                              (1)
For m=2, the bound n>=4 is attained by the real Bell-basis/partial-trace construction with n=4.

This includes all exact two-basis PSD fibres with a globally positive TP decoder: the first complete diagonal alone is enough for the obstruction. No positive encoder, inverse, full-fibre injectivity, exposed face, rank restriction, or basis-overlap hypothesis is needed.

### Proof Part I — at least 2m input coordinates

Write Phi=D*:S^m->S^n. Positivity and trace preservation make Phi POSITIVE and UNITAL: Phi(I_m)=I_n.

For a unit output vector u define the positive contraction
  A_u=Phi(uu^T),
and its eigenvalue-one subspace
  K_u=ker(I_n-A_u).
If Y>=0 has D(Y)=tau uu^T, then trY=tau and
  tr[(I_n-A_u)Y]=tr[(I_m-uu^T)D(Y)]=0.
Both matrices in the first pairing are PSD, so supp Y subset K_u. Surjectivity ensures dim K_u>=1 for every u.

If dim K_u=1, every such Y is forced to be the UNIQUE rank-one PSD matrix tau vv^T supported on the line K_u, with ||v||=1. But a fixed real ONB diagonal a supports at most 2^(k−1) distinct nonzero rank-one PSD matrices, where k is the number of positive a_j (because a rank-one vector has coordinates +/-sqrt(a_j)). A single Y has only one decoded output. Hence there are only FINITELY many projective source directions [u] for which dim K_u=1. For all other [u], dim K_u>=2.

Choose a real orthonormal source basis u_1,...,u_m avoiding this finite exceptional set. This is possible because the set of orthonormal frames having some column in a fixed finite set is Haar measure zero in O(m).

Let A_i=Phi(u_i u_i^T). These are PSD and sum_i A_i=I_n. Every K_(u_i) is the eigenspace of A_i at eigenvalue one. For any v in K_(u_i), the identity
  0=v^T(I-A_i)v=sum_(j!=i) v^T A_j v
and PSD of each A_j imply A_j v=0 for j!=i.
If w in K_(u_j) with j!=i, then A_j w=w, so
  <v,w>=<v,A_j w>=<A_j v,w>=0.
Thus the K_(u_i) are PAIRWISE ORTHOGONAL, each of dimension at least two. Consequently
  n>=sum_i dim K_(u_i)>=2m.

### Proof Part II — equality n=2m forces a twofold Jordan amplification

Assume n=2m. The preceding orthogonal subspaces each have dimension exactly two and fill R^n. Each A_i acts as identity on its own K_i and zero on every other K_j, hence
  A_i=P_(K_i),
the orthogonal projection onto a two-dimensional subspace.

For almost every source orthonormal basis all its columns avoid the finite exceptional set, so Phi maps the associated source rank-one projectors to rank-two orthogonal projections. It follows that Phi(uu^T) is a rank-two orthogonal projection for a dense set of unit vectors u. By continuity and the fact that the set of rank-two orthogonal projections is closed, the same holds for EVERY unit u.

For any real symmetric H write its spectral decomposition
  H=sum_i lambda_i u_i u_i^T
in an orthonormal eigenbasis. The matrices Phi(u_i u_i^T) are pairwise orthogonal projections summing to I_n (the argument above now applies without exceptional directions). Therefore
  Phi(H)^2
    =(sum_i lambda_i Phi(u_i u_i^T))^2
    =sum_i lambda_i² Phi(u_i u_i^T)
    =Phi(H²).
By polarization, Phi is a unital real symmetric JORDAN homomorphism.

The elementary matrix-unit classification, proved in Milestone 04 and reproduced here in essence, says that any unital Jordan homomorphism S^m→S^{2m} is orthogonally equivalent to X→X tensor I_2. Briefly: images of coordinate rank-one projections are mutually orthogonal equal-rank projections; images of symmetric off-diagonal matrix units square to the two corresponding diagonal projections, yielding orthogonal rank-two identifications across the blocks; the Jordan products E_1i o E_1j=E_ij/2 force coherent identifications. Thus there exists O in O(2m) such that
  Phi(H)=O(H tensor I_2)O^T.
Taking adjoints gives
  D(Y)=Tr_2(O^T Y O),
i.e. a real CPTP partial trace with only TWO Kraus operators.

But the exact full-rank-effect theorem of Milestone 39 applies to every positive TP decoder with a fixed-basis fibre projecting surjectively onto all trace-tau source states. It forces some output basis effect D(f_jf_j^T) to have full rank m. A two-Kraus decoder sends every rank-one input projector to an output of rank at most two. Hence m<=2. For m>=3 this contradicts equality n=2m and proves n>=2m+1. QED.

## Theorem B — a strictly positive uniform approximation floor for EVERY positive TP decoder

Fix m>=3, n<=2m and tau>0. There is a constant c(m,n,tau)>0 such that NO real ONB B, NO positive trace-preserving linear decoder D:S^n→S^m, and NO fixed first-basis target diagonal a>=0 with sum a=tau can admit approximate lifts of ALL pure source states with errors
  ||diag_B(Y_u)-a||_2<=epsilon,
  ||D(Y_u)-tau uu^T||_*<=eta
and epsilon+eta<c(m,n,tau), where each Y_u>=0 may depend arbitrarily on u.

Proof. Suppose instead a sequence of designs had epsilon_k+eta_k->0. The bases O(n) and diagonal vectors in the compact simplex are compact. The family of positive TP linear maps in fixed finite dimensions is ALSO compact: it is closed, and uniformly bounded. For symmetric H with ||H||_op<=1, positivity gives
  -D(I_n)<=D(H)<=D(I_n),
and D(I_n)>=0 with trD(I_n)=n; hence ||D(H)||_op<=n. Finite dimensionality gives precompactness. Extract a subsequence with convergent D_k, bases and target diagonals.

For each source unit u, its associated witnesses Y_(k,u)>=0 have bounded trace, because trace preservation and ||D_k(Y_(k,u))-tau uu^T||_*<=eta_k imply tr Y_(k,u)<=tau+eta_k. Extract a further subsequence (depending on u), obtaining an exact PSD lift Y_u with the limiting diagonal a and output tau uu^T. The design subsequence is common and independent of u. The fixed-diagonal PSD fibre is convex and compact; its positive decoder image contains every pure trace-tau source matrix and is contained in the trace-tau PSD body. Hence it equals the entire source density-matrix body, contradicting Theorem A for n<=2m,m>=3. Therefore the uniform gap exists. QED.

No explicit polynomial-in-m size for the gap is claimed; Milestone 41 supplies separate explicit effect conditioning lower bounds, and Milestone 39 supplies tau/n when all positive output basis effects are singular.

## Scope and audit

- The key new fact is ORTHOGONALITY of the eigenvalue-one support spaces for an arbitrary positive UNITAL adjoint; no Stinespring representation or CP assumption is needed.
- The finitely many exceptional source directions arise solely from finite rank-one PSD lifts under a fixed REAL diagonal; source directions are projective [u], so u and -u represent the same output.
- Equality n=2m makes the unital map preserve every rank-one projection, forcing Jordan rigidity. This is why a general high-Kraus or non-CP decoder cannot attain the boundary n=2m for m>=3.
- The classification of unital Jordan maps is a direct real matrix-unit argument; no complexification or implicit complete positivity assertion is used before the Jordan reduction.
- The lower bound n>=2m+1 is LINEAR in m, and does NOT settle unrestricted N=O(m²+p) universality. It is a rigorous architecture-independent constraint for all positive TP many-to-one PSD shadows of the trace-only source.
- The compactness argument for approximate reduction allows arbitrary tolerance-varying bases, positive decoders and nonlinear witness choices. Only fixed m,n and TP/positivity of the decoders are retained.
- A decoder with D*(I) singular (nonfaithful) or not scalar is outside the TP hypothesis, but a faithful nonTP decoder is subject to the separate normalized effect conditions of Milestones 40–41.
