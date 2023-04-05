n = int(input())
i = 0
sum = 0
while True:
    i += 1
    sum += i
    if sum > n:
        print(i-1)
        break
