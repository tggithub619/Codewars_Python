#https://www.codewars.com/kata/564f458b4d75e24fc9000041/train/python

def remainder(dividend, divisor):
    x = dividend // divisor
    return dividend - x * divisor

def remainder(dividend,divisor):
    while divisor <= dividend:
      dividend = dividend - divisor
    return dividend