# All-descending-rule obstruction — discovery checkpoint

2026-11-15. New independent branch from 7d385d7deacab0e453c087a447a22cbce44d95f5. Earlier files are unchanged.

## Mathematical advance under final checking

The prior release proved a unique SHADOW walk on interior MEMBERS. The stronger missing local conclusion can be proved for EVERY strictly objective-descending extreme-tangent-ray rule, on positive-definite NONMEMBERS, on a fixed nonsimplicial cone in every n>=4. A fixed integral congruence makes all target entries strictly positive. The argument does not enumerate pivot strategies.

Set r=n-2>=2, d=n(n+1)/2, and K={(t,z,y):t,y>=0, |z_i|<=t}. Use the inherited perfect vertices P_k=t^2-(2k+1)ty+(k^2+k+1)y^2, starting at P_1. Their integer minima have (t,y)=(1,0),(k,1),(k+1,1), with integer |z_i|<=t; their rank-one normals span Sym_n. Their consecutive difference F_k has ty entry -1 and yy entry 2(k+1), and the exact neighboring edge length is one.

Let a=9/10, h=29/10. Define B_N with top block N^2 diag(1,a I_r), yy=h, ty=N, z_1 y=aN, z_2 y=-aN, and all other cross entries zero. Its Schur complement is h-1-2a=1/10, so it is positive definite; lambda_min(B_N)>=1/90. Its trace is at most 2nN^2 for N>=1. Normalize A_N=B_N/(2nN^2).

The fixed Horn pullback on (t,z_1,z_2,y) is
Q=[[4,2,-2,0],[2,0,-2,-2],[-2,-2,0,2],[0,-2,2,1]].
It equals M^T H_5 M for M(t,z_1,z_2,y)=(t+z_1,t+z_2,t-z_1,t-z_2,y), so it is K-copositive. With D_N=diag(N,...,N,1), Q_N=D_N^{-T} Q D_N^{-1}, one has <Q_N,B_N>=-3/10 and ||Q_N||_F<=sqrt(57)<8. The explicit strict separator Q_N+3I/(40nN^2) has cone margin 3/(40nN^2) and negative pairing at most -3/(40nN^2) against A_N. Thus these are genuine positive-definite nonmembers, not PSD failures.

## The forcing invariant

For a tangent ray R at P_k, put h0(R)=R_tt+a sum_i R_zizi. This is the average of R[1,Z,0] with independent Z_i in {-1,0,1}, probabilities (9/20,1/10,9/20). All tested points are minimal at P_k. Thus h0>=0; equality forces the whole (t,z) principal block to vanish, because the positive-weight ternary normals span that symmetric space.

Normalize an extreme tangent ray to a primitive integral symmetric matrix. Active normals have entries bounded by 2(k+1)^2. Cofactors of d-1 independent active equations give
E_k=(d-1)! [2(k+1)^2]^(d-1),  |R_ij|<=E_k.
If h0>0, integrality gives h0>=1/10. Therefore
<B_N,R> >= N^2/10 -(28/5)N E_k -(29/10)E_k >= N^2/100
whenever N>=100 E_k.

The exposed tangent face h0=0 consists of forms 2bty+2 y ell.z+c y^2 with
c+2k(b-||ell||_1)>=0,
c+2(k+1)(b-||ell||_1)>=0.
It is generated EXACTLY by
F=(-1,0,2k+2), B=(1,0,-2k), G_i^+=(1,e_i,0), G_i^-=(1,-e_i,0)
in coordinates (b,ell,c). To verify, subtract sum |ell_i|G_i^sign and write the remaining (b-||ell||_1,c) as nonnegative alpha F+beta B, with alpha=[c+2k(b-||ell||_1)]/2 and beta=[c+2(k+1)(b-||ell||_1)]/2.

Against B_N, F has cost -2N+2h(k+1)<0, B has cost 2N-2hk>0, and G_i^+/- has cost at least N/5>0. The hypothesis N>=100E_k implies these strict signs. Hence F is the UNIQUE descending extreme ray of the ENTIRE tangent cone, not merely the unique shadow minimizer. It is not copositive (evaluate at t=k+2,y=1,z=0), and P_k cannot separate a positive-definite target because P_k is PSD.

Consequently every rule restricted to strict objective descent along extreme tangent rays must traverse at least
m_n(N)=max({0} union {k>=1:100(d-1)!2^(d-1)(k+1)^(2(d-1))<=N})
adjacent edges. For fixed n this is Omega_n(N^(1/[2(d-1)]))=2^{Omega_n(H)} where H includes input bits and log inverse distance. This is a lower bound on the restricted local walk, not on arbitrary preprocessing, nonlocal separators, jumps, or non-descending pivots.

## Robustness and global certificate

All conclusions persist under Frobenius perturbations of A_N of size at most 1/(2000 n^2 N^2), by the displayed strict ray-cost bounds, ||R||_F<=n E_k, the PSD margin, and the explicit strict separator. Under the fixed integral map S(t,z,y)=(t,z+2t*1,y+t), the normalized matrix S B_N S^T/(6nN^2) is strictly entrywise positive and PD. Since ||S||_2^2,||S^{-1}||_2^2<=5n, the ball of radius 1/(30000 n^3 N^2) remains strictly positive, PD, outside C(SK), and has the same forced local prefix. The transformed strict separator is S^{-T}(Q_N+3I/(40nN^2))S^{-1}.

Its construction and exact checking are polynomial in n and log N for this explicit family. Thus a short GLOBAL rational separator coexists with an exponential lower bound for EVERY rule in the specified local class. The proof is an arithmetic height-gap argument on one exposed tangent face, linked to the inherited rank-one normal and lattice conditioning mechanism.

This checkpoint preserves the complete mechanism and constants before packaging. Exact regeneration, independent verification, full manuscript addendum, and literature comparison are being completed in the current response. No empirical journal percentile, external review, or historical first-priority claim is made.