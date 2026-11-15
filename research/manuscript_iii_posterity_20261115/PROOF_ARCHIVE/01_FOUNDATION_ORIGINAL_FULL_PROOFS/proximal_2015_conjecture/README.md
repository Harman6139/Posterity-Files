# The 2015 exponential-quotient proximal conjecture

The proof is in `33_2015_EXPONENTIAL_QUOTIENT_CONJECTURE.md`.

It establishes the exact conjectural conclusion of Example 2.10 in Bauschke–Douglas–Moursi, arXiv:1505.04129v1 (May 15, 2015), for every starting point, including those outside the effective domain. It also establishes logarithmic coordinate asymptotics, the objective limit `lambda*k*F(z_k) -> 1`, and a multidimensional extension.

**Historical limitation:** the conjecture's date and original statement are verified. A search did not locate a later resolution, but its status as still open immediately before this proof is not certified. Do not present this packet as verified historical priority. The general cosmic-convergence conjecture was disproved in 2018 and is not the statement proved here.

## Numerical illustration

Run:

```sh
OPENBLAS_NUM_THREADS=1 python check_proximal_example.py
```

Requires Python 3 and SciPy. The script uses a scalar log-coordinate root solve, checks the optimality equations, the exact phase identity, and the proximal descent inequality. It writes `NUMERICAL_ILLUSTRATIONS.json` beside itself. Four cases include negative and zero initial second coordinates, with different positive fixed proximal parameters.

The analytical proof does not use these tests. The directional rate is only inverse-square-root-logarithmic, so the trajectory diagnostics intentionally show finite-time transients rather than asserting numerical equality with limiting constants.

No peer review, author contact, novelty guarantee, or journal decision is represented by these files.
