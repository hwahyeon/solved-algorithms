n = int(input())
l1 = [i for i in range(1, n+1)]
l2 = list(map(int, input().split()))
r = 0
for j in range(n):
    if l1[j] != l2[j]:
        r += 1
print(r)
