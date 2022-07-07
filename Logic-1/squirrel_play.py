def squirrel_play(temp, is_summer):
    if is_summer:
        if temp >= 60 and temp <= 100 :
            return True
        else:
            return False
    if temp >= 60 and temp <= 90 :
        return True
    return False
