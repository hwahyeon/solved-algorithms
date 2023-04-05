num = int(input())
for i in reversed(range(1, num+1)):
    print((i*'*').rjust(num))
