for t in range(int(input())):
    x,y = map(int,input().split())
    # A = (0,0), B = (x,y), C = ???
    # cx+cy = dab/2.0
    # cx,cy >= 0
    # abs(x-cx) + abs(y-cy) = dab/2.0
    
    dab = x+y
    if dab%2: print("-1 -1")
    else: # basically try the quarter-circle that's valid in the top-right quadrant. slow but it works.
        cx = dab//2
        for cy in range(cx+1):
            if abs(x-(cx-cy)) + abs(y-cy) == dab//2:
                print(cx-cy,cy)
                break
        else: print("-1 -1")


