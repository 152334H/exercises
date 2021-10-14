def numSquare(n: int) -> int:
    border = [n]
    seen = set()
    for l in range(n+1):
        nb = []
        for v in border:
            if v in seen: continue
            if not v: return l
            seen.add(v)
            for i in range(1,9999):
                sq = i*i
                if sq > v: break
                nb.append(v-sq)
        border = nb
print(numSquare(4586))
