for _ in range(int(input())):
    lst = list(map(int, input().split()))
    lst.sort()
    print(lst[-3])
