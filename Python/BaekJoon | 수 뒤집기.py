for _ in range(int(input())):
    n1 = input()
    n2 = n1[::-1]
    s = str(int(n1) + int(n2))
    print('YES') if s == s[::-1] else print('NO')
