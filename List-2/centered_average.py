def centered_average(nums):
    n = len(nums)
    sum = 0
    mini = nums[0]
    maxi = nums[0]
    for i in range(n):
        sum += nums[i]
        if mini > nums[i]:
            mini = nums[i]
        if maxi < nums[i]:
            maxi = nums[i]
    return (sum - mini - maxi) // (n-2)
