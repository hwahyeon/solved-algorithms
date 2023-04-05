n = input()
lst = list(map(int, input().split()))
cnt = 0

for num in lst:
    res = 0
    if num > 1 :
        for i in range(2, num):
            if num % i == 0:
                res += 1
        if res == 0:
            cnt += 1
print(cnt)
