l = list(map(int, input().split()))
m = [100, 100, 200, 200, 300, 300, 400, 400, 500]
r = False
for i in range(9):
    if l[i] > m[i]:
        r = True

if r:
    print('hacker')
elif sum(l) >= 100:
    print('draw')
else:
    print('none')
