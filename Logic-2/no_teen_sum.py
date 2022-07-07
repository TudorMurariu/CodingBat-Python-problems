def no_teen_sum(a, b, c):
    if fix_teen(a) :
        a = 0
    if fix_teen(b) :
        b = 0
    if fix_teen(c) :
        c = 0
    return a + b + c

def fix_teen(n):
    if n == 16 or n == 15 :
        return False
    elif n >= 13 and n <= 19:
        return True
    return False
