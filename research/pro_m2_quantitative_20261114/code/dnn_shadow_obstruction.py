"""Exact DNN shadow-path obstruction in every order n>=5.

The integer shear vertices are the known Dannenberg--Schuermann family.
The objectives below remain positive definite and entrywise nonnegative.
Every normal-cone certificate is an exact positive rational combination.
"""
from fractions import Fraction as F
from math import isqrt
from exact_copositive import pairing, quadratic
from ryshkov_certificates import shear_vertex, shear_ray, shear_anchor


def dnn_input(n, N, normalized=True):
    if n < 5 or N < 256*(n+1)**2:
        raise ValueError('Require n>=5 and N>=256(n+1)^2')
    r=n-1
    gamma=F(4*(r+2), r*(r+3))
    t=F(3,5)
    a=[[F(0) for _ in range(n)] for _ in range(n)]
    scale=[F(N),gamma,gamma,F(N)]+[F(N)]*(n-5)+[F(1)]
    for i in range(n):
        a[i][i]=scale[i]**2
    cycle=[0,1,2,3,n-1]
    for i,j in zip(cycle,cycle[1:]+cycle[:1]):
        a[i][j]=a[j][i]=t*scale[i]*scale[j]
    if normalized:
        a=[[v/(n*N*N) for v in row] for row in a]
    return a


def horn_separator(n,N):
    r=n-1
    gamma=F(4*(r+2), r*(r+3))
    scale=[F(N),gamma,gamma,F(N)]+[F(N)]*(n-5)+[F(1)]
    cycle=[0,1,2,3,n-1]
    edges={frozenset((i,j)) for i,j in zip(cycle,cycle[1:]+cycle[:1])}
    w=[[F(0) for _ in range(n)] for _ in range(n)]
    for i in cycle:
        for j in cycle:
            w[i][j]=F(-1 if frozenset((i,j)) in edges else 1)/(scale[i]*scale[j])
    return w


def normal_certificate(n,N,s):
    """Certificate for the unique ray from P_(s-1), not a pivot simulation."""
    a=dnn_input(n,N,normalized=False)
    r=n-1; h=F(r+2); c0=F(r*(r+3),2); b0=r*h
    stop=isqrt(N)//(4*(r+2))
    if not 2<=s<=stop:
        raise ValueError('s outside the proved range')
    lam=(s*c0-b0)/(F(6*N,5)-s)
    anchor=shear_anchor(n)
    c=[[anchor[i][j]+lam*a[i][j] for j in range(n)] for i in range(n)]
    small={1,2}
    large=[i for i in range(r) if i not in small]
    atoms=[]
    def add_pair(i,j,left,weight):
        u=[0]*n;u[i]=left;u[j]=s-left;u[-1]=1
        assert weight>0
        atoms.append((weight,u))
    for i in large:
        for j in sorted(small):
            add_pair(i,j,s-1,c[i][j]/(s-1))
    for ix,i in enumerate(large):
        for j in large[ix+1:]:
            add_pair(i,j,s-1,c[i][j]/(2*(s-1)))
            add_pair(j,i,s-1,c[i][j]/(2*(s-1)))
    left=s//2;right=s-left
    add_pair(1,2,left,c[1][2]/(left*right))
    means=[sum((weight*u[i] for weight,u in atoms),F(0)) for i in range(r)]
    residual=[c[i][-1]-means[i] for i in range(r)]
    for i in range(r):
        assert residual[i]>0,(n,N,s,'mean',i,residual[i])
        u=[0]*n;u[i]=s;u[-1]=1
        atoms.append((residual[i]/s,u))
    diagonal=[c[i][i]-s*c[i][-1]+sum(c[i][j] for j in range(r) if j!=i)
              for i in range(r)]
    for i in range(r):
        assert diagonal[i]>0,(n,N,s,'diagonal',i,diagonal[i])
        u=[0]*n;u[i]=1
        atoms.append((diagonal[i],u))
    reconstructed=[[sum((weight*u[i]*u[j] for weight,u in atoms),F(0))
                    for j in range(n)] for i in range(n)]
    assert reconstructed==c
    p=shear_vertex(n,s-1);ray=shear_ray(n,s-1)
    assert all(quadratic(p,u)==1 and quadratic(ray,u)==0 for _,u in atoms)
    assert pairing(a,ray)==-2*(F(6*N,5)-s)<0
    beta=(F(6*N,5)-s)/sum(a[i][i] for i in range(n))
    assert beta*(2*s+beta)<1
    assert pairing(a,p)>0
    return {'n':n,'N':N,'s':s,'lambda_unnormalized':lam,
            'atoms':atoms,'minimum_mean_slack':min(residual),
            'minimum_diagonal_slack':min(diagonal),
            'beta':beta,'ray':ray,'normal_matrix':c,
            'guaranteed_pivots':stop-1}


def compressed_dnn_certificate(n,N):
    a=dnn_input(n,N)
    w=horn_separator(n,N)
    r=n-1;gamma=F(4*(r+2),r*(r+3))
    assert pairing(a,w)==-F(1,n*N*N)
    assert pairing(a,a)<=1
    assert pairing(w,w)<=25/gamma**4
    stop=isqrt(N)//(4*(r+2))
    return {'n':n,'N':N,'input':a,'initial_vertex':shear_vertex(n,1),
            'anchor':shear_anchor(n),'separator':w,
            'separator_pairing':pairing(a,w),
            'distance_lower_bound':gamma**2/(5*n*N*N),
            'guaranteed_pivots':stop-1,
            'first_transition':normal_certificate(n,N,2),
            'last_certified_transition':normal_certificate(n,N,stop)}


if __name__=='__main__':
    cases=0
    for n in range(5,11):
        N=256*(n+1)**2
        stop=isqrt(N)//(4*(n+1))
        for s in range(2,stop+1):
            normal_certificate(n,N,s);cases+=1
        N=2**32
        stop=isqrt(N)//(4*(n+1))
        for s in (2,3,7,stop//2,stop):
            normal_certificate(n,N,s);cases+=1
        compressed_dnn_certificate(n,N)
    print({'exact_normal_cone_cases':cases,'dimensions':'5 through 10',
           'large_N':2**32})
