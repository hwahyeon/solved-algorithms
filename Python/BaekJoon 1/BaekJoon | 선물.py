N, X = map(int, input().split())
sock = list(map(int, input().split()))
p1 = (sock[0] + sock[1]) * X

for i in range(1, N - 2):
    p2 = ((sock[i] + sock[i + 1]) * X)
    if p1 > p2:
        p1 = p2

print(p1)
