from typing import List
def anyColor(cartridges: List[List[int]]) -> None or List[int]:
    '''
    >>> anyColor([[300000 200000 300000 500000], [300000 200000 500000 300000], [300000 500000 300000 200000]])
    [300000, 200000, 300000, 200000]
    '''
    mini = [min(ct[i] for ct in cartridges) for i in range(4)]
    if sum(mini) < 10**6: return None 
    for i in range(4):
        diff = sum(mini)-10**6
        redDiff = min(diff, mini[i])
        mini[i] -= redDiff
        if diff <= mini[i]: return mini

for t in range(int(input())):
    cartridges = [list(map(int, input().split())) for _ in range(3)]
    res = anyColor(cartridges)
    if res is None:
        print('Case #{}: IMPOSSIBLE'.format(t+1))
    else:
        print('Case #{}: {} {} {} {}'.format(t+1, *res))
