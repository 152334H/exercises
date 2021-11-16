# Greedily grab groups of 1x3, and then account for the remaining squares.
for t in range(int(input())):
    n,m = map(int,input().split())
    threes = n//3
    threes *= m
    threes += (n%3)*(m//3)
    remainder = (n%3)*(m%3)
    if remainder == 0: print(threes)
    elif remainder < 3: print(threes+1)
    else: print(threes+2)
