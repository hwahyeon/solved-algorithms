def max_sub(s):
    r = ""
    for i in range(len(s)):
        if s[i:] > r:
            r = s[i:]
    return r

s = input().strip()
print(max_sub(s))
