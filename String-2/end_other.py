def end_other(a, b):
    n = len(b)
    m = len(a)
    if m > n :
        return (a[m-n:m].lower() == b.lower())
    return (b[n-m:n].lower() == a.lower())
