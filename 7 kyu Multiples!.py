#https://www.codewars.com/kata/55a8a36703fe4c45ed00005b/train/python

def multiple(x):
    if x % 15 ==0:
        return "BangBoom"
    elif x % 3 ==0:
        return "Bang"
    elif x % 5 ==0:
        return "Boom"
    else :
        return "Miss"