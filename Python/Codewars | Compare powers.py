import math
def compare_powers(n1,n2):
    if n1 == n2 or (n1[0] < 2 and n2[0] < 2):
        return 0
    elif n1[0] < 2:
        return 1
    elif n1[1] > n2[1] * math.log(n2[0], n1[0]):
        return -1
    else:
        return 1
