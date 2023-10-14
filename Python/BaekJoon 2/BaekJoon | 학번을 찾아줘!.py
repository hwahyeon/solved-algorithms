T = int(input())
scores = list(map(int, input().split()))
korean, math, english, tamgu, foreign = (scores + [0]*5)[:5]

res = 0
if korean > english:
    res += (korean - english) * 508
else:
    res += (english - korean) * 108

if math > tamgu:
    res += (math - tamgu) * 212
else:
    res += (tamgu - math) * 305

if T == 5:
    res += foreign * 707

print(res * 4763)
