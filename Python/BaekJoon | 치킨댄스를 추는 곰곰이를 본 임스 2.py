c = 0
for _ in range(int(input())):
    e, d = input().split('-')
    if int(d) <= 90:
        c += 1
print(c)
