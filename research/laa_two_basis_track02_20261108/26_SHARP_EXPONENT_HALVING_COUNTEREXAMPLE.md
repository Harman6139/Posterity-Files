# Milestone 26 — exact exponent HALVING in the universal two-zero + positive-anchor construction

Date 2026-11-08. This gives an explicit, fully algebraic and quantitatively sharp counterexample to any claim that the universal Naimark two-zero construction (Milestone 21), even after strictly-positive signed-anchor composition (Milestone 24), preserves every non-Lipschitz PSD recovery modulus. The source exponent 1/2 becomes 1/4, and BOTH exponents are attained against ALL PSD competitors of unrestricted rank. The source is a four-by-four uniquely solvable PSD GRAPH-COMPLETION problem. The bad curves have constant rank two. This is an obstruction to the CURRENT CONSTRUCTION, not an impossibility theorem for other two-basis architectures.

## 1. Exact source frame and unique graph completion

Let d=4 and e_1,...,e_4 be the standard basis of R^4. Set eta=zeta=1/4, theta=sqrt(1-2eta²)=sqrt(7/8). For h in {1,3} and signs s,t in {+1,-1}, define
  g_(h,s,t)= (e_h+s eta e_2+t zeta e_4)/2.
Add two further frame columns
  g_2=theta e_2,  g_4=theta e_4.
There are M=10 columns. Let G be the 4-by-10 matrix of these columns.

By independent sign averaging,
  sum_(s,t) g_(h,s,t)g_(h,s,t)^T=e_h e_h^T+eta² e_2e_2^T+zeta²e_4e_4^T.
Therefore
  GG^T=I_4.
All 10 columns are nonzero and have norm strictly less than one.

Sign-Fourier inversion isolates, for each h=1,3, the directions
  e_h e_h^T+eta²e_2e_2^T+zeta²e_4e_4^T,
  E_(h,2)=e_h e_2^T+e_2 e_h^T,
  E_(h,4), and E_(2,4).
The two pure-coordinate columns isolate e_2e_2^T and e_4e_4^T. Hence
  W=span{g_jg_j^T}
   ={H in S^4:H_(1,3)=0},
  dim W=9.
(The symbol H_(1,3) denotes one matrix entry, not a source variable constraint.)

Define the inverse map M_G(Z)=(g_j^T Z g_j)_j. Since W^perp=span(E_(1,3)), the target
  Z_*=diag(1,1,0,0)
is the UNIQUE PSD completion of its data: any exact competitor equals Z_*+a E_(1,3); its (1,3) principal 2-by-2 block [[1,a],[a,0]] is PSD only for a=0.

The source local exponent is exactly 1/2, attained against unrestricted-rank PSD competitors. For residual rho<=1, linear inversion on W bounds every matrix entry of Z-Z_* except (1,3) by C rho. In particular Z_33<=C rho, Z_11<=1+C rho. PSD Cauchy-Schwarz gives |Z_13|<=sqrt(Z_11 Z_33)<=C' sqrt(rho). Thus ||Z-Z_*||_F<=C''sqrt(rho). For sharpness take
  w(t)=sqrt(1-t²)e_1+t e_3,
  Z(t)=w(t)w(t)^T+e_2e_2^T, 0<t<1.
Then rank Z(t)=2 for all t, tr Z(t)=2, and
  Z(t)-Z_* = t sqrt(1-t²) E_(1,3)+t²(e_3e_3^T-e_1e_1^T).
Because W annihilates E_(1,3),
  M_G(Z(t)-Z_*)=t² r,
where r_j=-1/4 for the four h=1 sign columns, +1/4 for the four h=3 sign columns, and zero for g_2,g_4. Moreover
  ||Z(t)-Z_*||_F=sqrt(2) t.
Thus alpha_source=1/2 exactly.

## 2. A special cross vector cancels the source error in BOTH basis lists

Define the length-M vector c by
  c_(1,s,t)=+s/(4eta)=s,
  c_(3,s,t)=-s/(4eta)=-s,
  c_(g2)=c_(g4)=0.
Direct sign summation gives Gc=0:
  sum_(s,t) c_(h,s,t)g_(h,s,t)
   = [(-sign_h)/(4eta)] sum_(s,t) s*(e_h+s eta e2+t zeta e4)/2
   =-sign_h e2/2,
where sign_1=-1 and sign_3=+1, and these contributions cancel.
Also ||c||²=8.

Let z=M-d=6 and choose ANY real 6-by-10 matrix K with orthonormal rows spanning ker G, so KK^T=I_6, KG^T=0, K^T K=I_10-G^T G. Put P=G^T G and form the canonical two-zero construction from Milestone 21:
  F_0=[G, 0_(4x6)] in R^(4x16),
  U_0=[[K^T,P],[0_(6x6),K]] in O(16).
Define the embedded source vector phi=F_0^T e_2 and the EXTERIOR vector
  v=(c,Kc) in R^10 direct-sum R^6.
Then F_0 v=Gc=0, so v in ran(F_0^T)^perp, and
  ||v||²=||c||²+||Kc||²=16.

The first-basis nonzero coordinate j has
  <e_j,phi>=<g_j,e2>,  <e_j,v>=c_j.
The second-basis nonzero coordinate 6+j is u_j=(P e_j,K e_j), with
  <u_j,phi>=<g_j,e2>,  <u_j,v>=c_j,
because Pc=0 and K^T Kc=c. All zero-coordinate basis vectors are perpendicular to phi.

For every j, a direct evaluation gives
  2 <g_j,e2> c_j=-r_j.
For the h=1 group this is 2*(s eta/2)*(s/(4eta))=+1/4=-r_j; for the h=3 group it is -1/4=-r_j; for the pure-coordinate columns both sides are zero.

Consequently the first-order exterior cross block
  t²(phi v^T+v phi^T)
has measured NONZERO-coordinate data exactly -t² r in EACH basis, canceling the source curve's measured change. Every measured zero coordinate receives zero cross data.

## 3. Explicit PSD rank-two curve with fourth-order data residual

Define
  Y_*=F_0^T Z_* F_0 = (F_0^T e1)(F_0^T e1)^T +phi phi^T,
and for 0<t<1,
  Y(t)=(F_0^T w(t))(F_0^T w(t))^T
       +(phi+t²v)(phi+t²v)^T.
Each Y(t) is PSD of rank EXACTLY TWO, because its two constituent vectors are orthogonal: w(t) is orthogonal to e2 and F_0v=0. Its source compression satisfies
  F_0Y(t)F_0^T=Z(t).

Expanding the difference gives
  Y(t)-Y_*=F_0^T(Z(t)-Z_*)F_0
             +t²(phi v^T+v phi^T)+t^4 vv^T.
By Section 2, the first two contributions cancel EXACTLY in both orthonormal-basis data lists, including all zero slots. Therefore
  A_(U0)(Y(t))-A_(U0)(Y_*)=t^4 A_(U0)(vv^T).    (3.1)
The coefficient is nonzero: the first-basis diagonal sums to tr(vv^T)=16. It also satisfies
  ||A_(U0)(vv^T)||_2>=16 sqrt(2/16)=4sqrt(2),
while ||A_(U0)(vv^T)||_2<=sqrt(2)||v||²=16sqrt(2).
Thus the full measurement residual is EXACTLY Theta(t^4), independently of the orthonormal completion K.

Meanwhile the Frobenius error is at least the compressed error:
  ||Y(t)-Y_*||_F>=||Z(t)-Z_*||_F=sqrt(2)t.
Thus no local Hölder exponent alpha>1/4 can hold at the unique full-ambient PSD target Y_*.

To prove attainment AT 1/4 against ALL ambient PSD competitors, use Milestone 21's quantitative near-fibre theorem:
  omega_zero(delta)<=omega_source(C sqrt(delta))+C sqrt(delta).
We proved omega_source(rho)<=C' sqrt(rho) above, so
  omega_zero(delta)<=C'' delta^(1/4)
for sufficiently small delta. The exact full-ambient fibre is unique by the two-zero exposing argument. Therefore
  **alpha_zero=1/4 (attained)**.

Even though the source graph measurement is Lipschitz in all its nine measured directions apart from its PSD singularity, the doubled-basis encoding introduces a genuine additional facial reduction step and doubles the square-root instability.

## 4. Strictly positive final two-basis observations retain the sharp 1/4 obstruction

Apply Milestone 24's SECOND signed-anchor two-basis dilation to the complete intermediate two-basis problem (order n=16). Its universal frame consists of two half-scaled ONBs and one duplicated weight-4 column. The signed-anchor output has order
  N_final=5n+4=84.
Every entry of the new orthogonal transition U_final can be selected nonzero; every encoded target observation is strictly positive, even though the intermediate problem had zero outcome slots. The final target
  X_*=F_1^T(Y_* direct-sum [1])F_1
has rank rank(Y_*)+1=3, and exact PSD fibre {X_*} among ALL ambient ranks. The final encoder is isometric on differences and is a fixed linear map plus a fixed positive anchor.

Milestone 24's signed even/odd transfer bounds give
  omega_final(delta)<=C omega_zero(C delta)+C sqrt(delta)
                     <=C' delta^(1/4).
The embedded rank-two curve produces a rank-three PSD final curve with Frobenius distance >=sqrt(2)t and measured residual Theta(t^4) (the two measured lists are linearly equivalent to all intermediate measurements on the embedded face). Hence no exponent alpha>1/4 is valid.

Therefore:
  **alpha_final=1/4 (attained)**,
while the original source exponent was 1/2.

This is a strictly-positive-data, all-overlap-nonzero, rank-three final two-basis counterexample showing that composing an exact two-zero frame dilation with a signed positive anchor does NOT preserve non-Lipschitz recovery exponents. It is distinct from the canonical graph-reflection embedding, which DOES preserve this graph source's exponent.

## 5. Why this does not refute general sharp universality

The counterexample rules out claiming that Milestones 21 and 24 automatically preserve any non-Lipschitz source modulus. It does NOT prove that no other two-basis representation of the same graph/source can preserve alpha=1/2. In fact the earlier signed-reflection graph lift does preserve non-Lipschitz moduli: the issue here is the specific universal frame compiler with independent exterior cross blocks.

The source graph is K_4 with the edge {1,3} removed, which is chordal. Hence even a sparse, single-step completion can acquire a second square-root loss through this universal but non-sharp encoding. The exact obstruction is the rank-one support-to-exterior cross vector v constructed above, not an abstract worst-case dimension count.

## Hostile audit

- The 10 frame columns are explicitly Parseval with a nine-dimensional projector span; no hidden unmeasured source directions beyond E_(1,3).
- The original source target is unique among ALL PSD matrices; the zero (3,3) diagonal together with the missing (1,3) entry makes the uniqueness argument exact.
- Both source and ambient bad curves preserve trace to order t², and the source curve preserves trace EXACTLY. The ambient exterior repair t^4 vv^T increases trace only at fourth order; there is no lower-order trace obstruction.
- The bad Y(t) is PSD by an explicit rank-two Gram factorization, without invoking a possibly invalid Schur complement at singular target.
- The cancellation identities hold for BOTH bases and include zero slots, not merely the first basis.
- The coefficient A(vv^T) is provably nonzero from its measured trace and has explicit uniform lower and upper constants.
- The local exponent upper bound comes from the fully all-ambient near-fibre theorem, not a fixed-rank analysis.
- The positive final construction makes all observations strictly positive without changing the fourth-order embedded data scaling, and the final target is unique among unrestricted-rank PSD competitors.
- This establishes SHARPNESS OF THE POSSIBLE ONE-HALF EXPONENT LOSS for the two-zero+anchor architecture, NOT an impossibility for all possible two-basis reductions.
