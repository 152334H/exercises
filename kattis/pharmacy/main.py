# NOTE: this is not a simple solution for the problem. The problem statement
# lends itself well to async programming techniques that I am unfamiliar with,
# and the procedural constructs used in lieu of said techniques are ugly.
from collections import namedtuple, deque
from heapq import heappush, heappop
# Different tuples for different sorting strategies.
Order = namedtuple('Order', ['rem', 'd', 'k'])
Work = namedtuple('Work', ['end', 'start', 'rem'])

n,tn = map(int, input().split())
def getline():
    tmp = input().split()
    return Order(d=int(tmp[0]), rem=tmp[1]=='R', k=int(tmp[2]))
orders = deque(getline() for _ in range(n)) # this is just a deque so that I don't need to call reversed()

time = orders[0].d  # The current time.
# next two variables are priority queues. heapq module is weird and uses lists as backing stores.
current = []        # current[] contains every untouched prescription in the pharmacy at the current `time`.
techies = []        # techies[] contains tuples representing a single techinican working on a prescription.
completion_time = ([],[])   # two lists of end-start values. For calculating final answer.
def update_time(to: int): # assumes self.time <= to.
    global time # ugly global variable. This used to be a part of an even uglier OOP solution for this problem.
    time = to
    while orders and orders[0].d <= to:
        heappush(current, orders.popleft()))
def next_order(): # a generator wrapper to make the loop less complex
    while orders or current:
        if not current: # if there's no open orders at self.time,
            update_time(orders[0].d) # push it forward
        yield heappop(current) # pass it out

for nxt in next_order():
    # There are two events that will "drive forward time". If there are no untouched prescriptions remaining, then
    # time = nxt.d as a new prescription is dropped in. Otherwise, 
    # time will be updated by techicians as they're released. In either case, time is correct.
    heappush(techies, Work(end=time+nxt.k, start=nxt.d, rem=nxt.rem))
    # if there is a techie that _should be finished_ by now, complete it, otherwise 
    # if no techies will be finished by this time AND all of them are still occupied, shift time forward to the next techie to be released.
    while techies and (techies[0].end <= time or len(techies) == tn):
        done = heappop(techies)
        if done.end > time: # DO NOT TIME TRAVEL BACK
            update_time(done.end)
        completion_time[done.rem].append(done.end-done.start)
for done in techies: # finish remaining jobs
    completion_time[done.rem].append(done.end-done.start)

print(' '.join(str(0 if not ls else sum(ls)/len(ls)) for ls in completion_time))
