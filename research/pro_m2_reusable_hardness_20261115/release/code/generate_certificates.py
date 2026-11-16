#!/usr/bin/env python3
"""Exact construction for fixed-block hardness amplification.

Standard library only. Produces finite certificates of identities used in the
analytical theorems; it does not simulate exponentially long trajectories.
"""
from __future__ import annotations
from fractions import Fraction as Q
from itertools import combinations
from math import factorial, isqrt, lcm
from pathlib import Path
import json, sys
if hasattr(sys, 'set_int_max_str_digits'): sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[1]

def zeros(n,m=None): return [[Q(0) for j in range(n if m is None else m)] for i in range(n)]
def eye(n): return [[Q(i==j) for j in range(n)] for i in range(n)]
def transpose(A): return [list(x) for x in zip(*A)]
def mm(A,B): return [[sum((a*b for a,b in zip(row,col)),Q(0)) for col in zip(*B)] for row in A]
def mv(A,x): return [sum((a*b for a,b in zip(row,x)),Q(0)) for row in A]
def dot(x,y): return sum((a*b for a,b in zip(x,y)),Q(0))
def pair(A,B): return sum((dot(a,b) for a,b in zip(A,B)),Q(0))
def add(A,B): return [[a+b for a,b in zip(x,y)] for x,y in zip(A,B)]
def scale(t,A): return [[t*x for x in row] for row in A]
def outer(x): return [[a*b for b in x] for a in x]
def trace(A): return sum((A[i][i] for i in range(len(A))),Q(0))
def rowsum(A): return max(sum(abs(x) for x in row) for row in A)
def inv(A):
    n=len(A); M=[row[:]+e for row,e in zip(A,eye(n))]
    for j in range(n):
        k=next(i for i in range(j,n) if M[i][j])
        M[j],M[k]=M[k],M[j]
        s=M[j][j]; M[j]=[x/s for x in M[j]]
        for i in range(n):
            if i!=j:
                s=M[i][j]; M[i]=[x-s*y for x,y in zip(M[i],M[j])]
    return [row[n:] for row in M]
def ceilq(x): return -((-x.numerator)//x.denominator)
def ceil_sqrt(x):
    z=isqrt(x.numerator//x.denominator)
    return z if z*z>=x else z+1
def diagcong(A,d): return [[x*d[i]*d[j] for j,x in enumerate(row)] for i,row in enumerate(A)]
def treepaths(r,edges):
    adj=[[] for _ in range(r)]
    for i,j in edges: adj[i].append(j);adj[j].append(i)
    out=[]
    for i in range(r):
        for j in range(i,r):
            par={i:None}; queue=[i]
            for u in queue:
                for v in adj[u]:
                    if v not in par: par[v]=u;queue.append(v)
            if j not in par: raise ValueError('basis tree must be connected')
            v=j; p=[Q(0)]*r
            while v is not None: p[v]=Q(1); v=par[v]
            out.append(p)
    return out

def constants(H,B,W,b0=Q(4),extra_radius=Q(1)):
    r=len(H);n=r+1;d=n*(n+1)//2;Hi=inv(H);Bi=inv(B)
    h=rowsum(H);j=rowsum(Hi);q=max(2,ceil_sqrt(2*r*h));Y=2*q**r
    t=max(1,max(ceil_sqrt(Hi[i][i]) for i in range(r)));K=Y+t
    Estar=factorial(d-1)*(2*K*K)**(d-1)
    L=1+2*h; Bs=b0+L+1; Zs=max(1,ceilq(j*(Bs+Q(1,2))))
    Ts=1+r*Zs; Ps=r*h+2*r*Bs+r*h*Zs**2+1
    C=[row[:r] for row in B[:r]]; c=[B[i][r] for i in range(r)];a=B[r][r]
    alpha=pair(C,H);DC=lcm(*(x.denominator for row in C for x in row))
    w=1+sum(abs(x) for row in W for x in row);gamma=-pair(W,B)
    mu=1/trace(Bi);theta=gamma/(4*trace(B))
    zeta=min(Q(1),mu/2,min(x for row in B for x in row)/2,gamma/(4*(w+n*theta+1)),extra_radius)
    s0=1+sum(x for row in B for x in row)+zeta
    u=2*sum(abs(x) for x in c)*Estar*Ts
    v=(a+n*zeta)*Estar*Ts**2
    u2=2*sum(abs(x) for x in c)*Bs;v2=zeta*Ps
    Gamma=ceilq(max(Q(1),4*DC*(u+v+1),4*(u2+v2+1)/alpha))
    return dict(H_inverse=Hi,B_inverse=Bi,b0=b0,q=q,Y=Y,t=t,K=K,E_star=Estar,
                h=h,j=j,L=L,B_star=Bs,Z_star=Zs,T_star=Ts,P_star=Ps,
                alpha_reserve=alpha,D_C=DC,w=w,gamma=gamma,mu=mu,theta=theta,
                zeta=zeta,s0=s0,u=u,v=v,u2=u2,v2=v2,Gamma=Gamma)

def seed(label,blocks,kind='path',weighted=False,large=False):
    r=sum(blocks);n=r+1;A=eye(r);edge=[];off=0
    if kind=='D': edge=[(i,i+1) for i in range(r-2)]+[(r-3,r-1)]
    else:
        for k in blocks:
            edge +=[(off+i,off+i+1) for i in range(k-1)];off+=k
    for p,(i,j) in enumerate(edge): A[i][j]=A[j][i]=Q(1,5+p%3) if weighted else Q(1,4)
    if weighted:
        for i in range(r): A[i][i]=1+Q(i%3,10)
    c=[Q(0)]*r;off=0
    if kind=='D': c[0]=c[r-2]=Q(1)
    elif weighted:
        for i,v in {0:Q(1),2:Q(1,2),5:Q(2,3),7:Q(3,2)}.items():c[i]=v
    else:
        for k in blocks: c[off]=c[off+k-1]=Q(1);off+=k
    M=[[x if i==j else -x for j,x in enumerate(row)] for i,row in enumerate(A)]
    Mi=inv(M);Ai=inv(A);v=mv(Mi,c);dvec=mv(Mi,[Q(1)]*r)
    alpha=dot(c,mv(Ai,c));beta=dot(c,v)
    drops=[v[i]*v[i]/Mi[i][i] for i in range(r)]
    delta=min([beta-alpha]+drops)/2;a=beta-delta
    F=[row+[c[i]] for i,row in enumerate(A)]+[c+[a]]
    graph_edges=edge+[(i,r) for i,x in enumerate(c) if x]
    QG=[[Q(1) for _ in range(n)] for _ in range(n)]
    for i,j in graph_edges: QG[i][j]=QG[j][i]=Q(-1)
    WF=diagcong(QG,v+[Q(1)]);D=dvec+[Q(1)]
    W=diagcong(WF,[1/x for x in D]);base=diagcong(F,D)
    hedge=edge if kind=='D' else [(i,i+1) for i in range(r-1)]
    H=eye(r)
    for i,j in hedge:H[i][j]=H[j][i]=Q(-1,2)
    paths=treepaths(r,hedge)
    if kind=='D':
        reserve=zeros(n)
        for p in paths:
            reserve=add(reserve,add(outer(p+[Q(0)]),outer(p+[Q(1)])))
        reserve[-1][-1]+=1
        atoms=[(2,p) for p in paths]
    else:
        reserve=[[Q((min(i,j)+1)*(n-max(i,j))) for j in range(n)] for i in range(n)]
        atoms=[]
        for lo in range(r):
            for hi in range(lo,r):
                p=[Q(lo<=i<=hi) for i in range(r)]
                atoms.append((Q(2 if hi==r-1 else 1),p))
    wp=1+sum(abs(x) for row in W for x in row)
    eps=delta/(4*wp*trace(reserve));B=add(base,scale(eps,reserve))
    weights=[(eps*w,p) for w,p in atoms]
    for i in range(r):
        p=[Q(j==i) for j in range(r)];weights.append((dvec[i],p))
    for i,j in edge:
        p=[Q(k==i or k==j) for k in range(r)];weights.append((A[i][j]*dvec[i]*dvec[j],p))
    if kind=='D':
        reserve_basis=[p+[Q(0)] for p in paths]+[[Q(i==j) for i in range(r)]+[Q(1)] for j in range(r)]+[[Q(0)]*r+[Q(1)]]
    else:
        reserve_basis=[[Q(lo<=i<=hi) for i in range(n)] for lo in range(n) for hi in range(lo,n)]
    U=transpose([[p[i]*p[j] for i in range(n) for j in range(i,n)] for p in reserve_basis])
    Ui=inv(U);repair_bound=rowsum(Ui);principal_radius=eps/(2*max(Q(1),repair_bound))
    con=constants(H,B,W,extra_radius=principal_radius)
    runs=[]
    for m in ([1,7,2**64] if large else [3,19]):
        N=con['Gamma']*(m+1)
        runs.append(dict(m=m,N=N,rho=con['zeta']/(con['s0']*N*N),
                         separator_margin=con['theta']/(N*N),
                         negative_pairing_bound=-con['gamma']/(2*con['s0']*N*N),
                         distance_lower_bound=con['gamma']/(2*con['s0']*(con['w']+n*con['theta'])*N*N)))
    return dict(label=label,kind=kind,blocks=blocks,n=n,A0=A,A0_inverse=Ai,M0=M,M0_inverse=Mi,
                c=c,alpha=alpha,beta=beta,v=v,deletion_drops=drops,delta=delta,a=a,F=F,
                graph_edges=graph_edges,normal_tree_edges=hedge,H=H,path_basis=paths,d=dvec,
                QG=QG,W_F=WF,W=W,reserve=reserve,epsilon=eps,B=B,normal_atoms=weights,
                reserve_basis=reserve_basis,reserve_basis_inverse=Ui,repair_bound=repair_bound,principal_radius=principal_radius,constants=con,runs=runs)

def geometry():
    inherited=json.loads((ROOT/'inputs/inherited_prefix.json').read_text())
    r=4;H=eye(r)
    for i in range(r-1):H[i][i+1]=H[i+1][i]=Q(-1,2)
    cases=[]
    for V in inherited['branching_prefix']['vertices']:
        b=list(map(Q,V['b']));c=Q(V['c']);z=list(map(Q,V['z']));ell=list(map(Q,V['ell']))
        a=[x.numerator//x.denominator for x in z]
        bb=[x+y for x,y in zip(b,mv(H,a))];cc=c+2*dot(b,a)+dot(a,mv(H,a))
        active=[list(map(Q,u))+[Q(1)] for u in V['active']]
        sheared=[[u[i]-a[i]*u[-1] for i in range(r)]+[u[-1]] for u in active]
        cases.append(dict(H=H,b=b,c=c,z=z,ell=ell,shift=a,bar_b=bb,bar_c=cc,
                          active=active,sheared_active=sheared,face_rays=V['all_face_rays']))
    # Exact large translations of a globally integral canonical form.
    b0=[Q(0)]*(r-1)+[Q(-1,2)];z0=mv(inv(H),[-x for x in b0])
    for a in ([1,2,3,4],[2**64,2**32,7,11]):
        b=[x-y for x,y in zip(b0,mv(H,a))];c=1-2*dot(b0,a)+dot(a,mv(H,a))
        z=[x+y for x,y in zip(z0,a)];active=[]
        for lo in range(r+1):active.append([Q(i>=lo)+a[i] for i in range(r)]+[Q(1)])
        shift=[x.numerator//x.denominator for x in z]
        cases.append(dict(H=H,b=b,c=c,z=z,ell=[Q(0)]*r,shift=shift,bar_b=b0,bar_c=Q(1),
                          active=active,sheared_active=[[u[i]-shift[i] for i in range(r)]+[Q(1)] for u in active],face_rays=[]))
    # Nonintegral denominator layer in dimension one: H=4, y=2 is active.
    # At b=-2,c=4/3? Enumerate exact bounded cells and independent intersections.
    one=[]
    for h in (Q(1),Q(4),Q(9)):
        q=max(2,ceil_sqrt(2*h));Y=2*q
        cons=[(Q(-2*u,y),Q(1-h*u*u,y*y),u,y) for y in range(1,Y+1) for u in range(-2*Y,2*Y+1)]
        for a,b in combinations(cons,2):
            if a[0]==b[0]:continue
            x=(b[1]-a[1])/(a[0]-b[0])
            if not -h<=x<=0:continue
            c=a[0]*x+a[1]
            if all(c>=s*x+t for s,t,u,y in cons):
                pair0=(x,c)
                if not any(v['b']==x and v['c']==c for v in one if v['h']==h):
                    active=[(u,y) for s,t,u,y in cons if c==s*x+t]
                    one.append(dict(h=h,b=x,c=c,active=active))
    return dict(vertices=cases,one_dimensional_templates=one,
                inherited_edges=inherited['branching_prefix']['edges'],
                inherited_vertices=len(inherited['branching_prefix']['vertices']))

def arrow_cases():
    out=[]
    for p,w,slack in [([1,2,3],[-1,Q(2,3),-2],Q(1,7)),([0,1,4],[2,-3,1],Q(0)),([Q(1,5),7,2,3],[-2,3,-1,0],Q(2))]:
        p=list(map(Q,p));w=list(map(Q,w));a=sum((x*x/y for x,y in zip(w,p) if x<0),Q(0))+slack
        mat=zeros(len(p)+1);psd=zeros(len(p)+1)
        for i,y in enumerate(p):mat[i][i]=psd[i][i]=y;mat[i][-1]=mat[-1][i]=w[i];psd[i][-1]=psd[-1][i]=min(w[i],Q(0))
        mat[-1][-1]=psd[-1][-1]=a
        out.append(dict(matrix=mat,psd=psd,nonnegative=add(mat,scale(-1,psd)),slack=slack))
    return out

def restrictions():
    C=[[Q(1),Q(2)],[Q(2),Q(5)]];R=[[Q(2),Q(-1)],[Q(-1),Q(0)]]
    H=[[Q(1),Q(-1,2)],[Q(-1,2),Q(1)]]
    same=eye(5)
    for i in range(4):same[i][i+1]=same[i+1][i]=Q(1,4)
    M=[[v if i==j else -v for j,v in enumerate(row)] for i,row in enumerate(same)]
    c=[Q(1),Q(0),Q(0),Q(0),Q(1)]
    return dict(normal_escape=dict(H=H,C=C,ray=R,pairing=pair(C,R)),
                same_color=dict(A=same,c=c,alpha=dot(c,mv(inv(same),c)),beta=dot(c,mv(inv(M),c))),
                triangle=dict(X=[[Q(1)]*3 for _ in range(3)],comparison=[[Q(1 if i==j else -1) for j in range(3)] for i in range(3)]),
                singular_block=dict(H=[[Q(1)]*2 for _ in range(2)],cases=[dict(k=k,b=[Q(-2*k-1,2)]*2,c=Q(k*k+k+1),active=[[Q(i),Q(s-i),Q(1)] for s in (k,k+1) for i in range(s+1)]) for k in (1,3,9)]))

def encode(x):
    if isinstance(x,Q):return str(x)
    if isinstance(x,int):return str(x)
    if isinstance(x,list) or isinstance(x,tuple):return [encode(v) for v in x]
    if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
    return x

def main():
    specs=[('C5',[4],'path',False,True),('C7',[6],'path',False,False),('C9',[8],'path',False,False),
           ('two_C7',[6,6],'path',False,False),('C5_C4',[4,3],'path',False,False),
           ('C5_leaf',[4,1],'path',False,False),('weighted_multi_attachment',[8],'path',True,False),
           ('branched_D7',[7],'D',False,True)]
    data=dict(kind='fixed_block_amplification_exact_certificates',seeds=[seed(*s) for s in specs],
              geometry=geometry(),arrows=arrow_cases(),restrictions=restrictions(),
              scope='Exact finite identities supplement the universal analytical proof; long trajectories are not simulated.')
    out=ROOT/'certificates';out.mkdir(exist_ok=True)
    (out/'exact_certificates.json').write_text(json.dumps(encode(data),indent=2)+'\n')
    print('Generated',len(specs),'seeds and geometry/correction/restriction certificates.')
if __name__=='__main__':main()
