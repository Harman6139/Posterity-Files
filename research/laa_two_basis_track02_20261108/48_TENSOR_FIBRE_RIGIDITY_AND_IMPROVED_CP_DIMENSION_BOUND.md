# Milestone 48 — sharp tensor fibre-covering rigidity and an improved CP fixed-diagonal density-shadow lower bound

Date: 2026-11-08. Two complete REAL linear-algebra results. The first, a sharp polynomial-syzygy dimension theorem for subspaces meeting every rank-one tensor fibre, is independently useful. Its application strengthens the earlier CP density-state input-order obstruction from n>=2m+1 (Milestone 42) to n>=2m+2 for every m>=3. The general POSITIVE but non-CP decoder lower bound remains n>=2m+1 (Milestone 43). This is NOT an unrestricted O(m²+p) universality impossibility theorem.

## 1. Sharp tensor fibre-covering lemma

Let m>=2, t>=1, and V be a real linear subspace of R^m tensor R^t. For u in R^m define its product fibre
  K_u={w in R^t:u tensor w in V}.

**Theorem A (sharp 2m−1 threshold).** Suppose dim K_u>=1 for a Zariski-dense set of real nonzero u (it suffices for every u or for all u in a nonempty Euclidean open set). If
  dim V <=2m−2,
then a NONZERO ancilla vector w0 exists with
  R^m tensor span(w0) subset V.                     (1)

The threshold is sharp: in R^m tensor R², the hyperplane
  V={A in R^(m×2): A_11+A_22=0}
has dimension 2m−1 and dim K_u>=1 for EVERY u, but contains NO full tensor factor R^m tensor w0 with w0!=0.

### Proof

Let Q=(R^m tensor R^t)/V and π be its quotient map. Write x=(x_1,...,x_m) as algebraically independent variables. The matrix of the linear map
  L(x):R(x)^t ->Q tensor R(x),  w ->π(x tensor w)
has entries that are homogeneous linear polynomials in x. By the generic nonzero-fibre hypothesis, its maximal minors vanish as polynomials, so L(x) has nonzero kernel over the rational function field R(x_1,...,x_m).

Solve the linear system over that field, clear denominators, and take a nonzero homogeneous component. This produces a nonzero vector
  w(x)=(w_1(x),...,w_t(x))
of HOMOGENEOUS polynomials of the same degree h>=0 satisfying
  π(x tensor w(x))=0
as an identity of vector-valued polynomials.

Every coefficient vector of x tensor w(x) lies in V. If all polynomial components w_j(x) are scalar multiples of one polynomial f(x), write w(x)=f(x)w0 for constant nonzero w0. The polynomial identity in the integral domain R[x] implies π(x tensor w0)=0 for all x, so R^m tensor w0⊂V, proving (1).

Otherwise choose two linearly independent homogeneous polynomial components f=w_i and g=w_j of the same degree. Consider the space of homogeneous polynomials
  f S_1+g S_1
of degree h+1, where S_1=span{x_1,...,x_m} has dimension m. Multiplication by a nonzero polynomial is injective, so both fS_1 and gS_1 have dimension m. Their intersection has dimension AT MOST ONE: if fℓ=gk with nonzero linear forms ℓ,k, then f and g being independent forces ℓ and k to be relatively prime; any second relation fℓ'=gk' must have ℓ' a scalar multiple of ℓ and k' the same multiple of k, by unique factorization. (If no such relation, the intersection is zero.) Hence
  dim(fS_1+gS_1)>=2m−1.

The coefficient matrix of the vector-valued polynomial x tensor w(x), considered as a vector in R^m tensor R^t with coordinates indexed by (a,j), has rank equal to the dimension of the linear span of its coordinate polynomials {x_a w_j(x)}. This span contains fS_1+gS_1, so the coefficient vectors span a subspace of V of dimension at least 2m−1. This contradicts dimV<=2m−2. Therefore the first case must occur, proving (1).

For sharpness, the stated trace-hyperplane V has K_u={w:u_1 w_1+u_2w_2=0}, a nonzero subspace for every u. If R^m tensor w0 lay in V, testing u=e1,e2 would force w0_1=w0_2=0, contradiction. QED.

## 2. Improved input-order obstruction for CP decoders

**Theorem B.** Let m>=3, tau>0 and let D:S^n ->S^m be a REAL completely positive TRACE-PRESERVING linear map. Suppose there exist an orthonormal input basis f_1,...,f_n and a PSD set T with fixed first-basis diagonal a such that
  D(T)={X>=0:trX=tau}.
Then necessarily
  n>=2m+2.                                        (2)

This holds for arbitrarily nonlinear many-to-one lift choices, arbitrary ancillary Kraus rank, all PSD input ranks, and ANY additional orthonormal-basis measurements. It strengthens Milestone 42 by one further dimension in every m>=3. It does not apply to merely positive non-CP decoders.

### Proof

Milestone 42 already proves n>=2m. For contradiction assume n=2m+1. Let
  D(Y)=sum_(a=1)^t B_a Y B_a^T,
  sum_a B_a^T B_a=I_n,
and define its explicit real Stinespring isometry
  V_iso:R^n ->R^m tensor R^t,
  V_iso z=sum_a B_a z tensor e_a.
Write H=ran V_iso (a linear tensor subspace of dimension n). For each real unit source u, define
  K_u={w:u tensor w in H}.

A pure source output tau uu^T has a PSD input preimage supported entirely on V_iso^T(span(u) tensor R^t), by marginal positivity. Consequently dim K_u>=1 for all u. If dim K_u=1, its positive preimage is uniquely rank-one, trace tau. Since a fixed real first-basis diagonal allows only finitely many rank-one PSD matrices (coordinates have fixed magnitudes and finitely many sign patterns), dimK_u=1 can occur for only finitely many projective source directions. Therefore
  dimK_u>=2
for all but finitely many [u] in real projective space.

Choose an ORTHONORMAL basis e_1,...,e_m of the source avoiding the finite exceptional directions. Their fibres W_i=K_{e_i} all have dimension >=2. The tensor subspaces e_i tensor W_i are mutually orthogonal and lie in H, so
  sum_i dim W_i <=dim H=2m+1.
There are exactly two possibilities:

Case I: one W_i has dimension 3 and all others have dimension 2, giving sum dimensions 2m+1=dim H. Then
  H=direct_sum_i (e_i tensor W_i).
For any generic u=sum_i c_i e_i with all c_i!=0, its product fibre equals
  K_u=intersection_i W_i.
It has dimension >=2 for generic u, so the intersection contains a 2-dimensional fixed ancilla space W0 and
  R^m tensor W0 subset H.

Case II: every W_i has dimension 2. The direct sum
  B=direct_sum_i(e_i tensor W_i)
has dimension 2m and codimension one in H. Write H=B direct-sum span{R} for a fixed nonzero tensor R; express R=sum_i e_i tensor r_i. For a generic u=sum_i c_i e_i with every c_i!=0, membership u tensor w∈H means there is scalar λ with
  c_i w −λ r_i∈W_i for every i.
Let Q_i=R^t/W_i and consider the linear map
  Λ_u:R^t -> direct_sum_i Q_i,
  Λ_u(w)=(c_i[w]_(Q_i))_i.
Its kernel is the common intersection W_int=intersection_i W_i, and Λ_u(K_u) lies in the ONE-dimensional span of ([r_i]_(Q_i))_i. Hence
  dim K_u<=dim W_int+1.
Since dim K_u>=2 generically, W_int contains some nonzero w0. Thus
  R^m tensor w0 subset H.

Split the ancilla orthogonally as R^t=span(w0) direct-sum B'. Since H contains the entire tensor core R^m tensor w0, it decomposes as
  H=(R^m tensor w0) direct-sum H',
  H' subset R^m tensor B',
with
  dim H'= (2m+1)−m=m+1.
The product fibres of H' have dimension dimK_u−1>=1 for generic u. Since m>=3 implies m+1<=2m−2, Theorem A forces a SECOND independent common ancilla vector w1 in B':
  R^m tensor w1 subset H'.
Therefore H contains a fixed full two-dimensional tensor subsystem
  C=R^m tensor W0, dim W0=2.

In both cases H contains C. In Case I H=C. In Case II its orthogonal complement in H has dimension one. Thus for ALL but finitely many projective source directions u, EVERY product tensor u tensor w in H lies in C. Indeed a one-dimensional complement can contribute a product tensor only for one first-factor projective direction (if its spanning tensor has rank one), or for none (if its tensor rank exceeds one).

Choose any input basis vector f_j with prescribed diagonal a_j>0; such an index exists because trace preservation makes sum_j a_j=tau>0. Let z_j=V_iso f_j in H. Project it to C, obtaining z_j^C. The corresponding partial trace effect
  E_j^C=Tr_(W0)(z_j^C (z_j^C)^T)
is PSD of rank at most dimW0=2.

For a generic unit source u, every exact PSD preimage Y_u of tau uu^T has its Stinespring image V_iso Y_u V_iso^T supported inside u tensor W0. Its trace is tau and therefore
  0<=V_iso Y_u V_iso^T <=tau P_(u tensor W0).
Consequently
  a_j=f_j^T Y_u f_j
     =z_j^T (V_iso Y_u V_iso^T) z_j
     <=tau z_j^T P_(u tensor W0)z_j
     =tau u^T E_j^C u.
The inequality holds for all u outside a finite projective set and hence, by continuity, for EVERY unit u. This forces
  E_j^C >=(a_j/tau)I_m>0,
contradicting rank E_j^C<=2<m. Therefore n=2m+1 is impossible and (2) holds. QED.

## 3. Corollary: polynomially stable approximation has a strict error floor at n<=2m+1

For fixed m>=3, n<=2m+1 and tau>0, there is a constant c(m,n,tau)>0 such that NO sequence of real first-basis designs and CPTP decoders of order n can approximately lift EVERY pure source state with both first-basis diagonal residual and decoded trace-norm error tending to zero. The proof is the same compactness argument as Milestone 42, but now Theorem B excludes all n<=2m+1. A positive quantitative error floor follows, though an explicit polynomial-in-m value is not derived. The result is unconditional with respect to decoder coefficients and nonlinear input witness selections, but requires exact CPTP structure.

## Scope and audit

- The tensor lemma is SHARP at 2m−1 and its polynomial-syzygy proof works over real scalars; no unproved existence of a rational section is needed because each product fibre is the kernel of a LINEAR pencil in w.
- The first common tensor factor is forced by a 1-dimensional residual space. The second common factor follows only after the sharp tensor lemma; it is not inferred from a false assertion that generic product fibres always share common ancilla vectors.
- The fixed-basis rank-one finiteness counts real sign choices; over complex Hilbert spaces continuous phases invalidate the same proof.
- The output effect E_j^C is built from the projection of the INPUT basis vector into the fixed two-copy core. The rank<=2 obstruction applies to almost every pure source lift, not to the full output effect D(f_jf_j^T), which may have full rank from decoder-invisible ancillary coordinates.
- The lower bound n>=2m+2 is still LINEAR in m and does not refute unrestricted n=O(m²+p) weak two-basis universality.
- The theorem is not claimed for globally positive non-CP decoders; their n>=2m+1 obstruction remains in Milestone 43.
- No novelty priority or external peer review is claimed; this is a self-contained proof and an independently reusable tensor fibre-covering lemma.
