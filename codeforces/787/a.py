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

def solve():
    a,b,c,x,y = ints()
    x -= a
    y -= b
    x = max(0,x)
    y = max(0,y)
    return "YES" if x+y <= c else "NO"

for t in range(int(input())):
    print(solve())


