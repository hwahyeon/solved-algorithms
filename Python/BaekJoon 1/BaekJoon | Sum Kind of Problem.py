for _ in range(int(input())):
    i, n = map(int, input().split())
    r1 = int(n*(n+1)/2)
    r2 = n ** 2
    r3 = r2 + n
    
    print(i, r1, r2, r3)
