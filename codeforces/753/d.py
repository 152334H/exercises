'''I failed this problem because I _completely_ misunderstood the problem for a solid hour. Uploading for posterity.'''
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    rb = input().strip()
    # find the maximum and minimum red and blue elements
    rmax,bmax = -10**10, -10**10
    rmin,bmin = 10**10, 10**10
    rls,bls = [],[]
    for i in range(n):
        if rb[i] == 'R':
            rmax = max(rmax, a[i])
            rmin = min(rmin, a[i])
            rls.append(a[i])
        else:
            bmax = max(bmax, a[i])
            bmin = min(bmin, a[i])
            bls.append(a[i])
    rls.sort()
    bls.sort()
    red_must_solve = [v for v in range(bmax+1, n+1)]
    blue_must_solve = [v for v in range(rmin-1, -1, -1)]
    """
    '''shift rmax/rmin and bmax/bmin to be within 1..=n.
    If this is not possible, then give up.'''
    if max(rmax-rmin,bmax-bmin) > n-1:
        print("NO")
        continue
    '''shift the arrays to be within 1..=n.'''
    rls.sort()
    rls = [x-rmin+1 for x in rls]
    r_holes = list(filter(lambda v: v > 1, [rls[i]-rls[i-1] for i in range(1,len(rls))]))
    bls.sort()
    bls = [x-bmin+1 for x in bls]
    b_segs = []
    prev = None
    for v in bls:
        if v-1 == prev: b_segs[-1] += 1
        else: b_segs.append(1)
        prev = v
    # now we try to fit the line.
    if -2 > len(r_holes) - len(b_segs) > 0:
        print("NO")
        continue
    # if b is within r, len(r_holes) == len(b_segs)
    # elif r is within b, len(r_holes) +2 == len(b_segs) 
    # else: len(r_holes)+1 == len(b_segs)
    if len(r_holes) == len(b_segs): # b is within r
        print("YES" if r_holes == b_segs and (rls[0],rls[-1]) == (1,n) else "NO") # and...
        continue
    elif len(r_holes) +2== len(b_segs): # r is within b
        print("YES" if r_holes == b_segs[1:-1] and (bls[0],bls[-1]) == (1,n) else "NO")
    else: # len(r_holes) == len(b_segs) + 1
        print("YES" if r_holes == b_segs[1:] or r_holes == b_segs[:-1] else "NO")
    """

