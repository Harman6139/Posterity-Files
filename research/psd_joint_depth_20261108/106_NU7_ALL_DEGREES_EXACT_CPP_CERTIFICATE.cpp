// Exact h=6 (target nullity seven) universal PSD exponent/depth certificate.
// Compile: g++ -O3 -std=c++17 106_NU7_ALL_DEGREES_EXACT_CPP_CERTIFICATE.cpp -o audit && ./audit
// Uses only C++ standard library and Boost header-only rational<long long>.
// Analytic NECESSITY: checkpoints 89/91/99; constructive SUFFICIENCY: 57/74.
// Checks 518400 one-action policies, all 0/1 extras, then every pair/triple
// of independent vs tied edges required by remaining target exponents.
// Independent leading edges must be globally distinct; no approximate SDP.
// Output counts: 325,857,817,596,321,117 at degrees 2 through 7.
#include <boost/rational.hpp>
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cassert>
using namespace std;
using Rat=boost::rational<long long>;
const int h=6, terminal=h+1;
struct Edge {
    int a,b;
    int id() const { return 8*a+b; }
    bool operator==(const Edge &o) const {return a==o.a&&b==o.b;}
};
struct Extra {int child; Edge edge; char kind;}; // 'I' independent, 'T' tied
vector<Edge> possible[7];
Edge parent_edge[7];
Rat weight[8];
map<int,set<pair<long long,long long>>> necessary, realized, need;
long long policy_total=0,strict_total=0;
long long pair_count=0,triple_count=0;
long long pair_policies=0,triple_policies=0;

bool solve_weights(){
    Rat M[6][7];
    for(int i=1;i<=h;++i){
        for(int j=0;j<=h;++j) M[i-1][j]=0;
        M[i-1][i-1]=2;
        for(int v:{parent_edge[i].a,parent_edge[i].b}){
            if(v==terminal) M[i-1][h]+=1;
            else if(v>0) M[i-1][v-1]-=1;
        }
    }
    for(int j=0;j<h;++j){
        int p=j;
        while(p<h && M[p][j]==0)++p;
        if(p==h)return false;
        if(p!=j)for(int z=0;z<=h;++z)swap(M[j][z],M[p][z]);
        Rat c=M[j][j];
        for(int z=j;z<=h;++z)M[j][z]/=c;
        for(int i=0;i<h;++i){
            if(i==j)continue;
            Rat factor=M[i][j];
            if(factor==0)continue;
            for(int z=j;z<=h;++z)M[i][z]-=factor*M[j][z];
        }
    }
    weight[0]=0;weight[terminal]=1;
    for(int i=1;i<=h;++i)weight[i]=M[i-1][h];
    for(int i=0;i<terminal;++i)
        if(!(weight[i]<weight[i+1]))return false;
    return true;
}
int primal_lower(){
    int j=terminal,steps=0;
    while(j>0){
        ++steps;
        if(j==terminal)j=terminal-1;
        else {
            int next=0;
            for(int i=1;i<j;++i)if(2*weight[i]<weight[j+1])++next;
            j=next;
        }
    }
    return steps;
}
int dual_upper(){
    int j=terminal,steps=0;
    while(j>0){
        ++steps;
        if(j==terminal){j=terminal-1;continue;}
        int p=1;
        while(p<=j && !(2*weight[p]>weight[j]+weight[p-1]))++p;
        assert(p<=j);
        j=p-1;
    }
    return steps;
}
int exact_peeling(const Extra *extra,int num){
    int remaining=(1<<(h+2))-1;
    int steps=0;
    while(remaining!=1){
        int exposed=remaining&~1;
        bool changed=true;
        while(changed){
            changed=false;
            for(int i=1;i<=h;++i){
                if(!(exposed&(1<<i)))continue;
                Edge tied[4];int nt=1;tied[0]=parent_edge[i];
                Edge independent[3];int ni=0;
                for(int z=0;z<num;++z)if(extra[z].child==i){
                    if(extra[z].kind=='T')tied[nt++]=extra[z].edge;
                    else independent[ni++]=extra[z].edge;
                }
                // A tied mode is active iff EVERY edge stays in face.
                bool active=true, fulfilled=false;
                for(int z=0;z<nt;++z){
                    int e=(1<<tied[z].a)|(1<<tied[z].b);
                    if((e&remaining)!=e)active=false;
                    if((e&exposed)==e)fulfilled=true;
                }
                bool blocked=active&&!fulfilled;
                // Every separate mode independently imposes its singleton edge.
                for(int z=0;z<ni;++z){
                    int e=(1<<independent[z].a)|(1<<independent[z].b);
                    if((e&remaining)==e && (e&exposed)!=e)blocked=true;
                }
                if(blocked){exposed^=(1<<i);changed=true;}
            }
        }
        assert(exposed!=0);
        remaining&=~exposed;
        ++steps;
    }
    return steps;
}
vector<Extra> permitted_extras(){
    bool used[64]={};
    for(int i=1;i<=h;++i)used[parent_edge[i].id()]=true;
    vector<Extra> out;
    for(int i=1;i<=h;++i){
        for(Edge edge:possible[i]){
            if(used[edge.id()])continue;
            Rat midpoint=(weight[edge.a]+weight[edge.b])/2;
            if(midpoint>=weight[i])out.push_back({i,edge,'I'});
            if(midpoint<=weight[i])out.push_back({i,edge,'T'});
        }
    }
    return out;
}
bool legal_leading(int vertex,const Extra *extra,int n){
    Edge lead={0,vertex};
    for(int i=1;i<=h;++i)if(parent_edge[i]==lead)return false;
    for(int i=0;i<n;++i)if(extra[i].edge==lead)return false;
    return true;
}
vector<pair<Rat,int>> leading_options(){
    vector<pair<Rat,int>> exps;
    for(int v=1;v<=terminal;++v){
        Rat alpha=weight[v]/2;
        if(alpha<=weight[1])exps.push_back({alpha,v});
    }
    return exps;
}
void visit_first(const Extra *extra,int num,
                 const vector<pair<Rat,int>>&exps){
    int degree=exact_peeling(extra,num);
    for(auto [alpha,v]:exps){
        if(alpha<Rat(1,1LL<<degree))continue;
        if(alpha<weight[1]&&!legal_leading(v,extra,num))continue;
        realized[degree].insert({alpha.numerator(),alpha.denominator()});
    }
}
void enumerate_initial(int i){
    if(i<=h){
        for(Edge e:possible[i]){parent_edge[i]=e;enumerate_initial(i+1);}
        return;
    }
    ++policy_total;
    if(!solve_weights())return;
    ++strict_total;
    int L=primal_lower(),U=dual_upper();
    assert(L<=U);
    auto exps=leading_options();
    for(auto [alpha,v]:exps)
        for(int d=L;d<=U;++d)
            if(alpha>=Rat(1,1LL<<d))
                necessary[d].insert({alpha.numerator(),alpha.denominator()});
    visit_first(nullptr,0,exps);
    auto all=permitted_extras();
    for(const Extra &x:all)visit_first(&x,1,exps);
}
vector<pair<Rat,int>> needed_leads(int L,int U){
    vector<pair<Rat,int>> exps;
    for(auto [alpha,v]:leading_options()){
        auto key=make_pair(alpha.numerator(),alpha.denominator());
        for(int d=L;d<=U;++d)
            if(need[d].count(key)){exps.push_back({alpha,v});break;}
    }
    return exps;
}
void collect_certificate(int d,const Extra *extra,int num,
                         const vector<pair<Rat,int>>&exps,bool print){
    for(auto [alpha,v]:exps){
        auto key=make_pair(alpha.numerator(),alpha.denominator());
        if(!need[d].count(key))continue;
        if(alpha<weight[1]&&!legal_leading(v,extra,num))continue;
        if(print){
            cout<<"THREE-EDGE WITNESS d="<<d<<" a="<<alpha.numerator()
                <<"/"<<alpha.denominator()<<" P=";
            for(int i=1;i<=h;++i)
                cout<<"("<<parent_edge[i].a<<","<<parent_edge[i].b<<")";
            cout<<" additions=";
            for(int z=0;z<num;++z)
                cout<<"("<<extra[z].child<<","
                    <<extra[z].edge.a<<","<<extra[z].edge.b
                    <<","<<extra[z].kind<<")";
            cout<<"\n";
        }
        need[d].erase(key);
    }
}
void enumerate_more(int i,int extras_count){
    if(i<=h){
        for(Edge e:possible[i]){parent_edge[i]=e;enumerate_more(i+1,extras_count);}
        return;
    }
    if(!solve_weights())return;
    int L=primal_lower(),U=dual_upper();
    auto exps=needed_leads(L,U);
    if(exps.empty())return;
    if(extras_count==2)++pair_policies;else ++triple_policies;
    auto all=permitted_extras();
    for(int a=0;a<(int)all.size();++a)
        for(int b=a+1;b<(int)all.size();++b){
            if(all[a].edge==all[b].edge)continue;
            if(extras_count==2){
                ++pair_count;
                Extra selected[2]={all[a],all[b]};
                int d=exact_peeling(selected,2);
                if(d>=L&&d<=U&&!need[d].empty())
                    collect_certificate(d,selected,2,exps,false);
            }else{
                for(int c=b+1;c<(int)all.size();++c){
                    if(all[a].edge==all[c].edge||
                       all[b].edge==all[c].edge)continue;
                    ++triple_count;
                    Extra selected[3]={all[a],all[b],all[c]};
                    int d=exact_peeling(selected,3);
                    if(d>=L&&d<=U&&!need[d].empty())
                        collect_certificate(d,selected,3,exps,true);
                }
            }
        }
}
int main(){
    for(int i=1;i<=h;++i)
        for(int a=0;a<i;++a)
            for(int b=i+1;b<=terminal;++b)
                possible[i].push_back({a,b});
    enumerate_initial(1);
    assert(policy_total==518400);
    assert(strict_total==34570);
    map<int,int> expected={{2,325},{3,857},{4,817},
                           {5,596},{6,321},{7,117}};
    for(auto[d,count]:expected){
        assert((int)necessary[d].size()==count);
        set_difference(necessary[d].begin(),necessary[d].end(),
                       realized[d].begin(),realized[d].end(),
                       inserter(need[d],need[d].end()));
    }
    enumerate_more(1,2);
    assert(need[2].empty()&&need[3].empty()&&need[4].empty()&&need[7].empty());
    assert(need[5].size()==4&&need[6].size()==6);
    enumerate_more(1,3);
    for(auto[d,count]:expected){
        assert(need[d].empty());
        cout<<"PASS d="<<d<<": "<<count<<" candidates, ALL REALIZED\n";
    }
    cout<<"PASS: "<<policy_total<<" harmonic policies; "
        <<strict_total<<" strictly increasing\n";
    cout<<"PASS: "<<pair_count<<" exact edge pairs, "
        <<triple_count<<" targeted triples\n";
    cout<<"PASS: complete arbitrary-dense PSD nullity-seven exponent-by-degree spectra\n";
}
