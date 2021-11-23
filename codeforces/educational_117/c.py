for t in range(int(input())):
    '''rather obvious binsearch problem, based on the number of emojis
    written if only `msgs` lines are written, which can be calculated
    in O(1) because sum(1..=k) == k*(k+1)//2'''
    k,x = map(int,input().split())
    def emojis_written(msgs):
        extra = msgs % k
        def formula(k): return k*(k+1)//2
        if msgs <= k: return formula(msgs)
        else: return formula(k) + formula(k-1) - formula(k-1-extra)

    lo,hi = 0,2*k-1
    if emojis_written(hi) < x: print(hi) # suppress edge case
    else: # loop invariant: e_w(lo) <= x <= e_w(hi)
        while lo < hi:
            mid = (lo+hi)//2
            if emojis_written(mid) < x: lo = mid+1
            else: hi = mid
        print(lo)
