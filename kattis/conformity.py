from collections import Counter
n = int(input())
ma = 0
total = 0
for (_,c) in Counter(frozenset(map(int,input().split())) for _ in range(n)).most_common(n):
    if c > ma: ma = c
    if ma > c: break
    else:  total += c
print(total)
