from collections import namedtuple, deque
from heapq import heappush, heappop
# Sort by increasing drop-off time, then by in-store before remote, then by increasing fill time.
Prescription = namedtuple('Prescription', ['d', 'rem', 'k'])
n,tn = map(int, input().split())
ordered_input = (deque(),deque())
q = []
prev_d = 0

for i in range(n):
    tmp = input().split()
    pres = Prescription(int(tmp[0]), tmp[1]=='R', int(tmp[2]))
    if prev_d < pres.d:
        prev_d = pres.d
        for t in sorted(q): ordered_input[t[1]].append(t)
        q = []
    q.append(pres)
for t in sorted(q): ordered_input[t[1]].append(pres)

Work = namedtuple('Work', ['end', 'start', 'rem'])
class Pharmacy:
    def __init__(self, orders: tuple): #Tuple[List,List]
        self.orders = orders
        self.time = 0
        self.techies = []
        self.completion_time = [[],[]]
        def gen():
            while any(self.orders): yield self.unsafe_next_order()
            return
        for nxt in gen():
            # Starting a new prescription is the primary driver of time.
            # At the start of each loop, either self.time has been set to nxt.d, or self.time was set by the _last released techie_.
            # In either case, self.time is correct.
            heappush(self.techies, Work(end=self.time+nxt.k, start=nxt.d, rem=nxt.rem))
            # if no techies are active, pass.
            # if there is a techie that _should be finished_, complete it.
            # if no techies will be finished by this time, but all of them are still occupied, shift time forward to the next techie to be released.
            while self.techies and (self.techies[0].end <= self.time or len(self.techies) == tn):
                done = heappop(self.techies)
                if done.end > self.time: # DO NOT TIME TRAVEL BACK
                    self.time = done.end # We need to drive time forward in the event that all techies are still filled at self.time.
                self.completion_time[done.rem].append(done.end-done.start)
        for t in self.techies:
            self.completion_time[t.rem].append(t.end-t.start)
        print(self.completion_time)
    def unsafe_next_order(self):
        for q in self.orders: # note that orders[0] refers to in-house orders.
            if q and self.time >= q[0].d: return q.popleft() # grab any order that is already here by self.time. In this case, the time of start for thisorder is self.time and not .d
        # at this point the next order must come from a .d > t
        # pick remote ONLY IF there is no in-house order before/during t AND the next remoteorder comes before the next in-house
        # assume that at least one in self.orders[] is valid
        ind = 1 if not self.orders[0] else 0 if not self.orders[1] else\
                self.orders[0][0].d > self.orders[1][0].d
        ret = self.orders[ind].popleft()
        self.time = ret.d
        return ret
    
print(' '.join(str(0 if not ls else sum(ls)/len(ls))
    for ls in Pharmacy(ordered_input).completion_time))

'''
4 1
1 R 2
2 R 5
3 R 2
6 S 2

should pick 1 R 2; time moves to 3
should pick 3 R 2; time moves to 5 <-- this is the problem.
should pick 2 R 5; time moves to 10
should pick 6 S 2; time moves to 12

expected: 6.0 (2+2+8)/3==4.0
'''
