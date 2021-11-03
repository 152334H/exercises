t = int(input())
for _ in range(t):
    keyboard = {v:i for i,v in enumerate(input().strip())}
    s = input().strip()
    print(sum(abs(keyboard[s[i]]-keyboard[s[i-1]]) for i in range(1,len(s))))

