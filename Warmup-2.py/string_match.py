def string_match(a, b):
    n = len(a)
    m = len(b)
    i = 0
    nr = 0
    while i < n-1 and i < m-1:
        if a[i] == b[i] and a[i+1] == b[i+1]:
            nr += 1
        i += 1
    return nr
