#!/usr/bin/env python3.8
from itertools import *
from operator import *
from collections import *
from dataclasses import dataclass
dd,ctr = defaultdict, Counter

_pow = pow
from math import *
pow = _pow # math's pow() doesn't provide the `mod` optional arg

from re import findall
from functools import reduce, lru_cache, singledispatchmethod

# non-generator versions of common funcs
Map = lambda f,it: list(map(f,it))
Filter = lambda f,it: list(filter(f,it))
Reversed = lambda ls: list(reversed(ls))
Zip = lambda *ls: list(zip(*ls))

# for the package
from typing import *

for T in range(int(input())):
    N,D = map(int,input().split())
    V = list(map(int,input().split()))
    #
    flatV = []
    i = 0
    while i < len(V):
        v = V[i]
        pi = i
        while i < len(V) and V[i] == v: i += 1
        flatV.append(v)
    #
    @lru_cache(maxsize=None)
    def dp(l,r):
        # eqs: (bool,bool). whether desired number is equal to flatV[l] || flatV[r]
        if l == r: return 0,0
        #print(l,r)
        is_eq = (flatV[l] == flatV[r])
        # try taking the left
        dist = flatV[l]-flatV[l+1]
        dist = min(dist%D,(-dist)%D)
        vl,_ = dp(l+1,r-is_eq)
        best = vl+dist
        #
        if not is_eq: # try taking the right
            dist = flatV[r]-flatV[r-1]
            dist = min(dist%D,(-dist)%D)
            vr,_ = dp(l,r-1)
            best = min(best,vr+dist)
        else: vr = 999
        #print('dp(%d,%d) = %d'%(l,r,best))
        return best, (vr-vl)
    i,r = 0,len(flatV)-1
    zeroing = flatV[i] == 0 and flatV[r] == 0
    res,diff = dp(0,len(flatV)-1)
    zeroing = zeroing or (flatV[i] == 0 and diff <= 0)
    zeroing = zeroing or (flatV[r] == 0 and diff >= 0)
    print('Case #{}: {}'.format(T+1,res+(not zeroing)))

