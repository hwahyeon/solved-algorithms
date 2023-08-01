from math import pow

pi = 3.14159265359
k = int(input())

for i in range(1, k+1):
    n, w = map(float, input().split())
    t = 0
    for j in range(int(n)):
        radius = float(input())
        t += 4.0 / 3.0 * pi * pow(radius, 3) / 1000
    
    print(f"Data Set {i}:")
    if t >= w:
        print("Yes")
    else:
        print("No")
    print()
