# timeout
a, b = map(int, input().split())

def todec(num):
    res = 0
    num = str(num)
    for n, i in enumerate(num[::-1]):
        res += (2**n)*int(i)
    return res

c = todec(a)+todec(b)

def tobin(num):
    res = ''
    while num != 1:
        res += str(num % 2)
        num = num//2
    t = '1'+res[::-1]
    return int(t)

print(tobin(c))



#
a, b = map(str, input().split())
a, b = int(a, 2), int(b, 2)
print(bin(a+b)[2:])
