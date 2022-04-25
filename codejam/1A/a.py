from itertools import *
from operator import *
from collections import *
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


for t in range(int(input())):
    inp = input().strip()
    next_changed_elem = []
    cnt = 0
    prev = '\0'
    for c in inp:
        if prev != c:
            next_changed_elem += [c]*cnt 
            cnt = 1
            prev = c
        else: cnt += 1
    next_changed_elem += ['\0']*(len(inp)-len(next_changed_elem))
    #print(next_changed_elem)
    res = '' # O(n)
    for i,c in enumerate(inp):
        if c < next_changed_elem[i]:
            res += c*2
        else: res += c
    print(f'Case #{t+1}: {res}')



