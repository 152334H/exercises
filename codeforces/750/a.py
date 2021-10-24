t = int(input())
ANS = {(0,0,0): 0,
       (0,0,1): 1, # can move 1
       (0,1,0): 0, # can move 1
       (1,0,0): 1,
       (1,1,0): 1,
       (1,0,1): 0, # move 1, or swap 1 and 2
       (0,1,1): 1,
       (1,1,1): 0}
for _ in range(t):
    print(ANS[tuple(map(lambda w: int(w)%2,input().split()))])
