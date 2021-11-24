# i did not realise the answer could be 0. So unsolved.
'''with (1,1) and (n,m), we'll have
x-1 + y-1 = b1
n-x + m-y = b2
where n,m,bi are known constants, which should always make x and y solvable.'''
"""
for t in range(int(input())):
    n,m = map(int,input().split())
    if min(n,m) == 1: print(1)
    else: print(2)
    print(min(n,m))
"""
from random import randint
rand = lambda: randint(1,10**9)
n,m = rand(),rand()
x,y = randint(1,n), randint(1,m)
print('ans:  ',x,y)
b1 = x-1 + y-1
print('guess:',end=' ')
if min(n,m) == 1:
    guess_x,guess_y = (1,1)
    if n == 1: guess_y += b1
    else: guess_x += b1
else:
    b2 = x-1 + m-y
    guess_x = (b1+b2+2-m)//2+1
    guess_y = b1-guess_x+2
assert(x == guess_x and y == guess_y)
print(guess_x,guess_y)
