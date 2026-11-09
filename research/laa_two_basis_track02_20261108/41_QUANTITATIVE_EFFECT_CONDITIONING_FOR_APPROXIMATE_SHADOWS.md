# Milestone 41 — sharp spectral conditioning inequality for approximate fixed-diagonal positive PSD shadows

Date 2026-11-08. A quantitative refinement of Milestones 39–40, proved for EVERY globally positive trace-preserving decoder, without complete positivity, an encoder, any bound on the lifted PSD ranks, or an exact feasible-fibre correspondence.

## Theorem 1 — approximate pure-state completeness forces positive basis effects

Let D:S^n ->S^m be real linear, positive and trace preserving. Let f_1,...,f_n be an ONB of R^n and E_j=D(f_jf_j^T)>=0, tr E_j=1. Let tau>0, a_j>=0 be prescribed first-basis diagonal observations. Suppose for every unit u∈R^m there is Y_u>=0 with
  ||diag_f Y_u-a||_2 <=epsilon,
  ||D(Y_u)-tau uu^T||_* <=eta,
where ||.||_* is nuclear trace norm and epsilon,eta>=0.

Then for every j,
  sqrt((a_j-epsilon)_+)
     <=sqrt((tau+eta) lambda_min(E_j))+sqrt(eta),       (1)
and consequently
  lambda_min(E_j)
    >= [max(0,sqrt((a_j-epsilon)_+)-sqrt(eta))]^2/(tau+eta).
                                                               (2)
For epsilon=eta=0 this recovers the EXACT full-rank effect condition
  E_j>=(a_j/tau)I_m
of Milestone 39.

For any CP decoder with Kraus count t<m, every E_j has a zero eigenvalue, so (1) yields
  a_j<=epsilon+eta   for every j,
  epsilon+eta>= (sum_j a_j)/n.
Thus Theorem 1 contains the sharp all-pure-state low-Kraus approximation floor of Milestone 37 as a direct corollary.

### Proof

Fix an index j. Let u be a unit eigenvector of E_j corresponding to e=lambda_min(E_j); completeness supplies Y=Y_u>=0. Write
  A=D*(uu^T).
Since D is positive trace preserving, its adjoint is positive and unital, so 0<=A<=I_n. Let
  alpha=tr(AY)=u^T D(Y)u,
  beta=tr((I-A)Y)=tr[(I_m-uu^T)D(Y)].
The nuclear norm error implies
  0<=alpha<=tau+eta,
  0<=beta<=eta,
because the target tau uu^T has zero mass on I_m-uu^T and both output and dual projections are PSD.

For any unit f=f_j, decompose
  f=A^(1/2) A^(1/2)f + (I-A)^(1/2)(I-A)^(1/2)f.
Apply Y^(1/2) and the triangle inequality:
  ||Y^(1/2)f||
  <=||Y^(1/2) A^(1/2)||_op ||A^(1/2)f||
   +||Y^(1/2)(I-A)^(1/2)||_op ||(I-A)^(1/2)f||.
The first operator norm squared is at most the trace
  tr(A^(1/2)Y A^(1/2))=alpha;
the second is at most beta. Moreover
  ||A^(1/2)f||²=f^TAf=u^T E_j u=e,
  ||(I-A)^(1/2)f||²=1-e<=1.
Therefore
  sqrt(f^T Y f)
    <=sqrt(alpha e)+sqrt(beta(1-e))
    <=sqrt((tau+eta)e)+sqrt(eta).
The coordinatewise first-basis residual bound implies f^TYf>=a_j-epsilon, hence (1). Squaring after moving sqrt eta and truncating at zero proves (2). QED.

## Theorem 2 — faithful non-trace-preserving version

Let D be positive with E=D*(I_m)>0. For each basis vector f_j define
  w_j=E^(-1/2) f_j,
  F_j=D(E^(-1) f_j f_j^T E^(-1)).
Assume the same approximate pure-output completeness and first-basis residuals epsilon,eta as Theorem 1. Then
  sqrt((a_j-epsilon)_+)
  <=sqrt((tau+eta)lambda_min(F_j)) + ||w_j|| sqrt(eta).
                                                               (3)
Consequently
  lambda_min(F_j)
    >=[max(0,sqrt((a_j-epsilon)_+)-sqrt(eta f_j^T E^(-1)f_j))]^2/(tau+eta).
                                                               (4)
The exact limit yields the faithful positive effect lower bound of Milestone 40.

Proof. Normalize the decoder by Dhat(Z)=D(E^(-1/2) Z E^(-1/2)), which is positive TP, and transform a witness Y into Z=E^(1/2) Y E^(1/2). Then Dhat(Z)=D(Y), and the original basis functional is f_j^TYf_j=w_j^TZ w_j. Repeat Theorem 1's two-term operator Cauchy–Schwarz calculation with the NONUNIT vector w_j. The first term contains w_j^T Dhat*(uu^T)w_j =u^TF_j u, while the second has norm at most ||w_j|| sqrt eta. QED.

## Interpretation and scope

- This is a NECESSARY CONDITION for all-tolerance weak universality on the trace-only source SDP, not a sufficient construction or a dimension lower bound for arbitrary noncommuting constraints.
- A positive first-basis target coordinate a_j bounded away from zero imposes a positive effect eigenvalue margin whenever epsilon and eta are small compared with a_j. This quantitatively rules out almost-singular effects in uniformly conditioned designs.
- For an unnormalized or ill-conditioned decoder, the faithful version correctly records the inverse trace-effect conditioning f_j^T E^-1 f_j. This term must not be silently dropped.
- Frobenius output error η_F can be used by replacing eta with sqrt(m) η_F.
- The operator-norm versus trace estimates are valid over REAL symmetric matrices and require only positivity/unitality of the adjoint.
- The result does not eliminate high-Kraus-rank decoders with well-conditioned effects, singular-trace-effect decoders with extra positive companions, or nonlinear source-specific quotients. These remain candidates for the unrestricted O(m²+p) frontier.
