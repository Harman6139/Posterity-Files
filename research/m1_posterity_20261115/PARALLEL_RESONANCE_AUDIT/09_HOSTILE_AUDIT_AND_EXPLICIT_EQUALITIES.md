# Checkpoint 09 — hostile audit and explicit equality data

2026-11-15. This checkpoint supplements 08, without claiming external peer review or historical priority. All three exact-arithmetic scripts were rerun successfully in a clean Python process. This is an audit of the proof, not a replacement of it by numerical evidence.

## 1. Twenty-two explicit rational measurements

Let A_i(X)=tr(A_i X), with the following symmetric coefficient matrices:

    A1=E00-E33, A2=E22+E55,
    A3=E11+F02-4E66, A4=E44+F35+4E66,
    A5=F01/2, A6=F34/2.

The remaining sixteen coefficient matrices are Fij/2 for the pairs, in this order,

    (0,3),(0,4),(0,5),(1,2),(1,3),(1,4),(1,5),(1,6),
    (2,3),(2,4),(2,5),(2,6),(3,6),(4,5),(4,6),(5,6).

Take b=(0,0,0,0,-1/2,-1/2,0,...,0). This gives precisely the six-dimensional affine space in 08. In particular the F02 coefficient in A3 measures 2X02, not X02. The right-hand side, all coefficient matrices, and the displayed Z0(10^5000) are rational.

The six direction generators have independent support coordinates. Their Gram equations give caff=2(cs-gs)/3 and the asymmetric system

    (3/2)cafa-2r=ca-ga,
    17r-8cafa=q+4ga.

Solving gives r=(3q+8ca+16ga)/35, exactly the projection used in all three scripts. Thus the projector really is the Frobenius orthogonal projector, not an oblique or reweighted projection.

## 2. What the symbolic calculation verifies

The executable exact_series.py builds the state and the affine projection from their definitions, solves the weighted Riccati equations coefficient by coefficient, reconstructs R_+, and only then forms the updated normalized coordinates. It verifies the claimed dependency zeros, both slow diagonal coefficients, the radial and phase coefficients, the two small diagonal overlaps, and the averaging-polynomial identity. The coefficient field is Q(sqrt(3)). It does not use floating-point eigenvectors.

Unknown graph coefficients beyond tau^2 cannot change the coefficients being checked. The missing first-column graph terms are O(t^8), the missing second-column terms O(t^7). Their first possible contributions to the off-diagonal state entries 12 and 16 are O(t^8), to top and middle diagonals O(t^7) or later, and to bottom diagonals O(t^9) or later. These are at least two t powers later than every coefficient retained in the normalized update. Laurent truncation therefore does not silently identify a high-order remainder as a low-order zero.

## 3. Holomorphic continuation: an important notation clarification

For the complex tau disk used in Cauchy estimates, all matrix formulas are continued using the ORDINARY TRANSPOSE, not conjugate transpose. They coincide with the real symmetric formulas at positive real tau. Complex conjugation would destroy holomorphy and is not being used in the proof. The Hermitian notation in earlier general cone statements is separate from this real-symmetric analytic continuation.

## 4. Explicit scaled formulas behind the majorants

Write the first reflected block in P=(0,1), Q=(2,6) coordinates as

    R_PP=[[alpha/t, Bp],[Bp,t delta]],
    R_PQ=[[t K,t xi],[hn,-tau chi]],
    R_QQ=[[qn/t,-t eta],[-t eta,t^3 D6]].

All alpha,Bp,delta,K,hn,qn,D6,chi are bounded analytic functions in the complex tau disk in 08. For the graph [[t^2 X,tY],[t^2 Z,tW]], define

    U0=X^2+Z^2, U1=Y^2+W^2, L=XY+ZW,
    Delta=1+tau U1+tau^2 U0+tau^3(U0 U1-L^2),
    a00=alpha+tau^2(KX+xi Z),
    a01=Bp+tau(KY+xi W),
    a10=Bp+tau hn X-tau^2 chi Z,
    a11=delta+hn Y-tau chi W.

The upper positive-part block is [[y00/t,y01],[y01,t y11]], where

    y00=[a00(1+tau U1)-tau^2 a01 L]/Delta,
    y01=[-tau a00 L+a01(1+tau^2 U0)]/Delta,
    y11=[-tau a10 L+a11(1+tau^2 U0)]/Delta.

These formulas make the apparent square-root factors explicit and reduce all needed coefficient bounds to analytic functions of tau. They also show directly that the updated top scale a'=t A_next stays close to 1. The updated bottom ratio is

    b_next=[b+tau^2(v22_scaled+v55_scaled)/2]/a'.

The remaining entries are reconstructed by multiplication with the graph and its transpose. There are no hidden denominators other than b, Delta, a', and the positive middle Schur factor, all bounded away from zero in the chart.

Correction to one sentence in 08, Section 5: composed expressions need NOT have phase degree at most four. What has degree four is the averaging polynomial P4. The 10^100 numerator bound is obtained by successive magnitude bounds on the immediate bounded arguments, NOT by a degree-four claim for expanded compositions. The formulas above, |X|,|Y|,|Z|,|W|<5, |Delta|>1/2, and the bounds in 08 give that conservative number without the incorrect global degree statement.

Normalized error quotients require at most three inverse powers of tau before cancellation; the charge-difference quotient requires at most four. Clearing six powers is therefore conservative. With the numerator bound 10^100 on radius r=10^-100, removable-singularity cancellation and Cauchy bound the analytic quotients by 10^700 and their first remainder coefficients by less than 10^803 on radius r/2. Squaring the step bounds and enlarging over all coordinates remains below the common constant 10^3000 used in 08. Thus the wording correction does not change the explicit starting threshold.

## 5. The spectral branch is checked, not presumed

The reflected 4-by-4 matrix has one positive and one negative eigenvalue of order t^-1, a positive Schur eigenvalue of order t with coefficient 1/8, and a negative final Schur eigenvalue of order t^3. The latter has coefficient -(S2-sqrt(3)eta^2). The strict phase annulus supplies a uniform positive lower bound on S2-sqrt(3)eta^2. Thus inertia is (2,2), and the analytic invariant graph used in the expansion is its positive spectral subspace. This explains why a formal smooth branch at gamma=1 cannot be used globally: its corresponding last sign condition fails at some phases.

## 6. All starts share the same state, but not an asserted step law

The orbit constructed in 08 supplies the common leading state without invoking any prior cosmic theorem. For arbitrary Z0', nonexpansiveness gives

    ||T^k Z0'-T^k Z0(10^5000)||_F <= ||Z0'-Z0(10^5000)||_F.

Dividing by k^(1/4) shows that EVERY orbit of this same operator satisfies Z_k/k^(1/4)->V. The nonzero transverse circle is proved for the specified rational-start family; no claim is made that every start has it. An invariant zero-seventh-column start has no such cut oscillation. This is a genuine separation between state universality and velocity universality.

## 7. Additional elementary constant checks

The coefficient identities used to identify the full step circle are

    c0/cA^3=cA/4,
    ||D||_F^2=8/3,
    ||H||_F^2=2cA^2, ||G||_F^2=2cA^2/3,
    ||G||^2=(1/4)||V||^2.

The norm-square excess is 2rstar^2 because both symmetric copies of each off-diagonal entry count in the Frobenius norm. The normalized-state chord coefficient is

    sqrt(2)N sqrt(Fstar)/(4c0 sqrt(8/3))
      =(2/3)sqrt(Fstar).

The accumulated travel ratio is sqrt(1+(64/9)Fstar). These factors were checked algebraically, not inferred from plots.

## 8. Scope after this audit

The assembled gamma=2 result is a complete proof attempt with exact supporting algebra and an explicit rational entry; the independent rerun found no coefficient or trapping-order failure. It refutes the universally quantified last-step assertion if all the displayed analytic estimates are accepted. The original gamma=1 small rational start remains unresolved. A robust parameter-family theorem, the self-contained general replacement, manuscript, literature-priority audit, and actual journal comparison are being kept as separate obligations; none is inferred from this checkpoint alone.
