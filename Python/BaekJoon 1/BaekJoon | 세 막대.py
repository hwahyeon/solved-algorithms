l = sorted(map(int, input().split()))
print(l[0] + l[1] + min(l[0] + l[1] - 1, l[2]))
