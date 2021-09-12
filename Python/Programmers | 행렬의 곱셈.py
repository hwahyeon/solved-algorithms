import numpy as np
def solution(arr1, arr2):
    res = np.array(arr1).dot(np.array(arr2))
    return list(res.tolist())
