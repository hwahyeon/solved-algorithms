plate = list(str(input()))
res = 0

for i in range(len(plate)):
    if i == 0:
        res += 10
    elif plate[i] == plate[i - 1]:
        res += 5
    else:
        res += 10

print(res)
