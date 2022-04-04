import re

R, C = map(int, input().split())
res = [-1]*9

for _ in range(R):
    S = re.split('[1-9]{2}', input())
    if S[0].count('.') != (C - 2):
        res[int(S[1][0])-1] = ((C - 5) - S[0].count('.'))

dict = {}
rank = 1
for num in sorted(res):
    if num not in dict:
        dict[num] = rank
        rank += 1
rank_list = [dict[i] for i in res]

for i in rank_list:
    print(i)
