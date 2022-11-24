n, s = map(int, input().split())
l = []
for _ in range(n):
    l.append(int(input()))
for i in l:
    print(int(i/sum(l)*s))
