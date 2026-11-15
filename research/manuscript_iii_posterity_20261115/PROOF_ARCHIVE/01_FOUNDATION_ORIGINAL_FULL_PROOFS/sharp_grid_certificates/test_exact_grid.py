from fractions import Fraction as F
from math import sqrt
import json
from exact_grid_certificates import *

results={"scope":"Exact rational checks; universal assertions are proved in manuscript 37.",
         "sharpness":[],"finite_accuracy":[],"descent":[],"margins":[]}
for q in [1,2,3,4,8]:
    Q=matrix([[0,F(-1,2*q)],[F(-1,2*q),1]])
    assert check_grid(Q,q)[0]
    A=matrix([[F(4*q*q,4*q*q+1),F(2*q,4*q*q+1)],
              [F(2*q,4*q*q+1),F(1,4*q*q+1)]])
    assert trace(A)==1 and pairing(Q,A)==-F(1,4*q*q+1)
    results["sharpness"].append({"q":q,"rational_lower":F(1,4*q*q+1),
        "sharp_constant_numeric":(sqrt(1+1/q**2)-1)/2,"rational_upper":F(1,4*q*q)})
    if q<=4:
        good=finite_accuracy_alternative(A,q)
        assert good["kind"]=="factor"
        results["finite_accuracy"].append({"case":f"sharp_rank_one_q{q}",**good})
    result=descent_or_separator(A,Q)
    assert result["kind"]=="negative_integer_vector"
    results["descent"].append({"case":f"sharp_negative_q{q}",**result})
# Rational CP boundary matrix with exact zero off-diagonal pattern.
A=matrix([[2,1,0],[1,2,1],[0,1,2]])
out=finite_accuracy_alternative(A,2)
assert out["kind"]=="factor"
assert out["matrix"][0][2]==0
assert all(v[0]*v[2]==0 for _,v in out["terms"])
results["finite_accuracy"].append({"case":"sparse_boundary",**out})
# Nonmember, negative-trace input, and zero-trace nonmember.
for A in [[[1,F(11,10)],[F(11,10),1]], [[-1,0],[0,0]], [[0,1],[1,0]]]:
    out=finite_accuracy_alternative(A,3)
    assert out["kind"]=="copositive_separator"
    results["finite_accuracy"].append(out)
# Positive definite, entrywise nonnegative, order-five non-CP input.
n=5
G=[[int((i-j)%n in [1,n-1]) for j in range(n)] for i in range(n)]
A=matrix([[int(i==j)+F(3,5)*G[i][j] for j in range(n)] for i in range(n)])
H=matrix([[1-2*G[i][j] for j in range(n)] for i in range(n)])
out=descent_or_separator(A,H)
assert out["kind"]=="copositive_separator" and out["pairing"] == -F(1,2)
assert out["strict_margin"]==F(191,8320)
results["descent"].append({"case":"Horn_cycle_five",**out})
horn=out
# Trace-zero candidate receives a strictly positive diagonal repair.
a0=matrix([[1,-1],[-1,1]])
r0=matrix([[0,1],[1,0]])
r=descent_or_separator(a0,r0)
assert r['kind']=='copositive_separator' and r['strict_margin']>0
assert r['pairing']<0
results['descent'].append({'case':'trace_zero_candidate',**r})
# Relative diagonal correction preserves an entire zero row.
a0=matrix([[1,F(1,2),0],[F(1,2),1,0],[0,0,0]])
eps=F(1,2)
b0=[[a0[i][j]+(eps*a0[i][i] if i==j else 0) for j in range(3)] for i in range(3)]
r=grid_cone_phase_one(b0,2)
assert r['kind']=='factor' and all(v[2]==0 for _,v in r['terms'])
results['finite_accuracy'].append({'case':'relative_diagonal_with_zero_row',**r})
for n in [2,3,4]:
    P=matrix([[F(1) if i==j else F(-1,2) if abs(i-j)==1 else F(0)
               for j in range(n)] for i in range(n)])
    result=strict_margin(P,max_q=8)
    assert result["kind"]=="strict_copositivity"
    results["margins"].append({"n":n,**result})
with open('EXACT_GRID_RESULTS.json','w') as f:
    json.dump(results,f,indent=2,default=str)
print(json.dumps({"status":"PASS", "sharpness_cases":len(results['sharpness']),
      "phase_one_cases":len(results['finite_accuracy']),
      "descent_cases":len(results['descent']),"strict_margin_cases":len(results['margins']),
      "horn_cutoff":horn['q'],"horn_pairing":str(horn['pairing'])},indent=2))
