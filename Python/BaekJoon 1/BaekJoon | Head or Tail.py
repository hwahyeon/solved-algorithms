while 1:
    n = int(input())
    if n == 0:
        break
    else:
        c = list(map(int, input().split()))
        print(f'Mary won {c.count(0)} times and John won {c.count(1)} times')
