#https://www.codewars.com/kata/5592e3bd57b64d00f3000047/train/python

def find_nb(m):
    total = 0
    i = 0
    while (total < m):
        i += 1
        total += (i ** 3)

    return i if total == m else -1