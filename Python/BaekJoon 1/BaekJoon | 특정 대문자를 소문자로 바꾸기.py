s = input()
l = input().split()
for i in l:
    s = s.replace(i, i.lower())
print(s)
