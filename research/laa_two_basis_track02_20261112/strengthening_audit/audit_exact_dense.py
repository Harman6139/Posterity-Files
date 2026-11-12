"""Exact Fraction certificate for the dense nonreflection compiler at m=p=1.
No floating point and no comparison of unrelated algebraic radicals is used.
The universal theorem is proved in 08, not inferred from this instance.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib,json

def dot(a,b):return sum((x*y for x,y in zip(a,b)),Q(0))
def outer_add(M,u,w):
    for i in range(len(u)):
        for j in range(len(u)):M[i][j]+=w*u[i]*u[j]
def main():
    d=5;eps=Q(1,40);h=Q(1,10);v0=Q(1,100)
    eye=[[Q(int(i==j)) for i in range(d)] for j in range(d)]
    raw=eye.copy()
    for sg in [1,-1]:
        for t in [1,-1]:raw.append([Q(t),Q(-sg*t),Q(1),Q(sg),Q(0)])
    raw.extend([[Q(0),Q(0),Q(1),Q(1),Q(0)], [Q(0),Q(0),Q(1),Q(-1),Q(0)]])
    assert len(raw)==11
    comp=[1-eps*5,1-eps*5,1-eps*7,1-eps*7,1-eps]
    sf=[eps]*len(raw)+comp[:-1]+[comp[-1]/2]*2
    uu=raw+eye[:-1]+[eye[-1],eye[-1]]
    Mb=len(sf);assert Mb==17
    GG=[[Q(0) for _ in range(d)] for _ in range(d)]
    for s,u in zip(sf,uu):outer_add(GG,u,s)
    assert GG==eye
    rr=[h*sum(sf[j]*uu[j][i] for j in range(Mb)) for i in range(d)]
    t0=2*(Mb+1);aa=(5+3*h*h)/7;bb=(1-5*h*h)/7
    factors=[];old=[];zr=[];weights=[]
    for i in range(d):
        for f,z,w in [(aa,(2*rr[i]+t0)/(3*aa),-1),(bb,-(5*rr[i]+4*t0)/(3*bb),2),(bb,Q(t0)/bb,3)]:
            factors.append(f);old.append(eye[i]);zr.append(z);weights.append(w)
    for s,u in zip(sf,uu):factors.append(s);old.append([h*x for x in u]);zr.append(Q(1));weights.append(4)
    nz=len(factors);Z=sum(s*z*z for s,z in zip(factors,zr));qZ=sum(w*s*z*z for w,s,z in zip(weights,factors,zr))
    eta0=Q(1)
    while (2*eta0)**2*Z>Q(1,1000) or 2*eta0>v0/100:eta0/=2
    J1=nz*(nz-1)//2+1;beta=eps*eta0*eta0/(2*J1)
    for step in range(J1):
        eta=eta0*(1+Q(step,J1-1))
        if all(factors[i]*factors[j]*(dot(old[i],old[j])+eta*eta*zr[i]*zr[j])**2>=beta**2 for i in range(nz) for j in range(i)):
            break
    else:raise AssertionError('Exact first grid failed')
    sa=sf[-2];v2=sa*v0*v0
    x2=(2+eta*eta*(qZ-2*Z)+2*v2)/3;y2=(1-eta*eta*(Z+qZ)-5*v2)/3
    u=[a+[eta*z] for a,z in zip(old,zr)]
    ec=[Q(0)]*d+[Q(1)]
    u +=[ec,ec,[v0*x for x in ec]]
    factors +=[x2,y2,sa];weights +=[-1,2,4]
    N=len(u);D=d+1;assert N==35
    tight=[[Q(0) for _ in range(D)] for _ in range(D)];signed=[[Q(0) for _ in range(D)] for _ in range(D)]
    for s,w,col in zip(factors,weights,u):outer_add(tight,col,s);outer_add(signed,col,w*s)
    assert tight==[[Q(int(i==j)) for j in range(D)] for i in range(D)]
    assert all(x==0 for row in signed for x in row)
    # R_ij = sqrt(factors[i]*factors[j]) * rat[i][j].
    rat=[[2*dot(u[i],u[j])-(1/factors[i] if i==j else 0) for j in range(N)] for i in range(N)]
    assert all(x!=0 for row in rat for x in row)
    ia=3*d+Mb-2;ib=N-1
    etaR=min(2*beta,eta0*eps*v0/2,v0*v0/8,Q(1,10))
    etanu=min(eta0*eps,v0/2,Q(1,2));xi=min(etaR,etanu)
    J2=12*N+5;dt=Q(1,10*(J2-1));bound=xi*dt*dt/200
    for j in range(J2):
        t=Q(1,10)+j*dt;c=(1-t*t)/(1+t*t);ss=2*t/(1+t*t)
        R=[row.copy() for row in rat]
        for i in range(N):
            R[i][ia]=c*rat[i][ia]+ss*rat[i][ib]
            R[i][ib]=-ss*rat[i][ia]+c*rat[i][ib]
        anchor1=factors[ia]*(c*u[ia][-1]+ss*u[ib][-1])**2
        anchor2=factors[ib]*(-ss*u[ia][-1]+c*u[ib][-1])**2
        if min(anchor1,anchor2)<bound**2:continue
        if any(factors[i]*factors[k]*R[i][k]**2<bound**2 for i in range(N) for k in [ia,ib]):continue
        fourth=[[factors[i]**2*factors[k]**2*R[i][k]**4 for k in range(N)] for i in range(N)]
        rows=[sum(r) for r in fourth];cols=[sum(fourth[i][k] for i in range(N)) for k in range(N)]
        if sorted(rows)!=sorted(cols):break
    else:raise AssertionError('Exact second grid failed')
    # A nonzero power-sum difference is a short invariant certificate.
    for power in range(2,N+1):
        cert=sum(x**power for x in rows)-sum(x**power for x in cols)
        if cert:break
    assert cert!=0
    out={'exact_arithmetic':'Python Fraction, no floating point','m':1,'p':1,'N':N,
         'parseval_identity':True,'signed_isotropy_identity':True,
         'all_reflection_entries_nonzero':True,'all_final_entries_nonzero':all(x!=0 for row in R for x in row),
         'matched_rotated_column_factors':str(sa),'eta':str(eta),'rotation_parameter':str(t),
         'positive_uniform_margin':str(bound),'nonreflection_power_sum_order':power,
         'nonreflection_certificate_nonzero':True,'certificate_sign':1 if cert>0 else -1,
         'certificate_numerator_bits':cert.numerator.bit_length(),'certificate_denominator_bits':cert.denominator.bit_length(),
         'certificate_sha256':hashlib.sha256(str(cert).encode()).hexdigest(),
         'scope':'One exact independent test. All-dimension proofs are in milestone 08.'}
    Path(__file__).with_name('EXACT_DENSE_RESULTS.json').write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
