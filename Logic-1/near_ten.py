def near_ten(num):
  if abs(num // 10* 10 - num) <= 2 or abs((num // 10 + 1)* 10 - num) <= 2:
    return True
  return False
