S1, S2, S3 = map(int, input().split())
lst = [0]*(S1+S2+S3)
for i in range(1, S1+1):
    for j in range(1, S2+1):
        for k in range(1, S3+1):
            lst[i+j+k-1] += 1
print(lst.index(max(lst))+1)
