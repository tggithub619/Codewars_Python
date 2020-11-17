#https://www.codewars.com/kata/58235a167a8cb37e1a0000db/train/python

def number_of_pairs(gloves):
    dct = {color: gloves.count(color) for color in gloves}
    return sum(count //2 for count in dct.values())