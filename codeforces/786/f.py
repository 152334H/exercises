#!/usr/bin/env python3
import os
import sys
from io import BytesIO, IOBase
from typing import *

# === fastio ===
BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)

class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")

sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# === end fastio ===

# === recursion ===
from types import GeneratorType

def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc

# === end recursion ===

# === personal ===
from functools import *
ints = lambda: map(int, input().split())
Ints = lambda: list(ints())
Map = lambda f,it: list(map(f, it))
Filter = lambda f,it: list(filter(f, it))
Reversed = lambda it: list(reversed(it))

def sum_array(ls: int) -> List[int]: return [0] + list(accumulate(ls))
class SAT(list):
    ''' summed array table of a 2d matrix
    !!! (y,x) !!! '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.width = len(self[0])
        self.height = len(self)
        self.sat = [[0 for _ in range(self.width+1)]\
                for _ in range(self.height+1)]
        for y in range(self.height):
            for x in range(self.width):
                self.sat[y+1][x+1] = self.sat[y][x+1] + self.sat[y+1][x] - self.sat[y][x] + self[y][x]
    def area(self, x1, y1, x2, y2):
        if x1 > x2 or y1 > y2 or x1 < 0 or y1 < 0 or x2 >= self.width or y2 >= self.height: raise RuntimeError('Invalid region')
        x1,y1,x2,y2 = x1+1,y1+1,x2+1,y2+1
        return self.sat[y2][x2] - self.sat[y2][x1] - self.sat[y1][x2] + self.sat[y1][x1]

# === end personal ===

# conceptually this is quite simple: keep track of which icons move where, and update on every query
# but impl is huge. Too much to finish.
def solve():
    R,C,Q = ints()
    def inc(p,v=1): # v!=1 NOT IMPLEMENTED!
        x,y = p
        y += v
        if y >= R:
            y -= R
            x += 1
        return x,y
    def dec(p,v=1):
        x,y = p
        y -= v
        if y < 0:
            y += R
            x -= 1
        return x,y
    def nth_icon_pos(n: int):
        # this is ZERO INDEXED!
        x,y = divmod(n,R)
        return x,y
    #
    desktop = {}
    for y in range(R):
        for x,c in enumerate(input()):
            desktop[x,y] = c == '*'
    # build the fixed desktop
    to,fr = (0,0), (C-1,R-1)
    desktop_fixed = dict(desktop)
    movements = {}
    movements_rev = {}
    from aoc import Grid,Point
    while to<fr:
        while desktop_fixed[to]: to = inc(to)
        while not desktop_fixed[fr]: fr = dec(fr)
        if to > fr: break
        desktop_fixed[to] = True
        desktop_fixed[fr] = False
        movements[fr] = to 
        movements_rev[to] = fr
    dk = Grid({Point(*k):'.*'[v] for k,v in desktop.items()})
    dk_fx = Grid({Point(*k):'.*'[v] for k,v in desktop_fixed.items()})
    def print_from_changes():
        clone = dict(desktop)
        for fr,to in movements.items():
            if movements_rev[to] != fr: raise RuntimeError 
            clone[to],clone[fr] = True,False
        print(Grid({Point(*k):'.*'[v] for k,v in clone.items()}))

    print(dk)
    print('becomes')
    print(dk_fx)
    #
    for i in range(Q):
        x,y = ints()
        y,x = x-1,y-1 # stupid qn statement
        desktop[x,y] = not desktop[x,y]
        if (x,y) in movements: # we can't move this star anymore!
            endpoint = movements[x,y]
            potentially_redirected = nth_icon_pos(len(movements))
            del movements_rev[endpoint]
            del movements[x,y]
            print(potentially_redirected)
            if potentially_redirected == endpoint: continue # we got lucky
            # otherwise
            redirected_to = dec(potentially_redirected)
            if potentially_redirected in movements_rev: # we can move the endpoint of
                originator = movements_rev[potentially_redirected]
                movements[originator] = redirected_to # this is an OVERWRITE
                del movements_rev[potentially_redirected]
                movements_rev[redirected_to] = originator
            else: # the star we want to redirect was actually originally at `potentially_redirected`.
                movements[potentially_redirected] = redirected_to 
                movements_rev[redirected_to] = potentially_redirected
            print(len(movements))
            print_from_changes()
            exit()
        elif (x,y) in movements_rev: # we can't move a star here anymore!
        else: 
    return 

solve()
