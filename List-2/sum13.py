def sum13(nums):
  sum = 0
  i = 0
  n = len(nums)
  while i < n:
    if nums[i] == 13:
      i += 1
    else:
      sum += nums[i]
    i += 1
  return sum
