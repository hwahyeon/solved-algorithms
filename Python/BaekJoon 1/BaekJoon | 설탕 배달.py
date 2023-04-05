N = int(input())
cnt = 0
while True:
    if N%5 == 0:
        print(N//5+cnt)
        break
    elif N < 0:
        print(-1)
        break
    else:
        N -= 3
        cnt += 1
