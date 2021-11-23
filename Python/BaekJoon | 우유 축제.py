n = int(input())
lst = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if lst[i] == cnt % 3:
        cnt += 1
print(cnt)
