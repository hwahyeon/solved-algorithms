import sys

arr = [[0]*101 for _ in range(101)]
for _ in range(4):
    x1, y1, x2, y2 = map(int,sys.stdin.readline().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = 1
print(sum(sum(arr,[])))
