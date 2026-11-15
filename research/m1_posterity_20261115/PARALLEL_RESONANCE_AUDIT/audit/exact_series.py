"""Exact Q(sqrt(3)) audit of the gamma=2 affine-PSD DRS chart.
Run with Python 3 and SymPy. No numerical eigendecomposition is used.
Formal identities become uniform Taylor identities by the chart proof.
"""
import sympy as sp
from sympy.polys.rings import ring
from sympy.polys.domains import QQ
from pathlib import Path
import time
K=QQ.algebraic_field(sp.sqrt(3))
varnames='x,y,B,h,ec,eg,echi,eac,eag,eq,ej,ad,bd,fa,efs'
R,*vars=ring(varnames,K)
x,y,B,h,ec,eg,echi,eac,eag,eq,ej,ad,bd,fa,efs=vars

def c(v):
    if hasattr(v,'ring'): return v
    return R.ground_new(K.from_sympy(sp.sympify(v)))
s=c(sp.sqrt(3)); b0=s/3; H0=s/4; ell=c(sp.Rational(3,4)); beta=c(sp.Rational(1,2))
N=c(sp.Rational(9,16)); kappa=9*s/8; c0=27*s/256; fs0=9*s/64
MAX=9

class S:
    def __init__(self,v=0):
        self.d={k:c(q) for k,q in v.items() if k<=MAX and q} if type(v) is dict else ({0:c(v)} if v else {})
    def __add__(self,v):
        if not isinstance(v,S): v=S(v)
        d=self.d.copy()
        for k,q in v.d.items(): d[k]=d.get(k,R.zero)+q
        return S(d)
    __radd__=__add__
    def __neg__(self): return S({k:-v for k,v in self.d.items()})
    def __sub__(self,v): return self+-convert(v)
    def __rsub__(self,v): return convert(v)+-self
    def __mul__(self,v):
        if not isinstance(v,S): v=S(v)
        d={}
        for k,a in self.d.items():
            for j,b in v.d.items():
                if k+j<=MAX: d[k+j]=d.get(k+j,R.zero)+a*b
        return S(d)
    __rmul__=__mul__
    def __truediv__(self,v):
        if not isinstance(v,S): return S({k:q/c(v) for k,q in self.d.items()})
        return self*v.inv()
    def __rtruediv__(self,v): return convert(v)*self.inv()
    def __pow__(self,n):
        if n<0: return self.inv()**(-n)
        out=S(1)
        for _ in range(n): out=out*self
        return out
    def inv(self):
        if not self.d: raise ZeroDivisionError
        low=min(self.d); a=self.d[low]
        if not a.is_ground: raise ValueError('Nonconstant leading inverse')
        rest=self.shift(-low)/a-S(1); out=S(1); term=S(1)
        m=min(rest.d) if rest.d else MAX+1
        assert m>0
        for _ in range((MAX+abs(low))//m+2):
            term=term*(-rest); out=out+term
        return (out/a).shift(-low)
    def shift(self,n): return S({k+n:q for k,q in self.d.items()})
    def coeff(self,k): return self.d.get(k,R.zero)

def convert(v): return v if isinstance(v,S) else S(v)
def zero(n,m=None): return [[S() for _ in range(m or n)] for _ in range(n)]
def eye(n): return [[S(int(i==j)) for j in range(n)] for i in range(n)]
def madd(A,B): return [[a+b for a,b in zip(aa,bb)] for aa,bb in zip(A,B)]
def mneg(A): return [[-a for a in row] for row in A]
def mmul(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),S()) for j in range(len(B[0]))] for i in range(len(A))]
def mt(A): return list(map(list,zip(*A)))
def sub(A,ii,jj): return [[A[i][j] for j in jj] for i in ii]
def minv_I_plus(V):
    out=eye(len(V)); term=eye(len(V))
    for _ in range(MAX//2+1):
        term=mmul(term,mneg(V)); out=madd(out,term)
    return out

def psi(H,b):
    cf=2*H**2/b**2-H/b
    return cf+H**2/b,H**2/b-cf/2

def jstar(x,y): return -(29*s*x*x+3*s*y*y-18*x*y)/12

def psia(j,x,y):
    rr=3*x*x; cf=2*s*j+4*rr+s*x*y
    return cf+3*j/2,2*rr-cf/2+3*j/2,rr-12*j

def model():
    t=S({1:1}); tau=t*t; H=H0+tau*h; b=b0+tau*B
    C,G=psi(H,b); C+=tau*ec; G+=tau*eg
    j=jstar(x,y)+tau*ej; Ca,Ga,Q=psia(j,S(x),S(y))
    Ca+=tau*eac; Ga+=tau*eag; Q+=tau*eq; chi=ell*y+tau*echi
    Z=zero(7); Z[0][0]=1/t+t**5*ad; Z[3][3]=1/t-t**5*ad
    Z[2][2]=b/t+t**5*bd; Z[5][5]=b/t-t**5*bd
    Z[1][1]=t*C+t**3*Ca; Z[4][4]=t*C-t**3*Ca; Z[6][6]=t**3*Q
    for i,jj,v in [(0,2,t*G+t**3*Ga),(3,5,t*G-t**3*Ga),
                  (1,2,H+tau*j),(4,5,H-tau*j),
                  (0,1,-beta+tau*fs0+t**4*(efs+fa)),
                  (3,4,-beta+tau*fs0+t**4*(efs-fa)),
                  (0,6,t*x),(2,6,t*y),(1,6,tau*chi)]:
        Z[i][jj]=Z[jj][i]=v
    A=(Z[0][0]+Z[3][3])/2; Bd=(Z[2][2]-Z[5][5])/2
    cs=(Z[1][1]+Z[4][4])/2; ca=(Z[1][1]-Z[4][4])/2
    gs=(Z[0][2]+Z[3][5])/2; ga=(Z[0][2]-Z[3][5])/2
    cf=2*(cs-gs)/3; rr=(3*Z[6][6]+8*ca+16*ga)/35
    cfa=2*(ca-ga+2*rr)/3; gfa=-cfa/2+2*rr
    U=zero(7); U[0][0]=U[3][3]=A; U[2][2]=Bd; U[5][5]=-Bd
    U[1][1]=cf+cfa; U[4][4]=cf-cfa; U[6][6]=rr
    for i,jj,v in [(0,1,-beta),(3,4,-beta),(0,2,-cf/2+gfa),
                  (3,5,-cf/2-gfa),(0,6,Z[0][6])]:
        U[i][jj]=U[jj][i]=v
    Rmat=madd([[2*a for a in row] for row in U],mneg(Z))
    return Z,U,Rmat

def project_chart(Rmat,ix,bordered):
    mat=sub(Rmat,ix,ix); PP=sub(mat,[0,1],[0,1])
    PQ=sub(mat,[0,1],list(range(2,len(ix)))); QP=mt(PQ)
    QQm=sub(mat,list(range(2,len(ix))),list(range(2,len(ix))))
    xx=S(-N); yy=S(-ell); zz=S(3*x); ww=S(4*x)
    def graph():
        return [[xx.shift(2),yy.shift(1)],[zz.shift(2),ww.shift(1)]] if bordered else [[xx.shift(2),yy.shift(1)]]
    for n in range(3):
        X=graph()
        EE=madd(madd(QP,mmul(QQm,X)),mneg(madd(mmul(X,PP),mmul(mmul(X,PQ),X))))
        rr=[EE[0][0].coeff(2*n+1),EE[0][1].coeff(2*n)]
        if n==0:
            assert rr==[R.zero,R.zero]
            if bordered: assert EE[1][0].coeff(1)==0 and EE[1][1].coeff(2)==0
            continue
        dy=rr[1]/b0; dx=(rr[0]+beta*dy)/(1+b0)
        xx+=S({2*n:dx}); yy+=S({2*n:dy})
        if bordered:
            r3=EE[1][0].coeff(2*n+1); r4=EE[1][1].coeff(2*n+2)
            dw=8*(r4+(-y+H0*4*x)*dy+beta*r3); dz=r3+beta*dw
            zz+=S({2*n:dz}); ww+=S({2*n:dw})
    X=graph()
    EE=madd(madd(QP,mmul(QQm,X)),mneg(madd(mmul(X,PP),mmul(mmul(X,PQ),X))))
    for n in range(3):
        assert EE[0][0].coeff(2*n+1)==0 and EE[0][1].coeff(2*n)==0
        if bordered: assert EE[1][0].coeff(2*n+1)==0 and EE[1][1].coeff(2*n+2)==0
    inv=minv_I_plus(mmul(mt(X),X))
    Y=mmul(madd(PP,mmul(PQ,X)),inv)
    F=eye(2)+X  # Vertical concatenation, not matrix addition.
    return mmul(mmul(F,Y),mt(F))

def calculate():
    start=time.time(); Z,U,Rmat=model(); V=zero(7)
    for ix,bord in [([0,1,2,6],True),([3,4,5],False)]:
        W=project_chart(Rmat,ix,bord)
        for i,ii in enumerate(ix):
            for j,jj in enumerate(ix): V[ii][jj]=W[i][j]
    Dstep=madd(V,mneg(U))
    for row in Dstep:
        for entry in row: assert all(k>=3 or not q for k,q in entry.d.items())
    Zn=madd(Z,Dstep)
    An=(Zn[0][0]+Zn[3][3])/2; tn=An.inv(); taun=tn**2
    bn=(Zn[2][2]+Zn[5][5])/(2*An); Hn=(Zn[1][2]+Zn[4][5])/2
    xn=Zn[0][6]/tn; yn=Zn[2][6]/tn; chin=Zn[1][6]/taun
    Cn=(Zn[1][1]+Zn[4][4])/(2*tn); Gn=(Zn[0][2]+Zn[3][5])/(2*tn)
    jn=(Zn[1][2]-Zn[4][5])/(2*taun)
    Can=(Zn[1][1]-Zn[4][4])/(2*tn**3)
    Gan=(Zn[0][2]-Zn[3][5])/(2*tn**3); Qn=Zn[6][6]/tn**3
    pp,pg=psi(Hn,bn); pa,pga,pq=psia(jn,xn,yn)
    outs={'h':((Hn-H0)/taun-h).shift(-2),
          'ec':(Cn-pp)/taun,'eg':(Gn-pg)/taun,
          'echi':(chin-ell*yn)/taun,
          'eac':(Can-pa)/taun,'eag':(Gan-pga)/taun,'eq':(Qn-pq)/taun,
          'ej':((jn-jstar(xn,yn))/taun-ej).shift(-2),
          'ad':(Zn[0][0]-Zn[3][3])/(2*tn**5),
          'bd':(Zn[2][2]-Zn[5][5])/(2*tn**5),
          'fa':(Zn[0][1]-Zn[3][4])/(2*tn**4),
          'efs':((Zn[0][1]+Zn[3][4])/2+beta-taun*fs0)/tn**4}
    for key,out in outs.items():
        for k,val in out.d.items():
            if k<0 and val: raise AssertionError((key,k,val))
    leads={key:out.coeff(0) for key,out in outs.items()}
    leads['DeltaA_over_t3']=(An-S({-1:1})).coeff(3)
    leads['DeltaB_over_t3']=((Zn[2][2]+Zn[5][5])/2-(Z[2][2]+Z[5][5])/2).coeff(3)
    leads['Delta_xi_over_t2']=(xn-x).coeff(2)
    leads['Delta_eta_over_t2']=(yn-y).coeff(2)
    leads['v66_over_t3']=V[6][6].coeff(3)
    leads['s66_over_t3']=(V[6][6]-Rmat[6][6]).coeff(3)
    assert leads['DeltaA_over_t3']==c0 and leads['DeltaB_over_t3']==c0*b0
    assert leads['Delta_xi_over_t2']==N*y and leads['Delta_eta_over_t2']==-N*x
    assert leads['v66_over_t3']==3*x*x
    assert leads['s66_over_t3']==29*s*x*x-18*x*y+3*s*y*y
    allowed={
      'ad':set('x y'.split()),'bd':set('x y'.split()),'fa':set('x y'.split()),
      'ec':set('x y ec eg'.split()),'eg':set('x y ec eg'.split()),
      'h':set('x y B h ec eg'.split()),'echi':set('x y B h'.split()),
      'eac':set('x y B h ec eg echi fa eac eag eq'.split()),
      'eag':set('x y B h ec eg echi fa eac eag eq'.split()),
      'eq':set('x y B h ec eg echi fa eac eag eq'.split()),
      'ej':set('x y B h ec eg echi fa eac eag eq ej'.split()),
      'efs':set('x y B h ec eg'.split())}
    for key,allowed_names in allowed.items():
        for index,name in enumerate(varnames.split(',')):
            if name not in allowed_names:
                assert all(mon[index]==0 for mon in leads[key]),(key,name)
    assert leads['h'].diff(h)==-kappa and leads['ej'].diff(ej)==-kappa
    P4=18*y**4-120*s*y**3*x+36*y*y*x*x-568*s*y*x**3/3-30*x**4
    S2=29*s*x*x+3*s*y*y-18*x*y
    assert N*(y*P4.diff(x)-x*P4.diff(y))==6*x*x*S2-135*s*(x*x+y*y)**2/2
    outdir=Path(__file__).resolve().parent/'results'; outdir.mkdir(exist_ok=True)
    with (outdir/'exact_leading_polynomials.txt').open('w') as f:
        for key,val in leads.items(): f.write(key+' = '+str(val.as_expr())+'\n\n')
    print('All exact series assertions passed; seconds:',time.time()-start)
    return leads

if __name__=='__main__':
    leads=calculate()
    for key,val in leads.items():
        used=[name for j,name in enumerate(varnames.split(',')) if any(mon[j] for mon in val)]
        print(key,used,'terms',len(val))
