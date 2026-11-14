# Track II: proved quantitative obstruction and effective Ryshkov interior bound

Date: 2026-11-14. Source baseline: 22ed4becd320695b41f8a11f1223ea090ef89ecf.
Status: The proposed polynomial-in-binary-precision bound for the specified adjacent-pivot rule is FALSE. The results below are mathematical proofs, not numerical evidence. Historical originality and the requested upper-quintile comparison are separate, not certified here.

## 1. Exact forced exponential path

For each integer N>=1, take

A_N = [[0,1/(4N)],[1/(4N),1/2]],
P_k = [[k^2+k+1,-k-1/2],[-k-1/2,1]]  (k>=0).

The canonical starting vertex is P_0. Every objective-decreasing adjacent-edge rule in Procedure 3 of Dutour Sikiric--Schuermann--Vallentin, including the prescribed minimum-ratio shadow rule, must visit P_0,P_1,...,P_N, and stops at P_N. Thus it makes exactly N adjacent pivots.

Proof. For integer a,b>=0,
P_k[(a,b)]=(b-ka)^2-a(b-ka)+a^2.
The integral form z^2-az+a^2 has minimum 1 on nonzero integer pairs. Its positive-orthant equality vectors are exactly e_2,(1,k),(1,k+1). Their rank-one matrices are independent, so P_k is a simple Ryshkov vertex. Its tangent cone has the following three extreme-ray generators:

R_k^+ = [[2k+2,-1],[-1,0]],
R_k^- = [[-2k,1],[1,0]],
T_k = [[2k(k+1),-(2k+1)],[-(2k+1),2]].

Each generator has zero value on two of the three active vectors and positive value on the third. The pairings with A_N are

<A_N,R_k^+>=-1/(2N),
<A_N,R_k^->=1/(2N),
<A_N,T_k>=1-(2k+1)/(2N),
<A_N,P_k>=1/2-(2k+1)/(4N).

For 0<=k<N the last two expressions are positive, so R_k^+ is the UNIQUE decreasing extreme ray. It is not copositive, since R_k^+[(1,k+2)]=-2. Also P_k+R_k^+=P_{k+1}. The endpoint is exact: both endpoints are feasible, and the new active vector (1,k+2) prevents extending the segment beyond parameter 1. Thus the next pivot is forced. At k=N the vertex pairing is -1/(4N)<0, so the procedure stops.

The Frobenius norm of A_N is less than 1. The negative eigenvalue has magnitude

delta_N=(sqrt(1+N^(-2))-1)/4
       =1/[4N^2(sqrt(1+N^(-2))+1)].

The positive eigenspace has an entrywise positive eigenvector. Therefore the PSD projection of A_N is a completely positive rank-one matrix, and delta_N is exactly its Frobenius distance to CP_2. Thus L_N=O(log N), log(1/delta_N)=O(log N), and H_N=O(log N). Taking N=2^m gives 2^{Omega(H_N)} forced pivots. This disproves the proposed theorem, even without degeneracy or pivot ties. It does NOT disprove finite termination, and it does not give a lower bound for algorithms allowed to preprocess PSD violations or make nonlocal jumps.

## 2. The sharp-grid modification does not remove the obstruction

At P_k, R=R_k^+, the objective-dependent rule of milestone 37 has

g=1/(2N), h=k+1, alpha=1/[4N(k+1)].

For k<=N-2, any admissible integer q satisfying 4q^2 alpha(1+alpha)>=1 must satisfy q>k+1: at q=k+1 the left side equals (k+1)/N+1/(4N^2)<1. Then (1,q) is a tested shell vector and R[(1,q)]=2(k+1-q)<0. The routine therefore cannot return a separator at those vertices. It must perform at least N-1 pivots.

At k=N-1 the least admissible q is N. All cube values are 2a(Na-b)>=0 for 0<=a,b<=N, so the least-q routine returns the corrected separator there. Thus this implementation makes exactly N-1 pivots. Choosing a larger q may instead find a negative vector and lead to the terminal vertex P_N. The exponential lower bound is unaffected.

## 3. Effective Ryshkov interior theorem, all orders

Let P be any real symmetric n-by-n matrix satisfying P[v]>=1 for all nonzero v in Z_+^n, and suppose ||P||_F<=M with M>=1. Set

q=ceil(sqrt(4nM)),
mu_n(M)=1/[2n q^{2(n-1)}].

Then P[x]>=mu_n(M)||x||^2 for every x>=0. In particular every active integer vector has Euclidean norm at most sqrt(2n)q^{n-1}.

Proof. Integer-ray density first shows P is copositive. Let mu=min{P[x]:x>=0,||x||=1}, and choose a minimizer with support S of size s. On that support, Lagrange multipliers give P_SS x_S=mu x_S. Divide by the largest coordinate to get y with max y_i=1 and the same eigenvector identity. Fix a coordinate equal to 1. The elementary pigeonhole proof of simultaneous Dirichlet approximation, applied to the other s-1 coordinates, gives an integer 1<=r<=q^{s-1} and an integer vector v supported on S with v_j=r at the fixed coordinate, 0<=v_i<=r, and |v_i-r y_i|<=1/q otherwise. Put e=v-r y. Then

P[v]=mu||v||^2+e^T(P_SS-mu I)e
    <=mu n q^{2(n-1)}+2Mn/q^2
    <=mu n q^{2(n-1)}+1/2.

Here 0<=mu<=M and ||e||^2<=(s-1)/q^2. Since v is a nonzero nonnegative integer vector, P[v]>=1. Rearranging proves the claim. This proof also establishes strict copositivity without using a qualitative compactness argument.

## 4. The exponent n-1 is sharp in every order

Let B be the canonical tridiagonal matrix with diagonal 1 and adjacent off-diagonal -1/2. For integer t>=1 let U_t=I-tS, where S has ones on its superdiagonal, and let Q_t=U_t^T B U_t.

U_t is integral unimodular and U_t^{-1}=I+tS+...+t^{n-1}S^{n-1} is nonnegative. The form B has minimum 1 on all nonzero integer vectors, so Q_t is in the Ryshkov set. Its transformed interval vectors U_t^{-1}1_[i,j] are nonnegative minimal vectors and their outer products span the symmetric space. Hence Q_t is a Ryshkov vertex.

Moreover ||Q_t||_F<=||B||_F(1+t)^2<=4n t^2, whereas x_t=U_t^{-1}e_n=(t^{n-1},...,t,1)^T satisfies Q_t[x_t]=1. Consequently

min_{x>=0,||x||=1}Q_t[x]<=t^{-2(n-1)}.

No uniform bound c(n)||Q||_F^{-beta} with beta<n-1 can therefore hold, even when restricted to positive-definite Ryshkov vertices. The active-vector height exponent (n-1)/2 is sharp as well.

## 5. Consequences under development in the accompanying manuscript

The effective bound gives finite, explicitly bounded active-vector enumeration and exact neighboring-vertex computation; it is not a proposed polynomial pivot potential. Combined with the verified shadow invariant and explicit anchor coercivity, it yields an all-order singly-exponential precision bound and polynomial bit heights. The exponential dependence cannot in general be replaced by a polynomial for adjacent descent. A standard exact support-enumeration copositivity test can replace the grid ray test, including on the boundary; this classical KKT mechanism is not claimed as a new invention.

Source audit: The original article already connects binary pivots with Farey/continued-fraction constructions. Oertel--Schuermann, Generalized Perfect Matrices, arXiv:2602.05841v2, proves qualitative interior-Ryshkov properties using Diophantine approximation. These are close antecedents. The new assertions requiring priority checking are the forced finite nonmember lower bound, its survival under the specified correction test, and the explicit sharp quantitative interior/height estimates. No top-20% journal assessment is claimed.