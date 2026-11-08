# Milestone 33 — dense nullity-four: three exponents force singularity degree two or less

2026-11-08. **PROVED for arbitrary dense real PSD measurement kernels** (not sparse), assuming the previously established dense sharp weighted-flag extraction. No novelty is claimed for the classical Gordan–Stiemke alternative.

## Theorem

Let X*>=0 uniquely solve L(X)=L(X*) among PSD matrices, with positive target rank r and nullity nu=n-r=4. If its sharp full-matrix Hölder exponent is any of
\[
\boxed{\alpha\in\{5/16,\ 5/12,\ 7/16\},}
\]
then its **minimal facial-reduction degree is exactly two**. In particular none of these values occurs at d>=3, regardless of how dense the measurement matrices are. The degree-two sparse realizations exist by the previously proved exact degree-two construction, so the degree conclusion is sharp.

## I. Exhaustive three valuation patterns

The reduced denominator of 2alpha is, respectively, 8, 6, 8, forcing three internal one-dimensional null valuation levels plus the terminal (nullity four). The prior complete rational mediated-set enumeration shows only:

D: alpha=5/16, (w1,w2,w3)=(1/2,5/8,3/4), with doubled leading weight w2.
E: alpha=5/12, (w1,w2,w3)=(1/2,2/3,5/6), with doubled leading weight w3.
F: alpha=7/16, (w1,w2,w3)=(1/2,3/4,7/8), with doubled leading weight w3.

The dense extraction provides G,H1,H2,H3 in K=ker L, where G has a nonzero support-to-e_t block (t=2 for D, t=3 for E,F), and Hi has positive e_i diagonal. Their arbitrary dense supports satisfy, with w0=0,w4=1:
   (H_i)_(a,b)=0 whenever w_a+w_b>2w_i,
   G_(a,b)=0 whenever w_a+w_b>2alpha.
No sparsity assumption. A positive terminal E44 coefficient at residual order one completes the sharp flag.

Every first exposing PSD stress lies in the terminal valuation subspace span(e4), by the universal first-stress alignment theorem. Hence the first stress is rank one, is E44 after scaling, and removes e4. Let W3=U0+span(e1,e2,e3), K3=K intersect S(W3), and E=span(e1,e2,e3).

## II. A PSD-null-compression alternative

We claim
\[
\boxed{\{P_E H P_E:H\in K_3\}\cap S^3_+=\{0\}.}
\tag{2.1}
\]
Suppose not. Choose H∈K3 with R=P_E H P_E>=0 nonzero, and let j be the largest index among 1,2,3 with H_jj>0. Then H_kk=0 for every k>j; since R is PSD, its entire k-th row and column in E vanish for k>j. Thus:
- H has arbitrary support-to-null blocks (U0 to any e_i, i<=3);
- its null-to-null blocks can be nonzero only among indices 1,...,j;
- its e_j diagonal is strictly positive.

Choose the **new earlier** positive diagonal weight v_j<w_j, adjust the other weights v1<v2<v3<1 according to the table in Section III, and insert H at exponent v_j. The only possible blocks of H have pair-weight at most
   max(v_j,v_3/2) <= v_j.
(The last inequality holds strictly when j=1,2 and tau=1/1000.) Therefore H is a valid positive leading diagonal coefficient at e_j, even though H may be arbitrarily dense on its permitted subspace. Retain/move the original kernel coefficients G,H1,H2,H3 as specified in the table. Every originally permitted dense block remains permitted by the new coefficient exponent. The old mode Hj, when replaced by H as the earliest diagonal coefficient at e_j, is retained at its **old** exponent w_j (so it cannot interfere negatively with the new leading diagonal).

The standard positive coefficient-rescaling lemma therefore constructs a positive definite full-matrix curve
   X(t)=X*+sum_{e<1}c_e t^e H_e+c_4 t E44
with residual Theta(t), displacement Theta(t^{p'}), and
   p'=v_t/2 < alpha.
This contradicts the optimality of alpha and proves (2.1).

## III. Full nine-case rational coefficient audit

Use tau=1/1000, write (a,b,c)=(w1,w2,w3), primes for new values, and list orders of (G,H1,H2,H3). The new H is inserted at v_j and has the PSD-null support restrictions above.

D, alpha=5/16:
 j=3: c'=c-tau; a'=a, b'=(a+c')/2; orders (b'/2,a,b',c).
 j=2: b'=b-tau; a'=a, c'=c; orders (b'/2,a,b,c).
 j=1: a'=a-tau; c'=(a'+1)/2, b'=(a'+c')/2; orders (b'/2,a,b',c').

E, alpha=5/12:
 j=3: c'=c-tau; a'=a, b'=(a+c')/2; orders (c'/2,a,b',c).
 j=2: b'=b-tau; a'=a, c'=(b'+1)/2; orders (c'/2,a,b,c').
 j=1: a'=a-tau; b'=(2a'+1)/3, c'=(b'+1)/2; orders (c'/2,a,b',c').

F, alpha=7/16:
 j=3: c'=c-tau; a'=a,b'=b; orders (c'/2,a,b,c).
 j=2: b'=b-tau; a'=a,c'=(b'+1)/2; orders (c'/2,a,b,c').
 j=1: a'=a-tau; b'=(a'+1)/2,c'=(b'+1)/2; orders (c'/2,a,b',c').

In every case, (i) the new weights are positive and strictly increasing; (ii) v_t/2 is strictly below alpha; (iii) EVERY formerly allowable block of each original coefficient satisfies v_a+v_b<=2(new order); (iv) every possible block of H satisfies the analogous inequality at its inserted order; (v) no earlier old coefficient has a negative unbalanced diagonal entry at a new valuation level. All checks are exact finite rational inequalities; the complete self-contained companion Python verifier (checkpoint 34) checks all 15 unordered block pairs for every old mode and all possible new H entries, and passed all nine cases. Thus the constructive contradiction is valid for **any dense kernel matrices** compatible with the sharp extracted flag, not merely for particular sparse parent edges.

## IV. Conclude by strict PSD separation

Let Q={P_E H P_E:H∈K3}, a linear subspace of S(E). By (2.1), Q∩S(E)_+={0}. The Gordan–Stiemke separation theorem for the PSD cone says that Q-perp contains a positive definite Z_E. Indeed, strictly separate the compact trace-one PSD matrices from Q; the separating normal is positive definite and perpendicular to Q.

The block matrix diag(0 on U0,Z_E) belongs to the orthogonal complement of K3 *inside S(W3)*. By the elementary compression-annihilator identity
   (K∩S(W3))^\perp_{S(W3)} = P_W3 K^\perp P_W3,
it lifts to an ambient measurement stress whose W3 compression is PSD and positive definite on all three remaining null directions. One facial-reduction step after E44 therefore reaches the target face. Thus d<=2. Because the dimension-dependent dense degree-one classification includes only exponents {1,1/2}, none of the three exponents here can have d=1. Consequently d=2. QED.

## Audit and scope

- **Universal dense**: actual K3 is arbitrary, not required to be generated by edge pencils.
- **All null ranks and arbitrary positive target rank**: the source block U0 may have any positive dimension; all its blocks carry valuation weight zero.
- **Exact positivity**: the coefficient-rescaling lemma verifies all PSD minors simultaneously.
- **Finite rigorous calculation**: the companion Fraction code is an arithmetic check of all support inclusions, not numerical optimization.
- **Still open**: the exponent 1/2 at degree >=3, the exact possibility of 1/7 at nullity four and degree three, and the fully explicit arithmetic spectrum for arbitrary nullity/degree.