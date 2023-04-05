cnt = 0
cow = [-1]*11
for _ in range(int(input())):
    c, r = map(int, input().split())
    if cow[c] == -1:
        cow[c] = r
    elif cow[c] != r:
        cow[c] = r
        cnt += 1

print(cnt)
