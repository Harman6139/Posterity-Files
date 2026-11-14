#!/usr/bin/env python3
"""Diagnostics for milestone 40. Finite runs are not proofs of limits.
Requires numpy, scipy, sympy. Deterministic; no network access needed.
"""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path
import numpy as np
from scipy.optimize import brentq
import sympy as sp


def tail(x: float, r: int, b: float) -> float:
    if x >= 0:
        return b * (1.0 + x) ** (-r)
    return b * (1.0 - r*x + r*(r+1)*x*x/2.0)


def tail_grad(x: float, r: int, b: float) -> float:
    if x >= 0:
        return -b*r*(1.0+x)**(-r-1)
    return b*(-r + r*(r+1)*x)


def prox_tail(u: float, weight: float, r: int, b: float) -> float:
    if weight == 0:
        return u
    c = weight*b*r
    if u <= -c:
        return (u+c)/(1.0+c*(r+1))
    lo = max(0.0, u)
    hi = max(0.0, u)+c
    if hi == lo:
        return lo
    w = max(lo, min(hi, u+c/(1.0+lo)**(r+1)))
    for _ in range(20):
        fw = w-c/(1+w)**(r+1)-u
        if fw > 0:
            hi = w
        else:
            lo = w
        derivative = 1+c*(r+1)/(1+w)**(r+2)
        new = w-fw/derivative
        if not lo <= new <= hi:
            new = (lo+hi)/2
        if abs(new-w) <= 3e-15*(1+abs(w)):
            return new
        w = new
    return brentq(lambda z: z-c/(1+z)**(r+1)-u, lo, hi,
                  xtol=1e-13, rtol=1e-14)


def scalar_cases(n: int) -> list[dict]:
    results=[]
    for r in (1,2):
        b=1.0/(8*r*(r+1))
        p=1.0/(r+2)
        V=(b*r*(r+2))**p
        B=p*p*V*V/(1-2*p)
        for alpha in (0.0,0.4,1.0):
            for eta in (0.5,1.5):
                x=-1.5
                energy=0.0
                half_gap=0.0
                max_ascent=0.0
                for k in range(n):
                    old_f=tail(x,r,b)
                    if k==n//2:
                        half_gap=old_f
                    u=x-eta*alpha*tail_grad(x,r,b)
                    nxt=prox_tail(u, eta*(1-alpha),r,b)
                    if k>=n//2:
                        energy+=(nxt-x)**2/eta
                    max_ascent=max(max_ascent,tail(nxt,r,b)-old_f)
                    x=nxt
                tau=eta*n
                nxt=prox_tail(x-eta*alpha*tail_grad(x,r,b),eta*(1-alpha),r,b)
                F=tail(x,r,b)
                results.append(dict(r=r,split_alpha=alpha,eta=eta,steps=n,
                    state_ratio=x/(V*tau**p),
                    shifted_state_ratio=(1+x)/(V*tau**p),
                    velocity_ratio=((nxt-x)/eta)*tau**(1-p)/(p*V),
                    gap_ratio=F*tau**(1-2*p)/B,
                    decrement_ratio=(F-tail(nxt,r,b))/eta*tau**(2-2*p)/(p*p*V*V),
                    window_energy_over_gap_drop=energy/(half_gap-F),
                    maximum_objective_ascent=max_ascent))
                assert max_ascent<1e-11
    return results


def coupled_cases(n: int) -> list[dict]:
    # Same nonsmooth F: phi(x1)+(x1-x2)^2/2+|x1-x2|.
    b=1/16
    eta=0.25
    p=1/3
    v=(3*b/2)**(1/3)
    V=np.array([v,v])
    B=p*p*float(V@V)/(1-2*p)
    def F(x):
        d=x[0]-x[1]
        return tail(float(x[0]),1,b)+d*d/2+abs(d)
    results=[]
    for explicit_quadratic in (False,True):
        x=np.array([-2.0,3.0])
        length=0.0
        max_ascent=0.0
        for _ in range(n):
            d=x[0]-x[1]
            grad=np.array([tail_grad(float(x[0]),1,b),0.0])
            if explicit_quadratic:
                grad+=np.array([d,-d])
            u=x-eta*grad
            mean=(u[0]+u[1])/2
            diff=math.copysign(max(abs(u[0]-u[1])-2*eta,0.0),u[0]-u[1])
            if not explicit_quadratic:
                diff/=1+2*eta
            nxt=np.array([mean+diff/2,mean-diff/2])
            length+=float(np.linalg.norm(nxt-x))
            max_ascent=max(max_ascent,F(nxt)-F(x))
            x=nxt
        d=x[0]-x[1]
        grad=np.array([tail_grad(float(x[0]),1,b),0.0])
        if explicit_quadratic:
            grad+=np.array([d,-d])
        u=x-eta*grad
        mean=(u[0]+u[1])/2
        diff=math.copysign(max(abs(u[0]-u[1])-2*eta,0.0),u[0]-u[1])
        if not explicit_quadratic:
            diff/=1+2*eta
        nxt=np.array([mean+diff/2,mean-diff/2])
        vel=(nxt-x)/eta*(eta*n)**(1-p)
        results.append(dict(explicit_quadratic=explicit_quadratic,steps=n,
            scaled_state=(x/(eta*n)**p).tolist(), expected_state=V.tolist(),
            scaled_velocity=vel.tolist(),expected_velocity=(p*V).tolist(),
            velocity_relative_error=float(np.linalg.norm(vel-p*V)/np.linalg.norm(p*V)),
            gap_ratio=F(x)*(eta*n)**(1-2*p)/B,
            travel_over_displacement=length/float(np.linalg.norm(x-np.array([-2.,3.]))),
            final_nonsmooth_coordinate=float(x[0]-x[1]),maximum_objective_ascent=max_ascent))
        assert max_ascent<1e-11
    return results


def radius_of_separable_level(rs,bs,delta):
    def coordinates(s):
        out=[]
        for r,b in zip(rs,bs):
            target=s*b*r
            hi=max(1.0,target**(1.0/(r+2)))
            root=brentq(lambda x:x*(1+x)**(r+1)-target,0.,hi,xtol=1e-12)
            out.append(root)
        return np.array(out)
    def error(s):
        x=coordinates(s)
        return sum(tail(float(xx),r,b) for xx,r,b in zip(x,rs,bs))-delta
    hi=1.
    while error(hi)>0:
        hi*=2
    s=brentq(error,0.,hi,xtol=1e-10,rtol=1e-12)
    return float(np.linalg.norm(coordinates(s)))


def angular_case(n: int) -> dict:
    rs=[1,3]
    bs=[1/(8*r*(r+1)) for r in rs]
    x=np.array([0.0,0.0])
    eta=1.
    angle_windows=[0.0,0.0]
    length=0.
    for k in range(n):
        nxt=np.array([prox_tail(float(xx),eta,r,b) for xx,r,b in zip(x,rs,bs)])
        length+=float(np.linalg.norm(nxt-x))
        if np.linalg.norm(x)>0 and np.linalg.norm(nxt)>0:
            a=x/np.linalg.norm(x); c=nxt/np.linalg.norm(nxt)
            chord=float(np.linalg.norm(c-a))
            if n//4<=k<n//2: angle_windows[0]+=chord
            if n//2<=k<n: angle_windows[1]+=chord
        x=nxt
    F=sum(tail(float(xx),r,b) for xx,r,b in zip(x,rs,bs))
    radius=radius_of_separable_level(rs,bs,F)
    nxt=np.array([prox_tail(float(xx),eta,r,b) for xx,r,b in zip(x,rs,bs)])
    p=1/3
    v=(bs[0]*3)**p
    return dict(steps=n,final_state=x.tolist(),state_direction=(x/np.linalg.norm(x)).tolist(),
        scaled_velocity=((nxt-x)*n**(1-p)).tolist(),expected_velocity=[p*v,0.],
        angular_chord_length_windows=angle_windows,
        norm_over_exact_minimum_radius=float(np.linalg.norm(x)/radius),
        travel_over_displacement=length/float(np.linalg.norm(x)))


def psd_projection(Z):
    vals,vecs=np.linalg.eigh((Z+Z.T)/2)
    return (vecs*np.maximum(vals,0.0))@vecs.T


def ap_case(m: int,n: int) -> dict:
    As=[]; rhs=[]
    def entry(i,j):
        A=np.zeros((m,m))
        if i==j: A[i,i]=1
        else: A[i,j]=A[j,i]=0.5
        return A
    As += [entry(0,0),entry(0,1)]; rhs += [0.,1.]
    for i in range(1,m-1):
        As.append(entry(i,i)-entry(0,i+1)); rhs.append(0.)
    AA=np.stack(As); rhs=np.array(rhs)
    gram=np.einsum('aij,bij->ab',AA,AA)
    inverse=np.linalg.inv(gram)
    def PU(Z):
        r=rhs-np.einsum('aij,ij->a',AA,Z)
        return Z+np.einsum('a,aij->ij',inverse@r,AA)
    rng=np.random.default_rng(20261114+m)
    M=rng.normal(size=(m,m)); Z=PU((M+M.T)/2)
    half_F=None; energy=0.; max_affine=0.; angular=0.; lastq=float('inf')
    max_speed_increase=0.
    for k in range(n):
        Y=psd_projection(Z)
        err=Z-Y; F=float(np.sum(err*err)/2)
        if k==n//2: half_F=F
        nxt=PU(Y); step=nxt-Z; q=float(np.sum(step*step))
        max_speed_increase=max(max_speed_increase,q-lastq);lastq=q
        max_affine=max(max_affine,float(np.linalg.norm(np.einsum('aij,ij->a',AA,nxt)-rhs)))
        if k>=n//2:
            energy+=q
            if np.linalg.norm(Z)>0 and np.linalg.norm(nxt)>0:
                angular+=float(np.linalg.norm(nxt/np.linalg.norm(nxt)-Z/np.linalg.norm(Z)))
        Z=nxt
    Y=psd_projection(Z); err=Z-Y; F=float(np.sum(err*err)/2)
    nxt=PU(Y); step=nxt-Z
    a0=2**(m-1)-1
    p=a0/(2*(a0+1))
    r=float(np.linalg.norm(err)); stepn=float(np.linalg.norm(step)); norm=float(np.linalg.norm(Z))
    eq=np.einsum('aij,ij->a',AA,Y)-rhs
    whiten=float(math.sqrt(eq@inverse@eq))
    assert max_affine<1e-8
    assert max_speed_increase<1e-8
    return dict(order=m,steps=n,p=p,
        scaled_state=(Z/n**p).tolist(),scaled_step=(step*n**(1-p)).tolist(),
        speed_to_state_ratio=n*stepn/norm,expected_speed_to_state_ratio=p,
        step_state_cosine=float(np.sum(step*Z)/(stepn*norm)),
        energy_state_ratio=n*F/(norm*norm),expected_energy_state_ratio=p*p/(1-2*p),
        velocity_vector_relative_to_state=float(np.linalg.norm(n*step-p*Z)/(p*norm)),
        normalized_residual_ratio=r*n**(0.5-p)/(p*(norm/n**p)*math.sqrt(2/(1-2*p))),
        whitened_residual_over_cone_distance=whiten/r,
        window_energy_over_gap_drop=energy/(half_F-F),
        angular_chord_length_last_half=angular,
        maximum_affine_error=max_affine,maximum_squared_speed_increase=max_speed_increase)


def exact_checks():
    checks=[]
    for r0 in (1,2,3,4):
        r=sp.Integer(r0); b=sp.Rational(1,8*r0*(r0+1));p=1/(r+2)
        V=(b*r*(r+2))**p
        B=p*p*V**2/(1-2*p)
        assert sp.simplify(B-b*V**(-r))==0
        checks.append({'tail_power':r0,'constant_identity':'exact'})
    p=sp.Rational(1,4);v=sp.sqrt(2)
    assert sp.simplify(p*v*sp.sqrt(2/(1-2*p))-1/sp.sqrt(2))==0
    assert sp.simplify(p*p*v*v/(1-2*p)-sp.Rational(1,4))==0
    checks.append({'order_two_ap_constants':'exact'})
    return checks


def nondefinable_split_case(n: int) -> dict:
    # F=phi(x)+y^2, g=y^2/2+sin(y)/4, h=phi(x)+y^2/2-sin(y)/4.
    b=1/16; eta=0.75; p=1/3; V=(3*b)**p; B=b/V
    x=-1.; y=3.
    for _ in range(n):
        x=prox_tail(x,eta,1,b)
        u=y-eta*(y+math.cos(y)/4)
        w=u/(1+eta)
        for j in range(12):
            error=(1+eta)*w-eta*math.cos(w)/4-u
            w-=error/(1+eta+eta*math.sin(w)/4)
        y=w
    nxt=prox_tail(x,eta,1,b)
    tau=eta*n
    return dict(steps=n,eta=eta,total_objective='phi(x)+y^2',
        smooth_piece='y^2/2+sin(y)/4',nonsmooth_or_proximal_piece='phi(x)+y^2/2-sin(y)/4',
        final_y=y,velocity_ratio=((nxt-x)/eta)*tau**(1-p)/(p*V),
        gap_ratio=(tail(x,1,b)+y*y)*tau**(1-2*p)/B,
        note='Neither convex piece is globally o-minimal definable; the total objective is semialgebraic.')


def endpoint_case(n=1000):
    x=-1.0;y=1.0;b=1/16
    for _ in range(n):
        x-=2*tail_grad(x,1,b)
        y=-y
    assert abs(y)==1.0
    return dict(steps=n,stepsize=2.,global_smoothness_bound=1.,
        final_transverse_coordinate=y,transverse_step_magnitude=2.,
        objective_gap=tail(x,1,b)+y*y/2,scope='Excluded critical stepsize; nondecaying transverse motion.')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--steps',type=int,default=80000)
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('EXACT_VELOCITY_RESULTS.json'))
    args=parser.parse_args()
    if args.steps<100: raise ValueError('Use at least 100 steps.')
    result=dict(scope='Exact identities and floating-point diagnostics only. Universal claims rest on the manuscript proof.',
        exact_checks=exact_checks(),scalar_splittings=scalar_cases(args.steps),
        nonsmooth_splittings=coupled_cases(args.steps),angular_separable=angular_case(args.steps),
        semidefinite_alternating_projections=[ap_case(m,args.steps) for m in (2,3)],
        nondefinable_convex_split=nondefinable_split_case(args.steps),excluded_endpoint=endpoint_case())
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'output':str(args.output),'scalar_cases':len(result['scalar_splittings']),
        'nonsmooth_cases':result['nonsmooth_splittings'],
        'angular':result['angular_separable'],'ap':result['semidefinite_alternating_projections'],
        'scope':result['scope']},indent=2))

if __name__=='__main__': main()
