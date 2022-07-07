def lone_sum(a, b, c):
  if a == b and b == c:
    return 0
  elif a == b:
    a,b = 0,0
  elif b == c:
    b,c = 0,0
  elif a == c:
    a,c = 0,0
  return a+b+c
