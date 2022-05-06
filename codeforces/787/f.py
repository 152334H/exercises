#!/usr/bin/env python3
'''FAILED ATTEMPT'''

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

import queue


def swap(a: int, b: int):
    """
    Return a tuple (b, a) when given two integers a and b
    >>> swap(2,3)
    (3, 2)
    >>> swap(3,4)
    (4, 3)
    >>> swap(67, 12)
    (12, 67)
    """
    a ^= b
    b ^= a
    a ^= b
    return a, b


def create_sparse(max_node: int, parent):
    """
    creating sparse table which saves each nodes 2^i-th parent
    """
    j = 1
    while (1 << j) < max_node:
        for i in range(1, max_node + 1):
            parent[j][i] = parent[j - 1][parent[j - 1][i]]
        j += 1
    return parent


# returns lca of node u,v
def lowest_common_ancestor(
    u: int, v: int, level, parent
):
    # u must be deeper in the tree than v
    if level[u] < level[v]:
        u, v = swap(u, v)
    # making depth of u same as depth of v
    for i in range(18, -1, -1):
        if level[u] - (1 << i) >= level[v]:
            u = parent[i][u]
    # at the same depth if u==v that mean lca is found
    if u == v:
        return u
    # moving both nodes upwards till lca in found
    for i in range(18, -1, -1):
        if parent[i][u] != 0 and parent[i][u] != parent[i][v]:
            u, v = parent[i][u], parent[i][v]
    # returning longest common ancestor of u,v
    return parent[0][u]


# runs a breadth first search from root node of the tree
def breadth_first_search(
    level,
    parent,
    max_node: int,
    graph,
    root=1,
):
    """
    sets every nodes direct parent
    parent of root node is set to 0
    calculates depth of each node from root node
    """
    level[root] = 0
    q = queue.Queue(maxsize=max_node)
    q.put(root)
    while q.qsize() != 0:
        u = q.get()
        for v in graph[u]:
            if level[v] == -1:
                level[v] = level[u] + 1
                q.put(v)
                parent[0][v] = u
    return level, parent 

def floyd_warshall(n, edges):
    dist = [[0 if i == j else float("inf") for i in range(n)] for j in range(n)]
    pred = [[None] * n for _ in range(n)]

    for u, v, d in edges:
        dist[u][v] = d
        pred[u][v] = u

    for k in range(1,n):
        for i in range(1,n):
            for j in range(1,n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]
    """Sanity Check
    for u, v, d in edges:
        if dist[u] + d < dist[v]:
            return None
    """

    return dist, pred

from random import randint
from collections import defaultdict as dd
def solve():
    '''Tree of size N, N-1 edges. Nodes are "Houses"
    Vlad wants to walk from node x to node y. However,
    he must also visit all nodes in A[] before reaching y.'''

    N,K = ints()
    x,y = ints()
    A = Ints()
    g = dd(set)
    important = set(A)
    important.add(x)
    important.add(y)
    #edges = []
    for _ in range(N-1):
        u,v = ints()
        #edges.append((u,v,1))
        #edges.append((v,u,1))
        g[u].add(v)
        g[v].add(u)
    #DIST,PRED = floyd_warshall(N+1,edges)
    ROOT = y
    root_dist = [None]*(N+1)
    border = [(None,ROOT)]
    d = 0
    seen = set()
    sparse_g = dd(dict)
    while border:
        nb = []
        for prev,n in border:
            if n in seen: continue 
            seen.add(n)
            if n in important:
                sparse_g[prev][n] = None 
                sparse_g[n][prev] = None
                prev = n
            for oth in g[n]: nb.append((prev,oth)) 
            root_dist[n] = d
        border = nb 
        d += 1
    del sparse_g[None]
    del sparse_g[ROOT][None]
    # COPY PASTE
    max_node = N
    parent = [[0 for _ in range(max_node+10)] for _ in range(20)]
    level = [-1 for _ in range(max_node+10)]
    level,parent = breadth_first_search(level, parent, max_node, g, ROOT)
    parent = create_sparse(max_node, parent)
    def LCA(a,b): return lowest_common_ancestor(a,b,level,parent)
    def distance(u,v) -> int: return root_dist[u]+root_dist[v]-2*root_dist[LCA(u,v)]
    # reduce the graph
    print(sparse_g)
    ng = dd(dict)
    leaves = set(n for n in sparse_g if len(sparse_g[n]) == 1)
    needed = 0
    ma = -1
    for l in leaves:
        d = distance(l,ROOT)
        print(l,d)
        needed += d
        ma = max(d,ma)
    return needed-ma
    

for t in range(int(input())):
    assert input() == ''
    print(solve())


