# Milestone 36 — order-(2m−1) CP-surjective PSD shadow with NO positive section, but a sharp fixed-basis no-go

Date 2026-11-08. A new architecture test for the remaining many-to-one near-quadratic problem. The positive quotient is unexpectedly SMALL (linear in source matrix order), much smaller than the symmetric-square shadow of Milestone 15. It has no positive linear right inverse, escaping positive-retract lower bounds. Nevertheless its pure-state fibres are generically unique, which prevents even ONE fixed ONB diagonal from being constant on a fibre that projects onto the entire trace-one PSD body. This construction is NOT a two-basis universality theorem.

## Theorem 1 — exact PSD cone surjection from order 2m−1

Let m>=2 and let V be the codimension-one real subspace of R^m tensor R² represented as m-by-2 matrices [a,b] satisfying
  a_1+b_2=0.
Its real dimension is d=2m−1. Let P_V denote the orthogonal projection onto V. For symmetric operators Y on V, define the real completely positive trace-preserving marginal
  D(Y)=Tr_aux(P_V Y P_V)
in S^m.

Then:
(i) D(S^d_+)=S^m_+ as cones, and D({Y>=0:trY=tau})={X>=0:trX=tau} for every tau>=0;
(ii) every linear source cost C is exactly pulled back to P_V(C tensor I_2)P_V on EVERY symmetric Y, with ||D||_(F->F)<=sqrt(2);
(iii) there is NO globally positive LINEAR right inverse J:S^m -> S^d to D for m>=2;
(iv) for tau>0, no nonempty PSD fibre T subset S^d_+ with a FIXED complete first-basis diagonal can satisfy D(T)={X>=0:trX=tau}. This remains true if a second ONB diagonal is also imposed.

Thus a positive CP quotient of compressed order O(m) can be surjective without possessing a positive linear section, but such a quotient need not support even one fixed-basis representation of the full density-matrix cone.

## Proof of exact surjectivity

The map D is CP because it is the ordinary partial trace restricted to an isometric subspace; its two real Kraus maps are the column extraction maps. Their adjoint squares sum to I_V, so it is trace preserving.

For any nonzero real x in R^m, put r=sqrt(x_1²+x_2²). If r>0, define the unit ancilla vector
  w(x)=(-x_2,x_1)/r.
Then the rank-one vector v=x tensor w(x) belongs to V because its selected entries satisfy
  (x tensor w)_(1,1)+(x tensor w)_(2,2)
   =x_1(-x_2/r)+x_2(x_1/r)=0.
Its partial trace is
  D(vv^T)=||w||² xx^T=xx^T.
If r=0, choose ANY unit w (for example (1,0)); then x tensor w also belongs to V and has the same partial trace. Therefore EVERY source rank-one ray admits a rank-one positive preimage.

For arbitrary X>=0, spectrally decompose X=sum_i lambda_i x_i x_i^T with unit x_i and lambda_i>=0. Take Y=sum_i lambda_i v_i v_i^T with v_i=x_i tensor w(x_i). Then Y>=0, D(Y)=X and trY=trX. This establishes (i). The adjoint of D is compression of C tensor I_2, giving (ii).

## Proof that no positive linear right inverse exists

Assume J is positive and D J=id. For each unit x with r>0, any PSD Y with D(Y)=xx^T has its range contained in
  (span(x) tensor R²) intersect V.
This follows because the expectation of D(Y) on every vector orthogonal to x is zero, and positivity forces the corresponding rows and columns of Y to vanish.

The intersection is ONE-dimensional whenever (x_1,x_2)!=(0,0): it consists of x tensor w with x_1 w_1+x_2 w_2=0. Therefore J(xx^T) is the UNIQUE PSD lift
  J(xx^T)=[x tensor w(x)][x tensor w(x)]^T,
where the coefficient is fixed by trace preservation.

Take x=e_1, e_2, x_+=(e_1+e_2)/sqrt2 and x_-=(e_1-e_2)/sqrt2. Source matrices obey
  x_+x_+^T+x_-x_-^T=e_1e_1^T+e_2e_2^T.
The unique lifts of e_1e_1^T and e_2e_2^T are respectively
  (e_1 tensor e_2)(e_1 tensor e_2)^T,
  (e_2 tensor e_1)(e_2 tensor e_1)^T.
They vanish on the vector e_1 tensor e_1.

But for x_+ and x_-, the unique unit ancilla states are (up to irrelevant sign)
  w_+=(e_1-e_2)/sqrt2,
  w_-=(e_1+e_2)/sqrt2.
The two corresponding rank-one lifts both have squared overlap 1/4 with e_1 tensor e_1, so their sum has positive expectation 1/2. This contradicts linearity of J on the equal source sums. Therefore no positive linear right inverse exists. QED.

## Proof of the no-fixed-ONB-diagonal obstruction

For every source pure trace-tau matrix tau xx^T with r>0, the preceding support argument yields a UNIQUE PSD preimage under D,
  Y_x=tau [x tensor w(x)][x tensor w(x)]^T,
which has rank ONE. As [x] ranges over the infinite projective set {x:r>0}, these are infinitely many DISTINCT rank-one PSD matrices.

If a fixed ONB diagonal in R^d is specified by a=(a_1,...,a_d), every rank-one PSD matrix with that diagonal is vv^T with v_j=+/−sqrt(a_j) (and v_j=0 when a_j=0), so there are at most 2^(k-1) distinct such matrices, where k is the number of positive a_j. Thus no single fixed diagonal can contain the infinite set {Y_x}. Since exact surjectivity D(T) onto all trace-tau source PSD matrices forces ALL Y_x into T, the desired fixed-diagonal fibre is impossible. A second basis cannot repair this. QED.

## Scope and audit

- The quotient dimension d=2m−1 is LINEAR, not quadratic; this shows lack of a positive section alone does NOT force a large compressed PSD space.
- Surjectivity is constructive for every PSD rank by a spectral sum of rank-one lifts. No linear section is claimed; it is provably impossible.
- Pure-state lift uniqueness holds for all x outside the codimension-two coordinate plane x_1=x_2=0, an infinite dense set, sufficient for the fixed-diagonal obstruction.
- The no-fixed-basis theorem concerns the ENTIRE trace-one source density body. It does not rule out b-specific proper source spectrahedra or a different CP quotient with mixed pure-state lifts.
- The real rank-one fixed-diagonal finiteness is essential; complex phase degrees of freedom would require a different argument.
- This construction sharpens the architectural alternatives from Milestones 15–18 but does not settle generic O(m²+p) two-ONB universality.
