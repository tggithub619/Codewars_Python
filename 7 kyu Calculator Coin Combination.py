#https://www.codewars.com/kata/564d0490e96393fc5c000029


def coin_combo(c):
    arr = []
    for i in (25, 10, 5, 1):
        arr.append(c//i)
        c = c%i
    return arr[::-1]