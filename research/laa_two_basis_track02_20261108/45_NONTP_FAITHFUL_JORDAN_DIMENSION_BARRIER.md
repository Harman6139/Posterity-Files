# Milestone 45 — n>=2m+1 for ALL FAITHFUL positive decoders, even when NOT trace preserving

Date 2026-11-08. This strengthens Milestones 40 and 43. The source trace-only PSD fibre and first complete basis diagonal are fixed, but the decoder is ANY globally positive linear map with faithful trace effect E=D*(I_m)>0. It need not be trace preserving, completely positive, injective, or possess a positive right inverse. Lifts may be nonlinear and many-to-one. The proof combines a positive congruence normalization with the finite rank-one-lift property of an arbitrary LINEARLY INDEPENDENT measurement frame.

## Theorem A

Let m>=2, tau>0 and let D:S^n ->S^m be a real positive linear map with
  E=D*(I_m)>0.
Suppose there is an ONB f_1,...,f_n and a fixed nonnegative vector a such that a PSD set T satisfies
  f_j^T Y f_j=a_j for all Y in T, and
  D(T)={X>=0:tr X=tau}.
Then
  n>=2m;
and if m>=3,
  n>=2m+1.
For m=2, n=4 is achievable with a trace-preserving partial trace decoder.

Proof. As in Milestone 40, define
  Dhat(Z)=D(E^(-1/2) Z E^(-1/2)),
which is positive TRACE PRESERVING, and set Z=E^(1/2)Y E^(1/2).
The original fixed-basis diagonal equalities become
  w_j^T Z w_j=a_j, w_j=E^(-1/2)f_j.
The n vectors w_1,...,w_n are LINEARLY INDEPENDENT because E is invertible. Consequently the set of rank-one PSD matrices vv^T satisfying these n scalar equations is FINITE: each equation gives w_j^T v=+/−sqrt(a_j), and the invertible linear map v->(w_j^Tv)_j has at most 2^n sign choices (with v and -v identified).

For any positive TP map Dhat and source unit u, let
  A_u=Dhat*(uu^T), 0<=A_u<=I_n,
  K_u=ker(I_n-A_u).
Every PSD lift Z with Dhat(Z)=tau uu^T must be supported on K_u, by the positive zero-pairing argument of Milestone 43. If dim K_u=1, such a lift is uniquely rank one, with its coefficient fixed by trace. Since there are only finitely many rank-one matrices satisfying the above INVERTIBLE frame outcomes, dim K_u=1 can occur for at most finitely many source projective directions.

Choose a source ONB u_1,...,u_m avoiding the finite exceptions. The positive unital adjoint maps their orthogonal rank-one projections to PSD contractions A_i whose eigenvalue-one spaces K_i are mutually orthogonal: sum_i A_i=I and A_i|K_i=I imply A_j|K_i=0 for j!=i. Each dim K_i>=2, so n>=2m.

If equality n=2m holds, the K_i exhaust input space and each A_i is a rank-two projection. Running over generic source ONBs and using continuity shows Dhat* maps EVERY source rank-one projection to a rank-two projection. By spectral decomposition it preserves all squares, so it is a unital real Jordan homomorphism S^m ->S^(2m). Matrix-unit classification gives
  Dhat*(H)=O(H tensor I_2)O^T,
so Dhat is a two-Kraus partial-trace decoder.

But Milestone 40's faithful effect bound applied to the independent frame w_j says that for any j with a_j>0, Dhat(w_jw_j^T) is positive definite on R^m. A two-Kraus decoder maps EVERY rank-one input to a PSD matrix of rank at most two. Since sum_j a_j=trY>0 for any nonzero Y in T, some a_j>0. Therefore m<=2, contradicting m>=3. Hence n>=2m+1 for m>=3. QED.

The only distinction from Milestone 43 is that rank-one fixed-data finiteness does not require an ONB: any invertible set of n real rank-one measurement directions suffices. Congruence normalization supplies exactly such a set.

## Theorem B — a uniform error floor under faithful conditioning

Fix m>=3,n<=2m,tau>0 and constants 0<alpha<=beta<infinity. Restrict to positive decoders D:S^n->S^m satisfying
  alpha I_n <=D*(I_m)<=beta I_n.
There exists c(m,n,tau,alpha,beta)>0 such that no ONB, nonnegative diagonal a with sum a_j in [tau/beta,tau/alpha], and positive decoder in this conditioned class can provide approximate lifts for EVERY pure source state with both:
  ||diag_B Y_u-a||_2<=epsilon,
  ||D(Y_u)-tau uu^T||_*<=eta,
and epsilon+eta<c.

Proof by compactness. The ONBs and diagonals lie in compact sets. The decoders form a closed bounded set: for ||H||_op<=1, -I<=H<=I, positivity gives -D(I)<=D(H)<=D(I), and trD(I)=trD*(I)<=n beta, hence a uniform norm bound. Passing to a convergent design subsequence, the uniform lower effect bound alpha ensures the limiting D*(I)>=alpha I remains faithful. The approximate witnesses have bounded traces:
  alpha trY_u<=trD(Y_u)<=tau+eta,
so they admit convergent subsequences for each u. At the limit one obtains a fixed-diagonal exact surjection onto all pure source states; by convexity and positivity it surjects onto the full trace-tau PSD body. This contradicts Theorem A for n<=2m,m>=3. QED.

The gap c is NONEXPLICIT from compactness; the explicit effect-based inequalities of Milestones 40–41 provide complementary bounds when output effects are singular or nearly singular.

## Scope

- Faithfulness is positivity of the decoder trace effect D*(I)>0, not injectivity of D. This strictly extends the TP model.
- The argument uses no CP assumption, Stinespring dilation, rank-restricted lifted competitors, or positive encoding.
- A NONFAITHFUL decoder (singular D*(I)) can evade the congruence normalization; such a decoder may use a large auxiliary block invisible to the output trace, as in positive companion constructions. This is a genuine remaining escape for unrestricted quadratic-size many-to-one universality.
- The dimension bound is LINEAR in source order. It does not refute N=O(m²+p) for arbitrary dense SDPs.
- The conditioning gap assumes both alpha and beta are fixed. It is not a dimension-only or polynomial-in-m explicit rate.
