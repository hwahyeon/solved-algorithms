a, b, c, d = map(int, input().split())
p, m, n = map(int, input().split())

def count_(v1, v2, v3, v4, s):
    res = 0
    if s%(v1+v2) <= v1 and s%(v1+v2) != 0:
        res += 1
    if s%(v3+v4) <= v3 and s%(v3+v4) != 0:
        res += 1
    return res

print(count_(a, b, c, d, p))
print(count_(a, b, c, d, m))
print(count_(a, b, c, d, n))
