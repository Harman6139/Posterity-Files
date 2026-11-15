# Proved and not proved — quadratic universality continuation

Date: 15 November 2026. The results below have complete internal proofs in the
supplied manuscript. Historical first priority and external validation are
separate questions and are not certified here.

## Proved

**Exact classification for every rational quadratic form.** Let Q and A be
rational symmetric, A nonzero PSD, V=range(A), and sigma=tr(QA)>=0.
Rational vectors satisfying u^TQu>=0 can sum as unweighted Gram columns to A
exactly when sigma>0, or Q restricted to V is zero, or sigma=0 and the
nondegenerate quotient of that restriction is rationally isotropic.
The quotient condition is essential: rational radical vectors alone do not
suffice. In the strict case the minimum rational permitted width is exactly
the unrestricted rational Gram width, bounded by rank(A)+3. On the
nontrivial feasible boundary, at most r(r+1)/2-1 weighted rational atoms and
four times that many unweighted columns suffice.

**Canonical carrier for every rational affine completion fiber.** Compute
the maximal support of its rational PSD points, test whether positive trace
is possible, and make at most one isotropy decision. The result is a rational
subspace or one quadratic cone/zero cone in such a subspace. It is exactly
the closure of viable rational Gram directions, preserves every rational
completion, has a relatively strictly feasible terminal slice, and describes
the closure of all rational completions. The construction uses at most
2n+3 rational convex-semialgebraic point queries. It includes real-feasible
fibers with no rational completion and does not confuse nonclosed images
with closed cones.

**Sharp Lorentz threshold and rational moment theorem.** Every rational
real-feasible Lorentz Gram matrix of rank at least five factors rationally.
There are explicit rank-two, rank-three, and rank-four counterexamples below
that threshold; the rank-four example is an integer matrix of order five.
Its normalized version gives rational spherical first/second moments with
no finitely supported rational-point law. Rank at least five and strict
ball moment slack imply rational realizability under the stated hypotheses.
These claims are about Lorentz columns, not ordinary orthant complete
positivity.

**Open-domain width and conditioning.** For any relatively open,
positive-scaling-invariant permitted domain in range(A), minimum rational
width is the maximum of minimum real permitted width and unrestricted
rational width. A signed Cayley argument gives explicit rational height in
terms of the base factor and logarithmic clearance. A column-clearance
hypothesis gives a quantitative Gram-cone ball and dual margin. The
unrestricted rank+3 width bound and its sharpness are classical quadratic
form consequences, not claimed as new.

**Exact obstruction to indiscriminate curvature generalization.** Two
quadratic observations over a product of 2-by-2 PSD column cones, or over
one larger PSD column cone, encode any rational polynomial circuit
feasibility problem, with both directions preserving rational solutions.
Arbitrary Gram width cannot escape it. An explicit repeated-squaring
family forces exponential coordinate bit height in variable dimension.
The theorem does NOT assert any present decidability/undecidability status
for rational polynomial feasibility.

**Failure of unconstrained totally-real descent for curved columns.**
The rank-two Lorentz example has a permitted factor over Q(sqrt(2)) but no
rational factor of any width. Thus the earlier polyhedral descent theorem
cannot be extended unchanged to all rational convex cones.

## Complexity proved and resources charged

Rational support computation is polynomial in total input bits for each
fixed dimension, using the established rational convex-point algorithm.
Isotropy is not declared a free or polynomial-time oracle: clearing
denominators to an integral k-by-k form of maximum coefficient M gives the
explicit Cassels search bound (3 k^2 M)^((k-1)/2). Finite enumeration yields a
conservative 2^{O_n(L)} bit algorithm. Successful seeds have O_n(L) height.
Once a seed is supplied, exact weighted factors have polynomial fixed-n
construction time and O_n(L+h) coordinate height. Four-square compression
is an existence width bound; deterministic binary-square conversion may
use O_n(L+h) columns. No variable-dimensional polynomial theorem is claimed.

## Fresh exact verification

Three low-rank obstruction matrices; 4,889 modular evaluations; four exact
rational-factor cases with 28 weighted atoms and 95 unweighted columns;
two carrier examples and four viable-column subtractions; three Cayley
cases with 44 signed charts; three circuit cases with 22 PSD blocks and
1,602 observation-matrix entries. Seven deliberately corrupted data sets
were rejected. See the saved JSON report and its exact hash.

## Not proved or not claimed

- An unrestricted rational-factor theorem for arbitrary spectrahedral,
  semialgebraic, or product-cone column domains.
- A new algorithmic resolution of rational polynomial feasibility.
- A new local-pivot lower bound for Lorentz cones. The prior robust all-local
  polyhedral theorem is inherited, not silently transferred.
- Optimal general boundary factor width beyond the stated bound and the
  sharp split-binary example.
- A production implementation of the general convex rational-point or
  isotropy subroutines; the programs are exact example verifiers.
- Independent human review, formal proof-assistant checking, exhaustive
  historical novelty certification, or the registered upper-20% LAA
  full-paper comparison. No journal acceptance probability is given.
