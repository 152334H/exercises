// I didn't figure out the important observation that, if a palindrome can be obtained by removing some instances of v, a palindrome can also be obtained by removing all instances of v.
#include <bits/stdc++.h>
using namespace std;
/*
dp = {}
def kalindrome(s,i,j,c=None):
    ''' If s[i] = s[j], d[i, j] = max(d[i+1, j-1] + 2, d[i, j-1], d[i+1, j]).
    Otherwise d[i, j] = max(d[i, j-1], d[i+1, j]). '''
    if -1 <= j-i < 1: dp[i,j,c] = j-i+1
    if (i,j,c) in dp: return dp[i,j,c]
    elif (i,j,None) in dp:
        dp[i,j,c] = dp[i,j,None]
        return dp[i,j,c]
    ma = -10**6
    if s[i] == s[j]: ma = kalindrome(s,i+1,j-1,c) + 2
    if c is None or c == s[i]: ma = max(ma, kalindrome(s,i+1,j,s[i]))
    if c is None or c == s[j]: ma = max(ma, kalindrome(s,i,j-1,s[j]))
    dp[i,j,c] = ma
    return ma

for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    if n < 2 or kalindrome(A,0,n-1) > 0: print("YES")
    else: print("NO")
    dp = {}
*/
;
#define compress(i,j,v) ((((long long)i)<<40) | (((long long)j)<<20) | (v))
int kalindrome(unordered_map<long long,int> &dp, vector<int> &A, int i, int j, int v = 0) {
    if (i >= j) return i == j;
    if (dp.count(compress(i,j,v))) return dp[compress(i,j,v)];
    if (dp.count(compress(i,j,0))) return dp[compress(i,j,v)]=dp[compress(i,j,0)];
    int ma = -10e6;
    if (A[i] == A[j]) ma = kalindrome(dp,A,i+1,j-1,v) + 2;
    if (ma < 0 && (!v || v == A[i])) ma = max(ma, kalindrome(dp,A,i+1,j,A[i]));
    if (ma < 0 && (!v || v == A[j])) ma = max(ma, kalindrome(dp,A,i,j-1,A[j]));
    return dp[compress(i,j,v)] = ma;
}
int main() {
    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        vector<int> A(n);
        for (int i = 0; i < n; i++) cin >> A[i];
        unordered_map<long long,int> dp;
        if (n < 2 or kalindrome(dp,A,0,n-1) > 0) cout << "YES" << endl;
        else cout << "NO" << endl;
    }
}
