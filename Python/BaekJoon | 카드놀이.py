A = list(map(int, input().split()))
B = list(map(int, input().split()))
res = []
for i in range(10):
    if A[i] > B[i]:
        res.append('A')
    elif A[i] < B[i]:
        res.append('B')
    else:
        res.append('D')
cnt_A = res.count('A')
cnt_B = res.count('B')
cnt_D = res.count('D')
print(cnt_A * 3 + cnt_D, cnt_B * 3 + cnt_D)
if A == B:
    print('D')
elif cnt_A > cnt_B:
    print('A')
elif cnt_A < cnt_B:
    print('B')
else:
    for j in res[::-1]:
        if j != 'D':
            print(j)
            break
