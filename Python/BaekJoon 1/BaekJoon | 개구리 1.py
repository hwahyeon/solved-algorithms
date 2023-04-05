a, b, c = map(abs, map(int, input().split()))
if (a+b<=c):
    if (a+b)%2 == 0 and c%2 == 0:
        print("YES")
    elif (a+b)%2 == 1 and c%2 == 1:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
