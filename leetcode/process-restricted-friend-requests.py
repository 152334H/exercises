from typing import List
from collections import defaultdict
class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        # restricted connections. Not really a graph.
        g = defaultdict(set)
        for u,v in restrictions:
            g[u].add(v)
            g[v].add(u)
        # weird ufds with an actual set backing each disjoint set
        sets = [set([i]) for i in range(n)]
        ufds = [i for i in range(n)]
        def find(x):
            if ufds[x] == x: return x
            ufds[x] = find(ufds[x])
            return ufds[x]
        # try each request; union when possible
        res = []
        for x,y in requests:
            a,b = find(x),find(y)
            ns = sets[a].union(sets[b])
            for i in ns: # very inefficient search that doesn't TLE??
                if any(r in ns for r in g[i]): break
            else: # union the sets
                ufds[a] = b
                sets[b] = ns
                res.append(True)
                continue
            res.append(False)
        return res

s = Solution()
for (inp,out) in [
    ((3,[[0,1]],[[0,2],[2,1]]), [True,False]),
    ((3,[[0,1]],[[1,2],[0,2]]), [True,False]),
    ((5,[[0,1],[1,2],[2,3]],[[0,4],[1,2],[3,1],[3,4]]), [True,False,True,False]),
    ]:
    res = s.friendRequests(*inp)
    assert res == out
