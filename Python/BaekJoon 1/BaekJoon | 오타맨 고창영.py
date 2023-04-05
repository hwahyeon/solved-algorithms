for _ in range(int(input())):
    i, s = input().split()
    i = int(i)
    print(s[:i-1] + s[i:])
