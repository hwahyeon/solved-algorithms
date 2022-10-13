def is_sorted_and_how(arr):
    asc = sorted(arr)
    if arr == asc:
        return 'yes, ascending'
    elif arr == asc[::-1]:
        return "yes, descending"
    else:
        return "no"
