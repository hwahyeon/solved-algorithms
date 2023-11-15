a, d, k = map(int, input().split())
m = k-a
if m%d == 0 and m//d >= 0:
    print(m//d + 1)
else:
    print('X')
