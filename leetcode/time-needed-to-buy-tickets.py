from typing import List
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        loops = tickets[k]
        # for each person in the queue, buy all tickets or buy tickets[k] tickets.
        res = sum(min(tickets[i],loops) for i in range(0,k+1))
        # minus 1 if the person is behind k in the queue.
        res+= sum(min(tickets[i],loops-1) for i in range(k+1,len(tickets)))
        return res
s = Solution()
for (inp,out) in [
        (([2,3,2],2), 6),
        (([5,1,1,1],0),8)
    ]:
    print(inp)
    assert s.timeRequiredToBuy(inp[0],inp[1]) == out
