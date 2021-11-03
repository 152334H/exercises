''' Just sort and try removing every minimum. '''
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print(a[0])
        continue
    a.sort()
    ma_min = a[0]
    add = 0
    for v in a:
        if v+add > ma_min:
            ma_min = v+add
        add += -v-add
    print(ma_min)
