def solve(n):
    cnt = 0
    dollars = [10, 20, 50, 100, 200, 500]
    for i in dollars[::-1]:
        cnt += n//i
        n %= i
    return cnt if n == 0 else -1
