n = int(input())
s = sorted(list(map(int, input().split())))
cluster = int(input())
cnt = 0
for i in s:
    if i > cluster:
        if i%cluster != 0:
            cnt += i//cluster + 1
        else:
            cnt += i//cluster
    elif i == 0:
        cnt += 0
    else:
        cnt += 1

print(cnt*cluster)
