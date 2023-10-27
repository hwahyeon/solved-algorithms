p1, y1, s1 = input().split()
p2, y2, s2 = input().split()
p3, y3, s3 = input().split()

ys = sorted([y1[2:], y2[2:], y3[2:]])
print(''.join(ys))

ps = sorted([(int(p1), s1), (int(p2), s2), (int(p3), s3)], key=lambda x: x[0], reverse=True)
ss = ''
for _, s in ps:
    ss += s[0]
print(ss)
