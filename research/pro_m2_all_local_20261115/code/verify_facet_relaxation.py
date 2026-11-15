#!/usr/bin/env python3
"""Exact additional facet-product check; no generator imports."""
from fractions import Fraction as Q
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]

def test(c):
    n=int(c['n']);N=int(c['N']);A=[[Q(x) for x in row] for row in c['target']]
    G=[]
    for j in range(1,n-1):
        for sign in (-1,1):
            v=[Q(0)]*n;v[0]=1;v[j]=sign;G.append(v)
    G.append([Q(0)]*(n-1)+[Q(1)])
    low=Q(1,20*n*N*N);eps=Q(1,2000*n*n*N*N)
    for u in G:
        for v in G:
            value=sum(u[i]*A[i][j]*v[j] for i in range(n) for j in range(n))
            if value<low:raise ValueError('facet-product bound fails')
    if not 2*eps<low:raise ValueError('robustness gap fails')
    for crossing in c['crossings']:
        s=int(crossing['k'])+1
        if N<100*s:raise ValueError('ray-correction cutoff fails')
        if -3*N+Q(N*N,6*s)<=0:raise ValueError('original ray correction could separate')
        if -3*N+Q(N*N,15*s)<=0:raise ValueError('transformed ray correction could separate')
    return (2*n-3)**2

def main():
    data=json.loads((ROOT/'certificates/all_local_certificates.json').read_text())
    entries=sum(test(c) for c in data['cases'])
    report=dict(status='PASS',families=len(data['cases']),facet_entries_checked=entries,
                ray_correction_cases=sum(len(c['crossings']) for c in data['cases']),
                scope='Exact finite checks of the universal analytical facet-product and ray-correction corollaries')
    (ROOT/'certificates/facet_relaxation_verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
if __name__=='__main__':main()
