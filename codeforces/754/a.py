for t in range(int(input())):
    a1,a2,a3 = map(int,input().split())
    '''
    (1,2) - deviation increases by 3
    (2,1) - deviation decreases by 3
    (1,3) - deviation does not change
    (2,3) - deviation decreases by 3
    '''
    deviation = abs(a1+a3-2*a2)
    print(int(bool(deviation%3)))

