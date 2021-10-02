a = int(input())
b = int(input())
c = int(input())
tot = str(a*b*c)
for i in range(10):
    print(tot.count(str(i)))
