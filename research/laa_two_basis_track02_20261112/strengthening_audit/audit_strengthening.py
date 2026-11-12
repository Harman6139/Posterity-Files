"""Adversarial diagnostics for milestones 06--08. Not the analytic proof.
Run with OPENBLAS_NUM_THREADS=1 python audit_strengthening.py.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
from dense_anchor import build


def amplified_inner(q, X, n):
    """The specified CP extension on block matrices, not entrywise scalar J."""
    c=q['core'];m=c['m'];d=c['d'];H=c['H'];rho=c['rho'];alpha=c['alpha']
    xb=X.reshape(m,n,m,n)
    tt=np.einsum('ij,iajb->ab',H,xb)
    Z=np.zeros((d*n,d*n)); z4=Z.reshape(d,n,d,n)
    for i in range(m):
        z4[i,:,i,:]=rho*tt/2; z4[m+i,:,m+i,:]=rho*tt/2
        for j in range(m):
            B=xb[i,:,j,:]-(rho*tt/2 if i==j else 0)
            z4[i,:,m+j,:]=B
            z4[m+i,:,j,:]=B
    a=c['anc'];s=c['shield']
    z4[a,:,a,:]=tt;z4[s,:,s,:]=tt
    for i in range(m):
        for j in range(m):
            ix=a+1+i*m+j
            copied=(xb[i,:,j,:]+xb[j,:,i,:])/2-(rho*tt/2 if i==j else 0)
            z4[a,:,ix,:]=copied;z4[ix,:,a,:]=copied
            z4[ix,:,ix,:]=alpha*tt
    return Z


def measure_amp(q,Y,n):
    U=np.kron(q['U'],np.eye(n));N=q['N']
    Y2=U.T@Y@U
    y=Y.reshape(N,n,N,n);y2=Y2.reshape(N,n,N,n)
    return np.stack([y[i,:,i,:] for i in range(N)]+[y2[i,:,i,:] for i in range(N)])


def test_case(A,z,X,label,rng):
    bd=np.einsum('aij,ij->a',A,X)
    q=build(A,z,bd);Y,Za=q['encode'](X)
    errors=dict(q['checks'])
    errors['forward_data']=float(np.linalg.norm(q['measure'](Y)-q['target']))
    errors['decoded_forward']=float(np.linalg.norm(q['V']@Y@q['V'].T-X))
    errors['inner_min_eigenvalue']=float(np.linalg.eigvalsh(Za)[0])
    errors['predicted_rank']=1 if np.trace(X)==0 else int(np.linalg.matrix_rank(X,tol=1e-9)+q['d']-q['m']+1)
    errors['observed_inner_rank']=int(np.linalg.matrix_rank(Za,tol=1e-8))
    C=rng.normal(size=X.shape);C=(C+C.T)/2
    Ctilde=q['V'].T@C@q['V']
    L=rng.normal(size=(q['N'],3));Ynoise=L@L.T
    err=np.linalg.norm(q['measure'](Ynoise)-q['target'])
    src=np.einsum('aij,ij->a',A,q['V']@Ynoise@q['V'].T)-bd
    assert np.linalg.norm(src)<=q['Kr']*err+1e-8
    errors['objective_error']=float(abs(np.sum(Ctilde*Ynoise)-np.sum(C*(q['V']@Ynoise@q['V'].T))))
    lam=rng.normal(size=len(A));Cdual=np.einsum('a,aij->ij',lam,A)+np.eye(q['m'])
    f=q['Robs'].T@lam;w=np.r_[q['weights'],q['weights']]
    gamma=np.r_[f/2,f/2]-np.max(np.abs(f))*w/2
    N=q['N'];dualB=np.diag(gamma[:N])+q['U']@np.diag(gamma[N:])@q['U'].T
    slack=q['V'].T@Cdual@q['V']-dualB
    errors['dual_lift_value_error']=float(abs(q['target']@gamma-bd@lam))
    errors['dual_lift_relative_psd_error']=float(np.linalg.eigvalsh(slack)[0]/max(1,np.linalg.norm(slack,2)))
    # Pull back a genuinely positive ambient dual slack.
    gamma2=np.r_[-np.full(N,2*np.linalg.norm(C,2)+1),np.zeros(N)]
    S=Ctilde-np.diag(gamma2[:N])
    m=q['m'];pb=np.zeros((m,m))
    for i in range(m):
        for j in range(i,m):
            H=np.zeros((m,m));H[i,j]=H[j,i]=1
            EH,_=q['encode'](H);Ezero,_=q['encode'](np.zeros((m,m)))
            val=float(np.sum(S*(EH-Ezero)))
            pb[i,j]=pb[j,i]=val if i==j else val/2
    errors['dual_pullback_min_eigenvalue']=float(np.linalg.eigvalsh(pb)[0])
    for name in ['coisometry','signed_isotropy','orthogonality','decoder_coisometry','stress_identity','extraction_operator']:
        assert errors[name]<1e-8,(label,name,errors[name])
    assert errors['minimum_overlap']>0 and errors['minimum_target']>0
    assert errors['fourth_moment_multiset_gap']>1e-12
    assert errors['forward_data']<1e-8 and errors['decoded_forward']<1e-8
    assert errors['inner_min_eigenvalue']>-1e-8
    assert errors['predicted_rank']==errors['observed_inner_rank']
    assert errors['dual_lift_relative_psd_error']>-1e-10
    return {'label':label,'checks':errors}


def choi_tests(rng):
    records=[]
    for m in [1,2,3,4]:
        B=rng.integers(-2,3,size=(m,m)).astype(float);H=B.T@B+np.eye(m)
        G=np.linalg.inv(H);rho=2*np.trace(G);alpha=m*rho*rho;k=m*m
        Ts=[]
        for i in range(m):
            for j in range(m):
                S=np.zeros((m,m));S[i,j]+=.5;S[j,i]+=.5
                Ts.append(S-(rho/2)*H*(i==j))
        W=np.kron(np.diag(np.r_[1.,np.full(k,alpha)]),H)
        for j,T in enumerate(Ts):W[:m,(j+1)*m:(j+2)*m]=T;W[(j+1)*m:(j+2)*m,:m]=T
        ev,Q=np.linalg.eigh(G);gs=(Q*np.sqrt(ev))@Q.T
        ss=sum((gs@T@gs)@(gs@T@gs) for T in Ts)
        exact=(G@G+np.trace(G)*G)/2-rho*G+m*rho*rho*np.eye(m)/4
        om=np.eye(m).reshape(-1)
        W1=rho*np.kron(np.eye(m),H)-np.outer(om,om)
        assert np.linalg.eigvalsh(W1)[0]>0 and np.linalg.eigvalsh(W)[0]>0
        assert np.linalg.norm(ss-exact)<1e-8
        assert np.linalg.eigvalsh(alpha*np.eye(m)/4-ss)[0]>-1e-9
        records.append({'m':m,'complement_choi_min_eigenvalue':float(np.linalg.eigvalsh(W1)[0]),
                        'arrow_choi_min_eigenvalue':float(np.linalg.eigvalsh(W)[0]),
                        'sum_of_squares_identity_error':float(np.linalg.norm(ss-exact)),
                        'normalized_squared_cross_norm':float(np.linalg.norm(ss,2)),
                        'proved_upper_bound':float(alpha/4)})
    return records


def ancilla_test(rng):
    m,n=2,3
    A=np.stack([np.eye(m),np.array([[2.,1.],[1.,-1.]])]);z=np.array([1.,0.])
    q=build(A,z,np.zeros(len(A)))
    fac=rng.normal(size=(m*n,4));X=fac@fac.T
    Z=amplified_inner(q,X,n)
    Za=np.zeros(((q['d']+1)*n,)*2);Za[:-n,:-n]=Z;Za[-n:,-n:]=np.eye(n)
    FF=np.kron(q['F'],np.eye(n));Y=FF.T@Za@FF
    VV=np.kron(q['V'],np.eye(n));decoded=VV@Y@VV.T
    bd=np.einsum('kij,iajb->kab',A,X.reshape(m,n,m,n))
    # Explicit affine data map from evaluations on the original scalar data basis.
    offset=q['target'];Phi=[]
    for i in range(len(A)):
        ei=np.eye(len(A))[i]; qi=build(A,z,ei)
        assert np.linalg.norm(qi['F']-q['F'])<1e-12
        Phi.append(qi['target']-offset)
    Phi=np.column_stack(Phi)
    expected=np.einsum('ki,iab->kab',Phi,bd)+offset[:,None,None]*np.eye(n)
    meas=measure_amp(q,Y,n)
    L=rng.normal(size=(q['N']*n,5));arbitrary=L@L.T
    rr=np.linalg.norm(measure_amp(q,arbitrary,n)-expected)
    XX=VV@arbitrary@VV.T
    sr=np.linalg.norm(np.einsum('kij,iajb->kab',A,XX.reshape(m,n,m,n))-bd)
    assert np.linalg.eigvalsh(Z)[0]>-1e-8
    assert np.linalg.norm(decoded-X)<1e-8
    assert np.linalg.norm(meas-expected)<1e-8
    assert sr<=q['Kr']*rr
    return {'m':m,'ancilla':n,'source_rank':int(np.linalg.matrix_rank(X)),
            'amplified_inner_min_eigenvalue':float(np.linalg.eigvalsh(Z)[0]),
            'section_error':float(np.linalg.norm(decoded-X)),
            'matrix_valued_data_error':float(np.linalg.norm(meas-expected)),
            'sampled_residual_ratio':float(sr/rr),'same_scalar_bound':float(q['Kr'])}


def cascade(k):
    m=k+1;mats=[np.eye(m)]
    last=np.zeros((m,m));last[-1,-1]=1;mats.append(last)
    for i in range(1,k):
        C=np.zeros((m,m));C[i,i]=1;C[0,i+1]=C[i+1,0]=-.5;mats.append(C)
    C=np.zeros((m,m));C[0,1]=C[1,0]=.5;mats.append(C)
    A=np.stack(mats);z=np.r_[1.,np.zeros(len(A)-1)];bd=z.copy();Xstar=np.diag(np.r_[1.,np.zeros(k)])
    return A,z,bd,Xstar


def leakage_tests():
    result=[]
    for k in [1,2,3]:
        A,z,bd,Xstar=cascade(k);q=build(A,z,bd)
        Y0,Z0=q['encode'](Xstar)
        for t in [.7,.5,.35]:
            v=np.r_[1.,0.,[t**(2**j) for j in range(1,k)]]
            W=np.outer(v,v);W[1,1]+=t*t;X=W/np.trace(W)
            _,Za=q['encode'](X)
            h=np.zeros(k+1);h[1]=np.sqrt(X[1,1]/2)
            hp=q['core']['V0'].T@h
            shield=q['core']['shield']
            Za[:q['d'],shield]+=hp;Za[shield,:q['d']]+=hp
            YY=q['F'].T@Za@q['F']
            sr=np.linalg.norm(np.einsum('aij,ij->a',A,X)-bd)
            predicted=t**(2**k)/np.trace(W)
            rr=np.linalg.norm(q['measure'](YY)-q['target'])
            leak=np.trace(X)-X[0,0]
            lower=np.sqrt(X[1,1])
            assert abs(sr-predicted)<1e-12
            assert np.linalg.eigvalsh(Za)[0]>-1e-8
            assert np.linalg.norm(q['V']@YY@q['V'].T-X)<1e-8
            # The exact two-list residual is 4 epsilon h^2 times source residual.
            expected=4*q['eps']*q['h']**2*sr
            assert abs(rr-expected)<1e-8
            result.append({'depth':k,'t':t,'source_residual':sr,'source_distance':float(np.linalg.norm(X-Xstar)),
                           'source_leakage':float(leak),'lifted_residual':float(rr),
                           'predicted_lifted_residual':float(expected),
                           'ambient_distance_certified_lower_bound':float(lower),
                           'predicted_source_exponent':2.**(-(k-1)),
                           'predicted_ambient_exponent':2.**(-k)})
    return result


def exact_checks():
    import sympy as sp
    m=2;H=sp.Matrix([[2,1],[1,3]]);G=H.inv();rho=2*sp.trace(G);alpha=m*rho**2
    Ts=[];Ss=[]
    for i in range(m):
        for j in range(m):
            S=sp.zeros(m);S[i,j]+=sp.Rational(1,2);S[j,i]+=sp.Rational(1,2)
            Ss.append(S);Ts.append(S-rho*H*int(i==j)/2)
    assert sum((S*G*S for S in Ss),sp.zeros(m))==(G+sp.trace(G)*sp.eye(m))/2
    # Equivalent rational congruence of the normalized identity (no matrix square roots).
    lhs=sum((T*G*T for T in Ts),sp.zeros(m))
    rhs=(G+sp.trace(G)*sp.eye(m))/2-rho*sp.eye(m)+m*rho**2*H/4
    assert lhs==rhs
    for k in range(1,7):
        t=sp.symbols('t',positive=True)
        v=sp.Matrix([1,0]+[t**(2**j) for j in range(1,k)])
        W=v*v.T;W[1,1]+=t*t
        assert W[k,k]==t**(2**k)
        assert W[0,1]==0
        for i in range(1,k):assert W[i,i]==W[0,i+1]
    return {'arrow_sum_of_squares':'exact rational congruence identity verified',
            'cascade_equations':'exact symbolic identities verified for k=1,...,6; general proof in 06'}


def main():
    rng=np.random.default_rng(61392026);tests=[]
    for m in [1,2,3]:
        A=np.stack([np.eye(m),np.ones((m,m))]);z=np.array([1.,0.])
        for rank in sorted(set([0,1,m])):
            R=rng.normal(size=(m,rank));X=R@R.T
            tests.append(test_case(A,z,X,f'm={m},rank={rank}',rng))
    A,z,bd,X=cascade(2);tests.append(test_case(A,z,X,'depth-two-rational-source',rng))
    out={'scope':'Independent numerical and exact rational diagnostics; universal proofs are in 06--08.',
         'seed':61392026,'exact':exact_checks(),'construction':tests,'choi':choi_tests(rng),
         'ancilla':ancilla_test(rng),'sharp_leakage_curves':leakage_tests()}
    Path(__file__).with_name('STRENGTHENING_RESULTS.json').write_text(json.dumps(out,indent=2))
    print(json.dumps({'passed':True,'construction_cases':len(tests),'choi_orders':[1,2,3,4],
                      'ancilla':out['ancilla'],'curve_cases':len(out['sharp_leakage_curves'])},indent=2))
if __name__=='__main__':main()
