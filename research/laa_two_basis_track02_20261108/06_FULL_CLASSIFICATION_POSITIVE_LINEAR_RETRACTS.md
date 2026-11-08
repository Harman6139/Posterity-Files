# Milestone 06 — complete normal form for positive linear PSD encoders with positive inverses

Date 2026-11-08. This is a rigorous finite-dimensional classification theorem. Its relation to known reversible positive maps and Euclidean Jordan retracts requires bibliographic priority work. It is NOT a universal near-quadratic two-basis representation theorem.

## Theorem (positive retract normal form)

Let J:S^m -> S^d and D:S^d -> S^m be positive real linear maps, D J=id. After discarding the common nullspace of J(I), there exist integers t>=1, k>=0 with mt+k=d, a fixed invertible real matrix C in GL_d(R), and a positive linear map
  T:S^m -> S^k,     T(S_+^m) subset S_+^k,
such that for every X in S^m,
  C^T J(X) C = (X tensor I_t) direct-sum T(X).                (1)
Conversely every such map admits a positive left inverse (normalized partial trace on the first summand), so this is an exact if-and-only-if classification, up to positive congruence and removal of a common nullspace.

Consequences:
(i) Every positive linear encoder with any positive decoder admits, after congruence, a canonical positive PRINCIPAL decoder.
(ii) The cross block of a positive encoder does not provide a new representation mechanism: it is forced by a fixed matrix and eliminated by fixed congruence.
(iii) To beat the generic quartic lower bounds in Milestones 01,02,05 while keeping a globally positive linear decoder, one MUST use a nonfaithful decoder and a genuinely matrix-valued positive companion T, with compressed order mt+k=O(m). The theorem does not assert that such a T exists for arbitrary dense measurement spaces.

### Proof

Step 1: normalize at the identity. J(I)>=0. If a vector u belongs to ker J(I), then for any 0<=X<=cI, 0<=J(X)<=cJ(I), so J(X)u=0. Since every symmetric X is the difference of PSD matrices, u lies in the kernel of all J(X). Restrict the output to S=supp J(I), where J(I)>0. Put R=J(I)^(1/2), and define
 Phi(X)=R^(-1)J(X)R^(-1),  Delta(Y)=D(RYR).
These maps are positive, unital and satisfy Delta Phi=id.

Step 2: recover the faithful Jordan subsystem. Put A=Delta*(I_m)>=0 and E=supp A. By positivity and a trace-zero argument, Delta(Y)=Delta(EYE) for every symmetric Y. The compressed maps
 Psi(X)=E Phi(X) E, delta(Y)=Delta(EYE)
are unital positive with delta Psi=id. They are faithful on the output: delta(Z)=0 and Z>=0 supported on E imply Z=0, because A>0 on E.

The real Kadison inequality for unital positive maps is Lambda(H^2)>=Lambda(H)^2; it follows from spectral decomposition H=sum lambda_i P_i and the isometry v -> (Lambda(P_i)^(1/2) v)_i. Apply it to Psi and delta:
  Psi(X^2)-Psi(X)^2>=0,
  delta(Psi(X^2))=X^2,
  delta(Psi(X)^2)>=delta(Psi(X))^2=X^2.
Positivity forces delta(Psi(X^2)-Psi(X)^2)=0, and faithfulness forces Psi(X^2)=Psi(X)^2. Polarization makes Psi a unital Jordan homomorphism.

For e_i=e_ie_i^T, its images P_i=Psi(e_i) are pairwise orthogonal projections summing to I_E. The images of E_ij=e_ie_j^T+e_je_i^T have only (i,j) off-diagonal blocks and square P_i+P_j, so each connects ran P_i and ran P_j by an orthogonal isomorphism. Their ranks are equal, say t. Choosing bases in the P_i via E_1i and using E_1i o E_1j=E_ij/2 identifies
  Psi(X)=X tensor I_t
on ran E of dimension mt. The m=1 and m=2 cases follow directly from the same matrix-unit argument.

Step 3: show the entire cross block has a forced form. In the decomposition ran E direct-sum E^perp, write
 Phi(X) = [ X tensor I_t,  C_0(X); C_0(X)^T, H(X) ].
For every u in R^m, Phi(uu^T)>=0. The upper diagonal block is (uu^T) tensor I_t and hence has range span(u) tensor R^t. Positivity of a block matrix forces the off-diagonal columns C_0(uu^T) to lie in the range of the upper block. Fix an ancillary index a=1,...,t and a column index j in E^perp. The corresponding m-vector c_a,j(uu^T) lies in span(u) for all u.

The polynomial rigidity lemma: if c:S^m->R^m is linear and c(uu^T) belongs to span(u) for every u, then c(X)=Xb for a fixed b in R^m. Indeed write p_i(u)=c_i(uu^T), homogeneous quadratic polynomials, and note u_i p_j-u_j p_i=0 for all u. For m>=2 the coordinate polynomials u_i,u_j are coprime, forcing p_i=u_i ell for a common linear form ell(u)=b^Tu. Thus c(uu^T)=uu^Tb, and rank-one symmetric matrices span S^m. The m=1 case is immediate.

Apply this lemma to all ancillary rows and auxiliary columns. There is a fixed matrix B of size (mt) by (d-mt) such that
  C_0(X)=(X tensor I_t) B
for every X.

Step 4: eliminate cross blocks. The constant block-triangular congruence
  M=[I_(mt) -B; 0 I_k]
satisfies
  M^T Phi(X) M = (X tensor I_t) direct-sum T(X),
  T(X)=H(X)-B^T(X tensor I_t)B.
Since Phi(X)>=0 whenever X>=0, T is a positive linear map. Combining this congruence with R and the orthogonal Jordan coordinate change yields C in (1). Conversely the normalized partial trace on the first block is positive and left-inverts X -> X tensor I_t direct-sum T(X). QED.

## Effective algebraic scope

Given exact J and D with rational/algebraic coefficients, the normal form can be constructed by eigenvalue decompositions, support computation of Delta*(I), orthogonal Jordan matrix-unit alignments, and linear block elimination. This uses a finite number of real algebraic operations. Uniform polynomial Turing bit complexity and well-conditioned numerics require positive separation margins for support spectra and for the congruence matrix C. The theorem makes no dimension-independent bounds on these margins.

## Hostile audit

- The decoder is faithful ONLY after compressing to supp Delta*(I). Without this step a false inference from delta(Z)=0 for Z>=0 to Z=0 would occur.
- The Jordan subrepresentation exists after unitalization by J(I)^(1/2). The original J need not itself be unital.
- The polynomial rigidity lemma requires positivity for all rank-one PSD inputs, not just at one feasible target. Therefore the classification is a GLOBAL positive-linear retract theorem, not a local theorem for an arbitrary chosen fibre.
- Even though J may have nonzero mixed blocks, they are necessarily (X tensor I_t)B and so can be eliminated without changing positivity.
- Nonfaithful decoder components are genuinely needed to escape tensor rank lower bounds; the classification does not prohibit a matrix-valued positive companion.
- A nonlinear encoder, decoder not globally positive, or non-face-embedded SDP extension is outside the theorem.
