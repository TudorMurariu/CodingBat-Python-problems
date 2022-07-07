def string_splosion(str):
    n = len(str)
    str2 = ""
    for i in range(n) :
        str2 = str2 + str[:i+1]
    return str2
