"""Diagnostics for two historical-script corrections; not universal proofs.
Requires NumPy and SymPy. The reduction-map identity is checked exactly.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
import sympy as sp


def symmetric_traceless_sample(m: int, ell: int, rng):
    """Sample inside the real symmetric traceless space, not all m-by-m arrays."""
    basis = []
    for i in range(m):
        E = np.zeros((m, m)); E[i, i] = 1.; basis.append(E)
    for i in range(m):
        for j in range(i + 1, m):
            E = np.zeros((m, m)); E[i, j] = E[j, i] = 1 / np.sqrt(2)
            basis.append(E)
    n = len(basis)
    if not 1 <= ell <= n - 1:
        raise ValueError('ell must fit in the symmetric traceless space.')
    identity = np.r_[np.ones(m), np.zeros(n - m)] / np.sqrt(m)
    coefficients = rng.normal(size=(n, ell))
    coefficients -= identity[:, None] * (identity @ coefficients)[None, :]
    coefficients, _ = np.linalg.qr(coefficients)
    out = np.einsum('ja,jkl->akl', coefficients, np.asarray(basis))
    assert np.linalg.norm(out - out.transpose(0, 2, 1)) < 1e-12
    assert np.linalg.norm(np.trace(out, axis1=1, axis2=2)) < 1e-12
    assert np.linalg.norm(out.reshape(ell, -1) @ out.reshape(ell, -1).T - np.eye(ell)) < 1e-12
    return out


def exact_reduction_identity(m: int):
    """Check sum J_ij Y J_ij^T = tr(Y) I - Y for a symbolic symmetric Y."""
    Y = sp.zeros(m)
    for i in range(m):
        for j in range(i, m):
            Y[i, j] = Y[j, i] = sp.Symbol(f'y_{i}_{j}')
    total = sp.zeros(m)
    for i in range(m):
        for j in range(i + 1, m):
            K = sp.zeros(m); K[i, j] = 1; K[j, i] = -1
            total += K * Y * K.T
    assert total == sp.trace(Y) * sp.eye(m) - Y
    return {'m': m, 'identity': 'exact symbolic equality', 'unnormalized_kraus_count': m*(m-1)//2}


def main():
    rng = np.random.default_rng(20261112)
    samples = []
    for m in (4, 5, 6):
        B = symmetric_traceless_sample(m, m + 2, rng)
        lowest = float('inf')
        for _ in range(100):
            T = rng.normal(size=(m, m)); T -= T.T; T /= np.linalg.norm(T)
            C = np.array([[np.trace(T @ (A @ D - D @ A)) for D in B] for A in B])
            lowest = min(lowest, float(np.linalg.svd(C, compute_uv=False)[3]))
        samples.append({'m': m, 'traceless_symmetric_dimension': m + 2,
                        'smallest_sampled_fourth_singular_value': lowest,
                        'sample_count': 100})
    result = {
        'exact_real_symmetric_reduction_checks': [exact_reduction_identity(m) for m in (2, 3, 4)],
        'corrected_symmetric_commutator_sampling': samples,
        'scope': 'Exact symbolic finite-size checks and corrected sampling only. The general skew-Kraus identity is proved entrywise in the audit report; no generic theorem is inferred from sampling.'
    }
    Path(__file__).with_name('HISTORICAL_CORRECTION_RESULTS.json').write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
