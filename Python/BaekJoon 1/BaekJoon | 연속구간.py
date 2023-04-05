for _ in range(3):
    s = input()
    mx = 1
    c = 1
    for i in range(1, 8):
        if s[i] == s[i-1]:
            c += 1
        else:
            mx = max(c, mx)
            c = 1
    print(max(c, mx))
