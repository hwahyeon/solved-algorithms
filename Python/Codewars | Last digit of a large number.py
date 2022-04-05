def last_digit(n1, n2):
    if n1 == 0 or n2 == 0:
        return 1
    
    lst = [ 0,
            1,
            [2,4,8,6],
            [3,9,7,1],
            [4,6,4,6],
            5,
            6,
            [7,9,3,1],
            [8,4,2,6],
            [9,1,9,1] ]
    
    n1 = int(str(n1)[-1])
    n2 = n2 % 4

    if n1 in [0, 1, 5, 6]:
        return lst[n1]
    else:
        return lst[n1][n2-1]
