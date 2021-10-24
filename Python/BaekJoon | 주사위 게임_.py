n = int(input())
dice = []
for i in range(n):
    a, b, c = map(int, input().split())
    if a == b == c:
        dice.append(10000 + (a*1000))
    elif a == b or b == c:
        dice.append(1000 + (b * 100))
    elif a == c:
        dice.append(1000 + (a * 100))
    else:
        dice.append(max(a, b, c)*100)

print(max(dice))
