from sys import stdout
N = int(input())

# The basic idea here is to do a "quarternary search".
# A range is split into 4 parts: [AJ-only, AJ&AB, AB-only, noone].

def observe(aj: range, ab: range) -> list:
    print('Q %d %d %d %d' % (aj.start, aj.stop-1, ab.start, ab.stop-1))
    stdout.flush()
    return [x == '1' for x in input().split()]
def query(bound: range) -> range:
    lo,hi = bound.start, bound.stop
    length = hi-lo
    cuts = [lo+round(v) for v in [length/4, length/2, 3*length/4]]
    res = observe(range(lo,cuts[1]), range(cuts[0], cuts[2]))
    if res == [False, False]: return range(cuts[2], hi)
    if res == [True, False]: return range(lo, cuts[0])
    if res == [True, True]: return range(cuts[0], cuts[1])
    if res == [False, True]: return range(cuts[1], cuts[2])

scan = range(1,N+1)
for i in range(16):
    scan = query(scan)
    if len(scan) <= 1:
        print('A %d' % scan.start)
        break
    else: # account for the creature jumping
        scan = range(1 if scan.start == 1 else scan.start-1,
            N+1 if scan.stop == N+1 else scan.stop+1)
