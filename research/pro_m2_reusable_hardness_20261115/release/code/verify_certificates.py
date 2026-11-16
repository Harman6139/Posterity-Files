#!/usr/bin/env python3
"""Independent exact verifier: imports no generator code.
Determinants use Bareiss integer elimination, not the generator's linear solver.
Analytical all-order statements are in the manuscript, not inferred from tests.
"""
from fractions import Fraction as F
from itertools import combinations
from math import lcm, factorial, ceil
from pathlib import Path
import hashlib, json, copy, argparse
ROOT=Path(__file__).resolve().parents[1]

def rational_matrix(a):return [[F(x) for x in r] for r in a]
def transpose(a):return [list(x) for x in zip(*a)]
def multiply(a,b):return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0)) for j in range(len(b[0]))] for i in range(len(a))]
def inner(a,b):return sum((a[i][j]*b[i][j] for i in range(len(a)) for j in range(len(a))),F(0))
def identity(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def equal(a,b,label):
    if a!=b:raise AssertionError(label)
def require(a,label):
    if not a:raise AssertionError(label)
def det(a):
    if not a:return F(1)
    den=[lcm(*(F(x).denominator for x in r)) for r in a]
    A=[[int(F(x)*d) for x in r] for r,d in zip(a,den)];n=len(A);sgn=1;last=1
    for k in range(n-1):
        p=next((i for i in range(k,n) if A[i][k]),None)
        if p is None:return F(0)
        if p!=k:A[k],A[p]=A[p],A[k];sgn=-sgn
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                val=A[i][j]*pivot-A[i][k]*A[k][j]
                require(val%last==0,'Bareiss exact division');A[i][j]=val//last
            A[i][k]=0
        last=pivot
    dd=1
    for d in den:dd*=d
    return F(sgn*A[-1][-1],dd)
def pd(a):return all(det([r[:k] for r in a[:k]])>0 for k in range(1,len(a)+1))
def psd(a):return all(det([[a[i][j] for j in S] for i in S])>=0 for k in range(1,len(a)+1) for S in combinations(range(len(a)),k))
def interval_vectors(n):return [[F(a<=i<=b) for i in range(n)] for a in range(n) for b in range(a,n)]
def gram(atoms,n):
    out=[[F(0)]*n for _ in range(n)]
    for w,v in atoms:
        w=F(w);v=list(map(F,v));require(w>=0 and all(x>=0 for x in v),'CP atom signs')
        for i in range(n):
            for j in range(n):out[i][j]+=w*v[i]*v[j]
    return out

def verify_seed(s):
    n=s['n'];r=n-1;B=rational_matrix(s['B']);W=rational_matrix(s['W']);A=rational_matrix(s['F']);C=rational_matrix(s['C']);M=rational_matrix(s['comparison']);h=list(map(F,s['h']));D=h+[F(1)];eps=F(s['epsilon'])
    require(pd(A),'seed F positive definite');require(all(x>=1 for x in h),'comparison positive scaling')
    equal([sum(M[i][j]*h[j] for j in range(r)) for i in range(r)],[F(1)]*r,'comparison solve')
    equal(M,[[A[i][j] if i==j else -A[i][j] for j in range(r)] for i in range(r)],'comparison data')
    equal(C,gram([(1,v) for v in interval_vectors(n)],n),'anchor identity')
    equal(B,[[D[i]*A[i][j]*D[j]+eps*C[i][j] for j in range(n)] for i in range(n)],'seed identity')
    require(all(x>0 for row in B for x in row),'strict target positivity')
    mu=F(s['mu']);require(pd([[B[i][j]-(mu if i==j else 0) for j in range(n)] for i in range(n)]),'certified PSD margin')
    Q=[[F(-1 if (i-j)%n in (1,n-1) else 1) for j in range(n)] for i in range(n)]
    require(not any(all(Q[i][j]<0 for i,j in combinations(S,2)) for S in combinations(range(n),3)),'triangle-free witness')
    equal(W,[[Q[i][j]/(D[i]*D[j]) for j in range(n)] for i in range(n)],'witness pullback')
    gamma=F(s['gamma']);require(gamma>0 and inner(W,B)<=-gamma,'negative pairing')
    equal(gram(s['exposure'],r),[row[:r] for row in B[:r]],'leading exposure identity')
    require(all(F(w)>0 for w,v in s['exposure']),'strict exposure')
    for p in s['proper']:
        S=[i for i in range(n) if i!=p['drop']]
        equal(gram(p['atoms'],r),[[B[i][j] for j in S] for i in S],'proper principal factor')
        CS=[[C[i][j] for j in S] for i in S]
        # Interval basis coefficients certify a full-dimensional positive reserve.
        for i in range(r):
            for j in range(i,r):
                f=lambda a,b:CS[a][b] if 0<=a<r and 0<=b<r else F(0)
                require(f(i,j)-f(i-1,j)-f(i,j+1)+f(i-1,j+1)>=1,'proper anchor reserve')
    beta=F(s['beta']);omega=F(s['omega']);tb=F(s['t_B']);eta=F(s['eta'])
    require(beta>=1 and beta*beta>=inner(B,B),'norm upper bound')
    require(omega*omega>=inner(W,W),'witness norm bound')
    equal(tb,gamma/(4*sum(B[i][i] for i in range(n))),'strict correction')
    require(0<eta<=min(1,mu/2,min(min(row) for row in B)/2,gamma/(4*(omega+tb)),eps/8),'perturbation margins')
    return len(s['proper']),sum(len(p['atoms']) for p in s['proper'])

def check_constants(s,c):
    n=s['n'];r=n-1;d=n*(n+1)//2;B=rational_matrix(s['B']);m=int(c['m']);N=int(c['N'])
    qb=lcm(*(x.denominator for row in B[:r] for x in row[:r]));FH=factorial(d-1)*(2*(2*(2*n)**r+n)**2)**(d-1)
    K=F(max(i*(n-i) for i in range(1,n)),1);T=2*sum(B[i][-1] for i in range(r))+B[-1][-1]+n+1
    sm=1+r*K*(1+F(5,2)*m)
    equal((int(c['q_B']),int(c['F_H']),F(c['K_H']),F(c['s_m'])),(qb,FH,K,sm),'scale constants')
    equal(N,ceil(8*qb*FH*T*sm),'linear scale formula');equal(c['N_bits'],N.bit_length(),'N bit count')
    lower=F(N*N,qb)-2*N*sum(B[i][-1] for i in range(r))*FH*sm-(B[-1][-1]+n*F(s['eta']))*FH*sm*sm
    require(lower>=F(N*N,2*qb),'uniform confinement inequality')
    return N,FH,qb

def check_shear(s,c):
    n=s['n'];r=n-1;N,FH,qb=check_constants(s,c['constants']);k=list(map(int,c['k']));P=rational_matrix(c['P']);Ui=identity(n)
    for i in range(r):Ui[i][-1]=k[i]
    T=identity(n)
    for i in range(n-1):T[i][i+1]=T[i+1][i]=-F(1,2)
    equal(multiply(transpose(Ui),multiply(P,Ui)),T,'normalized vertex')
    act=[list(map(F,v)) for v in c['active']];old=interval_vectors(n)
    equal(act,[[v[i]+(k[i]*v[-1] if i<r else 0) for i in range(n)] for v in old],'complete sheared minima')
    equal([sum(v[i]*P[i][j]*v[j] for i in range(n) for j in range(n)) for v in act],[F(1)]*len(act),'active equality')
    pos=[(i,i) for i in range(n)]+list(combinations(range(n),2));normal=[[v[i]*v[j]*(1 if i==j else 2) for i,j in pos] for v in old]
    require(det(normal)!=0,'perfection')
    B=rational_matrix(s['B']);BN=[[B[i][j]*(N if i<r else 1)*(N if j<r else 1) for j in range(n)] for i in range(n)];improving=0
    for idx,Rdata in enumerate(c['rays']):
        R=rational_matrix(Rdata);RR=multiply(transpose(Ui),multiply(R,Ui))
        require(all(x.denominator==1 and abs(x)<=FH for row in RR for x in row),'normalized ray height')
        vals=[sum(v[i]*RR[i][j]*v[j] for i in range(n) for j in range(n)) for v in old]
        require(all(v>=0 for v in vals) and sum(v>0 for v in vals)==1 and vals[idx]>0,'complete extreme ray basis')
        cost=inner(BN,R);equal(cost,F(c['costs'][idx]),'objective pairing')
        h=sum(B[i][j]*R[i][j] for i in range(r) for j in range(r));require(h>=0,'nonnegative exposure')
        if h>0:require(h>=F(1,qb) and cost>=F(N*N,2*qb),'escaping cost')
        else:require(all(R[i][j]==0 for i in range(r) for j in range(r)),'zero exposure exact face')
        if cost<0:improving+=1;require(h==0,'every improving ray trapped')
    require(improving>0,'improving ray existence')
    return len(c['rays']),improving

def rank3(rows):
    if not rows:return 0
    for d in range(min(3,len(rows)),0,-1):
        for I in combinations(range(len(rows)),d):
            for J in combinations(range(3),d):
                if det([[rows[i][j] for j in J] for i in I]):return d
    return 0

def verify(data):
    require(data['schema']=='finite_templates_hardness_v1','schema');stats=dict(seed_families=0,proper_principal_factors=0,weighted_factor_atoms=0,scale_cases=0,sheared_vertices=0,extreme_rays=0,improving_rays=0,graph_vertices=0,graph_pair_tests=0,spn_cases=0)
    for s in data['seeds']:
        p,a=verify_seed(s);stats['seed_families']+=1;stats['proper_principal_factors']+=p;stats['weighted_factor_atoms']+=a
    for b in data['scales']:
        for c in b['cases']:check_constants(data['seeds'][b['seed']],c);stats['scale_cases']+=1
    for b in data['shears']:
        for c in b['cases']:
            nr,ni=check_shear(data['seeds'][b['seed']],c);stats['sheared_vertices']+=1;stats['extreme_rays']+=nr;stats['improving_rays']+=ni
    graph=data['graph']
    for v in graph['vertices']:
        k=v['k'];b=list(map(F,v['b']));c=F(v['c']);equal(b,[-F(x)-F(1,2) for x in k],'grid coordinates');equal(c,F(1+sum(x*(x+1) for x in k)),'grid value')
        for u in v['active']:
            equal(sum(F(x*x) for x in u[:2])+2*sum(b[i]*u[i] for i in range(2))+c,F(1),'grid active')
        require(rank3([[2*u[0],2*u[1],1] for u in v['active']])==3,'grid vertex rank');stats['graph_vertices']+=1
    for a,b in combinations(graph['vertices'],2):
        shared=[u for u in a['active'] if u in b['active']];adj=rank3([[2*u[0],2*u[1],1] for u in shared])==2
        equal(adj,sum(abs(x-y) for x,y in zip(a['k'],b['k']))==1,'exact grid adjacency');stats['graph_pair_tests']+=1
    for R,count in graph['ball_counts']:equal(count,sum(1 for i in range(R+1) for j in range(R+1) if i+j<=R),'graph ball count')
    for x in data['spn']:
        P=rational_matrix(x['PSD']);Z=rational_matrix(x['matrix']);N=rational_matrix(x['nonnegative']);require(psd(P),'SPN PSD summand');require(all(y>=0 for row in N for y in row),'SPN nonnegative summand');equal([[P[i][j]+N[i][j] for j in range(4)] for i in range(4)],Z,'SPN sum');stats['spn_cases']+=1
    b=data['boundary'];B=rational_matrix(b['B']);R=rational_matrix(b['R']);require(pd(B),'boundary example PSD');vals=[sum(v[i]*R[i][j]*v[j] for i in range(3) for j in range(3)) for v in interval_vectors(3)]
    require(all(x>=0 for x in vals) and sum(x>0 for x in vals)==1,'boundary ray extreme');equal(inner(B,R),-F(1,4),'boundary improving escape')
    return stats

def main():
    p=ROOT/'certificates'/'exact_certificates.json';data=json.loads(p.read_text());stats=verify(data)
    def setB(d):d['seeds'][0]['B'][0][0]=str(F(d['seeds'][0]['B'][0][0])+1)
    def setW(d):d['seeds'][0]['W'][0][0]='0'
    def setCP(d):d['seeds'][0]['proper'][0]['atoms'][0][0]='-1'
    def setN(d):d['scales'][0]['cases'][0]['N']=str(int(d['scales'][0]['cases'][0]['N'])-1)
    def setR(d):d['shears'][0]['cases'][0]['rays'][0][0][0]='17'
    def setG(d):d['graph']['vertices'][0]['c']='19'
    def setS(d):d['spn'][0]['nonnegative'][0][0]='-1'
    rejected=[]
    for f in (setB,setW,setCP,setN,setR,setG,setS):
        bad=copy.deepcopy(data);f(bad)
        try:verify(bad)
        except (AssertionError,ValueError,ZeroDivisionError):rejected.append(f.__name__)
        else:raise AssertionError('corruption accepted: '+f.__name__)
    report=dict(status='PASS',checks=stats,corruptions_rejected=rejected,certificate_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),largest_analytic_prefix=str(2**64),order_five_N_bits=data['scales'][0]['cases'][-1]['N_bits'],scope='Exact independent code path, no generator imports. Analytical proofs cover all parameters; no long trajectory was simulated. Not human review or proof-assistant verification.')
    out=ROOT/'certificates'/'verification_report.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
