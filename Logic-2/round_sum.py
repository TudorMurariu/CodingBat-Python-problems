

#For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20.
#Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10.
#Given 3 ints, a b c, return the sum of their rounded values. 
#To avoid code repetition, write a separate helper "def round10(num):" 
# and call it 3 times. Write the helper entirely below and at the same indent level as round_sum().

#round_sum(16, 17, 18) → 60
#round_sum(12, 13, 14) → 30
#round_sum(6, 4, 4) → 10

# code:
def round_sum(a, b, c):
  if a%10 >= 5:
    a += (10 - a%10)
  else:
    a -= a%10 
    
  if b%10 >= 5:
    b += (10 - b%10)
  else:
    b -= b%10 
    
  if c%10 >= 5:
    c += (10 - c%10)
  else:
    c -= c%10 
    
  return a+b+c
