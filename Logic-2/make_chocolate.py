def make_chocolate(small, big, goal):
  neededBig = goal / 5  
  neededSmal = goal % 5
  if big < neededBig:
    neededBig -= big
    if neededBig*5 + neededSmal > small:
      return -1
    return neededBig*5 + neededSmal
  elif neededSmal > small:
    return -1
  return neededSmal
