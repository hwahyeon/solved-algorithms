y = input()
y0, y1, y2, y3 = y.count('L'), y.count('O'), y.count('V'), y.count('E')
n = int(input())
name_list = [input() for i in range(n)]
pro = 0
res = []
for i in name_list:
    s0 = i.count('L') + y0
    s1 = i.count('O') + y1
    s2 = i.count('V') + y2
    s3 = i.count('E') + y3
    score = ((s0+s1)*(s0+s2)*(s0+s3)*(s1+s2)*(s1+s3)*(s2+s3))%100
    res.append(score)

print(min([name_list[j] for j, v in enumerate(res) if v == max(res)]))
