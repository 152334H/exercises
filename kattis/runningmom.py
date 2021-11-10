from collections import defaultdict as dd
from sys import stdin
n = int(input())
g = dd(set)
for _ in range(n):
    u,v = input().strip().split()
    g[u].add(v) # directed graph

def find_safe(start):
    def dfs(n, vis):
        if n in vis:
            if start in vis: return True
        else:
            vis.add(n)
            if any(dfs(v,vis) for v in g[n]): return True
        vis.remove(n)
        return False
    return dfs(start,set())

for line in stdin:
    line = line.strip()
    print(line, 'safe' if find_safe(line) else 'trapped')
