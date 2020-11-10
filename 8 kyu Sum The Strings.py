#https://www.codewars.com/kata/5966e33c4e686b508700002d/train/python

def sum_str(a, b):
    a = int(a) if a else 0
    b = int(b) if b else 0
    return str(a + b)

def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))