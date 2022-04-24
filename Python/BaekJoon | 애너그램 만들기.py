lst = [0]*26

for i in list(input()):
    lst[ord(i) - 97] += 1
for j in list(input()):
    lst[ord(j) - 97] -= 1

print(sum(map(abs, lst)))

# Add new solution
a = list(input())
b = list(input())
a1, b1 = a[:], b[:]
out1 = [x for x in a if not x in b1 or b1.remove(x)]
out2 = [x for x in b if not x in a1 or a1.remove(x)]
print(len(out1)+len(out2))
