r = 0
for i in range(1, int(input())+1):
    s = sum(map(int, list(str(i))))
    if i % s == 0:
        r += 1
print(r)
