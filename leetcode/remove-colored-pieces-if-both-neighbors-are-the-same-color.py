from re import findall
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        def calctotal(ls): return sum(max(0,len(s)-2) for s in ls)
        alice = calctotal(findall('A+', colors))
        bob = calctotal(findall('B+', colors))
        return alice > bob
        

for i,o in [("AAABABB", True),
        ("AA", False),
        ("ABBBBBBBAAA", False)]:
    s = Solution()
    res = s.winnerOfGame(i)
    if res != o:
        print(i,o,res)
        exit()
