"""Exact algorithm in floating-point; diagnostics are not asymptotic proofs."""
from pathlib import Path
import argparse, json, time
import numpy as np
from numba import njit

def setup(variant='balanced', gamma=1.0):
    n=7
    def E(i): return np.diag(np.eye(n)[i])
    def F(i,j):
        a=np.zeros((n,n));a[i,j]=a[j,i]=1.;return a
    a=-(F(0,1)+F(3,4))/2
    ds=[E(0),E(3),E(1)-F(0,2)/2,E(4)-F(3,5)/2,E(6)+gamma*(F(0,2)-F(3,5)),F(0,6)]
    if variant=='balanced': ds=[E(0)+E(3),*ds[2:],E(2)-E(5)]
    elif variant!='original': raise ValueError(variant)
    B=np.linalg.qr(np.array([d.ravel() for d in ds]).T)[0]
    return a,B,F

@njit(cache=True)
def run_chunk(z,a,B,nsteps,stride=1000):
    out=np.zeros((nsteps//stride,18));ii=0
    for k in range(nsteps):
        p=(B@(B.T@z.reshape(49))).reshape(7,7)
        u=a+p; R=2*u-z
        ev,Q=np.linalg.eigh(R);v=(Q*np.maximum(ev,0))@Q.T
        d=v-u;zn=z+d
        if (k+1)%stride==0:
            y=z-a-p;off=z[:6,6];doff=d[:6,6]
            out[ii,0]=k+1;out[ii,1]=np.linalg.norm(z);out[ii,2]=np.linalg.norm(d)
            out[ii,3]=np.linalg.norm(off);out[ii,4]=np.linalg.norm(doff)
            out[ii,5]=u[6,6];out[ii,6]=y[1,1]+y[4,4];out[ii,7]=z[6,6]
            out[ii,8]=off[0];out[ii,9]=off[2];out[ii,10]=z[0,0]-z[3,3]
            out[ii,11]=z[2,2]-z[5,5];out[ii,12]=np.min(ev);out[ii,13]=y[6,6]
            out[ii,14]=np.linalg.norm(v@(-R+v));out[ii,15]=z[0,0]
            out[ii,16]=z[2,2];out[ii,17]=ev[3];ii+=1
        z=zn
    return z,out

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--variant',default='balanced');parser.add_argument('--steps',type=int,default=200000)
    parser.add_argument('--epsilon',type=float,default=.1);parser.add_argument('--gamma',type=float,default=1.);parser.add_argument('--resume',action='store_true')
    args=parser.parse_args()
    if args.steps<=0 or args.steps%1000: raise ValueError('steps must be a positive multiple of 1000')
    a,B,F=setup(args.variant,args.gamma);name=f'{args.variant}_eps{args.epsilon:g}_g{args.gamma:g}'
    path=Path(__file__).parent/'diagnostics';path.mkdir(exist_ok=True);file=path/f'{name}.npz'
    if args.resume and file.exists():
        old=np.load(file);z=old['state'];data=old['data'];offset=int(old['n'])
    else: z=a+args.epsilon*F(0,6)+.3*args.epsilon*F(2,6);data=np.empty((0,18));offset=0
    start=time.time();z,new=run_chunk(z,a,B,args.steps);new[:,0]+=offset;data=np.vstack([data,new]);total=offset+args.steps
    # Atomic checkpoint preserves the previous file until the replacement is ready.
    temp=file.with_suffix('.tmp.npz');np.savez_compressed(temp,state=z,data=data,n=total,affine_anchor=a,basis=B);temp.replace(file)
    r=data[-1];k=r[0]
    ans=dict(variant=args.variant,steps=total,seconds=time.time()-start,state_scaled=r[1]/k**.25,step_scaled=r[2]*k**.75,
             off_state_scaled=r[3]*k**.25,off_step_scaled=r[4]*k**.75,dual66=r[13],off0=r[8]*k**.25,off2=r[9]*k**.25)
    print(json.dumps(ans,indent=2))
