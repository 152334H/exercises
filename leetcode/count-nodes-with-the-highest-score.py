from typing import List
from collections import defaultdict as dd
from functools import reduce
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        children = dd(dict)
        for i,p in enumerate(parents):
            children[p][i] = 0
        def trav(n): # figure out children of each node,
            for c in children[n]: children[n][c] = trav(c)
            # and also the size of each child's subtree.
            return 1+sum(children[n].values())
        trav(0) # traverse from root

        ma, freq = 0,0
        for i in range(len(parents)):
            # calculate the product of the 3 subtrees
            prod = reduce(lambda a,b: a*b, children[i].values(),1)
            upside = len(parents)-1-sum(children[i].values())
            prod *= max(1,upside) # note: upside will be 0 for root.
            # update maximum && freq if needed.
            if ma < prod: ma,freq = prod,1
            elif ma == prod: freq += 1
        return freq

s = Solution()
for parents in ([-1,2,0,2,0], [-1,2,0]):
    print(s.countHighestScoreNodes(parents))
