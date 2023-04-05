s = input()
l = len(s)
res = []

for i in range(l-2):
    for j in range(i+1, l-1):
        for k in range(j+1, l):
            res.append(s[:j][::-1] + s[j:k][::-1] + s[k:][::-1])
print(sorted(res)[0])
