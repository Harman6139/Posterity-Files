#!/usr/bin/env python3
"""Independently verify exact quadratic-factor certificates.

No generator code is imported. The checks do not implement general rational
feasibility, a general isotropy algorithm, or formal verification of the paper.
"""
from __future__ import annotations
import argparse
import copy
from fractions import Fraction as R
from itertools import combinations, product
import hashlib
import json
from math import factorial, prod
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def require(condition,message):
    if not condition: raise ValueError(message)
def vec(v): return [R(x) for x in v]
def matrix(a): return [vec(r) for r in a]
def tr(a): return [list(v) for v in zip(*a)]
def mul(a,b):
    c=[[R(0) for _ in b[0]] for _ in a]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)): c[i][j]+=a[i][k]*b[k][j]
    return c

def ident(n): return [[R(i==j) for j in range(n)] for i in range(n)]
def diag(v): return [[R(v[i]) if i==j else R(0) for j in range(len(v))] for i in range(len(v))]
def add(a,b): return [[x+y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def scale(a,c): return [[c*x for x in row] for row in a]
def determinant(a):
    a=[r[:] for r in a]; n=len(a); out=R(1)
    if n==0:return R(1)
    for j in range(n):
        p=next((i for i in range(j,n) if a[i][j]),None)
        if p is None:return R(0)
        if p!=j:a[p],a[j]=a[j],a[p];out=-out
        pivot=a[j][j];out*=pivot
        for i in range(j+1,n):
            t=a[i][j]/pivot
            for k in range(j+1,n):a[i][k]-=t*a[j][k]
    return out

def inverse_adjugate(a):
    d=determinant(a);require(d!=0,'singular adjugate inverse');n=len(a)
    return [[R((-1)**(i+j))*determinant([[a[r][c] for c in range(n) if c!=i] for r in range(n) if r!=j])/d for j in range(n)] for i in range(n)]

def rank(a):
    a=[r[:] for r in a];m=len(a);n=len(a[0]);r=0
    for j in range(n):
        p=next((i for i in range(r,m) if a[i][j]),None)
        if p is None:continue
        a[r],a[p]=a[p],a[r];v=a[r][j]
        for i in range(r+1,m):
            t=a[i][j]/v
            for k in range(j,n):a[i][k]-=t*a[r][k]
        r+=1
        if r==m:break
    return r

def psd(a,strict=False):
    n=len(a)
    if a!=tr(a):return False
    for size in range(1,n+1):
        for S in combinations(range(n),size):
            d=determinant([[a[i][j] for j in S] for i in S])
            if d<0 or (strict and d==0):return False
    return True

def pairing(a,b):return sum((a[i][j]*b[i][j] for i in range(len(a)) for j in range(len(a))),R(0))
def gram(atoms,n):
    out=[[R(0)]*n for _ in range(n)]
    for w,v in atoms:
        for i in range(n):
            for j in range(n):out[i][j]+=w*v[i]*v[j]
    return out

def alg_add(a,b): return [x+y for x,y in zip(a,b)]
def alg_scale(a,c): return [c*x for x in a]
def alg_multiply(a,b,radicals):
    n=1<<len(radicals);out=[R(0)]*n
    for i in range(n):
        for j in range(n):
            common=i&j;factor=prod(radicals[k] for k in range(len(radicals)) if (common>>k)&1)
            out[i^j]+=a[i]*b[j]*factor
    return out

def const(a,n): return [R(a)]+[R(0)]*(n-1)

def verify_obstructions(cases):
    evaluations=0
    for c in cases:
        B=matrix(c['basis']);A=matrix(c['matrix']);m=vec(c['positive_diagonal']);J=diag(c['lorentz_diagonal'])
        q=vec(c['restricted_diagonal']);r=len(q)
        require(all(v>0 for v in m),'nonpositive support diagonal')
        require(rank(B)==r,'wrong range rank')
        require(mul(B,mul(diag(m),tr(B)))==A,'wrong obstruction Gram matrix')
        require(mul(tr(B),mul(J,B))==diag(q),'wrong quadratic restriction')
        require(pairing(J,A)==0,'trace boundary lost')
        cert=c['anisotropy'];mod=cert['modulus'];p=cert['forced_prime']
        require(p in (2,3) and mod%p==0,'unsupported modular descent')
        for v in product(range(mod),repeat=r):
            evaluations+=1
            if sum(int(a)*x*x for a,x in zip(q,v))%mod==0:
                require(all(x%p==0 for x in v),'primitive modular zero invalidates anisotropy')
        radicals=c['real_factor']['radicals'];degree=1<<len(radicals)
        cols=[[vec(v) for v in col] for col in c['real_factor']['columns']]
        n=len(A);G=[[[R(0)]*degree for _ in range(n)] for _ in range(n)]
        for col in cols:
            require(len(col)==n and all(len(x)==degree for x in col),'bad algebraic factor shape')
            require(all(x>=0 for x in col[0]) and any(x>0 for x in col[0]),'time coordinate not manifestly positive')
            value=[R(0)]*degree
            for i in range(n):
                value=alg_add(value,alg_scale(alg_multiply(col[i],col[i],radicals),J[i][i]))
                for j in range(n):G[i][j]=alg_add(G[i][j],alg_multiply(col[i],col[j],radicals))
            require(value==[R(0)]*degree,'algebraic column not null')
        require(all(G[i][j]==const(A[i][j],degree) for i in range(n) for j in range(n)),'real factor fails exact matrix identity')
    require(cases[0]['real_factor']['radicals']==[2],'totally real example changed')
    return dict(cases=len(cases),complete_modular_evaluations=evaluations)

def verify_rational(cases,obstructions):
    count=0;unweighted=0
    for c in cases:
        q=vec(c['quadratic_diagonal']);atoms=[(R(w),vec(v)) for w,v in c['weighted_atoms']];n=len(q)
        for w,v in atoms:
            require(w>0 and len(v)==n,'invalid positive atom')
            val=sum(a*x*x for a,x in zip(q,v))
            require(val>0 if c['column_condition']=='strict' else val==0,'column violates quadratic condition')
            count+=1
        require(gram(atoms,n)==matrix(c['matrix']),'rational factor reconstruction')
        cols=[vec(v) for v in c['rational_columns']]
        require(gram([(R(1),v) for v in cols],n)==matrix(c['matrix']),'unweighted rational columns do not reconstruct')
        for v in cols:
            val=sum(a*x*x for a,x in zip(q,v))
            require(val>0 if c['column_condition']=='strict' else val==0,'unweighted column constraint')
        unweighted+=len(cols)
        require(psd(matrix(c['matrix'])),'factor target not PSD')
        if c['name']=='rank_five_boundary': require(rank(matrix(c['matrix']))==5,'rank-five example wrong')
        if c['name']=='rank_preserving_strict':
            A=matrix(obstructions[2]['matrix']);b=[R(4),R(3),R(0),R(0),R(0)]
            target=add(A,gram([(R(1,5),b)],5))
            require(target==matrix(c['matrix']) and rank(target)==4,'rank-preserving correction wrong')
        if c['name']=='sharp_eight_column_boundary':
            require(len(atoms)==8 and matrix(c['matrix'])==diag([14,14]),'boundary-width example wrong')
    return dict(cases=len(cases),weighted_atoms=count,unweighted_columns=unweighted)

def verify_carriers(data):
    c=data['radical_reduction'];Q=diag(c['quadratic_diagonal']);A0=matrix(c['affine_base']);D=matrix(c['affine_direction']);X=matrix(c['full_support_witness'])
    require(add(A0,D)==X and psd(X,True),'maximal support witness')
    require(pairing(Q,A0)==0 and pairing(Q,D)==0,'affine trace identity')
    T=matrix(c['terminal_basis']);require(mul(Q,T)==[[R(0)] for _ in range(3)],'wrong radical')
    require(rank(Q)==2 and vec(c['quotient_diagonal'])==[R(1),R(-2)],'wrong nondegenerate quotient')
    atoms=[(R(1),vec(v)) for v in c['terminal_factor']]
    require(gram(atoms,3)==A0,'terminal factor reconstruction')
    c=data['curved_carrier'];Q=diag(c['quadratic_diagonal']);X=matrix(c['witness'])
    require(gram([(R(w),vec(v)) for w,v in c['weighted_atoms']],3)==X,'curved reserve factor')
    require(psd(X,True) and pairing(Q,X)==0,'curved reserve interior')
    for raw in c['viable_directions']:
        u=vec(raw);require(sum(Q[i][i]*u[i]*u[i] for i in range(3))==0,'viable vector not null')
        tau=1/(100*(1+sum(x*x for x in u)))
        Y=add(X,scale(gram([(R(1),u)],3),-tau))
        require(psd(Y,True) and pairing(Q,Y)==0,'reserve subtraction failed')
    return dict(carriers=2,viable_subtractions=len(c['viable_directions']))

def verify_cayley(cases):
    charts=0
    for c in cases:
        s=c['order'];T=matrix(c['skew']);O=matrix(c['orthogonal']);I=ident(s);D=diag(c['signs'])
        require(add(T,tr(T))==[[R(0)]*s for _ in range(s)],'skew symmetry failed')
        require(mul(tr(O),O)==I,'orthogonality failed')
        require(mul(mul(D,O),add(I,T))==add(I,scale(T,-1)),'Cayley equation failed')
        B=matrix(c['base_factor']);C=matrix(c['transformed_factor']);A=matrix(c['gram'])
        require(mul(B,O)==C and mul(B,tr(B))==A and mul(C,tr(C))==A,'exact Gram orbit failed')
        require(rank(B)<len(B),'rank-deficient test lost')
        dets=[]
        for signs in product((-1,1),repeat=s):
            dets.append(determinant(add(I,mul(diag(signs),O))));charts+=1
        require(sum(dets)==2**s and max(dets)>=1,'signed-chart determinant average failed')
        h=7;Th=[[R(0)]*s for _ in range(s)]
        for i in range(s):
            for j in range(i+1,s):
                a=T[i][j]*(2**h);nearest=(a+R(1,2)).numerator//(a+R(1,2)).denominator
                Th[i][j]=R(nearest,2**h);Th[j][i]=-Th[i][j]
        Oh=mul(D,mul(add(I,scale(Th,-1)),inverse_adjugate(add(I,Th))))
        require(mul(tr(Oh),Oh)==I,'rounded skew did not give exact orthogonal matrix')
        error=sum((Oh[i][j]-O[i][j])**2 for i in range(s) for j in range(s))
        require(error<=(R(2*s,2**h))**2,'Cayley Lipschitz bound failed')
        H=3+s*(h+s+1)+(factorial(s)-1).bit_length()
        require(all(abs(v.numerator)<=2**H and v.denominator<=2**H for row in Oh for v in row),'Cayley height bound failed')
    return dict(cases=len(cases),signed_charts=charts)

def verify_circuits(cases):
    blocks_checked=0;matrix_entries=0
    for c in cases:
        regs=c['registers'];k=len(regs);rad=c.get('radicals',[]);e=1<<len(rad)
        is_alg=bool(rad)
        def elem(x):return vec(x) if is_alg else const(R(x),1)
        blocks=[[[elem(x) for x in row] for row in b] for b in c['blocks']]
        values=[elem(x) for x in c['values']]
        t=blocks[0][0][0];require(t==const(1,e),'normalizing coordinate')
        flat=[];Fval=const(0,e)
        residual_vectors=[];n=3*k
        def resid(terms):
            v=[R(0)]*n
            for idx,coef in terms:v[idx]+=R(coef)
            residual_vectors.append(v)
        for j in range(1,k):resid([(3*j,1),(0,-1)])
        for j,(reg,b) in enumerate(zip(regs,blocks)):
            require(b[0][1]==b[1][0] and b[0][0]==const(1,e),'bad PSD block/time')
            u=b[0][1];v=b[1][1];flat.extend([b[0][0],u,v])
            det=alg_add(alg_multiply(b[0][0],v,rad),alg_scale(alg_multiply(u,u,rad),-1))
            require(det==const(0,e),'nonzero block determinant')
            require(u==values[j] and v==alg_multiply(u,u,rad),'register extraction incorrect')
            Fval=alg_add(Fval,det);blocks_checked+=1
            op=reg['op']
            if op=='constant':resid([(3*j+1,1),(0,-R(reg['value']))])
            elif op=='linear':
                require(all(i<j for i,a in reg['terms']),'circuit not acyclic')
                resid([(3*j+1,1)]+[(3*i+1,-R(a)) for i,a in reg['terms']])
            elif op=='square':
                require(reg['source']<j,'noncausal square gate')
                resid([(3*j+1,1),(3*reg['source']+2,-1)])
            else:require(op=='free','unknown circuit gate')
        for j in c['outputs']:resid([(3*j+1,1)])
        expected=[[R(0)]*n for _ in range(n)]
        for j in range(k):expected[3*j][3*j+2]+=R(1,2);expected[3*j+2][3*j]+=R(1,2);expected[3*j+1][3*j+1]-=1
        for coeff in residual_vectors:
            value=const(0,e)
            for a,z in zip(coeff,flat):value=alg_add(value,alg_scale(z,a))
            require(value==const(0,e),'circuit residual is nonzero')
            Fval=alg_add(Fval,alg_multiply(value,value,rad))
            for i in range(n):
                for j in range(n):expected[i][j]+=coeff[i]*coeff[j]
        Q=matrix(c['first_observation_matrix']);require(Q==expected,'quadratic observation coefficients incorrect')
        matrix_entries+=n*n
        direct=const(0,e)
        for i in range(n):
            for j in range(n):direct=alg_add(direct,alg_scale(alg_multiply(flat[i],flat[j],rad),Q[i][j]))
        require(direct==Fval==const(0,e),'first observation failed')
        require(alg_multiply(t,t,rad)==const(1,e),'mass observation failed')
        if c['name']=='forced_height_chain':
            require(values[-1]==const(2**(2**c['squarings']),e),'height-chain identity')
        if c['name']=='real_but_not_rational_circuit':
            require(rad==[2] and values[0]==[R(0),R(1)],'algebraic circuit witness changed')
            aa,bb=[vec(v) for v in c['rational_full_gram_vectors']]
            full=gram([(R(1),aa),(R(2),bb)],n)
            require(full==matrix(c['rational_full_gram']) and rank(full)==2,'rational full Gram obstruction')
            require(pairing(Q,full)==0 and full[0][0]==1,'full Gram observations')
            require(all(z==[aa[i],bb[i]] for i,z in enumerate(flat)),'algebraic orbit does not match full matrix')
    return dict(cases=len(cases),psd_blocks=blocks_checked,quadratic_matrix_entries=matrix_entries)

def verify(data):
    require(data.get('schema')==1,'unsupported schema')
    return dict(obstructions=verify_obstructions(data['obstructions']),
                rational_factors=verify_rational(data['rational_cases'],data['obstructions']),
                affine_carriers=verify_carriers(data['carriers']),
                cayley=verify_cayley(data['cayley']),circuits=verify_circuits(data['circuits']))

def corruption_tests(data):
    def run(change):
        bad=copy.deepcopy(data);change(bad)
        try:verify(bad)
        except (ValueError,ZeroDivisionError,IndexError,KeyError):return True
        return False
    changes=[
      lambda x:x['obstructions'][2]['matrix'][0].__setitem__(0,'49'),
      lambda x:x['obstructions'][0]['real_factor']['columns'][0][0].__setitem__(0,'2'),
      lambda x:x['rational_cases'][0]['weighted_atoms'][0].__setitem__(0,'2'),
      lambda x:x['carriers']['curved_carrier']['viable_directions'][0].__setitem__(2,2),
      lambda x:x['cayley'][0]['orthogonal'][0].__setitem__(0,'0'),
      lambda x:x['circuits'][0]['first_observation_matrix'][0].__setitem__(0,'999'),
      lambda x:x['circuits'][2]['blocks'][0][1][1].__setitem__(0,'3')]
    outcomes=[run(c) for c in changes]
    require(all(outcomes),'a deliberate corruption was accepted')
    return len(outcomes)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,default=ROOT/'certificates'/'quadratic_certificates.json')
    p.add_argument('--report',type=Path,default=ROOT/'certificates'/'verification_report.json')
    a=p.parse_args();raw=a.input.read_bytes();data=json.loads(raw)
    tests=verify(data);rejected=corruption_tests(data)
    report=dict(status='PASS',data_sha256=hashlib.sha256(raw).hexdigest(),tests=tests,
                deliberate_corruptions_rejected=rejected,
                scope='Separate exact code path; no generator imports. Not human review, a general solver, or formal proof.')
    a.report.parent.mkdir(parents=True,exist_ok=True)
    a.report.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))
if __name__=='__main__':main()
