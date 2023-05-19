n = input()
l = list(map(int, input().split()))
print(min(l.count(0), l.count(1)))
