"""Reproducible diagnostic constructor for the randomized escape lower bound.

The proof uses exact real arithmetic. This module uses floating point and is
for checking identities, derivatives and locality, not proving lower bounds.
The core's additive minimum is independent of its orthonormal frame. We leave
that constant symbolic: shifting it does not change any derivative or locality
check. No numerical minimum is silently treated as exact.
"""
from dataclasses import dataclass
import math
import numpy as np


@dataclass(frozen=True)
class Parameters:
    beta: float
    m: int
    radius: float
    gamma: float
    slope: float
    penalty: float
    join_width: float
    wall_radius: float
    gap_scale: float

    @classmethod
    def make(cls, beta: float, m: int):
        if not math.isfinite(beta) or beta <= 0 or m < 2:
            raise ValueError('Require finite beta>0 and integer m>=2.')
        theta = 2.0 / (2.0 * beta + 1.0)
        radius = m ** (beta * theta)
        gamma = radius / (16.0 * m ** 1.5)
        a = gamma / 128.0
        return cls(beta, m, radius, gamma, a, 16*a*a, 64*a*a,
                   radius/4.0, a*radius/math.sqrt(m))


def sparse_max(scores, penalty):
    """Value, gradient and Hessian in scores for max_p <p,s>-penalty sum p^1.5.

    Solve sum ((s_i-nu)_+/(1.5*penalty))^2=1 in a scaled interval.
    """
    s = np.asarray(scores, dtype=float)
    if s.ndim != 1 or not len(s) or not np.all(np.isfinite(s)) or penalty <= 0:
        raise ValueError('Invalid scores or regularization.')
    c = 1.5 * penalty
    offset = float(s.max())
    r = (s - offset) / c
    lo, hi = -1.0, 0.0
    for _ in range(80):
        mid = (lo + hi) / 2.0
        if np.square(np.maximum(r-mid, 0.0)).sum() > 1.0:
            lo = mid
        else:
            hi = mid
    h = np.maximum(r-(lo+hi)/2.0, 0.0)
    weights = h*h
    # Retain the formula, rather than silently renormalizing a failed root.
    if abs(float(weights.sum()) - 1.0) > 1e-10:
        raise ArithmeticError('Threshold solve failed.')
    w = 2.0*h/c
    jac = np.diag(w) - np.outer(w,w)/w.sum()
    value = float(s @ weights - penalty*np.power(weights, 1.5).sum())
    return value, weights, jac


def smooth_absolute(t, eps):
    if eps <= 0:
        raise ValueError('Positive smoothing width required.')
    if abs(t) >= eps:
        return abs(t), (1.0 if t >= 0 else -1.0), 0.0
    u = t/eps
    return (eps*(3.0/8.0 + 3*u*u/4.0-u**4/8.0),
            3*u/2.0-u**3/2.0,
            3*(1-u*u)/(2*eps))


class HardCore:
    """Core F_U before subtracting its orientation-independent minimum."""
    def __init__(self, frame, beta):
        u = np.asarray(frame, dtype=float)
        if u.ndim != 2 or u.shape[0] < u.shape[1] or u.shape[1] < 2:
            raise ValueError('Need a d by m frame with d>=m>=2.')
        if not np.allclose(u.T @ u, np.eye(u.shape[1]), atol=1e-10, rtol=1e-10):
            raise ValueError('Columns must be orthonormal.')
        self.u = u
        self.p = Parameters.make(beta, u.shape[1])
        self.d = u.shape[0]

    def wall(self, x):
        x = np.asarray(x, dtype=float)
        a = self.p.slope
        b = math.sqrt(float(x@x) + self.p.wall_radius**2)
        val = 2*a*(b-self.p.radius)
        grad = 2*a*x/b
        hess = 2*a*(np.eye(self.d)/b - np.outer(x,x)/(b**3))
        return val,grad,hess

    def evaluate(self, x, prefix=None):
        x = np.asarray(x, dtype=float)
        if x.shape != (self.d,) or not np.all(np.isfinite(x)):
            raise ValueError('Bad input vector.')
        j = self.p.m if prefix is None else int(prefix)
        if not 1 <= j <= self.p.m:
            raise ValueError('Bad prefix.')
        a = self.p.slope
        u = self.u[:,:j]
        ell = a*(u.T@x - self.p.gamma*np.arange(j))
        hv,pv,jac = sparse_max(ell,self.p.penalty)
        hg = a*u@pv
        hh = a*a*(u@jac@u.T)
        wv,wg,wh = self.wall(x)
        ab,ap,app = smooth_absolute(hv-wv,self.p.join_width)
        mu = (1+ap)/2.0
        val = (hv+wv+ab)/2.0
        grad = mu*hg + (1-mu)*wg
        hess = mu*hh + (1-mu)*wh + (app/2)*np.outer(hg-wg,hg-wg)
        return val,grad,hess


def tail(z, beta):
    p = 1.0/beta
    a = min(0.25,1.0/(4*p*(p+1)))
    if z >= 0:
        return (a*(1+z)**(-p), -a*p*(1+z)**(-p-1),
                a*p*(p+1)*(1+z)**(-p-2))
    return (a*(1-p*z+p*(p+1)*z*z/2),
            a*(-p+p*(p+1)*z), a*p*(p+1))


def sufficient_dimension(rounds, batch=1, failure=0.25):
    if rounds < 1 or batch < 1 or not 0 < failure < 1:
        raise ValueError('Invalid round/batch/probability parameters.')
    m = rounds+1
    return m + math.ceil((2**19)*m**3*math.log(8*batch*m*m/failure))
