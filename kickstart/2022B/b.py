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

#!/usr/bin/env python
from itertools import count

def getPalindrome():
    """
        Generator for palindromes.
        Generates palindromes, starting with 0.
        A palindrome is a number which reads the same in both directions.
    """
    yield 0
    for digits in count(1):
        first = 10 ** ((digits - 1) // 2)
        for s in map(str, range(first, 10 * first)):
            yield int(s + s[-(digits % 2)-1::-1])

PALINS = []

def pGen(gen=getPalindrome()):
    global PALINS
    for p in PALINS: yield p
    while 1:
        p = next(gen)
        PALINS.append(p)
        yield p

def allPalindromes(minP, maxP):
    """Get a sorted list of all palindromes in intervall [minP, maxP]."""
    palindromGenerator = pGen()
    for palindrome in palindromGenerator:
        if palindrome > maxP:
            break
        if palindrome < minP:
            continue
        yield palindrome

for T in range(int(input())):
    A = int(input())
    cnt = 0
    for f in allPalindromes(1,A):
        cnt += not A%f
    print('Case #{}: {}'.format(T+1,cnt))


