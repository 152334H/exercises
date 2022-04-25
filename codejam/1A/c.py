
from collections import defaultdict as dd
from random import randint

for t in range(int(input())):
    E,W = map(int,input().split()) # E: number of exercises, W: number of weight types (numbered 1..=W)
    #E,W = 10, 3 # E: number of exercises, W: number of weight types (numbered 1..=W)
    # X[e-1][i-1]: number of weights of type i required for exercise e. 
    X = [list(map(int,input().split())) for e in range(E)]
    #X = [list(randint(0,3) for _ in range(W)) for e in range(E)]
    #for l in X: print(' '.join(map(str,l)))
    # The bottom weight should be the one that sticks around the longest.
    next_case_of = [[(E,-1,-1,-1)]*W for _ in range(E+1)] # next_case_of[e][t][w]: the first exercise that requires exactly w weights of type t, ignoring all exercises before e
    for e in reversed(range(E)):
        for t in range(W):
            new_tup = list(next_case_of[e+1][t])
            new_tup[X[e][t]] = e
            next_case_of[e][t] = tuple(new_tup)
    #print(next_case_of)

    ops = 0

    stack = []
    added = dd(int)
    print(next_case_of)
    for e in range(E):
        while any(added[t] > X[e][t] for t in range(W)):
            added[stack.pop()] -= 1
            ops += 1
        print('postpop:', stack, added)
        weights = sum(X[e])
        while len(stack) < weights:
            best_t, best_e = -1,-1
            for t in range(W):
                for req in range(added[t]+1, 4):
                    next_e = next_case_of[e][t][req]
                    if next_e == -1: continue
                    if next_e > best_e: best_t, best_e = t, next_e
                    break
            stack.append(best_t)
            added[best_t] += 1
            ops += 1
        print('postpush:', stack)

    print(ops+len(stack))



