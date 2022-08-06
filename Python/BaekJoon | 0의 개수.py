for _ in range(int(input())):
    a, b = map(int, input().split())
    r = 0
    for i in range(a, b+1):
        r += str(i).count('0')
    print(r)
