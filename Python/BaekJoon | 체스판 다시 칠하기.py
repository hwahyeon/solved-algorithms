n, m = map(int, input().split())
board = []
res = []

for _ in range(n):
    board.append(input())

for i in range(n - 7):
    for j in range(m - 7):
        re1 = 0
        re2 = 0
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if board[a][b] != 'B':
                        re1 += 1
                    if board[a][b] != 'W':
                        re2 += 1
                else:
                    if board[a][b] != 'W':
                        re1 += 1
                    if board[a][b] != 'B':
                        re2 += 1
        res.append(re1)
        res.append(re2)
        
print(min(res))
