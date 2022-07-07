def count_code(str):
    nr = 0
    for i in range(len(str)-3):
        if str[i:i+2] == "co" and str[i+3] == 'e' :
            nr += 1
    return nr
