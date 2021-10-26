def incrementer(nums):
    for n, i in enumerate(nums):
        nums[n] = int(str(i+n+1)[-1])
    return nums
