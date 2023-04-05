def addall(n):
    r = n
    while n > 0:
        r += n % 10
        n //= 10
    return r

n = int(input())
s = len(str(n))
m_s = n - s*9

switch = 0

for i in range(m_s, n):
    if addall(i) == n:
        print(i)
        switch = 1
        break
if switch == 0:
    print(0)
