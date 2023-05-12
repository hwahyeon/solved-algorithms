n = int(input())
m = int(input())
l1 = [input() for _ in range(n)]
l2 = [input() for _ in range(m)]
for i in l1 :
    for j in l2 :
        print(f'{i} as {j}')
