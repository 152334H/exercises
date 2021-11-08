from functools import lru_cache
class Solution:
    @lru_cache(maxsize=None)
    def numTrees(self, n: int) -> int:
        return 1 if n <= 1 else sum(
            self.numTrees(i-1)*self.numTrees(n-i)
            for i in range(1,n+1)
        )

s = Solution()
for (inp,out) in [(3,5), (1,1)]:
    assert s.numTrees(inp) == out
