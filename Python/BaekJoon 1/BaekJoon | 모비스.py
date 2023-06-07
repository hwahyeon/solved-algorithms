s = str(set(input()))
r = 0
for i in 'MOBIS':
    if i in s:
        r += 1

if r == 5:
    print('YES')
else:
    print('NO')
