from typing import List
from heapq import heappush, heappop
from collections import defaultdict as dd
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        g = [set() for _ in range(n+1)]
        for u,v in edges:
            g[u].add(v)
            g[v].add(u)
        # lazy: keep track of all bfs history to figure out the paths from 1 to n
        q = [(1,[])]
        dists = dd(lambda: set())
        d = 0
        seen = set()
        fastest = [range(9999999)]
        while q:
            nq = []
            for u,his in q:
                dists[u].add(d)
                if u in seen: continue
                seen.add(u)
                nhis = his+[u]
                if u == n: 
                    if len(fastest[0]) > len(nhis): fastest = [nhis]
                    elif len(fastest[0]) == len(nhis): fastest.append(nhis)
                for v in g[u]: nq.append((v,nhis))
            q = nq
            d += 1
        # important part: finding out if the 2nd min time requires 1 extra edge traversal or 2
        can_use_one = False
        for path in fastest:
            for u in path:
                srt = sorted(dists[u])
                if len(srt) > 1 and srt[0] == srt[1]-1:
                    can_use_one = True
                    break
            if can_use_one: break
        # calculate the solution
        def time_of(edges:int):
            t = 0
            for _ in range(edges):
                is_red = t%(change*2) >= change
                add = 0 if not is_red else change-(t%change)
                t += time+add
            return t
        return time_of(len(fastest[0])+1-can_use_one)


s = Solution()
assert 13 == s.secondMinimum(n = 5, edges = [[1,2],[1,3],[1,4],[3,4],[4,5]], time = 3, change = 5)
assert 11 == s.secondMinimum(n = 2, edges = [[1,2]], time = 3, change = 2)
