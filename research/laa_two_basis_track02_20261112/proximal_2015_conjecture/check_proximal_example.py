"""Numerical illustrations only; the conjecture is proved algebraically.

Dependencies: Python 3 and SciPy. Run with `python check_proximal_example.py`.
The positive scalar displacement is solved in logarithmic coordinates.
"""
from __future__ import annotations
import json
import math
from pathlib import Path
from scipy.optimize import brentq


def prox_step(x: float, y: float, lam: float = 1.0) -> tuple[float, float, float]:
    if not all(map(math.isfinite, (x, y, lam))) or lam <= 0:
        raise ValueError('Finite x,y and positive finite lam are required.')
    target = x + math.log(lam)

    def positive_y(s: float) -> float:
        d = math.hypot(y, 2.0 * math.sqrt(s))
        return (y + d) / 2.0 if y >= 0 else 2.0 * s / (d - y)

    def equation(log_s: float) -> float:
        s = math.exp(log_s)
        return log_s + s + math.log(positive_y(s)) - target

    lo, hi = -1.0, 1.0
    while equation(lo) > 0:
        lo *= 2.0
        if lo < -700:
            raise ArithmeticError('Underflow in diagnostic scalar solve.')
    while equation(hi) < 0:
        hi *= 2.0
        if hi > 700:
            raise ArithmeticError('Overflow in diagnostic scalar solve.')
    log_s = brentq(equation, lo, hi, xtol=1e-13, rtol=1e-14)
    s = math.exp(log_s)
    return x - s, positive_y(s), s


def run_case(initial: tuple[float,float], lam: float, n: int=20000) -> dict:
    x,y = initial
    max_opt = max_identity = max_descent = 0.0
    snapshots = []
    for k in range(1,n+1):
        xn,yn,s = prox_step(x,y,lam)
        dy = yn-y
        fnew = math.exp(xn)/yn
        max_opt = max(max_opt, abs(s-lam*fnew), abs(dy-lam*fnew/yn))
        identity = (xn+yn*yn/2)-(x+y*y/2)+dy*dy/2
        max_identity = max(max_identity,abs(identity))
        if y>0:
            fold=math.exp(x)/y
            max_descent=max(max_descent, fnew+(s*s+dy*dy)/(2*lam)-fold)
        x,y=xn,yn
        if k in (100,1000,10000,n):
            norm=math.hypot(x,y)
            prediction=-math.log(k)+0.5*math.log(math.log(k))+0.5*math.log(2)-math.log(lam)
            snapshots.append(dict(k=k,x=x,y=y,phase=x+y*y/2,
                                  lambda_k_F=lam*k*fnew,
                                  x_minus_asymptotic= x-prediction,
                                  scaled_angle=math.sqrt(math.log(k))*math.hypot(x/norm+1,y/norm)))
    assert max_opt < 1e-9, max_opt
    assert max_identity < 1e-9, max_identity
    assert max_descent < 1e-9, max_descent
    return dict(initial=initial,lam=lam,iterations=n,
                max_optimality_error=max_opt,max_invariant_error=max_identity,
                max_descent_violation=max_descent,snapshots=snapshots)

if __name__=='__main__':
    data=dict(scope='Floating-point illustrations, not proof of the universal theorem.',
              expected_limits=dict(lambda_k_F=1, x_minus_asymptotic=0, scaled_angle=math.sqrt(2)),
              cases=[run_case((0.,1.),1.), run_case((3.,-2.),1.),
                     run_case((-2.,4.),0.2),run_case((1.,0.),5.)])
    path=Path(__file__).with_name('NUMERICAL_ILLUSTRATIONS.json')
    path.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))
