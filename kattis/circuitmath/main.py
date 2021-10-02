input()
v = [c=='T' for c in input().strip().split()]
stack = []
for c in input().strip().split():
    print(c)
    if c == '*': tmp = stack.pop() and stack.pop()
    elif c=='+': tmp = stack.pop() or stack.pop()
    elif c=='-': tmp = not stack.pop()
    else: tmp = v[ord(c)-ord('A')]
    stack.append(tmp)
    print(stack)
print("T" if stack[0] else "F")
