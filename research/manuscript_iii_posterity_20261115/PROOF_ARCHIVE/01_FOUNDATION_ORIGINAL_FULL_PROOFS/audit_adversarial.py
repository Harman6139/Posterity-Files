"""Adversarial checks of the proved construction; numerical diagnostics, not a proof."""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
from audit_quadratic_quotient import build, exact_raw_identity


def symbasis(n):
    out=[]
    for i in range(n):
        for j in range(i,n):
            T=np.zeros((n,n)); T[i,j]=T[j,i]=1.0
            if i!=j: T/=np.sqrt(2)
            out.append(T)
    return np.asarray(out)


def check_case(A,z,b,X,label,rng):
    o=build(A,z,b); m=A.shape[1]; N=o['N']
    target=np.r_[o['y0'],o['y0']]
    K=3*np.sqrt(2)*o['L']*(1+np.sqrt(o['d']+4*o['M']))*np.sqrt(9*o['S_A']/16+len(A)/8)
    for key in ('raw_frame_formula','parseval','orthogonal','decoder_coisometry','source_operator_identity'):
        assert o['checks'][key]<1e-8, (label,key,o['checks'][key])
    assert o['checks']['completion_gap']>=.5-1e-12
    assert o['checks']['stress_gap_min_eigenvalue']>=-1e-10
    assert o['checks']['source_data_identity']<1e-8*(1+np.linalg.norm(b))
    assert abs(o['yd']@o['y0'])<1e-9*(1+np.linalg.norm(o['y0']))
    C=rng.normal(size=(m,m)); C=(C+C.T)/2
    Ct=o['V'].T@C@o['V']
    assert abs(np.linalg.norm(Ct)-np.linalg.norm(C))<1e-10*(1+np.linalg.norm(C))
    ratios=[]; cost_errors=[]
    for rank in sorted(set((1,min(5,N),N))):
        B=rng.normal(size=(N,rank)); Y=B@B.T
        delta=np.linalg.norm(o['measure'](Y)-target)
        Xd=o['V']@Y@o['V'].T
        sr=np.linalg.norm(np.einsum('aij,ij->a',A,Xd)-b)
        assert sr<=K*delta+1e-8
        ratios.append(sr/max(delta,1e-300))
        cost_errors.append(abs(np.sum(Ct*Y)-np.sum(C*Xd)))
    cert_slack=[]; cert_pairing=[]
    w=np.r_[o['yd'],o['yd']]
    for i in range(len(A)):
        ell=np.zeros(N); ell[o['d']:o['d']+o['M0']]=3*o['R0'][i]/o['eps']
        Fsrc=o['V'].T@A[i]@o['V']
        beta=np.max(np.abs(ell))/2
        for sign in (1.,-1.):
            lam=sign*np.r_[ell/2,ell/2]+beta*w
            slack=np.diag(lam[:N])+o['U']@np.diag(lam[N:])@o['U'].T-sign*Fsrc
            scale=1+np.linalg.norm(slack,2)
            mineig=float(np.linalg.eigvalsh(slack)[0]/scale)
            pairing=abs(lam@target-sign*b[i])/(1+np.linalg.norm(lam)*np.linalg.norm(target))
            assert mineig>=-1e-10,(label,'dual slack',mineig)
            assert pairing<1e-10,(label,'dual pairing',pairing)
            cert_slack.append(mineig); cert_pairing.append(pairing)
    rec={'label':label,'m':m,'p':len(A),'N':N,'K_proved':float(K),
         'max_tested_residual_ratio':float(max(ratios)),
         'max_cost_error':float(max(cost_errors)),
         'min_relative_certificate_eigenvalue':min(cert_slack),
         'max_relative_certificate_pairing_error':max(cert_pairing)}
    if X is not None:
        E,J=o['encode'](X)
        rec.update({'section_error':float(np.linalg.norm(o['V']@E@o['V'].T-X)),
                    'relative_forward_data_error':float(np.linalg.norm(o['measure'](E)-target)/(1+np.linalg.norm(target))),
                    'inner_min_eigenvalue':float(np.linalg.eigvalsh(J)[0])})
        assert rec['section_error']<1e-8*(1+np.linalg.norm(X))
        assert rec['relative_forward_data_error']<1e-10
        assert rec['inner_min_eigenvalue']>=-1e-8*(1+np.linalg.norm(J))
    return rec,o


def main():
    rng=np.random.default_rng(6139)
    records=[]
    # Historical 62: the 4x4 rational fibre cannot be an unconstrained spectraplex image.
    A=np.zeros((8,4,4))
    for a,(i,j) in enumerate(((0,2),(0,3),(1,2),(1,3),(2,3))):
        A[a,i,j]=A[a,j,i]=.5
    A[5]=np.diag([1.,-1.,-2.,0.])
    A[6,0,1]=A[6,1,0]=.5; A[6,3,3]=-1
    A[7]=np.eye(4)
    z=np.r_[np.zeros(7),1.]; b=np.r_[np.zeros(7),6.]
    X=np.array([[3.,1,0,0],[1,1,0,0],[0,0,1,0],[0,0,0,1]])
    rec,o=check_case(A,z,b,X,'historical_62_nonspectrahedral_dual',rng)
    # Find a genuine non-section feasible point using an invisible auxiliary covariance.
    basis=symbasis(o['k']); QG=o['G'][2*4+1:]
    an=np.einsum('ij,aik,kj->ja',QG,basis,QG)
    _,sing,Vh=np.linalg.svd(an,full_matrices=True)
    rank=int(np.sum(sing>1e-10))
    assert rank<len(basis)
    auxT=np.einsum('a,aij->ij',Vh[-1],basis)
    T=np.zeros((o['d'],o['d'])); T[9:,9:]=auxT
    E,J=o['encode'](X)
    eta=np.linalg.eigvalsh(J)[0]/(4*np.linalg.norm(T,2))
    Z2=J+eta*T; Y2=o['F'].T@Z2@o['F']
    target=np.r_[o['y0'],o['y0']]
    slackdata=np.linalg.norm(o['measure'](Y2)-target)/(1+np.linalg.norm(target))
    decodererror=np.linalg.norm(o['V']@Y2@o['V'].T-X)
    assert slackdata<1e-10 and decodererror<1e-8
    assert np.linalg.eigvalsh(Z2)[0]>0 and np.linalg.norm(Y2-E)>1e-4
    rec['non_section_witness']={'auxiliary_constraint_rank':rank,
        'auxiliary_kernel_dimension':len(basis)-rank,'perturbation_norm':float(np.linalg.norm(Y2-E)),
        'relative_data_error':float(slackdata),'decoder_error':float(decodererror),
        'inner_min_eigenvalue':float(np.linalg.eigvalsh(Z2)[0])}
    records.append(rec)
    # Trace-only source, redundant/zero equations, pure/zero inputs and infeasible data.
    A2=np.array([np.eye(2),np.zeros((2,2)),np.eye(2),[[0.,1.],[1.,0.]]])
    z2=np.array([1.,0.,0.,0.])
    for label,b2,X2 in [
        ('rank_one_redundant_zero_rows',np.array([1.,0.,1.,0.]),np.diag([1.,0.])),
        ('zero_fibre_redundant_rows',np.zeros(4),np.zeros((2,2))),
        ('infeasible_duplicate_equation',np.array([1.,0.,2.,0.]),None),
        ('infeasible_zero_equation',np.array([1.,1.,1.,0.]),None),
        ('infeasible_negative_trace',np.array([-1.,0.,-1.,0.]),None)]:
        rec,_=check_case(A2,z2,b2,X2,label,rng);records.append(rec)
    rec,_=check_case(np.ones((1,1,1)),np.ones(1),np.ones(1),np.ones((1,1)),
                     'minimal_m1_p1_complement_singular',rng);records.append(rec)
    # Non-scalar trace certificate and mixed-sign coefficients.
    A3=np.array([[[2.,.5],[.5,1.]],[[1.,-1.],[-1.,-2.]],[[0.,2.],[2.,0.]]])
    z3=np.array([1.,0.,0.]); X3=np.array([[2.,1.],[1.,.5]])
    rec,_=check_case(A3,z3,np.einsum('aij,ij->a',A3,X3),X3,
                     'nonscalar_trace_control_rank_one',rng);records.append(rec)
    result={'seed':6139,'exact_raw_identity':exact_raw_identity(),'cases':records,
       'scope':'All assertions passed. Floating-point cases are diagnostics; the algebraic manuscript is the proof.'}
    Path(__file__).with_name('ADVERSARIAL_RESULTS.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
