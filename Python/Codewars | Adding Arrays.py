def arr_adder(arr):
    n = len(arr[0])
    t = len(arr)
    r = [''] * n
    for i in range(n):
        for j in range(t):
            r[i] += (arr[j][i])

    return ' '.join(r).rstrip()
