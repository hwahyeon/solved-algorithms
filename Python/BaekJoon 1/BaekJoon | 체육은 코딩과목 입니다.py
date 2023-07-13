x = 1080 

for _ in range(10):
    n = int(input())
    if n == 1:
        x += 90
    elif n == 2:
        x += 180
    elif n == 3:
        x -= 90

x //= 90
x %= 4
    
print(['N', 'E', 'S', 'W'][x])
