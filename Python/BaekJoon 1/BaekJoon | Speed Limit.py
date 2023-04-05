while 1:
    n = int(input())
    if n == -1:
        break
    else:
        T = 0
        R = 0
        for _ in range(n):
            S, H = map(int, input().split())
            R += (S * (H - T))
            T += (H - T)
        print(f'{R} miles')
