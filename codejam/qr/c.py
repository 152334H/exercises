from typing import List
def longestSequence(dice: List[int]) -> int:
    ''' Each dice can provide one number smaller-than-or-equal to itself.
    Need to find the longest sequence 1..x'''
    dropped = 0
    for i,d in enumerate(sorted(dice)):
        if d < i+1-dropped: dropped += 1
    return len(dice)-dropped

for t in range(int(input())):
    n = int(input())
    S = list(map(int, input().split()))
    print(f'Case #{t+1}: {longestSequence(S)}')
