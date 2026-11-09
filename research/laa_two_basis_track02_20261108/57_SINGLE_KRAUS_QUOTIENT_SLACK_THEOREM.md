# Milestone 57 — generic dimension/slack obstruction for ALL single-Kraus two-basis PSD quotients, without an encoder

Research Track 02, 2026-11-09. This theorem strengthens the earlier positive-retract and Kraus/slack bounds in a direction critical for the unresolved near-quadratic many-to-one problem: it assumes NO source encoder AT ALL (not even affine, not even positive), and allows a full, arbitrarily large family of decoder-invisible auxiliary feasible matrices. The decoder must be a fixed POSITIVE rank-one Kraus map Y↦CYC^T. No full-rank ambient lift, reflection, or other basis geometry is assumed.

## 1. Theorem and exact hypotheses

Let m>=3, D_m=m(m+1)/2, choose an integer 1<=s<=D_m-2, and write ell=D_m-s. Let L be an ell-dimensional subspace of S^m containing I_m, and choose a linear source measurement map A with range(A*)=L. Fix b=A(I_m), so
  F_b={X>=0:A(X)=b}
is compact, has a positive-definite point I_m, and has affine dimension s.

Consider ANY two real orthonormal bases of R^N and their diagonal measurement map B:S^N→R^(2N), a target datum y, and a REAL matrix C of size m-by-N such that the positive decoder
  D(Y)=CYC^T
has the exact SURJECTIVITY property
  D({Y>=0:B(Y)=y})=F_b.                                  (1)
No encoder, right inverse, uniqueness of lifted solutions, rank bound on any Y, or global cone-positive affine encoding is assumed.

Let E⊂R^N be the minimum PSD support of the lifted fibre T={Y>=0:B(Y)=y}; put d=dim E. The compressed two-basis rank-one measurement span W⊂S^d has dimension q. Put
  a=dim ker(B|S(E))∩ker(D|S(E)),
the affine dimension of decoder-invisible feasible directions.

**Theorem A (generic parameter/slack inequalities).** For generic rational trace-controlled measurement spaces L containing I (in the open dense full-measure sense), EVERY representation (1) must satisfy
  q(d-1) >=g:=(ell-1)s,                                 (2)
  q=D_d-s-a <=2N-1,                                    (3)
  m<=d<=N.                                             (4)
Here D_d=d(d+1)/2. For a fixed m,N,d,q the exceptional representable source spaces violating (2) form a proper lower-dimensional semialgebraic subset of the source measurement Grassmannian.

In particular, if N<=C m² for a fixed C>0 and ell,s=Theta(m²), then
  d=Omega_C(m²),   a=Omega_C(m⁴).                       (5)
If instead a<=A m² for a fixed A>0, then
  N=Omega_A(m^(8/3)).                                  (6)
These bounds hold with a purely positive single-Kraus decoder even though an affine or globally positive encoder may NOT exist. They exclude a "small compressed support + nonlinear positive fibre selection" shortcut when using one canonical matrix block for decoding.

## 2. Exact tangent-surjection identity

Let M be the restriction of the two-basis measurement map to S(E). Every Y in T is supported on E by definition. There exists Y0 in T positive definite on E: average finitely many feasible matrices whose ranges span E; PSD positivity ensures the average's range equals their span.

We first show the exact linear equality
  D(ker M)=ker A.                                       (7)

Soundness: for any H in ker M and sufficiently small real t, Y0+tH>=0 on E and remains in T. Hence A(D(Y0+tH))=b for both signs, giving A(D(H))=0.

Completeness: for any K in ker A, choose epsilon>0 small enough that I_m+/-epsilon K>=0. Both lie in F_b and by (1) have preimages Y_+,Y_- in T. Then H=(Y_+-Y_-)/(2epsilon) is in ker M and D(H)=K. Thus (7) holds.

Consequently the decoder-invisible subspace has dimension
  a=dim ker M -dim ker A=(D_d-q)-s,
which is (3). Taking orthogonal complements of (7),
  L=(D(ker M))^perp
   ={H in S^m:D*(H) in W}.                             (8)
This is an exact identity: no positivity of a source encoding is being assumed.

## 3. Normalize the arbitrary single-Kraus decoder for FREE

Restrict C to E and regard it as an m-by-d matrix C_E. Because the source fibre contains I_m, there is Y_I in T with C_E Y_I C_E^T=I_m. Thus C_E has full row rank m and d>=m.

There exists a fixed invertible matrix R in GL_d(R) such that
  C_E R=[I_m 0_(m x(d-m))].
Conjugating all compressed feasible matrices by R^-1 and all compressed rank-one projectors by R^T produces an equivalent linear-algebraic description: the transformed measurement span W_R is STILL SPANNED BY q RANK-ONE PSD PROJECTORS, and the transformed decoder is exactly
  pi(Z)=Z_(top m-by-m).
In particular (8) becomes
  L={H in S^m:[H 0;0 0] in W_R}.                      (9)

CRUCIAL: although the actual compressed bases need not remain orthonormal after this congruence, their projectors remain rank one. We use the LARGER family of all rank-one-generated q-dimensional spaces W_R as a relaxation, so the dimension lower bound remains valid.

The formula (9) contains NO unknown coefficients of C, no source encoder, and no auxiliary-positive-map parameters. This is what eliminates the tmd term present in the general Kraus-rank-t tradeoff of Milestone 09 when t=1.

## 4. Semialgebraic Grassmannian dimension proof

The parameter space of ell-dimensional source measurement spaces L containing I_m has real dimension
  g=(ell-1)(D_m-ell)=(ell-1)s.                          (10)

Every q-dimensional rank-one-generated subspace W_R⊂S^d has q linearly independent rank-one PSD generators v_jv_j^T. Scaling v_j changes no generator line, so such W_R are parametrized by q points in RP^(d-1). Their real semialgebraic family has dimension at most
  q(d-1).                                               (11)

On the locus where (9) has dimension ell and contains I_m, the rule
  W_R ->{H:[H 0;0 0] in W_R}
is a semialgebraic Grassmannian map: its matrix entries are obtained by solving linear equations in rank-one projector coordinates. Therefore its image has semialgebraic dimension at most q(d-1).

If q(d-1)<g, the image cannot contain a nonempty open subset of the g-dimensional source Grassmannian. Its closure is a proper semialgebraic subset. For any fixed m,N there are only finitely many integers d,q, so the union of all representable source L violating (2) is lower-dimensional. Its complement contains a nonempty open set and hence rational source spaces, since rational Grassmannian charts are dense. This proves the generic inequality (2).

The proof is unaffected by target-dependent C, bases, target data y, or the existence of many feasible Y per original X, because all those data disappear after (9).

## 5. Explicit asymptotic consequences

Take s=floor(D_m/2), ell=D_m-s, so
  g=(ell-1)s=m⁴/16+O(m³).

From (2)-(3), q<=2N-1 and d<=N give
  g<=q(d-1)<2N²,
so even with arbitrarily large auxiliary slack a one has the unconditional quadratic constant-order obstruction
  N>=sqrt(g/2)= (1/(4sqrt2)+o(1))m².

More strongly suppose N<=C m². Then (2) gives
  d>=1+g/q>=1+g/(2N-1)
     >=(1/(32C)-o(1))m².
Since a=D_d-q-s and q<=2Cm², s=O(m²), this implies
  a>= (1/(2048 C²)-o(1))m⁴.
Thus (5) is explicit for sufficiently large m.

If a<=A m², then (3) gives
  d(d+1)/2=q+s+a<=2N-1+(A+1)m²
and hence d<=sqrt(4N+2(A+1)m²)+1. Consequently
  g<=q(d-1)<2N[sqrt(4N+2(A+1)m²)+1].
To reach g=Theta(m⁴) requires N=Omega_A(m^(8/3)); this proves (6).

## 6. Consequences and exact limits

- A globally positive rank-one Kraus decoder is automatically a positive principal compression after a fixed congruence on the minimum feasible support. The decoder normalization does NOT require a positive right inverse on the original source cone.
- Therefore a generic dense SDP cannot be represented through a small order-O(m) compressed source support using ANY single-Kraus positive decoder, even when arbitrary nonlinear witness selection and giant auxiliary feasible sets are permitted.
- If one insists on N=O(m²), this architecture must have d=Omega(m²) and a=Omega(m⁴): a very large decoder-invisible spectrahedral fibre. Such a giant-slack construction is NOT ruled out.
- General CP decoders with t>=2 cannot be normalized to a single principal block. For t=Theta(m²), their matrix parameters can have enough dimension to defeat this Grassmannian argument. The surviving universal frontier must use giant auxiliary slack, genuinely high-Kraus/non-Jordan decoding, or a decoder without the globally positive single-Kraus structure.
- This theorem does not assert that arbitrary weak SDP optimization reductions are impossible at O(m²+p); exact SURJECTIVE recovery of every source feasible point is a stronger requirement.
- No uniform polynomial-bit complexity or target support singular-gap bound is claimed. The result is pure exact real-algebraic geometry and applies already before conditioning is considered.
