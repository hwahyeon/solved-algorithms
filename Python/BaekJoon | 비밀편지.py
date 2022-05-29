dic = { '000000':'A',
        '001111':'B',
        '010011':'C',
        '011100':'D',
        '100110':'E',
        '101001':'F',
        '110101':'G',
        '111010':'H' }

n = int(input())
s = input()
res = ''
f = 0
for m, i in enumerate(range(0, n*6, 6)):
    w = s[i:i + 6]
    if w in dic:
        res += dic[w]
    else:
        close = 0
        for j in dic.keys():
            cnt = 0
            for k in range(6):
                if j[k] == w[k]:
                    cnt += 1
            if cnt == 5:
                res += dic[j]
                close += 1
        if close == 0:
            f += m+1
            break
print(res) if f == 0 else print(f)
