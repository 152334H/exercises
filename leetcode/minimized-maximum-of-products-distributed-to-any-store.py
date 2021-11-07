#!/usr/bin/env python3.8
from collections import deque,defaultdict as dd
from typing import List,Optional
from math import ceil
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        '''
        let ls be a list of len(quantities), where sum(ls) == n.
        find the minimum value of max(ceil(quantities[i]/ls[i]) for i in range(len(ls)))
        '''
        best = [10**9 for _ in range(n+1)] # best[i] is the best minimum if everything previously has to be distributed to n retail stores.
        for i in range(1,n+2-len(quantities)):
            best[i] = ceil(quantities[0]/i)
        # this is something in the bound of O(n**2.5). So TLE.
        for i,q in enumerate(quantities[1:],1):
            dupe = best[:]
            for k in range(len(best)): best[k] = 10**9
            for total_stores in range(i+1, n+2-len(quantities)+i):
                mi,ma = 1, total_stores+1-i
                while mi < ma:
                    cur_stores = (mi+ma)//2
                    left_best = max(ceil(q/cur_stores), dupe[total_stores-cur_stores])
                    right_best = max(ceil(q/(1+cur_stores)), dupe[total_stores-cur_stores-1])
                    if left_best < right_best: # go left
                        ma = cur_stores
                    elif left_best > right_best:
                        mi = cur_stores+1
                    else: mi = ma = cur_stores
                print(mi,ma)
                best[total_stores] = max(ceil(q/mi), dupe[total_stores-mi])
                '''
                for cur_stores in range(1,total_stores+1-i):
                    new_best = max(ceil(q/cur_stores), dupe[total_stores-cur_stores])
                    if new_best >= best[total_stores]: break # new_best will only go up after this
                    best[total_stores] = new_best
                '''
        return best[n]

s = Solution()
for inp,out in [
        ((6,[11,6]), 3),
        ((7,[15,10,10]), 5),
        ((1,[100000]), 100000),
        ((99984, [455,971,761,93461,614,966,226,671,43,200,41,55,301,613,28,172,346,123,569,21780,815,226,65085,935,267,81,15,63418,242,695,44949,920,245,120,69422,720,48735,734,698,522,145,654,99,370,706,69740,685,810,47178,89531,355,552,498,74716,44,864,78,98507,49481,88,32744,128,533,313,932,950,48,713,603,677,237,23982]), 1)
    ]:
    res = s.minimizedMaximum(*inp)
    print(inp,out)
    assert res == out

