''' This is what a simple solution looks like:
from functools import lru_cache
def longestPalindrome(s: str) -> str:
    @lru_cache(None)
    def dp(start,end,remove=None):
        def valid(oth): return remove is None or remove == oth
        if start == end: return 1
        edges_equal = s[start] == s[end]
        if start+1 == end: # length is 2
            if edges_equal: return 2
            if any(valid(c) for c in (s[start], s[end])):
                return 1 # remove either side.
            return -9999999 # corrupt all values.
        if s[start] == s[end]:
            return 2 + dp(start+1,end-1, remove)
        ma = -9999999
        if valid(s[start]): ma = dp(start+1,end,s[start])
        if valid(s[end]): ma = max(dp(start,end-1,s[end]), ma)
        return ma
    return dp(0,len(s)-1)

Why does it fail? Recursion depth. Test with 'a'*10**5.
Segfault will happen if you try to use sys.setrecursionlimit too.

The obvious solution here is to figure out iterative dp.
Since I can't do that, I simulated a stack on the heap with coroutunes.
'''
from collections import defaultdict as dd
def longestPalindrome(s: str) -> str:
    dp = dd(lambda: -9999999)
    def retdp(k, v: int) -> int:
        dp[k] = v
        return v
    def do_dp(start, end, remove):
        def valid(oth): return remove is None or remove == oth
        t = (start,end,remove)
        if t in dp: return dp[t]
        if start == end: return retdp(t,1)
        edges_equal = s[start] == s[end]
        if start+1 == end: # length is 2
            if edges_equal: return retdp(t,2)
            if any(valid(c) for c in (s[start], s[end])):
                return retdp(t,1) # remove either side.
            return retdp(t,-9999999) # corrupt all values.
        # at this point, end-start >= 2
        if s[start] == s[end]:
            yield (start+1,end-1,remove)
            res = yield
            return retdp(t,2+res)
        ma = -9999999
        if valid(s[start]):
            yield (start+1,end,s[start])
            res = yield
            ma = max(res,ma)
        if valid(s[end]):
            yield (start,end-1,s[end])
            res = yield
            ma = max(res,ma)
        return ma
    stack = [do_dp(0,len(s)-1,None)]
    while not isinstance(stack[0],int):
        coret = stack.pop()
        if isinstance(coret, int):
            real_coret = stack.pop()
            next(real_coret)
            try:
                stack.append(real_coret)
                stack.append(do_dp(*real_coret.send(coret)))
            except StopIteration as e:
                stack.pop() # get rid of the fake
                stack.append(e.value)
        else:
            try:
                to_do = next(coret)
                stack.append(coret)
                stack.append(do_dp(*to_do))
            except StopIteration as e: stack.append(e.value)
    return stack[0]

for t in range(int(input())):
    n = int(input()) # 1 <= n <= 10**5
    s = input().strip()
    length = longestPalindrome(s)
    if length < 1: print(-1)
    else: print(n-length)
