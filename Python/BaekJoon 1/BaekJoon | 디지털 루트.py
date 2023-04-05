def dig_root(n):
    s = sum(list(map(int, n)))
    if s < 10:
        return s
    else:
        return dig_root(str(s))

while 1:
    n = input()
    if n == '0':
        break
    else:
        print(dig_root(n))
