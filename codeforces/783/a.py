

for t in range(int(input())):
    n,m = map(int,input().split())
    mhat = n+m-2
    mi = min(n,m)
    diff = abs(n-m)-1
    if diff >= 1:
        if mi <= 1: mhat = -1
        else: mhat += diff + (diff&1)
    print(mhat)
