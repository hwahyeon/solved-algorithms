def find_uniq(arr):
    s = set(arr)
    for i in s:
        if arr.count(i) == 1:
            return i
