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
from sys import stdout

def printf(*args, **kwargs):
    print(*args, **kwargs)
    stdout.flush()

from random import randint

for T in range(int(input())):
    printf('00000000')
    ones = int(input())
    while ones:
        s = '0'*8
        while s.count('1') != ones:
            v = randint(1,255)
            s = bin(v)[2:]
        printf(s.ljust(8,'0'))
        ones = int(input())
