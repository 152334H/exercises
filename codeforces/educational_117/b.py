for t in range(int(input())):
    n,a,b = map(int,input().split())
    '''A permutation of length n is an array p=[p1,p2,…,pn] which contains every integer from 1 to n (inclusive) exactly once. For example, p=[4,2,6,5,3,1] is a permutation of length 6
    You are given three integers n, a and b, where n is an even number. Print any permutation of length n that the minimum among all its elements of the left half equals a and the maximum among all its elements of the right half equals b.'''
    if a > n//2 + 1: # dead
        print(-1)
    elif b < n//2: # dead
        print(-1)
    else: # possible but still not guaranteed. O(n) attempt to find a permutation that satisfies the condition.
        als = [a]
        for v in range(n,-1,-1):
            if len(als) == n//2: break
            if v < a: break
            if v != a and v != b: als.append(v)
        if len(als) != n//2:
            print(-1)
            continue
        #
        bls = [b]
        for v in range(1,n+1):
            if len(bls) == n//2: break
            if v > b: break
            if v != a and v != b: bls.append(v)
        if len(bls) != n//2:
            print(-1)
            continue
        #
        print(' '.join(map(str,als+bls)))
