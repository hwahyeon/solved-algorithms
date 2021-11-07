tup1 = (1,3,5,7)
tup2 = (0,2,4,6)
cnt = 0
for i in range(8):
    str = input()
    if i%2 != 0:
        for j in tup1:
            if 'F' == str[j]:
                cnt += 1
    else:
        for k in tup2:
            if 'F' == str[k]:
                cnt += 1
print(cnt)
