from typing import List
from math import ceil
from collections import defaultdict as dd
class Solution:
    # old solution. very inefficient.
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        N = len(patience)
        # get APSP
        dist = [[1<<60 for _ in range(N)] for __ in range(N)]
        #
        g = [[] for _ in range(N)]
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        #
        for i in range(N):
            q = [i]
            d = 0
            seen = set()
            while q:
                new_q = []
                for u in q:
                    if u in seen: continue
                    seen.add(u)
                    dist[i][u] = d
                    new_q += g[u]
                q = new_q
                d += 1
        #
        ma = 0
        for i in range(1,N):
            d = dist[i][0]
            messages_sent = ceil(2*d/patience[i])
            endtime = 2*d + (messages_sent-1)*patience[i]
            if ma < endtime: ma = endtime
        return ma+1



















        '''
        for (u,v) in edges: dist[u][v] = dist[v][u] = 1
        for i in range(N): dist[i][i] = 0
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        '''
for edges,patience,out in [([[0,1],[1,2]], [0,2,1], 8),
        ([[0,1],[0,2],[1,2]], [0,10,10], 3)]:
    s = Solution()
    res = s.networkBecomesIdle(edges, patience)
    if res != out:
        print(len(edges),len(patience),out,res)
