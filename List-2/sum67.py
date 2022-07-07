def sum67(nums):
    n = len(nums)
    if n == 0:
        return 0
    sum = 0
    ok = 0
    for i in range(n):
        if nums[i] == 6:
            ok = 1
            continue
        elif ok == 1 and nums[i] == 7:
            ok = 0
            continue
        elif ok == 1:
            continue
        sum += nums[i]
    return sum
