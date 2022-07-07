def close_far(a, b, c):
    if abs(a-b) > abs(a-c) :
        b = b + c
        c = b - c
        b = b - c

    if abs(a-b) <= 1 and abs(a-c) >= 2 and abs(b-c) >= 2 :
        return True
    return False
