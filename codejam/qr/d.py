from typing import List,Dict,Set
from dataclasses import dataclass,field
from collections import defaultdict as dd, Counter as ctr, deque as dq

@dataclass
class JoinNode:
    children: Set[int] = field(default_factory=set)
    compFun: int = 0

def buildGraph(P: List[int], F: List[int]):
    leaves = dq(set(range(1,len(P))) - set(P))
    junctions = {k for k,v in ctr(P).items() if v > 1} - {0}
    g = dd(lambda: JoinNode())
    while leaves:
        orig = u = leaves.popleft()
        ma = F[u]
        while u:
            u = P[u]
            if u in junctions:
                g[u].children.add(orig)
                g[orig].compFun = ma
                leaves.append(u)
                break
            ma = max(F[u],ma)
        else: # encountered zero
            g[orig].compFun = ma 
            g[0].children.add(orig)
    return g

def maxFun(g,n):
    res = maxFunReal(g,n)
    #print('maxFun(g,{}) == {}'.format(n,res))
    return res

def maxFunReal(g,n):
    ''' for all children funs,
    pick the smallest fun to pass upwards
    add the rest of the funs to the sum total
    '''
    if not g[n].children: return 0,g[n].compFun
    totalFun = 0
    possibleMinFuns = []
    for u in g[n].children:
        childFun, childMin = maxFun(g,u)
        totalFun += childFun
        possibleMinFuns.append(childMin)
    totalFun += sum(possibleMinFuns)
    minFun = min(possibleMinFuns)
    totalFun -= minFun 
    return totalFun, max(minFun,g[n].compFun)

for t in range(int(input())):
    n = int(input())
    F = [-float('inf')]+[int(x) for x in input().split()]
    P = [-float('inf')]+[int(x) for x in input().split()]
    g = buildGraph(P, F)
    #print(g)
    totalFun, minFun = maxFun(g,0)
    print(f'Case #{t+1}: {totalFun+minFun}')

