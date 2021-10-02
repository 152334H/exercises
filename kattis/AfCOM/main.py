from functools import reduce
N = int(input())
M = 500001
parent = [i for i in range(M)]
lens = [1 for i in range(M)]
def findset(x:int) -> int: # locate the set id for an element
    p = parent[x]
    if p == x: return x
    parent[x] = findset(p)
    return parent[x]
def union(x:int,y:int) -> int: # unify the sets containing x and y
    a,b = findset(x), findset(y)
    if a != b:
        parent[b] = a
        lens[a] += lens[b]
    return a # return id of the merged set
count = 0
for recipe in (list(map(int,input().split()))[1:] for _ in range(N)):
    groups = set(findset(x) for x in recipe)
    print(recipe, groups, lens[:6])
    if sum(lens[g] for g in groups) == len(recipe): # valid
        reduce(union, groups)
        count += 1
print(count)
