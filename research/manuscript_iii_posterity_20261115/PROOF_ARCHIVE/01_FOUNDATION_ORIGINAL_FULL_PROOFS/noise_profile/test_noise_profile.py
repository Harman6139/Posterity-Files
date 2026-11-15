"""Reproducible exact identities and numerical implementation diagnostics.

Run: OPENBLAS_NUM_THREADS=1 python test_noise_profile.py
Dependencies: NumPy and SymPy. Output is not a universal proof.
"""
from __future__ import annotations
import json
from math import sqrt
from pathlib import Path
import numpy as np
import sympy as sp
from noise_profile import PowerTail, ExponentialTail, HardPair, project_ball, accelerated_batched, certified_budget


def exact_checks() -> dict:
    x, R, delta, sign, sample = sp.symbols("x R delta sign sample", real=True)
    h = delta*(2*sp.sqrt((x/R)**2+3)-sign*x/R-3)
    hp, hm = h.subs(sign, 1), h.subs(sign, -1)
    assert sp.simplify(hp.subs(x, R)) == 0
    assert sp.simplify(hm.subs(x, -R)) == 0
    assert sp.simplify(sp.diff(hp-hm, x)+2*delta/R) == 0
    l = delta*(2*sp.sqrt((x/R)**2+3)-3)-sample*x
    assert sp.simplify(sp.diff(l, x, 2)-sp.diff(hp, x, 2)) == 0
    # 6*(2*sqrt(3)-3)>1, using exact positive squaring.
    assert 12**2*3 > 19**2
    # The smooth core Hessian bound and the maximum-profile upper constant.
    assert sp.Rational(1,12)+sp.Rational(27,256) == sp.Rational(145,768)
    assert sp.Rational(145,768) < sp.Rational(1,4)
    return {"hard_pair_derivative_difference": "exact", "both_zero_core_minima": "exact",
            "sample_hessian_independent_of_sample": "exact", "lower_bound_gap_constant": "exact",
            "hidden_core_smoothness_constant": "145/768 < 1/4"}


def numerical_checks() -> dict:
    rng = np.random.default_rng(6139)
    tails = [PowerTail(v) for v in [0.25,0.5,1.0,2.0,4.0]]+[ExponentialTail()]
    profile_tests = 0
    max_surrogate_disagreement = 0.0
    max_energy_violation = 0.0
    for tail in tails:
        delta = tail.s0/8.0
        plus, minus = HardPair(tail,delta,1), HardPair(tail,delta,-1)
        C = tail.doubling+2
        for s in np.geomspace(tail.s0*1e-4, tail.s0, 35):
            z = tail.radius(s/2)
            x = 0.0 if s >= 2*(2*sqrt(3)-3)*delta else plus.radius
            point=np.array([x,z])
            assert plus.value(point) <= s*(1+1e-11)
            assert np.linalg.norm(point) <= C*tail.radius(s)*(1+1e-11)
            assert tail.radius(s/2) <= tail.doubling*tail.radius(s)*(1+1e-11)
            profile_tests+=1
        for _ in range(50):
            point=np.array([rng.normal()*plus.radius, rng.normal()*3])
            gp=plus.common_surrogate_gradient(point)
            gm=minus.common_surrogate_gradient(point)
            err=np.linalg.norm(gp-gm)
            max_surrogate_disagreement=max(max_surrogate_disagreement, float(err))
            assert err <= 1e-12*(1+np.linalg.norm(gp))
            assert np.linalg.norm(gp-plus.gradient(point)) <= plus.signal*(1+1e-10)
            assert np.linalg.eigvalsh(plus.hessian(point)).min() >= 0
        # Test the one-step energy inequality with arbitrary errors.
        qradius=5.0
        for _ in range(200):
            oldx=project_ball(rng.normal(size=2)*6, qradius)
            oldz=project_ball(rng.normal(size=2)*6, qradius)
            u=project_ball(rng.normal(size=2)*6, qradius)
            A=float(rng.uniform(0,50))
            a=(1+sqrt(1+8*A))/4
            Ap=A+a
            y=(A*oldx+a*oldz)/Ap
            nu=0.04
            bv=project_ball(rng.normal(size=2),nu)
            xi=rng.normal(size=2)*0.08
            zp=project_ball(oldz-a*(plus.gradient(y)+bv+xi),qradius)
            xp=(A*oldx+a*zp)/Ap
            lhs=Ap*(plus.value(xp)-plus.value(u))+np.linalg.norm(zp-u)**2/2
            rhs=A*(plus.value(oldx)-plus.value(u))+np.linalg.norm(oldz-u)**2/2
            rhs+=2*a*qradius*nu+a*a*np.linalg.norm(xi)**2-a*np.dot(xi,oldz-u)
            violation=(lhs-rhs)/(1+abs(lhs)+abs(rhs))
            max_energy_violation=max(max_energy_violation,float(violation))
            assert violation <= 2e-12
    budgets=[]
    for tail in [PowerTail(0.5), PowerTail(1), ExponentialTail()]:
        for sigma in [0.0,0.01,0.2]:
            epsilon=min(tail.s0,0.01)
            zero=certified_budget(tail,epsilon,sigma,0.0,parallel=16)
            result=certified_budget(tail,epsilon,sigma,zero['maximum_certified_bias'],parallel=16)
            assert result['expected_error_upper_bound']<=epsilon*(1+1e-12)
            result.update({"tail":type(tail).__name__,"beta":getattr(tail,'beta',None),"epsilon":epsilon,"sigma":sigma})
            budgets.append(result)
    return {"profile_witness_checks":profile_tests,"energy_checks":1200,
            "maximum_normalized_energy_violation":max_energy_violation,
            "maximum_common_oracle_disagreement":max_surrogate_disagreement,
            "budget_arithmetic":budgets}


def run_small_experiment() -> dict:
    tail=PowerTail(0.5)
    pair=HardPair(tail, tail.s0/2,1)
    steps,batch,sigma,radius=350,16,0.015,8.0
    values=[]
    for seed in range(24):
        rng=np.random.default_rng(5000+seed)
        def oracle(point, size):
            avg=float(rng.normal(pair.signal, sigma/sqrt(size)))
            return pair.sampled_gradient(point,avg)
        out=accelerated_batched(oracle,2,radius,steps,batch,max_samples=100000)
        values.append(pair.value(out))
    u=np.array([pair.radius, 5.0])
    assert np.linalg.norm(u)<=radius
    theoretical=pair.value(u)+4*radius**2/(steps+1)**2+sigma**2*steps/(2*batch)
    return {"scope":"Finite Monte Carlo illustration, not a rate proof or statistical certification",
            "runs":len(values),"steps":steps,"batch":batch,"sigma":sigma,"radius":radius,
            "values":values,"empirical_mean":float(np.mean(values)),
            "proved_expected_upper_bound_with_displayed_comparator":theoretical}


if __name__=="__main__":
    result={"exact":exact_checks(),"diagnostics":numerical_checks(),"illustration":run_small_experiment(),
            "scope":"Exact symbolic identities plus finite floating-point checks; universal claims are proved in manuscript 39."}
    Path("NOISE_PROFILE_RESULTS.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"exact":result['exact'],
                     "profile_checks":result['diagnostics']['profile_witness_checks'],
                     "energy_checks":result['diagnostics']['energy_checks'],
                     "energy_max":result['diagnostics']['maximum_normalized_energy_violation'],
                     "empirical_mean":result['illustration']['empirical_mean'],
                     "expected_bound":result['illustration']['proved_expected_upper_bound_with_displayed_comparator']},indent=2))
