#!/usr/bin/env python3
"""Self-contained exact-rational enumeration of the first unresolved dense case.
Enumerates sparse midpoint graphs and combines with separately proved universal
bounds. DOES NOT assert dense=sparse facial depth.
"""
from fractions import Fraction as F
from itertools import product

def solve(a,b):
 n=len(b); M=[list(map(F,row))+[F(b[i])] for i,row in enumerate(a)]
 for j in range(n):
  p=next(i for i in range(j,n) if M[i][j]);M[j],M[p]=M[p],M[j]
  c=M[j][j];M[j]=[z/c for z in M[j]]
  for i in range(n):
   if i!=j:
    c=M[i][j]
    if c:M[i]=[x-c*y for x,y in zip(M[i],M[j])]
 return tuple(row[-1] for row in M)

def networks(h):
 choices=[[(a,b) for a in range(i) for b in range(i+1,h+2)] for i in range(1,h+1)]
 for pars in product(*choices):
  a=[[F(0) for _ in range(h)] for _ in range(h)];rhs=[F(0)]*h
  for i,(lo,hi) in enumerate(pars):
   a[i][i]=F(2)
   for p in (lo,hi):
    if p==h+1:rhs[i]+=1
    elif p!=0:a[i][p-1]-=1
  w=solve(a,rhs)
  if all(v<u for v,u in zip((F(0),)+w,w+(F(1),))):yield w,pars

def peeling(pars):
 h=len(pars);rem=set(range(h+2));layers=[]
 while rem!={0}:
  C=rem-{0}
  while True:
   bad={v for v in C if 1<=v<=h and all(p in rem for p in pars[v-1]) and not all(p in C for p in pars[v-1])}
   if not bad:break
   C-=bad
  assert C
  layers.append(tuple(sorted(C)));rem-=C
 return layers

def main():
 allvals=set();sparse_d4=set();witnesses={F(3,16):[],F(3,14):[]}
 for w,pars in networks(3):
  d=len(peeling(pars))
  for x in w+(F(1),):
   alpha=x/2
   if alpha<=w[0]:
    allvals.add(alpha)
    if d==4:sparse_d4.add(alpha)
    if alpha in witnesses:witnesses[alpha].append((w,pars,d))
 # Previously proved universal dense maxdepth bound: alpha<=1/4.
 dense_candidates={x for x in allvals if x<=F(1,4)}
 unknown=dense_candidates-sparse_d4
 assert len(allvals)==21
 assert sparse_d4=={F(1,q) for q in range(4,9)}|{F(1,q) for q in range(10,17,2)}
 assert unknown=={F(3,16),F(3,14)}
 assert len(witnesses[F(3,16)])==2 and len(witnesses[F(3,14)])==1
 assert all(d==3 for x in witnesses for _,_,d in witnesses[x])
 print('PASS: nu4 unconditional:',len(allvals),'exponents')
 print('PASS: constructed universal d4 reciprocals:',','.join(map(str,sorted(sparse_d4))))
 print('UNRESOLVED dense d4:',','.join(map(str,sorted(unknown))))
 for x in sorted(witnesses):
  for w,p,d in witnesses[x]:print(x,'weights',list(map(str,w)),'parents',p,'sparse depth',d)

if __name__=='__main__':main()
