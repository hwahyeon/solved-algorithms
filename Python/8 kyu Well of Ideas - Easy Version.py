def well(x):
    n = x.count('good')
    return 'Fail!' if n == 0 else('Publish!' if n == 1 or n ==2 else 'I smell a series!')
