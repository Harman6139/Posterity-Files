# Fresh analytic milestone 01 — exact Lipschitz certificates and the first-exposure invariant

Date: 2026-11-12. Parent research handoff: ff6117295c329dc88d5bc280ee18adfe64cda8b0.

**Status and scope.** The theorems below are proved for arbitrary finite real PSD linear systems, arbitrary nonempty feasible fibres, arbitrary singularity degree, and all ambient PSD competitors. No positive encoder, chosen witness section, unique solution, complete positivity, or strictly feasible lifted point is assumed. They characterize the quantitative SOUNDNESS requirement of the frontier. They do NOT establish near-quadratic universality or an unrestricted dimension lower bound. In particular, positive quotient completeness remains a separate requirement.

## 1. Definitions

Let M:S^n -> R^q be linear and let T={Y>=0:M(Y)=y} be nonempty. The matrix inner product is trace(FY); data norms are Euclidean. For F in S^n and c in R, consider

  |<F,Y>-c| <= K ||M(Y)-y||  for every Y>=0.                 (1)

Necessarily <F,Y>=c on T. Let K_*(F,c) be the least nonnegative K in (1), or infinity when there is none.

No trace-control or boundedness hypothesis is required in Sections 2–5.

## 2. Exact two-sided dual-certificate theorem

**Theorem 1.** For K>=0, inequality (1) holds if and only if there are lambda_+,lambda_- in R^q such that

  ||lambda_+|| <= K,   M*lambda_+ - F >= 0,   lambda_+ . y = c,
  ||lambda_-|| <= K,   M*lambda_- + F >= 0,   lambda_- . y = -c.       (2)

Consequently, when finite,

  K_*(F,c) = max{k_+(F,c), k_-(F,c)},

where k_+ is the minimum norm of a vector satisfying the first PSD/equality pair in (2), and k_- is the analogous minimum for the second pair. Both minima are attained. Empty certificate sets have minimum infinity.

### Proof: sufficiency

For any Y>=0, positivity of S_+=M*lambda_+-F gives

  <F,Y>-c = lambda_+ . (M(Y)-y) - <S_+,Y>
           <= ||lambda_+|| ||M(Y)-y||.

The second certificate bounds the negative of the same expression. This proves (1).

### Proof: necessity, with a compact finite-intersection argument

It suffices to derive the first certificate from the upper half of (1). Let B_K={lambda:||lambda||<=K}. For each Y>=0 define the affine function

  L_Y(lambda) = <F-M*lambda,Y> + lambda.y - c.

For every Y>=0 the assumed upper bound says

  min_{lambda in B_K} L_Y(lambda)
    = <F,Y>-c-K||M(Y)-y|| <= 0.                              (3)

We claim that some lambda in B_K has L_Y(lambda)<=0 simultaneously for all Y>=0. To prove it, first take finitely many Y_1,...,Y_s. If no common lambda existed, the compact convex set

  { (L_{Y_1}(lambda),...,L_{Y_s}(lambda)) : lambda in B_K }

would be disjoint from the closed negative orthant. Strict separation gives coefficients alpha_j>=0, sum alpha_j=1, with

  min_{lambda in B_K} sum_j alpha_j L_{Y_j}(lambda) > 0.

But this sum is L_{Ybar}(lambda), where Ybar=sum_j alpha_j Y_j>=0, contradicting (3). Thus every finite collection of the closed subsets {lambda in B_K:L_Y(lambda)<=0} has nonempty intersection. Compactness of B_K gives the claimed common lambda.

Now L_Y(lambda)<=0 for every PSD Y. Scaling Y through arbitrary positive multiples implies M*lambda-F>=0. Taking Y=0 gives lambda.y<=c. Taking any Y_0 in T and using the PSD slack gives

  0 <= <M*lambda-F,Y_0> = lambda.y-c.

Therefore lambda.y=c. This is the first certificate. Apply the same argument to (-F,-c) for the second certificate.

Each certificate set is closed. A nonempty closed set in finite-dimensional Euclidean space attains its minimum distance to zero, by restriction to a sufficiently large compact ball. The exact constant formula follows. QED.

**Important duality point.** This proof does not assume Slater's condition, closedness of an arbitrary linear image of the PSD cone, or attainment of an unrelated SDP dual. The uniform residual inequality itself forces the attained dual certificates.

## 3. Local soundness is already global soundness

**Theorem 2.** Fix Y_0 in T and suppose <F,Y_0>=c. If (1) holds with constant K for every PSD Y in any neighbourhood of Y_0, then it holds globally with exactly the same K. The same conclusion holds if it is initially assumed only when ||M(Y)-y||<=epsilon for some epsilon>0.

**Proof.** For arbitrary Y>=0 put Y_t=(1-t)Y_0+tY, 0<t<=1. Convexity gives Y_t>=0, and

  M(Y_t)-y=t(M(Y)-y),
  <F,Y_t>-c=t(<F,Y>-c).

Choose t>0 small enough for the stated local hypothesis, apply it, and divide by t. QED.

The proof applies unchanged to a vector-valued affine output and any norm. It is about an all-competitor Lipschitz inequality, not merely a bound along a selected parametrized family.

## 4. The first-exposure invariant

Define the cone of globally PSD measured zero stresses

  C_0 = {M*eta : M*eta>=0, eta.y=0}.

Choose S_0 in C_0 of maximum rank. Such an element exists because the set is nonempty (it contains zero), and its attainable ranks belong to {0,...,n}. Write S_0=M*eta_0, and set

  R = range(S_0),  E = ker(S_0).

If C_0={0}, use R={0}, E=R^n, S_0=0. Every S in C_0 is supported on R: otherwise S+S_0, still in C_0, would have larger rank. Here we use ker(S+S_0)=ker(S) intersect ker(S_0) for PSD matrices.

Let S(R) denote the linear space of symmetric matrices supported on R, namely T=P_R T P_R. This includes neither E-E terms nor E-R cross terms.

**Theorem 3 (exact stable-observable space).** The set of all F for which there exist c and finite K satisfying (1) is exactly

  V_Lip = range(M*) + S(R).                                 (4)

The value c is uniquely determined by F and the nonempty fibre T. If

  F=M*lambda+T_R,  T_R in S(R),

then c=lambda.y. For nonzero R define

  beta=|| (S_0|_R)^(-1/2) (T_R|_R) (S_0|_R)^(-1/2) ||_op.

A valid explicit bound is

  K_*(F,c) <= ||lambda|| + beta ||eta_0||.                   (5)

For R={0}, T_R=0 and beta=0.

### Proof: necessity

Obtain the two certificates of Theorem 1, and let

  S_+=M*lambda_+-F>=0,
  S_-=M*lambda_-+F>=0.

Their sum is M*(lambda_++lambda_-), and its data pairing is c-c=0. Thus S_++S_- belongs to C_0 and is supported on R. Since 0<=S_+,S_-<=S_++S_-, both slacks are supported on R. Hence F=M*lambda_+-S_+ belongs to the right side of (4).

### Proof: sufficiency and constants

Every Y_0 in T obeys <S_0,Y_0>=eta_0.y=0. PSD positivity then forces Y_0 to be supported on E. Consequently <T_R,Y_0>=0 and c=lambda.y.

The definition of beta gives the Loewner inequalities

  -beta S_0 <= T_R <= beta S_0.

For arbitrary Y>=0, therefore,

  |<T_R,Y>| <= beta <S_0,Y>
              = beta eta_0.(M(Y)-y)
              <= beta ||eta_0|| ||M(Y)-y||.

Combining this with the measured term proves (5). Alternatively, explicit certificates are lambda_+=lambda+beta eta_0 and lambda_-=-lambda+beta eta_0, with slacks beta S_0-T_R and beta S_0+T_R. QED.

### Consequences and precise meaning

1. Only the **first globally PSD exposure** appears in (4). E may be strictly larger than the minimal feasible support. Later facial-reduction certificates, positive only after restriction, cannot be substituted for members of C_0.
2. The relevant correction space is supported on the RANGE R of the stress, i.e. the directions removed by that exposure. It is not the space supported on its kernel.
3. If T contains a positive-definite matrix, C_0={0}; thus V_Lip=range(M*).
4. If the first exposure already reaches the minimal face, (4) also forbids uncontrolled E-R cross terms. This specializes the strict-stress criterion in historical Milestone 28 but requires neither uniqueness nor a supported rank-one observable.
5. The algebraic annihilator is V_Lip^perp=ker(M) intersect S(R)^perp. At high singularity degree a vector in this annihilator need not itself yield a quadratic feasible curve at a chosen solution; no universal square-root exponent is asserted here.
6. Maximum-rank stress selection is an existence statement, not an assertion that exact facial reduction is unconditionally polynomial-time in the Turing model.

## 5. Vector residuals and the actual two-basis frontier

Let A:S^m->R^p, let D:S^n->S^m be linear, and put F_i=D*(A_i), where A_i is the i-th source measurement matrix. Then

  ||A(D(Y))-b||_2 <= K ||M(Y)-y||_2 for every Y>=0           (6)

implies that each (F_i,b_i) has the certificate pair (2) with norms at most K. Conversely, if each pair has certificates of norms at most K_i, then (6) holds with K=(sum_i K_i^2)^(1/2).

An exact operator-norm formulation is also available: (6) is equivalent to the upper certificate for every u in the unit sphere of R^p,

  ||lambda_u||<=K,
  M*lambda_u-D*A*u>=0,
  lambda_u.y=u.b.

No continuity or linear dependence of lambda_u on u is required.

For a more directly computable sufficient bound, suppose

  F_i=M*lambda_i+T_i,  T_i supported on R,  b_i=lambda_i.y.

Let Lambda have rows lambda_i^T and define beta_i using T_i as in Theorem 3. Then

  ||A(D(Y))-b||_2
   <= [||Lambda||_(2->2)+||beta||_2 ||eta_0||_2] ||M(Y)-y||_2.       (7)

If gamma=lambda_min(S_0|_R)>0, beta_i<=||T_i||_op/gamma. This displays the exposure conditioning explicitly; no uniform gap in a degenerate system is claimed.

For the frontier, set M=B_U, the two complete basis-diagonal map. Then range(M*) is precisely the sum of the two diagonal symmetric operator spaces. Equations (2) and (4) are necessary and sufficient for finite all-PSD decoded residual control for the FIXED proposed design (U,y,D). They remain valid for singular lifted supports, arbitrary positive non-CP decoders, and nonlinear/nonunique witness selection.

If D is globally positive and exact completeness D(T)=F_b has separately been proved, the source modulus immediately gives

  dist_F(D(Y),F_b) <= omega_b(K ||B_U(Y)-y||).

Every source cost C has exact ambient pullback D*C on all symmetric matrices. These conclusions concern decoded source distance and objectives. They do not identify ambient distance to T and do not prove any sharp ambient bi-Hölder law.

## 6. Adversarial audit and remaining frontier

- All statements quantify over the full ambient PSD cone, without rank restrictions.
- T is only required to be nonempty; zero targets, nonsingleton fibres and higher-depth faces are included.
- The certificate proof avoids any unjustified SDP dual-attainment assumption.
- Local-to-global extension uses an actual PSD segment, not a tangent-space approximation.
- First exposure and the minimal feasible face are deliberately distinguished.
- The vector criterion does not assume a single linear certificate selector u -> lambda_u.
- These theorems verify soundness for a supplied design. They do not construct an admissible design, prove positive surjectivity, or bound N.
- In particular they do NOT close the unrestricted N=O(m^2+p) frontier. The missing universal step remains the construction, or unrestricted exclusion, of a positive surjective two-basis quotient of that order satisfying these certificates with controlled constants.

All proofs above are self-contained finite-dimensional arguments. External priority is not claimed. Historical context: Milestones 09 (minimal-face tangent surjection), 22 (sufficient transverse exposure), 28 (strict-stress supported observable criterion), and 49–60 (full-rank/two-MASA and decoder-specific obstructions).
