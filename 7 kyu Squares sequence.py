#https://www.codewars.com/kata/5546180ca783b6d2d5000062/train/python

def squares(x, n):
    arr = []
    for i in range(n):
        arr.append(x)
        x = x*x
    return arr

def squares(x, n):
    return [x**2**(i) for i in range(n)]
