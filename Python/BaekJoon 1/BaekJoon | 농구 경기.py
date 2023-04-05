n = int(input())
player = []
for i in range(n):
    player.append(input()[0])

res = []
ind = set(player)
for j in ind:
    if player.count(j) > 4:
        res.append(j)
res.sort()
if res == []:
    print('PREDAJA')
else:
    print(''.join(res))
