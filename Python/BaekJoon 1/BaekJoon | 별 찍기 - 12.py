n = int(input())
for s, i in enumerate(range(n, 0, -1)):
    print(' '*(i-1)+'*'*(s+1))
for s, i in enumerate(range(n, 0, -1)):
    print(' '*+(s+1)+'*'*(i-1))
