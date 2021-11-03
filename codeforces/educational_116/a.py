t = int(input())
from collections import defaultdict as dd
def find_change(orig: str, new:str) -> tuple:
    orig_score = (1,0) if orig == 'ab' else (0,1) if orig == 'ba' else (0,0)
    new_score = (1,0) if new == 'ab' else (0,1) if new == 'ba' else (0,0)
    return (new_score[0] - orig_score[0], new_score[1] - orig_score[1])
for _ in range(t):
    s = input().strip()
    ab,ba = 0,0
    for i in range(len(s)-1):
        if s[i] == 'a' and s[i+1] == 'b':
            ab += 1
        elif s[i] == 'b' and s[i+1] == 'a':
            ba += 1
    # find the minimum number of steps needed to make ab == ba
    for i in range(len(s)):
        if ab == ba: break
        change = (0,0)
        c = s[i]
        flipped = 'a' if c == 'b' else 'b'
        if i > 0:
            change = find_change(s[i-1:i+1], s[i-1]+flipped)
        if i < len(s)-1:
            tmp = find_change(s[i:i+2], flipped+s[i+1])
            change = (change[0] + tmp[0], change[1] + tmp[1])
        #greedy
        new_state = (ab + change[0], ba + change[1])
        if abs(new_state[0] - new_state[1]) < abs(ab - ba):
            ab += change[0]
            ba += change[1]
            s = s[:i] + flipped + s[i+1:]
    print(s)

