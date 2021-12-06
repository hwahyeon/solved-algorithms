b, c = 2000, 2000
for i in range(3):
    b = min(b, int(input()))
for i in range(2):
    c = min(c, int(input()))
print(b + c - 50)
