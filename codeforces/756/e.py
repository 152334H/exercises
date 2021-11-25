# only part 1 of the problem
from collections import defaultdict
for t in range(int(input())):
    '''n and k (1≤k<n≤2*10**5) — the no. of rooms and no. of friends
    integers x1,x2,…,xk (2≤xi≤n) — friend i is in room xi. xi is unique
    The next n−1 lines contain descriptions of the corridors, two numbers per line vj and uj (1≤uj,vj≤n) — numbers of rooms that connect the j corridor. All corridors are bidirectional. From any room, you can go to any other by moving along the corridors.'''
    input()
    n,k = map(int,input().split())
    x = list(map(int,input().split()))
    g = defaultdict(set)
    for _ in range(n-1):
        v,u = map(int,input().split())
        g[v].add(u)
        g[u].add(v)
    def game(): # just BFS the friends and vlad simultaneously.
        enemy_tiles = set(x)
        enemy_border = x
        vlad_tiles = set([1])
        vlad_border = [1]
        while vlad_border:
            new_enemy_border = []
            for u in enemy_border:
                for v in g[u]:
                    if v not in enemy_tiles:
                        enemy_tiles.add(v)
                        new_enemy_border.append(v)
            enemy_border = new_enemy_border
            #
            new_vlad_border = []
            for u in vlad_border:
                for v in g[u]:
                    if v not in vlad_tiles and v not in enemy_tiles:
                        if len(g[v]) == 1: # vlad has won
                            return "YES"
                        vlad_tiles.add(v)
                        new_vlad_border.append(v)
            vlad_border = new_vlad_border
        return "NO"
    print(game())
