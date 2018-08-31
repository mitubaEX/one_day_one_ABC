#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;

#define REP(i,n) for(int i=0, i##_len=(n); i<i##_len; ++i)

template<class T> inline void amin(T &x, const T &y) { if (y<x) x=y; }
template<class T> inline void amax(T &x, const T &y) { if (x<y) x=y; }

int N, W[311];
int dp[311][311];


int main() {

    while (scanf("%d", &N), N) {
	REP (i, N) scanf("%d", W + i);
	memset(dp, 0, sizeof dp);

	for (int i=N-1; i>=0; i--) {
	    dp[i][i] = 0;
	    dp[i][i+1] = 0;
	    for (int j=i+1; j<=N; j++) {
		if (i + 1 < j && abs(W[i] - W[j-1]) <= 1 && dp[i+1][j-1] == j-i-2)
		    dp[i][j] = j - i;

		for (int k=j+1; k<=N; k++)
		    amax(dp[i][k], dp[i][j] + dp[j][k]);
	    }
	}

	printf("%d\n", dp[0][N]);
    }

    return 0;
}
