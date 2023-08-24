P = int(input())
C = int(input())

score = P * 50 - C * 10

if P > C:
    score += 500

print(score)
