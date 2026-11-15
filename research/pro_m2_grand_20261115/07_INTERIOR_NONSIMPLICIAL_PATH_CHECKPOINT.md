# Checkpoint 007: interior nonsimplicial paths and arithmetic-depth obstruction

Date: 2026-11-15. New continuation; original checkpoints are unchanged. This is an analytic derivation being expanded and independently checked, not a priority or publication-threshold claim.

For r>=2, n=r+2, fix K={(t,z,y):t,y>=0, |z_i|<=t}. It has 2^r+1 extreme rays and is nonsimplicial. Define P_k=t^2-(2k+1)ty+(k^2+k+1)y^2 (zero z block), k>=1. Its minimal integer vectors have (t,y)=(1,0),(k,1),(k+1,1) and arbitrary integer z in [-t,t]^r. These forms are perfect: variation of z on the boxes first determines all z coefficients, and the three distinct base atoms determine the remaining binary form.

The edge P_(s-1) to P_s retains (1,0) and (s,1). Their active normals span a codimension-one subspace; the edge direction has ty entry -1 and yy entry 2s. Both endpoints are feasible and (s+1,z,1) violates beyond the next endpoint, so edge length is exactly one.

At P_1 the sum-of-all-minima anchor has tt entry a=2*3^r+4*5^r, ty entry b=3^r+2*5^r, yy entry c=3^r+5^r, and z diagonal zeta=4*3^(r-1)+10*5^(r-1). Other entries vanish. Note a=2b and 2c-b=3^r.

For integer N>=2, put T=N+1/2, U=N^2+N+1 and let A_N have binary (t,y) block [[U,T],[T,1]], z block (U/2)I, and no other entries. This is positive definite. More strongly it has an explicit rational Gram factorization: take base vectors (1,0),(N,1),(N+1,1), each with weight 1/2; for each, independently choose z_i=-t,0,t with probabilities 1/4,1/2,1/4. The resulting 3*3^r weighted atoms span Sym_n and all weights are positive, so A_N lies in the interior of CP(K), not merely its boundary. Every weight is an inverse power of two; splitting odd powers into two equal squares yields at most 6*3^r rational Gram columns of height O_r(log N).

For s=2,...,N set lambda_s=(s*c-b)/(T-s)>0. At C_s=C0+lambda_s A_N the binary mean ratio equals s. The exact base decomposition is chi_s*(1,0)^2+(c+lambda_s)*(s,1)^2, where
chi_s=a-s*b+lambda_s*(U-s*T)
      =a-b*T+s*(c*T-b)+(3/4)*lambda_s>0.
Indeed c*T-b>0 and at s=2 this is (2c-b)*T+(3/4)*lambda_2>0. Set v_s=(zeta+lambda_s U/2)/(a+lambda_s U), which lies strictly between 0 and 1. Lift each base atom by independent choices z_i=-t,0,t with probabilities v_s/2,1-v_s,v_s/2. This gives exactly C_s with positive weights whose normals span the retained facet. The only vanishing tangent ray is R_(s-1); its objective pairing is -2(T-s)<0.

The lambda_s strictly increase. Between consecutive crossings, positive combinations of the two facet certificates lie in the interior normal cone of P_s. The initial anchor is interior at P_1 and A_N itself is interior at P_N. Therefore the specified shadow walk makes exactly N-1 adjacent pivots P_1,...,P_N, with unique choices at all crossings. It cannot terminate earlier by exact CP recognition in the current Voronoi cone. This is a statement about that local walk, not about arbitrary preprocessing which could use the displayed factorization immediately.

Scaling A_N by the rational square [2n(N+1)]^-2 gives norm <=1 without changing the path or rational factor width. The input length and all factor/vertex heights are O_n(log N). A full-rank integer subfamily of the displayed atoms and Cramer's rule give an inverse-polynomial-in-N interior radius, hence binary conditioning O_n(log N). The exact radius bound is to be written out in the full proof.

Consequences: an exact, strictly feasible rational Gram fiber can have arithmetic reduction depth zero while its unique shadow path is exponential in binary input and conditioning size. Thus facial reduction depth (even with polynomial object heights) cannot bound the number of local adjacent crossings. The global certificate is explicitly available with constant width for fixed n. This provides a structural separation rather than attributing long paths to irrational boundary factors. It does not claim every descending local rule follows this path.
