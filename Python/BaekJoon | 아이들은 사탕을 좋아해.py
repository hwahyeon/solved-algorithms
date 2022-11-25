for _ in range(int(input())):
    N, K = map(int, input().split())
    candy = list(map(int, input().split()))
    r = 0
    for i in candy:
        r += i//K
    print(r)
