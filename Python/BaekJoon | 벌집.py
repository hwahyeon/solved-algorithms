n = int(input())
t = 1
if n == 1:
    print(1)
else:
    while True:
        n -= t*6
        t += 1
        if n < 2:
            print(t)
            break
