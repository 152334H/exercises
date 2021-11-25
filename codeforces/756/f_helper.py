# to generate random test cases for f
from random import randint
t = randint(1,5)
print(t)
for i in range(t):
    n = randint(1,100)
    s = randint(1,1000)
    print(n,s)
    a = [randint(-100,100) for i in range(n)]
    print(' '.join(map(str,a)))
