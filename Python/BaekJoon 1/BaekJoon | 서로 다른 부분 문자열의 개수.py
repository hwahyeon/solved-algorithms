s = input()
r = set([s])

for i in range(len(s)):
    for j in range(len(s)):
        r.add(s[j:j+i])

print(len(r)-1) # 공집합 제거
