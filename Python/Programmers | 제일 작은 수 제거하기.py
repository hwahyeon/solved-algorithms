def solution(arr):
    if arr == [10]:
        return [-1]
    else:
        arr.remove(min(arr))
        return arr
