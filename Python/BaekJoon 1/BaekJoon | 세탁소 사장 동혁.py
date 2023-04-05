n = int(input())
for i in range(n):
    T = int(input())
    Q = T//25
    T -= 25*Q

    D = T//10
    T -= 10*D

    N = T//5
    T -= 5*N

    print(Q, D, N, T)
