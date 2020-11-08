#https://www.codewars.com/kata/57d814e4950d8489720008db/train/python

import math

def index(array, n):
    if len(array) <= n:
        return -1
    else:
        return math.pow(array[n], n)


def index(array, n):
    return array[n]**n if n < len(array) else -1