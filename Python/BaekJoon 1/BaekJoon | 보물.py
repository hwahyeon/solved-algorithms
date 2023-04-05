n = input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)
t = 0
for i, j in zip(a, b):
    t += i*j
print(t)
