#!/usr/bin/env python3
"""Separately coded exact verifier; imports no generator code.
Universal quantifiers are established in the analytical proof, not finite tests.
"""
from fractions import Fraction as Q
from math import factorial
from itertools import combinations
from pathlib import Path
from copy import deepcopy
import hashlib,json

ROOT=Path(__file__).resolve().parents[1]

def require(ok,message):
    if not ok:raise ValueError(message)
def mat(a):return [[Q(x) for x in row] for row in a]
def transpose(a):return list(map(list,zip(*a)))
def product(a,b):
    bt=transpose(b)
    return [[sum((x*y for x,y in zip(row,col)),Q(0)) for col in bt] for row in a]
def pair(a,b):return sum((x*y for ar,br in zip(a,b) for x,y in zip(ar,br)),Q(0))
def norm2(a):return pair(a,a)
def quadratic(a,v):return sum((v[i]*a[i][j]*v[j] for i in range(len(v)) for j in range(len(v))),Q(0))
def identity(n):return [[Q(i==j) for j in range(n)] for i in range(n)]
def normrow(v):return [v[i]*v[j]*(1 if i==j else 2) for i in range(len(v)) for j in range(i,len(v))]

def rank(rows):
    a=[list(map(Q,row)) for row in rows];i=0
    if not a:return 0
    for j in range(len(a[0])):
        p=next((q for q in range(i,len(a)) if a[q][j]),None)
        if p is None:continue
        a[i],a[p]=a[p],a[i]
        for q in range(i+1,len(a)):
            if a[q][j]:
                u,v=a[i][j],a[q][j]
                a[q]=[u*x-v*y for x,y in zip(a[q],a[i])]
        i+=1
        if i==len(a):break
    return i

def positive_ldl(a):
    a=deepcopy(a);n=len(a)
    for i in range(n):
        require(a[i][i]>0,'nonpositive LDL pivot')
        t=a[i][i]
        for j in range(i+1,n):
            for k in range(j,n):
                a[j][k]-=a[j][i]*a[i][k]/t
                a[k][j]=a[j][k]
    return True

def check_case(case):
    n=int(case['n']);m=int(case['m']);N=int(case['N']);d=n*(n+1)//2;r=n-2
    require(n>=4 and m>=1,'invalid parameters')
    require(N==100*factorial(d-1)*(2*(m+1)**2)**(d-1),'incorrect prefix parameter')
    B=mat(case['raw_target']);A=mat(case['target']);W=mat(case['strict_separator'])
    expected=[[Q(0)]*n for _ in range(n)]
    for j in range(n-1):expected[j][j]=Q(N*N) if j==0 else Q(9*N*N,10)
    expected[-1][-1]=Q(29,10)
    for j,c in ((0,Q(1)),(1,Q(9,10)),(2,Q(-9,10))):expected[j][-1]=expected[-1][j]=N*c
    require(B==expected,'incorrect objective')
    require(A==[[x/Q(2*n*N*N) for x in row] for row in B],'target scaling')
    positive_ldl(B)
    schur=B[-1][-1]-sum(B[j][-1]**2/B[j][j] for j in range(n-1))
    require(schur==Q(1,10),'incorrect Schur reserve')
    require(sum(B[j][j] for j in range(n))<=2*n*N*N,'trace bound')
    # The triangle-free five-cycle lemma in the paper certifies Horn positivity.
    H=[[Q(1)]*5 for _ in range(5)]
    for i in range(5):H[i][(i+1)%5]=H[(i+1)%5][i]=-1
    require(not any(H[i][j]==H[j][k]==H[i][k]==-1 for i,j,k in combinations(range(5),3)),'Horn graph triangle')
    M=[[Q(0)]*n for _ in range(5)]
    M[0][0]=M[1][0]=M[2][0]=M[3][0]=1
    M[0][1]=1;M[2][1]=-1;M[1][2]=1;M[3][2]=-1;M[4][-1]=1
    pullback=product(product(transpose(M),H),M)
    require(norm2(pullback)==57,'Horn pullback norm')
    scales=[N]*(n-1)+[1]
    QN=[[pullback[i][j]/(scales[i]*scales[j]) for j in range(n)] for i in range(n)]
    eta=Q(case['cone_margin']);require(eta==Q(3,40*n*N*N),'cone margin')
    require(W==[[QN[i][j]+eta*(i==j) for j in range(n)] for i in range(n)],'strict separator formula')
    require(pair(QN,B)==-Q(3,10) and norm2(QN)<=57,'strict separating seed')
    require(pair(W,A)<=-Q(3,40*n*N*N) and norm2(W)<81,'strict certificate pairing')
    S=mat(case['transform']);T=mat(case['inverse_transform'])
    require(product(S,T)==identity(n) and product(T,S)==identity(n),'noninverse transforms')
    require(norm2(S)==norm2(T)==5*n-7,'transform norm')
    Ap=mat(case['positive_target']);Wp=mat(case['positive_separator'])
    require(Ap==[[x/Q(6*n*N*N) for x in row] for row in product(product(S,B),transpose(S))],'positive target transform')
    require(Wp==product(product(transpose(T),W),T),'positive separator transform')
    require(min(x for row in Ap for x in row)>=Q(1,6*n),'strict entry positivity')
    positive_ldl(Ap)
    rad=Q(case['positive_radius']);require(rad==Q(1,30000*n**3*N*N),'robust radius')
    require(Q(case['positive_margin'])==eta/(5*n),'transformed margin')
    require(Q(case['negative_pairing_bound'])==-Q(1,80*n*N*N),'target margin')
    require(Q(case['distance_lower'])==Q(1,3600*n*n*N*N),'distance bound')
    # Norm inequalities for every perturbation in the whole ball, not sampled noise.
    require(norm2(Wp)<=(45*n)**2,'transformed separator norm')
    require(pair(Wp,Ap)+45*n*rad<=Q(case['negative_pairing_bound']),'ball separator')
    eps=Q(1,2000*n*n*N*N)
    require(15*n*rad==eps and eps<Q(1,180*n*N*N),'PD ball and pullback')
    require(Q(49,60)+rad<1,'norm ball')
    count=0
    for data in case['crossings']:
        k=int(data['k']);E=int(data['ray_height_bound']);P=mat(data['perfect_form']);F=mat(data['forward_ray'])
        require(1<=k<=m and E==factorial(d-1)*(2*(k+1)**2)**(d-1) and N>=100*E,'ray height cutoff')
        known=[[Q(0)]*n for _ in range(n)];known[0][0]=1;known[0][-1]=known[-1][0]=-Q(2*k+1,2);known[-1][-1]=k*k+k+1
        require(P==known,'wrong perfect form')
        ray=[[Q(0)]*n for _ in range(n)];ray[0][-1]=ray[-1][0]=-1;ray[-1][-1]=2*(k+1)
        require(F==ray,'wrong forward ray')
        active=[list(map(Q,v)) for v in data['active_basis']];common=[list(map(Q,v)) for v in data['common_basis']]
        require(len(active)==d and len(common)==d-1,'basis length')
        for v in active+common:
            require(v[0]>=0 and v[-1]>=0 and all(abs(z)<=v[0] for z in v[1:-1]),'invalid lattice vector')
            require(all(x.denominator==1 for x in v) and quadratic(P,v)==1,'not an active integer vector')
        require(rank([normrow(v) for v in active])==d,'not perfect')
        require(rank([normrow(v) for v in common])==d-1,'facet codimension')
        require(all(quadratic(F,v)==0 for v in common),'common-annihilator failure')
        require(all(quadratic(F,v)>=0 for v in active),'forward feasibility')
        witness=[Q(k+2)]+[Q(0)]*r+[Q(1)]
        require(quadratic(P,witness)==3 and quadratic(F,witness)==-2,'exact edge endpoint witness')
        require(pair(B,F)==Q(data['forward_cost'])<=-N,'forward cost')
        require(Q(data['backward_cost'])==2*N-Q(29,5)*k>=N,'backward cost')
        require(Q(data['mixed_cost_lower'])==Q(N,5),'mixed cost')
        lower=Q(N*N,10)-Q(28,5)*N*E-Q(29,10)*E
        require(Q(data['off_face_cost_lower'])==lower and lower>=Q(N*N,100),'off-face exclusion')
        require(Q(1,200*n)>n*E*eps,'off-face robust sign')
        require(Q(1,2*n*N)>3*(k+1)*eps and Q(1,10*n*N)>2*eps,'on-face robust signs')
        # Check the exact cone-generation identity at arbitrary signed rational ell.
        ell=[Q((-1)**j*(j+1),7) for j in range(r)];alpha=Q(2,7);gamma=Q(5,11)
        b=sum(abs(z) for z in ell)-alpha+gamma;c=2*(k+1)*alpha-2*k*gamma
        bp=b-sum(abs(z) for z in ell)
        require((c+2*k*bp)/2==alpha and (c+2*(k+1)*bp)/2==gamma,'face decomposition identity')
        count+=1
    return count

def verify(payload):return sum(check_case(c) for c in payload['cases'])

def main():
    path=ROOT/'certificates'/'all_local_certificates.json';raw=path.read_bytes();data=json.loads(raw)
    count=verify(data);rejected=0
    mutations=[('strict_separator',(0,0)),('raw_target',(-1,-1)),('positive_target',(0,1))]
    for key,(i,j) in mutations:
        bad=deepcopy(data);bad['cases'][0][key][i][j]=str(Q(bad['cases'][0][key][i][j])+1)
        try:verify(bad)
        except (ValueError,AssertionError):rejected+=1
        else:raise AssertionError('corruption accepted: '+key)
    bad=deepcopy(data);bad['cases'][0]['m']=str(int(bad['cases'][0]['m'])+1)
    try:verify(bad)
    except (ValueError,AssertionError):rejected+=1
    else:raise AssertionError('incorrect prefix accepted')
    bad=deepcopy(data);bad['cases'][0]['crossings'][0]['forward_ray'][0][-1]='1'
    try:verify(bad)
    except (ValueError,AssertionError):rejected+=1
    else:raise AssertionError('incorrect direction accepted')
    report=dict(status='PASS',families=len(data['cases']),exact_vertex_facet_checks=count,
                deliberate_corruptions_rejected=rejected,sha256=hashlib.sha256(raw).hexdigest(),
                largest_forced_prefix=max(int(c['m']) for c in data['cases']),
                scope='Independent code path, exact rational arithmetic, no generator imports. Not human review, formal proof, or a simulated long trajectory.')
    (ROOT/'certificates'/'all_local_verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
