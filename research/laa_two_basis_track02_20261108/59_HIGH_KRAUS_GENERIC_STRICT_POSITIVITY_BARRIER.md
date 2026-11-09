# Milestone 59 — generic high-Kraus CP decoders cannot reach ANY singular PSD output; explicit eigenvalue/error floor

Research Track 02, 2026-11-09. Complete real matrix-algebra theorem. It identifies a new tension in the remaining many-to-one quadratic two-basis SDP frontier: a large Kraus rank supplies enough free parameters to defeat earlier Grassmannian parameter counts, but GENERICALLY makes the decoder strictly positivity improving and therefore unable to reach boundary points of any proper PSD fibre. Successful high-Kraus quotients must lie in a special determinantal matrix-pencil locus. This is a generic architecture obstruction, NOT an impossibility for all high-Kraus channels or all two-basis SDP normal forms.

## 1. Main theorem

Let m>=2, d>=1, and t>=d+m−1. Consider REAL Kraus operators B_1,...,B_t in R^(m×d), defining a completely positive map
  D:S^d→S^m,
  D(Y)=sum_(a=1)^t B_a Y B_a^T.
For a unit source vector u, define the t-by-d real matrix pencil
  A_B(u)=[u^T B_1; ...; u^T B_t].
Let
  kappa_B=min_(||u||=1) sigma_min(A_B(u))>=0.

**Theorem A (generic uniform positivity improvement).** There is a nonempty real Zariski-open dense, full-Lebesgue-measure set of Kraus families B=(B_1,...,B_t) for which kappa_B>0. For every such family and every Y>=0,
  D(Y) >= kappa_B² (tr Y) I_m.                    (1)
Consequently every nonzero PSD input has a POSITIVE-DEFINITE decoded output, and no rank-deficient target X>=0,X!=0 lies in D(S^d_+).

This genericity remains valid after normalizing the Kraus family to make D TRACE PRESERVING, i.e. after replacing B_a by B_a G^(-1/2) where G=sum B_a^T B_a>0. The full-column-rank property of A_B(u) is preserved by the invertible common right factor.

### Proof

Fix any nonzero u. The linear map from all t Kraus matrices to A_B(u) is surjective onto R^(t×d): each row u^T B_a can be chosen arbitrarily by setting B_a=u row_a/||u||². The determinantal variety of t-by-d matrices with column rank <=d−1 has complex algebraic codimension t−d+1 (when t>=d).

Consider the incidence set
  I={(B,[u]) : [u] in P^(m−1), rank A_B(u)<=d−1}
inside the Kraus parameter space of dimension tmd and projective u-space of dimension m−1. Each fixed-u bad fibre has codimension t−d+1, so
  dim I <=tmd + (m−1) −(t−d+1)
         =tmd −(t−d−m+2).
When t>=d+m−1, the parenthesized defect is at least one. The projection of I to the B-parameter space is therefore a PROPER algebraic subset (the projective u-space makes the projection closed). Its complement is nonempty Zariski-open. Real points are dense, so it has real Euclidean open dense full measure. On this complement, A_B(u) has full column rank for every nonzero real u.

By continuity and compactness of the unit sphere,
  kappa_B=min_(||u||=1) sigma_min A_B(u)>0.

For any Y>=0 and any unit u,
  u^T D(Y)u
  =sum_a (B_a^T u)^T Y(B_a^T u)
  =tr(Y A_B(u)^T A_B(u))
  >=kappa_B² trY.
This holds for every unit u, proving (1).

For trace normalization, G=sum_a B_a^T B_a>0 on the generic class, and A_(B G^(-1/2))(u)=A_B(u)G^(-1/2) preserves full column rank. QED.

## 2. Quantitative approximation barrier

Suppose D is CP and has kappa_B>0, and put E=D*(I_m)=sum_a B_a^T B_a>0. Let beta=||E||_op. Let X>=0 be ANY singular matrix of trace tau>0 and let u be a unit vector in kerX.

For every Y>=0, put eta=||D(Y)-X||_* (nuclear norm). Trace comparison gives
  trD(Y)>=tau−eta
and
  trD(Y)=tr(EY)<=beta trY,
so
  trY>=(tau−eta)/beta
when eta<tau. By (1),
  u^T D(Y)u >=kappa_B² trY
                >=(kappa_B²/beta)(tau−eta).
Since u^T X u=0 and nuclear norm bounds every unit quadratic form,
  eta>=u^T D(Y)u.
Therefore
  eta >= [kappa_B²/(beta+kappa_B²)] tau.         (2)
If eta>=tau the same inequality is trivial. In the TRACE-PRESERVING case E=I_d, beta=1, yielding
  ||D(Y)-X||_* >= [kappa_B²/(1+kappa_B²)]tau
for EVERY Y>=0. This is an explicit, strictly positive source-output error floor independent of any two-basis measurement design or input witness-selection algorithm.

## 3. Characterization of the necessary nongeneric locus

If a CP decoder D has ANY nonzero singular source output D(Y)=X>=0 with kernel u and Y>=0,Y!=0, then
  0=u^TD(Y)u=tr(Y A_B(u)^T A_B(u)).
Both factors are PSD, hence suppY⊂ker A_B(u). In particular A_B(u) fails full column rank. Therefore every CP decoder whose image contains even one nonzero singular PSD matrix belongs to the determinantal incidence locus
  {B: exists 0!=u, rank A_B(u)<d}.               (3)

If an SDP fibre contains rank-(m−1) boundary points with an OPEN family of kernel directions (e.g. the rational arrow instance of Milestone 58), a decoder surjecting onto that fibre must satisfy rank A_B(u)<d for EVERY u in that open set. The maximal d-by-d minors of A_B(u) are homogeneous polynomials in u. Vanishing on a nonempty open subset makes them IDENTICALLY zero, so
  rank A_B(u)<d for ALL u∈R^m.                  (4)

This is a particularly strong algebraic rigidity requirement: a successful high-Kraus decoder for such a source fibre must yield a LINEAR SPACE OF COLUMN-RANK-DEFICIENT MATRICES A_B(u), not just one exceptional singular value direction. The structure of these singular matrix pencils is a concrete remaining frontier, related to bounded-rank linear matrix spaces and polynomial matrix syzygies.

## 4. Interpretation and hostile audit

- A large/minimal Kraus rank t by itself does NOT force strict positivity improvement; the result is GENERIC, and channels with special entanglement/partial-trace structure can surject onto all rank-deficient source matrices even at large t.
- The condition t>=d+m−1 is sufficient for generic all-u full column rank by projective incidence. No assertion of its sharpness for every m,d is made.
- The interval of source kernel directions in Milestone 58 is genuinely open; polynomial vanishing then implies the whole rank-deficient pencil condition (4).
- The error floor is a trace-norm bound for ALL PSD inputs, not a mere first-order perturbative estimate.
- The trace normalization uses a common invertible Kraus right factor, preserving the rank of every A_B(u); it is not claimed to preserve its exact numerical singular gap.
- This theorem does not require an encoder, an SDP optimization objective, two ONBs, positive observation data, or any assumptions on input PSD rank. It is a pure CP quotient obstruction.
- Arbitrary positive but non-CP decoders do not admit the Kraus matrix pencil representation and are outside this theorem.
- The high-Kraus dimensional regime needed to escape the prior Grassmannian parameter counts can still be viable on the SPECIAL singular-pencil locus. This theorem provides a precise algebraic target for a constructive counterdesign.
