a, b = map(int, input().split())

r = 1
for i in range(a, b+1):
    r *= int(((1+i)*i)/2)
print(r%14579)
