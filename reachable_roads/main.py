from collections import defaultdict as dd, deque
for _ in range(int(input())):
    m = int(input())
    adjls = dd(lambda: [])
    for _r in range(int(input())):
        e,g = map(int, input().split())
        adjls[e].append(g)
        adjls[g].append(e)
    seen = set()
    bubbles = -1
    for i in range(m):
        if i in seen: continue
        bubbles += 1
        q = deque([i])
        while q:
            k = q.pop()
            if k in seen: continue
            seen.add(k)
            for j in adjls[k]: q.append(j)
    print(bubbles)
