COLORS = {
        'U': 0,
        'R': 1,
        'Y': 0b10,
        'O': 0b11,
        'B': 0b100,
        'P': 0b101,
        'G': 0b110,
        'A': 0b111,
}

for t in range(int(input())):
    n = int(input())
    s = input().strip()
    s = [COLORS[c] for c in s]
    res = 0
    for bits in (1,2,4):
        i = 0
        while i < n:
            while i < n and s[i]&bits == 0: i += 1 # seek to next start
            if i == n: break # if no more start, break
            while i < n and s[i]&bits != 0: i += 1 # seek to next end
            res += 1
    print('Case #%d: %d' % (1+t,res) )
