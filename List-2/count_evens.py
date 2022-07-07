def count_evens(nums):
    nr = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            nr += 1
    return nr
