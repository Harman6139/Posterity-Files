#!/usr/bin/env python3
"""Independent exact checker. Does not import the certificate generator.
The finite examples check identities and interfaces, not universal proof claims.
"""
from fractions import Fraction
from math import isqrt
from pathlib import Path
from copy import deepcopy
import json, hashlib
Q=Fraction
ROOT=Path(__file__).resolve().parents[1]

def matrix(rows): return [[Q(v) for v in row] for row in rows]
def check(condition, message):
    if not condition: raise ValueError(message)
def upper(A): return [A[i][j] for i in range(len(A)) for j in range(i,len(A))]
def quadratic(A,x): return sum(A[i][j]*x[i]*x[j] for i in range(len(x)) for j in range(len(x)))
def rank(rows):
    a=[list(map(Q,row)) for row in rows]; r=0
    if not a:return 0
    for j in range(len(a[0])):
        pivot=next((i for i in range(r,len(a)) if a[i][j]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        for i in range(r+1,len(a)):
            if a[i][j]:
                p,q=a[r][j],a[i][j]
                a[i]=[p*x-q*y for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return r

def determinant(rows):
    a=[list(map(Q,row)) for row in rows]; n=len(a); result=Q(1)
    for j in range(n):
        pivot=next((i for i in range(j,n) if a[i][j]),None)
        if pivot is None:return Q(0)
        if pivot!=j:a[j],a[pivot]=a[pivot],a[j];result=-result
        v=a[j][j];result*=v
        for i in range(j+1,n):
            factor=a[i][j]/v
            for k in range(j+1,n):a[i][k]-=factor*a[j][k]
            a[i][j]=0
    return result

def reconstruct(records,n):
    result=[[Q(0) for _ in range(n)] for _ in range(n)]; normals=[]
    for raw_w,raw_x in records:
        w=Q(raw_w); x=list(map(Q,raw_x)); check(w>0,'nonpositive atom weight')
        check(len(x)==n,'atom dimension')
        normal=[]
        for i in range(n):
            for j in range(n):result[i][j]+=w*x[i]*x[j]
            for j in range(i,n):normal.append(x[i]*x[j])
        normals.append(normal)
    return result,normals

def root_rational(x):
    a,b=isqrt(x.numerator),isqrt(x.denominator)
    check(a*a==x.numerator and b*b==x.denominator,'nonrational square root')
    return Q(a,b)

def verify_angles(cases):
    for case in cases:
        q=case['q']; grid=list(map(Q,case['grid'])); e=Q(case['epsilon'])
        check(grid==sorted(set(grid)) and grid[0]==-1 and grid[-1]==1,'invalid grid')
        check(len(grid)==2*q+1,'grid cardinality')
        gaps=[(1-a*b-root_rational((1-a*a)*(1-b*b)))/2 for a,b in zip(grid,grid[1:])]
        check(max(gaps)==e==Q(1,q*q+1),'exact angular coefficient')
        target=matrix(case['target']); actual,_=reconstruct(case['atoms'],3)
        check(actual==target,'incorrect moment reconstruction')
        for w,x in case['atoms']:
            x=list(map(Q,x)); check(x[0]==1 and x[1] in grid and x[2] in grid,'atom not on grid')
        y=[target[0][1],target[0][2]]
        check(target[0][0]==1 and target[1][2]==y[0]*y[1],'preserved moments')
        check(all(target[i+1][i+1]==y[i]**2+e*(1-y[i]**2) for i in range(2)),'diagonal correction')
        a=grid[-2]; u=Q(case['witness_mean']); bad=Q(case['bad_epsilon'])
        value=(u-a)*(u-1)+bad*(1-u*u)
        check(all((v-a)*(v-1)>=0 for v in grid),'dual grid positivity')
        check(value==Q(case['sharp_value']) and value<0 and 0<bad<e,'strict sharpness witness')
    return len(cases)

def verify_paths(cases):
    nc=0
    for case in cases:
        r=case['r']; n=case['n']; N=int(case['N']); d=n*(n+1)//2
        check(n==r+2 and r>=2 and N>=2,'path hypotheses')
        a,b,c,z=map(Q,case['anchor_parameters'])
        check([a,b,c,z]==[2*3**r+4*5**r,3**r+2*5**r,3**r+5**r,4*3**(r-1)+10*5**(r-1)],'anchor')
        U=Q(N*N+N+1); T=Q(2*N+1,2)
        A=matrix(case['objective']); recovered,rows=reconstruct(case['target_atoms'],n)
        check(A==recovered and rank(rows)==d,'interior factor spanning/reconstruction')
        expected=[[Q(0) for _ in range(n)] for _ in range(n)]
        expected[0][0]=U; expected[-1][-1]=1; expected[0][-1]=expected[-1][0]=T
        for j in range(1,n-1):expected[j][j]=U/2
        check(A==expected and U-T*T==Q(3,4),'positive definite objective')
        for w,x in case['target_atoms']:
            x=list(map(Q,x)); check(x[0]>=0 and x[-1]>=0 and all(abs(v)<=x[0] for v in x[1:-1]),'target cone constraint')
            den=Q(w).denominator; check(Q(w).numerator==1 and den&(den-1)==0,'dyadic square conversion')
        check(int(case['pivots'])==N-1,'symbolic pivot count')
        check(case['normalization_square_root']==2*n*(N+1),'normalization')
        last=-1
        for entry in case['crossings']:
            s=entry['s']; lam=Q(entry['lambda_value']); chi=Q(entry['chi']); v=Q(entry['variance'])
            check(2<=s<=N and lam>last,'ordered crossings');last=lam
            check(lam==Q(s*c-b,T-s),'crossing parameter')
            check(chi==a+lam*U-s*s*(c+lam) and chi>0,'axis reserve')
            check(v==(z+lam*U/2)/(a+lam*U) and 0<v<1,'variance reserve')
            C,normalrows=reconstruct(entry['normals'],n)
            expect=[[lam*A[i][j] for j in range(n)] for i in range(n)]
            expect[0][0]+=a;expect[0][-1]+=b;expect[-1][0]+=b;expect[-1][-1]+=c
            for j in range(1,n-1):expect[j][j]+=z
            check(C==expect,'facet reconstruction')
            check(rank(normalrows)==d-1,'facet codimension')
            for w,x in entry['normals']:
                x=list(map(Q,x)); t,y=x[0],x[-1]
                check(t>=0 and y>=0 and all(abs(vv)<=t for vv in x[1:-1]),'normal domain')
                check(t*t-(2*s-1)*t*y+(s*s-s+1)*y*y==1,'old active constraint')
                check(t*t-(2*s+1)*t*y+(s*s+s+1)*y*y==1,'new active constraint')
            check(-2*T+2*s<0,'objective descent');nc+=1
    return nc

def verify_obstruction(data):
    A0,A1,W0,W1=(matrix(data[k]) for k in ('A0','A1','W0','W1'))
    for A in (A0,A1):
        for W in (W0,W1):check(sum(A[i][j]*W[i][j] for i in range(4) for j in range(4))==0,'exposer not zero on affine fiber')
    check(determinant(W0)==data['rational_kernel_determinant']==-8,'rational zero kernel determinant')
    for W in (W0,W1):
        check(all(W[i][j]==W[j][i] for i in range(4) for j in range(4)),'exposer symmetry')
        check(all(W[i][j]==0 for i in (0,1) for j in (2,3)),'exposer block structure')
    check(data['field_polynomial']==[-2,0,1],'exposing number field')
    lo,hi=map(Q,data['positive_root_interval'])
    check(0<lo<hi and lo*lo<2<hi*hi,'positive root isolation')
    # Pair arithmetic in Q[sqrt(2)] checks both 2x2 determinants exactly.
    def mul(x,y):return (x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
    for ids in ((0,1),(2,3)):
        i,j=ids; p=(W0[i][i],W1[i][i]); q=(W0[j][j],W1[j][j]); z=(W0[i][j],W1[i][j])
        check(mul(p,q)==mul(z,z),'exposer block determinant')
        check(p[0]>=0 and p[1]>=0 and p!=(0,0),'positive diagonal')
    check(A0==matrix([[0,2,0,0],[2,0,0,0],[0,0,2,0],[0,0,0,1]]) and A1==matrix([[1,0,0,0],[0,2,0,0],[0,0,0,1],[0,0,1,0]]),'affine example changed')
    return 1

def main():
    path=ROOT/'certificates'/'new_exact_certificates.json'; raw=path.read_bytes(); data=json.loads(raw)
    counts=dict(angular_cases=verify_angles(data['angular_grids']),facet_cases=verify_paths(data['interior_paths']),arithmetic_obstructions=verify_obstruction(data['arithmetic_obstruction']))
    rejected=0
    for key,func,mutate in [
      ('angular_grids',verify_angles,lambda x:x[0].__setitem__('epsilon','1/3')),
      ('interior_paths',verify_paths,lambda x:x[0]['crossings'][0].__setitem__('chi','0')),
      ('arithmetic_obstruction',verify_obstruction,lambda x:x['W0'][0].__setitem__(0,0))]:
        x=deepcopy(data[key]); mutate(x)
        try:func(x)
        except ValueError:rejected+=1
        else:raise RuntimeError('corruption was not detected')
    report=dict(status='PASS',counts=counts,deliberate_corruptions_rejected=rejected,sha256=hashlib.sha256(raw).hexdigest(),
                scope='separately written exact verifier, no generator import; not independent human or formal verification; universal claims depend on analytical proofs')
    (ROOT/'certificates'/'verification_report.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
if __name__=='__main__':main()
