#https://www.codewars.com/kata/56606694ec01347ce800001b/train/python

def is_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
