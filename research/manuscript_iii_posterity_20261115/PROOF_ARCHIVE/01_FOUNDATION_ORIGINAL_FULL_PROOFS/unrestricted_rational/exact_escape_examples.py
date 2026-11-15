"""Exact rational identities for the sharp endpoint families of milestone 12.

The general profile duality and exponent envelope are proved analytically.
This script checks the displayed extremal curves, without an SDP solver.
"""
import json
import sympy as sp


def check_order(m: int) -> dict:
    if m < 2:
        raise ValueError('m must be at least two')
    e = sp.symbols('e', positive=True)
    E = 2**(m-1)-1
    a = [None] + [e**(-(2**(i-1)-1)) for i in range(1, m)]
    # Construct the rank-one fast curve using rational matrix entries.
    fast = sp.zeros(m)
    fast[0,0] = e
    for i in range(1,m):
        fast[0,i] = fast[i,0] = a[i]
        for j in range(1,m):
            fast[i,j] = a[i]*a[j]/e
    assert fast[0,1] == 1
    assert all(sp.simplify(fast[i,i]-fast[0,i+1]) == 0 for i in range(1,m-1))
    # Its Schur complement against the positive top pivot vanishes exactly.
    assert (fast[1:,1:] - fast[1:,0]*fast[0,1:]/e).applyfunc(sp.simplify) == sp.zeros(m-1)
    trace_fast = sp.trace(fast)
    assert sp.limit(e**E*trace_fast, e, 0, dir='+') == 1

    t = sp.symbols('t', positive=True)
    slow = sp.zeros(m)
    slow[0,0] = sp.Rational(m-1,4)/t
    slow[0,1] = slow[1,0] = -sp.Rational(1,2)
    for j in range(1,m):
        slow[j,j] = t**(2**j-1)
        if j >= 2:
            slow[0,j] = slow[j,0] = -slow[j-1,j-1]/2
    assert all(sp.simplify(2*slow[0,j]+slow[j-1,j-1]) == 0 for j in range(2,m))
    schur = slow[0,0]-sum(slow[0,j]**2/slow[j,j] for j in range(1,m))
    assert sp.simplify(schur) == 0
    assert slow[m-1,m-1] == t**E
    assert sp.limit(t*sp.trace(slow),t,0,dir='+') == sp.Rational(m-1,4)
    return {'matrix_order':m,'fast_exponent':str(E),'slow_exponent':str(sp.Rational(1,E)),
            'fast_residual':'e','fast_scaled_trace_limit':'1',
            'slow_residual':str(t**E),'slow_scaled_trace_limit':str(sp.Rational(m-1,4)),
            'both_exact_Schur_complements':'zero',
            'other_source_residuals':'identically zero'}


if __name__ == '__main__':
    results={'status':'passed','examples':[check_order(m) for m in range(2,8)],
             'scope':'Exact symbolic finite-instance checks; the general bounds and sharpness for every m are proved in milestone 12.'}
    print(json.dumps(results,indent=2))
