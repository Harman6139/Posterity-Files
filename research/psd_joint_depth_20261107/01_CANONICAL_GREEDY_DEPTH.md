# Universal PSD recovery: checkpoint 01 — canonical greedy facial reduction
Date: 2026-11-07

## Status
This establishes a rigorous *canonical computation of minimal facial-reduction degree for an individual dense map*. It does **not** yet prove a complete exponent–depth realization spectrum at every (n,r,d). Neither a dense-to-midpoint network depth-preservation theorem nor a converse is claimed.

## Theorem (canonical maximal-stress greedy chain)
Let K be the kernel of a linear measurement map and X_*\succeq0 uniquely feasible in (X_*+K)\cap S_+^n. Put U=range(X_*). For any linear subspace W\supseteq U define
\[
\mathscr C(W)=\{ P_WZP_W:\ Z\in K^\perp,\ \langle Z,X_*\rangle=0,\ P_WZP_W\succeq0\}.
\]
Here P_W is the orthogonal projector; the zero matrix is allowed. Define
\[
G(W)=W\cap\bigcap_{S\in \mathscr C(W)}\ker S.
\]
Starting with W_0=R^n, iterate W_{j+1}=G(W_j). Then this is a valid facial-reduction chain and terminates at U. Its number of *strict* steps equals the **minimum singularity degree**. The face W_j is canonical, independent of choices of exposing stresses.

### Proof
The PSD cone \mathscr C(W) is convex. Every pair S,T\succeq0 satisfies ker(S+T)=ker S\cap ker T. By finite dimensionality, finitely many members have intersection of kernels equal to the intersection over the entire cone, and their sum exposes exactly G(W). Thus a single allowed exposing stress produces the greedy step (if G(W)\subsetneq W). If no exposing stress exists and W properly contains U, the separating hyperplane theorem for semidefinite feasibility on the face S_+(W) provides a nonzero such stress: uniqueness ensures that the feasible set is contained in the proper face S_+(U). Thus the iteration terminates at U.

Compare against any admissible chain V_0\supsetneq V_1\supsetneq\dots\supsetneq V_q=U. Inductively, W_j\subseteq V_j. If Z_j exposes V_{j+1} inside V_j, then the same Z_j has PSD compression on W_j, so it belongs to \mathscr C(W_j). Hence W_{j+1}\subseteq W_j\cap\ker(P_{W_j}Z_jP_{W_j})\subseteq V_{j+1}. Thus W_q\subseteq U; since every greedy W_j contains U, W_q=U. The greedy chain therefore uses no more steps than any other chain and itself is admissible. QED.

### Verification of target orthogonality
The condition \langle Z,X_*\rangle=0 is essential: without it, a PSD compression could expose a face that does not contain the target. For a positive-semidefinite compression, this condition implies S|_U=0 since X_* is positive definite on U.

### Finite implementation
Each step finds any relative-interior matrix in the cone \mathscr C(W), or equivalently a maximum-rank compression: all such compressions have identical kernel, because the PSD sum of a maximum-rank compression and another cone member cannot increase its rank. These steps use only linear equations and PSD feasibility, not recovery arcs.

## Connection to the unresolved classification
The earlier weighted-flag theorem gives the sharp exponent through finitely many geometric patterns and rational linear programs. The canonical greedy chain computes singularity degree for the *same kernel K*. Combining them yields an instance-wise exact pair (alpha,d), but does **not** yet classify which pairs are simultaneously realizable at fixed matrix size and target rank without ranging over possible dense kernels. Sparse midpoint-network peeling is a sufficient family, not yet proved universal for depth.

## Research next target
Derive a necessary-compatible graph/flag layer invariant from \mathscr C(W_j) acting on sharp weighted-flag coefficients, and either prove sparse-network realization preserving depth or produce an explicit dense counterexample.
## Bibliographic attribution correction (audited)
The maximal-rank / relative-interior exposing-stress rule giving a shortest facial-reduction sequence is **established prior literature**, not a new theorem. In particular see Sremac, Woerdeman, Wolkowicz, *Error Bounds and Singularity Degree in Semidefinite Programming* (SIAM J. Optim. 31 (2021), doi:10.1137/19M1289327), and discussions of relative-interior exposing vectors in work on facial reduction. The proof here is included for self-containment, and its new role is as the depth half of the **joint** exact classification. No novelty of the greedy rule itself is claimed.
