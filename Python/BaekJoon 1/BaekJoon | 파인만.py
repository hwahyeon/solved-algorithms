while 1:
    n = int(input())
    if n == 0:
        break
    r = 0
    for i in range(n+1):
        r += i**2
    print(r)
