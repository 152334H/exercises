from typing import List
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        return sum(abs(a-b) for a,b in zip(seats,students))


for seats,students,out in [([3,1,5], [2,7,4], 4),
        ([4,1,5,9], [1,3,2,6], 7),
        ([2,2,6,6], [1,3,2,6], 4)]:
    s = Solution()
    res = s.minMovesToSeat(seats, students)
    if res != out:
        print(seats, students, out, res)
        exit()
                    
