from re import findall
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = list(map(int,findall('[0-9]+', s)))
        return all(nums[i] < nums[i+1] for i in range(len(nums)-1))
s = Solution()
for t in ("1 box has 3 blue 4 red 6 green and 12 yellow marbles",
        "hello world 5 x 5",
        "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s",
        "4 5 11 26"):
    print(s.areNumbersAscending(t))
