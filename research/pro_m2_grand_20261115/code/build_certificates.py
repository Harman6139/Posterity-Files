#!/usr/bin/env python3
"""Build exact, reproducible examples for arithmetic polyhedral Gram reduction.

Only Python's standard library is used. These examples test formulas and
certificate interfaces; they are not a production real-quantifier-elimination
implementation and do not replace the general proofs.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import product, combinations
from math import comb, isqrt
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "certificates"

def zero(n, m=None): return [[F(0) for _ in range(n if m is None else m)] for _ in range(n)]
def eye(n): return [[F(i == j) for j in range(n)] for i in range(n)]
def tr(a): return list(map(list, zip(*a)))
def mm(a,b): return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0)) for j in range(len(b[0]))] for i in range(len(a))]
def plus(a,b): return [[x+y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def scale(a,c): return [[c*x for x in row] for row in a]
def outer(v): return [[x*y for y in v] for x in v]
def gram(atoms,n):
    a=zero(n)
    for weight,v in atoms: a=plus(a,scale(outer(v),weight))
    return a

def enc(x):
    if isinstance(x,F): return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
    if isinstance(x,dict): return {k:enc(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)): return [enc(v) for v in x]
    return x

def save(name,payload):
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/name).write_text(json.dumps(enc(payload),indent=2)+"\n")

def phi(a,e):
    b=[row[:] for row in a]
    for i in range(1,len(a)): b[i][i]=(1-e)*a[i][i]+e*a[0][0]
    return b

def grid_distribution(v,q):
    t=v[0]
    if t<=0: raise ValueError("positive homogenizing coordinate required")
    probs=[(1+x/t)/2 for x in v[1:]]
    if any(p<0 or p>1 for p in probs): raise ValueError("atom outside cube cone")
    out=[]
    for ks in product(range(q+1),repeat=len(probs)):
        w=F(1)
        for k,p in zip(ks,probs): w*=comb(q,k)*p**k*(1-p)**(q-k)
        if w:
            x=[t]+[t*(-1+F(2*k,q)) for k in ks]
            out.append((w,x))
    return out

def cube_certificates():
    inputs=[(F(2,3),[F(3),F(1),F(-2)]),(F(5,4),[F(1),F(1),F(1,3)])]
    a=gram(inputs,3)
    cases=[]
    for q in (1,2,3,5):
        for e in sorted(set((F(1,q),F(q+1,2*q)))):
            atoms=[]
            theta=F(1) if q==1 else (1-e)/(1-F(1,q))
            for original_weight,v in inputs:
                for w,x in grid_distribution(v,q): atoms.append((original_weight*theta*w,x))
                if theta<1:
                    for w,x in grid_distribution(v,1): atoms.append((original_weight*(1-theta)*w,x))
            atoms=[(w,v) for w,v in atoms if w]
            target=phi(a,e)
            if gram(atoms,3)!=target: raise AssertionError("cube factor identity")
            sharp_e=F(1,q)-F(1,4*q*q)
            y=1-F(1,4*q*q)
            aa=1-F(2,q)
            Q=zero(3); Q[0][0]=aa; Q[1][1]=1; Q[0][1]=Q[1][0]=-(1+aa)/2
            sharp_value=(1-y)*(aa-y+sharp_e*(1+y))
            if sharp_value>=0: raise AssertionError("sharpness sign")
            cases.append(dict(q=q,epsilon=e,input=a,target=target,weighted_atoms=atoms,
                              dual_grid_form=Q,sharp_epsilon=sharp_e,sharp_y=y,sharp_value=sharp_value))
    return dict(kind="cube_moment_correction",dimension=3,input_atoms=inputs,cases=cases)

def obstruction():
    a0=zero(4); a1=zero(4)
    a0[0][1]=a0[1][0]=2; a0[2][2]=2; a0[3][3]=1
    a1[0][0]=1; a1[1][1]=2; a1[2][3]=a1[3][2]=1
    w0=zero(4); w1=zero(4)
    w0[0][0]=2; w0[1][1]=1; w0[2][3]=w0[3][2]=-2
    w1[0][1]=w1[1][0]=-1; w1[2][2]=1; w1[3][3]=2
    return dict(kind="one_step_arithmetic_obstruction",A0=a0,A1=a1,W_coefficients=[w0,w1],
                exposing_field_polynomial=[-2,0,1],exposing_root_interval=[F(7,5),F(3,2)],
                factor_field_polynomial=[-2,0,0,0,1],factor_root_interval=[1,F(5,4)],
                real_factor_columns=[[[0,1,0,0],[0,0,0,1],[0,0,0,0],[0,0,0,0]],
                                     [[0,0,0,0],[0,0,0,0],[0,0,1,0],[1,0,0,0]]],
                rational_kernel_determinant=F(-8),terminal_inconsistent_entry=[0,1,2])

def total_real():
    r=[[F(2),F(6)],[F(0),F(-4)],[F(1),F(1)]]
    q0=[[F(49,51),F(0)],[F(0),F(49,51)]]
    q1=[[F(0),F(-10,51)],[F(10,51),F(0)]]
    b0=mm(r,q0); b1=mm(r,q1)
    a=mm(r,tr(r))
    if plus(mm(b0,tr(b0)),scale(mm(b1,tr(b1)),2))!=a: raise AssertionError("descent identity")
    if plus(mm(b0,tr(b1)),mm(b1,tr(b0)))!=zero(3): raise AssertionError("irrational coefficient")
    return dict(kind="totally_real_constrained_descent",field_polynomial=[-2,0,1],root_interval=[1,F(3,2)],
                domain="t >= |z_1|, t >= |z_2|",algebraic_factor_coefficients=[b0,b1],
                rational_factor=r,target=a,conjugate_column_outside_domain=0)

def base_objective(m,N,gamma):
    b=zero(m+1); t=F(3,5)
    ids=[0,1,2,3,m]; ds=[F(N),gamma,gamma,F(N),F(1)]
    for i,u in enumerate(ids): b[u][u]=ds[i]**2
    for i in range(5):
        j=(i+1)%5; u,v=ids[i],ids[j]
        b[u][v]=b[v][u]=t*ds[i]*ds[j]
    for i in range(4,m): b[i][i]=F(N*N)
    return b

def normal_certificate(m,N,s):
    h=25*m+34; c=F(m*(25*m+43),2); gamma=F(2*h,c); beta=F(25); t=F(3,5)
    lam=(s*c-m*h)/(2*t*N-s)
    b=base_objective(m,N,gamma)
    c0=zero(m+1)
    for i in range(m):
        for j in range(m): c0[i][j]=F(25)+(25*m+68 if i==j else 0)
        c0[i][m]=c0[m][i]=F(h)
    c0[m][m]=c
    target=plus(c0,scale(b,lam))
    means=[target[i][m] for i in range(m)]
    atoms=[]
    small={1,2}; large=[i for i in range(m) if i not in small]
    def add_comp(i,j,a,bv,w):
        v=[F(0)]*(m+1); v[i]=F(a); v[j]=F(bv); v[m]=1; atoms.append((w,v))
    for i in large:
        for j in sorted(small): add_comp(i,j,s-1,1,target[i][j]/(s-1))
    for i,j in combinations(large,2):
        add_comp(i,j,s-1,1,target[i][j]/(2*(s-1)))
        add_comp(i,j,1,s-1,target[i][j]/(2*(s-1)))
    p=s//2; qq=s-p
    add_comp(1,2,p,qq,target[1][2]/(p*qq))
    used=[sum((w*v[i] for w,v in atoms),F(0)) for i in range(m)]
    for i in range(m):
        v=[F(0)]*(m+1); v[i]=s; v[m]=1
        atoms.append(((means[i]-used[i])/s,v))
    for i in range(m):
        chi=target[i][i]-s*means[i]+sum(target[i][j] for j in range(m) if j!=i)
        v=[F(0)]*(m+1); v[i]=1
        atoms.append((chi,v))
    if any(w<=0 for w,v in atoms): raise AssertionError("nonpositive normal weight")
    if gram(atoms,m+1)!=target: raise AssertionError("normal matrix reconstruction")
    z0=m*(25*m+37)
    total=sum(target[i][j] for i in range(m) for j in range(m))
    variance=(z0+lam)/total
    e=min(variance,1-variance)/2
    lift=[]
    for a in (1,s):
        ha=F(a+1,3*a); alpha=(variance-e*ha)/(1-e)
        if not (0<alpha<1 and 0<e<1): raise AssertionError("box distribution")
        lift.append(dict(a=a,uniform_mass=e,endpoint_fraction=alpha))
    return dict(s=s,lambda_value=lam,base_atoms=atoms,base_target=target,
                normalized_variance=variance,box_distributions=lift)

def shadow_certificates():
    cases=[]
    for m,N in ((4,2**128),(5,(32*(25*5+34))**2),(7,(40*(25*7+34))**2)):
        h=25*m+34; c=F(m*(25*m+43),2); gamma=F(2*h,c)
        M=isqrt(N)//(4*h)
        if N<256*h*h or M<2: raise AssertionError("prefix hypotheses")
        b=base_objective(m,N,gamma)
        normal_cases=[normal_certificate(m,N,s) for s in sorted({2,3,max(2,M//2),M})]
        cases.append(dict(m=m,n=m+3,N=str(N),prefix_endpoint=str(M),minimum_pivots=str(M-1),
                          h=h,c=c,gamma=gamma,base_objective=b,normal_certificates=normal_cases,
                          normalized_input_denominator=str((m+3)*N*N),
                          distance_lower_bound=gamma**2/(5*(m+3)*N*N),
                          proof_type="symbolic prefix theorem plus exact compressed normal certificates; not a trajectory simulation"))
    return dict(kind="nonsimplicial_dnn_shadow_paths",cases=cases)

def solve(a,b):
    n=len(a); mat=[list(map(F,row))+[F(rhs)] for row,rhs in zip(a,b)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if mat[i][j]),None)
        if pivot is None: return None
        mat[j],mat[pivot]=mat[pivot],mat[j]
        c=mat[j][j]; mat[j]=[x/c for x in mat[j]]
        for i in range(n):
            if i!=j and mat[i][j]:
                c=mat[i][j]; mat[i]=[x-c*y for x,y in zip(mat[i],mat[j])]
    return [row[-1] for row in mat]

def inverse(a):
    n=len(a); cols=[]
    for i in range(n):
        sol=solve(a,[F(j==i) for j in range(n)])
        if sol is None: raise ValueError("singular")
        cols.append(sol)
    return tr(cols)

def lattice_certificates():
    cases=[]
    for n,q in ((3,2),(4,5),(4,2**32)):
        B=eye(n)
        for j in range(1,n): B[0][j]=1
        V=eye(n)
        for i in range(n-1): V[i][i+1]=-q
        T=eye(n)
        for i in range(n-1): T[i][i+1]=T[i+1][i]=F(-1,2)
        Binv=inverse(B); Vinv=inverse(V)
        P=mm(tr(Binv),mm(tr(V),mm(T,mm(V,Binv))))
        atoms=[]
        for a in range(n):
            for b in range(a,n):
                e=[[F(a<=i<=b)] for i in range(n)]
                v=[row[0] for row in mm(B,mm(Vinv,e))]
                value=mm([v],mm(P,[[x] for x in v]))[0][0]
                if value!=1 or v[0]<max(abs(x) for x in v[1:]): raise AssertionError("lattice atom")
                atoms.append(v)
        w=[row[0] for row in mm(B,mm(Vinv,[[F(i==n-1)] for i in range(n)]))]
        cases.append(dict(n=n,q=str(q),lattice_basis=B,shear=V,reference_form=T,perfect_form=P,
                          active_vectors=atoms,long_minimal_vector=w,
                          margin_upper_bound=1/sum(x*x for x in w)))
    return dict(kind="sharp_cube_lattice_conditioning",cases=cases)

def horn_support_certificate():
    n=5; H=[[F(1) for _ in range(n)] for _ in range(n)]
    for i in range(n): H[i][(i+1)%n]=H[(i+1)%n][i]=F(-1)
    records=[]
    for size in range(1,n+1):
        for S in combinations(range(n),size):
            K=[[H[i][j] for j in S]+[F(-1)] for i in S]+[[F(1)]*size+[F(0)]]
            sol=solve(K,[F(0)]*size+[F(1)])
            if sol is None: outcome="singular"
            elif any(x<=0 for x in sol[:-1]): outcome="not_positive_support"
            elif sol[-1]>=0: outcome="nonnegative_stationary_value"
            else: raise AssertionError("Horn not copositive")
            records.append(dict(support=list(S),outcome=outcome,solution=sol))
    return dict(kind="rational_support_copositivity",matrix=H,records=records)

def main():
    save("arithmetic_obstruction.json",obstruction())
    save("totally_real_descent.json",total_real())
    save("cube_moment_corrections.json",cube_certificates())
    save("nonsimplicial_shadow_paths.json",shadow_certificates())
    save("lattice_sharpness.json",lattice_certificates())
    save("horn_support_certificate.json",horn_support_certificate())
    print("Wrote six exact certificate files to",OUT)

if __name__=="__main__": main()
