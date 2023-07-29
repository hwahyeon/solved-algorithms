r = 5000
for n in map(int, input().split()):
    if n == 1:
        r -= 500
    elif n == 2:
        r -= 800
    elif n == 3:
        r -= 1000
print(r)
