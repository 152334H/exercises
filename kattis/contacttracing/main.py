'''This is an attempt at implementing a balanced interval tree as a 
solution for the problem. This solution does _not_ run fast enough to
succeed on the hidden test cases, but it will handle dense graphs a lot
better than the Rust solution, because people that are sick will only be
returned once in this solution (as they are pruned from the interval tree)
as opposed to the BFS solution (which will have to deal with O(N^2) operations
just by building the graph alone, in the worst-case situation).'''

segtree = None
def safeheight(interval): return -1 if interval is None else interval.height
class Interval: # interval follows range() convention of [)
    '''The invariant here is sorting based on the _minimum value_ of each interval.
    The maximum value possible (uninclusive) within a subtree is given by self.max'''
    def __init__(self, r: range, n: int):
        self.low, self.high = r.start, r.stop
        self.max = self.high
        self.L, self.R = None, None
        self.n = n
        self.parent = None
        self.height = 0
    def bf(self): return safeheight(self.L) - safeheight(self.R)
    def isRoot(self): return False
    def __str__(self):
        return 'Interval({}({},{}), max={}, height={}, parent={})'.format(
            self.n, self.low, self.high, self.max, self.height, None if not self.parent else 'root' if self.parent.isRoot() else (self.parent.low, self.parent.high))
    def rotateLeft(self): # assert self.R is not None
        r = self.R
        if self.parent is not None: self.parent.changeChild(self, r)
        self.parent = r
        self.R = r.L
        if r.L is not None: r.L.parent = self
        r.L = self
        self.fixHeight()
        r.fixHeight()
    def fixHeight(self): self.height = max(safeheight(self.L), safeheight(self.R)) + 1
    def rotateRight(self): # assert self.L is not None
        l = self.L
        if self.parent is not None: self.parent.changeChild(self, l)
        #    if self.parent.L is self: self.parent.L = l
        #    else: self.parent.R = l
        #l.parent = self.parent
        self.parent = l
        self.L = l.R
        if l.R is not None: l.R.parent = self
        l.R = self
        self.fixHeight()
        l.fixHeight()
    def changeChild(self, child: 'Interval', to: 'Interval'): # assume child == self.L or self.R
        # THIS WILL NOT UPDATE THE HEIGHT CORRECTLY.
        if self.L == child: self.L = to
        elif self.R == child: self.R = to
        else: raise RuntimeError("{} is not a child of {}".format(str(child), str(self)))
        if to is not None: to.parent = self
    def successor(self) -> 'None or Interval':
        if self.R is None: # go upwards
            node = self.parent
            while node is not None and node.low < self.low: node = node.parent
            return node # this could be None.
        else: # go right, and then left all-the-way
            node = self.R
            while node.L is not None: node = node.L
            return node
    def remove(self, it: 'Interval'):
        '''questions:
        - is height correct? parent?
        - what if `it` is the root?
        '''
        #global segtree
        #segtree.display()
        #print('{}.remove({})'.format(str(self), str(it)))
        #print('{}|{}'.format(str(self.L), str(self.R)))
        if self is it: # remove self!
            if it.L is None and it.R is None: # remove leaf
                self.parent.changeChild(self, None)
            elif it.L is None or it.R is None: # connect self.child to self.parent
                self.parent.changeChild(self, it.L or it.R)
            else: # there are two children. uh-oh.
                suc = self.successor() # this will not be None.
                #print('if-else: suc={}'.format(str(suc)))
                old_parent = suc.parent
                self.parent.changeChild(self, suc)
                suc.parent,new_parent = old_parent,suc.parent
                self.R.remove(suc)
                suc.parent = new_parent
                suc.L, suc.R = self.L, self.R
                # in the case where self.L || self.R == suc, suc.R || suc.L will be None.
                if suc.R is not None: suc.R.parent = suc
                if suc.L is not None: suc.L.parent = suc
                self.fixHeight()
                suc.fixHeight()
        elif it.low < self.low: # go left
            if self.L is not None: self.L.remove(it)
            self.fixHeight()
        else: # go right
            if self.R is not None: self.R.remove(it)
            self.fixHeight()
    def add(self, oth: 'Interval'):
        if oth.low < self.low: # this cheap comparison will bite us later.
            if self.L is None:
                self.L = oth
                self.L.parent = self
            else: self.L.add(oth)
        else:
            if self.R is None:
                self.R = oth
                self.R.parent = self
            else: self.R.add(oth)
        # post-addition.
        if oth.high > self.max: self.max = oth.high
        self.fixHeight()
        if abs(self.bf()) > 1: # this subtree is unbalanced!
            if self.bf() > 0: # +2
                if self.L.bf() < 0: # == -1
                    self.L.rotateLeft()
                self.rotateRight() # always do this
            else: # bf() == -2
                if self.R.bf() > 0: # 1
                    self.R.rotateRight()
                self.rotateLeft() # always do this
    def overlaps(self, oth: range):
        if self.high > oth.start and oth.stop > self.low: # if overlapping
            yield self
        if self.L is not None and self.L.max > oth.start: yield from self.L.overlaps(oth)
        if self.R is not None and self.low < oth.stop: yield from self.R.overlaps(oth)
class ITree(Interval):
    def display(self):
        print('===DISPLAY===')
        q = [(0,self.root)]
        while q:
            tabs,node = q.pop()
            if node.L is not None: q.append((tabs+1, node.L))
            if node.R is not None: q.append((tabs+1, node.R))
            print('\t'*tabs + str(node))
        print('=====END=====')
    def isRoot(self): return True
    def __init__(self, intervals: list):
        self.root = None
        self.low = float('-inf')
        for it in intervals: self.add(it)
    def changeChild(self, child: 'Interval', to: 'Interval'):
        if self.root is child: self.root = to
        else: raise RuntimeError("{} is not the root element.".format(str(child)))
        if to is not None: to.parent = self
    def remove(self, it: 'Interval'): self.root.remove(it)
    def add(self, oth: "Interval"):
        if self.root is None:
            self.root = oth
            self.root.parent = self
        else: self.root.add(oth)
    def overlaps(self, oth: range): yield from self.root.overlaps(oth)

def trav(st): # for debugging
    if st.L is not None: yield from trav(st.L)
    yield st.low, st.high
    if st.R is not None: yield from trav(st.R)

N,D = map(int, input().split())
C, *infected = map(int, input().split())
infected = set(infected)
timeline = [None] + [(lambda t: Interval(range(t[0],t[1]+1), n=i+1))([int(s) for s in input().split()]) for i in range(N)]
infections = [range(timeline[n].low, timeline[n].high) for n in infected]
'''variables:
N,D,C: as defined in the problem
infected: the final set of people that have been infected afer D days
timeline: a list where timeline[i] has the time interval for person i
infections: the time ranges that are poisoned by infections on the _current day_.
segtree: a constant self-balancing segment tree for all of the time ranges available.
'''

# Need a datastructure that can figure out "which ranges overlap with range R" in O(1) time, while also accepting range updates in O(!)
segtree = ITree(timeline[1:])
for days in range(D): # for each day,
    new_infections = []
    for r in infections: # for every time range poisoned by infection,
        ma,mi = r.stop, r.start
        if segtree.root is None: break
        for oth in list(segtree.overlaps(r)): # for every range overlapping with inf
            segtree.remove(oth) # note that the segtree is getting modified in-loop, so we need to use list() above
            infected.add(oth.n)
            if oth.high > ma: ma = oth.high
            if oth.low < mi: mi = oth.low
        # reminder that segtree is linear to the number of elements returned.
        if mi < r.start: new_infections.append(range(mi, r.start))
        if ma > r.stop: new_infections.append(range(r.stop, ma))
    infections = new_infections # update infections to the next day

print(' '.join(str(x) for x in sorted(infected)))
