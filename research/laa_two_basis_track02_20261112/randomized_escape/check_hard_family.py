"""Finite diagnostics only. The universal lower bound is analytic."""
import json
from pathlib import Path
from fractions import Fraction
import numpy as np
import sympy as sp
from hard_family import HardCore, Parameters, sparse_max, smooth_absolute, tail, sufficient_dimension


def exact_checks():
    t,e=sp.symbols('t e',real=True,positive=True)
    q=3*e/8+3*t**2/(4*e)-t**4/(8*e**3)
    eqs=[sp.simplify(q.subs(t,e)-e),
         sp.simplify(sp.diff(q,t).subs(t,e)-1),
         sp.simplify(sp.diff(q,t,2).subs(t,e))]
    assert eqs==[0,0,0]
    bound=Fraction(1,12)+Fraction(27,256)
    assert bound==Fraction(145,768) and bound<Fraction(1,4)
    assert Fraction(3,4)>Fraction(24,128)
    assert Fraction(1,2)>Fraction(24,128)
    # All numerical constants use only m>=2.
    tau_ratio=Fraction(16,2048*2)
    smooth_ratio=Fraction(12,2048*2)
    assert -Fraction(1,2)+smooth_ratio <= -Fraction(15,32)
    assert 2+Fraction(1,32)+tau_ratio < Fraction(5,2)
    assert Fraction(5,2)+smooth_ratio < 3
    assert Fraction(15,32)-Fraction(1,16)-tau_ratio > Fraction(1,4)
    assert Fraction(2**19,294912)>1
    return dict(join_C2_at_boundary=True, core_hessian_bound=str(bound),
                locality_margin=True, gap_constant='1/8192',
                rounding_of_probability_constant_verified=True)


def main():
    rng=np.random.default_rng(6139)
    summaries=[]
    for beta in [0.25,0.5,1.0,2.0,5.0]:
        for m in [2,4,7]:
            d=2*m+5
            Q,_=np.linalg.qr(rng.normal(size=(d,d)))
            core=HardCore(Q[:,:m],beta)
            p=core.p
            max_value_error=0.0
            max_gradient_error=0.0
            max_hessian_error=0.0
            max_hessian=0.0
            min_hessian=1.0
            for j in range(1,m):
                for _ in range(8):
                    co=rng.normal(size=d)
                    co[:j-1]*=p.radius/(4*np.sqrt(max(j-1,1)))
                    co[j-1:m]=rng.uniform(-p.gamma/16,p.gamma/16,size=m-j+1)
                    co[m:]*=p.radius/(8*np.sqrt(d-m))
                    x=Q@co
                    v,g,h=core.evaluate(x)
                    vv,gg,hh=core.evaluate(x,prefix=j)
                    max_value_error=max(max_value_error,abs(v-vv))
                    max_gradient_error=max(max_gradient_error,float(np.linalg.norm(g-gg)))
                    max_hessian_error=max(max_hessian_error,float(np.linalg.norm(h-hh)))
                    ev=np.linalg.eigvalsh(h)
                    max_hessian=max(max_hessian,float(ev[-1]))
                    min_hessian=min(min_hessian,float(ev[0]))
            # Queries outside the visible radius have precisely radial responses.
            for _ in range(8):
                x=rng.normal(size=d); x*=4*p.radius/np.linalg.norm(x)
                v,g,h=core.evaluate(x)
                vv,gg,hh=core.wall(x)
                assert abs(v-vv)<1e-12
                assert np.linalg.norm(g-gg)<1e-12
                assert np.linalg.norm(h-hh)<1e-10
            # Negative comparison value and origin upper bound.
            xb=-p.radius/(2*np.sqrt(m))*core.u.sum(axis=1)
            fb=core.evaluate(xb)[0]
            f0=core.evaluate(np.zeros(d))[0]
            assert fb <= -15*p.gap_scale/32+1e-12
            assert f0 <= 12*p.slope*p.slope+1e-12
            # Realize a late-direction-small output; use fb as an upper bound on min F.
            co=rng.normal(size=d); co*=p.radius/(2*np.linalg.norm(co))
            co[m-1]=p.gamma/16
            x=Q@co
            gap_lower=core.evaluate(x)[0]-fb
            assert gap_lower >= p.gap_scale/4-1e-12
            assert max_value_error<1e-12 and max_gradient_error<1e-11
            assert max_hessian_error<1e-9
            assert min_hessian>=-1e-10 and max_hessian<=145/768+1e-8
            summaries.append(dict(beta=beta,m=m,dimension=d,
                                  max_value_locality_error=max_value_error,
                                  max_gradient_locality_error=max_gradient_error,
                                  max_hessian_locality_error=max_hessian_error,
                                  sampled_min_hessian_eigenvalue=min_hessian,
                                  sampled_max_hessian_eigenvalue=max_hessian,
                                  comparison_value_over_Delta=fb/p.gap_scale,
                                  output_gap_lower_over_Delta=gap_lower/p.gap_scale))
    # Test the sparse maximum at genuinely multi-active scores, not just isolated pieces.
    active_tests=[]
    for m in [2,3,8]:
        for _ in range(10):
            lam=0.7
            scores=rng.uniform(-0.08,0.08,size=m)
            val,pv,hess=sparse_max(scores,lam)
            assert abs(pv.sum()-1)<1e-10
            ev=np.linalg.eigvalsh(hess)
            assert ev[0]>-1e-10 and ev[-1]<4/(3*lam)+1e-10
            direction=rng.normal(size=m); direction/=np.linalg.norm(direction)
            dt=1e-6
            vp,pp,_=sparse_max(scores+dt*direction,lam)
            vm,pm,_=sparse_max(scores-dt*direction,lam)
            verr=abs((vp-vm)/(2*dt)-pv@direction)
            herr=np.linalg.norm((pp-pm)/(2*dt)-hess@direction)
            assert verr<1e-7 and herr<1e-6
            active_tests.append(dict(m=m,active=int((pv>0).sum()),
                                     value_derivative_error=float(verr),
                                     hessian_derivative_error=float(herr)))
    result={'exact_symbolic':exact_checks(),'construction_cases':summaries,
            'multi_active_smoothing_cases':active_tests,
            'theorem_dimensions_not_allocated':{str(t):sufficient_dimension(t) for t in [1,4,16]},
            'scope':'Exact scalar identity checks and finite floating-point construction diagnostics only; not empirical proof of arbitrary randomized-oracle lower bounds.'}
    out=Path(__file__).with_name('RESULTS.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'exact':result['exact_symbolic'],'construction_cases':len(summaries),
                      'smoothing_cases':len(active_tests),'all_passed':True,
                      'output':str(out)},indent=2))

if __name__=='__main__': main()
