from typing import List
from itertools import combinations
from functools import reduce
class Solution:
    # len(nums) < 17, just bruteforce
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        or_of = lambda ls: reduce(lambda a,b: a|b, ls)
        bOR = or_of(nums)
        count = 0
        for r in range(1,len(nums)+1):
            for comb in combinations(nums,r):
                if or_of(comb) == bOR: count += 1
        return count
s = Solution()
for inp, out in [
        ([3,1],2),
        ([2,2,2],7),
        ([3,2,1,5],6),
        (list(range(1,16)),5),
    ]:
    res = s.countMaxOrSubsets(inp)
    print(res,out, res == out)
