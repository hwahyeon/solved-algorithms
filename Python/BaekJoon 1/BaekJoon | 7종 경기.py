def score(A, B, C, P):
    return int(A * abs(B-P)**C)

for _ in range(int(input())):
    l = list(map(int, input().split()))
    res = score(9.23076,  26.7, 1.835, l[0]) +\
          score(1.84523,  75,   1.348, l[1]) +\
          score(56.0211,  1.5,  1.05,  l[2]) +\
          score(4.99087,  42.5, 1.81,  l[3]) +\
          score(0.188807, 210,  1.41,  l[4]) +\
          score(15.9803,  3.8,  1.04,  l[5]) +\
          score(0.11193,  254,  1.88,  l[6])
    print(res)
