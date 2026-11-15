#!/usr/bin/env python3
"""Independent exact verifier: no generator imports, determinant-based ray checks.

Checks explicit arithmetic and a complete short branching prefix. It does not
simulate the exponentially long prefix or replace the analytic induction.
"""
from __future__ import annotations
from fractions import Fraction as Q
from itertools import combinations, product
from math import factorial, gcd, lcm
from pathlib import Path
import copy, hashlib, json, sys
if hasattr(sys,'set_int_max_str_digits'): sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[1]
def require(test,msg):
    if not test: raise AssertionError(msg)
def mat(x): return [[Q(v) for v in row] for row in x]
def vector(x): return [Q(v) for v in x]
def trace(A): return sum(A[i][i] for i in range(len(A)))
def ip(A,B): return sum(A[i][j]*B[i][j] for i in range(len(A)) for j in range(len(A)))
def bil(A,x): return sum(A[i][j]*x[i]*x[j] for i in range(len(x)) for j in range(len(x)))
def scalar(a,b): return sum(x*y for x,y in zip(a,b))
def determinant(A):
    """Bareiss elimination after a positive common-denominator clearing."""
    n=len(A)
    if n==0:return Q(1)
    den=lcm(*(Q(x).denominator for row in A for x in row))
    a=[[int(Q(x)*den) for x in row] for row in A]
    prev=1; sign=1
    for k in range(n-1):
        p=next((i for i in range(k,n) if a[i][k]),None)
        if p is None:return Q(0)
        if p!=k:a[k],a[p]=a[p],a[k];sign=-sign
        piv=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                value=a[i][j]*piv-a[i][k]*a[k][j]
                require(value%prev==0,'Bareiss exact division')
                a[i][j]=value//prev
            a[i][k]=0
        prev=piv
    return Q(sign*a[-1][-1],den**n)
def full_column_rank(rows,k):
    return any(determinant([rows[i] for i in I]) for I in combinations(range(len(rows)),k))
def canonical_T(n):
    return [[Q(1) if i==j else (Q(-1,2) if abs(i-j)==1 else Q(0)) for j in range(n)] for i in range(n)]
def primitive(v):
    den=lcm(*(Q(x).denominator for x in v)); z=[int(Q(x)*den) for x in v]; g=gcd(*z)
    return tuple(x//g for x in z)
def enumerate_face_rays(active):
    r=len(active[0]); rows=[[2*u for u in v]+[1] for v in active]; rays=set()
    for ids in combinations(range(len(rows)),r):
        A=[rows[i] for i in ids]
        cof=[(-1)**j*determinant([[row[k] for k in range(r+1) if k!=j] for row in A]) for j in range(r+1)]
        if not any(cof):continue
        v=primitive(cof)
        for sign in (1,-1):
            ray=tuple(sign*x for x in v)
            if all(scalar(row,ray)>=0 for row in rows):rays.add(ray)
    return rays

def verify_family(f):
    n=int(f['n']);r=n-1;m=int(f['m']); d=n*(n+1)//2
    Y=2*(2*n)**r;U=2*Y*n*n*(m+1);E=factorial(d-1)*(2*U*U)**(d-1);N=20000*n**3*E**2
    for key,val in [('r',r),('d',d),('q',2*n),('Y',Y),('U',U),('E',E),('N',N),('N_bits',N.bit_length()),('guaranteed_pivots',m)]:
        require(int(f[key])==val,'parameter '+key)
    eps=Q(1,100*n**3);rho=Q(1,1600*n**4*N*N)
    require(Q(f['epsilon'])==eps and Q(f['radius'])==rho,'epsilon/radius')
    B=mat(f['B']);A=mat(f['A']);W=mat(f['W']);scale=[N]*r+[1]
    D=[Q(1)]*n;D[1]=D[2]=Q(8,5)
    cycle=[0,1,2,3,n-1];edges={frozenset((cycle[i],cycle[(i+1)%5])) for i in range(5)}
    require(all(sum(frozenset(p) in edges for p in combinations(S,2))<3 for S in combinations(cycle,3)),'triangle-free Horn certificate')
    C=[[Q(0) for _ in range(n)] for _ in range(n)]
    for left in range(n):
        for right in range(left,n):
            for i in range(left,right+1):
                for j in range(left,right+1): C[i][j]+=1
    expected=[[D[i]*D[j]*(Q(i==j)+Q(3,5)*int(frozenset((i,j)) in edges))+eps*C[i][j] for j in range(n)] for i in range(n)]
    require(B==expected,'target B reconstruction')
    require(min(x for row in B for x in row)>=eps,'strict entry reserve')
    require(ip(B,B)<=9*n*n and trace(B)<=3*n,'norm/trace bound')
    require(all((x*500*n**3).denominator==1 for row in B for x in row),'common denominator')
    for k in range(1,n+1):
        shift=[[B[i][j]-Q(i==j,40) for j in range(k)] for i in range(k)]
        require(determinant(shift)>0,'positive definite margin')
    require(A==[[scale[i]*B[i][j]*scale[j]/(4*n*N*N) for j in range(n)] for i in range(n)],'normalization')
    H=[[Q((i in cycle) and (j in cycle))-2*int(frozenset((i,j)) in edges) for j in range(n)] for i in range(n)]
    W0=[[H[i][j]/(D[i]*D[j]) for j in range(n)] for i in range(n)]
    require(ip(W0,W0)<=25 and ip(W0,B)<=Q(-19,20),'Horn separator')
    require(W==[[W0[i][j]/(scale[i]*scale[j])+Q(i==j,20*n*N*N) for j in range(n)] for i in range(n)],'strict separator reconstruction')
    require(ip(W,W)<=36 and ip(W,A)<=Q(-1,5*n*N*N),'strict separator bounds')
    require(ip(W,A)+6*rho<=Q(-1,6*n*N*N),'robust negative pairing')
    require(Q(1,160*n*N*N)>rho and Q(3,4)+rho<=1,'robust PSD/norm')
    require(min(x for row in A for x in row)>=4*rho,'robust positive entries')
    c=[B[i][-1] for i in range(r)];a=B[-1][-1]
    require(0<a<2 and all(x>0 for x in c) and sum(c)<2,'cross-column bounds')
    weights=f['interval_weights'];require(len(weights)==r*(r+1)//2,'interval count')
    seen=set();rec=[[Q(0) for _ in range(r)] for _ in range(r)]
    for left,right,w in weights:
        w=Q(w);require(0<=left<=right<r and (left,right) not in seen and w>=eps,'interval reserve')
        seen.add((left,right))
        for i in range(left,right+1):
            for j in range(left,right+1):rec[i][j]+=w
    require(rec==[row[:r] for row in B[:r]],'top Gram identity')
    require(ip(rec,canonical_T(r))>=1,'leading pairing')
    require(Q(N*N,500*n**3)-7*N*E>=Q(N*N,1000*n**3),'all-ray confinement inequality')
    M=m+1
    require(N*N-12*N*M-Q(n*n*M*M,40)>=Q(N*N,4),'no vertex separator')
    require(-7*N*E+Q(N*N,2*E)>0,'identity correction obstruction')
    return n,m,N,B

def verify_canonical(record, fam):
    n=int(record['n']);B=fam[3];N=fam[2];sn=[N]*(n-1)+[1];T=canonical_T(n)
    intervals=[(a,b) for a in range(n) for b in range(a,n)];pairs=list(combinations(range(n),2))
    upp=[(i,j) for i in range(n) for j in range(i,n)];normals=[];vs=[]
    for a,b in intervals:
        v=[int(a<=i<=b) for i in range(n)];vs.append(v)
        require(bil(T,v)==1,'canonical minimum')
        normals.append([v[i]*v[j]*(1 if i==j else 2) for i,j in upp])
    require(determinant(normals)!=0,'canonical perfection')
    require(len(record['rays'])==len(intervals),'canonical all rays count')
    negative=0
    for entry,iv in zip(record['rays'],intervals):
        require(tuple(entry['interval'])==iv,'ray interval indexing')
        R=mat(entry['ray']);vals=[bil(R,v) for v in vs];k=intervals.index(iv)
        require(vals[k]>0 and all(v==0 for j,v in enumerate(vals) if j!=k),'exact dual extreme ray')
        cost=sum(sn[i]*B[i][j]*sn[j]*R[i][j] for i in range(n) for j in range(n))
        require(bool(entry['improving'])==(cost<0),'ray objective sign')
        if cost<0:
            negative+=1;require(all(R[i][j]==0 for i in range(n-1) for j in range(n-1)),'initial face confinement')
    require(negative>=1,'at least one improving canonical ray')
    return len(intervals),negative

def verify_prefix(data,fam):
    n=int(data['n']);r=n-1;require(r==4,'short-prefix validation dimension')
    T=canonical_T(r);B=fam[3];N=fam[2];c0=[B[i][-1] for i in range(r)];a0=B[-1][-1]
    pts=data['vertices'];require(vector(pts[0]['b'])==[Q(0),Q(0),Q(0),Q(-1,2)] and Q(pts[0]['c'])==1,'canonical prefix initialization')
    finite_checks=0;all_rays=[]
    for p in pts:
        b=vector(p['b']);c=Q(p['c']);z=vector(p['z']);ell=vector(p['ell']);gamma=c-bil(T,z)
        require(ell==[b[i]+scalar(T[i],z) for i in range(r)],'KKT residual identity')
        require(min(z)>=0 and min(ell)>=0 and all(x*y==0 for x,y in zip(z,ell)),'KKT optimality')
        require(gamma==Q(p['gamma']) and gamma>Q(1,4),'all denominators y>=2 strictly excluded')
        # If u is outside this box then (u-z)^T T (u-z)>1,
        # since each diagonal entry of T^{-1} is below 4.
        boxes=[range(max(0,t.numerator//t.denominator-2),-(-t.numerator//t.denominator)+3) for t in z]
        active=[];count=0
        for u in product(*boxes):
            value=bil(T,u)+2*scalar(b,u)+c
            require(value>=1,'all potentially violating y=1 vectors')
            if value==1:active.append(list(u))
            count+=1
        finite_checks+=count
        require(active==p['active'] and count==p['finite_values_checked'],'complete active set')
        rows=[[2*x for x in u]+[1] for u in active]
        require(full_column_rank(rows,r+1),'vertex rank')
        rays=enumerate_face_rays(active);all_rays.append(rays)
        require(rays=={tuple(v) for v in p['all_face_rays']},'complete relative tangent ray enumeration')
        improving={v for v in rays if 2*N*scalar(c0,v[:-1])+a0*v[-1]<0}
        require(improving=={tuple(v) for v in p['improving_face_rays']},'all improving relative rays')
        require(improving,'improving relative ray exists')
    out={i:set() for i in range(len(pts))};shared=0
    for edge in data['edges']:
        i,j=int(edge['start']),int(edge['end']);v=tuple(edge['direction']);t=Q(edge['length'])
        require(v in all_rays[i] and v in {tuple(w) for w in pts[i]['improving_face_rays']} and t>0,'valid edge direction')
        b,c=vector(pts[i]['b']),Q(pts[i]['c']);bb,cc=vector(pts[j]['b']),Q(pts[j]['c'])
        require(bb==[b[k]+t*v[k] for k in range(r)] and cc==c+t*v[-1],'endpoint identity')
        require(max(abs(x-y) for x,y in zip(b,bb))<=Q(5,2),'universal movement bound')
        common={tuple(u) for u in pts[i]['active']} & {tuple(u) for u in pts[j]['active']}
        require(common,'common active constraint')
        shared+=len(common);out[i].add(v)
    for i,level in enumerate(data['levels']):
        if level<int(data['depth']):
            require(out[i]=={tuple(v) for v in pts[i]['improving_face_rays']},'every improving branch included')
    return dict(vertices=len(pts),edges=len(data['edges']),finite_lattice_checks=finite_checks,shared_active_incidents=shared)

def verify(payload):
    require(payload['kind']=='ordinary_CP_canonical_all_rules','certificate kind')
    families=[verify_family(f) for f in payload['families']]
    canonical=[]
    for rec in payload['canonical']:
        fam=next(f for f in families if f[0]==int(rec['n']) and (f[1]==8 if f[0]==5 else f[1]==7))
        canonical.append(verify_canonical(rec,fam))
    fam=next(f for f in families if f[0]==5 and f[1]==8)
    prefix=verify_prefix(payload['branching_prefix'],fam)
    return dict(families=len(families),canonical_extreme_rays=sum(x[0] for x in canonical),
                improving_initial_ray_counts=[x[1] for x in canonical],branching_prefix=prefix)

def main():
    path=ROOT/'certificates/exact_certificates.json'; raw=path.read_bytes(); payload=json.loads(raw)
    result=verify(payload); rejected=[]
    mutations=[('scale parameter',lambda p:p['families'][0].__setitem__('N','7')),
               ('target entry',lambda p:p['families'][0]['B'][0].__setitem__(0,'-1')),
               ('separator',lambda p:p['families'][0]['W'][0].__setitem__(0,'0')),
               ('interval weight',lambda p:p['families'][0]['interval_weights'][0].__setitem__(2,'0')),
               ('canonical ray',lambda p:p['canonical'][0]['rays'][0]['ray'][0].__setitem__(0,'-1')),
               ('edge length',lambda p:p['branching_prefix']['edges'][0].__setitem__('length','0')),
               ('missing improving branch',lambda p:p['branching_prefix']['vertices'][0].__setitem__('improving_face_rays',[]))]
    for label,change in mutations:
        bad=copy.deepcopy(payload);change(bad)
        try:verify(bad)
        except (AssertionError,ValueError,ZeroDivisionError):rejected.append(label)
        else:raise AssertionError('corrupted certificate accepted: '+label)
    result.update(status='PASS',sha256=hashlib.sha256(raw).hexdigest(),deliberate_corruptions_rejected=rejected,
                  largest_forced_prefix=str(max(int(x['m']) for x in payload['families'])),
                  scope='Separate exact verifier; finite tests and short complete branching prefix. No generator imports, no long simulation, no human/formal proof certification.')
    report=ROOT/'certificates/verification_report.json';report.write_text(json.dumps(result,indent=2)+'\n');print(report.read_text())
if __name__=='__main__':main()
