# Checkpoint 02 — algebraic germ fingerprints and a sharp regular-pencil collapse

Date: 2026-11-15. This is a structural partial theorem in the original exact-rational information model. It does not classify all rank-changing pencils and therefore does not resolve the full optimization frontier.

## 1. A computable algebraic probe, independent of coefficient heights

Fix matrix order m>=1 and coordinate dimension d>=1. A rational pencil means X_a(x)=X_0+sum_i x_i H_i with rational symmetric coefficients; normalization and weak infeasibility are not needed for this section. Put f_a(x)=dist_F(X_a(x),S_+^m)^2/2.

THEOREM A. There is a computable integer D=D(m,d)>=m and, in every prescribed nonempty rational open ball, an explicitly constructible real algebraic vector q with the following simultaneous properties for ALL pairs of rational pencils of this order and dimension, without a coefficient-height bound:

(a) f_a(q)=f_b(q) if and only if f_a and f_b have the same real-analytic germ at q.
(b) grad f_a(q)=grad f_b(q) if and only if their gradients have the same germ at q; equivalently f_a-f_b is constant on a neighborhood of q.
(c) Every rational pencil has locally constant maximal rank at q. Its natural objective is real analytic near q, even if the pencil has a persistent kernel or repeated nonzero eigenvalues.

One can take q=c+eta(alpha,alpha^(D+1),...,alpha^((D+1)^(d-1))), where c is the rational center of the chosen ball, eta>0 is a sufficiently small rational number, K=(D+1)^d, and alpha is the positive root of z^K-2. Thus its algebraic field degree is K. With c=0 and eta=1/(4d), q lies in the unit ball. No polynomial bound on K or the intervening computation is claimed.

### Proof of a uniform semialgebraic degree bound

Treat every independent entry of the two coefficient lists a,b as a FREE REAL PARAMETER. For a symmetric matrix X, introduce symmetric Y,Z and impose

   Y>=0, Z>=0, YZ=0, X=Y-Z.

These polynomial conditions have a unique solution: Y=X_+ and Z=(-X)_+. Indeed YZ=0 implies ZY=0, so Y,Z commute and can be simultaneously orthogonally diagonalized; their nonnegative eigenvalues have disjoint supports, and the assertion follows entry by entry. Positivity is expressed by all principal minors. The natural value is tr(Z^2)/2 and its i-th coordinate derivative is -tr(H_i Z).

Consequently each of the two relations

   E_0(a,b,x): f_a(x)=f_b(x),
   E_1(a,b,x): grad f_a(x)=grad f_b(x)

has a first-order formula over the reals of a fixed finite polynomial format determined only by m,d. Apply a fixed effective quantifier-elimination algorithm to these TWO UNIVERSAL formulas, eliminating the Y,Z variables but retaining a,b,x. Let D be the larger of m,1 and the x-degrees of all polynomials in the resulting quantifier-free formulas. This DEFINES a computable integer depending only on m,d, not on coefficient sizes, input instances, or query horizon.

After substituting rational a,b, every resulting polynomial is either identically zero or is a nonzero rational polynomial in x of total degree at most D. The identically zero polynomials cause no difficulty: their sign is constantly zero.

This use of quantifier elimination is classical. An explicit closed elementary degree estimate is unnecessary for the theorem: the fixed algorithm on a fixed symbolic formula produces the specified finite D effectively. We make no claim that the degree or runtime is practical. The construction must not be described as a polynomial-bit identification algorithm.

### Proof that the algebraic probe avoids every relevant nonzero polynomial

For P in Q[x_1,...,x_d] of total degree at most D, substitution x_i=z^((D+1)^(i-1)) sends different monomials to different powers of z. Each monomial has coordinate exponents at most D, so these powers are their distinct base-(D+1) digit encodings. Every exponent is at most K-1. Thus a nonzero P becomes a nonzero polynomial of degree below K.

The polynomial z^K-2 is irreducible over Q by Eisenstein at 2. Hence no nonzero polynomial of degree below K can vanish at alpha. An invertible rational affine rescaling x=c+eta v preserves nonzeroness and total degree. Therefore NO nonzero rational polynomial of degree at most D vanishes at q.

In each of the specialized quantifier-free formulas for E_0 and E_1, every nonconstant sign at q is nonzero and remains unchanged on some neighborhood. Taking the finite intersection of these neighborhoods shows that the truth value of E_0 or E_1 is locally constant. If equality holds at q, it therefore holds on a neighborhood. The reverse implication is immediate.

### Analyticity at maximal-rank points

For a fixed pencil let r be its maximal rank on R^d. At least one r-by-r minor is a nonzero polynomial of degree at most m; it does not vanish at q. Thus rank X(q)=r. The same minor remains nonzero nearby, while rank cannot exceed r, so the rank is constant in a neighborhood. This includes r=0, when the pencil is identically zero.

At a point of locally constant rank, the nonzero negative eigenvalues can be separated from zero and the positive eigenvalues by a fixed finite complex contour. The spectral projector

   P_-(x)=(1/(2 pi i)) integral_Gamma (zI-X(x))^(-1) dz

is analytic there: the integrand has a locally convergent power series in x uniformly on the contour. Persistent zero eigenvalues lie outside the contour. The objective is

   f(x)=tr(X(x)^2 P_-(x))/2,

so is real analytic on that neighborhood. Crossings and multiplicities among NONZERO negative eigenvalues do not matter. This proves (c) and completes Theorem A.

## 2. A sharp one-query theorem for globally constant-rank pencils

Let R_(m,d)^Q be the class of rational pencils whose rank is constant on ALL of R^d. Its members have constant inertia, although persistent kernels are allowed. Restrict to the normalized isometric, genuinely weakly infeasible members when discussing optimization.

THEOREM B. One exact natural VALUE query identifies the objective of any member of R_(m,d)^Q up to global functional equality. One exact GRADIENT query does the same when all candidates are promised to have the common infimum zero. The queries can lie in the unit ball, and the same query works for every coefficient height. Unlimited computation then returns an epsilon-approximate point for every epsilon>0 without further calls.

Proof. Every objective in this class is real analytic on connected R^d by the preceding local argument. Equality of values at q yields equality on a neighborhood by Theorem A. The real-analytic identity theorem gives equality everywhere. Equality of gradients gives a locally constant difference, hence a globally constant difference by the same identity principle. A common finite infimum zero forces that constant to be zero.

This is objective identification, NOT unique coefficient recovery. Orthogonal congruences, invisible positive blocks, and other observational equivalences can give different matrix descriptions of the same function.

### Effective decoding under the declared exact arithmetic model

Enumerate all rational coefficient lists of the declared m,d. Constant rank, isometry, weak infeasibility and the common infimum promise can be tested by first-order real algebraic sentences; it is enough to test constant rank and the common infimum for the gradient-only version. Evaluate the candidate value or gradient at the algebraic q using exact real-algebraic arithmetic and compare with the oracle reply. The true input occurs at a finite index, so the first match is eventually found. The theorem guarantees that every matching candidate has the true global objective.

For epsilon>0, enumerate rational points and evaluate the identified objective until finding value below epsilon. Infimum zero and continuity ensure an open nonempty sublevel {f<epsilon}; it contains a rational point. This second enumeration terminates. Neither enumeration has a polynomial-time guarantee, and the query has potentially enormous algebraic degree. These costs are permitted by the original oracle model but would matter in a bit-complexity model.

### Sharpness

The two order-two pencils

   [[0,1],[1,z]] and [[0,1],[1,-z]]

are rational, isometric, nonsingular of inertia (1,1) everywhere, and weakly infeasible. They share the beta=1/2 escape profile and f(0)=1/2. For every epsilon<1/2, their epsilon-success sets lie respectively in z>0 and z<0. Under an independent fair sign prior, a zero-query randomized output succeeds with probability at most 1/2. Therefore one query is necessary and sufficient for a uniform success probability 2/3 on the constant-rank class containing this pair.

## 3. What the invariant actually says

The algebraic obstruction is not the size of a finite real query. A bounded query can separate all rational polynomial identities up to a fixed format-dependent degree. At that point an exact response distinguishes different local analytic germs; it cannot distinguish members sharing that germ.

Global constant rank supplies a sufficient SPECTRAL CONTINUATION condition: every germ continues as a single real-analytic function over connected R^d. Rank-changing pencils can fail this condition, and checkpoint 01 gives an arbitrarily large exact identification lower bound. The condition is sufficient, NOT necessary: some rank-changing pencils still have globally analytic squared-distance objectives (quadratic stars are an example).

This is therefore a rigorous subclass theorem, not a complete classification of spectral observability. In particular the assertion 'rank changes occur, therefore optimization is hard' is false, as checkpoint 01 demonstrates.

## 4. Finite families: value queries simulate first-order replies one for one

There is also a useful general information-model fact, separate from rationality.

LEMMA. Let f_1,...,f_N be a known finite family of C1 functions on R^d. With unrestricted exact queries and computation, one VALUE-only query can simulate a value-and-gradient query at any prescribed x. The query location may change. For rational semialgebraic families the relocation can be found effectively using exact real arithmetic and rational-point enumeration.

Proof. Consider only pairs (i,j) whose value/gradient jets at x differ. If f_i(x)!=f_j(x), their values differ throughout a neighborhood of x. Otherwise grad(f_i-f_j)(x)!=0, so by continuity of the gradient and the implicit function theorem the local zero set is a hypersurface with empty interior. For the finitely many relevant pairs, a sufficiently small common ball therefore contains an open nonempty set on which EVERY relevant pair has distinct values. Choose a rational q in that set. Enumerating rational q and testing the finitely many required inequalities finds one whenever the models are exactly evaluable. A returned value f_i(q) identifies a subset of candidates, and every candidate in that subset has the SAME value-and-gradient jet at x. Return that common jet.

For measurable algorithm models, enumerating rational points and taking the first one passing the finite tests gives a measurable relocation rule as a function of x. Recursively applying the simulation preserves adaptive randomized transcripts, outputs and query counts. Conversely a value/gradient oracle plainly supplies a value. Thus their minimax QUERY COUNTS on a fixed known finite family are identical. No efficiency claim follows.

The lemma is an elementary exact-information observation, not a new lower bound or a claim that numerical finite differences compute exact gradients. It emphasizes why known finite rational priors and exact readout must be treated carefully. It does not collapse an infinite real-coefficient class, and does not identify an entire piecewise function from one local observation.

## 5. Attribution and frontier status

Effective real quantifier elimination, Kronecker monomial substitution, Eisenstein irreducibility, analytic spectral projectors, and the analytic identity theorem are established ingredients. The claimed synthesis is the height-independent conic germ probe, the explicit regular-pencil recovery theorem, and the exact separation from rank-changing global identification. A substantive priority assessment is still required before claiming historical novelty.

Primary source checked: S. Basu, Algorithms in Real Algebraic Geometry: A Survey, Section 2.1, Theorem 2.1 and its algorithmic discussion, https://www.math.purdue.edu/~sbasu/raag_survey2011.pdf. Also see Basu--Pollack--Roy, Algorithms in Real Algebraic Geometry, quantifier-elimination chapters; the 1996 JACM paper on combinatorial and algebraic complexity of quantifier elimination.

The original arbitrary-rank-changing rational exact-oracle OPTIMIZATION lower bound is neither proved nor disproved by this checkpoint. No upper-quintile or submission-readiness claim is made.