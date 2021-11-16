# based on the very simple observation that all the answers in the
# test cases were multiples of square numbers.
from math import gcd
for t in range(int(input())):
    u,v = map(int,input().split())
    g = gcd(u,v)
    u,v = u//g,v//g
    x,y = (-u**2),v**2
    print(x,y)

