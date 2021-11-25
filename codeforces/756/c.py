from collections import deque
for t in range(int(input())):
    n = int(input())
    a = deque(map(int, input().split()))
    # note that the last element has to be the largest element of p.
    p = deque([n])
    if a[0] == n: a.popleft()
    elif a[-1] == n: a.pop()
    else:
        print(-1)
        continue

    '''I have a premonition that this code is not fully correct'''
    while a:
        left,right = a[0], a[-1]
        if left < p[-1]: # could've been left
            p.appendleft(a.popleft())
        elif right < p[0]: # could've been right
            p.append(a.pop())
        else:
            print(-1)
            break
    else: print(' '.join(map(str, p)))
