from typing import List
DELTA = [(1,0),(0,1),(-1,0),(0,-1)]
DIRS = 'ENWS'
class Point(tuple):
    def __add__(self, other):
        return Point(self[0] + other[0], self[1] + other[1])
class Robot:
    def __init__(self, width: int, height: int):
        self.POSSIBLE = [[i,0] for i in range(width)] + \
                        [[width-1,i] for i in range(1,height)] + \
                        [[i,height-1] for i in range(width-1)][::-1] + \
                        [[0,i] for i in range(1,height-1)][::-1]
        self.ind = 0
        self.w, self.h = width, height
        self.just_started = True
        '''
        self.d = 0 # ENWS
        self.wall = (width+height-2)*2
        '''
        
    def move(self, num: int) -> None:
        self.just_started = False
        self.ind += num
        self.ind %= len(self.POSSIBLE)

    def getPos(self) -> List[int]:
        return self.POSSIBLE[self.ind]

    def getDir(self) -> str:
        if self.ind == 0 and not self.just_started: return 'South'
        if self.ind < self.w: return 'East'
        if self.ind < self.w + self.h - 1: return 'North'
        if self.ind < self.w*2 + self.h-2: return 'West'
        return 'South'
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.move(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
r = Robot(2,2)
print(r.getPos())
print(r.getDir())
r.move(1)
print(r.getPos())
print(r.getDir())
r.move(1)
print(r.getPos())
print(r.getDir())
r.move(1)
print(r.getPos())
print(r.getDir())
r.move(1)
print(r.getPos())
print(r.getDir())
r.move(1)
'''
r = Robot(6,3)
r.move(2)
r.move(2)
assert r.getPos() == [4,0]
assert r.getDir() == 'East'
print(r.getPos())
r.move(2)
print(r.getPos())
r.move(1)
print(r.getPos())
r.move(4)
print(r.getPos())
assert r.getPos() == [1,2]
assert r.getDir() == 'West'
'''
