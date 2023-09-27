N, K = map(int, input().split())
l = list(map(int, input().split()))
r = []
grade_num = 0
for i in l:
    P = (i*100)//N
    if 0 <= P <= 4:
        grade_num = 1
    elif 4 < P <= 11:
        grade_num = 2
    elif 11 < P <= 23:
        grade_num = 3
    elif 23 < P <= 40:
        grade_num = 4
    elif 40 < P <= 60:
        grade_num = 5
    elif 60 < P <= 77:
        grade_num = 6
    elif 77 < P <= 89:
        grade_num = 7
    elif 89 < P <= 96:
        grade_num = 8
    elif 96 < P <= 100:
        grade_num = 9
    r.append(grade_num)
print(*r)
