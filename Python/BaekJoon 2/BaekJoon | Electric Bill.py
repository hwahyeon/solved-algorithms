rk, r = map(int, input().split())

for _ in range(int(input())):
    consum = int(input())
    if consum <= 1000:
        charges = consum * rk
    else:
        charges = 1000 * rk + (consum - 1000) * r
    print(consum, charges)
