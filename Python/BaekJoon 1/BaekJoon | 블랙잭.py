N, M = map(int, input().split())
arr = list(map(int, input().split()))
res = 0
for i in range(N):
   for j in range(i+1, N):
       for k in range(j+1, N):
           if arr[i] + arr[j] + arr[k] > M:
               continue
           else:
               res = max(res, arr[i]+arr[j]+arr[k])
print(res)
