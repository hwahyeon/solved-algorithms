A, B = input().split()

r = [''] * len(B)

for i in range(len(A)):
    if A[i] in B:
        break

for k in range(len(B)):
    r[k] = '.' * i + B[k] + '.' * (len(A)-i-1)
r[B.find(A[i])] = A

print('\n'.join(r))
