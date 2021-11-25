from collections import defaultdict as dd
''' for testing purposes:
from random import randint,shuffle,choice
for t in range(10):
    n = randint(1, 100)
    b = [None for _ in range(n)]
    root = randint(1, n)
    b[root-1] = root
    parents = [root]
    while 1:
        unallocated = len([x for x in b if x is None])
        if not unallocated: break
        allocate = randint(1, unallocated)
        i = 0
        while allocate:
            if b[i] is not None:
                i += 1
                continue
            b[i] = choice(parents)
            parents.append(b[i])
            allocate -= 1
    p = [i+1 for i in range(n)]
    shuffle(p)
    print(n,b,p)
'''
for t in range(int(input())):
    n = int(input())
    b = [int(x) for x in input().split()]
    p = [int(x) for x in input().split()]
    p_ind = {x:i+1 for i,x in enumerate(p)}
    root = next(i+1 for i,x in enumerate(b) if x == i+1) # find root
    g = dd(set) # build a directed graph of parents to children.
    for i,par in enumerate(b): g[par].add(i+1)
    g[root].remove(root)
    # test if p is a valid topological sort of graph g.
    for u,s in g.items():
        if len(s) == 0: continue
        if p_ind[u] > min(p_ind[v] for v in s): break
    else: # this is a valid sort, and thus a valid permutation.
        dist_to_root = {root:0}
        for i,u in enumerate(p[1:],1):
            root_dist = dist_to_root[b[u-1]]+1
            root_dist = max(root_dist, dist_to_root[p[i-1]]+1)
            dist_to_root[u] = root_dist
        res = []
        for i in range(1,n+1):
            u,par = i,b[i-1]
            res.append(dist_to_root[u]-dist_to_root[par])
        print(' '.join(map(str,res)))
        continue
    print(-1)

