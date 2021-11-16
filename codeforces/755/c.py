# Sort and compare a[i] to b[i].
for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort(); b.sort()
    for i in range(n):
        if a[i] not in (b[i],b[i]-1): break
    else:
        print("YES")
        continue
    print("NO")
