#https://www.codewars.com/kata/58e0bd6a79716b7fcf0013b1/train/python

def get_ages(sum, d):
    a = (sum + d) / 2
    b = sum - a
    return None if sum < 0 or d < 0 or a < 0 or b < 0 else (max(a,b), min(a,b))