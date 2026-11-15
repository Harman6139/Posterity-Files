"""Reproducible diagnostics for the analytic two-basis quotient construction.
The proof is algebraic; these checks are not a substitute for it.
Dependencies: numpy; sympy for the exact rational identity check.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np


def build(A: np.ndarray, z: np.ndarray, b: np.ndarray):
    p, m, _ = A.shape
    H = np.einsum('i,ijk->jk', z, A)
    if np.linalg.eigvalsh(H)[0] <= 0:
        raise ValueError('The supplied trace certificate is not positive definite.')
    rho = float(np.trace(np.linalg.inv(H)))
    alpha = m * rho * rho
    tau = float(z @ b)
    k, d = m*m, (m+1)**2
    anc = 2*m
    aux = lambda i,j: anc + 1 + i*m + j
    e = np.eye(d)
    vectors, values = [], []
    base_idx, copy_idx, src_idx = {}, {}, {}
    t = np.r_[np.full(2*m, rho*tau/2), tau, np.full(k, alpha*tau)]
    for j in range(d):
        vectors.append(e[j]); values.append(t[j])
    for block in range(2):
        for i in range(m):
            for j in range(i+1,m):
                for sign in (1,-1):
                    base_idx[block,i,j,sign] = len(vectors)
                    vectors.append(e[block*m+i]+sign*e[block*m+j])
                    values.append(rho*tau)
    for i in range(m):
        for j in range(m):
            for sigma in (1,-1):
                for eta in (1,-1):
                    copy_idx[i,j,sigma,eta] = len(vectors)
                    vectors.append(e[anc]+sigma*e[aux(i,j)]+eta*e[i]-sigma*eta*e[m+j])
                    values.append((1+alpha+rho)*tau)
    for a in range(p):
        av = np.zeros(d); av[anc+1:] = A[a].reshape(-1)
        beta = b[a] - rho*tau*np.trace(A[a])/2
        for sign in (1,-1):
            src_idx[a,sign] = len(vectors)
            vectors.append(e[anc]+sign*av)
            values.append(tau*(1+alpha*np.sum(A[a]**2))+2*sign*beta)
    raw = np.stack(vectors, axis=1)
    c0 = np.asarray(values)
    M0 = raw.shape[1]
    assert M0 == 7*m*m+1+2*p
    R0 = np.zeros((p,M0))
    for a in range(p):
        for block in range(2):
            for i in range(m):
                R0[a,block*m+i] += A[a,i,i]/2
            for i in range(m):
                for j in range(i+1,m):
                    for sign in (1,-1):
                        R0[a,base_idx[block,i,j,sign]] += sign*A[a,i,j]/4
        for i in range(m):
            for j in range(m):
                for sigma in (1,-1):
                    for eta in (1,-1):
                        R0[a,copy_idx[i,j,sigma,eta]] -= sigma*A[a,i,j]/8
        for sign in (1,-1):
            R0[a,src_idx[a,sign]] += sign/4
    S_A = float(np.sum(A*A))
    L = 4*m*m+6*m+2*p+6+2*S_A
    eps = 1/(2*L)
    Q0 = raw @ raw.T
    q_expected = np.zeros((d,d))
    q_expected[:2*m,:2*m] = (6*m-1)*np.eye(2*m)
    q_expected[anc,anc] = 1+4*m*m+2*p
    AA = A.reshape(p,k)
    q_expected[anc+1:,anc+1:] = 5*np.eye(k)+2*AA.T@AA
    completion = np.zeros((d,d))
    completion[:2*m,:2*m] = np.sqrt(1-eps*(6*m-1))*np.eye(2*m)
    completion[anc,anc] = np.sqrt(1-eps*(1+4*m*m+2*p))
    rem_aux = np.eye(k)-eps*q_expected[anc+1:,anc+1:]
    completion[anc+1:,anc+1:] = np.linalg.cholesky(rem_aux)
    ccomp = np.r_[np.full(2*m,(1-eps*(6*m-1))*rho*tau/2),
                     (1-eps*(1+4*m*m+2*p))*tau,
                     alpha*tau*np.sum(completion[anc+1:,anc+1:]**2,axis=0)]
    G = np.c_[np.sqrt(eps)*raw, completion]
    c = np.r_[eps*c0,ccomp]
    M = G.shape[1]
    F = np.c_[np.sqrt(2/3)*np.eye(d),G/np.sqrt(3)]
    N = F.shape[1]
    assert M == 8*m*m+2*m+2+2*p
    assert N == 9*m*m+4*m+3+2*p
    P = F.T @ F
    U = 2*P-np.eye(N)
    W = np.r_[np.eye(m),np.eye(m)]/np.sqrt(2)
    V0 = np.zeros((m,d)); V0[:,:2*m] = W.T
    V = V0 @ F
    y0 = np.r_[(2/3)*t,c/3]
    yd = np.r_[-np.ones(d),2*np.ones(M)]
    Dsigned = np.diag(yd)
    stress = Dsigned+U@Dsigned@U.T
    Kframe = 3*(1+np.sqrt(d+4*M))/np.sqrt(2)
    Ksource = Kframe*np.linalg.norm(R0,2)/eps
    checks = {
        'raw_frame_formula': float(np.linalg.norm(Q0-q_expected)),
        'parseval': float(np.linalg.norm(G@G.T-np.eye(d))),
        'orthogonal': float(np.linalg.norm(U@U.T-np.eye(N))),
        'decoder_coisometry': float(np.linalg.norm(V@V.T-np.eye(m))),
        'target_trace_identity': float(abs(c.sum()-t.sum())),
        'stress_data_zero': float(abs(2*yd@y0)),
        'source_data_identity': float(np.linalg.norm(R0@c0-b)),
        'source_operator_identity': max(float(np.linalg.norm(
            np.einsum('j,ij,kj->ik',R0[a],raw,raw)-V0.T@A[a]@V0)) for a in range(p)),
        'stress_gap_min_eigenvalue': float(np.linalg.eigvalsh(stress-2*(np.eye(N)-P))[0]),
        'completion_gap': float(np.linalg.eigvalsh(np.eye(d)-eps*Q0)[0]),
    }
    def encode(X):
        tx = float(np.sum(H*X))
        B = X-rho*tx*np.eye(m)/2
        Z = np.zeros((d,d))
        Z[:m,:m] = Z[m:2*m,m:2*m] = rho*tx*np.eye(m)/2
        Z[:m,m:2*m] = B
        Z[m:2*m,:m] = B.T
        Z[anc,anc] = tx
        Z[anc,anc+1:] = B.reshape(-1)
        Z[anc+1:,anc] = B.reshape(-1)
        Z[anc+1:,anc+1:] = alpha*tx*np.eye(k)
        return F.T@Z@F,Z
    def measure(Y):
        return np.r_[np.diag(Y),np.diag(U.T@Y@U)]
    return locals()


def exact_raw_identity():
    import sympy as sp
    m=2; k=4; d=9; anc=4
    mats=[sp.eye(m),sp.Matrix([[2,3],[3,-1]]),sp.Matrix([[0,1],[1,4]])]
    p=len(mats); e=sp.eye(d)
    col=lambda j:e[:,j]
    vs=[]; base_idx={}; copy_idx={}; src_idx={}
    for j in range(d): vs.append(col(j))
    for block in range(2):
        for i in range(m):
            for j in range(i+1,m):
                for s in (1,-1):
                    base_idx[block,i,j,s]=len(vs)
                    vs.append(col(block*m+i)+s*col(block*m+j))
    for i in range(m):
        for j in range(m):
            for s in (1,-1):
                for u in (1,-1):
                    copy_idx[i,j,s,u]=len(vs)
                    vs.append(col(anc)+s*col(anc+1+i*m+j)+u*col(i)-s*u*col(m+j))
    for a,A in enumerate(mats):
        av=sp.zeros(d,1)
        for i in range(m):
            for j in range(m): av[anc+1+i*m+j]=A[i,j]
        for s in (1,-1):
            src_idx[a,s]=len(vs); vs.append(col(anc)+s*av)
    raw=sp.Matrix.hstack(*vs)
    V0=sp.zeros(m,d)
    # Work with sqrt(2) symbolically; the resulting symmetric form is rational.
    for i in range(m): V0[i,i]=V0[i,m+i]=1/sp.sqrt(2)
    for a,A in enumerate(mats):
        r=sp.zeros(1,len(vs))
        for block in range(2):
            for i in range(m):r[block*m+i]+=A[i,i]/2
            for i in range(m):
                for j in range(i+1,m):
                    for s in (1,-1):r[base_idx[block,i,j,s]]+=s*A[i,j]/4
        for i in range(m):
            for j in range(m):
                for s in (1,-1):
                    for u in (1,-1):r[copy_idx[i,j,s,u]]-=s*A[i,j]/8
        for s in (1,-1):r[src_idx[a,s]]+=sp.Rational(s,4)
        assert raw*sp.diag(*list(r))*raw.T == V0.T*A*V0
    return {'m':m,'p':p,'source_operator_identity':'exact rational equality verified'}


def main():
    rng=np.random.default_rng(6139)
    records=[]
    for m in (1,2,3,4):
        p=1+m*m
        Z=rng.integers(-2,3,size=(m,m)).astype(float)
        H=Z.T@Z+np.eye(m)
        A=np.empty((p,m,m)); A[0]=H
        for a in range(1,p):
            T=rng.integers(-3,4,size=(m,m)).astype(float)
            A[a]=(T+T.T)/2
        z=np.r_[1.,np.zeros(p-1)]
        for rank in sorted(set((0,1,m))):
            B=rng.normal(size=(m,rank))
            X=B@B.T
            b=np.einsum('aij,ij->a',A,X)
            obj=build(A,z,b)
            E,J=obj['encode'](X)
            checks=obj['checks']
            checks.update({
                'forward_min_eigenvalue':float(np.linalg.eigvalsh(J)[0]),
                'section_identity':float(np.linalg.norm(obj['V']@E@obj['V'].T-X)),
                'encoded_data':float(np.linalg.norm(obj['measure'](E)-np.r_[obj['y0'],obj['y0']])),
            })
            ratios=[]
            for _ in range(4):
                Zr=rng.normal(size=(obj['N'],min(4,obj['N'])))
                Y=Zr@Zr.T
                residual=np.linalg.norm(obj['measure'](Y)-np.r_[obj['y0'],obj['y0']])
                decoded=np.einsum('aij,ij->a',A,obj['V']@Y@obj['V'].T)-b
                ratios.append(float(np.linalg.norm(decoded)/residual))
            checks['largest_sampled_residual_ratio']=max(ratios)
            checks['proved_residual_bound']=float(obj['Ksource'])
            records.append({'m':m,'p':p,'rank_X':rank,'d':obj['d'],'M':obj['M'],'N':obj['N'],'checks':checks})
    out={'seed':6139,'exact':exact_raw_identity(),'numerical':records,
         'scope':'Diagnostics only; universal validity follows from the manuscript identities.'}
    path=Path(__file__).with_name('AUDIT_RESULTS.json')
    path.write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
