m = 0
for i in range(int(input())):
    s = input()
    m = max(m, s.count('for') + s.count('while'))
print(m)
