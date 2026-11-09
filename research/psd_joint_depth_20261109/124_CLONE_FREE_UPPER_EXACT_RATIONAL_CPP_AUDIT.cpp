// Exact-rational certificate for Milestone 123, clone-free upper peeling.
// Compile: g++ -std=c++17 -O3 124_CLONE_FREE_UPPER_EXACT_RATIONAL_CPP_AUDIT.cpp -o audit && ./audit
// Uses Boost header-only boost::rational<long long>; NO floating point or SDP.
// Exhausts all (h!)^2 ordered harmonic policies for each h=1,...,6.
// Every strict solution: build globally UNIQUE offdiagonal generators;
// each generator has 1 or 2 nonnegative child-diagonal coefficients.
// Compute maximal PSD exposing closure and compare ALL layers with U(w).
#include <boost/rational.hpp>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cassert>
using namespace std;
using F=boost::rational<long long>;
struct Edge{
 int a,b;
 bool operator<(const Edge&o)const{return a<o.a||(a==o.a&&b<o.b);}
};
struct Audit{
 int h,k;vector<vector<Edge>> allowed;vector<Edge>P;vector<F>w;
 long long count=0,valid=0,coupled=0;
 explicit Audit(int n):h(n),k(n+1),allowed(n+1),P(n+1),w(n+2){
  for(int i=1;i<=h;i++)for(int a=0;a<i;a++)for(int b=i+1;b<=k;b++)
   allowed[i].push_back({a,b});
 }
 bool harmonic(){
  vector<vector<F>>A(h,vector<F>(h+1,0));
  for(int i=1;i<=h;i++){
   A[i-1][i-1]=2;
   for(int p:{P[i].a,P[i].b}){
    if(p==k)A[i-1][h]+=1;
    else if(p>0)A[i-1][p-1]-=1;
   }
  }
  for(int j=0;j<h;j++){
   int p=j;while(p<h&&A[p][j]==0)p++;if(p==h)return false;
   swap(A[p],A[j]);F f=A[j][j];
   for(int z=j;z<=h;z++)A[j][z]/=f;
   for(int i=0;i<h;i++)if(i!=j){
    f=A[i][j];if(f==0)continue;
    for(int z=j;z<=h;z++)A[i][z]-=f*A[j][z];
   }
  }
  w[0]=0;w[k]=1;
  for(int i=1;i<=h;i++)w[i]=A[i-1][h];
  for(int i=0;i<k;i++)if(w[i]>=w[i+1])return false;
  return true;
 }
 vector<int> upperStages(){
  vector<int>time(k+1);
  int j=k,t=1;
  while(j){
   int q;
   if(j==k)q=k-1;
   else{
    int p=1;
    while(p<=j&&!(2*w[p]>w[j]+w[p-1]))p++;
    assert(p<=j);q=p-1;
   }
   for(int i=q+1;i<=j;i++)time[i]=t;
   j=q;t++;
  }
  return time;
 }
 void check(){
  map<Edge,vector<int>>G;
  for(int i=1;i<=h;i++)G[P[i]].push_back(i);
  for(int i=1;i<=h;i++){
   int b=i+1;
   while(b<=k&&w[i-1]+w[b]<2*w[i])b++;
   assert(b<=k);
   Edge e={i-1,b};auto&children=G[e];
   if(find(children.begin(),children.end(),i)==children.end())
    children.push_back(i);
  }
  assert(G.size()>=size_t(h)&&G.size()<=size_t(2*h));
  bool shared=false;
  for(auto&item:G){
   assert(item.second.size()<=2);
   if(item.second.size()==2)shared=true;
   for(int i:item.second){
    assert(item.first.a<i&&i<item.first.b);
    assert(w[item.first.a]+w[item.first.b]>=2*w[i]);
   }
  }
  coupled+=shared;
  vector<int>target=upperStages();
  int R=(1<<(k+1))-1,t=1;
  while(R!=1){
   int C=R&~1;
   while(true){
    int bad=0;
    for(auto const&item:G){
     int e=(1<<item.first.a)|(1<<item.first.b);
     if((e&R)==e&&(e&C)!=e)
      for(int i:item.second)if(C&(1<<i))bad|=1<<i;
    }
    if(!bad)break;
    C&=~bad;
   }
   assert(C);
   for(int i=1;i<=k;i++)if(C&(1<<i))assert(target[i]==t);
   R&=~C;t++;
  }
 }
 void recurse(int i){
  if(i<=h){for(auto e:allowed[i]){P[i]=e;recurse(i+1);}return;}
  count++;if(!harmonic())return;
  valid++;check();
 }
 void run(){
  recurse(1);
  const long long strict[]={0,1,3,18,165,2099,34570};
  assert(valid==strict[h]);
  cout<<"PASS h="<<h<<" policies="<<count<<" strict="<<valid
      <<" with_multichild="<<coupled<<"\n";
  if(h==6)assert(count==518400&&coupled==6276);
 }
};
int main(){
 for(int h=1;h<=6;h++)Audit(h).run();
 cout<<"PASS: complete exact 1..6 internal-node upper-depth multi-child audit\n";
}