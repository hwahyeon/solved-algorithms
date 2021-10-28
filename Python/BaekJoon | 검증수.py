lst_ = list(map(int, input().split()))
res = 0
for i in lst_:
    res += i**2
print(res%10)
