q, r = [], []
for _ in range(8):
    q.append(int(input()))
s = sorted(q)[-5:]
print(sum(s))
for i in s:
    r.append(q.index(i)+1)
r.sort()
r = map(str, r)
print(' '.join(r))
