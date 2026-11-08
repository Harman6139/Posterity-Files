# Universal canonical sharp stability for bounded **nonsingleton** PSD feasible sets

**PROVED, 2026-11-07.** Exact exponent- and minimal-facial-depth-preserving gauge reduction from any bounded PSD feasible set to a uniquely solvable PSD problem. Combined with the universal canonical Dikin–Hessian theorem (checkpoint 10), it classifies the sharp full-matrix *distance-to-set* modulus by a single algebraic central path. Full proof below.

Let F={X>=0:LX=b} be nonempty and bounded. Pick X0∈relint(F) of maximal rank, let W=range X0, and define N=ker L ∩ S(W), the subspace of symmetric matrices supported on W and invisible to the measurements. Let P_N be its Frobenius orthogonal projector and set Lhat(H)=(L H,P_N H). Then X0 is the unique PSD feasible point for Lhat X=Lhat X0.

For the set-distance modulus
    Omega(delta)=sup{dist(Y,F):Y>=0, ||L Y-b||<=delta}
and the unique-target modulus omegahat of (Lhat,X0), there exist positive constants lambda,C such that for all small delta:
    omegahat(delta) <= Omega(delta)+delta;
    Omega(delta) <= C omegahat(lambda delta).
Consequently the two problems have identical optimal Hölder exponent and **identical minimal singularity degree**. In particular that exact set-distance exponent is computed by the universal Dikin-Hessian classifier applied to Lhat and X0.

## Complete proof

**Affine face and uniqueness.** Since X0∈relint(F), for each Z∈F some t>0 satisfies X0+t(X0-Z)∈F. Testing its PSD on v∈ker X0 gives v'Z v=0 and hence ker X0⊂ker Z, so every feasible Z is supported on W. Conversely X0|W>0 implies X0±s H∈F for small s if H∈ker L∩S(W)=N. Thus aff F=X0+N. If Lhat Y=Lhat X0 with Y>=0, then Y∈F, so Y-X0∈N and P_N(Y-X0)=0; thus Y=X0.

**Distance comparison.** Put H=Y-X0 and e(Y)=||P_(N⊥)H||=dist(Y,aff F). Bounded residual sublevels yield M with ||P_N H||<=M. Let mu=min eig(X0|W)>0. The affine projection Z=X0+P_NH onto aff F satisfies Z_W>=-e(Y)I from Y=Z+P_(N⊥)H>=0. With theta=e(Y)/(mu+e(Y)), the matrix Z'=(1-theta)Z+theta X0=X0+(1-theta)P_NH is PSD, belongs to F, and
    e(Y)<=dist(Y,F)<=||Y-Z'||<=e(Y)+theta M <=(1+M/mu)e(Y).
For an augmented residual competitor, ||P_NH||<=delta, so ||Y-X0||<=dist(Y,F)+delta. Taking supremum proves omegahat(delta)<=Omega(delta)+delta.

Choose fixed lambda>0 small enough (1-lambda)mu>=lambda M. Given any original competitor Y define
    Yhat=X0+lambda P_(N⊥)(Y-X0)
        =lambda Y+(1-lambda)X0-lambda P_N(Y-X0).
The last two terms together are PSD and supported on W, so Yhat>=0. Since L P_N H=0, its original measurement residual is <=lambda delta, its added gauge residual vanishes, and ||Yhat-X0||=lambda e(Y). Therefore omegahat(lambda delta)>=lambda e(Y), and the previous distance inequality gives Omega(delta)<=(1+M/mu)/lambda omegahat(lambda delta).

**Exact depth preservation.** At any intermediate face supported on V⊃W, an exposing stress of augmented constraints is Z=L*y+T with T∈N. Its compression P_V ZP_V is PSD and annihilates X0. Since X0|W>0, PSD implies P_W ZP_W=0, and hence <Z,T>=0. But <Z,T>=<L*y,T>+<T,T>=||T||² since L T=0. Thus T=0. Every augmented exposing stress at every step is already an original exposing stress; conversely originals remain valid. So all facial-reduction chains and the minimal singularity degree agree. QED.

**Scope.** The appropriate modulus is distance to F, not distance to an arbitrary chosen member. For noncompact feasible sets or unbounded residual sublevels this global worst-case modulus can be infinite; boundedness matters. The direct Dikin radius on ker L would detect free feasible motion and falsely give exponent zero, hence the canonical gauge is indispensable.