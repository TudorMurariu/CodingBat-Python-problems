def has22(nums):
    n = len(nums)
    for i in range(n-1):
        if nums[i] == 2 and nums[i+1] == 2:
            return True
    return False
