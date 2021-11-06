lst = []
for i in range(10):
    lst.append(int(input()))

res = 0
for n, j in enumerate(lst):
    res += j
    if res == 100:
        print(100)
        break
    elif res > 100:
        res2 = res - lst[n]
        if abs(100-res) <= abs(100-res2):
            print(res)
            break
        else:
            print(res2)
            break
if res < 100:
    print(res)
