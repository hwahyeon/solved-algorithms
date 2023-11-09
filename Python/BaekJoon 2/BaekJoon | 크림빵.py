n, k, p = map(int, input().split())
br = list(map(int, input().split()))

bu = []
tb = (len(br) + k - 1) // k 

for i in range(tb):
    bu.append(br[i * k:(i + 1) * k])

res = n
for b in bu:
    if b.count(0) >= p:
        res -= 1

print(res)
