H, M = map(int, input().split())
time = int(input())

res = H * 60 + M + time
H = res//60
if H >= 24:
    print((res//60)-24, res%60)
else:
    print(res // 60, res % 60)
