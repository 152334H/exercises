'''lots of failed attempts here. I ultimately missed the important observation of len <= 7.'''
from collections import defaultdict as dd
from functools import lru_cache
for t in range(int(input())):
    n = int(input()) # length of s
    s = input().strip() # string containing only 'a' 'b' and 'c'
    ''' find the length of the smallest substring where
    - length >= 2
    - 'a' appears more often than 'b'
    - 'a' appears more often than 'c'
    '''
    '''
    sat = {c:[0] for c in 'abc'}
    a_positions = []
    for i,c in enumerate(s):
        if c == 'a': a_positions.append(i)
        for k in sat: sat[k].append(sat[k][-1]+(c==k))
    INVALID = 10**7
    @lru_cache(maxsize=None)
    def dp(start, end):
        while start < end and s[start] != 'a': start += 1
        while start < end and s[end-1] != 'a': end -= 1
        if end-start < 2: return INVALID
        ctr = {k:sat[k][end]-sat[k][start] for k in sat}
        if ctr['a'] < 2: return INVALID
        # remove left, remove right, or try this one.
        mi = dp(start+1,end)
        mi = min(mi, dp(start,end-1))
        if ctr['b'] < ctr['a'] and ctr['c'] < ctr['a']:
            mi = min(mi, end-start)
        return mi
    res = dp(0,n)
    print(-1 if res == INVALID else res)
    '''
    """
    i, length = 0, 2
    ctr = dd(int)
    for c in s[:2]: ctr[c] += 1
    mi = float('inf')
    while i+length < n:
        shrink = False
        if ctr['a'] > ctr['b'] and ctr['a'] > ctr['c']: # shrink left
            mi = min(mi, length)
            shrink = True
        if shrink or s[i] != 'a' and length > 2:
            ctr[s[i]] -= 1 # remove left char
            length -= 1
            i += 1
        else: # grow right
            length += 1
            ctr[s[i+length-1]] += 1
    if ctr['a'] > ctr['b'] and ctr['a'] > ctr['c']:
        mi = min(mi, length)
    
    if mi == float('inf'): print('-1')
    else: print(mi)
    """
    '''
    for length in range(2,n+1):
        ctr = dd(int)
        for i in range(length): ctr[s[i]] += 1
        for i in range(n-length):
            if ctr['a'] > ctr['b'] and ctr['a'] > ctr['c']: break
            ctr[s[i]] -= 1
            ctr[s[i+length]] += 1
        else:
            if ctr['a'] > ctr['b'] and ctr['a'] > ctr['c']: pass
            else: continue
        print(length)
        break
    else: print('-1')
    '''
    sat = {c:[0] for c in 'abc'}
    a_positions = []
    for i,c in enumerate(s):
        if c == 'a': a_positions.append(i)
        for k in sat: sat[k].append(sat[k][-1]+(c==k))
    #
    substrings = [(p,1,{'a':1,'b':0,'c':0}) for p in a_positions]
    mi = float('inf')
    while len(substrings) > 1:
        nsub = []
        for i in range(len(substrings)-1):
            # try to merge substrings[i] with substrings[i+1]
            cur,nxt = substrings[i:i+2]
            cur_end = cur[0]+cur[1]
            res = nxt[2].copy()
            for k in res: res[k] += cur[2][k]
            for k in sat:
                add = sat[k][nxt[0]]-sat[k][cur_end]
                res[k] += add
            merged = (cur[0],nxt[0]-cur[0]+nxt[1],res)
            if res['a'] > res['b'] and res['a'] > res['c']:
                mi = min(mi, merged[1])
            nsub.append(merged)
        if mi != float('inf'): break
        substrings = nsub
    else: # nothing
        print('-1')
        continue
    print(mi)

