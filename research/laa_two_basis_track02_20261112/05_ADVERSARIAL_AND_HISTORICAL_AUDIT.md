# Milestone 05 — adversarial audit and precise frontier resolution

Date: 2026-11-12.
Branch: laa-track02-gptpro-analytic-frontier-20261112.
Historical corpus pinned at ff6117295c329dc88d5bc280ee18adfe64cda8b0.

## 1. Conclusion and exact scope

The construction and proofs in 02, with the conditioning/complexity guarantees in 03–04, establish the positive alternative in the handoff's unrestricted representation model:

  N=9m^2+4m+3+2p=O(m^2+p),
  D(Y)=VYV^T, VV^T=I_m,
  D({Y>=0:B_U(Y)=Phi b})={X>=0:A(X)=b},
  ||A(D(Y))-b||_2<=K_r||B_U(Y)-Phi b||_2 for EVERY Y>=0.

The theorem is uniform in dimensions, ranks, target degeneracies, source singularity degree, dense/noncommuting source measurements, redundant equations, non-singleton fibres and inconsistent data. No source solution, source strictly feasible point, facial-reduction sequence or target rank is supplied to the construction.

The algebraic proof is complete for this model. It is not an architectural impossibility theorem, a linear-inclusion conjecture, or a result deduced from finite test cases. Its correctness has not been certified by an independent external referee, and literature priority has not been established.

Computational scope is stated explicitly: polynomial-bit exact construction when a rational positive trace certificate is supplied; a rational certificate-finding algorithm polynomial in the declared numerical inverse cone margin when it is not. Every individual algebraic output coefficient has degree at most two and polynomial bit length in the certificate-input model. This is not a claim of unconditioned polynomial-time exact SDP solving.

The theorem transfers decoded source distance through the source's actual recovery modulus, preserves every objective exactly, and transfers weak-feasibility gaps in both directions. It does NOT assert a prescribed rank amplification, exact preservation of facial depth, all-nonzero basis overlaps, a nonreflection basis change, or the older sharp law for distance to the entire ambient lifted fibre. Those extra requirements are not silently substituted for the handoff's unrestricted positive-quotient model.

## 2. Load-bearing proof audit

### A. Positivity of the forward lift is global

For any PSD X, t=<H,X> and rho H>=I imply 0<=X<=rho t I. The base block in J(X) is orthogonally equivalent to X direct-sum (rho t I-X). The arrow block has the exact Schur-complement lower bound 3 alpha t I/4 when t>0. When t=0, X=0 and both blocks vanish. This uses no source feasibility assumption or target-dependent positive gap.

### B. The decoder never subtracts a Schur complement

D(Y)=VYV^T is a genuine compression, with VV^T=I. Thus PSD positivity, Frobenius contraction, and exact objective pullback hold on the FULL ambient PSD cone. No indefinite correction or competitor-dependent normalization is used.

### C. Entry-copy identity includes every unwanted cross term

For each ordered source entry, the four coefficients 1,s,u,-su are distinct characters of the two-sign group. Multiplication by s and summation isolates exactly 8(Z_(a,q_ij)-Z_(l_i,r_j)). It removes diagonals and all other cross terms, whether or not those cross terms vanish in a candidate reverse lift. The reverse proof does not assume the chosen forward block structure.

### D. Source equations are an exact linear identity

The explicit R_0 in 02 satisfies A D_0=R_0 M_raw on the entire symmetric matrix space and R_0 c^0(b)=b for every datum. These are matrix identities, not statements restricted to J(X) or to a feasible tangent space. The squared row-norm bound in 02 gives a displayed polynomial residual constant without inversion of a source analysis map.

### E. Parseval completion does not overconstrain source points

The nondiagonal part of the raw frame operator occurs only in the auxiliary covariance block. Every forward J(X) has that block equal to alpha tr(HX)I. Therefore every completion observation has a value determined by the trace datum alone. All raw observations are retained. Completion can only restrict auxiliary freedom, never remove any forward lift or create a spurious decoded source point.

The completion matrix lies between I/2 and I. Rational LDL factorization is therefore uniformly separated from zero pivots. This avoids an unproved admissible-orthonormal-basis selection step and avoids orbit-search conditioning entirely.

### F. There are exactly two complete physical bases

F=[sqrt(2/3)I,G/sqrt(3)] is a coisometry. U=2F^TF-I is a real orthogonal matrix. The measurements are precisely diag Y and diag(U^T Y U), with N coordinates in each list. There is no third measurement family in the output: all intermediate rank-one data are recovered from these lists after the proved exposure and averaging identities.

### G. The exact reverse argument treats the entire fibre

With Delta=diag(-I_d,2I_M), the stress S=Delta+U Delta U=2Q Delta Q satisfies S>=2Q. The prescribed data pair to zero with its multiplier for EVERY b. Every exact PSD solution therefore lies in ran(F^T), and the exact full-fibre identity is

  T_b={F^T ZF:Z>=0,M_G(Z)=c(b)}.

This is not replaced by T_b=E(F_b). The latter identity generally fails and is not required. Any Z in the displayed set decodes correctly by the raw operator identity, and every feasible source X has the explicit positive lift J(X).

### H. Noise estimates are global, not rank-restricted

For arbitrary Y>=0, positivity gives tr(QYQ)<=sqrt((d+4M)/2) delta. Reflection averaging cancels both support-to-exterior cross blocks exactly. The remaining diagonal of QYQ has Euclidean norm at most its trace. These statements yield the global constant K_r of 02 for all residual sizes and all target data. No assumption of a positive-definite ambient point is hidden in the proof.

The explicit two-sided dual multipliers in 02 independently certify both signs of each decoded source residual on the entire PSD cone. They satisfy the necessary-and-sufficient first-exposure criterion in 01, not merely its compression to an exact feasible face.

### I. Hostile Schur-complement perturbations

Take an exact Y_0 and any cross block K=P K Q whose column range lies in range(Y_0). The repaired curve

  Y(s)=Y_0+s(K+K^T)+s^2 K^T Y_0^dagger K

is PSD by its exact Gram factorization. Even when its linear measured variation cancels, it cannot produce a hidden first-order decoded source error: VQ=0, so D(Y(s))=D(Y_0) identically. Arbitrary perturbations inside P are controlled by the exact raw source-operator identity, and arbitrary mixtures of inner and outer perturbations are covered by the global averaging proof. This specifically addresses the mechanism behind the historical double-zero exponent-halving counterexamples.

### J. Degeneracy and closed-image checks

The same formulas apply at m=1, at rank-one source points, at zero data, and with zero or duplicate measurement rows. At zero data, the first complete diagonal forces Y=0; trace control forces X=0. Infeasible data yield no exact lifted point by soundness, and feasible data yield one by J.

Both relevant cone images are closed for explicit reasons: convergence of source data bounds source trace through H; convergence of two-basis data bounds lifted trace through the first diagonal. The proof never asserts that arbitrary linear images of PSD cones are closed.

## 3. The historical 4-by-4 obstruction is genuinely bypassed

Milestones 62–64 use the rational source map

  A(X)=(X13,X14,X23,X24,X34,
        X11-X22-2X33,X12-X44,tr X),
  b=(0,0,0,0,0,0,0,6).

Its homogeneous cone has a dual slice with a nonexposed extreme point, excluding positive images of an UNCONSTRAINED spectraplex at every finite order. The new theorem gives N=179 for this very instance. It uses essential copy and source-equation constraints on the inner PSD matrix; that inner fibre is not an unconstrained trace slice. Thus it does not contradict or assume away the historical obstruction.

An analytic witness that the lifted fibre is larger than the encoder image is also available here. The auxiliary block has order 16, so its symmetric space has dimension 136. Its measurements impose at most 16 coordinate conditions, 8 source quadratic conditions, and 16 completion conditions, hence at most 40 linear conditions. There is a nonzero auxiliary-supported symmetric T annihilated by every frame measurement. The source point

  X=[[3,1,0,0],[1,1,0,0],[0,0,1,0],[0,0,0,1]]

is positive definite, and J(X) is positive definite for H=I,rho=4. Consequently J(X)+eta T is PSD for all sufficiently small |eta|, has precisely the same frame data, and decodes to X. The matrix F^T(J(X)+eta T)F differs from E(X) when eta is nonzero. Since DE=id, it cannot equal E(X') for any other X'. This proves, without numerical rank assumptions, that the quotient is genuinely many-to-one.

The numerical audit additionally found an auxiliary nullity of 109 in this instance; that particular number is only a floating-point diagnostic. The proof above needs merely the exact lower bound 136-40=96.

## 4. Historical obstruction map

The following is a scope comparison, not an assertion that every inherited proof has received a new independent referee-level verification.

- **01–10, 46–48: exact positive retracts and restricted companions.** The new design has positive E,D with DE=id, but does not require the full fibre to equal E(F_b). Its auxiliary arrow is not a bounded collection of source-sized trace-affine congruence blocks. Therefore the exact-bijection kernel identity and low-rank pullback caps used in these lower bounds do not apply.
- **09 and 57: quotient slack tradeoffs.** These are compatible with the construction. The inner support has order d=(m+1)^2 and, in regimes p=O(m^2) with a positive-definite inner point, it has Theta(m^4) affine freedom invisible to the decoder. The construction realizes the permitted large-slack alternative rather than refuting the tradeoff.
- **11–13: compactness and affine-isomorphism lower bounds.** The new reduction is already exact; its large quotient fibres are not affine-isomorphic to the source fibres.
- **14–20 and 36–45,48: fixed-diagonal pure-state and faithful-effect barriers.** The decoder has singular trace effect V^T V of rank m. It is not trace preserving on the ambient cone and is not faithful. Its pure-source lifts may be mixed and nonunique. Assumptions requiring faithful trace effect, a prescribed marginal architecture, or unique pure lifts are not present.
- **21–30: zero-exposure cancellation and local sharpness.** The new construction uses a signed strict stress, not only zero coordinates. Its exact reflection average removes the dangerous cross terms before decoding. No unsupported source-modulus dichotomy is needed.
- **31–35: universal quartic balanced compilers.** The new frame avoids their full auxiliary-covariance identification. Free covariance permits an order-O(m^2+p) frame directly, so applying a quadratic-in-inner-order compiler is unnecessary.
- **49–56 and 60: two-MASA/commutator obstructions.** Every new lifted fibre lies in a proper exposed face. The compressed measurements are frames, not two maximal diagonal algebras on that face. The actual source observables differ from measured combinations by explicitly controlled Q-supported PSD slacks. The ambient positive-definite hypothesis needed to force full operator inclusion fails.
- **58–59: entanglement-breaking and generic strict-positivity decoders.** A compression is a structured coherent single-Kraus map, not finite measure-and-prepare and not a generic many-Kraus positivity-improving map.
- **61–64: spectraplex-image route.** The new inner PSD fibre has genuine nontrivial affine constraints and handles the nonspectrahedral-dual example above. It does not put all source geometry into an unconstrained PSD trace-section image.

No historical generic dimension-count theorem, symplectic-incidence formula, or unverified complexity assertion is used as a premise in 02–04. Those proofs are self-contained finite-dimensional algebra and inequalities.

## 5. Reading and correction audit

Read at the immutable historical commit: the complete handoff and original Track 02 brief; archive 00; every canonical numbered milestone 01–64; the additional 26–28 manuscripts on non-Lipschitz exponent halving, sharp Parseval transfer, all-depth dyadic halving, general synthesis, complete functional modulus law, and elementary full-rank Stiefel compilation; and the original dense-quadratic, rigidity-open, codimension-two and rational-obstruction manuscripts. Truncated long documents were expanded in additional line ranges.

The four specifically flagged corrections were inspected in their actual commit diffs:

  17: 104d084630fc9663e474c0a1f7ac244d7322577b
      Fixed-first-basis commuting completion is linear, not quadratic.
  47: fd1eee0b74a4e4e7ef0aadfdf5bf5d7e4182a6f6
      Require nonzero source coefficient/source injectivity.
  51: 69fede47aef7c7b5a8279a706832a25c7e25cb89
      Use a fixed linear Moore-Penrose splitter, not pointwise minimal splits.
  60: 8f5e3d9f5e3955ae3c15a7abd877e56211c1f05c
      Require a decoded positive-definite point to infer full row rank.

Historical Python scripts inspected include the fixed-basis linear test, commutator audit, balanced two/three-block and complement-twin audits, dual-spectraplex obstruction, dyadic and single exponent-halving audits, positive-decoder effects, Stiefel span, Mercedes tangent, positive-frame composition, sharp Parseval and two-zero Naimark audits. These were read, not all rerun. No claim is made that every historical repository revision or every old numerical output has been exhaustively reproduced.

### Additional issues found

**Milestone 15 normalization typo.** In the symmetric-square no-section argument, the sum of the two indicated expectations is 1, not 1/2; each expectation is 1/2. The contradiction with the asserted zero sum survives the correction.

**Milestone 17 stale wording.** A sentence still calls the correction system nonlinear despite the explicit linearity correction. Use the corrected linear criterion and Milestone 20's formula.

**Milestone 48 dimension typo.** The Case I sentence identifying H with its two-copy core C omits the one-dimensional complement: the dimensions are 2m+1 and 2m. The subsequent core-effect contradiction should be read with H=C direct-sum R. The new theorem does not depend on this argument.

**Historical commutator sampling bug.** AUDIT_TWO_MASA_COMMUTATOR.py constructs a random traceless subspace in all m-by-m arrays, without imposing symmetry. Its generic-sampling portion therefore does not test the stated real symmetric operator-system theorem. The reduced-skew tight-frame calculation is a separate check and is unaffected. The replacement diagnostic in audit_historical_corrections.py samples coefficients in an orthonormal symmetric basis, removes the identity, and asserts symmetry, zero trace and orthonormality.

**Real-domain reduction-map label.** AUDIT_FIXED_DIAGONAL_POSITIVE_DECODERS.py labels (tr(Y)I-Y)/(m-1) as positive but not CP. On the real symmetric domain used in this project it has the real Kraus representation

  (tr(Y)I-Y)/(m-1)
   =sum_(i<j) [J_ij/sqrt(m-1)] Y [J_ij/sqrt(m-1)]^T,
  J_ij=e_i e_j^T-e_j e_i^T.

For a symmetric Y, the diagonal entry at i of the unnormalized sum is sum_(j!=i)Y_jj, and its off-diagonal (i,j) entry is -Y_ij. This proves the formula in every dimension m>=2. The usual non-CP statement for the reduction map on the full complex matrix algebra is different: the Kraus formula extends as tr(Z)I-Z^T, agreeing on real symmetric matrices. The effect-singularity calculations in the historical script remain valid; its real-domain non-CP label does not. The replacement script checks the symbolic identity exactly for m=2,3,4 as a regression diagnostic.

These errata are recorded here rather than silently rewriting the immutable historical proofs. None is a premise of the new universal construction.

## 6. Reproducible checks and observed results

Run from this directory:

  OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python audit_quadratic_quotient.py
  OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python audit_adversarial.py
  OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python audit_historical_corrections.py

Dependencies: NumPy and SymPy. No external optimization solver or network access is used. These scripts use floating-point Cholesky for diagnostics; the exact proof uses rational LDL and recorded positive square roots.

The first script verifies the raw operator identity by exact rational SymPy arithmetic at m=2,p=3 and diagnoses dimensions m=1,2,3,4 with zero, rank-one and full-rank source points. It writes AUDIT_RESULTS.json.

The adversarial script checks the theorem's conservative closed-form constant, all signed dual certificates, objective identities, arbitrary ambient PSD ranks including full rank, duplicate/zero equations, inconsistent data, negative trace data, the singular m=p=1 boundary, a nonscalar trace certificate, and the historical 62 example. All assertions passed. Its committed output is ADVERSARIAL_RESULTS.json.

For the historical 62 instance, N=179, the largest tested source/lift residual ratio was about 0.2432, versus the proved conservative K_r about 45904.16. Relative signed-certificate eigenvalue errors were around -6.4e-16, forward-data error around 2.8e-16, and section error around 1.9e-15. A non-section feasible perturbation of Frobenius norm about 0.2352 retained the data to relative error about 2.8e-16. These numerical tolerances are not formal positivity certificates; the formulas in Sections 2–3 and in 02 provide the proofs.

The corrected historical diagnostic passed the exact symbolic skew-Kraus identities. With seed 20261112 and 100 skew samples each, the smallest sampled fourth commutator singular values were about 0.24823, 0.20496 and 0.23614 for m=4,5,6. Sampling does not certify a uniform minimum or any generic theorem, and none is needed for the new proof.

## 7. Completion statement

The near-quadratic unrestricted two-basis normal-form frontier in the handoff is resolved by the explicit positive quotient in 02–04, in the declared conditioning and exact-output model. The mathematical mechanism is one construction for all inputs: anchored entry copies, free auxiliary covariance, block-respecting Parseval completion, and strict signed reflection exposure.

The remaining activities of independent refereeing, literature-priority assessment, improving the constant 9, or imposing optional stronger geometric properties are not substituted for missing load-bearing steps: the exact full-fibre and quantitative all-PSD normal-form assertions above have complete proofs already committed.
