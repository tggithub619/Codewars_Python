#https://www.codewars.com/kata/56269eb78ad2e4ced1000013/train/python

import math

def find_next_square(sq):
    num = math.sqrt(sq)
    if num % 1 == 0:
        res = num + 1
        return res * res
    return -1

def find_next_square(sq):
    x = sq**0.5
    return -1 if x % 1 else (x+1)**2