#!/usr/bin/env python3
"""Illustrations for manuscripts 35--36; numerical limits are not proof premises.
Requires Python 3, NumPy, SciPy, SymPy. The all-order SDP target is not proved.
"""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path
import numpy as np
from scipy.optimize import brentq


def transverse_square(t: float, v2: float) -> float:
    if v2 == 0:
        return 0.0
    q = t ** -3
    r = v2 / (1 + q*q)
    for _ in range(40):
        f = r*((1+q*r)**2+q*q)-v2
        df = (1+q*r)*(1+3*q*r)+q*q
        rn = max(0.0, r-f/df)
        if abs(rn-r) <= 2e-15*max(v2, abs(r), 1e-200):
            return rn
        r = rn
    raise ArithmeticError('Scalar transverse solve did not converge')


def analytic_resolvent(z: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Tz and displacement -A(Tz), avoiding subtraction of close states."""
    u, v = float(z[0]), np.asarray(z[1:], dtype=float)
    v2 = float(v@v)
    def equation(t: float) -> float:
        r = transverse_square(t, v2)
        return t-u-(1+0.75*r*r)/t**4
    if u > 0:
        lo = u
        hi = u+(1+0.75*v2*v2)/u**4+1e-12
    else:
        lo = 1e-6
        while equation(lo) >= 0:
            lo *= 0.5
        hi = max(1.0, u+1.0)
    while equation(hi) <= 0:
        hi *= 2
    t = brentq(equation, lo, hi, xtol=1e-14, rtol=1e-14)
    r = transverse_square(t, v2)
    q = t**-3
    aa = 1+q*r
    jv = np.array([-v[1],v[0]])
    y = (aa*v-q*jv)/(aa*aa+q*q)
    jy = np.array([-y[1],y[0]])
    output = np.r_[t,y]
    displacement = np.r_[(1+0.75*r*r)/t**4, -(r*y+jy)/t**3]
    return output, displacement


def counterexample_run(iterations: int) -> dict:
    z = np.array([1.0,1.0,0.0])
    samples = set(np.unique(np.geomspace(100,iterations,32).astype(int)))
    records=[]
    phase=0.0
    max_inverse_error=0.0
    for k in range(iterations):
        new,d = analytic_resolvent(z)
        phase -= math.atan(1/(new[0]**3+float(new[1:]@new[1:])))
        max_inverse_error=max(max_inverse_error,float(np.linalg.norm(new-z-d)))
        if k+1 in samples:
            kk=k+1
            records.append({'k':kk,'state_scaled':(new/kk**0.2).tolist(),
              'step_scaled':(d*kk**0.8).tolist(),
              'scaled_step_norm':float(np.linalg.norm(d)*kk**0.8),
              't_times_transverse_norm':float(new[0]*np.linalg.norm(new[1:])),
              'phase':phase,'phase_over_t_squared':phase/new[0]**2})
        z=new
    return {'iterations':iterations,'predicted_state_coefficient':5**0.2,
      'predicted_axial_step_coefficient':5**-0.8,
      'predicted_step_norm_coefficient':math.sqrt(2)*5**-0.8,
      'largest_inverse_equation_error':max_inverse_error,'samples':records}


def rotated_soc_projection(x: np.ndarray) -> np.ndarray:
    a,b=float(x[0]),float(x[1]); zz=x[2:]
    time=(a+b)/math.sqrt(2)
    spatial=np.r_[(a-b)/math.sqrt(2),zz]
    norm=float(np.linalg.norm(spatial))
    if time>=norm:return x.copy()
    if time<=-norm:return np.zeros_like(x)
    new_time=(time+norm)/2
    new_spatial=(new_time/norm)*spatial
    return np.r_[(new_time+new_spatial[0])/math.sqrt(2),
                 (new_time-new_spatial[0])/math.sqrt(2),new_spatial[1:]]


def affine_projection(x: np.ndarray, z0: np.ndarray, free: np.ndarray) -> np.ndarray:
    return np.r_[x[0],0.0,z0+free*x[2:]]


def soc_recurrence(x: np.ndarray,z0: np.ndarray,free: np.ndarray) -> tuple[np.ndarray,np.ndarray]:
    a,b=x[:2]; s=a+b; d=b-a
    w=free*x[2:]; u=(1-free)*x[2:]; h=2*z0-u
    h2=float(h@h+w@w); D=math.sqrt(s*s+2*h2)
    if a<0 or b<0 or D==0:
        shadow=affine_projection(x,z0,free)
        step=rotated_soc_projection(2*shadow-x)-shadow
        return x+step,step
    ds=h2/(D+s); dd=-h2*d/(D*(D+s))
    q=(1-d/D)/2
    wnew=q*w; unew=u/2-d*h/(2*D)
    step=np.r_[(ds-dd)/2,(ds+dd)/2,wnew-w+unew-u]
    return x+step,step


def soc_run(dim: int,c: float,seed: int,iterations: int) -> dict:
    rng=np.random.default_rng(seed)
    z0=np.zeros(dim-2);z0[-1]=c
    free=np.zeros(dim-2);free[:max(0,(dim-3)//2)]=1
    x=rng.normal(size=dim)*5
    records=[];samples=set(np.unique(np.geomspace(100,iterations,16).astype(int)))
    max_projection_error=0.
    for k in range(iterations):
        new,step=soc_recurrence(x,z0,free)
        if k<200:
            shadow=affine_projection(x,z0,free)
            direct=rotated_soc_projection(2*shadow-x)-shadow
            max_projection_error=max(max_projection_error,float(np.linalg.norm(direct-step)))
        if k+1 in samples:
            kk=k+1; u=affine_projection(new,z0,free)
            a=u[0];q2=float(u[2:]@u[2:])
            distance=q2/(math.sqrt(a*a+2*q2)+a) if a>=0 else float(np.linalg.norm(u-rotated_soc_projection(u)))
            records.append({'k':kk,'state_scaled':(new/math.sqrt(kk)).tolist(),
              'step_scaled':(step*math.sqrt(kk)).tolist(),
              'scaled_step_norm':float(np.linalg.norm(step)*math.sqrt(kk)),
              'scaled_affine_shadow_distance':distance*math.sqrt(kk)})
        x=new
    assert max_projection_error<1e-10
    return {'dimension':dim,'c':c,'seed':seed,'iterations':iterations,
      'predicted_light_state':[c,c]+[0.]*(dim-2),
      'predicted_light_step':[c/2,c/2]+[0.]*(dim-2),
      'predicted_step_norm':c/math.sqrt(2),'predicted_shadow_distance':c/2,
      'max_recurrence_projection_discrepancy':max_projection_error,'samples':records}


def exact_checks() -> dict:
    import sympy as sp
    t,r=sp.symbols('t r',positive=True)
    B=sp.diag(3*r*r/t**3,r*r/t**3)
    cross=sp.Matrix([-3*r**3/t**4,-sp.Rational(3,2)*r/t**4])
    top=(4+3*r**4)/t**5
    schur=sp.factor(top-(cross.T*B.inv()*cross)[0])
    assert sp.simplify(schur-7/(4*t**5))==0
    s,D,d=sp.symbols('s D d',positive=True)
    sn=(s+D)/2;dn=(1+s/D)*d/2
    assert sp.simplify(sn**2-s**2-(D-s)*(D+3*s)/4)==0
    assert sp.simplify(dn-d+(D-s)*d/(2*D))==0
    q=sp.symbols('q',positive=True)
    tau=q**5-1; discounted=tau/q**4
    assert sp.simplify(q-q**-4-discounted)==0
    return {'Schur_complement':str(schur),'Lorentz_s_and_d_identities':'exact',
            'discounted_axis_identity':'exact'}


def firm_spot_checks() -> dict:
    rng=np.random.default_rng(20261114);worst=0.;res=0.
    for _ in range(100):
        x=rng.normal(size=3)*3;y=rng.normal(size=3)*3
        tx,dx=analytic_resolvent(x);ty,dy=analytic_resolvent(y)
        gap=float(np.linalg.norm(tx-ty)**2-(tx-ty)@(x-y))
        worst=max(worst,gap)
        res=max(res,float(np.linalg.norm(tx-x-dx)),float(np.linalg.norm(ty-y-dy)))
    assert worst<1e-10 and res<1e-10
    return {'largest_positive_firmness_violation':worst,'largest_resolvent_error':res,
            'scope':'100 numerical pairs, not proof of universal firm nonexpansiveness'}


def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument('--counter-iterations',type=int,default=150000)
    parser.add_argument('--soc-iterations',type=int,default=40000)
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('LAST_ITERATE_RESULTS.json'))
    args=parser.parse_args()
    if args.counter_iterations<100 or args.soc_iterations<100:
        parser.error('Iteration counts must be at least 100')
    result={'exact_identities':exact_checks(),'firm_spot_checks':firm_spot_checks(),
      'analytic_rotating_example':counterexample_run(args.counter_iterations),
      'single_Lorentz_cases':[soc_run(d,c,s,args.soc_iterations) for d,c,s in
                             [(3,1.,11),(5,.5,7),(12,2.,19)]],
      'scope':'Finite exact identities and numerical illustrations. Universal proofs are manuscripts 35 and 36. Higher-order SDP last-step theorem NOT proved.'}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'exact':result['exact_identities'],'firm':result['firm_spot_checks'],
       'counter_last':result['analytic_rotating_example']['samples'][-1],
       'soc_last':[c['samples'][-1] for c in result['single_Lorentz_cases']]},indent=2))

if __name__=='__main__':main()
