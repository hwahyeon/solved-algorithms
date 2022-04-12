# 시간 초과
import sys

def min_word_finder(res):
    min_word = None
    for word in res:
        if min_word == None or len(word) < len(min_word):
            min_word = word
    return min_word

res = [sys.stdin.readline().strip() for i in range(int(sys.stdin.readline()))]
res = sorted(list(set(res)))

for i in range(len(res)):
    n = res.index(min_word_finder(res[i:]))
    res[i], res[n] = res[n], res[i]

for j in res:
    print(j)

# re
import sys

res = [sys.stdin.readline().strip() for i in range(int(sys.stdin.readline()))]
res = sorted(list(set(res)))
res.sort(key = len)
for i in res:
    print(i)
