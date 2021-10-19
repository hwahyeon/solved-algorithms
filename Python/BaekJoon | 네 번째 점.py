lst_x = []
lst_y = []
for i in range(3):
        x, y = map(int, input().split())
        lst_x.append(x)
        lst_y.append(y)
for i in range(3):
        if lst_x.count(lst_x[i]) == 1:
                a = lst_x[i]
        if lst_y.count(lst_y[i]) == 1:
                b = lst_y[i]
print(a, b)
