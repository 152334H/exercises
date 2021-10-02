class STree():
    def __init__(self, ls: list):
        n = len(ls)
        self.t = [0 for _ in range(n)] + ls
        for i in range(n-1,0,-1):
            self.t[i] = self.t[i<<1] + self.t[i<<1|1]
        self.n = n
    def modify(self,p,v):
        p += self.n
        self.t[p] = v
        while p > 1:
            self.t[p>>1] = self.t[p] + self.t[p^1]
            p >>= 1
    def query(self, l, r):
        res = 0
        l += self.n
        r += self.n
        while l < r:
            if l&1:
                res += self.t[l]
                l += 1
            if r&1:
                r -= 1
                res += self.t[r]
            l >>= 1
            r >>= 1
        return res

get_ints = lambda: map(int, input().strip().split(' '))
_,Q = get_ints()
P = list(get_ints())
V = [p-1 for p in map(int,input())] # dirty one-indexing
trees = [STree([v==i for v in V]) for i in range(6)]

for _ in range(Q):
    q,a,b = get_ints()
    if q == 1:
        k,p = a-1,b-1 # dirty one-indexing
        # modify both trees[V[k]] && V[k] itself.
        orig_p = V[k]
        V[k] = p
        trees[orig_p].modify(k,0)
        trees[p].modify(k,1)
    elif q == 2:
        p,v = a-1,b # dirty one-indexing
        P[p] = v
    else:
        l,r = a-1,b # dirty one-indexing. r doesn't need to be changed since we want an inclusive query.
        print(sum(trees[p].query(l,r)*P[p]
            for p in range(6)))


t = STree(list(range(13)))
print(t.query(0,7))
