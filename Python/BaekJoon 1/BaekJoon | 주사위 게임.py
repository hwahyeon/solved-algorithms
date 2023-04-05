n = int(input())
a_res = 100
b_res = 100
for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        b_res -= a
    elif a < b:
        a_res -= b
    else:
        pass

print(a_res)
print(b_res)
