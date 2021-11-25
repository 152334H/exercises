for t in range(int(input())):
    a,b = map(int,input().split())
    mi,ma = min(a,b),max(a,b)
    if mi*3 < ma: print(mi) # if 3:1 ratio teams are all required
    else: print((mi+ma)//4) # some mixture of team ratios.
