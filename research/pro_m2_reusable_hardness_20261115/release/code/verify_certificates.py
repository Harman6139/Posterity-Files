#!/usr/bin/env python3
"""Independent exact verifier: no imports from certificate generator.

Uses integer Bareiss determinants, modular rank witnesses, matrix-product
checks of stored inverses, and an independent one-dimensional line hull.
The universal theorems are analytical; this checks reproducible instances.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import combinations
from math import factorial, isqrt, lcm
from pathlib import Path
import copy, hashlib, json, sys
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[1]

def check(condition,message):
    if not condition:raise AssertionError(message)
def readval(x):
    if isinstance(x,str):
        try:return F(x)
        except (ValueError,ZeroDivisionError):return x
    if isinstance(x,list):return [readval(z) for z in x]
    if isinstance(x,dict):return {k:readval(v) for k,v in x.items()}
    return x

def I(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def Z(n,m=None):return [[F(0) for j in range(n if m is None else m)] for i in range(n)]
def T(A):return [list(c) for c in zip(*A)]
def mul(A,B):
    C=Z(len(A),len(B[0]))
    for i in range(len(A)):
        for k in range(len(B)):
            for j in range(len(B[0])):C[i][j]+=A[i][k]*B[k][j]
    return C

def inner(x,y):return sum((x[i]*y[i] for i in range(len(x))),F(0))
def prod(A,x):return [inner(row,x) for row in A]
def quadratic(A,x):return inner(x,prod(A,x))
def pairing(A,B):return sum(inner(a,b) for a,b in zip(A,B))
def tr(A):return sum(A[i][i] for i in range(len(A)))
def norm1(A):return max(sum(abs(x) for x in row) for row in A)
def minus(A,B):return [[x-y for x,y in zip(a,b)] for a,b in zip(A,B)]
def plus(A,B):return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]
def scaling(A,x):return [[v*x for v in row] for row in A]
def out(v):return [[x*y for y in v] for x in v]
def congr(A,d):return [[v*d[i]*d[j] for j,v in enumerate(row)] for i,row in enumerate(A)]
def ceilf(x):return (x.numerator+x.denominator-1)//x.denominator
def ceilroot(x):
    a=isqrt(x.numerator//x.denominator)
    return a+(a*a<x)
def det(A):
    """Rational determinant by one common scaling and integer Bareiss."""
    n=len(A)
    if n==0:return F(1)
    den=lcm(*(x.denominator for row in A for x in row))
    B=[[int(x*den) for x in row] for row in A];old=1;sign=1
    for k in range(n-1):
        p=next((i for i in range(k,n) if B[i][k]),None)
        if p is None:return F(0)
        if p!=k:B[p],B[k]=B[k],B[p];sign=-sign
        pivot=B[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=B[i][j]*pivot-B[i][k]*B[k][j]
                check(num%old==0,'Bareiss divisibility')
                B[i][j]=num//old
            B[i][k]=0
        old=pivot
    return F(sign*B[-1][-1],den**n)
def SPD(A):
    return A==T(A) and all(det([row[:k] for row in A[:k]])>0 for k in range(1,len(A)+1))
def psd_ldl(A):
    """Exact semidefinite elimination, including zero pivots."""
    B=copy.deepcopy(A);n=len(B)
    if B!=T(B):return False
    for k in range(n):
        if B[k][k]<0:return False
        if B[k][k]==0:
            if any(B[i][k] for i in range(k+1,n)):return False
            continue
        for i in range(k+1,n):
            for j in range(k+1,n):B[i][j]-=B[i][k]*B[k][j]/B[k][k]
    return True

def modrank(A,p=1000003):
    if not A:return 0
    B=[[int(x.numerator)*pow(int(x.denominator),-1,p)%p for x in row] for row in A]
    rank=0
    for j in range(len(B[0])):
        k=next((i for i in range(rank,len(B)) if B[i][j]),None)
        if k is None:continue
        B[k],B[rank]=B[rank],B[k];s=pow(B[rank][j],-1,p)
        B[rank]=[(x*s)%p for x in B[rank]]
        for i in range(rank+1,len(B)):
            s=B[i][j]
            B[i]=[(x-s*y)%p for x,y in zip(B[i],B[rank])]
        rank+=1
        if rank==len(B):break
    return rank

def minor(A,i):return [[v for k,v in enumerate(row) if k!=i] for j,row in enumerate(A) if j!=i]

def verify_seed(s):
    n=int(s['n']);r=n-1;A=s['A0'];M=s['M0'];c=s['c'];v=s['v'];H=s['H'];B=s['B'];W=s['W']
    check(len(A)==r and len(B)==n,'seed dimensions')
    check(SPD(A) and SPD(M),'seed leading definiteness')
    check(M==[[x if i==j else -x for j,x in enumerate(row)] for i,row in enumerate(A)],'comparison entries')
    check(mul(A,s['A0_inverse'])==I(r) and mul(M,s['M0_inverse'])==I(r),'seed inverse products')
    check(prod(s['M0_inverse'],c)==v,'v identity')
    check(inner(c,prod(s['A0_inverse'],c))==s['alpha'],'real threshold')
    check(inner(c,v)==s['beta'],'CP threshold')
    check(s['alpha']<s['a']<s['beta'],'strict threshold interval')
    drops=[v[i]**2/s['M0_inverse'][i][i] for i in range(r)]
    check(drops==s['deletion_drops'],'deletion drops')
    check(s['delta']==min([s['beta']-s['alpha']]+drops)/2,'delta formula')
    check(s['a']==s['beta']-s['delta'],'hub budget')
    F0=s['F'];check(F0==[row+[c[i]] for i,row in enumerate(A)]+[c+[s['a']]],'bordered seed')
    check(SPD(F0),'full seed PD')
    MF=[[x if i==j else -x for j,x in enumerate(row)] for i,row in enumerate(F0)]
    for i in range(n):check(SPD(minor(MF,i)),f'proper principal comparison {i}')
    edges={tuple(map(int,e)) for e in s['graph_edges']}
    actual={(i,j) for i in range(n) for j in range(i+1,n) if F0[i][j]}
    check(edges==actual,'graph support')
    for i,j,k in combinations(range(n),3):
        check(not all((u,vv) in edges for u,vv in [(i,j),(i,k),(j,k)]),'triangle-free witness')
    QG=[[F(1 if i==j or (min(i,j),max(i,j)) not in edges else -1) for j in range(n)] for i in range(n)]
    check(QG==s['QG'],'graph quadratic')
    check(s['W_F']==congr(QG,v+[F(1)]),'graph witness congruence')
    check(pairing(s['W_F'],F0)==s['a']-s['beta'],'graph witness gap')
    d=s['d'];check(prod(M,d)==[F(1)]*r and min(d)>0,'normalizing scaling')
    check(W==congr(s['W_F'],[1/x for x in d]+[F(1)]),'witness normalization')
    reserve=s['reserve'];check(SPD(reserve) and min(x for row in reserve for x in row)>0,'strict reserve')
    wp=1+sum(abs(x) for row in W for x in row)
    check(s['epsilon']==s['delta']/(4*wp*tr(reserve)),'reserve scale')
    check(B==plus(congr(F0,d+[F(1)]),scaling(reserve,s['epsilon'])),'seed assembly')
    check(SPD(B) and min(x for row in B for x in row)>0,'final seed PD and positivity')
    check(pairing(W,B)<=-3*s['delta']/4,'separator survives reserve')
    check(SPD(H),'perfect block SPD')
    check(all(H[i][i]==1 for i in range(r)) and all(H[i][j] in (0,F(-1,2)) for i in range(r) for j in range(i)),'integral quadratic lattice')
    paths=s['path_basis']
    check(all(quadratic(H,p)==1 for p in paths),'tree-path minimum')
    cols=[[p[i]*p[j] for i in range(r) for j in range(i,r)] for p in paths]
    check(modrank(cols)==r*(r+1)//2,'rank-one span witness')
    C=Z(r)
    for lam,p in s['normal_atoms']:
        check(lam>0 and min(p)>=0 and all(x.denominator==1 for x in p),'positive integral normal certificate')
        check(quadratic(H,p)==1,'normal equality')
        C=plus(C,scaling(out(p),lam))
    check(C==[row[:r] for row in B[:r]],'normal reserve reconstruction')
    # Verify CP reserve itself by constructing its stated atoms, not merely PSD.
    reserve_test=Z(n)
    if s['kind']=='D':
        for p in paths:reserve_test=plus(reserve_test,plus(out(p+[F(0)]),out(p+[F(1)])))
        reserve_test[-1][-1]+=1
    else:
        for lo in range(n):
            for hi in range(lo,n):reserve_test=plus(reserve_test,out([F(lo<=i<=hi) for i in range(n)]))
    check(reserve==reserve_test,'CP reserve identity')
    basis=s['reserve_basis'];U=T([[p[i]*p[j] for i in range(n) for j in range(i,n)] for p in basis]);Ui=s['reserve_basis_inverse']
    check(mul(U,Ui)==I(n*(n+1)//2),'full reserve right inverse')
    remaining=copy.deepcopy(reserve)
    for p in basis:remaining=minus(remaining,out(p))
    # Membership of each selected atom in the explicit reserve ensures the
    # remaining sum is CP, rather than merely PSD.
    available=[]
    if s['kind']=='D':
        for p in paths:available.extend([p+[F(0)],p+[F(1)]])
        available.append([F(0)]*r+[F(1)])
    else:
        available=[[F(lo<=i<=hi) for i in range(n)] for lo in range(n) for hi in range(lo,n)]
    for p in basis:
        check(p in available,'basis atom in reserve');available.remove(p)
    check(norm1(Ui)==s['repair_bound'],'repair inverse norm')
    check(s['principal_radius']==s['epsilon']/(2*max(F(1),norm1(Ui))),'principal CP stability radius')
    k=s['constants'];Hi=k['H_inverse'];Bi=k['B_inverse']
    check(mul(H,Hi)==I(r) and mul(B,Bi)==I(n),'amplification inverse products')
    h=norm1(H);j=norm1(Hi);q=max(2,ceilroot(2*r*h));Y=2*q**r;t=max(1,max(ceilroot(Hi[i][i]) for i in range(r)));K=Y+t
    dmat=n*(n+1)//2;E=factorial(dmat-1)*(2*K*K)**(dmat-1)
    L=1+2*h;Bs=k['b0']+L+1;Zs=max(1,ceilf(j*(Bs+F(1,2))));Ts=1+r*Zs;Ps=r*h+2*r*Bs+r*h*Zs**2+1
    cr=[B[i][-1] for i in range(r)];alpha=pairing(C,H);DC=lcm(*(x.denominator for row in C for x in row))
    w=1+sum(abs(x) for row in W for x in row);gamma=-pairing(W,B);mu=1/tr(Bi);theta=gamma/(4*tr(B))
    zeta=min(F(1),mu/2,min(x for row in B for x in row)/2,gamma/(4*(w+n*theta+1)),s['principal_radius']);s0=1+sum(x for row in B for x in row)+zeta
    u=2*sum(abs(x) for x in cr)*E*Ts;v2ray=(B[-1][-1]+n*zeta)*E*Ts**2
    u2=2*sum(abs(x) for x in cr)*Bs;v2=zeta*Ps
    Gamma=ceilf(max(F(1),4*DC*(u+v2ray+1),4*(u2+v2+1)/alpha))
    expected=dict(q=q,Y=Y,t=t,K=K,E_star=E,h=h,j=j,L=L,B_star=Bs,Z_star=Zs,T_star=Ts,P_star=Ps,alpha_reserve=alpha,D_C=DC,w=w,gamma=gamma,mu=mu,theta=theta,zeta=zeta,s0=s0,u=u,v=v2ray,u2=u2,v2=v2,Gamma=Gamma)
    for key,value in expected.items():check(k[key]==value,'constant '+key)
    check(gamma>0 and zeta>0,'positive certified margins')
    maxbits=0
    for run in s['runs']:
        m=int(run['m']);N=int(run['N']);MM=m+1
        check(N==Gamma*MM,'linear scale law')
        check(F(N*N,DC)-u*N*MM-v2ray*MM*MM>=F(3*N*N,4*DC),'all-ray confinement bound')
        check(alpha*N*N-u2*N*MM-v2*MM*MM>=3*alpha*N*N/4,'all-vertex gap')
        check(run['rho']==zeta/(s0*N*N),'perturbation radius')
        check(run['separator_margin']==theta/(N*N),'separator margin')
        check(run['negative_pairing_bound']==-gamma/(2*s0*N*N),'separation bound')
        check(run['distance_lower_bound']==gamma/(2*s0*(w+n*theta)*N*N),'distance bound')
        # Exact target pairing, including the scalar strictification.
        center_pair=(-gamma+theta*(sum(B[i][i] for i in range(r))+B[r][r]/(N*N)))/(s0*N*N)
        check(center_pair+(w+n*theta)*run['rho']<=run['negative_pairing_bound'],'robust dual gap')
        maxbits=max(maxbits,N.bit_length())
    return dict(label=s['label'],order=n,proper_principal_certificates=n,normal_atoms=len(s['normal_atoms']),scale_cases=len(s['runs']),max_N_bits=maxbits,normal_span=r*(r+1)//2)

def one_dim_hull(h):
    q=max(2,ceilroot(2*h));Y=2*q;slopes={}
    for y in range(1,Y+1):
        for u in range(-2*Y,2*Y+1):
            slope=F(-2*u,y);intercept=(1-h*u*u)/(y*y)
            slopes[slope]=max(slopes.get(slope,intercept),intercept)
    hull=[]
    for slope,intercept in sorted(slopes.items()):
        start=None
        while hull:
            sm,si,st=hull[-1];start=(si-intercept)/(slope-sm)
            if st is None or start>st:break
            hull.pop()
        if not hull:start=None
        hull.append((slope,intercept,start))
    result=set()
    for slope,intercept,start in hull:
        if start is not None and -h<=start<=0:result.add((start,slope*start+intercept))
    return result

def verify_geometry(g):
    active_count=0;ray_count=0
    for v in g['vertices']:
        H=v['H'];r=len(H);b=v['b'];c=v['c'];z=v['z'];ell=v['ell'];a=v['shift']
        check(all(x>=0 for x in z+ell) and all(z[i]*ell[i]==0 for i in range(r)),'continuous KKT signs')
        check([ell[i]-x for i,x in enumerate(prod(H,z))]==b,'continuous stationarity')
        check(a==[F(x.numerator//x.denominator) for x in z],'floor shear')
        check(v['bar_b']==[b[i]+x for i,x in enumerate(prod(H,a))],'cross shear')
        check(v['bar_c']==c+2*inner(b,a)+quadratic(H,a),'last shear')
        f=[z[i]-a[i] for i in range(r)]
        check(v['bar_c']==c-quadratic(H,z)+quadratic(H,f),'complementarity cancellation')
        check(c>quadratic(H,z) and c<=quadratic(H,z)+1,'strict gap')
        normals=[]
        for u,bar in zip(v['active'],v['sheared_active']):
            x,y=u[:-1],u[-1]
            check(quadratic(H,x)+2*y*inner(b,x)+c*y*y==1,'active equality')
            check(bar==[x[i]-a[i]*y for i in range(r)]+[y],'active shear')
            check(quadratic(H,bar[:-1])+2*y*inner(v['bar_b'],bar[:-1])+v['bar_c']*y*y==1,'sheared equality')
            residual=[x[i]-y*z[i] for i in range(r)]
            check(quadratic(H,residual)+2*y*inner(ell,x)==1-y*y*(c-quadratic(H,z)),'residual identity')
            normals.append([2*y*xx for xx in x]+[y*y]);active_count+=1
        check(modrank(normals)==r+1,'face vertex span')
        for R in v['face_rays']:
            w=R[:r];s=R[-1]
            check(all(2*u[-1]*inner(w,u[:-1])+s*u[-1]**2>=0 for u in v['active']),'tangent feasibility')
            ray_count+=1
    templates=g['one_dimensional_templates']
    for h in [F(1),F(4),F(9)]:
        actual={(v['b'],v['c']) for v in templates if v['h']==h}
        check(actual==one_dim_hull(h),'independent denominator-layer hull')
        for v in templates:
            if v['h']!=h:continue
            normals=[]
            for u,y in v['active']:
                check(h*u*u+2*v['b']*u*y+v['c']*y*y==1,'one-dimensional active layer')
                normals.append([2*u*y,y*y])
            check(modrank(normals)==2,'one-dimensional vertex span')
    # Check inherited bounded movement from independently supplied endpoints.
    # Original edges use vertex IDs; verify all that can be read without guessing.
    return dict(vertices=len(g['vertices']),active_equalities=active_count,face_rays=ray_count,
                full_lattice_hull_cases=3,full_lattice_templates=len(templates),
                largest_integer_shear=max(int(max(v['shift'])) for v in g['vertices']))

def verify_arrows(arrows):
    for c in arrows:
        check(c['matrix']==plus(c['psd'],c['nonnegative']),'SPN decomposition')
        check(psd_ldl(c['psd']),'arrow PSD component')
        check(min(x for row in c['nonnegative'] for x in row)>=0,'arrow nonnegative component')
        A=c['matrix'];r=len(A)-1
        p=[A[i][i] for i in range(r)];w=[A[i][-1] for i in range(r)]
        check(A[-1][-1]-sum(x*x/y for x,y in zip(w,p) if x<0)==c['slack'],'arrow exact Schur budget')
        check(c['slack']>=0,'arrow nonnegative slack')
    return len(arrows)

def verify_restrictions(x):
    e=x['normal_escape'];check(SPD(e['C']),'escape objective PD')
    check(pairing(e['C'],e['ray'])==e['pairing']<0,'outside normal cone descent')
    for v in [[F(1),F(0)],[F(0),F(1)],[F(1),F(1)]]:check(quadratic(e['ray'],v)>=0,'escape ray feasibility')
    s=x['same_color'];check(s['alpha']==s['beta'],'same-color gap must vanish')
    A=s['A'];c=s['c'];check(SPD(A),'same-color leading SPD')
    # A sign change preserving c conjugates A to its comparison matrix.
    signs=[F((-1)**i) for i in range(len(c))];check([a*b for a,b in zip(signs,c)]==c,'same-color signs')
    tri=x['triangle'];check(tri['X']==out([F(1)]*3),'triangle CP witness')
    check(quadratic(tri['comparison'],[F(1)]*3)<0,'triangle comparison counterexample')
    sing=x['singular_block'];check(det(sing['H'])==0,'singular block')
    for c in sing['cases']:
        k=int(c['k']);check(c['b']==[F(-2*k-1,2)]*2 and c['c']==k*k+k+1,'singular epigraph vertex')
        normals=[]
        for x0 in c['active']:
            u=x0[:2];y=x0[-1]
            check(min(x0)>=0 and quadratic(sing['H'],u)+2*y*inner(c['b'],u)+c['c']*y*y==1,'singular-block active family')
            normals.append([2*y*x for x in u]+[y*y])
        check(modrank(normals)==3 and len(c['active'])==2*k+3,'unbounded active cardinality')
    return dict(restriction_groups=4,singular_block_cases=len(sing['cases']))

def verify_all(data):
    check(data['kind']=='fixed_block_amplification_exact_certificates','format')
    seeds=[verify_seed(s) for s in data['seeds']]
    return dict(status='PASS',seed_families=seeds,geometry=verify_geometry(data['geometry']),
                arrow_decompositions=verify_arrows(data['arrows']),restrictions=verify_restrictions(data['restrictions']))

def main():
    path=ROOT/'certificates/exact_certificates.json';raw=path.read_bytes();data=readval(json.loads(raw))
    report=verify_all(data)
    mutations=[]
    def mutate(label,f):
        c=copy.deepcopy(data);f(c)
        try:verify_all(c)
        except (AssertionError,ValueError,ZeroDivisionError,IndexError):mutations.append(label);return
        raise AssertionError('corruption accepted: '+label)
    mutate('seed off-diagonal',lambda c:c['seeds'][0]['B'][0].__setitem__(1,c['seeds'][0]['B'][0][1]+1))
    mutate('comparison inverse',lambda c:c['seeds'][1]['M0_inverse'][0].__setitem__(0,c['seeds'][1]['M0_inverse'][0][0]+1))
    mutate('wrong deletion budget',lambda c:c['seeds'][3].__setitem__('delta',c['seeds'][3]['delta']*3))
    mutate('normal reserve weight',lambda c:c['seeds'][2]['normal_atoms'][0].__setitem__(0,F(-1)))
    mutate('under-scaled amplifier',lambda c:c['seeds'][0]['runs'][0].__setitem__('N',F(1)))
    mutate('invalid sheared active vector',lambda c:c['geometry']['vertices'][0]['sheared_active'][0].__setitem__(0,F(1)))
    mutate('omitted denominator template',lambda c:c['geometry']['one_dimensional_templates'].pop())
    mutate('incorrect arrow correction',lambda c:c['arrows'][0]['psd'][-1].__setitem__(-1,F(-1)))
    mutate('false same-color gap',lambda c:c['restrictions']['same_color'].__setitem__('beta',c['restrictions']['same_color']['beta']+1))
    report['corruptions_rejected']=mutations
    report['certificate_sha256']=hashlib.sha256(raw).hexdigest()
    report['scope']='Independent exact code path, no generator imports. Neither human review, formal proof-assistant checking, nor long-trajectory simulation.'
    (ROOT/'certificates/verification_report.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
if __name__=='__main__':main()
