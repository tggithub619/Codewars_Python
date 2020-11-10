#https://www.codewars.com/kata/557af9418895e44de7000053/train/python

def repeat_it(string,n):
    return string * n if isinstance(string, str) else "Not a string"