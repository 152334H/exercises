def printBorder(length: int, noFirst: bool=False) -> None:
    s = '..' if noFirst else '+-'
    s += '+-' * (length-1)
    s += '+'
    print(s)
def printDots(length: int, noFirst: bool=False) -> None:
    s = '..' if noFirst else '|.'
    s += '|.' * (length-1)
    s += '|'
    print(s)
def printCard(r: int, c: int) -> None:
    '''
    Case #1:
    ..+-+-+-+
    ..|.|.|.|
    +-+-+-+-+
    |.|.|.|.|
    +-+-+-+-+
    |.|.|.|.|
    +-+-+-+-+
    Case #2:
    ..+-+
    ..|.|
    +-+-+
    |.|.|
    +-+-+
    Case #3:
    ..+-+-+
    ..|.|.|
    +-+-+-+
    |.|.|.|
    +-+-+-+
    '''
    printBorder(c, noFirst=True)
    printDots(c, noFirst=True)
    for i in range(r-1):
        printBorder(c)
        printDots(c)
    printBorder(c)
for t in range(int(input())):
    r, c = map(int, input().split())
    print('Case #{}:'.format(t+1))
    printCard(r, c)
