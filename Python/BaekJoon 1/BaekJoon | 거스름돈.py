m = 1000 - int(input())
coin = 0
yen = (1000, 500, 100, 50, 10, 5, 1)
for i in yen:
    if m >= i:
        c = m // i
        coin += c
        m -= c * i
print(coin)
