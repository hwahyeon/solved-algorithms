for _ in range(int(input())):
    s, n1, n2 = input().split()
    print(s[:int(n1)]+s[int(n2):])
