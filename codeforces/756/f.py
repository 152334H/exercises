def NSE(arr: list,add):
    n =len(arr)
    s = []
    mp = {}
    s.append(arr[0])
    for i in range(1, n):
        if (len(s) == 0):
            s.append(arr[i])
            continue
        while (len(s) != 0 and s[-1] > arr[i]+add):
            mp[s[-1]] = i
            s.pop()
        s.append(arr[i])
 
    while (len(s) != 0):
        mp[s[-1]] = None
        s.pop()
    return {arr[i]: mp[arr[i]] for i in range(n)}

for t in range(int(input())):
    n,s = map(int,input().split())
    a = list(map(int,input().split()))
    '''A subsequence a[i:j] is considered valid if and only if
    min(a[i:k] for k in range(i+1,j)) >= -s
    Find the largest possible contiguous subsequence.'''
    sat = [0]*(n+1)
    for i in range(n): sat[i+1] = sat[i] + a[i]
    next_smallest_index = NSE(sat,s)
    print(s)
    print(sat)
    print(next_smallest_index)
    print(sat[31], sat[33])
    # not sure how i ended up thinking of this.
    ans = 0
    best = None
    for i in range(n):
        j = next_smallest_index[sat[i]]
        if j is None: j = n
        else:
            assert sat[j]+s < sat[i]
            j -= 1
        if j-i > ans:
            ans = j-i
            best = (i,j)
    if best is None: print(-1)
    else: print(' '.join(map(str,[best[0]+1,best[1]])))








''' obvious O(n^2) solution that I assumed would TLE (haven't tested)
for j in range(i+1,n+1):
    if sat[j] - sat[i] >= -s:
        if j-i > ans:
            ans = j-i
            best = (i,j)
    else: break # first instance of sat[j]+s < sat[i]
'''
