def partition(arr, classifier_method):
    a, b = [], []
    for i in arr:
        if classifier_method(i):
            a.append(i)
        else:
            b.append(i)
    return (a, b)
