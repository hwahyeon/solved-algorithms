s_num = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    s_num.add(i)

self_num = sorted(set(range(1, 10001)) - s_num)
for k in self_num:
    print(k)
