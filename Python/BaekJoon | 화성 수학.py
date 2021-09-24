n = int(input())

for i in range(n):
    lst_ = list(input().split())
    lst_[0] = float(lst_[0])
    for i in lst_[1:]:
        if i == '@':
            lst_[0] *= 3
        elif i == '%':
            lst_[0] += 5
        else:
            lst_[0] -= 7
    print(f'{lst_[0]:.2f}')
