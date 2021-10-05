n = int(input())

for i in range(n):
    lst_ = list(map(int, input().split()))[1:]
    aver = (sum(lst_)/len(lst_))
    res = 0
    for j in lst_:
        if j > aver:
            res += 1
    print("{:.3f}%".format(res/len(lst_)*100))
