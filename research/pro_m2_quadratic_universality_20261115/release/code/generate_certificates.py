#!/usr/bin/env python3
"""Generate exact examples for the single-quadratic Gram classification.

Standard library only. This is not a general rational-point or isotropy solver.
All arithmetic in the saved certificates is rational or in a specified formal
multiquadratic algebra; the verifier is a separate program.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import argparse
import json

ROOT = Path(__file__).resolve().parents[1]

def zeros(n, m=None):
    return [[F(0) for _ in range(n if m is None else m)] for _ in range(n)]
def transpose(a): return [list(v) for v in zip(*a)]
def matmul(a,b):
    return [[sum((x*y for x,y in zip(row,col)),F(0)) for col in zip(*b)] for row in a]
def diagonal(v): return [[F(v[i]) if i==j else F(0) for j in range(len(v))] for i in range(len(v))]
def outer(v): return [[x*y for y in v] for x in v]
def gram(atoms,n):
    a=zeros(n)
    for w,v in atoms:
        for i in range(n):
            for j in range(n): a[i][j]+=w*v[i]*v[j]
    return a

def inverse(a):
    n=len(a); b=[list(map(F,row))+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        p=next((i for i in range(j,n) if b[i][j]),None)
        if p is None: raise ValueError('singular matrix')
        b[j],b[p]=b[p],b[j]
        z=b[j][j]; b[j]=[v/z for v in b[j]]
        for i in range(n):
            if i!=j:
                z=b[i][j]; b[i]=[x-z*y for x,y in zip(b[i],b[j])]
    return [row[n:] for row in b]

def alg(value=0,dim=2,index=0):
    out=[F(0)]*dim; out[index]=F(value); return out

def obstructions():
    # Coordinates in the real factors use square-root basis masks.
    B2=[[F(1),F(0)],[F(0),F(1)],[F(0),F(1)]]
    cols2=[[alg(1),alg(F(sign,2),index=1),alg(F(sign,2),index=1)] for sign in (1,-1)]
    B3=zeros(6,3); B3[0][0]=1
    B3[1][1]=B3[2][1]=1
    B3[3][2]=B3[4][2]=B3[5][2]=1
    cols3=[]
    for sign in (1,-1):
        cols3.append([alg(1,4),alg(F(sign,2),4,1),alg(F(sign,2),4,1),alg(0,4),alg(0,4),alg(0,4)])
    for sign in (1,-1):
        cols3.append([alg(F(1,2),4,3),alg(0,4),alg(0,4),alg(F(sign,2),4,1),alg(F(sign,2),4,1),alg(F(sign,2),4,1)])
    B4=zeros(5,4); B4[0][0]=4; B4[1][0]=3
    for j in range(1,4): B4[j+1][j]=1
    cols4=[]
    for i in range(3):
        for sign in (1,-1):
            col=[alg(2,4,1),alg(F(3,2),4,1)]+[alg(0,4) for _ in range(3)]
            col[i+2]=alg(F(sign,2),4,3); cols4.append(col)
    raw=[('rank_two',B2,[2,1],[1,-2],[2],cols2,8,2),
         ('rank_three',B3,[5,1,1],[1,-2,-3],[2,3],cols3,9,3),
         ('rank_four_sharp',B4,[3,7,7,7],[7,-1,-1,-1],[2,7],cols4,8,2)]
    out=[]
    for name,B,m,q,radicals,cols,modulus,p in raw:
        A=matmul(B,matmul(diagonal(m),transpose(B)))
        out.append(dict(name=name,basis=B,positive_diagonal=m,matrix=A,
                        lorentz_diagonal=[1]+[-1]*(len(A)-1),restricted_diagonal=q,
                        real_factor=dict(radicals=radicals,columns=cols),
                        anisotropy=dict(modulus=modulus,forced_prime=p,
                          statement='Every zero modulo modulus has every coordinate divisible by forced_prime; primitive integer descent.')))
    return out

def rational_cases(obs):
    r5=[]
    for i in range(1,5):
        for sign in (1,-1):
            v=[F(1)]+[F(0)]*4; v[i]=sign; r5.append((F(1),v))
    c3=[]
    for t in (F(0),F(1),F(-1),F(2),F(1,2)):
        c3.append((F(1),[1-t*t,2*t,1+t*t]))
    # A rank-preserving strict rationalization of the rank-four obstruction.
    B=obs[2]['basis']; strict=[]
    for i in range(1,4):
        for sign in (1,-1):
            v=[F(5)]+[F(0)]*3; v[i]=13*sign
            strict.append((F(7,338),[row[0] for row in matmul(B,[[x] for x in v])]))
    strict.append((F(79,845),[4,3,0,0,0]))
    width=[]
    for sign in (1,-1):
        for a in (2,1,1,1): width.append((F(1),[F(a),F(sign*a)]))
    raw=[('rank_five_boundary',[1,-1,-1,-1,-1],r5,'zero'),
         ('split_quadric_boundary',[1,1,-1],c3,'zero'),
         ('rank_preserving_strict',[1,-1,-1,-1,-1],strict,'strict'),
         ('sharp_eight_column_boundary',[1,-1],width,'zero')]
    return [dict(name=name,quadratic_diagonal=q,weighted_atoms=atoms,
                 matrix=gram(atoms,len(q)),column_condition=cond) for name,q,atoms,cond in raw]

def carrier_cases():
    return dict(
      radical_reduction=dict(quadratic_diagonal=[1,-2,0],
        affine_base=diagonal([0,0,1]),affine_direction=diagonal([2,1,0]),
        full_support_witness=diagonal([2,1,1]),terminal_basis=[[0],[0],[1]],
        terminal_factor=[[0,0,1]],quotient_diagonal=[1,-2]),
      curved_carrier=dict(quadratic_diagonal=[1,1,-1],witness=diagonal([1,1,2]),
        weighted_atoms=[(F(1,2),[1,0,1]),(F(1,2),[1,0,-1]),
                        (F(1,2),[0,1,1]),(F(1,2),[0,1,-1])],
        viable_directions=[[1,0,1],[3,4,5],[5,12,13],[-8,15,17]]))

def cayley_cases():
    out=[]
    for s in (2,3,5):
        T=zeros(s)
        for i in range(s):
            for j in range(i+1,s): T[i][j]=F((i+2)*(j+1)-s,7); T[j][i]=-T[i][j]
        I=diagonal([1]*s)
        IpT=[[I[i][j]+T[i][j] for j in range(s)] for i in range(s)]
        ImT=[[I[i][j]-T[i][j] for j in range(s)] for i in range(s)]
        D=diagonal([(-1)**i for i in range(s)])
        O=matmul(D,matmul(ImT,inverse(IpT)))
        B=[[F(i+j+1,3) for j in range(s)] for i in range(2)]
        B.append([B[0][j]+B[1][j] for j in range(s)]) # rank deficient
        factor=matmul(B,O)
        out.append(dict(order=s,skew=T,signs=[(-1)**i for i in range(s)],orthogonal=O,
                        base_factor=B,transformed_factor=factor,gram=matmul(B,transpose(B))))
    return out

class Circuit:
    def __init__(self): self.reg=[]; self.values=[]; self.outputs=[]
    def free(self,name,value):
        self.reg.append(dict(name=name,op='free')); self.values.append(F(value)); return len(self.reg)-1
    def const(self,name,value):
        self.reg.append(dict(name=name,op='constant',value=F(value))); self.values.append(F(value)); return len(self.reg)-1
    def lin(self,name,terms):
        terms=[(int(i),F(c)) for i,c in terms]
        self.reg.append(dict(name=name,op='linear',terms=terms))
        self.values.append(sum((c*self.values[i] for i,c in terms),F(0))); return len(self.reg)-1
    def square(self,name,i):
        self.reg.append(dict(name=name,op='square',source=int(i)))
        self.values.append(self.values[i]**2); return len(self.reg)-1
    def export(self,name):
        blocks=[[[F(1),a],[a,a*a]] for a in self.values]
        return dict(name=name,registers=self.reg,outputs=self.outputs,values=self.values,
                    blocks=blocks,observation_target=[0,1])

def circuits():
    C=Circuit(); x=C.free('x',F(3,2)); y=C.free('y',F(-2,3))
    plus=C.lin('plus',[(x,1),(y,1)]); minus=C.lin('minus',[(x,1),(y,-1)])
    pp=C.square('plus_squared',plus); mm=C.square('minus_squared',minus)
    p=C.lin('product',[(pp,F(1,4)),(mm,F(-1,4))]); one=C.const('one',1)
    z=C.lin('equation_xy_plus_one',[(p,1),(one,1)]); C.outputs=[z]
    first=C.export('rational_multiplication')
    C=Circuit(); v=C.const('a0',2)
    for j in range(1,9): v=C.square(f'a{j}',v)
    second=C.export('forced_height_chain'); second['squarings']=8
    # An algebraic solution of x^2=2, in Q(sqrt(2)).
    registers=[dict(name='x',op='free'),dict(name='x2',op='square',source=0),
               dict(name='two',op='constant',value=F(2)),
               dict(name='equation',op='linear',terms=[(1,F(1)),(2,F(-1))])]
    vals=[alg(1,index=1),alg(2),alg(2),alg(0)]
    squares=[alg(2),alg(4),alg(4),alg(0)]
    blocks=[[[alg(1),a],[a,v]] for a,v in zip(vals,squares)]
    third=dict(name='real_but_not_rational_circuit',registers=registers,outputs=[3],
               radicals=[2],values=vals,blocks=blocks,observation_target=[0,1],
               rational_obstruction='x^2=2 implies a primitive integral zero of t^2-2u^2; see modular certificate')
    avec=[F(1),F(0),F(2),F(1),F(2),F(4),F(1),F(2),F(4),F(1),F(0),F(0)]
    bvec=[F(0)]*12; bvec[1]=1
    third['rational_full_gram']=gram([(F(1),avec),(F(2),bvec)],12)
    third['rational_full_gram_vectors']=[avec,bvec]
    return [first,second,third]

def attach_observation(case):
    regs=case['registers']; k=len(regs); n=3*k; residuals=[]
    def row(terms):
        r=[F(0)]*n
        for index,value in terms: r[index]+=F(value)
        residuals.append(r)
    for j in range(1,k): row([(3*j,1),(0,-1)])
    for j,reg in enumerate(regs):
        if reg['op']=='constant': row([(3*j+1,1),(0,-reg['value'])])
        elif reg['op']=='linear': row([(3*j+1,1)]+[(3*i+1,-c) for i,c in reg['terms']])
        elif reg['op']=='square': row([(3*j+1,1),(3*reg['source']+2,-1)])
    for j in case['outputs']: row([(3*j+1,1)])
    Q=zeros(n)
    for j in range(k):
        Q[3*j][3*j+2]+=F(1,2); Q[3*j+2][3*j]+=F(1,2); Q[3*j+1][3*j+1]-=1
    for r in residuals:
        for i in range(n):
            for j in range(n): Q[i][j]+=r[i]*r[j]
    case['first_observation_matrix']=Q
    case['mass_coordinate']=0
    return case

def expand_rational_columns(case):
    columns=[]
    for weight,v in case['weighted_atoms']:
        weight=F(weight);ab=weight.numerator*weight.denominator;power=0
        while ab:
            if ab&1:
                scale=F(2**(power//2),weight.denominator)
                for _ in range(1 if power%2==0 else 2):columns.append([scale*x for x in v])
            ab>>=1;power+=1
    case['rational_columns']=columns
    return case

def encode(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,dict): return {k:encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)): return [encode(v) for v in x]
    return x

def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--output',type=Path,default=ROOT/'certificates'/'quadratic_certificates.json')
    args=ap.parse_args(); obs=obstructions()
    payload=dict(schema=1,scope='Exact examples; universal statements are analytical proofs.',
                 obstructions=obs,rational_cases=[expand_rational_columns(c) for c in rational_cases(obs)],carriers=carrier_cases(),
                 cayley=cayley_cases(),circuits=[attach_observation(c) for c in circuits()])
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(encode(payload),indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(args.output)
if __name__=='__main__': main()
