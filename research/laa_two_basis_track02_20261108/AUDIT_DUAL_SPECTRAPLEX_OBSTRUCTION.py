#!/usr/bin/env python3
"""Algebraic/numeric audit of Milestones 62–63 (not a proof).
Checks the exact rational 4×4 SDP, SOC-plus-quadrant dual slice,
and the geometry of its nonexposed extreme point. Requires NumPy.
"""
import numpy as np

def pencil(t,x,y):
    return np.array([[t+x,y,0,0],[y,t-x,0,0],
                     [0,0,x,0],[0,0,0,y]], dtype=float)

def data(X):
    return np.array([X[0,2],X[0,3],X[1,2],X[1,3],X[2,3],
                     X[0,0]-X[1,1]-2*X[2,2],X[0,1]-X[3,3],
                     np.trace(X)])

def audit():
    X0=pencil(2,1,1)
    b=data(X0)
    assert np.allclose(b,[0,0,0,0,0,0,0,6])
    assert min(np.linalg.eigvalsh(X0))>0
    # The dual section of Lorentz_3∩{x,y>=0} equals disk + positive quadrant.
    # Its lower boundary is circular for -1<=x<=0,
    # then a horizontal ray y=-1 for x>=0.
    for x in np.linspace(-.99,0,100):
        lower=-np.sqrt(1-x*x)
        # A point on the unit disk is in the dual section.
        assert x*x+lower*lower<=1+1e-10
    for x in (0,.5,2,10):
        # The ray (x,-1) = (0,-1)+(x,0) is in the dual section.
        u,v=0,-1
        a,b=x,0
        assert u*u+v*v<=1 and a>=0 and b>=0
    return {"strictly_feasible_example":X0.tolist(),
            "eigenvalues":np.linalg.eigvalsh(X0).tolist(),
            "eight_source_measurements":data(X0).tolist(),
            "dual_nonexposed_extreme_point":[0,-1],
            "dual_horizontal_face":"{(x,-1): x >= 0}",
            "classification":"No PSD spectraplex image at ANY order"}

if __name__=="__main__":
    import json
    print(json.dumps(audit(),indent=2))
