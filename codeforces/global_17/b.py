# slow solution, and also dies to maxrecursionlimit
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
