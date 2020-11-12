#https://www.codewars.com/kata/534ea96ebb17181947000ada/train/python

def breakChocolate(n, m):
    count = 0
    s =  n * m
    if s > 1:
        s = s-1
        count = s
    elif s < 1:
        count = 0
    return count