a = 0
for i in range(5):
    e = int(input())
    if e >= 40:
        a += e
    else:
        a += 40
print(int(a/5))
