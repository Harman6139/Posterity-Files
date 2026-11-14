"""Explicit models and a certified-budget algorithm for Milestone 39.

Python 3 + NumPy. All numerical experiments are diagnostics, not substitutes
for the universal proofs. The solver consumes noisy gradients only; values
are used only by the optional energy-diagnostic helper, never by an update.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import ceil, exp, isfinite, log, sqrt
from typing import Callable, Protocol
import numpy as np

Array = np.ndarray


class Tail(Protocol):
    s0: float
    doubling: float
    def value(self, z: float) -> float: ...
    def derivative(self, z: float) -> float: ...
    def second(self, z: float) -> float: ...
    def radius(self, s: float) -> float: ...


@dataclass(frozen=True)
class PowerTail:
    beta: float

    def __post_init__(self) -> None:
        if not isfinite(self.beta) or self.beta <= 0:
            raise ValueError("beta must be finite and positive")

    @property
    def p(self) -> float:
        return 1.0 / self.beta

    @property
    def b(self) -> float:
        return min(0.25, 1.0 / (4.0 * self.p * (self.p + 1.0)))

    @property
    def s0(self) -> float:
        return min(1.0 / 64.0, self.b * 2.0 ** (-self.p))

    @property
    def doubling(self) -> float:
        return 2.0 ** (self.beta + 1.0)

    def value(self, z: float) -> float:
        p, b = self.p, self.b
        return b * (1.0 + z) ** (-p) if z >= 0 else b * (1.0 - p*z + p*(p+1.0)*z*z/2.0)

    def derivative(self, z: float) -> float:
        p, b = self.p, self.b
        return -b*p*(1.0+z)**(-p-1.0) if z >= 0 else b*(-p+p*(p+1.0)*z)

    def second(self, z: float) -> float:
        p, b = self.p, self.b
        return b*p*(p+1.0)*(1.0+z)**(-p-2.0) if z >= 0 else b*p*(p+1.0)

    def radius(self, s: float) -> float:
        if not 0 < s < self.b:
            raise ValueError("radius expects 0 < s < phi(0)")
        return (self.b/s)**self.beta - 1.0


@dataclass(frozen=True)
class ExponentialTail:
    b: float = 0.25

    def __post_init__(self) -> None:
        if not 0 < self.b <= 0.25:
            raise ValueError("b must lie in (0,1/4]")

    @property
    def s0(self) -> float:
        return min(1.0/64.0, self.b/exp(1.0))

    @property
    def doubling(self) -> float:
        return 2.0

    def value(self, z: float) -> float:
        return self.b*exp(-z) if z >= 0 else self.b*(1.0-z+z*z/2.0)

    def derivative(self, z: float) -> float:
        return -self.b*exp(-z) if z >= 0 else self.b*(z-1.0)

    def second(self, z: float) -> float:
        return self.b*exp(-z) if z >= 0 else self.b

    def radius(self, s: float) -> float:
        if not 0 < s < self.b:
            raise ValueError("radius expects 0 < s < phi(0)")
        return log(self.b/s)


@dataclass(frozen=True)
class HardPair:
    tail: Tail
    delta: float
    sign: int

    def __post_init__(self) -> None:
        if self.sign not in (-1, 1):
            raise ValueError("sign must be -1 or +1")
        if not 0 < self.delta <= min(self.tail.s0, 0.125):
            raise ValueError("delta is outside the proved hard-pair range")

    @property
    def radius(self) -> float:
        return self.tail.radius(self.delta)

    @property
    def signal(self) -> float:
        return self.delta / self.radius

    def value(self, point: Array) -> float:
        x, z = map(float, point)
        s = x / self.radius
        return self.delta*(2.0*sqrt(s*s+3.0)-self.sign*s-3.0)+self.tail.value(z)

    def gradient(self, point: Array) -> Array:
        x, z = map(float, point)
        s = x / self.radius
        return np.array([self.signal*(2.0*s/sqrt(s*s+3.0)-self.sign), self.tail.derivative(z)])

    def hessian(self, point: Array) -> Array:
        x, z = map(float, point)
        s = x / self.radius
        return np.diag([6.0*self.delta/(self.radius**2*(s*s+3.0)**1.5), self.tail.second(z)])

    def common_surrogate_gradient(self, point: Array) -> Array:
        """Identical oracle for both signs; bias norm is exactly signal."""
        result = self.gradient(point)
        result[0] += self.sign*self.signal
        return result

    def sampled_loss(self, point: Array, scalar_sample: float) -> float:
        """Sample mean is the population value if E sample = sign*signal."""
        x, z = map(float, point)
        s = x / self.radius
        return self.delta*(2.0*sqrt(s*s+3.0)-3.0)-scalar_sample*x+self.tail.value(z)

    def sampled_gradient(self, point: Array, scalar_sample: float) -> Array:
        result = self.common_surrogate_gradient(point)
        result[0] -= scalar_sample
        return result


def project_ball(point: Array, radius: float) -> Array:
    length = float(np.linalg.norm(point))
    return point.copy() if length <= radius else point * (radius / length)


def accelerated_batched(
    oracle: Callable[[Array, int], Array],
    dimension: int,
    radius: float,
    steps: int,
    batch_size: int,
    *,
    max_samples: int = 10_000_000,
) -> Array:
    """oracle(y, batch_size) returns an average gradient at y.

    A hard resource cap raises an error; it does not silently truncate a
    run and then claim the theorem's guarantee.
    """
    if dimension < 1 or steps < 1 or batch_size < 1:
        raise ValueError("dimension, steps and batch_size must be positive")
    if not isfinite(radius) or radius <= 0:
        raise ValueError("radius must be finite and positive")
    if steps*batch_size > max_samples:
        raise RuntimeError("requested run exceeds max_samples")
    x = np.zeros(dimension)
    z = np.zeros(dimension)
    A = 0.0
    for _ in range(steps):
        a = (1.0 + sqrt(1.0 + 8.0*A))/4.0
        Ap = A + a
        y = (A*x+a*z)/Ap
        gradient = np.asarray(oracle(y.copy(), batch_size), dtype=float)
        if gradient.shape != (dimension,) or not np.all(np.isfinite(gradient)):
            raise ValueError("oracle returned an invalid gradient")
        zp = project_ball(z-a*gradient, radius)
        x = (A*x+a*zp)/Ap
        z, A = zp, Ap
    return x


def certified_budget(tail: Tail, epsilon: float, sigma: float, bias: float, parallel: int = 1) -> dict:
    if not 0 < epsilon/4.0 <= tail.s0:
        raise ValueError("epsilon/4 must lie in (0,s0]")
    if sigma < 0 or bias < 0 or parallel < 1:
        raise ValueError("noise, bias, and parallel parameters invalid")
    C = tail.doubling+2.0
    R = C*tail.radius(epsilon/4.0)
    K = ceil(4.0*R/sqrt(epsilon))
    M = max(1, ceil(2.0*sigma*sigma*K/epsilon))
    admissible = bias <= epsilon/(8.0*R)
    bound = epsilon/4.0+4.0*R*R/(K+1)**2+sigma*sigma*K/(2.0*M)+2.0*R*bias
    return {
        "radius": R, "outer_steps": K, "batch_size": M,
        "samples": K*M, "parallel_rounds": K*ceil(M/parallel),
        "bias_condition_met": admissible,
        "expected_error_upper_bound": bound,
        "maximum_certified_bias": epsilon/(8.0*R),
    }


def gaussian_pair_kl(delta: float, radius: float, sigma: float, samples: int) -> float:
    if sigma <= 0 or samples < 0:
        raise ValueError("sigma must be positive and samples nonnegative")
    return 2.0*samples*(delta/radius/sigma)**2
