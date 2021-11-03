from math import ceil
t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    avail = 1
    hours = 0
    while avail < k and avail < n:
        avail <<= 1
        hours += 1
    # now there are avail computers available
    if avail >= n: # all computers are available
        print(hours)
    else:
        hours += (n-avail)//k
        if (n-avail)%k: hours += 1
        print(hours)
