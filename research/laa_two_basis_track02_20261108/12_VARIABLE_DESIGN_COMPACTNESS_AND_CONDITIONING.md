# Milestone 12 — tolerance-varying two-basis designs: compactness forces a limit exact representation

Date 2026-11-08. This extends Milestone 11 to variable orthogonal bases, target data, and CP decoders under UNIFORM quantitative guarantees. It yields a useful necessary large-slack-or-degeneracy dichotomy, not an unrestricted no-go for all algorithms.

## Theorem A (compactness of uniformly sound approximate representations)

Fix m,N,t and a nonempty closed source PSD fibre F_b={X>=0:A(X)=b}. Let eps_n downarrow0 and, for each n, choose U_n in O(N), data y_n in R^(2N), and completely positive real linear decoder D_n:S^N -> S^m with Kraus rank <=t.

Assume:
1. (uniform data and decoder bounds) sup_n ||y_n||<infinity, sup_n ||D_n||_{F->F}<infinity.
2. (uniform soundness) There are fixed delta_0>0 and a function rho:[0,delta_0]->[0,infinity) with rho(delta)->0 as delta downarrow0 such that for all n, every Y>=0 with ||A_{U_n}(Y)-y_n||<=delta_0 satisfies
   dist(D_n(Y),F_b)<=rho(||A_{U_n}(Y)-y_n||).
3. (asymptotic completeness) For every X in F_b and every n there exists Y_n(X)>=0 with
   ||A_{U_n}(Y_n(X))-y_n||<=eps_n,
   ||D_n(Y_n(X))-X||<=eps_n.

Then, after passing to ONE subsequence independent of X, the triples (U_n,y_n,D_n) converge to (U,y,D), where U is orthogonal and D is CP of Kraus rank <=t, and
  D({Y>=0:A_U(Y)=y})=F_b.
Thus a uniformly conditioned variable-design approximate normal form has an exact surjective two-basis PSD limit.

**Proof.**
O(N) and any bounded subset of R^(2N) are compact. To see precompactness of the CP decoders without invoking a Choi theorem for real symmetric matrices, pad every Kraus family with zeros to t terms and write
  D_n(Y)=sum_{a=1}^t B_{a,n} Y B_{a,n}^T.
The PSD matrix D_n(I_N)=sum_a B_{a,n}B_{a,n}^T has bounded norm because ||D_n|| is bounded. Therefore sum_a ||B_{a,n}||_F^2=tr D_n(I_N) is bounded. Passing to a subsequence makes all B_{a,n} converge, so D_n converges to a CP map D with <=t Kraus terms. Together with compactness of U_n,y_n this gives the common subsequence.

For each fixed X in F_b, the witness Y_n(X) has
  tr Y_n(X)<=sum_{j=1}^N (y_n)_j +sqrt N eps_n.
For PSD Y, ||Y||_F<=tr Y. Thus the witnesses are uniformly bounded, and each X admits a (possibly X-dependent) subsubsequence converging to some Y(X)>=0. Because the triple of parameters already has the same limit along every subsubsequence, continuity gives
  A_U(Y(X))=y, D(Y(X))=X.
Hence F_b subset D(T), T={Y>=0:A_U(Y)=y}.

For any fixed Y in T, define delta_n(Y)=||A_{U_n}(Y)-y_n||. This tends to zero. For large n it is <=delta_0, so the uniform soundness inequality gives dist(D_n(Y),F_b)<=rho(delta_n(Y))->0. As D_n(Y)->D(Y) and F_b is closed, D(Y) in F_b. Hence D(T) subset F_b. QED.

## Corollary B (giant slack in the exact limiting fibre)

Let F_b be the generic rational trace-controlled source family of Milestone 09, with b=A(I_m), ell=Theta(m^2), s=Theta(m^2). Fix C>0 and suppose a sequence of varying-design reductions satisfies Theorem A with
  N<=C m^2, t<=C m
(the order may be padded to a common N without changing constraints).
Then the exact LIMIT two-basis fibre T has minimal face order
  d>=c_C m^2
and decoder-invisible affine fibre dimension
  a>=c'_C m^4
for sufficiently large m, by Milestone 09. Hence any uniformly sound and complete quadratic-size reduction with a low-Kraus CP decoder must acquire Omega(m^4) auxiliary degrees of freedom in a zero-noise accumulation fibre.

If a proposed construction has uniformly bounded (by O(m^2)) auxiliary fibre dimension for its approximate exact systems, then the limit must undergo a rank/support degeneracy (unless some other uniformity assumption of Theorem A fails). In practical terms: either the exact measurement-analysis singular gaps, the minimal-face support eigenvalue gaps, or the uniform data/decoder/modulus bounds collapse as accuracy increases. This last assertion is an alternative, not a quantitative gap rate.

## Limitations and adversarial audit

- We do not assume that D_n are the same map, nor that U_n are reflections. Only uniform bounds and Kraus-rank <=t are used.
- The soundness hypothesis must hold for every residual delta up to a fixed delta_0, with a modulus rho independent of n. A guarantee only at a single requested eps_n does NOT imply soundness at delta_n(Y) for a fixed limit feasible Y, and the theorem makes no claim for that weaker model.
- Completeness witnesses may depend arbitrarily on X and n; extraction of the parameter subsequence is independent of X, while witness subsubsequences may depend on X.
- Traces bound witnesses because a complete first-basis diagonal is measured. Without this property the conclusion can fail.
- The limit CP rank upper bound follows by explicit bounded Kraus matrices, not by assuming CP rank is continuous without justification.
- The giant auxiliary fibre conclusion concerns the limiting exact fibre. Its dimension need not equal the dimensions of the finite-n exact fibres unless separate uniform nondegeneracy promises are imposed.
- This is a conditional obstruction, not a universal quadratic lower bound for arbitrary weak feasibility algorithms or nonlinear decoders.
