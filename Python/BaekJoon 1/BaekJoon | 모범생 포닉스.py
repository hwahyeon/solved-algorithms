n = int(input())
l = map(int, input().split())
r = sum(l) + (n - 1) * 8
print(r//24, r%24)
