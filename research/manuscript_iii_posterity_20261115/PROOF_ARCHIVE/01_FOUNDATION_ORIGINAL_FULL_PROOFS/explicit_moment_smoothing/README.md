# Explicit Boolean-moment smoothing

The proof is in `../24_EXPLICIT_BOOLEAN_MOMENT_POLYNOMIAL_HARDNESS.md` (proof commit `05445b2e61a1942beda92f92f81e991cb57ea12d`).

For n>=2, put D=1+n+binom(n,2), let p be the least power of two at least 2^16 n^4, and define

    P_n(x)=||x||^2/(4D)+sum_{s in {-1,1}^n}< (1,s_i,s_i s_j),x >^(2p).

For all sufficiently large n, every convex body within Hausdorff distance 2^-20 n^-4 of {P_n<=1} requires single PSD order 2^(Omega(n^(1/8)))=2^(Omega(D^(1/16))). The defining polynomial is rational, SOS-convex and of polynomial degree. Its boundary is analytic and strictly curved with polynomial quantitative bounds. The proof supplies a finite rational SOC formulation and a polynomial-time individual-coefficient oracle.

Run the exact finite checks with Python 3 (no dependencies), from this directory:

    python test_explicit_moment_smoothing.py

Print the theorem parameters without evaluating the large polynomial:

    python explicit_moment_smoothing.py 16

The `value`, `derivatives`, and `soc_witness` functions enumerate all `2**n` Boolean vectors and are intended for small diagnostics. The theoretical exponent is large; do not infer polynomial-time evaluation from the coefficient oracle. Tests use smaller exponents only to check algebraic identities. `EXACT_IDENTITY_RESULTS.json` contains the recorded passing checks.

The all-dimensional lower bound imports Lee–Raghavendra–Steurer, arXiv:1411.6317v1, Theorems 3.8 and 5.3. No finite experiment proves that theorem or a lower bound for all matrix orders.

This continuation proves deterministic coefficient-explicit hardness at inverse-polynomial tolerance. It does **not** prove the stronger polynomial-total-description, fixed-tolerance, dimension-independently curved near-sphere target. No new LRS lower bound or named conjecture resolution is claimed.
