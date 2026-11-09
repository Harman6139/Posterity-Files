#!/usr/bin/env python3
"""Small exact/numerical sanity checks for Milestones 37, 39 and 40.
Not a substitute for the analytic proofs. Requires numpy.
"""
import numpy as np

def pauli_bell():
    I=np.eye(2)
    Z=np.diag([1.,-1.])
    X=np.array([[0.,1.],[1.,0.]])
    J=np.array([[0.,1.],[-1.,0.]])
    U=np.column_stack([A.reshape(-1)/np.sqrt(2) for A in (I,Z,X,J)])
    assert np.allclose(U.T@U,np.eye(4))
    # Partial-trace decoder R^2 tensor R^2 -> R^2, t=2 exactly m.
    E=[]
    for psi in U.T:
        A=psi.reshape(2,2)
        E.append(A@A.T)
    E=np.asarray(E)
    assert np.allclose(E,np.eye(2)[None,:,:]/2)
    for u in (np.array([1.,0.]),np.array([0.,1.]),np.array([.6,.8])):
        X=np.outer(u,u)
        Y=np.kron(X,np.eye(2)/2)
        y=np.diag(U.T@Y@U)
        assert np.allclose(y,np.ones(4)/4)
        assert np.allclose(np.einsum("iaja->ij",Y.reshape(2,2,2,2)),X)
    return {"m":2,"n":4,"kraus_rank":2,"basis_outcomes":[.25]*4,
            "min_effect_eigenvalue":.5,"required_effect_eigenvalue":.25}

def reduction_positive_not_cp():
    m=3
    D=lambda Y:(np.trace(Y)*np.eye(m)-Y)/(m-1)
    E=np.array([D(np.outer(np.eye(m)[:,j],np.eye(m)[:,j]))
                for j in range(m)])
    eig=[np.linalg.eigvalsh(e) for e in E]
    assert all(abs(e[0])<1e-12 for e in eig)
    assert all(np.linalg.eigvalsh(D(np.outer(v,v))).min()>-1e-12
               for v in (np.eye(3)[0],np.eye(3)[1],np.ones(3)/np.sqrt(3)))
    return {"m":3,"n":3,"positive_trace_preserving":True,
            "basis_effect_ranks":[int(np.linalg.matrix_rank(x)) for x in E],
            "all_effects_singular":True,
            "approximate_floor_epsilon_plus_eta":1/3}

if __name__=="__main__":
    import json
    print(json.dumps([pauli_bell(),reduction_positive_not_cp()],indent=2))
