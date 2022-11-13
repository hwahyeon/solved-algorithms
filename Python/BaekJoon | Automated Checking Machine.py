X = list(map(int, input().split()))
Y = list(map(int, input().split()))
C = 0
for i in range(5):
    if X[i] + Y[i] == 1:
        C += 1
print('Y' if C == 5 else 'N')
