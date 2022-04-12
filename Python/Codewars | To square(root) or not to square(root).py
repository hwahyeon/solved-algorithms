def square_or_square_root(arr):
    for n, i in enumerate(arr):
        if (i**0.5) == int(i**0.5):
            arr[n] = (i**0.5)
        else:
            arr[n] = i**2
    return arr
