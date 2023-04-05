max_num = 0
R = 0
C = 0
for i in range(9):
    lst = list(map(int, input().split()))
    if max(lst) > max_num:
        max_num = max(lst)
        R = i + 1
        C = lst.index(max(lst)) + 1

print(max_num)
print(R, C)
