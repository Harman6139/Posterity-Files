# Milestone 22 — a general sharp modulus-transfer criterion for exposed PSD faces beyond reflections

2026-11-08. Complete theorem for arbitrary finite-dimensional REAL PSD linear measurements. It subsumes the even/odd reflection argument by a finite linear transversality criterion, and explicitly identifies when a two-zero Naimark dilation can avoid the usual additional square-root loss. The criterion is sufficient, not claimed necessary in every degenerate case.

## 1. Setting

Let F in R^{d x N} satisfy FF^T=I_d; P=F^T F and Q=I-P. Let B:S^N -> R^k be a real linear measurement map containing the trace in its measurement span, and write
  B_V(Z)=B(F^T ZF).
Let Z_*>=0 be a target with source PSD feasible fibre
  C={Z>=0:B_V(Z)=B_V(Z_*)},
and Y_*=F^T Z_* F.

Assume an EXPOSING CERTIFICATE
  S=B* w >=gamma Q, S P=0, gamma>0.
Then every exact ambient PSD competitor lies in P, and the exact lifted fibre is F^T C F, without any rank restrictions.

Define two finite-dimensional output subspaces:
  V_out=range(B_V), 
  K_out={B(K+K^T): K=P K Q}.
Their **transversality margin** is
  sigma=inf{ ||P_(K_out^perp) v||_2 : v in V_out, ||v||_2=1}.
The convention is sigma=1 if V_out={0}. We assume sigma>0, equivalently V_out intersect K_out={0}.

Let
  kappa=||w||_2/gamma,
  beta=||B||_(F->2),
  T=tr(Y_*)+sqrt(N)  (for B the two-basis map; more generally replace sqrt(N) by any measured-trace constant),
  a=(1+beta*kappa)/sigma.

## Theorem 1 (uniform arbitrary-ambient noisy transfer)

For every Y>=0 with delta=||B(Y-Y_*)||_2<=1, put Z=F Y F^T>=0. Then
  ||B_V(Z-Z_*)||_2 <= a delta,                                  (1)
  ||Y-F^T ZF||_F <= kappa delta+sqrt(2 T kappa delta).         (2)
Consequently the worst-case distance-to-fibre modulus obeys
  omega_lift(delta)
    <= omega_source(a delta)+kappa delta+sqrt(2 T kappa delta),
  omega_lift(delta)>=omega_source(delta),                      (3)
where the source modulus uses B_V and the ambient modulus uses B. The lower bound is exact because the face embedding is Frobenius-isometric and preserves B residual.

If the full cross-block measurement map K->B(K+K^T) is injective on {K=P K Q}, its smallest positive singular value eta>0 gives the stronger estimate
  omega_lift(delta) <= omega_source(a delta)+ C(delta),
where C(delta)=O(delta) with explicit coefficient depending on eta,beta,kappa,sigma. Thus the source modulus is preserved up to fixed multiplicative factors, including in the Lipschitz case.

If there exists nonzero K=R_* K Q with R_* the projector onto ran Y_*, satisfying
  B(K+K^T)=0,
then
  omega_lift(delta)>=c sqrt(delta),
and hence
  omega_lift(delta) ~ omega_source(delta)+sqrt(delta).          (4)
Here c>0 is an explicit function of K, Y_*^dagger and B(K^T Y_*^dagger K), which is nonzero because the trace is measured. For a non-Lipschitz source PSD modulus, omega_source(delta)>=c' sqrt(delta) by the standard tangent-cone dichotomy, so the entire modulus is preserved.

## Proof

Write Y in P/Q blocks:
  A=PYP=F^T ZF, B0=QYQ, K=PYQ.
Thus
  Y-Y_*=(A-Y_*)+(K+K^T)+B0.
By the exposing certificate,
  gamma tr B0 <=<S,Y>=<w,B(Y-Y_*)><=||w|| delta,
so tr B0<=kappa delta and ||B0||_F<=kappa delta.
Trace control gives trY<=T for delta<=1. Positivity and block Cauchy-Schwarz yield
  ||K||_F²<=tr(PYP)tr(QYQ)<=T kappa delta.
Since the P/Q decomposition is Frobenius-orthogonal,
  ||Y-A||_F²=2||K||_F²+||B0||_F²,
which implies (2).

Let Pi be the map from R^k to V_out which first projects orthogonally to K_out^perp and then inverts that projection on V_out. The transversality condition gives ||Pi||<=1/sigma. It satisfies Pi v=v for v in V_out and Pi u=0 for u in K_out. Apply Pi to the measurement decomposition:
  Pi B(Y-Y_*)=B_V(Z-Z_*)+Pi B(B0).
Thus
  ||B_V(Z-Z_*)||<=sigma^(-1)[delta+beta||B0||_F]
  <=a delta,
proving (1). The ambient distance to the lifted source fibre is at most
  dist(Z,C)+||Y-F^T ZF||,
so (3) upper follows. Its lower bound follows from restricting ambient competitors to embedded source PSD matrices.

If the full cross-map is injective, define a second bounded projection Pi_K onto K_out annihilating V_out, by the analogous direct-sum decomposition. Since ||Pi_K|| is bounded by a finite angle constant and since B(B0)=O(delta),
  ||B(K+K^T)||<=C0 delta.
Injectivity gives ||K||<=C0 delta/eta. Then ||Y-A||<=kappa delta+sqrt(2)C0 delta/eta, proving the stronger O(delta) term.

For the matching square-root obstruction, take K=R_*KQ nonzero with B(K+K^T)=0 and put G=K^T Y_*^dagger K>=0, G!=0. Define
  Y(t)=Y_*+t(K+K^T)+t²G
      =(I+tK^T Y_*^dagger) Y_* (I+tY_*^dagger K).
This is PSD of the SAME rank as Y_*, and the trace-preserving measurement assumption implies B(G)!=0. Its residual is t²||B(G)||, while its distance from every matrix supported on P is at least sqrt(2)t||K||. Taking t=sqrt(delta/||B(G)||) proves the lower bound and (4).

## Corollary: why the double-zero construction can lose a square root

For Milestone 21, the two frames have equal compressed nonzero data and the independent exterior cross-block directions affect the two lists differently. Unless the finite cross-image transversality test above succeeds, one cannot infer an O(delta) source residual merely from exterior mass O(delta). The general Milestone 21 upper estimate omega_source(C sqrt(delta))+C sqrt(delta) remains the valid unconditional statement; the sharper (3) requires checking sigma>0.

## Structural scope and audit

- The criterion involves only linear algebra on the given measurement map and the embedded face; no reflection, diagonal-data symmetry, graph or rank assumption is required.
- It is valid for nonsingleton source fibres because distance is taken to the ENTIRE exact PSD fibre.
- The exact square-root lower curve is PSD by a product factorization and competes among all ambient ranks.
- The source/residual transversality margin can be arbitrarily small; no dimension-only positive gap is asserted.
- The norm T must be obtained from a measured trace functional; in the two-basis setting the first list fixes trace and T=trY_*+sqrt(N) suffices.
- The full cross-map injectivity is a strong sufficient condition for no extra square-root term; the criterion is NOT stated as a necessary and sufficient classification of every PSD instance.
- The tangent-cone dichotomy for PSD moduli is a separate elementary result proved in the earlier Track 02 work; the precise assertion used is omega_source(t)=O(t) or omega_source(t)>=c sqrt(t).
- All comparisons are local for a fixed instance; none establishes uniform Turing bit complexity absent a lower bound on sigma or eta.
