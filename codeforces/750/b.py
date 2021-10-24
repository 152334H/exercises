for _ in range(int(input())):
    n = int(input())
    zeros,ones = 0,0
    for i in map(int, input().split()):
        if i == 1: ones += 1
        if i == 0: zeros += 1
    print(ones<<zeros)
