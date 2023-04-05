n = int(input())
for i in range(n):
    num, str_ = input().split()
    res_ = ''
    for i in str_:
        res_ += int(num) * i
    print(res_)
