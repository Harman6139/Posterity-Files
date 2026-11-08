#!/usr/bin/env python3
"""Exact Fraction validation of all nine dense-kernel deformation cases in milestone 31.
This checks EVERY block pair originally allowed by a sharp weighted flag, not just
parent-edge supports. No floating point values, numerical optimization, or sampling.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement
T=F(1,1000)
cases={
'A':{'w':(F(0),F(3,8),F(1,2),F(3,4),F(1)), 'p':F(3,16),'t':1},
'B':{'w':(F(0),F(1,4),F(3,8),F(1,2),F(1)), 'p':F(3,16),'t':2},
'C':{'w':(F(0),F(3,7),F(5,7),F(6,7),F(1)), 'p':F(3,14),'t':1},
}
def check(name,who,wnew,orders,new_e,new_type):
    old=cases[name]['w']; p=cases[name]['p']; target=cases[name]['t']
    assert F(0)<wnew[1]<wnew[2]<wnew[3]<wnew[4]==1
    assert wnew[target]/2<p
    # Check the implication: every old permitted entry remains permitted
    # at the chosen new order, across ALL 15 unordered pairs of five blocks.
    for i,eold in [('G',p),('H1',old[1]),('H2',old[2]),('H3',old[3])]:
        order=orders[i]
        for a,b in combinations_with_replacement(range(5),2):
            if old[a]+old[b]<=2*eold:
                assert wnew[a]+wnew[b]<=2*order,(name,who,i,(a,b))
    # Newly forced K3 or K2 kernel mode: verify ALL its possible blocks.
    if new_type=='K3':
        allowed=list(combinations_with_replacement(range(4),2))
        idx=3
    elif new_type=='K2_diag2':
        allowed=list(combinations_with_replacement(range(3),2))
        idx=2
    else:
        allowed=[(a,b) for a,b in combinations_with_replacement(range(3),2)
                 if (a,b) not in ((1,2),(2,2))]
        idx=1
    for a,b in allowed:
        assert wnew[a]+wnew[b]<=2*new_e,(name,who,'new',(a,b))
    assert new_e==wnew[idx]
    # No old coefficient is placed BEFORE a positive diagonal-leading level
    # while still having a permitted nonzero entry on that level.
    for i,eold in [('G',p),('H1',old[1]),('H2',old[2]),('H3',old[3])]:
        order=orders[i]
        for j in range(1,5):
            if order<wnew[j]:
                assert old[j]>eold,(name,who,'earlydiag',i,j)
    print('PASS',name,who,'old exponent',p,'new exponent',wnew[target]/2)

for name,dt in cases.items():
    w=dt['w'];w1,w2,w3=w[1:4]
    # I. An extra H in K3 has positive e3 diagonal
    if name=='A':
        x=w3-T;wn=(F(0),x/2,w2,x,F(1))
        orders={'G':wn[1]/2,'H1':wn[1],'H2':w2,'H3':w3}
    elif name=='B':
        x=w3-T;wn=(F(0),x/2,F(3,4)*x,x,F(1))
        orders={'G':wn[2]/2,'H1':wn[1],'H2':wn[2],'H3':w3}
    else:
        x=w3-T;wn=(F(0),x/2,(x/2+1)/2,x,F(1))
        orders={'G':wn[1]/2,'H1':wn[1],'H2':wn[2],'H3':w3}
    check(name,'K3-H33',wn,orders,x,'K3')
    # II. An extra H in K2 has positive e2 diagonal
    if name=='A':
        y=w2-T;wn=(F(0),(y+1)/4,y,(y+1)/2,F(1))
        orders={'G':wn[1]/2,'H1':wn[1],'H2':w2,'H3':wn[3]}
    elif name=='B':
        y=w2-T;wn=(F(0),w1,y,w3,F(1))
        orders={'G':y/2,'H1':w1,'H2':w2,'H3':w3}
    else:
        y=w2-T;wn=(F(0),(y+1)/4,y,(y+1)/2,F(1))
        orders={'G':wn[1]/2,'H1':wn[1],'H2':w2,'H3':wn[3]}
    check(name,'K2-H22',wn,orders,y,'K2_diag2')
    # III. A J in K2 satisfies J11>0, J12=J22=0
    if name=='A':
        x=w1-T;wn=(F(0),x,w2,w3,F(1))
        orders={'G':x/2,'H1':w1,'H2':w2,'H3':w3}
    elif name=='B':
        x=w1-T;wn=(F(0),x,(x+w3)/2,w3,F(1))
        orders={'G':wn[2]/2,'H1':w1,'H2':wn[2],'H3':w3}
    else:
        x=w1-T;y=(x+1)/2;z=(y+1)/2
        wn=(F(0),x,y,z,F(1))
        orders={'G':x/2,'H1':w1,'H2':y,'H3':z}
    check(name,'K2-J11',wn,orders,x,'K2_diag1')
print('PASS: all nine *dense* deformation certificates in exact rational arithmetic')
