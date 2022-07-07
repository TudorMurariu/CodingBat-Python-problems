def make_bricks(small, big, goal):
    if big * 5 + small < goal:
        return False
    elif (goal % 5 == 0) and (big >= goal//5):
        return True
    elif (big >= goal // 5) and (small >= goal % 5):
        return True
    elif goal - big * 5 <= small and big * 5 <= goal:
        return True
    return False
