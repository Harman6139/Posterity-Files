"""Numerical diagnostics for the exact factored-column dense anchored compiler.
The manuscript gives rational LDL arithmetic and rational grid comparisons.
This implementation uses floating point only as an independent sanity check.
"""
from __future__ import annotations
import numpy as np
from strict_shield import build as build_core


def build(A: np.ndarray, z: np.ndarray, bdata: np.ndarray):
    core=build_core(A,z,bdata)
    d=core['d']; m=core['m']; M0=core['M0']; eps=core['eps']
    G0=core['G']; M=G0.shape[1]
    # Rational LDL column factors, represented numerically here.
    s0=np.r_[np.full(M0,eps),np.diag(core['completion'])**2]
    uu0=G0/np.sqrt(s0)[None,:]
    # Split the shield completion, and retain one untouched duplicate.
    ss=np.r_[s0[:-1],s0[-1]/2,s0[-1]/2]
    uu=np.column_stack([uu0[:,:-1],uu0[:,-1],uu0[:,-1]])
    G=uu*np.sqrt(ss)[None,:]
    c=np.r_[core['c'][:-1],core['c'][-1]/2,core['c'][-1]/2]
    Mb=G.shape[1]; h=.1; v0=.01
    a2=(5+3*h*h)/7; b2=(1-5*h*h)/7
    aa=np.sqrt(a2); bb=np.sqrt(b2)
    rr=h*(uu*ss).sum(axis=1); t0=2*(Mb+1)
    factors=[]; columns=[]; zratio=[]; weights=[]
    for i in range(d):
        ei=np.eye(d)[:,i]
        for f,q,w in ((a2,(2*rr[i]+t0)/(3*a2),-1),
                      (b2,-(5*rr[i]+4*t0)/(3*b2),2),
                      (b2,t0/b2,3)):
            factors.append(f); columns.append(ei); zratio.append(q); weights.append(w)
    for j in range(Mb):
        factors.append(ss[j]); columns.append(h*uu[:,j]); zratio.append(1.); weights.append(4)
    fac=np.asarray(factors); old=np.column_stack(columns)
    zr=np.asarray(zratio); zz=np.sqrt(fac)*zr; ww=np.asarray(weights,float)
    A0=old*np.sqrt(fac)[None,:]; nz=len(fac)
    Z=float(zz@zz); qZ=float((ww*zz)@zz)
    eta0=1.
    while (2*eta0)**2*Z>1/1000 or 2*eta0>v0/100:
        eta0/=2
    J1=nz*(nz-1)//2+1
    beta=eps*eta0*eta0/(2*J1)
    upper=np.triu_indices(nz,1)
    for trial in range(J1):
        eta=eta0*(1+trial/(J1-1))
        gram=A0.T@A0+eta*eta*np.outer(zz,zz)
        if np.min(np.abs(gram[upper]))>=beta:
            break
    else:
        raise RuntimeError('First finite grid failed in floating point.')
    sa=ss[-2]; v2=sa*v0*v0
    x2=(2+eta*eta*(qZ-2*Z)+2*v2)/3
    y2=(1-eta*eta*(Z+qZ)-5*v2)/3
    uold=np.vstack([old,eta*zr])
    uout=np.column_stack([uold,np.r_[np.zeros(d),1.],np.r_[np.zeros(d),1.],np.r_[np.zeros(d),v0]])
    sf=np.r_[fac,x2,y2,sa]
    F=uout*np.sqrt(sf)[None,:]
    weights=np.r_[ww,-1,2,4]
    N=F.shape[1]; P=F.T@F; R=2*P-np.eye(N); Q=np.eye(N)-P
    ia=3*d+Mb-2; duplicate=ia+1; ib=N-1
    etaR=min(2*beta,eta0*eps*v0/2,v0*v0/8,.1)
    etav=min(eta0*eps,v0/2,.5)
    xi=min(etaR,etav); J2=12*N+5; step=1/(10*(J2-1)); threshold=xi*step*step/100
    for j in range(J2):
        t=.1+j*step; co=(1-t*t)/(1+t*t); si=2*t/(1+t*t)
        O=np.eye(N); O[ia,ia]=O[ib,ib]=co; O[ib,ia]=si; O[ia,ib]=-si
        U=R@O
        nu=F[-1]; nu2=O.T@nu
        row4=np.sum(U**4,axis=1); col4=np.sum(U**4,axis=0)
        mismatch=np.max(np.abs(np.sort(row4)-np.sort(col4)))
        if np.min(np.abs(U[:,[ia,ib]]))>=threshold/2 and min(abs(nu2[ia]),abs(nu2[ib]))>=threshold/2 and mismatch>1e-15:
            break
    else:
        raise RuntimeError('Nonreflection test needs exact rational arithmetic for this instance.')
    V=np.c_[core['V0'],np.zeros(m)]@F
    yfirst=[]
    for i in range(d):
        for jloc in range(3):
            j=3*i+jloc
            yfirst.append(fac[j]*core['t'][i]+eta*eta*zz[j]*zz[j])
    yfirst.extend(h*h*c+eta*eta*ss)
    yfirst.extend([x2,y2,v2]); yfirst=np.asarray(yfirst)
    ysecond=yfirst.copy(); cab=eta*sa*v0
    ysecond[ia]=co*co*yfirst[ia]+si*si*yfirst[ib]+2*co*si*cab
    ysecond[ib]=si*si*yfirst[ia]+co*co*yfirst[ib]-2*co*si*cab
    target=np.r_[yfirst,ysecond]
    def encode(X):
        _,Zinner=core['encode'](X)
        Za=np.zeros((d+1,d+1));Za[:d,:d]=Zinner;Za[d,d]=1
        return F.T@Za@F,Za
    def measure(Y):
        return np.r_[np.diag(Y),np.diag(U.T@Y@U)]
    # Exact linear extraction formulas; no singular-value inversion.
    es=np.zeros(N); es[nz]=1/x2
    cross=np.zeros((d,N))
    for i in range(d):
        j2,j3=3*i+1,3*i+2
        denom=2*bb*eta*(zz[j3]-zz[j2])
        cross[i,j3]+=1/denom;cross[i,j2]-=1/denom
        cross[i]-=eta*(zz[j3]+zz[j2])/(2*bb)*es
    recover=np.zeros((Mb,N))
    for j in range(Mb):
        idx=3*d+j
        if idx==ia:idx=duplicate
        recover[j,idx]=1/h**2
        recover[j]-=(2*eta*np.sqrt(ss[j])/h)*(G[:,j]@cross)
        recover[j]-=(eta**2*ss[j]/h**2)*es
    Robs=core['R0']@recover[:M0]/eps
    stress=np.diag(weights)+U@np.diag(weights)@U.T
    kappa=np.linalg.norm(weights)/np.sqrt(2)
    CG=100*(2+np.sqrt(d)+4*np.sqrt(Mb))
    Kr=(np.linalg.norm(core['R0'],2)/eps)*CG*(1/np.sqrt(2)+kappa)
    checks={
        'Mbar':Mb,'N':N,'predicted_N':11*m*m+8*m+14+2*len(A),
        'coisometry':float(np.linalg.norm(F@F.T-np.eye(d+1))),
        'signed_isotropy':float(np.linalg.norm((F*weights)@F.T)),
        'orthogonality':float(np.linalg.norm(U@U.T-np.eye(N))),
        'decoder_coisometry':float(np.linalg.norm(V@V.T-np.eye(m))),
        'stress_identity':float(np.linalg.norm(stress-2*Q@np.diag(weights)@Q)),
        'stress_gap_error':float(np.linalg.eigvalsh(stress-2*Q)[0]),
        'minimum_overlap':float(np.min(np.abs(U))),
        'minimum_anchor_first':float(np.min(np.abs(nu))),
        'minimum_anchor_second':float(np.min(np.abs(nu2))),
        'fourth_moment_multiset_gap':float(mismatch),
        'minimum_target':float(np.min(target)),
        'target_stress':float(abs(np.r_[weights,weights]@target)),
        'extraction_target':float(np.linalg.norm(Robs@yfirst-bdata)),
        'extraction_operator':max(float(np.linalg.norm((F*Robs[i])@F.T-np.block([[core['V0'].T@A[i]@core['V0'],np.zeros((d,1))],[np.zeros((1,d+1))]]))) for i in range(len(A))),
        'rotated_extraction_coefficients':float(np.linalg.norm(Robs[:,[ia,ib]])),
        'eta':eta,'rotation_cayley_parameter':t,'global_source_bound':Kr,
    }
    return locals()
