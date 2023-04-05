import re
p = re.compile('[06]')

n = int(input())
s = 0
for _ in range(n):
    r = int(p.sub('9', input()))
    if r >= 100:
        s += 100
    else:
        s += r

def roundUp(n):
    return int(n)+1 if (n - int(n)) >= 0.5 else int(n)

print(roundUp(s / n))
