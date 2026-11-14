"""Separate certificate checker; imports no producer modules.

The determinant implementation deliberately uses a different algorithm (Leibniz
expansion). Suitable for the supplied order-five certificates, not intended as a
fast general-purpose determinant routine. All mathematical checks are exact.
"""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import copy
import json
import sys


def require(condition, message):
    if not condition:
        raise ValueError(message)


def determinant(a):
    n = len(a)
    total = F(0)
    for p in permutations(range(n)):
        inversions = sum(p[i] > p[j] for i in range(n) for j in range(i+1,n))
        term = F(-1 if inversions % 2 else 1)
        for i in range(n):
            term *= a[i][p[i]]
            if not term:
                break
        total += term
    return total


def check(record):
    a = [[F(x) for x in row] for row in record['input']]
    w = [[F(x) for x in row] for row in record['separator']]
    n = len(a)
    require(n > 0 and all(len(r)==n for r in a+w) and len(w)==n, 'Bad dimensions')
    require(all(a[i][j]==a[j][i] and w[i][j]==w[j][i] for i in range(n) for j in range(n)), 'Not symmetric')
    eps = F(record['certificate']['epsilon'])
    require(eps > 0, 'Nonpositive margin')
    require(all(abs(x)<=1 for row in w for x in row), 'Box violated')
    require(sum(x*x for row in a for x in row)<=1, 'Input normalization violated')
    target = sum(a[i][j]*w[i][j] for i in range(n) for j in range(n))
    require(target <= -eps, 'Target gap violated')
    q = [[w[i][j]-(eps if i==j else 0) for j in range(n)] for i in range(n)]
    table = record['certificate']['cop_certificate_for_W_minus_epsilon_I']
    require(len(table)==(1<<n)-1, 'Incomplete support table')
    seen=set(); retained=0
    for row in table:
        s=tuple(i-1 for i in row['support'])
        require(s and s==tuple(sorted(set(s))) and all(0<=i<n for i in s), 'Invalid support')
        require(s not in seen, 'Duplicated support')
        seen.add(s); k=len(s)
        b=[[q[i][j] for j in s]+[F(-1)] for i in s]+[[F(1)]*k+[F(0)]]
        det=determinant(b)
        require(det==F(row['determinant']), 'Wrong determinant')
        if not det:
            require('x' not in row and 'value' not in row, 'Singular system falsely solved')
            continue
        x=[F(v) for v in row['x']]; t=F(row['value'])
        require(len(x)==k and sum(x)==1, 'Wrong simplex normalization')
        require(all(sum(q[i][j]*x[z] for z,j in enumerate(s))==t for i in s), 'KKT identity fails')
        if all(v>=0 for v in x):
            retained+=1
            require(t>=0, 'Negative simplex candidate')
    require(retained>=n, 'Missing singleton candidates')
    return {'order':n,'supports_checked':len(table),'feasible_candidates_checked':retained,'target_pairing':str(target),'epsilon':str(eps),'valid':True}


def main():
    file=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('five_cycle_nonlocal_certificate.json')
    data=json.loads(file.read_text())
    result=check(data)
    corrupt=[]
    x=copy.deepcopy(data); x['certificate']['cop_certificate_for_W_minus_epsilon_I'].pop(); corrupt.append(x)
    x=copy.deepcopy(data); x['certificate']['cop_certificate_for_W_minus_epsilon_I'][0]['determinant']='2'; corrupt.append(x)
    x=copy.deepcopy(data); x['certificate']['epsilon']='-1'; corrupt.append(x)
    x=copy.deepcopy(data); x['certificate']['cop_certificate_for_W_minus_epsilon_I'][0]['value']='-123'; corrupt.append(x)
    caught=0
    for x in corrupt:
        try:
            check(x)
        except ValueError:
            caught+=1
    require(caught==len(corrupt), 'Corruption was not detected')
    result['corruptions_rejected']=caught
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
