from typing import List
from collections import defaultdict as dd
class Solution:
    # this solution is incredibly inefficient (state explosion).
    # see the rust version for a much more efficient one.
    def maxProfit(self, prices: List[int]) -> int:
        ''' this is a dp problem. maxProfit = dp[day,prieBought]
        At each day i, the choices available are:
         - skip this day (i.e. dp[day+1,priceBought] = dp[~])
         - if priceBought is None, buy (so dp[day+1,prices[i]] = dp[~]-prices[i])
         - else, sell (so dp[day+2,None] = dp[~] + prices[i])
        '''
        dp = [dd(lambda:-99999999) for _ in range(len(prices)+2)]
        dp[0][None] = 0
        for i,p in enumerate(prices):
            for priceBought,totalProfit in dp[i].items(): 
                dp[i+1][priceBought] = max(dp[i+1][priceBought], totalProfit) # skip
                if priceBought is None: dp[i+1][p] = max(dp[i+1][p], totalProfit-p)
                else: dp[i+2][None] = max(dp[i+2][None],totalProfit+p)
        best = 0
        for i in range(len(prices), len(prices)+2):
            if dp[i]: best = max(best,max(dp[i].values()))
        return best

obj = Solution()
for i,o in [([1,2,3,0,2], 3),
        ([1],0), ([1,2],1),
        ([1,2,4], 3)]:
    res = obj.maxProfit(i)
    if res != o: print(i,o,res)
