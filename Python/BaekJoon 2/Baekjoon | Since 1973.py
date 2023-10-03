res = 0
for i in range(int(input())):
    res += 1
    if str(i).find("50") > -1:
        res += 1
print(res)
