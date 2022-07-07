def xyz_there(str):
  while str.find('xyz') >= 0:
    x = str.find('xyz') 
    if x == 0:
      return True
    elif x > 0:
      if str[x-1] != '.':
        return True
    str = str.replace('.xyz','')
  return False

# more on https://www.w3schools.com/python/ref_string_find.asp
