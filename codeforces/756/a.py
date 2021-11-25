for t in range(int(input())):
    n = [int(c) for c in input().strip()]
    if n[-1] & 1 == 0: print(0) # number is already even.
    elif n[0] & 1 == 0: print(1) # last digit can be swapped with first
    elif any(d&1 == 0 for d in n): print(2) # swap middle for first, then first for last.
    else: print(-1) # give up.
