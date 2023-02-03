for _ in range(int(input())):
    d, n, s, p = map(int, input().split())
    
    A = d + n*p
    B = n*s
    if A > B:
        print("do not parallelize")
    elif A == B:
        print("does not matter")
    elif A < B:
        print("parallelize")
