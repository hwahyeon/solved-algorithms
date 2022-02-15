n = input()
lennum = len(n)
tot = 0
for i in range(0, lennum):
    tot += 9 * (10 ** i) * (i + 1)
tot += (int(n) - (10 ** lennum) + 1) * lennum
print(tot)
