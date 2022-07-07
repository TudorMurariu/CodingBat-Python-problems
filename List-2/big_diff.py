def big_diff(nums):
    mini = nums[0]
    maxi = nums[0]
    for i in range(len(nums)):
        if nums[i] > maxi:
            maxi = nums[i]
        elif nums[i] < mini:
            mini = nums[i]
    return maxi-mini
