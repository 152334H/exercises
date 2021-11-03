t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    digits = [0]
    prev = 0
    for a in map(int,input().split()):
        if a == 0: continue
        #
        ddiff = a-prev
        extra = (10**ddiff)-1
        if k < extra: break
        digits[-1] += extra
        for _ in range(ddiff): digits.append(0)
        k -= extra
        prev = a
    if k > 0:
        digits[-1] += k +1
    print(sum(10**i*digits[i] for i in range(len(digits))))
    #print(digits[::-1])

