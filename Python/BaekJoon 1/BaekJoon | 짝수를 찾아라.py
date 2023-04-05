for _ in range(int(input())):
    lst = list(map(int, input().split()))
    min_number = 100
    res = 0
    for i in lst:
        if i % 2 == 0:
            res += i
            if i < min_number:
                min_number = i
    print(res, min_number)
