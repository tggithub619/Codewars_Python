#https://www.codewars.com/kata/5b077ebdaf15be5c7f000077/train/python

def count_sheep(n):
    res = ""
    for i in range(1, n+1):
         res +=  str(i) + " sheep..."
    return res