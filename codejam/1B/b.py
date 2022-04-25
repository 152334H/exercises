#!/usr/bin/env python3
from itertools import *
from operator import *
from collections import *
dd,ctr = defaultdict, Counter

_pow = pow
from math import *
pow = _pow # math's pow() doesn't provide the `mod` optional arg

from re import findall
from functools import *

# non-generator versions of common funcs
Map = lambda f,it: list(map(f,it))
Filter = lambda f,it: list(filter(f,it))
Reversed = lambda ls: list(reversed(ls))
Zip = lambda *ls: list(zip(*ls))

# for the package
from typing import *
import sys
sys.setrecursionlimit(2500) # phew

def solve():
    N,P = map(int,input().split())
    X = [Map(int,input().split()) for _ in range(N)]
    mima = []
    for ls in X:
        ls.sort()
        mima.append((ls[0],ls[-1]))
    #
    # dp[i][start_from] = ... # minimum button presses to get from ith customer to end if the gas starts at start_from
    @lru_cache(None)
    def dp(i: int, start_from: int) -> int:
        if i == N: return 0
        #
        d = mima[i][1] - mima[i][0]
        from_left = dp(i+1, mima[i][1])+abs(start_from-mima[i][0])
        from_right= dp(i+1, mima[i][0])+abs(start_from-mima[i][1])
        return min(from_left, from_right)+d
    #
    return dp(0,0)

for T in range(int(input())):
    res = solve()
    print('Case #{}: {}'.format(T+1,res))
