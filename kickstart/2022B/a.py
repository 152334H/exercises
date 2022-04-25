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

def area(r: int) -> float: return pi * r**2
for T in range(int(input())):
    R,A,B = map(int,input().split())
    total = 0
    while R:
        total += area(R)
        print(R)
        R *= A
        total += area(R)
        print(R)
        R //= B
    print('Case #{}: {}'.format(T+1,total))
