#https://www.codewars.com/kata/56efc695740d30f963000557/train/python

def to_alternating_case(str):
    res = ""
    for i, el in enumerate(str):
        if  el.islower():
             res += el.upper()
        else :
             res += el.lower()
    return res

def to_alternating_case(string):
    return string.swapcase()