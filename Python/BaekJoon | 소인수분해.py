n = int(input())
lst = []

i = 2
while True:
    if n == 1:
        break
    elif n%i == 0:
        n = n/i
        lst.append(i)
    else:
        i += 1
for l in lst:
    print(l)
