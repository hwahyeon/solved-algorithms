n = int(input())

for _ in range(n):
    y, m, d = map(int, input().split())

    if y < 1989:
        print("Yes")
    elif y == 1989:
        if m < 2:
            print("Yes")
        elif m == 2 and d <= 27:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
