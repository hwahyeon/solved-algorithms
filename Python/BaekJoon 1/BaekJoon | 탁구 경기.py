n = int(input())
D, P = 0, 0
for i in range(n):
    if abs(D - P) < 2:
        if input() == 'D':
            D += 1
        else:
            P += 1
print(f'{D}:{P}')
