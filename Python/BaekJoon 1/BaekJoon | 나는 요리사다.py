S = 0
M = 0
for i in range(5):
    M += 1
    cur_score = sum(list(map(int, input().split())))
    if S < cur_score:
        S = cur_score
        cur_mem = M
print(cur_mem, S)
