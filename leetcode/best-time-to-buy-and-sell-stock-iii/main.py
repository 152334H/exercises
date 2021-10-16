from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''states:
        - have never bought anything
        - have bought first item
        - have sold first item
        - have bought second item
        - have sold second item
        '''
        dp = [[0,-99999,-99999,-99999,-99999] for i in range(len(prices)+1)]
        for i,p in enumerate(prices):
            dp[i+1][0] = dp[i][0] # this one is kinda a waste.
            dp[i+1][1] = max(dp[i][1], dp[i][0]-p)
            dp[i+1][2] = max(dp[i][2], dp[i][1]+p)
            dp[i+1][3] = max(dp[i][3], dp[i][2]-p)
            dp[i+1][4] = max(dp[i][4], dp[i][3]+p)
        return max(dp[len(prices)])

obj = Solution()
for i,o in [([3,3,5,0,0,3,1,4],6),
        ([1,2,3,4,5],4),
        ([7,6,4,3,1],0),
        ([1],0)]:
    res = obj.maxProfit(i)
    if res != o:
        print(i,o,res)
