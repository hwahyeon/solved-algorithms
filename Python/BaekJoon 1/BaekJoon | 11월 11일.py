for _ in range(int(input())) :
    y, m = map(int, input().split())
    
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0) :
        f = 29
    else:
        f = 28
    
    d = [31, f, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if m == 1:
        print(y - 1, m + 11, d[m + 10])
    else:
        print(y, m - 1, d[m - 2])
