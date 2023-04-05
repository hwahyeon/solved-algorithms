n = int(input())
res = 0
for i in range(1, n+1):
    s = str(i)
    res += s.count('3')
    res += s.count('6')
    res += s.count('9')

print(res)
