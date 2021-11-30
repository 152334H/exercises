from typing import List
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(v):
            if v == len(graph)-1: yield [v]
            else: yield from ([v]+ls for u in graph[v] for ls in dfs(u))
        return dfs(0)
s = Solution()
for (graph,out) in [
    ([[1,2], [3], [3], []], [[0,1,3],[0,2,3]]),
    ([[4,3,1],[3,2,4],[3],[4],[]], [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]),
    ([[1],[]], [[0,1]]),
    ([[1,2,3],[2],[3],[]],[[0,1,2,3],[0,2,3],[0,3]]),
    ([[1,3],[2],[3],[]], [[0,1,2,3],[0,3]])
    ]:
    assert s.allPathsSourceTarget(graph) == out
