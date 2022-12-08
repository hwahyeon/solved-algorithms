A, B = map(int, input().split())
r = str(A//B)+'.'
A = (A%B) * 10
for _ in range(1000):
    r += str(A//B)
    A = (A%B) * 10
print(r)
