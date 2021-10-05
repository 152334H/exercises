PONES = ['Twilight Sparkle', 'Applejack', 'Rarity', 'Pinkie Pie', 'Fluttershy', 'Rainbow Dash', 'Spike']
exploitable = [list(map(lambda c: c == '1', input().split(' '))) for _ in range(7)]
possible = [0]
bit_order = [{} for _ in range(128)]
''' This version of the loop is a lot more efficient:
for n,line in enumerate(exploitable):
    np = set()
    for v in possible:
        added = False
        for i,b in enumerate(line):
            if not b: continue
            bit = b<<i
            if v&bit: continue # don't consider this an update
            np.add(v|bit)
            bit_order[v|bit] = bit_order[v] + [(n,i)]
            added = True
        if not added: np.add(v) # if no new bits were seen, keep the old set
''' # I'm using the inefficient version to build bit_order conclusively.
for n,line in enumerate(exploitable):
    nbo = bit_order.copy()
    np = set()
    for v in possible:
        for i,b in enumerate(line):
            if not b: continue
            bit = b<<i
            if bit|v == v: continue
            np.add(v|bit)
            nbo[v|bit] = {**bit_order[v], **{n:i}}
        np.add(v)
    possible = np
    bit_order = nbo
# prune all sets in `np` that are subsets of other sets in `np`.
remove = set()
for v in np: # this is O(n^2) 
    for oth in np:
        if v == oth: continue
        if oth|v == oth: # if v is strictly a subset of oth
            remove.add(v)
            break
possible = np-remove
# `possible` is now smaller. Specifically, it's at most 7-choose-3.5 == ??? elements large.
# But if `possible` really _is_ that large, then it's highly likely that p <= 2.
# If `possible` is small, then p may be larger, but the program is still fast enough.

# screw it, bruteforce
from itertools import combinations
from functools import reduce
for r in range(1,8):
    for comb in combinations(possible,r):
        if reduce(lambda a,b: a|b, comb) == 127: #solution found
            done = 0
            print(len(comb))
            for v in comb:
                needed = 127-done
                bits = v&needed
                print(bin(bits).count('1'))
                for n,i in bit_order[bits].items(): print(PONES[n], i+1)
                done |= bits
            exit()
print("IMPOSSIBLE")
