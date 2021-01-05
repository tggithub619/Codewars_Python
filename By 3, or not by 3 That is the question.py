#https://www.codewars.com/kata/59f7fc109f0e86d705000043

def divisible_by_three(st):
    s = 0
    for i in st:
        s+= int(i)
    while s >0 :
        s-=3
    return True if s==0 else False