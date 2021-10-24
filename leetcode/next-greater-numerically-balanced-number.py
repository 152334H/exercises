from collections import defaultdict as dd
def is_bal(n: int):
    ctr = dd(lambda: 0)
    while n:
        rem = n%10
        ctr[rem] += 1
        n //= 10
    return all(k==v for k,v in ctr.items())

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        # silly brute-force solution
        for i in range(1,99999999):
            if is_bal(n+i): return n+i

