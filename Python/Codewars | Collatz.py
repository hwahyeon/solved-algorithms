def collatz(n):
    if n == 1:
        return '1'
    else:
        res = [n]
        while (n > 2):
            if (n % 2 == 0):
                n /= 2; res.append(n)
            else:
                n = 3 * n + 1; res.append(n)
        res.append(1)
        return '->'.join(list(map(str, list(map(int, res)))))
