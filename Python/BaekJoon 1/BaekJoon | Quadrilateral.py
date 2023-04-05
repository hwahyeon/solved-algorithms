r = ''
for _ in range(int(input())):
    w, h = map(int, input().split())
    for i in range(h):
        r += 'X'*w
        r += '\n'
    r += '\n'
print(r[:-1])
