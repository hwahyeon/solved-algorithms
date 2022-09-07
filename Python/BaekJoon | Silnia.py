n = int(input())
if n < 10:
    r = 1
    for i in range(1, n+1):
        r *= i
    print(int(str(r)[-1]))
else:
    print(0)
