#!/usr/bin/env python3
"""Exact identities and finite numerical illustrations of manuscripts 30--31.

Requires SymPy. Numerical results do not prove the universal theorems.
No network, optimization solver, or external data is used.
"""
from __future__ import annotations
import json
import math
from pathlib import Path
from typing import Any
import sympy as sp


def exact_discounted_drs() -> dict[str, Any]:
    t = sp.symbols('t', positive=True)
    h = t * sp.sqrt(t + 1) / (t + 2)
    b = 2 / (t + 2)
    z = sp.Matrix([[h, b], [b, h]])
    anchor = sp.Matrix([[0, 1], [1, 0]])
    u = sp.Matrix([[0, 1], [1, h]])
    reflection = 2*u-z
    v = sp.Matrix([[h/t, 1+(b-1)/t],
                   [1+(b-1)/t, (1+1/t)*h]])
    neg = v-reflection
    checks = {
        'positive_part_determinant': sp.simplify(v.det()) == 0,
        'negative_part_determinant': sp.simplify(neg.det()) == 0,
        'orthogonal_parts': (v*neg).applyfunc(sp.simplify) == sp.zeros(2),
        'discounted_equation': (v-u-(z-anchor)/t).applyfunc(sp.simplify) == sp.zeros(2),
        'leading_diagonal': sp.limit(h/sp.sqrt(t), t, sp.oo) == 1,
        'leading_offdiagonal': sp.limit(b/sp.sqrt(t), t, sp.oo) == 0,
    }
    # Both diagonals of v and neg are explicitly positive at t>0; determinant
    # zero then proves that each is PSD, without a floating-point eigenvalue.
    for entry in (v[0,0], v[1,1], neg[0,0], neg[1,1]):
        assert sp.simplify(entry).is_positive is True
    assert all(checks.values())
    return checks


def drs_invariant_orbits(steps: int = 200_000) -> list[dict[str, Any]]:
    if steps < 1:
        raise ValueError('steps must be positive')
    checkpoints = {1000, 10000, 100000, steps}
    results: list[dict[str, Any]] = []
    for gamma in (0.0, 1.0, 2.0):
        h, b = 0.0, 1.0
        for k in range(steps):
            d = math.hypot(h, 2.0-b)
            th, tb = (h+d)/2.0, b/2.0
            denominator = k+1.0+gamma
            h = (k+1.0)*th/denominator
            b = (gamma+(k+1.0)*tb)/denominator
            if k+1 in checkpoints:
                predicted = (0.5+gamma)**(-0.5)
                results.append({
                    'family': 'two_by_two_DRS', 'anchor_weight': gamma,
                    'iteration': k+1,
                    'diagonal_over_sqrt_k': h/math.sqrt(k+1),
                    'predicted_diagonal_limit': predicted,
                    'ratio_to_prediction': h/(predicted*math.sqrt(k+1)),
                    'offdiagonal_over_sqrt_k': b/math.sqrt(k+1),
                })
        assert abs(h/math.sqrt(steps)/predicted-1) < 0.02
    return results


def scalar_power_orbits(steps: int = 40_000) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for p in (0.25, 0.5, 0.75, 1.0):
        c = p**p  # leading coefficient of the discounted curve
        for gamma in (0.0, 1.0, 2.0):
            x = 0.0
            for k in range(steps):
                tx = (x**(1/p)+1)**p
                x = (k+1)*tx/(k+1+gamma)
            predicted = c/(p+gamma)**p
            ratio = x/(predicted*steps**p)
            assert abs(ratio-1) < 0.02
            results.append({'family': 'scalar_power', 'p': p,
                            'gamma': gamma, 'steps': steps,
                            'scaled_state': x/steps**p,
                            'predicted_limit': predicted, 'ratio': ratio})
        for label, schedule in (
            ('constant_half', lambda k: 0.5),
            ('inverse_sqrt', lambda k: 1/math.sqrt(k+1)),
        ):
            x, clock = 0.0, 0.0
            for k in range(steps):
                theta = schedule(k)
                tx = (x**(1/p)+1)**p
                x = (1-theta)*x+theta*tx
                clock += theta
            ratio = x/(clock**p)  # p^-p c = 1
            assert abs(ratio-1) < 0.03
            results.append({'family': 'variable_relaxation', 'p': p,
                            'schedule': label, 'steps': steps, 'clock': clock,
                            'ratio_to_physical_time_prediction': ratio})
    return results


def gradient_prox_flow(steps: int = 25_000) -> list[dict[str, Any]]:
    # f(x)=(1+x)^(-b) on x>=0, with its positive-curvature quadratic
    # continuation on x<0. All iterates below stay on the positive half-line.
    results: list[dict[str, Any]] = []
    for b in (0.5, 1.0, 2.0, 4.0):
        p = 1/(b+2)
        step = 1/(2*b*(b+1))  # below the global smoothness threshold
        gd, prox = 0.0, 0.0
        for _ in range(steps):
            gd += step*b/(1+gd)**(b+1)
            # Proximal first-order equation y-old=step*b/(1+y)^(b+1).
            lo, hi = prox, prox+step*b/(1+prox)**(b+1)
            for _bisect in range(35):
                mid = (lo+hi)/2
                if mid-prox-step*b/(1+mid)**(b+1) > 0:
                    hi = mid
                else:
                    lo = mid
            prox = (lo+hi)/2
        physical_time = step*steps
        flow = (1+b*(b+2)*physical_time)**p-1
        leading = (b*(b+2)*physical_time)**p
        results.append({'family': 'gradient_prox_flow', 'b': b, 'p': p,
                        'steps': steps, 'step': step,
                        'gradient': gd, 'proximal': prox, 'flow_exact': flow,
                        'leading_prediction': leading,
                        'gradient_minus_proximal': gd-prox,
                        'gradient_over_flow': gd/flow,
                        'proximal_over_flow': prox/flow,
                        'note': 'Additive -1 creates a visible finite-horizon relative transient.'})
        assert abs(gd/flow-1) < 0.01
        assert abs(prox/flow-1) < 0.01
    return results


def no_last_displacement_inference(steps: int = 10_000) -> dict[str, Any]:
    # Exact formula for T(x,y)=(sqrt(max(x,0)^2+1),-y), start (0,1).
    x, y = math.sqrt(steps), (-1.0)**steps
    radius = math.hypot(x, y)
    residual = math.hypot(math.sqrt(steps+1)-math.sqrt(steps), 2*y)
    assert residual >= 2
    return {'steps': steps, 'normalized_state': [x/radius, y/radius],
            'residual': residual, 'residual_limit': 2,
            'scope': 'A cosmic leading term alone does not imply a vanishing last displacement.'}


def main() -> None:
    data = {
        'exact_discounted_DRS': exact_discounted_drs(),
        'DRS_orbits': drs_invariant_orbits(),
        'scalar_powers': scalar_power_orbits(),
        'common_gradient_prox_flow': gradient_prox_flow(),
        'scope_counterexample': no_last_displacement_inference(),
        'status': 'Exact finite identities and numerical illustrations; universal proofs are manuscripts 30--31.',
    }
    out = Path(__file__).with_name('TAME_COSMIC_RESULTS.json')
    out.write_text(json.dumps(data, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(data, indent=2))

if __name__ == '__main__':
    main()
