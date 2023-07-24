def calculate_ans(N, w, d, sum):
    full = N * (N - 1) // 2 * w
    ans = (sum - full) // d
    if not ans:
        return N
    else:
        return abs(ans)

while 1:
    try:
        N, w, d, sum = map(int, input().split())
        print(calculate_ans(N, w, d, sum))
    except EOFError:
        break
