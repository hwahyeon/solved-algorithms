n = int(input())
c = 0
for _ in range(n):
    s = input().split('.')
    if len(s) != 2 or s[0] == '' or s[-1] == '':
        c += 1
    elif len(s[-1]) > 3:
        c += 1
    elif len(s[0]) > 8:
        c += 1
print(n-c)
