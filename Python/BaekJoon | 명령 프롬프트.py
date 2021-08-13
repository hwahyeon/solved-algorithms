len_ = int(input())
rst = list(input())
rst_len = len(rst)
for i in range(len_ - 1):
    con = list(input())
    for j in range(rst_len):
        if rst[j] != con[j]:
            rst[j] = '?'
print(''.join(rst))
