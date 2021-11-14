from collections import deque
for t in range(int(input())):
    n = int(input()) # length of binary string
    s = input().strip() # binary string
    positions = ([],[])
    for i,c in enumerate(s): positions[c=='1'].append(i)
    one_ind, zero_ind = 0, -1
    subseq_ones, subseq_zeros = [],[]
    while one_ind < len(positions[1]) and -zero_ind-1 < len(positions[0]) and positions[1][one_ind] < positions[0][zero_ind]:
        subseq_ones.append(positions[1][one_ind])
        subseq_zeros.append(positions[0][zero_ind])
        one_ind += 1
        zero_ind -= 1
    final = subseq_ones + list(reversed(subseq_zeros))
    if final:
        print(1)
        print(len(final), ' '.join(map(lambda v: str(v+1),final)))
    else: print(0)
