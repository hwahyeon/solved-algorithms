def pro(n):
    r = 1
    for i in str(n):
        r *= int(i)
    r = str(r)
    return r

n = input()
r = 0
while len(n) != 1:
    r += 1
    n = pro(n)

print(r)
