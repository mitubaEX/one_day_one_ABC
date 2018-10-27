#include <iostream>
#include <vector>
#include <map>
#include <utility>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <stack>
#include <queue>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <numeric>
#include <complex>
#include <bitset>
#include <functional>
#include <stack>
#include <regex>
#include <tuple>
#include <iomanip>

#define rrep(i,n) for(int i=n;i>0;i--)
#define RREP(i,a,n) for(int i=n;i>a;i--)
#define rep(i,n) for(int i=0;i<n;i++)
#define REP(i,a,n) for(int i=a;i<n;i++)
#define all(a) (a).begin(),(a).end()
#define pb(x) push_back(x)
#define mp(x,y) make_pair((x),(y))

#define fs first
#define sc second

#define MOD 1000000007
#define INF 1LL<<55

#define show(...) cerr<<#__VA_ARGS__<<" = ";_DEBUG(__VA_ARGS__)

using namespace std;

using ll = long long;

template<typename T1,typename T2> using P = pair< T1, T2 >;
using Pii = P<int,int>;
using Pll = P<ll,ll>;
using Pdd = P<double,double>;

template<typename T> using V = vector< T >;
using Vi = V<int>;
using Vll = V<ll>;
using Vs = V<string>;

template<typename T1,typename T2> using M = map< T1, T2>;
using Mii = M<int, int>;
using Mll = M<ll, ll>;
using Msi = M<string, int>;

template<class T> istream& operator >>(istream &is, vector<T> &v){for(T &e:v)is>>e;return is;}
template<class T> ostream& operator <<(ostream &os, vector<T> v){os<<"{";for(T &e:v)os<<e<<(v.size()-(int)(&e-&v[0])>1?", ":"");os<<"}";return os;}

void _DEBUG(){}
template<typename H,typename... T> void _DEBUG(H a,T...b){cerr<<a<<(sizeof...(b)?",":"\n");_DEBUG(b...);}

inline void in(){}
template<typename H,typename... T>void in(H &a, T&... b){cin>>a;in(b...);}
inline void out(){}
template<typename H,typename... T> void out(H a, T... b){cout<<a<<(sizeof...(b)?" ":"\n");out(b...);}

template<class T> void resz(int n,T& v){v.resize(n);}
template<class H,class... T> void resz(int n,H& a,T&... b){a.resize(n);resz(n,b...);}

// please declaration dx[8], dy[8]
#define DX {-1,0,1,0,-1,-1,1,1}
#define DY {0,-1,0,1,-1,1,1,-1}
#define DX2 {-1,0,1,0}
#define DY2 {0,-1,0,1}

signed main() {
  // N
  // Ai
  ll N;
  in(N);
  Vll vec(N);
  in(vec);
  sort(all(vec));

  V<bool> used(N);
  rep(i, N) {
    used[i] = false;
  }
  // out(vec);
  ll n = 0, m = N - 1;
  ll ans = 0;

  ans += abs(vec[m] - vec[n]) + abs(vec[m - 1] - vec[n]);
  used[n] = true;
  used[m] = true;
  used[m-1] = true;
  n++;

  // out(ans);
  while (true) {
    if (used[n] && used[m] && used[m - 2]) {
      break;
    } else if (used[m - 2]) {
      ans += abs(vec[m] - vec[n]);
    } else {
      if (N % 2 == 0) {
        ans += abs(vec[m] - vec[n]) + abs(vec[m - 2] - vec[n]);
      } else {
        ans += abs(vec[m] - vec[n]) + abs(vec[m - 2] - vec[m - 1]);
      }
    }
    // out(ans);
    used[n] = true;
    used[m] = true;
    used[m-2] = true;
    n++;
    m--;
  }
  out(ans);


  return 0;
}
