import re

l = []
N, L = map(int, input().split())
for _ in range(N):
    l.append(re.sub(r'1{2,}', '1', input()).count('1'))
print(max(l), l.count(max(l)))
