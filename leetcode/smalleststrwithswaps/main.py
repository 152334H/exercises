from typing import List
from collections import defaultdict as dd, deque

def smallestStringWithSwaps(s: str, pairs: List[List[int]]) -> str:
    adjls = dd(lambda: [])
    for e in pairs:
        u,v = e
        adjls[u].append(v)
        adjls[v].append(u)
    seen = set()
    sets = []
    for i in range(len(s)):
        if i not in adjls: continue
        if i in seen: continue
        q = deque([i])
        g = set()
        while q:
            nxt = q.pop()
            if nxt in seen: continue
            seen.add(nxt)
            for v in adjls[nxt]: q.appendleft(v)
            g.add(nxt)
        sets.append(g)
    t = [None]*len(s)
    for g in sets:
        chars = sorted(s[i] for i in g)
        for i,j in enumerate(sorted(g)): t[j] = chars[i]
    for i,c in enumerate(t):
        if c is None: t[i] = s[i]
    return ''.join(t)
for s,ls in [("dcab", [[0,3],[1,2]]),
        ("dcab", [[0,3],[1,2],[0,2]]),
        ("cba", [[0,1],[1,2]]),
        ("dcab", []),
        ("vbjjxgdfnru", [[8,6],[3,4],[5,2],[5,5],[3,5],[7,10],[6,0],[10,0],[7,1],[4,8],[6,2]]),
        ("wiftyfgoqfohnzelum", [[3,2],[6,2],[9,11],[2,3],[5,4],[2,2],[4,3],[9,3],[10,0],[4,16],[5,8],[14,5],[4,16],[17,1],[9,7],[12,9],[1,17],[16,7]])]: print(smallestStringWithSwaps(s,ls))
