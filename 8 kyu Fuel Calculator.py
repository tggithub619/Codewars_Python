#https://www.codewars.com/kata/57b58827d2a31c57720012e8/train/python

def fuel_price(l, pl):
    for i in range(2, 11, 2):
        if(i<= l ):
            pl -= 0.05
    return round(l*pl, 2)

def fuel_price(l, pl):
    return round(l*(pl-min(0.05*(l//2), 0.25)), 2)