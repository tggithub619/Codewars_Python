#https://www.codewars.com/kata/5641c3f809bf31f008000042/train/python

import math


def two_decimal_places(n):
    def truncate(n, decimals=0):
        multiplier = 10 ** decimals
        return int(n * multiplier) / multiplier

    return truncate(n, 2)


def two_decimal_places(number):
    return int(number * 100) / 100.0


import math


def two_decimal_places(number):
    return math.trunc(number * 100.0) / 100.0