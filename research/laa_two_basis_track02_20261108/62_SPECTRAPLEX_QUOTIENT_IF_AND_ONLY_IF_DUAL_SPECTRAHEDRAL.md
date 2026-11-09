# Milestone 62 — EXACT classification of PSD spectraplex quotients, and an explicit 4×4 rational SDP that admits NO such quotient at ANY order

Track 02, 2026-11-09. Complete self-contained proof, with contextual antecedents in spectrahedral polarity (Ramana–Goldman and Blekherman–Parrilo–Thomas). This is a mathematically decisive NO-GO for generalizing Milestone 61 by sending an unconstrained trace-normalized PSD cone through an arbitrary positive linear decoder. The missing ingredient is NOT Kraus count: for the explicit example even an arbitrary non-CP positive linear map, nonlinear selection of preimages, and an arbitrarily large input PSD matrix cannot work. It does **NOT** rule out two-basis fibres with nontrivial auxiliary measurement constraints, so the unrestricted many-to-one O(m²+p) frontier is still open.

## 1. Precise spectraplex quotient theorem

Let E be a finite-dimensional real inner-product space, let K⊂E be a closed convex proper cone (closed, pointed, spanning E and with nonempty interior) and let e∈int(K*) be a strictly positive linear functional. For τ>0 define the compact base
  F_τ={x∈K : <e,x>=τ}.
For an integer n let Δ_n(τ)={Y∈S^n_+:tr Y=τ}.

**Theorem A (exact if-and-only-if, any size).** The following are equivalent:

(i) There exist n<∞ and a real LINEAR map D:S^n→E with D(Δ_n(τ))=F_τ.

(ii) K is the linear image of some full PSD cone S^n_+.

(iii) The dual cone K*⊂E is SPECTRAHEDRAL: there exist real symmetric matrices A_1,...,A_dim E with
  K*={y∈E : A(y)=Σ_i y_i A_i ⪰0}.
Moreover, when these conditions hold, D in (i) can be chosen positive (D(S^n_+)⊂K) and trace preserving relative to e:
  <e,D(Y)>=tr Y for every Y∈S^n.
If E is a linear subspace of symmetric matrices and K⊂S^m_+, this D is a globally positive linear PSD decoder. No completely positive hypothesis is needed.

### Proof of (i)⇔(ii)

If D(Δ_n(τ))=F_τ, any nonzero Y⪰0 has s=trY>0, so (τ/s)Y∈Δ_n(τ). Therefore D(Y)=(s/τ)D((τ/s)Y)∈K. Conversely every nonzero x∈K can be written x=(<e,x>/τ) x_0 with x_0∈F_τ; if x_0=D(Y_0) with Y_0∈Δ_n(τ), then x=D((<e,x>/τ)Y_0). Thus D(S^n_+)=K. The reverse implication gives a spectraplex quotient after a fixed normalization detailed below.

### Proof (ii)⇒(iii)

If D(S^n_+)=K, then by self-duality of the real PSD cone
  K*={y∈E : <y,D(Y)>≥0 for every Y⪰0}
     ={y : D*(y)⪰0}.
This is exactly a finite homogeneous LMI. (No closedness subtlety arises because K is assumed equal to the image, not merely its closure.)

### Proof (iii)⇒(ii) with CLOSED-IMAGE control and trace normalization

Write K*={y:A(y)⪰0}, with A:E→S^n linear. Since e∈intK*, for any y∈E one has e±ε y∈K* for all sufficiently small ε>0. Let U=ker A(e). If v∈U then
  0<=v^T A(e±ε y)v=±ε v^T A(y)v
for both signs. Hence v^T A(y)v=0. Both A(e±ε y) are PSD, so each annihilates v. Subtract them to obtain A(y)v=0. Thus U is the COMMON KERNEL of all A(y). Compress A to U^perp, where A(e) is positive definite. This preserves the same cone K*.

Let L=A*:S^n→E be the adjoint. For PSD Y,
  <e,L(Y)>=<A(e),Y>≥λ_min(A(e)) trY.
Therefore L(S^n_+) is CLOSED: if L(Y_j) converges with Y_j⪰0, the displayed bound keeps trY_j bounded, hence the PSD Y_j have a convergent subsequence. The dual of L(S^n_+) is
  {y:L*(y)=A(y)⪰0}=K*.
By the bipolar theorem and closedness,
  L(S^n_+)=K**=K.

Set P=A(e)^(1/2)>0 and define
  D(Z)=L(P^(-1) Z P^(-1)).
Then D(S^n_+)=K and
  <e,D(Z)>=<A(e),P^(-1) Z P^(-1)>=trZ
for EVERY symmetric Z. Consequently D(Δ_n(τ))=F_τ, proving (i) and the trace-preserving assertion.

This proves all equivalences without closure or Slater assumptions hidden in the construction.

## 2. Explicit rational 4×4 SDP counterexample

For (t,x,y)∈R³ define the injective rational linear pencil
  X(t,x,y)=
    [[t+x, y, 0, 0],
     [y, t−x, 0, 0],
     [0, 0, x, 0],
     [0, 0, 0, y]]
in S⁴.
Its PSD cone is linearly isomorphic to
  K={ (t,x,y): t≥sqrt(x²+y²), x≥0, y≥0}
    =Lorentz_3 ∩ {x≥0}∩{y≥0}.                   (1)

The usual source matrix trace is
  trX(t,x,y)=2t+x+y.
Fix τ=6 and the compact strictly feasible rational source fibre
  F={X(t,x,y)⪰0 : trX(t,x,y)=6}.
It contains X(2,1,1)>0. Choose a rational linear measurement operator A:S⁴→R⁸ whose kernel is the 2-dimensional trace-zero subspace of the 3-dimensional pencil span, and set b=A(X(2,1,1)). Then
  F={X⪰0:A(X)=b}.
The source is bounded and trace-controlled. Its conical hull is exactly the injective image of K by the pencil X, because trX is positive on every nonzero X⪰0.

**Theorem B (no unconstrained spectraplex quotient).** There is NO integer n and NO real linear decoder D:S^n→S⁴ such that
  D({Y⪰0:trY=6})=F.                             (2)
This remains impossible for arbitrary positive (including non-CP), completely positive, or non-trace-preserving decoder models. The input order n is UNRESTRICTED. The assertion is about an unconstrained trace-slice PSD input, NOT an arbitrary two-basis constrained input fibre.

### Proof: explicit NON-EXPOSED face of the dual

Write Q={(s,u,v):s≥sqrt(u²+v²)} for the 3-dimensional self-dual Lorentz cone and e_x=(0,1,0), e_y=(0,0,1). By elementary conic polarity,
  K*=Q+R_+e_x+R_+e_y.                           (3)
The sum is CLOSED: in any convergent sequence with sum coordinates bounded, the Q-component's s coordinate is bounded and its u,v components are bounded by |s|; the remaining nonnegative coordinate additions are then also bounded. Thus the ordinary intersection-duality formula needs no further closure.

The affine section at s=1 of K* is
  C={ (x,y)=(u+a,v+b):
       u²+v²≤1, a,b≥0 }
    =closed unit disk+R_+².                         (4)

Consider z=(0,−1). It is an EXTREME point of C: every member has y≥−1, and equality y=−1 forces the disk component (u,v)=(0,−1), b=0, and x=a≥0. Thus the face C∩{y=−1} is the ray {(x,−1):x≥0}, whose endpoint z is extreme.

But z is NOT EXPOSED. Any supporting line of C at z also supports the contained closed unit disk at z. The disk has the UNIQUE supporting tangent line y=−1 there. That line exposes the ENTIRE positive horizontal ray, not the singleton {z}. Therefore {z} is a non-exposed face of C.

Every spectrahedron has only EXPOSED faces. Elementary proof: for S={z:M(z)⪰0}, choose x in the relative interior of any face F and let P be the orthogonal projector onto ker M(x). The nonnegative linear/affine functional z↦tr(PM(z)) vanishes precisely on the minimal face containing x, which equals F. Thus every face of S is exposed.

Hence C is NOT a spectrahedron. Were K* spectrahedral, its affine section {s=1} would itself be a spectrahedron, contradiction. Therefore K* is NOT spectrahedral. By Theorem A, K and its 4×4 PSD pencil image cannot be the image of any full PSD cone under any linear map, and F cannot be the decoder image of any spectraplex. QED.

## 3. Implication for the Milestone 61 coherent-CP route

Milestone 61 successfully constructs a coherent CP map D_arrow taking an entire order-m spectraplex onto a bounded rational arrow SDP fibre, and composes it with the maximally-entangled TWO-basis trace-only template to obtain N=2m² exact many-to-one recovery. Theorem B shows that this strategy CANNOT be universal, even if one increases the input PSD order arbitrarily or replaces the CP map by an arbitrary positive linear decoder: the 4×4 source F above has a non-spectrahedral dual cone.

**Exactly which source cones support this route?** Theorem A gives the COMPLETE answer: those and only those whose DUAL cone is spectrahedral. This is a necessary-and-sufficient, representation-independent classification of the spectraplex-quotient architecture.

It does NOT refute the full two-basis frontier. A genuine two-basis fibre T={Y⪰0:diag_B1Y=a,diag_B2Y=c} is a NONTRIVIAL slice of S_+^N, and its decoder image can have a non-spectrahedral dual. To reach arbitrary SDPs with O(m²+p), a new construction must use those auxiliary diagonal constraints substantively (or use nonlinear decoding), not rely solely on a full-trace PSD cone quotient.

## 4. Audit, complexity, novelty

- The 4×4 example is rational, has a positive-definite point and fixed trace, and is an affine spectrahedron. It is not an exotic non-semialgebraic target.
- The duality argument operates in the 3-dimensional linear span E of the pencil, not in the whole S⁴. Any D with spectraplex image F automatically has its FULL positive cone image inside E, hence extends to a linear map into E; no ambient-space duality mismatch remains.
- Positivity of D follows automatically from the equality of the spectraplex image with F; it is not an extra hypothesis.
- The nonexposed extreme point is identified on an explicit affine section of the dual cone, and the unique-supporting-line argument is exact.
- The required source measurement operator exists with rational coefficients because it is simply a rational basis of the annihilator of the 2-dimensional trace-zero pencil tangent, plus trace. No invented operator coefficients are needed.
- Under the assumption K* spectrahedral, the proof constructs a finite linear PSD quotient with a globally trace-preserving normalization and avoids the usual unclosed-image pitfall by the strict positivity of A(e).
- This is a new consequence for the Track 02 frontier of classical spectrahedral-polar geometry, not a claim that spectrahedral duality or nonexposed faces were first discovered here. External novelty audit is pending.
- No polynomial size bound is asserted in Theorem A for the LMI of K*, and no unconditional O(m²+p) normal form is obtained.
