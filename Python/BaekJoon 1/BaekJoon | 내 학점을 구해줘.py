for _ in range(int(input())):
    a_r, b_r = 0, 0
    for i in range(int(input())):
        a, b = map(float, input().split())
        a_r += a
        b_r += a*b
    print(int(a_r), round(b_r/a_r, 1))
