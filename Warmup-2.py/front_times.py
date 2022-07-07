def front_times(str, n):
    l = len(str)
    if l < 3 :
        return str * n
    result = str[:3]

    return result * n


