N = input()
F = int(input())

res = int(N[:-2] + '00')

while 1:
    if res % F == 0 :
        break
    res += 1

print(str(res)[-2:])
