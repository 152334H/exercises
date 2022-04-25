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

def solve():
    N = int(input())
    D = deque(map(int, input().split()))
    prevBest = 0
    cnt = 0
    while D:
        if D[0] < prevBest: D.popleft()
        elif D[-1] < prevBest: D.pop()
        elif D[0] < D[-1]:
            prevBest = D[0]
            D.popleft()
            cnt += 1
        else:
            prevBest = D[-1]
            D.pop()
            cnt += 1
    return cnt

for T in range(int(input())):
    res = solve()
    print("Case #{}: {}".format(T+1, res))
