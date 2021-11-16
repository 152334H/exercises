from string import ascii_lowercase
for t in range(int(input())):
    s = input().strip()
    f = input().strip()
    lower_bound = {} # lower_bound[c] == index of first character in f lexiographically greater-than-or-equal-to c
    f_ind = 0
    for c in ascii_lowercase:
        lower_bound[c] = f_ind
        if f_ind < len(f) and f[f_ind] == c: f_ind += 1

    res = 0
    for c in s:
        gte_ind = lower_bound[c]
        hi = f[0] if gte_ind == len(f) else f[gte_ind]
        lo = f[gte_ind-1] # -1 will work here
        possible = (abs(ord(c)-ord(hi)), abs(ord(c)-ord(lo)))
        res += min(min(26-p,p) for p in possible)
    print('Case #%d: %d' %(t+1,res))
