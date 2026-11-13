# Exact rational unrestricted two-basis normal form and sharp escape examples

Date: 2026-11-13. Proofs are in the parent directory, milestones 10–12; current overview: ../00_CURRENT_RESULTS.md.

## Run

Requires Python 3.10 or later and SymPy. No numerical optimization solver, floating-point eigenvalue routine, or network access is used by these programs.

    python rational_two_basis.py
    python exact_escape_examples.py

Recorded outputs are RATIONAL_RESULTS.json and ESCAPE_RESULTS.json. The mathematical results do not depend on finite-instance checks.

## Constructor usage

    import sympy as s
    from rational_two_basis import construct
    A = [s.diag(1, 0), s.Matrix([[0, s.Rational(1,2)], [s.Rational(1,2), 0]])]
    instance = construct(A)
    b = s.Matrix([0, 1])
    epsilon = s.Rational(1, 10)
    X = s.Matrix([[epsilon, 1], [1, 1/epsilon]])
    Y = instance.encode(X)
    assert instance.decode(Y) == X
    residual = instance.centered_measure(Y) - instance.centered_target(b)
    assert (residual.T * residual)[0] == epsilon**2

The source convention is A_i(X)=trace(A_i*X). Thus an offdiagonal entry measurement uses one-half in both symmetric positions of A_i. The example above is weakly infeasible, but each displayed X is PSD and its residual tends to zero.

The returned orthogonal matrix U is entirely rational and gives the second basis; the first is standard. Physical exact data satisfy

    (diag Y,diag(U.T*Y*U)) = W*b + t*v,

with exactly ONE shared free scalar t. For exact solutions t=trace(Y)/ctrace=trace(decode(Y)). The centered observation map subtracts v*trace(Y)/ctrace and divides by the rational scale f. Its target matrix W/f has orthonormal columns, making forward source residuals exactly isometric.

The source measurement list can be empty; use construct([],m=...) in that case. Redundant and zero rows are allowed. No trace-control or feasibility certificate is supplied. The constructor does NOT solve feasibility or compute a source solution.

## Proof commits

- Rational compiler, milestone 10: 31d40a5bf1100545564830bd70dc069ed4f118c8.
- One-scale unrestricted theorem, milestone 11: cd97bc32a1febc3f37ad3803c7cd582d140cf04d.
- Exact conic escape duality and sharp SDP envelope, milestone 12: 2e2f8f75c99f49e4b6e51fad2a37b41891928901.

The endpoint script checks the exact Schur-complement identities, unchanged equations, and leading trace orders of the two rational families. It does not estimate an exponent by fitting samples. The general upper/lower envelope and the reciprocal-exponent law are proved analytically in milestone 12.
