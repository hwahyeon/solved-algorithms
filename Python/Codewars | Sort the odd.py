def sort_array(arr):
    sub = []
    for i in range(len(arr)):
        if arr[i]%2 != 0:
            sub.append(arr[i])
            arr[i] = '*'
    sub.sort()
    k = 0
    for j in range(len(arr)):
        if arr[j] == '*':
            arr[j] = sub[k]
            k += 1
    return arr
