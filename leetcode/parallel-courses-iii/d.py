from collections import defaultdict as dd
from typing import List
from heapq import heappop,heappush
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        not_starts = set() # nodes that have dependencies
        requires = dd(set) # requires[n] == set of nodes that n requires
        g = dd(set) # g[n] == set of nodes that requires n
        for prev,nxt in relations: # generate the graph(s)
            g[prev].add(nxt)
            not_starts.add(nxt)
            requires[nxt].add(prev)

        pq = []
        for s in set(range(1,n+1))-not_starts: # i.e. for all nodes w/ no dependencies
            heappush(pq,(time[s-1],s))
        while pq: # just use a priority queue to move forward time
            end_time, node = heappop(pq)
            print(end_time,node)
            for nxt in g[node]: # for all nodes dependent on node,
                requires[nxt].remove(node) # finish the dependency
                if not requires[nxt]: # if all dependencies satisfied
                    heappush(pq,(time[nxt-1]+end_time,nxt))
        return end_time # this is the last value of end_time seen.
s = Solution()
print(s.minimumTime(3, [[1,3],[2,3]], [3,2,5]))
print(s.minimumTime(5, [[1,5],[2,5],[3,5],[3,4],[4,5]], time = [1,2,3,4,5]))

