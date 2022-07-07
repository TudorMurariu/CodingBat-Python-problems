def lucky_sum(a, b, c):
  if a == 13:
    a,b,c = 0,0,0
  elif b == 13:
    b,c = 0,0
  elif c == 13:
    c = 0
  return a+b+c
