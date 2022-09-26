def in_array(array1, array2):
    res = []
    l1, l2 = len(array1), len(array2)
    for i in range(l1):
        for j in range(l2):
            if array1[i] in array2[j]:
                res.append(array1[i])
    return sorted(list(set(res)))
