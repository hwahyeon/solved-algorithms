a = input().strip()
b = input().strip()

res = ""

for i in range(len(a)):
    if a[i] > b[i]:
        res += a[i]
    else:
        res += b[i]

print(res)
