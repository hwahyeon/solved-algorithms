res = int(input())
while 1:
    o = input()
    if o == '=':
        break
    n = int(input())
    if o == '+':
        res += n
    elif o == '-':
        res -= n
    elif o == '*':
        res *= n
    else:
        res //= n

print(res)
