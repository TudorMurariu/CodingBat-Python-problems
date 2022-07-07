def array_front9(nums):
  n = len(nums)
  i = 0
  while i<n and i<4 :
      if nums[i] == 9 :
          return True
      i += 1
  return False
