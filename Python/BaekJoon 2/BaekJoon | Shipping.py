n = int(input())

for _ in range(n):
    x = int(input())
    r = 0.0
    for _ in range(x):
        item, qty, price = input().split()
        r += int(qty) * float(price)
    print(f"${r:.2f}")
