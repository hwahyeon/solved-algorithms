num = int(input())
for j in range(num):
    Y, K = 0, 0
    for i in range(9):
        a, b = map(int, input().split())
        Y += a
        K += b
    if Y > K:
        print('Yonsei')
    elif Y == K:
        print('Draw')
    else:
        print('Korea')
