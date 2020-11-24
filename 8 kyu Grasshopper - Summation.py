#https://www.codewars.com/kata/55d24f55d7dd296eb9000030/train/python

def summation(num):
    s = 0
    for i in range(0,num + 1):
        s+= i
    return s


def summation(num):
    return sum(range(1, num + 1))
