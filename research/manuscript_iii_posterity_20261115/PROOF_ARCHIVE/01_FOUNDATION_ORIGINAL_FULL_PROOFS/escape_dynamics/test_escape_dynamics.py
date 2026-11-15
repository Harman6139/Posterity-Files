#!/usr/bin/env python3
"""Reproducible diagnostics for escape-controlled projection rates.

These floating-point diagnostics do not prove the asymptotic theorems.
They verify the comparator energy inequalities and compare observed tail
slopes with the analytic exponents on explicit weakly infeasible SDPs.
Dependencies: numpy.  No solver or network is used.
"""
from __future__ import annotations
import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
import numpy as np


def psd_projection(x: np.ndarray) -> np.ndarray:
    x = (x + x.T) / 2
    values, vectors = np.linalg.eigh(x)
    return (vectors * np.maximum(values, 0.0)) @ vectors.T


def entry(m: int, i: int, j: int) -> np.ndarray:
    x = np.zeros((m, m))
    if i == j:
        x[i, i] = 1.0
    else:
        x[i, j] = x[j, i] = 0.5
    return x


@dataclass
class SDP:
    matrices: np.ndarray
    b: np.ndarray
    escape: float
    family: str

    def __post_init__(self) -> None:
        self.m = self.matrices.shape[1]
        self.rows = self.matrices.reshape(len(self.b), -1)
        gram = self.rows @ self.rows.T
        self.correction = self.rows.T @ np.linalg.pinv(gram)
        self.x0 = self.affine(np.zeros((self.m, self.m)))

    def affine(self, x: np.ndarray) -> np.ndarray:
        flat = x.ravel()
        return (flat + self.correction @ (self.b - self.rows @ flat)).reshape(x.shape)

    def loss(self, x: np.ndarray) -> float:
        z = x - psd_projection(x)
        return 0.5 * float(np.sum(z * z))

    def comparator(self, t: float = 0.6) -> np.ndarray:
        m = self.m
        if self.family == 'fast':
            u = np.array([math.sqrt(t)] +
                         [t ** (-(2 ** (i-1) - 0.5)) for i in range(1, m)])
            z = np.outer(u, u)
        else:
            z = np.zeros((m, m))
            d = [t ** (2 ** j - 1) for j in range(1, m)]
            z[0, 0] = (m - 1) / (4*t)
            for j in range(1, m):
                z[j, j] = d[j-1]
                z[0, j] = z[j, 0] = -0.5 if j == 1 else -d[j-2]/2
        return self.affine(z)


def make_problem(m: int, family: str) -> SDP:
    if m < 2:
        raise ValueError('Weakly infeasible endpoint examples require m >= 2.')
    if family == 'fast':
        aa = [entry(m, 0, 0), entry(m, 0, 1)]
        b = [0.0, 1.0]
        for i in range(1, m-1):
            aa.append(entry(m, i, i) - entry(m, 0, i+1))
            b.append(0.0)
        exponent = float(2 ** (m-1) - 1)
    elif family == 'slow':
        aa = [entry(m, m-1, m-1), entry(m, 0, 1)]
        b = [0.0, -0.5]
        for j in range(2, m):
            aa.append(2*entry(m, 0, j) + entry(m, j-1, j-1))
            b.append(0.0)
        for i in range(1, m):
            for j in range(i+1, m):
                aa.append(entry(m, i, j)); b.append(0.0)
        exponent = 1.0 / (2 ** (m-1) - 1)
    else:
        raise ValueError('family must be fast or slow')
    return SDP(np.array(aa), np.array(b), exponent, family)


def simulate(problem: SDP, accelerated: bool, iterations: int) -> dict:
    x = problem.x0.copy()
    z = x.copy()
    weight = 0.0
    u = problem.comparator()
    fu = problem.loss(u)
    r0sq = float(np.sum((problem.x0-u)**2))
    checkpoints = set(np.unique(np.geomspace(10, iterations, 90).astype(int)).tolist())
    records = []
    max_relative_energy_violation = 0.0
    max_affine_error = 0.0
    for k in range(1, iterations+1):
        if accelerated:
            a = (1.0 + math.sqrt(1.0 + 4.0*weight))/2.0
            nxt = weight+a
            y = (weight*x + a*z)/nxt
            g = y-psd_projection(y)
            z = problem.affine(z-a*g)
            x = (weight*x+a*z)/nxt
            weight = nxt
            witness = z
            clock = weight
        else:
            x = problem.affine(psd_projection(x))
            witness = x
            clock = float(k)
        if k in checkpoints:
            px = psd_projection(x)
            fx = 0.5*float(np.sum((x-px)**2))
            lhs = clock*(fx-fu)+0.5*float(np.sum((witness-u)**2))
            rhs = r0sq/2
            violation = (lhs-rhs)/max(1.0,abs(lhs),rhs,clock*fu)
            max_relative_energy_violation = max(max_relative_energy_violation, violation)
            ae = float(np.linalg.norm(problem.rows@x.ravel()-problem.b))
            max_affine_error=max(max_affine_error,ae)
            records.append({'k':k,'residual':math.sqrt(2*fx),
                            'iterate_norm':float(np.linalg.norm(x)),
                            'psd_trace':float(np.trace(px)),
                            'source_residual':float(np.linalg.norm(problem.rows@px.ravel()-problem.b))})
    tail = records[-20:]
    logk = np.log([v['k'] for v in tail])
    residual_slope = float(np.polyfit(logk,np.log([v['residual'] for v in tail]),1)[0])
    norm_slope = float(np.polyfit(logk,np.log([v['iterate_norm'] for v in tail]),1)[0])
    a = problem.escape
    factor = 2 if accelerated else 1
    expected_res = -factor/(2*(a+1))
    expected_norm = factor*a/(2*(a+1))
    if max_relative_energy_violation>1e-8:
        raise AssertionError(f'Energy inequality violation: {max_relative_energy_violation}')
    return {'family':problem.family,'matrix_order':problem.m,
            'method':'accelerated_projected_gradient' if accelerated else 'alternating_projections',
            'escape_exponent':a,'iterations':iterations,
            'predicted_residual_slope':expected_res,'observed_tail_residual_slope':residual_slope,
            'predicted_norm_slope':expected_norm,'observed_tail_norm_slope':norm_slope,
            'max_normalized_comparator_violation':max_relative_energy_violation,
            'max_affine_error':max_affine_error,'last':records[-1],
            'interpretation':'Tail slopes are diagnostics only; transients are not theorem failures.'}


def scalar_checks(iterations: int) -> list[dict]:
    results=[]
    for p in (0.5,1.0,2.0,4.0):
        lipschitz=p*(p+1)
        for accelerated in (False,True):
            x=z=weight=0.0
            u=3.0
            fu=(1+u)**(-p)
            worst=0.0
            vals=[]
            for k in range(1,iterations+1):
                if accelerated:
                    a=(1+math.sqrt(1+4*lipschitz*weight))/(2*lipschitz)
                    nxt=weight+a
                    y=(weight*x+a*z)/nxt
                    z=max(0.0,z+a*p*(1+y)**(-p-1))
                    x=(weight*x+a*z)/nxt
                    weight=nxt; clock=weight; witness=z
                else:
                    x=max(0.0,x+p*(1+x)**(-p-1)/lipschitz)
                    clock=k/lipschitz; witness=x
                fx=(1+x)**(-p)
                err=clock*(fx-fu)+(witness-u)**2/2-u*u/2
                worst=max(worst,err/max(1.0,clock*fu,(witness-u)**2))
                if k>=iterations//2 and k%100==0:
                    vals.append((k,fx,x))
            assert worst<1e-9
            logk=np.log([a[0] for a in vals])
            slope=float(np.polyfit(logk,np.log([a[1] for a in vals]),1)[0])
            mult=2 if accelerated else 1
            results.append({'p':p,'method':'accelerated' if accelerated else 'projected_gradient',
                            'predicted_loss_exponent':-mult*p/(p+2),
                            'observed_loss_slope':slope,'energy_violation':worst})
    return results


def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument('--iterations',type=int,default=40000)
    parser.add_argument('--output',type=Path,default=Path('DYNAMICS_RESULTS.json'))
    args=parser.parse_args()
    if args.iterations<1000:
        raise ValueError('Use at least 1000 iterations for diagnostic slopes.')
    results=[]
    for m,fam in ((2,'fast'),(3,'fast'),(3,'slow')):
        problem=make_problem(m,fam)
        for acc in (False,True):
            results.append(simulate(problem,acc,args.iterations))
    data={'scope':'Floating-point diagnostic checks, not mathematical proof or bit-complexity guarantees.',
          'psd_cases':results,'scalar_cases':scalar_checks(args.iterations)}
    args.output.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))

if __name__=='__main__':
    main()
