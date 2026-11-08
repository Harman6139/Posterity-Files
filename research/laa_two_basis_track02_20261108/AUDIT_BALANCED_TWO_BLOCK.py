#!/usr/bin/env python3
"""Independent numerical checks of Milestone 35. Requires numpy.
Uses the compiler from AUDIT_COMPLEMENT_TWIN.py (Milestone 31).
Tests do not substitute for the analytic depth and modulus proofs.
"""
import numpy as np
from AUDIT_COMPLEMENT_TWIN import compiler

def balanced(X):
    d=X.shape[0]
    return np.block([[X/2,np.zeros((d,d))],
                     [np.zeros((d,d)),np.trace(X)*np.eye(d)-X/2]])

def run(G):
    d,M=G.shape
    F=compiler(G)
    assert np.linalg.norm(F@F.T-np.eye(2*d))<1e-10
    # The admissible ONB is independent of the measured operator system.
    for i in range(d):
        e=np.eye(d)[:,i]
        for s in (-1,1):
            f=np.r_[e,s*e]/np.sqrt(2)
            aa,bb=f[:d],f[d:]
            pull=(np.outer(aa,aa)-np.outer(bb,bb))/2+(bb@bb)*np.eye(d)
            assert np.linalg.norm(pull-.5*np.eye(d))<1e-10
    X=np.outer(np.eye(d)[:,0],np.eye(d)[:,0])
    J=balanced(X)
    lower=J[d:,d:]
    assert np.min(np.linalg.eigvalsh(lower))>.49
    assert np.linalg.matrix_rank(J)==d+1
    Y=np.random.default_rng(d).normal(size=(d,d))
    Y=(Y+Y.T)/2
    lhs=np.linalg.norm(balanced(Y))**2
    rhs=.5*np.linalg.norm(Y)**2+(d-1)*np.trace(Y)**2
    assert abs(lhs-rhs)<1e-9
    return {"d":d,"source_M":M,"rankone_compressed_rank":int(np.linalg.matrix_rank(J)),
            "auxiliary_gap":float(np.min(np.linalg.eigvalsh(lower))),
            "frame_error":float(np.linalg.norm(F@F.T-np.eye(2*d))),
            "norm_identity_error":float(abs(lhs-rhs))}

def main():
    tetra=np.array([[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]],float)/2
    print(run(np.eye(2)))
    print(run(tetra))

if __name__=="__main__":main()
