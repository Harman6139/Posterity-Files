#!/usr/bin/env python3
"""Exact Fraction audit: full dense-block deformation inequalities (Milestone 33).
Every unordered pair of 5 weight blocks checked for each original kernel mode.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement
T=F(1,1000)
cases={
 'D':{'w':(F(0),F(1,2),F(5,8),F(3,4),F(1)), 'p':F(5,16),'t':2},
 'E':{'w':(F(0),F(1,2),F(2,3),F(5,6),F(1)), 'p':F(5,12),'t':3},
 'F':{'w':(F(0),F(1,2),F(3,4),F(7,8),F(1)), 'p':F(7,16),'t':3},
}
def check(name,j,wn,orders):
 old=cases[name]['w'];p=cases[name]['p'];target=cases[name]['t'];e=wn[j]
 assert 0<wn[1]<wn[2]<wn[3]<wn[4]==1
 assert wn[target]/2<p
 for i,eold in [('G',p),('H1',old[1]),('H2',old[2]),('H3',old[3])]:
  for a,b in combinations_with_replacement(range(5),2):
   if old[a]+old[b]<=2*eold:
    assert wn[a]+wn[b]<=2*orders[i],(name,j,i,(a,b))
 for a,b in combinations_with_replacement(range(4),2):
  if a==0 or b==0 or (a<=j and b<=j):
   assert wn[a]+wn[b]<=2*e,(name,j,'new mode',(a,b))
 for i,eold in [('G',p),('H1',old[1]),('H2',old[2]),('H3',old[3])]:
  for k in range(1,5):
   if orders[i]<wn[k]:
    assert old[k]>eold,(name,j,'early diagonal',i,k)
 print('PASS',name,'extra PSD rank last coordinate j=',j,'new exponent=',wn[target]/2)
for name,dt in cases.items():
 o=dt['w'];a,b,c=o[1:4]
 if name=='D':
  cp=c-T;wn=(F(0),a,(a+cp)/2,cp,F(1));check(name,3,wn,{'G':wn[2]/2,'H1':a,'H2':wn[2],'H3':c})
  bp=b-T;wn=(F(0),a,bp,c,F(1));check(name,2,wn,{'G':bp/2,'H1':a,'H2':b,'H3':c})
  ap=a-T;cp=(ap+1)/2;bp=(ap+cp)/2;wn=(F(0),ap,bp,cp,F(1));check(name,1,wn,{'G':bp/2,'H1':a,'H2':bp,'H3':cp})
 elif name=='E':
  cp=c-T;wn=(F(0),a,(a+cp)/2,cp,F(1));check(name,3,wn,{'G':cp/2,'H1':a,'H2':wn[2],'H3':c})
  bp=b-T;cp=(bp+1)/2;wn=(F(0),a,bp,cp,F(1));check(name,2,wn,{'G':cp/2,'H1':a,'H2':b,'H3':cp})
  ap=a-T;bp=(2*ap+1)/3;cp=(bp+1)/2;wn=(F(0),ap,bp,cp,F(1));check(name,1,wn,{'G':cp/2,'H1':a,'H2':bp,'H3':cp})
 else:
  cp=c-T;wn=(F(0),a,b,cp,F(1));check(name,3,wn,{'G':cp/2,'H1':a,'H2':b,'H3':c})
  bp=b-T;cp=(bp+1)/2;wn=(F(0),a,bp,cp,F(1));check(name,2,wn,{'G':cp/2,'H1':a,'H2':b,'H3':cp})
  ap=a-T;bp=(ap+1)/2;cp=(bp+1)/2;wn=(F(0),ap,bp,cp,F(1));check(name,1,wn,{'G':cp/2,'H1':a,'H2':bp,'H3':cp})
print('PASS: nine dense-mode Gordan–Stiemke deformation checks')
