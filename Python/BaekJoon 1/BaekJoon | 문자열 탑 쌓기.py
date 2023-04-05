def comp(s1, s2):
    n = len(s1)
    for i in range(n):
        if s1[:n - i] == s2[i:] or s2[:n - i] == s1[i:]:
            return True
    return False

n, s = map(int, input().split())

floor = input()
ON = True
for _ in range(n-1):
    si = input()
    if comp(si, floor):
        floor = si
    else:
        ON = False

print(1) if ON else print(0)
