def cat_dog(str):
    nrC = 0
    nrD = 0
    for i in range(len(str)-2) :
        if str[i] == 'c' and str[i+1] == 'a' and str[i+2] == 't':
            nrC += 1
        elif str[i] == 'd' and str[i+1] == 'o' and str[i+2] == 'g':
            nrD += 1
    return (nrC == nrD)
