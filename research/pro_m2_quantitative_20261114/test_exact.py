"""Reproducible exact tests; finite tests supplement, not replace, the proofs."""
from fractions import Fraction as F
from math import isqrt
import json, time
from exact_algorithms import *


def family(N):
    return [[F(0),F(1,4*N)],[F(1,4*N),F(1,2)]]

def pk(k):
    return [[F(k*k+k+1),F(-2*k-1,2)],[F(-2*k-1,2),F(1)]]

def rp(k):
    return [[F(2*k+2),F(-1)],[F(-1),F(0)]]

def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]

def transpose(a): return [list(x) for x in zip(*a)]

def run():
    started=time.time(); report={"arithmetic":"fractions.Fraction; no floating-point decisions","tests":[]}
    # Singular bordered systems must be handled, not called positive by default.
    cases=[([[0,0],[0,0]],0),([[1,0],[0,1]],F(1,2)),([[0,1],[1,0]],0),
           ([[2,-1],[-1,0]],F(-1,4)),([[1,-1],[-1,1]],0),([[1,1],[1,1]],1)]
    for q,want in cases:
        m,x,cert=simplex_min(q,True); assert m==want and quad(q,x)==m
    report['tests'].append({"name":"support enumeration including singular and boundary cases","cases":len(cases),"passed":True})
    # Full generic shadow computation, not just the closed-form recurrence.
    paths=[]
    for N in [1,2,3,5,8]:
        A=family(N); W,path,kind=shadow_separate(A,max_vectors=2_000_000)
        assert kind=='vertex' and len(path)-1==N
        assert all(P==pk(k) for k,P in enumerate(path))
        assert pairing(A,W)==F(-1,4*N)
        paths.append({"N":N,"pivots":len(path)-1,"pairing":str(pairing(A,W))})
    report['tests'].append({"name":"generic exact shadow engine follows the forced family","runs":paths,"passed":True})
    # Exact shell obstruction and minimal-q termination, with direct enumeration.
    grid=[]
    for N in [1,2,4,7,12]:
        for k in range(N):
            alpha=F(1,4*N*(k+1)); q=1
            while 4*q*q*alpha*(1+alpha)<1: q+=1
            vals=[quad(rp(k),v) for v in product(range(q+1),repeat=2) if max(v)==q]
            if k<N-1: assert q>k+1 and min(vals)<0
            else:
                assert q==N and min(vals)>=0
                W=add(rp(k),[[1,0],[0,1]],alpha*trace(rp(k)))
                assert simplex_min(W)[0]>0 and pairing(family(N),W)==F(-1,4*N)
        grid.append({"N":N,"grid_modified_pivots":N-1})
    report['tests'].append({"name":"specified corrected-grid family","runs":grid,"passed":True})
    # A large binary parameter is checked symbolically at representative indices.
    N=1<<100
    for k in [0,1,N//2,N-1]:
        assert pairing(family(N),rp(k))==F(-1,2*N)
        assert add(pk(k),rp(k))==pk(k+1)
        assert quad(rp(k),(1,k+2))==-2
    report['tests'].append({"name":"100-bit parameter identities (not a simulated 2^100-step run)","N":str(N),"passed":True})
    # General-order sharpness construction: exact minimal-vector certificates.
    sharp=[]
    for n in [2,3,4,5,6]:
        for t in [1,2,5]:
            B=canonical(n)
            U=[[F(1) if i==j else (F(-t) if j==i+1 else F(0)) for j in range(n)] for i in range(n)]
            V=[[F(t**(j-i)) if j>=i else F(0) for j in range(n)] for i in range(n)]
            assert mm(U,V)==[[F(i==j) for j in range(n)] for i in range(n)]
            Q=mm(mm(transpose(U),B),U)
            active=[]
            for i in range(n):
                for j in range(i,n):
                    z=[F(i<=k<=j) for k in range(n)]
                    v=[dot(row,z) for row in V]
                    assert min(v)>=0 and quad(Q,v)==1
                    active.append(normal(v))
            _,det=solve_det(active,[F(0)]*len(active)); assert det!=0
            x=[F(t**(n-1-i)) for i in range(n)]
            assert quad(Q,x)==1
            _,mu,_=effective_ir_bound(n,norm1(Q))
            m,_,_=simplex_min(add(Q,[[F(i==j) for j in range(n)] for i in range(n)],-mu))
            assert m>=0
            sharp.append({"n":n,"t":t,"margin_lower_bound":str(mu)})
    report['tests'].append({"name":"sharp all-order height construction and effective IR bound","runs":sharp,"passed":True})
    # A genuine five-dimensional COP boundary example, beyond entrywise/PSD tests.
    n=5
    G=[[F((i-j)%n in (1,n-1)) for j in range(n)] for i in range(n)]
    H=[[F(1)-2*G[i][j] for j in range(n)] for i in range(n)]
    A=[[F(i==j)+F(3,5)*G[i][j] for j in range(n)] for i in range(n)]
    mh,_,cert=simplex_min(H,True)
    assert mh==0 and pairing(A,H)==-1
    report['tests'].append({"name":"Horn five-cycle copositive boundary certificate","supports":len(cert),"minimum":str(mh),"pairing":str(pairing(A,H)),"passed":True})
    # Nonlocal rational algorithm, no shortcut using the family formula.
    global_runs=[]
    for N in [1,3,8]:
        A=family(N)
        W,info=nonlocal_separate(A,max_iterations=3000)
        eps=F(info['epsilon']); E=[[F(i==j) for j in range(2)] for i in range(2)]
        assert simplex_min(add(W,E,-eps))[0]>=0
        assert pairing(A,W)<=-eps
        item={"N":N,"W":serialize_matrix(W),"pairing":str(pairing(A,W)),**info}
        global_runs.append(item)
    report['tests'].append({"name":"nonlocal rounded-rational ellipsoid","runs":global_runs,"passed":True})
    # Limits must never be mistaken for a mathematical outcome.
    try: neighbor(pk(0),rp(0),max_vectors=1)
    except ResourceLimit: pass
    else: raise AssertionError('Expected resource exception')
    report['tests'].append({"name":"resource limits fail safely","passed":True})
    report['elapsed_seconds']=round(time.time()-started,3)
    report['all_passed']=True
    with open('verification_results.json','w') as f: json.dump(report,f,indent=2)
    print(json.dumps({"all_passed":True,"test_groups":len(report['tests']),"elapsed_seconds":report['elapsed_seconds'],"nonlocal_iterations":[x['iterations'] for x in global_runs]},indent=2))

if __name__=='__main__':
    if not __debug__: raise RuntimeError('Do not run these tests with -O or -OO')
    run()
