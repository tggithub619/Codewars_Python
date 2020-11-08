#https://www.codewars.com/kata/57eae65a4321032ce000002d/train/python

def fake_bin(x):
    res =  ""
    for i in range(len(x)):
        if int(x[i]) >= 5:
            res += '1'
        else:
            res += '0'
    return res