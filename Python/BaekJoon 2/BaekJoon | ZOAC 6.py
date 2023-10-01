r = 0

for _ in range(int(input())):
    s = input()
    if s.count('01') or s.count('OI'):
        r += 1
print(r)
