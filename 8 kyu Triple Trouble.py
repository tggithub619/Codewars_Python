#https://www.codewars.com/kata/5704aea738428f4d30000914/train/python

def triple_trouble(one, two, three):
    str = ""
    for i in range(len(one)):
        str += one[i] + two[i] + three[i]
    return str
