# Sharp finite-grid CP/COP certificates — 2026-11-14

## Main result

The parent manuscript `37_SHARP_CUBICAL_CERTIFICATES_AND_RATIONAL_CP_REGULARIZATION.md` proves the exact optimal trace-diagonal correction

    eta_q = (sqrt(1+1/q^2)-1)/2

for the nonnegative integer cube's outer layer. It gives matching primal and dual inclusions, rational diagonal regularization of every rational CP matrix, finite-LP certificates, and an objective-aware descent-or-separator test for the shadow pivot.

## Reproduce

Python 3, standard library only:

```sh
python test_exact_grid.py
```

It writes `EXACT_GRID_RESULTS.json`. The completed run contains five rational sharpness checks, nine exact phase-I LP alternatives, seven descent/certificate checks, and three strict-copositivity margin checks. The five-cycle test uses 2,101 grid vectors at q=4 and obtains pairing -1/2 and strict margin 191/8320. All decompositions and certificate inequalities use `fractions.Fraction`. The numerical eta values are illustrations only; no floating-point comparison certifies a result. The committed JSON is compactly formatted; rerunning may change whitespace but not its parsed contents.

`grid_cone_phase_one` returns a weighted rational CP decomposition, not a Gram factor formed with floating-point square roots. The proof uses four integer squares per weight to obtain a rational nonnegative Gram factor with at most 2*n*(n+1) columns. Four-square search is not implemented here. The general finite-neighbor subroutine is proved, not implemented by this new module; no full high-dimensional shadow path is claimed.

## Scope and cost

The grid size is (q+1)^n-q^n. Enumeration and rational simplex can be expensive. Runtime caps raise exceptions rather than report a false mathematical infeasibility. The factor branch concerns a diagonally PERTURBED matrix, not automatically the original input. The separator branch produces a genuine copositive separator of the original input.

This concerns completely positive matrices, not completely positive quantum channels. Optimality of eta_q is for this grid model. Established CP/COP polyhedral hierarchies, rational interior factorizations, and O(q^-2) convergence are cited, not claimed new.

The proposed positive universal boundary-factorization conjecture has external counterexample manuscripts dated September 2026. Those are not this continuation's discovery or independently revalidated computations. The new regularization theorem does not assert a rational factor for every unperturbed rational CP matrix.
