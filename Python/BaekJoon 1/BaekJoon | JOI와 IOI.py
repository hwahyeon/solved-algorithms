s = input()
ioi = 0
for i in range(len(s)-2):
    if s[i:i+3] == 'IOI':
        ioi += 1

print(s.count('JOI'))
print(ioi)
