# Adversarial proof audit

This is an internal audit and a record of separately coded finite checks, not external expert review or formal verification.

## Structural checks

**Non-exposed matrix faces.** No step assumes that the minimal matrix-cone face is exposed. A proper exposer is selected only for the current real cone and current affine slice. Subsequent exposers need not be copositive on the original domain; the complete chain is part of the obstruction certificate.

**Algebraic coefficients.** A rational column has rational coordinates in a rational basis of its minimal vector face. Therefore independence of a number-field basis makes every coefficient-kernel equation necessary. This would be invalid for an arbitrary algebraic parametrization whose free parameters were allowed to be irrational.

**No lost rational factors.** The exposed quadratic values of the rational columns are nonnegative and sum to zero. Each column is retained by the exact rational-zero-domain lemma. The reverse inclusion is immediate from domain containment.

**Carrier uniqueness.** A terminal rational relative-interior completion can absorb a sufficiently small rational multiple of every rational terminal atom. Thus every surviving rational direction is actually viable, not merely a superset approximation. Conversely every viable direction survives all reductions. Density proves equality of terminal domains for every execution.

**Rational congruence.** For any invertible rational T, feasible factors correspond by u -> Tu and X -> TXT^T. Positive rational insertion coefficients are unchanged. Taking closures proves A(TP, THT^T)=T A(P,H). This covariance requires no orthant parametrization or bound in the number of extreme generators.

**Zero and lower-dimensional cases.** The vector domain contains zero. A zero-only feasible fiber has carrier {0}, distinct from EMPTY. Lineality is handled through rational equalities and signed generators. All interiors and spans are relative. Observation-margin assertions are stated for a nonzero Gram cone; the zero cone is decided directly.

**Totally real descent.** Conjugates need not remain in the column cone. The proof uses PSD restrictions on rational minimal-face spans, so the trace sum remains nonnegative. The affine constraint is preserved by embeddings because its coefficients are rational. The weighted version requires totally positive weights; the sqrt(2) example rules out positivity at only one embedding.

**Width versus time.** Four squares prove the 4d-column existence bound. The deterministic polynomial algorithm instead permits O(dh) columns via binary square splitting. A polynomial four-square routine is not silently assumed.

**Decision transcripts.** Reproducible exact sampling/elimination transcripts are charged. No claim that a full cylindrical cell decomposition has the same singly-exponential bounds is needed. The source was clarified accordingly.

**Measurement images.** Closedness follows only under the stated coercivity condition. The examples distinguish real-feasible arithmetic failure, strong infeasibility without an observation-supported positive cone margin, and weak infeasibility with no strict separator.

**Angular polarity.** The moment map is not self-adjoint. Its adjoint changes Q00 and the Qii exactly as stated. Endpoint angular gaps are interpreted by limits. Strict rational witnesses exist at every suboptimal coefficient; exact rational attainment of the optimal grid is a separate question.

**Local rule scope.** The path proof certifies the specified minimum-ratio walk, including uniqueness at crossings. It does not claim every descending ray rule is exponential. The new targets are interior members; nonlocal recognition can terminate immediately using the displayed short factors. This is the intended obstruction, not a hidden failure of the lower bound.

## Exact checks actually rerun

Five angular grids, eleven compressed facet certificates, one four-dimensional arithmetic obstruction, and three deliberate corruptions were checked using Fraction arithmetic. Generator and verifier are separate programs; the verifier imports no generator function. It checks full rank and codimension, moment reconstruction, permitted-column inequalities, number-field identities and strict signs. The universal theorem is not established by these examples.

## Residual uncertainty

The universal proofs have not received independent human review or formalization. The general real-algebraic decision algorithm is specified and bounded using primary algorithmic results, but is not implemented as a production package. Historical first priority and the publication benchmark remain uncertified. These limitations are not relabeled as mathematical proof gaps or hidden behind test results.
