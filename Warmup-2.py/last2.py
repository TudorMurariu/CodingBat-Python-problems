def last2(str):
    if len(str) <= 2:
        return 0
    l2 = str[len(str)-2:]
    nr = 0
    for i in range(len(str)-2):
        sub = str[i:i+2]
        if l2 == sub:
            nr += 1
    return nr

