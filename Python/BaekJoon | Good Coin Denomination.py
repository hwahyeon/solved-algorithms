res = ''
for _ in range(int(input())):
    l = list(map(int, input().split()))[1:]
    t = True
    for i in range(len(l)-1):
        if not (l[i]*2 <= l[i+1]):
            t = False
    r = ' '.join(map(str, l))
    res += f'Denominations: {r}'
    res += '\n'
    if t:
        res += 'Good coin denominations!'
        res += '\n'
    else:
        res += 'Bad coin denominations!'
        res += '\n'
    res += '\n'
print(res[:-1])
