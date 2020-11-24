#https://www.codewars.com/kata/5eb27d81077a7400171c6820/solutions/python/me/best_practice

import math


def graceful_tipping(bill):
    full = bill + bill * 0.15
    res = 0
    if full < 10:
        res = math.ceil(full)
    elif full < 100:
        res = math.ceil(full / 5) * 5
    elif full < 1000:
        res = math.ceil(full / 50) * 50
    elif full < 10000:
        res = math.ceil(full / 500) * 500
    elif full < 100000:
        res = math.ceil(full / 5000) * 5000
    elif full < 1000000:
        res = math.ceil(full / 50000) * 50000
    elif full < 10000000:
        res = math.ceil(full / 500000) * 500000

    return res