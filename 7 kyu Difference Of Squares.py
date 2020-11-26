#https://www.codewars.com/kata/558f9f51e85b46e9fa000025/train/python

def difference_of_squares(n):
    s = 0
    sSq = 0
    for i in range(1, n+1):
        s += i
        sSq += i**2
    return s**2- sSq