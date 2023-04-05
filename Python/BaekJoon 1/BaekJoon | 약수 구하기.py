N, K = map(int, input().split())
lst=[]
for i in range(1, N+1):
    if N % i == 0:
        lst.append(i)
print(0) if K > len(lst) else print(lst[K-1])
