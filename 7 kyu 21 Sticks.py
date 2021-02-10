#https://www.codewars.com/kata/5866a58b9cbc02c4f8000cac

def make_move(sticks):
    return sticks % 4 if sticks % 4 != 0 else 1


def make_move(sticks):
    if sticks < 4:
        return sticks
    else:
        if sticks % 4 == 0:
            return 1
        return sticks % 4
