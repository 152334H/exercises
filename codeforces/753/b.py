t = int(input())
def fast(iseven: bool, n: int) -> int:
    '''n > 0. O(1).'''
    sign = (1,-1)[iseven]
    x0 = 1*sign
    bound = (n+1)//4 # want sum(8n-3 for n in 1..=bound1) == bound1*(8bound1-3+5)/2
    x0 -= sign*(4*bound+1)*bound
    bound = (n-1)//4 # want sum(8n+1 for n in 1..=bound) == bound*(8bound+1+9)/2
    x0 += sign*(4*bound+5)*bound
    #x0 -= sign*sum(8*n-3 for n in range(1,1+(n+1)//4))
    #x0 += sign*sum(8*n+1 for n in range(1,1+(n-1)//4))
    mo = n%4
    if mo == 1: pass
    elif mo == 2: x0 -= sign*n
    elif mo == 3: pass
    else: x0 += sign*n
    return x0

def slow(iseven: bool, n: int) -> int:
    '''This function exists to check my other code.'''
    x0 = -1 if iseven else 1
    for i in range(2,n+1):
        x0 += i*(-1,1)[(x0+(not iseven))%2]
    return x0

for _ in range(t):
    x0,n = map(int,input().split())
    '''if x0 is even, then
    5 9 13
    -1 +2 +3 -4 -5 +6 +7 ... == -1
    + sum(8n-3 for n in range(1,1+(n+1)//4))
    - sum(8n+1 for n in range(1,1+(n-1)//4))
    otherwise,
    +1 -2 -3 +4 +5 -6 -7 ...'''
    if n == 0: print(x0)
    else: print(x0+fast(x0%2==0,n))
